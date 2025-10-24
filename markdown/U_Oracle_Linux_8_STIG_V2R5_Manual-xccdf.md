# STIG Benchmark: Oracle Linux 8 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248519`

### Rule: The OL 8 audit package must be installed.

**Rule ID:** `SV-248519r1015024_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred and their source, location, and outcome, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in OL 8 audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured OL 8 system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000062-GPOS-00031, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit service is configured to produce audit records. Check that the audit service is installed with the following command: $ sudo yum list installed audit If the "auditd" package is not installed, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248520`

### Rule: OL 8 audit records must contain information to establish what type of events occurred, the source of events, where events occurred, and the outcome of events.

**Rule ID:** `SV-248520r1015025_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred and their source, location, and outcome, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in OL 8 audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured OL 8 system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000062-GPOS-00031, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit service is configured to produce audit records with the following command: $ sudo systemctl status auditd.service auditd.service - Security Auditing Service Loaded:loaded (/usr/lib/systemd/system/auditd.service; enabled; vendor preset: enabled) Active: active (running) since Tues 2020-12-11 12:56:56 EST; 4 weeks 0 days ago If the audit service is not "active" and "running", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248521`

### Rule: OL 8 must be a vendor-supported release.

**Rule ID:** `SV-248521r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists verifies compliance with federal standards and establishes a common security baseline across the DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example, registry settings; account, file, and directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the version of the operating system is vendor supported. Check the version of the operating system with the following command: $ udo cat /etc/oracle-release Oracle Linux Server release 8.2 Current End of Premier Support for Oracle Linux 8 is July 2029, while Extended Support might consider an extended term. If the release is not supported by the vendor, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248523`

### Rule: OL 8 vendor-packaged system security patches and updates must be installed and up to date.

**Rule ID:** `SV-248523r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Timely patching is critical for maintaining the operational availability, confidentiality, and integrity of information technology (IT) systems. However, failure to keep operating system and application software patched is a common mistake made by IT professionals. New patches are released daily, and it is often difficult for even experienced System Administrators to keep abreast of all the new patches. When new weaknesses in an operating system exist, patches are usually made available by the vendor to resolve the problems. If the most recent security patches and updates are not installed, unauthorized users may take advantage of weaknesses in the unpatched software. The lack of prompt attention to patching could result in a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system security patches and updates are installed and up to date. Updates are required to be applied with a frequency determined by the site or Program Management Office (PMO). Obtain the list of available package security updates from Oracle. The URL for updates is https://linux.oracle.com/errata/. It is important to note that updates provided by Oracle may not be present on the system if the underlying packages are not installed. Check that the available package security updates have been installed on the system with the following command: $ sudo yum history list | more Loaded plugins: langpacks, product-id, subscription-manager ID | Command line | Date and time | Action(s) | Altered ------------------------------------------------------------------------------- 70 | install aide | 2020-03-05 10:58 | Install | 1 69 | update -y | 2020-03-04 14:34 | Update | 18 EE 68 | install vlc | 2020-02-21 17:12 | Install | 21 67 | update -y | 2020-02-21 17:04 | Update | 7 EE If package updates have not been performed on the system within the timeframe that the site/program documentation requires, this is a finding. Typical update frequency may be overridden by Information Assurance Vulnerability Alert (IAVA) notifications from CYBERCOM. If the operating system is not in compliance with the Information Assurance Vulnerability Management (IAVM) process, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-248524`

### Rule: OL 8 must implement NIST FIPS-validated cryptography for the following: To provision digital signatures, to generate cryptographic hashes, and to protect data requiring data-at-rest protections in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-248524r1069154_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. OL 8 uses GRUB 2 as the default bootloader. Note that GRUB 2 command-line parameters are defined in the "kernelopts" variable of the "/boot/grub2/grubenv" file for all kernel boot entries. The command "fips-mode-setup" modifies the "kernelopts" variable, which in turn updates all kernel boot entries. The fips=1 kernel option needs to be added to the kernel command line during system installation so that key generation is done with FIPS-approved algorithms and continuous monitoring tests in place. Users must also ensure the system has plenty of entropy during the installation process by moving the mouse around, or if no mouse is available, ensuring that many keystrokes are typed. The recommended amount of keystrokes is 256 and more. Less than 256 keystrokes may generate a nonunique key. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000423-GPOS-00187</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system implements DOD-approved encryption to protect the confidentiality of remote access sessions. Check to see if FIPS mode is enabled with the following command: $ fips-mode-setup --check FIPS mode is enabled If FIPS mode is "enabled", check if the kernel boot parameter is configured for FIPS mode with the following command: $ sudo grub2-editenv list | grep fips kernelopts=...fips=1 If the kernel boot parameter is configured to use FIPS mode, check to see if the system is in FIPS mode with the following command: $ sudo cat /proc/sys/crypto/fips_enabled 1 If FIPS mode is not "enabled", the kernel boot parameter is not configured for FIPS mode, or the system does not have a value of "1" for "fips_enabled" in "/proc/sys/crypto", this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-248525`

### Rule: All OL 8 local disk partitions must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at-rest protection.

**Rule ID:** `SV-248525r1016496_rule`
**Severity:** high

**Description:**
<VulnDiscussion>OL 8 systems handling data requiring "data-at-rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption. If there is a documented and approved reason for not having data-at-rest encryption at the operating system level, such as encryption provided by a hypervisor or a disk storage array in a virtualized environment, this requirement is not applicable. Verify all system partitions are encrypted with the following command: $ sudo blkid /dev/mapper/ol-root: UUID="67b7d7fe-de60-6fd0-befb-e6748cf97743" TYPE="crypto_LUKS" Every persistent disk partition present must be of type "crypto_LUKS". If any partitions other than the boot partition or pseudo file systems (such as "/proc" or "/sys") are not listed, ask the administrator to indicate how the partitions are encrypted. If there is no evidence that these partitions are encrypted, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-248526`

### Rule: OL 8 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via an SSH logon.

**Rule ID:** `SV-248526r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that any publicly accessible connection to the operating system displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system. Check for the location of the banner file being used with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*banner' banner /etc/issue This command will return the banner keyword and the name of the file that contains the SSH banner (in this case "/etc/issue"). If the line is commented out, this is a finding. If conflicting results are returned, this is a finding. View the file specified by the banner keyword to check that it matches the text of the Standard Mandatory DOD Notice and Consent Banner: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the system does not display a graphical logon banner or the banner does not match the Standard Mandatory DOD Notice and Consent Banner, this is a finding. If the text in the file does not match the Standard Mandatory DOD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-248527`

### Rule: OL 8 must display a banner before granting local or remote access to the system via a graphical user logon.

**Rule ID:** `SV-248527r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify OL 8 displays a banner before granting access to the operating system via a graphical user logon. Determine if the operating system displays a banner at the logon screen with the following command: $ sudo grep banner-message-enable /etc/dconf/db/local.d/* banner-message-enable=true If "banner-message-enable" is set to "false" or is missing, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-248528`

### Rule: OL 8 must display the Standard Mandatory DoD Notice and Consent Banner before granting local or remote access to the system via a graphical user logon.

**Rule ID:** `SV-248528r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify OL 8 displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the operating system via a graphical user logon. Check that the operating system displays the exact Standard Mandatory DoD Notice and Consent Banner text with the command: $ sudo grep banner-message-text /etc/dconf/db/local.d/* banner-message-text= 'You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.\nBy using this IS (which includes any device attached to this IS), you consent to the following conditions:\n-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.\n-At any time, the USG may inspect and seize data stored on this IS.\n-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.\n-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. ' Note: The "\n" characters are for formatting only. They will not be displayed on the graphical interface. If the banner does not match the Standard Mandatory DoD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-248529`

### Rule: OL 8 must display the Standard Mandatory DoD Notice and Consent Banner before granting local or remote access to the system via a command line user logon.

**Rule ID:** `SV-248529r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the operating system via a command line user logon. Check that OL 8 displays a banner at the command line login screen with the following command: $ sudo cat /etc/issue If the banner is set correctly, it will return the following text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the banner text does not match the Standard Mandatory DoD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-248530`

### Rule: All OL 8 remote access methods must be monitored.

**Rule ID:** `SV-248530r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 monitors all remote access methods. Check that remote access methods are being logged by running the following command: $ sudo grep -E '(auth\.\*|authpriv\.\*|daemon\.\*)' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:auth.*;authpriv.*;daemon.* /var/log/secure If "auth.*", "authpriv.*", or "daemon.*" are not configured to be logged, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-248531`

### Rule: OL 8, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-248531r1015027_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, the relying party cannot make an informed trust decision when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000384-GPOS-00167</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8, for PKI-based authentication, has valid certificates by constructing a certification path (which includes status information) to an accepted trust anchor. Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is Not Applicable. Check that the system has a valid DOD root CA installed with the following command: $ sudo openssl x509 -text -in /etc/sssd/pki/sssd_auth_ca_db.pem Certificate: Data: Version: 3 (0x2) Serial Number: 1 (0x1) Signature Algorithm: sha256WithRSAEncryption Issuer: C = US, O = U.S. Government, OU = DoD, OU = PKI, CN = DoD Root CA 3 Validity Not Before: Mar 20 18:46:41 2012 GMT Not After : Dec 30 18:46:41 2029 GMT Subject: C = US, O = U.S. Government, OU = DoD, OU = PKI, CN = DoD Root CA 3 Subject Public Key Info: Public Key Algorithm: rsaEncryption If the root ca file is not a DOD-issued certificate with a valid date installed in the "/etc/sssd/pki/sssd_auth_ca_db.pem" location, this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-248532`

### Rule: OL 8, for certificate-based authentication, must enforce authorized access to the corresponding private key.

**Rule ID:** `SV-248532r958450_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains access to a private key without a passcode, that user would have unauthorized access to any system where the associated public key has been installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH private key files have a passcode. For each private key stored on the system, use the following command: $ sudo ssh-keygen -y -f /path/to/file If the contents of the key are displayed, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-248533`

### Rule: OL 8 must encrypt all stored passwords with a FIPS 140-2 approved cryptographic hashing algorithm.

**Rule ID:** `SV-248533r1015028_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DOD data may be compromised. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DOD requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the shadow password suite configuration is set to encrypt passwords with a FIPS 140-2 approved cryptographic hashing algorithm. Check the hashing algorithm that is being used to hash passwords with the following command: $ sudo cat /etc/login.defs | grep -i crypt ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" does not equal SHA512 or greater, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-248534`

### Rule: OL 8 must employ FIPS 140-2 approved cryptographic hashing algorithms for all stored passwords.

**Rule ID:** `SV-248534r1015029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system must use a strong hashing algorithm to store the password. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm that the interactive user account passwords are using a strong password hash with the following command: $ sudo cut -d: -f2 /etc/shadow $6$kcOnRq/5$NUEYPuyL.wghQwWssXRcLRFiiru7f5JPV6GaJhNC2aK5F3PZpE/BCCtwrxRc/AInKMNX3CdMw11m9STiql12f/ Password hashes "!" or "*" indicate inactive accounts not available for logon and are not evaluated. If any interactive user password hash does not begin with "$6$", this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-248535`

### Rule: The OL 8 shadow password suite must be configured to use a sufficient number of hashing rounds.

**Rule ID:** `SV-248535r1044786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system must use a strong hashing algorithm to store the password. The system must use a sufficient number of hashing rounds to ensure the required level of entropy. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that a minimum number of hash rounds is configured by running the following command: $ sudo grep -E "^SHA_CRYPT_" /etc/login.defs If only one of "SHA_CRYPT_MIN_ROUNDS" or "SHA_CRYPT_MAX_ROUNDS" is set, and this value is below "100000", this is a finding. If both "SHA_CRYPT_MIN_ROUNDS" and "SHA_CRYPT_MAX_ROUNDS" are set, and the value for either is below "100000", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-248537`

### Rule: OL 8 operating systems booted with United Extensible Firmware Interface (UEFI) must require authentication upon booting into single-user mode and maintenance.

**Rule ID:** `SV-248537r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the system does not require valid authentication before it boots into single-user or maintenance mode, anyone who invokes single-user or maintenance mode is granted privileged access to all files on the system. GRUB 2 is the default boot loader for OL 8 and is designed to require a password to boot into single-user mode or modify the boot menu.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that use BIOS, this is not applicable. Determine if an encrypted password is set for the grub superusers account. On systems that use UEFI, use the following command: $ sudo grep -iw grub2_password /boot/efi/EFI/redhat/user.cfg GRUB2_PASSWORD=grub.pbkdf2.sha512.[password_hash] If the grub superusers account password does not begin with "grub.pbkdf2.sha512", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-248538`

### Rule: OL 8 operating systems booted with United Extensible Firmware Interface (UEFI) must have a unique name for the grub superusers account when booting into single-user mode and maintenance.

**Rule ID:** `SV-248538r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system does not require valid authentication before it boots into single-user or maintenance mode, anyone who invokes single-user or maintenance mode is granted privileged access to all files on the system. GRUB 2 is the default boot loader for OL 8 and is designed to require a password to boot into single-user mode or modify the boot menu. The GRUB 2 superuser account is an account of last resort. Establishing a unique username for this account hardens the boot loader against brute force attacks. Due to the nature of the superuser account database being distinct from the OS account database, this allows the use of a username that is not among those within the OS account database. Examples of non-unique superusers names are (root, superuser, unlock, etc.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that use BIOS, this is Not Applicable. Verify that a unique name is set as the "superusers" account: $ sudo grep -iw "superusers" /boot/efi/EFI/redhat/grub.cfg set superusers="[someuniqueUserNamehere]" export superusers If "superusers" is identical to any OS account name or is missing a name, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-248539`

### Rule: OL 8 operating systems booted with a BIOS must have a unique name for the grub superusers account when booting into single-user and maintenance modes.

**Rule ID:** `SV-248539r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system does not require valid authentication before it boots into single-user or maintenance mode, anyone who invokes single-user or maintenance mode is granted privileged access to all files on the system. GRUB 2 is the default boot loader for OL 8 and is designed to require a password to boot into single-user mode or modify the boot menu. The GRUB 2 superuser account is an account of last resort. Establishing a unique username for this account hardens the boot loader against brute force attacks. Due to the nature of the superuser account database being distinct from the OS account database, this allows the use of a username that is not among those within the OS account database. Examples of non-unique superusers names are (root, superuser, unlock, etc.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that use UEFI, this is Not Applicable. Verify that a unique name is set as the "superusers" account: $ sudo grep -iw "superusers" /boot/grub2/grub.cfg set superusers="[someuniqueUserNamehere]" export superusers If "superusers" is identical to any OS account name or is missing a name, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-248540`

### Rule: OL 8 operating systems booted with a BIOS must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-248540r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the system does not require valid authentication before it boots into single-user or maintenance mode, anyone who invokes single-user or maintenance mode is granted privileged access to all files on the system. GRUB 2 is the default boot loader for OL 8 and is designed to require a password to boot into single-user mode or modify the boot menu.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that use UEFI, this is not applicable. Determine if an encrypted password is set for the grub superusers account. On systems that use a BIOS, use the following command: $ sudo grep -iw grub2_password /boot/grub2/user.cfg GRUB2_PASSWORD=grub.pbkdf2.sha512.[password_hash] If the grub superusers account password does not begin with "grub.pbkdf2.sha512", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-248541`

### Rule: OL 8 operating systems must require authentication upon booting into rescue mode.

**Rule ID:** `SV-248541r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system does not require valid root authentication before it boots into emergency or rescue mode, anyone who invokes emergency or rescue mode is granted privileged access to all files on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system requires authentication for rescue mode with the following command: $ sudo grep sulogin-shell /usr/lib/systemd/system/rescue.service ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue If the "ExecStart" line is configured for anything other than "/usr/lib/systemd/systemd-sulogin-shell rescue" or is commented out or missing, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-248542`

### Rule: OL 8 operating systems must require authentication upon booting into emergency mode.

**Rule ID:** `SV-248542r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system does not require valid root authentication before it boots into emergency or rescue mode, anyone who invokes emergency or rescue mode is granted privileged access to all files on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system requires authentication for emergency mode with the following command: $ sudo grep sulogin-shell /usr/lib/systemd/system/emergency.service ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency If the "ExecStart" line is configured for anything other than "/usr/lib/systemd/systemd-sulogin-shell emergency" or is commented out or missing, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-248543`

### Rule: The OL 8 "pam_unix.so" module must be configured in the system-auth file to use a FIPS 140-2 approved cryptographic hashing algorithm for system authentication.

**Rule ID:** `SV-248543r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. OL 8 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "pam_unix.so" module is configured to use sha512. Check that pam_unix.so module is configured to use sha512 in /etc/pam.d/system-auth with the following command: $ sudo grep password /etc/pam.d/system-auth | grep pam_unix password sufficient pam_unix.so sha512 If "sha512" is missing, or is commented out, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-248544`

### Rule: The OL 8 "pam_unix.so" module must be configured in the password-auth file to use a FIPS 140-2 approved cryptographic hashing algorithm for system authentication.

**Rule ID:** `SV-248544r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. OL 8 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "pam_unix.so" module is configured to use sha512 in "/etc/pam.d/password-auth" with the following command: $ sudo grep password /etc/pam.d/password-auth | grep pam_unix password sufficient pam_unix.so sha512 If "sha512" is missing, or is commented out, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-248545`

### Rule: OL 8 must prevent system daemons from using Kerberos for authentication.

**Rule ID:** `SV-248545r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. OL 8 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. The key derivation function (KDF) in Kerberos is not FIPS compatible. Ensuring the system does not have any keytab files present prevents system daemons from using Kerberos for authentication. A keytab is a file containing pairs of Kerberos principals and encrypted keys. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 prevents system daemons from using Kerberos for authentication. If the system is a server using krb5-server-1.17-18.el8.x86_64 or newer, this requirement is not applicable. If the system is a workstation using krb5-workstation-1.17-18.el8.x86_64 or newer, this requirement is not applicable. Check if there are available keytabs with the following command: $ sudo ls -al /etc/*.keytab If this command produces any file(s), this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-248546`

### Rule: The krb5-workstation package must not be installed on OL 8.

**Rule ID:** `SV-248546r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. OL 8 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. Currently, Kerberos does not use FIPS 140-2 cryptography. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the krb5-workstation package has not been installed on the system with the following commands: If the system is a server or is using krb5-workstation-1.17-18.el8.x86_64 or newer, this is Not Applicable. $ sudo yum list installed krb5-workstation krb5-workstation.x86_64 1.17-9.el8 repository If the krb5-workstation package is installed and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-248547`

### Rule: The krb5-server package must not be installed on OL 8.

**Rule ID:** `SV-248547r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. OL 8 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. Currently, Kerberos does not use FIPS 140-2 cryptography. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the krb5-server package has not been installed on the system with the following commands: If the system is a workstation or is using krb5-server-1.17-18.el8.x86_64 or newer, this is Not Applicable $ sudo yum list installed krb5-server krb5-server.x86_64 1.17-9.el8 repository If the krb5-server package is installed and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-248548`

### Rule: OL 8 must use a Linux Security Module configured to enforce limits on system services.

**Rule ID:** `SV-248548r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes but is not limited to establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system verifies correct operation of all security functions. Check if "SELinux" is in "Enforcing" mode with the following command: $ getenforce Enforcing If "SELinux" is not in "Enforcing" mode, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-248549`

### Rule: OL 8 must have the "policycoreutils" package installed.

**Rule ID:** `SV-248549r958518_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes but is not limited to establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system has the "policycoreutils" package installed with the following command: $ sudo yum list installed policycoreutils policycoreutils.x86_64 2.9-3.el8 @anaconda If the "policycoreutils" package is not installed, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-248551`

### Rule: A sticky bit must be set on all OL 8 public directories to prevent unauthorized and unintended information transferred via shared system resources.

**Rule ID:** `SV-248551r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all world-writable directories have the sticky bit set. Verify that all world-writable directories have the sticky bit set by running the following command: $ sudo find / -type d \( -perm -0002 -a ! -perm -1000 \) -print 2>/dev/null If any of the returned directories are world-writable and do not have the sticky bit set, this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-248552`

### Rule: OL 8 must be configured so that all network connections associated with SSH traffic terminate after becoming unresponsive.

**Rule ID:** `SV-248552r986329_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session. OL 8 uses "/etc/ssh/sshd_config" for configurations of OpenSSH. Within the "sshd_config", the product of the values of "ClientAliveInterval" and "ClientAliveCountMax" is used to establish the inactivity threshold. The "ClientAliveInterval" is a timeout interval in seconds after which if no data has been received from the client, sshd will send a message through the encrypted channel to request a response from the client. The "ClientAliveCountMax" is the number of client alive messages that may be sent without sshd receiving any messages back from the client. If this threshold is met, sshd will disconnect the client. For more information on these settings and others, refer to the sshd_config man pages. Satisfies: SRG-OS-000126-GPOS-00066, SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server automatically terminates a user session after the SSH client has become unresponsive. Check that the "ClientAliveCountMax" is set to "1" by running the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientalivecountmax' ClientAliveCountMax 1 If "ClientAliveCountMax" does not exist, does not have a product value of "1" in "/etc/ssh/sshd_config", or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-248553`

### Rule: OL 8 must be configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive.

**Rule ID:** `SV-248553r986330_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session. OL 8 uses "/etc/ssh/sshd_config" for configurations of OpenSSH. Within the "sshd_config", the product of the values of "ClientAliveInterval" and "ClientAliveCountMax" is used to establish the inactivity threshold. The "ClientAliveInterval" is a timeout interval in seconds after which if no data has been received from the client, sshd will send a message through the encrypted channel to request a response from the client. The "ClientAliveCountMax" is the number of client alive messages that may be sent without sshd receiving any messages back from the client. If this threshold is met, sshd will disconnect the client. For more information on these settings and others, refer to the sshd_config man pages. Satisfies: SRG-OS-000126-GPOS-00066, SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server automatically terminates a user session after the SSH client has been unresponsive for 10 minutes. Check that the "ClientAliveInterval" variable is set to a value of "600" or less by running the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientaliveinterval' ClientAliveInterval 600 If "ClientAliveInterval" does not exist, does not have a product value of "600" or less in "/etc/ssh/sshd_config", or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248554`

### Rule: The OL 8 "/var/log/messages" file must have mode 0640 or less permissive.

**Rule ID:** `SV-248554r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 8 system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/var/log/messages" file has mode "0640" or less permissive with the following command: $ sudo stat -c "%a %n" /var/log/messages 640 /var/log/messages If a value of "0640" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248555`

### Rule: The OL 8 "/var/log/messages" file must be owned by root.

**Rule ID:** `SV-248555r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 8 system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the /var/log/messages file is owned by root with the following command: $ sudo stat -c "%U" /var/log/messages root If "root" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248556`

### Rule: The OL 8 "/var/log/messages" file must be group-owned by root.

**Rule ID:** `SV-248556r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 8 system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log/messages" file is group-owned by root with the following command: $ sudo stat -c "%G" /var/log/messages root If "root" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248557`

### Rule: The OL 8 "/var/log" directory must have mode 0755 or less permissive.

**Rule ID:** `SV-248557r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 8 system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/var/log" directory has a mode of "0755" or less with the following command: $ sudo stat -c "%a %n" /var/log 755 /var/log If a value of "0755" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248558`

### Rule: The OL 8 "/var/log" directory must be owned by root.

**Rule ID:** `SV-248558r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 8 system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /var/log directory is owned by root with the following command: $ sudo stat -c "%U" /var/log root If "root" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248559`

### Rule: The OL 8 "/var/log" directory must be group-owned by root.

**Rule ID:** `SV-248559r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 8 system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log" directory is group-owned by root with the following command: $ sudo stat -c "%G" /var/log root If "root" is not returned as a result, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-248560`

### Rule: The OL 8 SSH daemon must be configured to use system-wide crypto policies.

**Rule ID:** `SV-248560r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 8 incorporates system-wide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/ directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that system-wide crypto policies are in effect: $ sudo grep -i CRYPTO_POLICY /etc/sysconfig/sshd # CRYPTO_POLICY= If the "CRYPTO_POLICY" is uncommented, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-248561`

### Rule: The OL 8 SSH server must be configured to use only Message Authentication Codes (MACs) employing FIPS 140-2 validated cryptographic hash algorithms.

**Rule ID:** `SV-248561r958510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography, enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 8 incorporates system-wide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the "/etc/sysconfig/sshd" file. The employed algorithms can be viewed in the "/etc/crypto-policies/back-ends/opensshserver.config" file. The system will attempt to use the first hash presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest hash available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to use only MACs employing FIPS 140-2-approved algorithms with the following command: $ sudo grep -i macs /etc/crypto-policies/back-ends/opensshserver.config -oMACS=hmac-sha2-512,hmac-sha2-256,hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com If the MACs entries in the "opensshserver.config" file have any hashes other than shown here, the order differs from the example above, or they are missing or commented out, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-248562`

### Rule: The OL 8 SSH server must be configured to use only ciphers employing FIPS 140-2 validated cryptographic algorithms.

**Rule ID:** `SV-248562r958510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. Operating systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system. The system will attempt to use the first hash presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest cipher available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OL 8 SSH server is configured to use only ciphers employing FIPS 140-2 approved algorithms with the following command: $ sudo grep -i ciphers /etc/crypto-policies/back-ends/opensshserver.config CRYPTO_POLICY='-oCiphers=aes256-ctr,aes192-ctr,aes128-ctr,aes256-gcm@openssh.com,aes128-gcm@openssh.com' If the cipher entries in the "opensshserver.config" file have any ciphers other than shown here, the order differs from the example above, or they are missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-248563`

### Rule: The OL 8 SSH server must be configured to use strong entropy.

**Rule ID:** `SV-248563r991593_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The most important characteristic of a random number generator is its randomness, namely its ability to deliver random numbers that are impossible to predict. Entropy in computer security is associated with the unpredictability of a source of randomness. The random source with high entropy tends to achieve a uniform distribution of random values. Random number generators are one of the most important building blocks of cryptosystems. The SSH implementation in OL 8 uses the OPENSSL library, which does not use high-entropy sources by default. By using the SSH_USE_STRONG_RNG environment variable, the OPENSSL random generator is reseeded from "/dev/random". This setting is not recommended on computers without the hardware random generator because insufficient entropy causes the connection to be blocked until enough entropy is available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system SSH server uses strong entropy with the following command: $ sudo grep -i ssh_use_strong_rng /etc/sysconfig/sshd SSH_USE_STRONG_RNG=32 If the "SSH_USE_STRONG_RNG" line does not equal "32" or is commented out or missing, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-248564`

### Rule: The OL 8 operating system must implement DoD-approved encryption in the OpenSSL package.

**Rule ID:** `SV-248564r1069146_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography, enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 8 incorporates systemwide crypto policies by default. The employed algorithms can be viewed in the "/etc/crypto-policies/back-ends/openssl.config" file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OpenSSL library is configured to use only ciphers employing FIPS 140-2-approved algorithms: Verify that systemwide crypto policies are in effect: $ sudo grep -i opensslcnf.config /etc/pki/tls/openssl.cnf .include /etc/crypto-policies/back-ends/opensslcnf.config If the "opensslcnf.config" is not defined in the "/etc/pki/tls/openssl.cnf" file, this is a finding. Verify which systemwide crypto policy is in use: $ sudo fips-mode-setup --check FIPS mode is enabled. If the systemwide crypto policy is set to anything other than "FIPS", this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-248565`

### Rule: The OL 8 operating system must implement DoD-approved TLS encryption in the OpenSSL package.

**Rule ID:** `SV-248565r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography, enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 8 incorporates system-wide crypto policies by default. The employed algorithms can be viewed in the "/etc/crypto-policies/back-ends/openssl.config" file. Satisfies: SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000125-GPOS-00065</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OpenSSL library is configured to use only DoD-approved TLS encryption: For versions prior to crypto-policies-20210617-1.gitc776d3e.el8.noarch: $ sudo grep -i MinProtocol /etc/crypto-policies/back-ends/opensslcnf.config MinProtocol = TLSv1.2 If the "MinProtocol" is set to anything older than "TLSv1.2", this is a finding. For version crypto-policies-20210617-1.gitc776d3e.el8.noarch and newer: $ sudo grep -i MinProtocol /etc/crypto-policies/back-ends/opensslcnf.config TLS.MinProtocol = TLSv1.2 DTLS.MinProtocol = DTLSv1.2 If the "TLS.MinProtocol" is set to anything older than "TLSv1.2" or the "DTLS.MinProtocol" is set to anything older than "DTLSv1.2", this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-248566`

### Rule: The OL 8 operating system must implement DoD-approved TLS encryption in the GnuTLS package.

**Rule ID:** `SV-248566r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Transport Layer Security (TLS) encryption is a required security setting as a number of known vulnerabilities have been reported against Secure Sockets Layer (SSL) and earlier versions of TLS. Encryption of private information is essential to ensuring data confidentiality. If private information is not encrypted, it can be intercepted and easily read by an unauthorized party. SQL Server must use a minimum of FIPS 140-2 approved TLS version 1.2, and all non-FIPS-approved SSL and TLS versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography, enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. The GnuTLS library offers an API to access secure communications protocols. SSLv2 is not available in the GnuTLS library. The OL 8 system-wide crypto policy defines employed algorithms in the "/etc/crypto-policies/back-ends/gnutls.config" file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the GnuTLS library is configured to only allow DoD-approved SSL/TLS versions: $ sudo grep -io +vers.* /etc/crypto-policies/back-ends/gnutls.config +VERS-ALL:-VERS-DTLS0.9:-VERS-SSL3.0:-VERS-TLS1.0:-VERS-TLS1.1:-VERS-DTLS1.0:+COMP-NULL:%PROFILE_MEDIUM If the "gnutls.config" does not list "-VERS-DTLS0.9:-VERS-SSL3.0:-VERS-TLS1.0:-VERS-TLS1.1:-VERS-DTLS1.0" to disable unapproved SSL/TLS versions, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-248567`

### Rule: OL 8 system commands must have mode 755 or less permissive.

**Rule ID:** `SV-248567r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories have mode "755" or less permissive with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -exec ls -l {} \; If any system commands are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-248568`

### Rule: OL 8 system commands must be owned by root.

**Rule ID:** `SV-248568r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are owned by "root" with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -exec ls -l {} \; If any system commands are returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-248569`

### Rule: OL 8 system commands must be group-owned by root or a system account.

**Rule ID:** `SV-248569r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are group-owned by "root" or a required system account, with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -exec ls -l {} \; If any system commands are returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-248570`

### Rule: OL 8 library files must have mode 755 or less permissive.

**Rule ID:** `SV-248570r1101862_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" have mode 0755 or less permissive. Check that the systemwide shared library files have mode 0755 or less permissive with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' -perm /022 -exec stat -c "%n %a" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-248571`

### Rule: OL 8 library files must be owned by root.

**Rule ID:** `SV-248571r1101865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are owned by root with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -user root -exec stat -c "%n %U" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-248572`

### Rule: OL 8 library files must be group-owned by root.

**Rule ID:** `SV-248572r1101868_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are group owned by root with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -group root -exec stat -c "%n %G" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-248573`

### Rule: The OL 8 file integrity tool must notify the system administrator (SA) when changes to the baseline configuration or anomalies in the operation of any security functions are discovered within an organizationally defined frequency.

**Rule ID:** `SV-248573r1069152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's information system security manager (ISSM)/information system security officer (ISSO) and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Notifications provided by information systems include messages to local computer consoles and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection. OL 8 comes with many optional software packages, including the file integrity tool Advanced Intrusion Detection Environment (AIDE). This requirement assumes the use of AIDE; however, a different tool may be used if the requirements are met. Note that AIDE does not have a configuration that will send a notification, so a cron job is recommended that uses the mail application on the system to email the results of the file integrity check. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000446-GPOS-00200, SRG-OS-000447-GPOS-00201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system routinely checks the baseline configuration for unauthorized changes and notifies the SA when anomalies in the operation of any security functions are discovered. Check that OL 8 routinely executes a file integrity scan for changes to the system baseline. The command used in the example will use a daily occurrence. Check the cron directories for scripts controlling the execution and notification of results of the file integrity application. For example, if AIDE is installed on the system, use the following commands: To search for an aide script: $ sudo ls -al /etc/cron.* | grep aide -rwxr-xr-x 1 root root 29 Nov 22 2015 aide To search for scheduled cron jobs: $ sudo grep -r aide /etc/cron* /etc/cron.d/aide:0 0 * * * root /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily AIDE integrity check run" root@example_server_name.mil Check the contents of script files: $ sudo more /etc/cron.d/aide #!/bin/bash /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily AIDE integrity check run" root@example_server_name.mil If the file integrity application does not exist, a script file controlling the execution of the file integrity application does not exist, or the file integrity application does not notify designated personnel of changes, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-248574`

### Rule: YUM must be configured to prevent the installation of patches, service packs, device drivers, or OL 8 system components that have not been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-248574r1015031_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved Certificate Authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that YUM verifies the signature of packages from a repository prior to install with the following command: $ sudo grep gpgcheck /etc/yum.repos.d/*.repo gpgcheck=1 If "gpgcheck" is not set to "1", or if options are missing or commented out, ask the system administrator (SA) how the certificates for patches and other operating system components are verified. If there is no process to validate certificates that is approved by the organization, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-248575`

### Rule: OL 8 must prevent the installation of software, patches, service packs, device drivers, or operating system components of local packages without verification they have been digitally signed using a certificate that is issued by a Certificate Authority (CA) that is recognized and approved by the organization.

**Rule ID:** `SV-248575r1015032_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved Certificate Authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system prevents the installation of patches, service packs, device drivers, or operating system components from a repository without verification that they have been digitally signed using a certificate that is recognized and approved by the organization. Check if YUM is configured to perform a signature check on local packages with the following command: $ sudo grep -i localpkg_gpgcheck /etc/dnf/dnf.conf localpkg_gpgcheck =True If "localpkg_gpgcheck" is not set to either "1", "True", or "yes", commented out, or is missing from "/etc/dnf/dnf.conf", this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-248576`

### Rule: OL 8 must prevent the loading of a new kernel for later execution.

**Rule ID:** `SV-248576r1015033_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Disabling "kexec_load" prevents an unsigned kernel image (that could be a windows kernel or modified vulnerable kernel) from being loaded. Kexec can be used to subvert the entire secureboot process and should be avoided at all costs, especially since it can load unsigned kernel images. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For OL 8 systems using the Oracle Unbreakable Enterprise Kernel (UEK) Release 6 or above and with secureboot enabled, this requirement is Not Applicable. Verify the operating system is configured to disable kernel image loading with the following commands. Check the status of the "kernel.kexec_load_disabled" kernel parameter: $ sudo sysctl kernel.kexec_load_disabled kernel.kexec_load_disabled = 1 If "kernel.kexec_load_disabled" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r kernel.kexec_load_disabled /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:kernel.kexec_load_disabled = 1 If "kernel.kexec_load_disabled" is not set to "1" or is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-248577`

### Rule: OL 8 must enable kernel parameters to enforce Discretionary Access Control (DAC) on symlinks.

**Rule ID:** `SV-248577r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAC is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When DAC policies are implemented, subjects are not constrained as to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control (MAC) policies is still able to operate under the less rigorous constraints of this requirement. Therefore, while MAC imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of DAC require identity-based access control, that limitation is not required for this use of DAC. By enabling the "fs.protected_symlinks" kernel parameter, symbolic links are permitted to be followed only when outside a sticky world-writable directory, or when the UID of the link and follower match, or when the directory owner matches the symlink's owner. Disallowing such symlinks helps mitigate vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat(). The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to enable DAC on symlinks with the following commands. Check the status of the "fs.protected_symlinks" kernel parameter: $ sudo sysctl fs.protected_symlinks fs.protected_symlinks = 1 If "fs.protected_symlinks" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r fs.protected_symlinks /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:fs.protected_symlinks = 1 If "fs.protected_symlinks" is not set to "1" or is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-248578`

### Rule: OL 8 must enable kernel parameters to enforce Discretionary Access Control (DAC) on hardlinks.

**Rule ID:** `SV-248578r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAC is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When DAC policies are implemented, subjects are not constrained as to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control (MAC) policies is still able to operate under the less rigorous constraints of this requirement. Therefore, while MAC imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of DAC require identity-based access control, that limitation is not required for this use of DAC. By enabling the "fs.protected_hardlinks" kernel parameter, users can no longer create soft or hard links to files they do not own. Disallowing such hardlinks mitigate vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat(). The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to enable DAC on hardlinks with the following commands. Check the status of the "fs.protected_hardlinks" kernel parameter: $ sudo sysctl fs.protected_hardlinks fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r fs.protected_hardlinks /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1" or is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-248579`

### Rule: OL 8 must restrict access to the kernel message buffer.

**Rule ID:** `SV-248579r958524_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components. Restricting access to the kernel message buffer limits access to only root. This prevents attackers from gaining additional system information as a non-privileged user. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to restrict access to the kernel message buffer with the following commands. Check the status of the "kernel.dmesg_restrict" kernel parameter: $ sudo sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r kernel.dmesg_restrict /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-248580`

### Rule: OL 8 must prevent kernel profiling by unprivileged users.

**Rule ID:** `SV-248580r958524_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components. Setting the "kernel.perf_event_paranoid" kernel parameter to "2" prevents attackers from gaining additional system information as a non-privileged user. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to prevent kernel profiling by unprivileged users with the following commands. Check the status of the "kernel.perf_event_paranoid" kernel parameter: $ sudo sysctl kernel.perf_event_paranoid kernel.perf_event_paranoid = 2 If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r kernel.perf_event_paranoid /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:kernel.perf_event_paranoid = 2 If "kernel.perf_event_paranoid" is not set to "2" or is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-248581`

### Rule: OL 8 must require users to provide a password for privilege escalation.

**Rule ID:** `SV-248581r1101870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/sudoers" has no occurrences of "NOPASSWD". Check that the "/etc/sudoers" file has no occurrences of "NOPASSWD" by running the following command: $ sudo grep -iR 'NOPASSWD' /etc/sudoers /etc/sudoers.d/ %admin ALL=(ALL) NOPASSWD: ALL If any occurrences of "NOPASSWD" are returned from the command and have not been documented with the information system security officer (ISSO) as an organizationally defined administrative group using multifactor authentication (MFA), this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-248582`

### Rule: OL 8 must require users to reauthenticate for privilege escalation and changing roles.

**Rule ID:** `SV-248582r1101872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/sudoers" file has no occurrences of "!authenticate" by running the following command: $ sudo egrep -iR '!authenticate' /etc/sudoers /etc/sudoers.d/ If any occurrences of "!authenticate" return from the command, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248583`

### Rule: OL 8 must restrict privilege elevation to authorized personnel.

**Rule ID:** `SV-248583r1101874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sudo command allows a user to execute programs with elevated (administrator) privileges. It prompts the user for their password and confirms your request to execute a command by checking a file, called sudoers. If the "sudoers" file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "sudoers" file restricts sudo access to authorized personnel. $ sudo grep -iwR 'ALL' /etc/sudoers /etc/sudoers.d/ | grep -v '#' If the either of the following entries are returned, this is a finding: ALL ALL=(ALL) ALL ALL ALL=(ALL:ALL) ALL

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248584`

### Rule: OL 8 must use the invoking user's password for privilege escalation when using "sudo".

**Rule ID:** `SV-248584r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sudoers security policy requires that users authenticate themselves before they can use sudo. When sudoers requires authentication, it validates the invoking user's credentials. If the rootpw, targetpw, or runaspw flags are defined and not disabled, by default the operating system will prompt the invoking user for the "root" user password. For more information on each of the listed configurations, reference the sudoers(5) manual page.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the sudoers security policy is configured to use the invoking user's password for privilege escalation. $ sudo grep -Eir '(rootpw|targetpw|runaspw)' /etc/sudoers /etc/sudoers.d* | grep -v '#' /etc/sudoers:Defaults !targetpw /etc/sudoers:Defaults !rootpw /etc/sudoers:Defaults !runaspw If conflicting results are returned, this is a finding. If "Defaults !targetpw" is not defined, this is a finding. If "Defaults !rootpw" is not defined, this is a finding. If "Defaults !runaspw" is not defined, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-248585`

### Rule: OL 8 must require reauthentication when using the "sudo" command.

**Rule ID:** `SV-248585r1050789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the organization requires the user to reauthenticate when using the "sudo" command. If the value is set to an integer less than 0, the user's time stamp will not expire and the user will not have to reauthenticate for privileged actions until the user's session is terminated. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system requires re-authentication when using the "sudo" command to elevate privileges. $ sudo grep -Eir 'timestamp_timeout' /etc/sudoers /etc/sudoers.d* /etc/sudoers:Defaults timestamp_timeout=0 If conflicting results are returned, this is a finding. If "timestamp_timeout" is set to a negative number, is commented out, or no results are returned, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-248586`

### Rule: OL 8 must have the package required for multifactor authentication installed.

**Rule ID:** `SV-248586r1015037_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using an authentication device, such as a DOD Common Access Card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, credentials stored on the authentication device will not be affected. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD CAC. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system has the package required for multifactor authentication installed with the following command: $ sudo yum list installed openssl-pkcs11 openssl-pkcs11.x86_64 0.4.8-2.el8 @anaconda If the "openssl-pkcs11" package is not installed, ask the administrator to indicate what type of multifactor authentication is being used and what packages are installed to support it. If there is no evidence of multifactor authentication being used, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-248587`

### Rule: OL 8 must implement certificate status checking for multifactor authentication.

**Rule ID:** `SV-248587r1015038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a DOD Common Access Card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, credentials stored on the authentication device will not be affected. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD CAC. OL 8 includes multiple options for configuring certificate status checking but for this requirement focuses on the system security services daemon (sssd). By default, sssd performs Online Certificate Status Protocol (OCSP) checking and certificate verification using a sha256 digest function. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system implements certificate status checking for multifactor authentication. Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable. Determine if Online Certificate Status Protocol (OCSP) is enabled and using the proper digest value on the system with the following command: $ sudo grep certificate_verification /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf | grep -v "^#" certificate_verification = ocsp_dgst=sha1 If the certificate_verification line is missing from the [sssd] section, or is missing "ocsp_dgst=sha1", ask the administrator to indicate what type of multifactor authentication is being used and how the system implements certificate status checking. If there is no evidence of certificate status checking being used, this is a finding.

## Group: SRG-OS-000376-GPOS-00161

**Group ID:** `V-248588`

### Rule: OL 8 must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-248588r958816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. The DoD has mandated the use of the Common Access Card (CAC) to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 accepts PIV credentials. Check that the "opensc" package is installed on the system with the following command: $ sudo yum list installed opensc opensc.x86_64 0.19.0-5.el8 @anaconda Check that "opensc" accepts PIV cards with the following command: $ sudo opensc-tool --list-drivers | grep -i piv PIV-II Personal Identity Verification Card If the "opensc" package is not installed and the "opensc-tool" driver list does not include "PIV-II", this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-248589`

### Rule: OL 8 must implement non-executable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-248589r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced, with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NX (no-execution) bit flag is set on the system with the following commands: $ sudo dmesg | grep NX [ 0.000000] NX (Execute Disable) protection: active If "dmesg" does not show "NX (Execute Disable) protection" active, check the "cpuinfo" settings with the following command: $ sudo less /proc/cpuinfo | grep -i flags flags : fpu vme de pse tsc ms nx rdtscp lm constant_tsc If "flags" does not contain the "nx" flag, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-248590`

### Rule: OL 8 must clear the page allocator to prevent use-after-free attacks.

**Rule ID:** `SV-248590r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Adversaries may launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Poisoning writes an arbitrary value to freed pages, so any modification or reference to that page after being freed or before being initialized will be detected and prevented. This prevents many types of use-after-free vulnerabilities at little performance cost. Also prevents leak of data and detection of corrupted memory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that GRUB 2 is configured to enable page poisoning to mitigate use-after-free vulnerabilities with the following commands: $ sudo grub2-editenv list | grep page_poison kernelopts=root=/dev/mapper/ol-root ro crashkernel=auto resume=/dev/mapper/ol-swap rd.lvm.lv=ol/root rd.lvm.lv=ol/swap rhgb quiet fips=1 page_poison=1 vsyscall=none audit=1 audit_backlog_limit=8192 boot=UUID=8d171156-cd61-421c-ba41-1c021ac29e82 If "page_poison" is not set to "1" or is missing, this is a finding. Check that page poisoning is enabled by default to persist in kernel updates: $ sudo grep page_poison /etc/default/grub GRUB_CMDLINE_LINUX="page_poison=1" If "page_poison" is not set to "1" or is missing or commented out, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-248591`

### Rule: OL 8 must disable virtual syscalls.

**Rule ID:** `SV-248591r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Syscalls are special routines in the Linux kernel, which userspace applications ask to do privileged tasks. Invoking a system call is an expensive operation because the processor must interrupt the currently executing task and switch context to kernel mode and then back to userspace after the system call completes. Virtual syscalls map into user space a page that contains some variables and the implementation of some system calls. This allows the system calls to be executed in userspace to alleviate the context switching expense. Virtual syscalls provide an opportunity of attack for a user who has control of the return instruction pointer. Disabling vsyscalls help to prevent return-oriented programming (ROP) attacks via buffer overflows and overruns. If the system intends to run containers based on OL 6 components, then virtual syscalls will need enabled so the components function properly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that GRUB 2 is configured to disable vsyscalls with the following commands: $ sudo grub2-editenv list | grep vsyscall kernelopts=root=/dev/mapper/ol-root ro crashkernel=auto resume=/dev/mapper/ol-swap rd.lvm.lv=ol/root rd.lvm.lv=ol/swap rhgb quiet fips=1 page_poison=1 vsyscall=none audit=1 audit_backlog_limit=8192 boot=UUID=8d171156-cd61-421c-ba41-1c021ac29e82 If "vsyscall" is not set to "none" or is missing, this is a finding. Check that vsyscalls are disabled by default to persist in kernel updates: $ sudo grep vsyscall /etc/default/grub GRUB_CMDLINE_LINUX="vsyscall=none" If "vsyscall" is not set to "none", is missing or commented out and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-248592`

### Rule: OL 8 must clear memory when it is freed to prevent use-after-free attacks.

**Rule ID:** `SV-248592r1069149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Poisoning writes an arbitrary value to freed pages, so any modification or reference to that page after being freed or before being initialized will be detected and prevented. This prevents many types of use-after-free vulnerabilities at little performance cost. Also prevents leak of data and detection of corrupted memory. init_on_free is a Linux kernel boot parameter that enhances security by initializing memory regions when they are freed, preventing data leakage. This process ensures that stale data in freed memory cannot be accessed by malicious programs. SLUB canaries add a randomized value (canary) at the end of SLUB-allocated objects to detect memory corruption caused by buffer overflows or underflows. Redzoning adds padding (red zones) around SLUB-allocated objects to detect overflows or underflows by triggering a fault when adjacent memory is accessed. SLUB canaries are often more efficient and provide stronger detection against buffer overflows compared to redzoning. SLUB canaries are supported in hardened Linux kernels like the ones provided by Linux-hardened. SLAB objects are blocks of physically contiguous memory. SLUB is the unqueued SLAB allocator. Satisfies: SRG-OS-000433-GPOS-00192, SRG-OS-000134-GPOS-00068</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify GRUB2 is configured to mitigate use-after-free vulnerabilities by employing memory poisoning. Inspect the "GRUB_CMDLINE_LINUX" entry of /etc/default/grub as follows: $ sudo grep -i grub_cmdline_linux /etc/default/grub GRUB_CMDLINE_LINUX="... init_on_free=1" If "init_on_free=1" is missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248593`

### Rule: OL 8 must not let Meltdown and Spectre exploit critical vulnerabilities in modern processors.

**Rule ID:** `SV-248593r1069159_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Hardware vulnerabilities allow programs to steal data that is currently processed on the computer. While programs are typically not permitted to read data from other programs, a malicious program can exploit Meltdown and Spectre to obtain secrets stored in the memory of other running programs. This might include passwords stored in a password manager or browser; personal photos, emails, and instant messages; and business-critical documents.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is configured to enable mitigations with the following command: $ grubby --info=/boot/vmlinuz-$(uname -r) | grep mitigations If the "mitigations" parameter is set to "off" (mitigations=off), this is a finding. Note: The default behavior of the kernel is to enable mitigations for vulnerabilities like Meltdown and Spectre based on hardware and system requirements. Therefore, if the "mitigation" parameter is not present or if it is set to on this is not a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-248594`

### Rule: OL 8 must implement address space layout randomization (ASLR) to protect its memory from unauthorized code execution.

**Rule ID:** `SV-248594r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced, with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 implements ASLR with the following command: $ sudo sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If "kernel.randomize_va_space" is not set to "2", this is a finding. Check that the configuration files are present to enable this kernel parameter. $ sudo grep -r kernel.randomize_va_space /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:kernel.randomize_va_space = 2 If "kernel.randomize_va_space" is not set to "2", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-248595`

### Rule: YUM must remove all software components after updated versions have been installed on OL 8.

**Rule ID:** `SV-248595r958936_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system removes all software components after updated versions have been installed. Check if YUM is configured to remove unneeded packages with the following command: $ sudo grep -i clean_requirements_on_remove /etc/yum.conf clean_requirements_on_remove=True If "clean_requirements_on_remove" is not set to "True", commented out, or missing from "/etc/yum.conf", this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-248596`

### Rule: OL 8 must enable the SELinux targeted policy.

**Rule ID:** `SV-248596r958944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, they may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes but is not limited to establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the operating system verifies correct operation of all security functions. Verify that "SELinux" is active and is enforcing the targeted policy with the following command: $ sudo sestatus SELinux status: enabled SELinuxfs mount: /sys/fs/selinux SELinux root directory: /etc/selinux Loaded policy name: targeted Current mode: enforcing Mode from config file: enforcing Policy MLS status: enabled Policy deny_unknown status: allowed Memory protection checking: actual (secure) Max kernel policy version: 31 If the "Loaded policy name" is not set to "targeted", this is a finding. Verify that the "/etc/selinux/config" file is configured to the "SELINUXTYPE" as "targeted": $ sudo grep -i "selinuxtype" /etc/selinux/config | grep -v '^#' SELINUXTYPE = targeted If no results are returned or "SELINUXTYPE" is not set to "targeted", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248597`

### Rule: There must be no "shosts.equiv" files on the OL 8 operating system.

**Rule ID:** `SV-248597r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The "shosts.equiv" files are used to configure host-based authentication for the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no "shosts.equiv" files on OL 8 with the following command: $ sudo find / -name shosts.equiv If an "shosts.equiv" file is found, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248598`

### Rule: There must be no ".shosts" files on the OL 8 operating system.

**Rule ID:** `SV-248598r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The ".shosts" files are used to configure host-based authentication for individual users or the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no ".shosts" files on OL 8 with the following command: $ sudo find / -name '*.shosts' If any ".shosts" files are found, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248599`

### Rule: OL 8 must enable the hardware random number generator entropy gatherer service.

**Rule ID:** `SV-248599r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The most important characteristic of a random number generator is its randomness, namely its ability to deliver random numbers that are impossible to predict. Entropy in computer security is associated with the unpredictability of a source of randomness. The random source with high entropy tends to achieve a uniform distribution of random values. Random number generators are one of the most important building blocks of cryptosystems. The rngd service feeds random data from hardware device to kernel random device. Quality (nonpredictable) random number generation is important for several security functions (i.e., ciphers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For OL versions 8.4 and above running with kernel FIPS mode enabled as specified by OL08-00-010020, this requirement is Not Applicable. Check that OL 8 has enabled the hardware random number generator entropy gatherer service. Verify the rngd service is enabled and active with the following commands: $ sudo systemctl is-enabled rngd enabled $ sudo systemctl is-active rngd active If the service is not "enabled" and "active", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248600`

### Rule: OL 8 must have the packages required to use the hardware random number generator entropy gatherer service.

**Rule ID:** `SV-248600r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The most important characteristic of a random number generator is its randomness, namely its ability to deliver random numbers that are impossible to predict. Entropy in computer security is associated with the unpredictability of a source of randomness. The random source with high entropy tends to achieve a uniform distribution of random values. Random number generators are one of the most important building blocks of cryptosystems. The rngd service feeds random data from hardware device to kernel random device. Quality (non-predictable) random number generation is important for several security functions (i.e., ciphers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that OL 8 has the packages required to enabled the hardware random number generator entropy gatherer service with the following command: $ sudo yum list installed rng-tools rng-tools.x86_64 6.8-3.el8 @anaconda If the "rng-tools" package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248601`

### Rule: The OL 8 SSH public host key files must have mode "0644" or less permissive.

**Rule ID:** `SV-248601r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH public host key files have mode "0644" or less permissive with the following command: $ sudo ls -l /etc/ssh/*.pub -rw-r--r-- 1 root wheel 618 Nov 28 06:43 ssh_host_dsa_key.pub -rw-r--r-- 1 root wheel 347 Nov 28 06:43 ssh_host_key.pub -rw-r--r-- 1 root wheel 238 Nov 28 06:43 ssh_host_rsa_key.pub If any "key.pub" file has a mode more permissive than "0644", this is a finding. Note: SSH public key files may be found in other directories on the system depending on the installation.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248602`

### Rule: The OL 8 SSH private host key files must have mode "0640" or less permissive.

**Rule ID:** `SV-248602r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH private host key files have mode "0640" or less permissive with the following command: $ sudo ls -alL /etc/ssh/ssh_host*key -rw-r----- 1 root wheel 668 Nov 28 06:43 ssh_host_dsa_key -rw-r----- 1 root wheel 582 Nov 28 06:43 ssh_host_key -rw-r----- 1 root wheel 887 Nov 28 06:43 ssh_host_rsa_key If any private host key file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248603`

### Rule: The OL 8 SSH daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-248603r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log on to the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon performs strict mode checking of home directory configuration files with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*strictmodes' StrictModes yes If "StrictModes" is set to "no" or is missing, or if the returned line is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248605`

### Rule: The OL 8 SSH daemon must not allow authentication using known host's authentication.

**Rule ID:** `SV-248605r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring this setting for the SSH daemon provides additional assurance that remote logon via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow authentication using known host’s authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*ignoreuserknownhosts' IgnoreUserKnownHosts yes If the value is returned as "no", the returned line is commented out, or no output is returned, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248606`

### Rule: The OL 8 SSH daemon must not allow Kerberos authentication, except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-248606r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring this setting for the SSH daemon provides additional assurance that remote logon via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow Kerberos authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*kerberosauthentication' KerberosAuthentication no If the value is returned as "yes", the returned line is commented out, or no output is returned or has not been documented with the information system security officer (ISSO), this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248607`

### Rule: The OL 8 SSH daemon must not allow GSSAPI authentication, except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-248607r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring this setting for the SSH daemon provides additional assurance that remote logon via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow GSSAPI authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*gssapiauthentication' GSSAPIAuthentication no If the value is returned as "yes", the returned line is commented out, or no output is returned or has not been documented with the information system security officer (ISSO), this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248608`

### Rule: OL 8 must use a separate file system for "/var".

**Rule ID:** `SV-248608r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system has been created for "/var" with the following command: $ sudo grep /var /etc/fstab /dev/mapper/... /var xfs defaults,nodev 0 0 If a separate entry for "/var" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248609`

### Rule: OL 8 must use a separate file system for "/var/log".

**Rule ID:** `SV-248609r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system has been created for "/var/log". Check that a file system has been created for "/var/log" with the following command: $ sudo grep /var/log /etc/fstab /dev/mapper/... /var/log xfs defaults,nodev,noexec,nosuid 0 0 If a separate entry for "/var/log" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248610`

### Rule: OL 8 must use a separate file system for the system audit data path.

**Rule ID:** `SV-248610r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for the system audit data path with the following command: Note: "/var/log/audit" is used as the example as it is a common location. $ sudo grep /var/log/audit /etc/fstab UUID=3645951a /var/log/audit ext4 defaults 1 2 If an entry for "/var/log/audit" does not exist, ask the System Administrator if the system audit logs are being written to a different file system/partition on the system and then grep for that file system/partition. If a separate file system/partition does not exist for the system audit data path, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248611`

### Rule: OL 8 must use a separate file system for "/tmp".

**Rule ID:** `SV-248611r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing. Check Text: Verify that a separate file system/partition has been created for non-privileged local interactive user home directories. $ sudo grep /tmp /etc/fstab /dev/mapper/ol-tmp /tmp xfs defaults,nodev,nosuid,noexec 0 0 If a separate entry for the file system/partition "/tmp" does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248612`

### Rule: OL 8 must use a separate file system for /var/tmp.

**Rule ID:** `SV-248612r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system has been created for "/var/tmp". Check that a file system has been created for "/var/tmp" with the following command: $ sudo grep /var/tmp /etc/fstab /dev/mapper/... /var/tmp xfs defaults,nodev,noexec,nosuid 0 0 If a separate entry for "/var/tmp" is not in use, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-248613`

### Rule: OL 8 must not permit direct logons to the root account using remote access via SSH.

**Rule ID:** `SV-248613r1015039_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Although the communications channel may be encrypted, an additional layer of security is gained by extending the policy of not logging on directly as root. In addition, logging on with a user-specific account provides individual accountability of actions performed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify remote access using SSH prevents users from logging on directly as "root" with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permitrootlogin' PermitRootLogin no If the "PermitRootLogin" keyword is set to "yes", is missing, or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248615`

### Rule: OL 8 must have the rsyslog service enabled and active.

**Rule ID:** `SV-248615r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring OL 8 to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across the DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example, registry settings; account, file, and directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the rsyslog service is enabled and active with the following commands: $ sudo systemctl is-enabled rsyslog enabled $ sudo systemctl is-active rsyslog active If the service is not enabled and active, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248616`

### Rule: OL 8 must prevent files with the setuid and setgid bit set from being executed on file systems that contain user home directories.

**Rule ID:** `SV-248616r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that file systems containing user home directories are mounted with the "nosuid" option. Find the file system(s) that contain the user home directories with the following command: $ sudo awk -F: '($3>=1000)&&($1!="nobody"){print $1,$3,$6}' /etc/passwd smithj 1001 /home/smithj robinst 1002 /home/robinst Check the file systems that are mounted at boot time with the following command: $ sudo more /etc/fstab UUID=a411dc99-f2a1-4c87-9e05-184977be8539 /home ext4 rw,relatime,discard,data=ordered,nosuid,nodev,noexec 0 2 If a file system found in "/etc/fstab" refers to the user home directory file system and it does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248617`

### Rule: OL 8 must prevent files with the setuid and setgid bit set from being executed on the /boot directory.

**Rule ID:** `SV-248617r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that use UEFI, this is Not Applicable. Verify the /boot directory is mounted with the "nosuid" option with the following command: $ sudo mount | grep '\s/boot\s' /dev/sda1 on /boot type xfs (rw,nosuid,relatime,seclabe,attr2,inode64,noquota) If the /boot file system does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248618`

### Rule: OL 8 must prevent files with the setuid and setgid bit set from being executed on the /boot/efi directory.

**Rule ID:** `SV-248618r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that use BIOS, this is Not Applicable. Verify the /boot/efi directory is mounted with the "nosuid" option with the following command: $ sudo mount | grep '\s/boot/efi\s' /dev/sda1 on /boot/efi type vfat (rw,nosuid,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=winnt,errors=remount-ro) If the /boot/efi file system does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248619`

### Rule: OL 8 must prevent special devices on non-root local partitions.

**Rule ID:** `SV-248619r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the /dev directory located on the root partition.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all non-root local partitions are mounted with the "nodev" option with the following command: $ sudo mount | grep '^/dev\S* on /\S' | grep --invert-match 'nodev' If any output is produced, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248620`

### Rule: OL 8 file systems that contain user home directories must not execute binary files.

**Rule ID:** `SV-248620r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system not to execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that file systems containing user home directories are mounted with the "noexec" option. Find the file system(s) that contain the user home directories with the following command: $ sudo awk -F: '($3>=1000)&&($1!="nobody"){print $1,$3,$6}' /etc/passwd smithj 1001 /home/smithj robinst 1002 /home/robinst Check the file systems that are mounted at boot time with the following command: $ sudo more /etc/fstab UUID=a411dc99-f2a1-4c87-9e05-184977be8539 /home ext4 rw,relatime,discard,data=ordered,nosuid,nodev,noexec 0 2 If a file system found in "/etc/fstab" refers to the user home directory file system and it does not have the "noexec" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248621`

### Rule: OL 8 file systems must not interpret character or block special devices from untrusted file systems.

**Rule ID:** `SV-248621r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system not to interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that file systems used for removable media are mounted with the "nodev" option with the following command: $ sudo more /etc/fstab UUID=2bc871e4-e2a3-4f29-9ece-3be60c835222 /mnt/usbflash vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "nodev" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248622`

### Rule: OL 8 file systems must not execute binary files on removable media.

**Rule ID:** `SV-248622r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system not to execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that file systems used for removable media are mounted with the "noexec" option with the following command: $ sudo more /etc/fstab UUID=2bc871e4-e2a3-4f29-9ece-3be60c835222 /mnt/usbflash vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "noexec" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248623`

### Rule: OL 8 must prevent files with the setuid and setgid bit set from being executed on file systems that are used with removable media.

**Rule ID:** `SV-248623r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that file systems used for removable media are mounted with the "nosuid" option with the following command: $ sudo more /etc/fstab UUID=2bc871e4-e2a3-4f29-9ece-3be60c835222 /mnt/usbflash vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248624`

### Rule: OL 8 file systems must not execute binary files that are imported via Network File System (NFS).

**Rule ID:** `SV-248624r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system not to execute binary files. This option must be used for mounting any file system not containing approved binary as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that file systems being imported via NFS are mounted with the "noexec" option with the following command: $ sudo grep nfs /etc/fstab | grep noexec UUID=e06097bb-cfcd-437b-9e4d-a691f5662a7d /store nfs rw,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to NFS and it does not have the "noexec" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248625`

### Rule: OL 8 file systems must not interpret character or block special devices that are imported via NFS.

**Rule ID:** `SV-248625r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that file systems being imported via NFS are mounted with the "nodev" option with the following command: $ sudo grep nfs /etc/fstab | grep nodev UUID=e06097bb-cfcd-437b-9e4d-a691f5662a7d /store nfs rw,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to NFS and it does not have the "nodev" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248626`

### Rule: OL 8 must prevent files with the setuid and setgid bit set from being executed on file systems that are imported via Network File System (NFS).

**Rule ID:** `SV-248626r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that file systems being imported via NFS are mounted with the "nosuid" option with the following command: $ sudo grep nfs /etc/fstab | grep nosuid UUID=e06097bb-cfcd-437b-9e4d-a691f5662a7d /store nfs rw,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to NFS and it does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248627`

### Rule: Local OL 8 initialization files must not execute world-writable programs.

**Rule ID:** `SV-248627r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If user start-up files execute world-writable programs, especially in unprotected directories, they could be maliciously modified to destroy user files or otherwise compromise the system at the user level. If the system is compromised at the user level, it is easier to elevate privileges to eventually compromise the system at the root and network level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that local initialization files do not execute world-writable programs. Check the system for world-writable files. The following command will discover and print world-writable files. Run it once for each local partition [PART]: $ sudo find [PART] -xdev -type f -perm -0002 -print For all files listed, check for their presence in the local initialization files with the following commands: Note: The example will be for a system that is configured to create users' home directories in the "/home" directory. $ sudo grep <file> /home/*/.* If any local initialization files are found to reference world-writable files, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-248628`

### Rule: OL 8 must disable kernel dumps unless needed.

**Rule ID:** `SV-248628r991562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system partition. OL 8 installation media presents the option to enable or disable the kdump service at the time of system installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that kernel core dumps are disabled unless needed with the following command: $ sudo systemctl status kdump.service kdump.service - Crash recovery kernel arming Loaded: loaded (/usr/lib/systemd/system/kdump.service; disabled; vendor preset: enabled) Active: failed (Result: exit-code)since Mon 2020-05-04 16:08:09 EDT; 3min ago Main PID: 1130 (code=exited, status=0/FAILURE) If the "kdump" service is active, ask the System Administrator if the use of the service is required and documented with the Information System Security Officer (ISSO). If the service is active and is not documented, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248629`

### Rule: OL 8 must disable the "kernel.core_pattern".

**Rule ID:** `SV-248629r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 disables storing core dumps with the following commands: $ sudo sysctl kernel.core_pattern kernel.core_pattern = |/bin/false If the returned line does not have a value of "|/bin/false", or a line is not returned and the need for core dumps is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r kernel.core_pattern /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:kernel.core_pattern = |/bin/false If "kernel.core_pattern" is not set to "|/bin/false", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248630`

### Rule: OL 8 must disable acquiring, saving, and processing core dumps.

**Rule ID:** `SV-248630r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems. When the kernel invokes "systemd-coredump" to handle a core dump, it runs in privileged mode and will connect to the socket created by the "systemd-coredump.socket" unit. This, in turn, will spawn an unprivileged "systemd-coredump@.service" instance to process the core dump.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is not configured to acquire, save, or process core dumps with the following command: $ sudo systemctl status systemd-coredump.socket systemd-coredump.socket Loaded: masked (Reason: Unit systemd-coredump.socket is masked.) Active: inactive (dead) If the "systemd-coredump.socket" is loaded and not masked and the need for core dumps is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248631`

### Rule: OL 8 must disable core dumps for all users.

**Rule ID:** `SV-248631r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables core dumps for all users with the following command: $ sudo grep -r -s '^[^#].*core' /etc/security/limits.conf /etc/security/limits.d/*.conf * hard core 0 This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains. If the "core" item is missing or commented out or the value is anything other than "0", and the need for core dumps is not documented with the Information System Security Officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248632`

### Rule: OL 8 must disable storing core dumps.

**Rule ID:** `SV-248632r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables storing core dumps for all users with the following command: $ sudo grep -i storage /etc/systemd/coredump.conf Storage=none If the "Storage" item is missing or commented out or the value is anything other than "none", and the need for core dumps is not documented with the Information System Security Officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248633`

### Rule: OL 8 must disable core dump backtraces.

**Rule ID:** `SV-248633r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables core dump backtraces by issuing the following command: $ sudo grep -i ProcessSizeMax /etc/systemd/coredump.conf ProcessSizeMax=0 If the "ProcessSizeMax" item is missing or commented out or the value is anything other than "0", and the need for core dumps is not documented with the Information System Security Officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248634`

### Rule: For OL 8 systems using Domain Name Servers (DNS) resolution, at least two name servers must be configured.

**Rule ID:** `SV-248634r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To provide availability for name resolution services, multiple redundant name servers are mandated. A failure in name resolution could lead to the failure of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the system is using local or DNS name resolution with the following command: $ sudo grep hosts /etc/nsswitch.conf hosts: files dns If the DNS entry is missing from the host's line in the "/etc/nsswitch.conf" file, the "/etc/resolv.conf" file must be empty. Verify the "/etc/resolv.conf" file is empty with the following command: $ sudo ls -al /etc/resolv.conf -rw-r--r-- 1 root root 0 Aug 19 08:31 resolv.conf If local host authentication is being used and the "/etc/resolv.conf" file is not empty, this is a finding. If the DNS entry is found on the host's line of the "/etc/nsswitch.conf" file, verify the operating system is configured to use two or more name servers for DNS resolution. Determine the name servers used by the system with the following command: $ sudo grep nameserver /etc/resolv.conf nameserver 192.168.1.2 nameserver 192.168.1.3 If fewer than two lines are returned that are not commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248635`

### Rule: Executable search paths within the initialization files of all local interactive OL 8 users must only contain paths that resolve to the system default or the user's home directory.

**Rule ID:** `SV-248635r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory (other than the user's home directory), executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is interpreted as the current working directory. If deviations from the default system search path for the local interactive user are required, they must be documented with the Information System Security Officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all local interactive user initialization files' executable search path statements do not contain statements that will reference a working directory other than the users' home directory with the following commands: Note: The example will be for the "smithj" user, which has a home directory of "/home/smithj". $ sudo grep -i path /home/smithj/.* /home/smithj/.bash_profile:PATH=$PATH:$HOME/.local/bin:$HOME/bin /home/smithj/.bash_profile:export PATH If any local interactive user initialization files have executable search path statements that include directories outside of their home directory, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248636`

### Rule: All OL 8 world-writable directories must be owned by root, sys, bin, or an application user.

**Rule ID:** `SV-248636r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a world-writable directory is not owned by root, sys, bin, or an application User Identifier (UID), unauthorized users may be able to modify files created by others. The only authorized public directories are the temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following command will discover and print world-writable directories that are not owned by a system account, given the assumption that only system accounts have a UID lower than 1000. Run it once for each local partition [PART]: $ sudo find [PART] -xdev -type d -perm -0002 -uid +999 -print If there is output, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248637`

### Rule: All OL 8 world-writable directories must be group-owned by root, sys, bin, or an application group.

**Rule ID:** `SV-248637r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a world-writable directory is not group-owned by root, sys, bin, or an application Group Identifier (GID), unauthorized users may be able to modify files created by others. The only authorized public directories are the temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following command will discover and print world-writable directories that are not group-owned by a system account, given the assumption that only system accounts have a gid lower than 1000. Run it once for each local partition [PART]: $ sudo find [PART] -xdev -type d -perm -0002 -gid +999 -print If there is output, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248638`

### Rule: All OL 8 local interactive users must have a home directory assigned in the "/etc/passwd" file.

**Rule ID:** `SV-248638r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify local interactive users on OL 8 have a home directory assigned with the following command: $ sudo pwck -r user 'lp': directory '/var/spool/lpd' does not exist user 'news': directory '/var/spool/news' does not exist user 'uucp': directory '/var/spool/uucp' does not exist user 'www-data': directory '/var/www' does not exist Ask the System Administrator (SA) if any users found without home directories are local interactive users. If the SA is unable to provide a response, check for users with a User Identifier (UID) of 1000 or greater with the following command: $ sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6}' /etc/passwd If any interactive users do not have a home directory assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248639`

### Rule: All OL 8 local interactive user home directories must have mode "0750" or less permissive.

**Rule ID:** `SV-248639r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all local interactive users has a mode of "0750" or less permissive with the following command. Note: This may miss interactive users that have been assigned a privileged User Identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. $ sudo ls -ld $(awk -F: '($3>=1000)&&($1!="nobody"){print $6}' /etc/passwd) drwxr-x--- 2 smithj admin 4096 Jun 5 12:41 smithj If home directories of interactive users referenced in "/etc/passwd" do not have a mode of "0750" or less permissive, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248640`

### Rule: All OL 8 local interactive user home directory files must have mode "0750" or less permissive.

**Rule ID:** `SV-248640r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all files and directories contained in a local interactive user home directory, excluding local initialization files, have a mode of "0750". Files that begin with a "." are excluded from this requirement. Note: The example will be for the user "smithj", who has a home directory of "/home/smithj". $ sudo ls -lLR /home/smithj -rwxr-x--- 1 smithj smithj 18 Mar 5 17:06 file1 -rwxr----- 1 smithj smithj 193 Mar 5 17:06 file2 -rw-r-x--- 1 smithj smithj 231 Mar 5 17:06 file3 If any files or directories are found with a mode more permissive than "0750", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248641`

### Rule: All OL 8 local interactive user home directories must be group-owned by the home directory owner's primary group.

**Rule ID:** `SV-248641r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of a local interactive user’s home directory is not the same as the primary GID of the user, this would allow unauthorized access to the user’s files. Users that share the same group may not be able to access files to which they legitimately should have access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all local interactive users is group-owned by that user’s primary GID with the following command. Note: This may miss local interactive users that have been assigned a privileged User Identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. The returned directory "/home/smithj" is used as an example. $ sudo ls -ld $(awk -F: '($3>=1000)&&($1!="nobody"){print $6}' /etc/passwd) drwxr-x--- 2 smithj admin 4096 Jun 5 12:41 smithj Check the user's primary group with the following command: $ sudo grep $(grep smithj /etc/passwd | awk -F: '{print $4}') /etc/group admin:x:250:smithj,jonesj,jacksons If the user home directory referenced in "/etc/passwd" is not group-owned by that user’s primary GID, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248642`

### Rule: OL 8 must be configured so that all files and directories contained in local interactive user home directories are group-owned by a group of which the home directory owner is a member.

**Rule ID:** `SV-248642r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a local interactive user's files are group-owned by a group of which the user is not a member, unintended users may be able to access them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all files and directories in a local interactive user home directory are group-owned by a group that the user is a member. Check the group owner of all files and directories in a local interactive user's home directory with the following command: Note: The example will be for the user "smithj", who has a home directory of "/home/smithj". $ sudo ls -lLR /<home directory>/<users home directory>/ -rw-r--r-- 1 smithj smithj 18 Mar 5 17:06 file1 -rw-r--r-- 1 smithj smithj 193 Mar 5 17:06 file2 -rw-r--r-- 1 smithj sa 231 Mar 5 17:06 file3 If any files found with a group-owner different from the home directory user private group, determine if the user is a member of that group with the following command: $ sudo grep smithj /etc/group sa:x:100:juan,shelley,bob,smithj smithj:x:521:smithj If any files or directories are group owned by a group that the directory owner is not a member of, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248643`

### Rule: All OL 8 local interactive user home directories defined in the "/etc/passwd" file must exist.

**Rule ID:** `SV-248643r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a local interactive user has a home directory defined that does not exist, the user may be given access to the "/" directory as the current working directory upon logon. This could create a denial of service because the user would not be able to access their logon configuration files, and it may give them visibility to system files they normally would not be able to access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the assigned home directory of all local interactive users on OL 8 exists with the following command: $ sudo ls -ld $(awk -F: '($3>=1000)&&($1!="nobody"){print $6}' /etc/passwd) drwxr-xr-x 2 smithj admin 4096 Jun 5 12:41 smithj Note: This may miss interactive users that have been assigned a privileged User ID (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. Check that all referenced home directories exist with the following command: $ sudo pwck -r user 'smithj': directory '/home/smithj' does not exist If any home directories referenced in "/etc/passwd" are returned as not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248644`

### Rule: All OL 8 local interactive user accounts must be assigned a home directory upon creation.

**Rule ID:** `SV-248644r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all local interactive users on OL 8 are assigned a home directory upon creation with the following command: $ sudo grep -i create_home /etc/login.defs CREATE_HOME yes If the value for "CREATE_HOME" parameter is not set to "yes", the line is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248645`

### Rule: All OL 8 local initialization files must have mode "0740" or less permissive.

**Rule ID:** `SV-248645r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon logon. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all local initialization files have a mode of "0740" or less permissive with the following command: Note: The example will be for the "smithj" user, who has a home directory of "/home/smithj". $ sudo ls -al /home/smithj/.* | more -rwxr----- 1 smithj users 896 Mar 10 2011 .profile -rwxr----- 1 smithj users 497 Jan 6 2007 .login -rwxr----- 1 smithj users 886 Jan 6 2007 .something If any local initialization files have a mode more permissive than "0740", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248646`

### Rule: All OL 8 files and directories must have a valid owner.

**Rule ID:** `SV-248646r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unowned files and directories may be unintentionally inherited if a user is assigned the same User Identifier "UID" as the UID of the unowned files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all files and directories on OL 8 have a valid owner with the following command: $ sudo find / -nouser If any files on the system do not have an assigned owner, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248647`

### Rule: All OL 8 files and directories must have a valid group owner.

**Rule ID:** `SV-248647r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files without a valid group owner may be unintentionally inherited if a group is assigned the same Group Identifier (GID) as the GID of the files without a valid group owner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all files and directories on OL 8 have a valid group with the following command: $ sudo find / -nogroup If any files on the system do not have an assigned group, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248648`

### Rule: A separate OL 8 filesystem must be used for user home directories (such as "/home" or an equivalent).

**Rule ID:** `SV-248648r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system has been created for non-privileged local interactive user home directories. Check the home directory assignment for all non-privileged users, users with a User Identifier (UID) greater than 1000, on the system with the following command: $ sudo awk -F: '($3>=1000)&&($1!="nobody"){print $1,$3,$6}' /etc/passwd doej 1001 /home/doej publicj 1002 /home/publicj smithj 1003 /home/smithj The output of the command will give the directory that contains the home directories for the nonprivileged users on the system (in this example, "/home") and users’ shell. All accounts with a valid shell (such as "/bin/bash") are considered interactive users. Check that a file system has been created for the nonprivileged interactive users with the following command. Note: The partition of "/home" is used in the example. $ sudo grep /home /etc/fstab /dev/mapper/... /home xfs defaults,noexec,nosuid,nodev 0 0 If a separate entry for the file system that contains the nonprivileged interactive users' home directories does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-248649`

### Rule: Unattended or automatic logon via the OL 8 graphical user interface must not be allowed.

**Rule ID:** `SV-248649r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify the operating system does not allow an unattended or automatic logon to the system via a graphical user interface. Check for the value of "AutomaticLoginEnable" in the "/etc/gdm/custom.conf" file with the following command: $ sudo grep -i automaticloginenable /etc/gdm/custom.conf AutomaticLoginEnable=false If the value of "AutomaticLoginEnable" is not set to "false", this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-248650`

### Rule: OL 8 must not allow users to override SSH environment variables.

**Rule ID:** `SV-248650r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SSH environment options potentially allow users to bypass access restriction in some configurations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that unattended or automatic login via SSH is disabled with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permituserenvironment' PermitUserEnvironment no If "PermitUserEnvironment" is set to "yes", is missing completely, or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-248651`

### Rule: OL 8 temporary user accounts must be provisioned with an expiration time of 72 hours or less.

**Rule ID:** `SV-248651r958364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, OL 8 must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. To address access requirements, many OL 8 operating systems may be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information. $ sudo chage -l system_account_name Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248652`

### Rule: OL 8 systems below version 8.2 must automatically lock an account when three unsuccessful logon attempts occur.

**Rule ID:** `SV-248652r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. OL 8 can use the "pam_faillock.so" for this purpose. Note that manual changes to the listed files may be overwritten by the "authselect" program. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system locks an account after three unsuccessful logon attempts with the following commands. Note: If the System Administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is not applicable. Note: This check applies to OL versions 8.0 and 8.1. If the system is OL version 8.2 or newer, this check is not applicable. $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "deny" option is not set to "3" or less (but not "0") on the "preauth" line with the "pam_faillock.so" module or is missing from this line, this is a finding. If any line referencing the "pam_faillock.so" module is commented out, this is a finding. $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "deny" option is not set to "3" or less (but not "0") on the "preauth" line with the "pam_faillock.so" module or is missing from this line, this is a finding. If any line referencing the "pam_faillock.so" module is commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248653`

### Rule: OL 8 systems, versions 8.2 and above, must automatically lock an account when three unsuccessful logon attempts occur.

**Rule ID:** `SV-248653r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2, the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the "pam_faillock.so" module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in "/etc/passwd" and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer. If the system is OL version 8.0 or 8.1, this check is not applicable. Verify the "/etc/security/faillock.conf" file is configured to lock an account after three unsuccessful logon attempts: $ sudo grep 'deny =' /etc/security/faillock.conf deny = 3 If the "deny" option is not set to "3" or less (but not "0") or is missing or commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248654`

### Rule: OL 8 systems below version 8.2 must automatically lock an account when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-248654r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. OL 8 can use the "pam_faillock.so" for this purpose. Note that manual changes to the listed files may be overwritten by the "authselect" program. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system locks an account after three unsuccessful logon attempts within a period of 15 minutes with the following commands. Note: If the System Administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is not applicable. Note: This check applies to OL versions 8.0 and 8.1. If the system is OL version 8.2 or newer, this check is not applicable. $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "fail_interval" option is not set to "900" or more on the "preauth" lines with the "pam_faillock.so" module or is missing from this line, this is a finding. $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "fail_interval" option is not set to "900" or more on the "preauth" lines with the "pam_faillock.so" module or is missing from this line, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248655`

### Rule: OL 8 systems, versions 8.2 and above, must automatically lock an account when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-248655r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2, the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the "pam_faillock.so" module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in "/etc/passwd" and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer. If the system is OL version 8.0 or 8.1, this check is not applicable. Verify the "/etc/security/faillock.conf" file is configured to lock an account after three unsuccessful logon attempts within 15 minutes: $ sudo grep 'fail_interval =' /etc/security/faillock.conf fail_interval = 900 If the "fail_interval" option is not set to "900" or more or is missing or commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248656`

### Rule: OL 8 systems below version 8.2 must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-248656r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. OL 8 can use the "pam_faillock.so" for this purpose. Note that manual changes to the listed files may be overwritten by the "authselect" program. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system locks an account after three unsuccessful logon attempts within a period of 15 minutes until released by an administrator with the following commands. Note: If the System Administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is not applicable. Note: This check applies to OL versions 8.0 and 8.1. If the system is OL version 8.2 or newer, this check is not applicable. $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "unlock_time" option is not set to "0" on the "preauth" and "authfail" lines with the "pam_faillock.so" module or is missing from these lines, this is a finding. $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "unlock_time" option is not set to "0" on the "preauth" and "authfail" lines with the "pam_faillock.so" module or is missing from these lines, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248657`

### Rule: OL 8 systems, versions 8.2 and above, must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-248657r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2, the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the "pam_faillock.so" module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in "/etc/passwd" and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer. If the system is OL version 8.0 or 8.1, this check is not applicable. Verify the "/etc/security/faillock.conf" file is configured to lock an account until released by an administrator after three unsuccessful logon attempts: $ sudo grep 'unlock_time =' /etc/security/faillock.conf unlock_time = 0 If the "unlock_time" option is not set to "0" or is missing or commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248658`

### Rule: OL 8 systems below version 8.2 must ensure account lockouts persist.

**Rule ID:** `SV-248658r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. OL 8 can use the "pam_faillock.so" for this purpose. Note that manual changes to the listed files may be overwritten by the "authselect" program. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the faillock directory contents persist after a reboot with the following commands: Note: If the System Administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is not applicable. Note: This check applies to OL versions 8.0 and 8.1. If the system is OL version 8.2 or newer, this check is not applicable. $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "dir" option is not set to a non-default documented tally log directory on the "preauth" and "authfail" lines with the "pam_faillock.so" module or is missing from these lines, this is a finding. $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "dir" option is not set to a non-default documented tally log directory on the "preauth" and "authfail" lines with the "pam_faillock.so" module or is missing from these lines, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248659`

### Rule: OL 8 systems, versions 8.2 and above, must ensure account lockouts persist.

**Rule ID:** `SV-248659r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2, the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the "pam_faillock.so" module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in "/etc/passwd" and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer. If the system is OL version 8.0 or 8.1, this check is not applicable. Verify the "/etc/security/faillock.conf" file is configured use a non-default faillock directory to ensure contents persist after reboot: $ sudo grep 'dir =' /etc/security/faillock.conf dir = /var/log/faillock If the "dir" option is not set to a non-default documented tally log directory or is missing or commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248660`

### Rule: OL 8 systems below version 8.2 must prevent system messages from being presented when three unsuccessful logon attempts occur.

**Rule ID:** `SV-248660r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. OL 8 can use the "pam_faillock.so" for this purpose. Note that manual changes to the listed files may be overwritten by the "authselect" program. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system prevents informative messages from being presented to the user pertaining to logon information with the following commands. Note: If the System Administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is not applicable. Note: This check applies to OL versions 8.0 and 8.1. If the system is OL version 8.2 or newer, this check is not applicable. $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "silent" option is missing from the "preauth" line with the "pam_faillock.so" module, this is a finding. $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "silent" option is missing from the "preauth" line with the "pam_faillock.so" module, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248661`

### Rule: OL 8 systems, versions 8.2 and above, must prevent system messages from being presented when three unsuccessful logon attempts occur.

**Rule ID:** `SV-248661r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2, the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the" pam_faillock.so" module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in "/etc/passwd" and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer. If the system is OL version 8.0 or 8.1, this check is not applicable. Verify the "/etc/security/faillock.conf" file is configured to prevent informative messages from being presented at logon attempts: $ sudo grep silent /etc/security/faillock.conf silent If the "silent" option is not set or is missing or commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248662`

### Rule: OL 8 systems below version 8.2 must log user name information when unsuccessful logon attempts occur.

**Rule ID:** `SV-248662r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. OL 8 can use the "pam_faillock.so" for this purpose. Note that manual changes to the listed files may be overwritten by the "authselect" program. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system logs user name information when unsuccessful logon attempts occur with the following commands. Note: If the System Administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is not applicable. Note: This check applies to OL versions 8.0 and 8.1. If the system is OL version 8.2 or newer, this check is not applicable. $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "audit" option is missing from the "preauth" line with the "pam_faillock.so" module, this is a finding. $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "audit" option is missing from the "preauth" line with the "pam_faillock.so" module, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248663`

### Rule: OL 8 systems, versions 8.2 and above, must log user name information when unsuccessful logon attempts occur.

**Rule ID:** `SV-248663r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2, the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the "pam_faillock.so" module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in "/etc/passwd" and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer. If the system is OL version 8.0 or 8.1, this check is not applicable. Verify the "/etc/security/faillock.conf" file is configured to log user name information when unsuccessful logon attempts occur: $ sudo grep audit /etc/security/faillock.conf audit If the "audit" option is not set, is missing or commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248664`

### Rule: OL 8 systems below version 8.2 must include root when automatically locking an account until the locked account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-248664r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. OL 8 can use the "pam_faillock.so" for this purpose. Note that manual changes to the listed files may be overwritten by the "authselect" program. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system includes the root account when locking an account after three unsuccessful logon attempts within a period of 15 minutes with the following commands. Note: If the System Administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is not applicable. Note: This check applies to OL versions 8.0 and 8.1. If the system is OL version 8.2 or newer, this check is not applicable. $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "even_deny_root" option is missing from the "preauth" line with the "pam_faillock.so" module, this is a finding. $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "even_deny_root" option is missing from the "preauth" line with the "pam_faillock.so" module, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248665`

### Rule: OL 8 systems, versions 8.2 and above, must include root when automatically locking an account until the locked account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-248665r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2, the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the "pam_faillock.so" module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in /etc/passwd and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer. If the system is OL version 8.0 or 8.1, this check is not applicable. Verify the "/etc/security/faillock.conf" file is configured to log user name information when unsuccessful logon attempts occur: $ sudo grep even_deny_root /etc/security/faillock.conf even_deny_root If the "even_deny_root" option is not set or is missing or commented out, this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-248666`

### Rule: OL 8 must limit the number of concurrent sessions to 10 for all accounts and/or account types.

**Rule ID:** `SV-248666r958398_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that use an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system limits the number of concurrent sessions to 10 for all accounts and/or account types by issuing the following command: $ sudo grep "maxlogins" /etc/security/limits.conf /etc/security/limits.d/*.conf * hard maxlogins 10 This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains. If the "maxlogins" item is missing or commented out, or the value is not set to "10" or less for all domains that have the "maxlogins" item assigned, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248667`

### Rule: OL 8 must configure the use of the pam_faillock.so module in the /etc/pam.d/system-auth file.

**Rule ID:** `SV-248667r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2 the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the pam_faillock.so module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in /etc/passwd and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable a different tally directory must be set with the "dir" option. The preauth argument must be used when the module is called before the modules that ask for user credentials, such as the password. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer, if the system is OL version 8.0 or 8.1, this check is not applicable. Verify the pam_faillock.so module is present in the "/etc/pam.d/system-auth" file: $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth auth required pam_faillock.so authfail account required pam_faillock.so If the pam_faillock.so module is not present in the "/etc/pam.d/system-auth" file with the "preauth" line listed before pam_unix.so, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248668`

### Rule: OL 8 must configure the use of the pam_faillock.so module in the /etc/pam.d/password-auth file.

**Rule ID:** `SV-248668r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. In OL 8.2 the "/etc/security/faillock.conf" file was incorporated to centralize the configuration of the pam_faillock.so module. Also introduced is a "local_users_only" option that will only track failed user authentication attempts for local users in /etc/passwd and ignore centralized (AD, IdM, LDAP, etc.) users to allow the centralized platform to solely manage user lockout. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable a different tally directory must be set with the "dir" option. The preauth argument must be used when the module is called before the modules that ask for user credentials, such as the password. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check applies to OL versions 8.2 or newer, if the system is OL version 8.0 or 8.1, this check is not applicable. Verify the pam_faillock.so module is present in the "/etc/pam.d/password-auth" file: $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth auth required pam_faillock.so authfail account required pam_faillock.so If the pam_faillock.so module is not present in the "/etc/pam.d/password-auth" file with the "preauth" line listed before pam_unix.so, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248669`

### Rule: OL 8 systems, versions 8.2 and above, must configure SELinux context type to allow the use of a non-default faillock tally directory.

**Rule ID:** `SV-248669r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. From "faillock.conf" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be re-enabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. SELinux, enforcing a targeted policy, will require any non-default tally directory's security context type to match the default directory's security context type. Without updating the security context type, the pam_faillock module will not write failed login attempts to the non-default tally directory. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system does not have SELinux enabled and enforcing a targeted policy, or if the pam_faillock module is not configured for use, this requirement is not applicable. Note: This check applies to OL versions 8.2 or newer. If the system is OL version 8.0 or 8.1, this check is not applicable. Verify the location of the non-default tally directory for the pam_faillock module with the following command: $ sudo grep -w dir /etc/security/faillock.conf dir = /var/log/faillock Check the security context type of the non-default tally directory with the following command: $ sudo ls -Zd /var/log/faillock unconfined_u:object_r:faillog_t:s0 /var/log/faillock If the security context type of the non-default tally directory is not "faillog_t", this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-248670`

### Rule: OL 8 systems below version 8.2 must configure SELinux context type to allow the use of a non-default faillock tally directory.

**Rule ID:** `SV-248670r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. SELinux, enforcing a targeted policy, will require any non-default tally directory's security context type to match the default directory's security context type. Without updating the security context type, the pam_faillock module will not write failed login attempts to the non-default tally directory. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system does not have SELinux enabled and enforcing a targeted policy, or if the pam_faillock module is not configured for use, this requirement is not applicable. Note: This check applies to OL versions 8.0 and 8.1. If the system is OL version 8.2 or newer, this check is not applicable. Verify the location of the non-default tally directory for the pam_faillock module with the following command: $ sudo grep -w dir /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock auth required pam_faillock.so authfail dir=/var/log/faillock Check the security context type of the non-default tally directory with the following command: $ sudo ls -Zd /var/log/faillock unconfined_u:object_r:faillog_t:s0 /var/log/faillock If the security context type of the non-default tally directory is not "faillog_t", this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-248671`

### Rule: OL 8 must enable a user session lock until that user reestablishes access using established identification and authentication procedures for graphical user sessions.

**Rule ID:** `SV-248671r1015040_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To establish acceptance of the application usage policy, a click-through banner at system logon is required. The system must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify the operating system enables a user's session lock until that user reestablishes access using established identification and authentication procedures with the following command: $ sudo gsettings get org.gnome.desktop.screensaver lock-enabled true If the setting is "false", this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-248672`

### Rule: OL 8 must initiate a session lock for graphical user interfaces when the screensaver is activated.

**Rule ID:** `SV-248672r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify the operating system initiates a session lock a for graphical user interfaces when the screensaver is activated with the following command: $ sudo gsettings get org.gnome.desktop.screensaver lock-delay uint32 5 If the "uint32" setting is missing, or is not set to "5" or less, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248673`

### Rule: OL 8 must disable the user list at logon for graphical user interfaces.

**Rule ID:** `SV-248673r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving the user list enabled is a security risk since it allows anyone with physical access to the system to enumerate known user accounts without authenticated access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify the operating system disables the user logon list for graphical user interfaces with the following command: $ sudo gsettings get org.gnome.login-screen disable-user-list true If the setting is "false", this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-248678`

### Rule: OL 8 must enable a user session lock until that user reestablishes access using established identification and authentication procedures for command line sessions.

**Rule ID:** `SV-248678r1015045_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, OL 8 needs to provide users with the ability to manually invoke a session lock so users may secure their session should the need arise for them to temporarily vacate the immediate physical vicinity. Systemd, a core component of OL 8, has a variety of dependencies needed to function. One of those packages is the Keytable files and keyboard utilities (kbd.x86_64). This package provides the "vlock" binary, a utility used to lock one or several user virtual console sessions. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 has the "vlock" package installed by running the following command: $ sudo grep vlock /usr/bin/* Binary file /usr/bin/vlock matches If "vlock" is not installed, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-248679`

### Rule: OL 8 must be able to initiate directly a session lock for all connection types using smartcard when the smartcard is removed.

**Rule ID:** `SV-248679r1015046_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock must remain in place until the user reauthenticates. No other activity aside from reauthentication must unlock the system. OL 8 includes "authselect" as a tool to configure system identity, authentication sources, and providers by selecting a specific profile. A profile is a set of files that describes the resulting system configuration. When a profile is selected, "authselect" will create the "nsswitch.conf" and "PAM" stack to use identity and authentication sources defined by the profile. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system enables a user's session lock until that user reestablishes access using established identification and authentication procedures with the following command: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. $ sudo grep -r removal-action /etc/dconf/db/* /etc/dconf/db/distro.d/20-authselect:removal-action='lock-screen' If the "removal-action='lock-screen'" setting is missing or commented out from the "dconf" database files, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-248680`

### Rule: OL 8 must automatically lock graphical user sessions after 15 minutes of inactivity.

**Rule ID:** `SV-248680r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems must be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify the operating system initiates a session lock after a 15-minute period of inactivity for graphical user interfaces with the following commands: $ sudo gsettings get org.gnome.desktop.session idle-delay uint32 900 If "idle-delay" is set to "0" or a value greater than "900", this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-248682`

### Rule: OL 8 must prevent a user from overriding the session lock-delay setting for the graphical user interface.

**Rule ID:** `SV-248682r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. Implementing session settings will have little value if a user is able to manipulate these settings from the defaults prescribed in the other requirements of this implementation guide. Locking these settings from non-privileged users is crucial to maintaining a protected baseline. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify the operating system prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ sudo grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from non-privileged user modification with the following command. Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ sudo grep -i lock-delay /etc/dconf/db/local.d/locks/* /org/gnome/desktop/screensaver/lock-delay If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-248683`

### Rule: OL 8 must prevent a user from overriding the session idle-delay setting for the graphical user interface.

**Rule ID:** `SV-248683r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. Implementing session settings will have little value if a user is able to manipulate these settings from the defaults prescribed in the other requirements of this implementation guide. Locking these settings from non-privileged users is crucial to maintaining a protected baseline. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify the operating system prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ sudo grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from non-privileged user modification with the following command. Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ sudo grep -i idle /etc/dconf/db/local.d/locks/* /org/gnome/desktop/screensaver/idle-delay If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-248684`

### Rule: OL 8 must prevent a user from overriding the session lock-enabled setting for the graphical user interface.

**Rule ID:** `SV-248684r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. Implementing session settings will have little value if a user is able to manipulate these settings from the defaults prescribed in the other requirements of this implementation guide. Locking these settings from non-privileged users is crucial to maintaining a protected baseline. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the OL 8 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify the operating system prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ sudo grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from non-privileged user modification with the following command. Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ sudo grep -i lock-enabled /etc/dconf/db/local.d/locks/* /org/gnome/desktop/screensaver/lock-enabled If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-248685`

### Rule: OL 8 must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-248685r958452_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis. There are various methods of mapping certificates to user/group accounts for OL 8. For the purposes of this requirement, the check and fix will account for Active Directory mapping. Some of the other possible methods include joining the system to a domain and using an idM server, or a local system mapping, where the system is not part of a domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the certificate of the user or group is mapped to the corresponding user or group in the "sssd.conf" file with the following command: Note: If the System Administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable. $ sudo cat /etc/sssd/sssd.conf [sssd] config_file_version = 2 services = pam, sudo, ssh domains = testing.test [pam] pam_cert_auth = True [domain/testing.test] id_provider = ldap [certmap/testing.test/rule_name] matchrule =<SAN>.*EDIPI@mil maprule = (userCertificate;binary={cert!bin}) domains = testing.test If the "certmap" section does not exist, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-248686`

### Rule: OL 8 must ensure the password complexity module is enabled in the password-auth file.

**Rule ID:** `SV-248686r982195_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Use of "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system. OL 8 uses "pwquality" as a mechanism to enforce password complexity. This is set in both of the following: /etc/pam.d/password-auth /etc/pam.d/system-auth Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000070-GPOS-00038</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system uses "pwquality" to enforce the password complexity rules. Check for the use of "pwquality" in the password-auth file with the following command: $ sudo cat /etc/pam.d/password-auth | grep pam_pwquality password requisite pam_pwquality.so If the command does not return a line containing the value "pam_pwquality.so" as shown, or the line is commented out, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-248687`

### Rule: OL 8 must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-248687r1015047_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 8 uses pwquality as a mechanism to enforce password complexity. Note that in order to require uppercase characters without degrading the "minlen" value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf". Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000070-GPOS-00038</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value for "ucredit" in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r ucredit /etc/security/pwquality.conf* /etc/security/pwquality.conf:ucredit = -1 If the value of "ucredit" is a positive number or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-248688`

### Rule: OL 8 must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-248688r1015048_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 8 uses pwquality as a mechanism to enforce password complexity. Note that in order to require lowercase characters without degrading the "minlen" value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value for "lcredit" in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r lcredit /etc/security/pwquality.conf* /etc/security/pwquality.conf:lcredit = -1 If the value of "lcredit" is a positive number or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-248689`

### Rule: OL 8 must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-248689r1015049_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 8 uses "pwquality" as a mechanism to enforce password complexity. Note that in order to require numeric characters without degrading the minlen value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value for "dcredit" in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r dcredit /etc/security/pwquality.conf* /etc/security/pwquality.conf:dcredit = -1 If the value of "dcredit" is a positive number or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-248690`

### Rule: OL 8 must require the maximum number of repeating characters of the same character class be limited to four when passwords are changed.

**Rule ID:** `SV-248690r1015050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 8 uses "pwquality" as a mechanism to enforce password complexity. The "maxclassrepeat" option sets the maximum number of allowed same consecutive characters in the same class in the new password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the value of the "maxclassrepeat" option in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r maxclassrepeat /etc/security/pwquality.conf* /etc/security/pwquality.conf:maxclassrepeat = 4 If the value of "maxclassrepeat" is set to "0", more than "4" or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-248691`

### Rule: OL 8 must require the maximum number of repeating characters be limited to three when passwords are changed.

**Rule ID:** `SV-248691r1015051_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 8 uses "pwquality" as a mechanism to enforce password complexity. The "maxrepeat" option sets the maximum number of allowed same consecutive characters in a new password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the value of the "maxrepeat" option in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r maxrepeat /etc/security/pwquality.conf* /etc/security/pwquality.conf:maxrepeat = 3 If the value of "maxrepeat" is set to more than "3" or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-248692`

### Rule: OL 8 must require the change of at least four character classes when passwords are changed.

**Rule ID:** `SV-248692r1015052_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 8 uses "pwquality" as a mechanism to enforce password complexity. The "minclass" option sets the minimum number of required classes of characters for the new password (digits, uppercase, lowercase, others).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value of the "minclass" option in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r minclass /etc/security/pwquality.conf* /etc/security/pwquality.conf:minclass = 4 If the value of "minclass" is set to less than "4" or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-248693`

### Rule: OL 8 must require the change of at least eight characters when passwords are changed.

**Rule ID:** `SV-248693r1015053_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 8 uses "pwquality" as a mechanism to enforce password complexity. The "difok" option sets the number of characters in a password that must not be present in the old password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value of the "difok" option in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r difok /etc/security/pwquality.conf* /etc/security/pwquality.conf:difok = 8 If the value of "difok" is set to less than "8" or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-248694`

### Rule: OL 8 passwords for new users or password changes must have a 24 hours/one day minimum password lifetime restriction in "/etc/shadow".

**Rule ID:** `SV-248694r1015054_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the minimum time period between password changes for each user account is one day or greater. $ sudo awk -F: '$4 < 1 {print $1 " " $4}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-248695`

### Rule: OL 8 passwords for new users or password changes must have a 24 hours/one day minimum password lifetime restriction in "/etc/login.defs".

**Rule ID:** `SV-248695r1015055_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system enforces 24 hours/one day as the minimum password lifetime for new user accounts. Check for the value of "PASS_MIN_DAYS" in "/etc/login.defs" with the following command: $ sudo grep -i pass_min_days /etc/login.defs PASS_MIN_DAYS 1 If the "PASS_MIN_DAYS" parameter value is not "1" or greater or is commented out, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-248696`

### Rule: OL 8 user account passwords must have a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-248696r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If OL 8 does not limit the lifetime of passwords and force users to change their passwords, there is the risk that OL 8 passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 enforces a 60-day maximum password lifetime for new user accounts by running the following command: $ sudo grep -i pass_max_days /etc/login.defs PASS_MAX_DAYS 60 If the "PASS_MAX_DAYS" parameter value is greater than "60", or commented out, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-248697`

### Rule: OL 8 user account passwords must be configured so that existing passwords are restricted to a 60-day maximum lifetime.

**Rule ID:** `SV-248697r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If OL 8 does not limit the lifetime of passwords and force users to change their passwords, there is the risk that OL 8 passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the maximum time period for existing passwords is restricted to 60 days with the following commands: $ sudo awk -F: '$5 > 60 {print $1 " " $5}' /etc/shadow $ sudo awk -F: '$5 <= 0 {print $1 " " $5}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-248699`

### Rule: OL 8 passwords must have a minimum of 15 characters.

**Rule ID:** `SV-248699r1015058_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to increase exponentially the time and/or resources required to compromise the password. OL 8 uses "pwquality" as a mechanism to enforce password complexity. Configurations are set in the "etc/security/pwquality.conf" file. The "minlen", sometimes noted as minimum length, acts as a "score" of complexity based on the credit components of the "pwquality" module. By setting the credit components to a negative value, not only will those components be required, but they will not count toward the total "score" of "minlen". This will enable "minlen" to require a 15-character minimum.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system enforces a minimum 15-character password length. The "minlen" option sets the minimum number of characters in a new password. Check for the value of the "minlen" option in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r minlen /etc/security/pwquality.conf* /etc/security/pwquality.conf:minlen = 15 If the command does not return a "minlen" value of 15 or greater or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-248700`

### Rule: OL 8 passwords for new users must have a minimum of 15 characters.

**Rule ID:** `SV-248700r1015059_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to increase exponentially the time and/or resources required to compromise the password. The DOD minimum password requirement is 15 characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 enforces a minimum 15-character password length for new user accounts by running the following command: $ sudo grep -i pass_min_len /etc/login.defs PASS_MIN_LEN 15 If the "PASS_MIN_LEN" parameter value is less than "15" or is commented out, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-248701`

### Rule: OL 8 duplicate User IDs (UIDs) must not exist for interactive users.

**Rule ID:** `SV-248701r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, interactive users must be identified and authenticated to prevent potential misuse and compromise of the system. Interactive users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Interactive users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000042-GPOS-00020, SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 contains no duplicate UIDs for interactive users with the following command: $ sudo awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced and the accounts listed are interactive user accounts, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-248702`

### Rule: OL 8 must implement multifactor authentication for access to interactive accounts.

**Rule ID:** `SV-248702r1015060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a Common Access Card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DOD CAC. There are various methods of implementing multifactor authentication for OL 8. Some methods include a local system multifactor account mapping or joining the system to a domain and using an idM server or Microsoft Windows Active Directory server. Any of these methods will require that the client operating system handle the multifactor authentication correctly. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 uses multifactor authentication for local access to accounts. Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is Not Applicable. Check that the "pam_cert_auth" setting is set to "true" in the "/etc/sssd/sssd.conf" file. Check that the "try_cert_auth" or "require_cert_auth" options are configured in both "/etc/pam.d/system-auth" and "/etc/pam.d/smartcard-auth" files with the following command: $ sudo grep -ir cert_auth /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf /etc/pam.d/* /etc/sssd/sssd.conf:pam_cert_auth = True /etc/pam.d/smartcard-auth:auth sufficient pam_sss.so try_cert_auth /etc/pam.d/system-auth:auth [success=done authinfo_unavail=ignore ignore=ignore default=die] pam_sss.so try_cert_auth If "pam_cert_auth" is not set to "true" in "/etc/sssd/sssd.conf", this is a finding. If "pam_sss.so" is not set to "try_cert_auth" or "require_cert_auth" in both the "/etc/pam.d/smartcard-auth" and "/etc/pam.d/system-auth" files, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-248703`

### Rule: The OL 8 system-auth file must disable access to the system for account identifiers (individuals, groups, roles, and devices) with 35 days of inactivity.

**Rule ID:** `SV-248703r1015061_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. OL 8 needs to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity by checking the account inactivity value with the following command: $ sudo grep 'inactive\|pam_unix' /etc/pam.d/system-auth | grep -w auth auth required pam_lastlog.so inactive=35 auth sufficient pam_unix.so If the pam_lastlog.so module is listed below the pam_unix.so module in the "system-auth" file, this is a finding. If the value of "inactive" is set to zero, a negative number, or is greater than 35, this is a finding. If the line is commented out or missing, ask the administrator to indicate how the system disables access for account identifiers. If there is no evidence that the system is disabling access for account identifiers after 35 days of inactivity, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-248704`

### Rule: The OL 8 password-auth file must disable access to the system for account identifiers (individuals, groups, roles, and devices) with 35 days of inactivity.

**Rule ID:** `SV-248704r1015062_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. OL 8 needs to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity by checking the account inactivity value with the following command: $ sudo grep 'inactive\|pam_unix' /etc/pam.d/password-auth | grep -w auth auth required pam_lastlog.so inactive=35 auth sufficient pam_unix.so If the pam_lastlog.so module is listed below the pam_unix.so module in the "password-auth" file, this is a finding. If the value of "inactive" is set to zero, a negative number, or is greater than 35, this is a finding. If the line is commented out or missing, ask the administrator to indicate how the system disables access for account identifiers. If there is no evidence that the system is disabling access for account identifiers after 35 days of inactivity, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248705`

### Rule: The OL 8 lastlog command must have a mode of "0750" or less permissive.

**Rule ID:** `SV-248705r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of the contents of the /var/log/lastlog file can reveal system data to attackers, thus compromising its confidentiality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "lastlog" command has a mode of "0750" or less permissive with the following command: $ sudo stat -c "%a %n" /usr/bin/lastlog 750 /usr/bin/lastlog If the "lastlog" command has a mode more permissive than "0750", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248706`

### Rule: The OL 8 lastlog command must be owned by root.

**Rule ID:** `SV-248706r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of the contents of the /var/log/lastlog file can reveal system data to attackers, thus compromising its confidentiality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "lastlog" command is owned by root with the following command: $ sudo ls -l /usr/bin/lastlog -rwxr-x---. 1 root root 21200 Nov 4 22:51 /usr/bin/lastlog If the "lastlog" command is not owned by root, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-248707`

### Rule: The OL 8 lastlog command must be group-owned by root.

**Rule ID:** `SV-248707r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of the contents of the /var/log/lastlog file can reveal system data to attackers, thus compromising its confidentiality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "lastlog" command is group-owned by root with the following command: $ sudo ls -l /usr/bin/lastlog -rwxr-x---. 1 root root 21200 Nov 4 22:51 /usr/bin/lastlog If the "lastlog" command is not group-owned by root, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-248708`

### Rule: OL 8 must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-248708r958508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary accounts are privileged or nonprivileged accounts that are established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not either manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to expoitation by unauthorized users or insider threat actors. Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements. The automatic expiration of temporary accounts may be extended as needed by the circumstances but it must not be extended indefinitely. A documented permanent account should be established for privileged users who need long-term maintenance accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information: $ sudo chage -l <temporary_account_name> | grep -i "account expires" Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-248709`

### Rule: All OL 8 passwords must contain at least one special character.

**Rule ID:** `SV-248709r1015063_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 8 uses "pwquality" as a mechanism to enforce password complexity. Note that to require special characters without degrading the "minlen" value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value for "ocredit" in "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r ocredit /etc/security/pwquality.conf* /etc/security/pwquality.conf:ocredit = -1 If the value of "ocredit" is a positive number or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-248710`

### Rule: OL 8 must prohibit the use of cached authentications after one day.

**Rule ID:** `SV-248710r958828_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable. OL 8 includes multiple options for configuring authentication, but this requirement will focus on the System Security Services Daemon (SSSD). By default, SSSD does not cache credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSSD prohibits the use of cached authentications after one day. Note: If smart card authentication is not being used on the system, this item is not applicable. Check that SSSD allows cached authentications with the following command: $ sudo grep -ir cache_credentials /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf cache_credentials = true If "cache_credentials" is set to "false" or is missing from the configuration file, this is not a finding and no further checks are required. If "cache_credentials" is set to "true", check that SSSD prohibits the use of cached authentications after one day with the following command: $ sudo grep -ir offline_credentials_expiration /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-248711`

### Rule: OL 8 must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-248711r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 allows the user to select passwords based on dictionary words, this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 prevents the use of dictionary words for passwords. Determine if the field "dictcheck" is set in the "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r dictcheck /etc/security/pwquality.conf* /etc/security/pwquality.conf:dictcheck=1 If the "dictcheck" parameter is not set to "1" or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-248712`

### Rule: OL 8 must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-248712r991588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists verifies compliance with federal standards and establishes a common security baseline across the DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example, registry settings; account, file, and directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system enforces a delay of at least four seconds between console logon prompts following a failed logon attempt with the following command: $ sudo grep -i fail_delay /etc/login.defs FAIL_DELAY 4 If the value of "FAIL_DELAY" is not set to "4" or greater or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248713`

### Rule: OL 8 must not have unnecessary accounts.

**Rule ID:** `SV-248713r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all accounts on the system are assigned to an active system, application, or user account. Obtain the list of authorized system accounts from the Information System Security Officer (ISSO). Check the system accounts on the system with the following command: $ sudo more /etc/passwd root:x:0:0:root:/root:/bin/bash bin:x:1:1:bin:/bin:/sbin/nologin daemon:x:2:2:daemon:/sbin:/sbin/nologin sync:x:5:0:sync:/sbin:/bin/sync shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown halt:x:7:0:halt:/sbin:/sbin/halt games:x:12:100:games:/usr/games:/sbin/nologin gopher:x:13:30:gopher:/var/gopher:/sbin/nologin Accounts such as "games" and "gopher" are not authorized accounts as they do not support authorized system functions. If the accounts on the system do not match the provided documentation, or accounts that do not support an authorized system function are present, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248714`

### Rule: OL 8 must not allow accounts configured with blank or null passwords.

**Rule ID:** `SV-248714r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that null passwords cannot be used, run the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permitemptypasswords' PermitEmptyPasswords no If "PermitEmptyPasswords" is set to "yes", this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248715`

### Rule: OL 8 must not allow blank or null passwords in the system-auth file.

**Rule ID:** `SV-248715r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that null passwords cannot be used, run the following command: $ sudo grep -i nullok /etc/pam.d/system-auth If output is produced, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248716`

### Rule: OL 8 must not allow blank or null passwords in the password-auth file.

**Rule ID:** `SV-248716r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that null passwords cannot be used, run the following command: $ sudo grep -i nullok /etc/pam.d/password-auth If output is produced, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248717`

### Rule: OL 8 must display the date and time of the last successful account logon upon logon.

**Rule ID:** `SV-248717r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Providing users with feedback on when account accesses last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify users are provided with feedback on when account accesses last occurred with the following command: $ sudo grep pam_lastlog /etc/pam.d/postlogin session required pam_lastlog.so showfailed If "pam_lastlog" is missing from the "/etc/pam.d/postlogin" file or the silent option is present, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248718`

### Rule: OL 8 must display the date and time of the last successful account logon upon an SSH logon.

**Rule ID:** `SV-248718r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users with feedback on when account accesses via SSH last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH provides users with feedback on when account accesses last occurred with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*printlastlog' PrintLastLog yes If the "PrintLastLog" keyword is set to "no", is missing, or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-248719`

### Rule: OL 8 default permissions must be defined in such a way that all authenticated users can read and modify only their own files.

**Rule ID:** `SV-248719r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created, they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 defines default permissions for all authenticated users in such a way that the user can read and modify only their own files with the following command: $ sudo grep -i "umask" /etc/login.defs UMASK 077 If the "UMASK" variable is set to "000", this is a finding with the severity raised to a CAT I. If the value of "UMASK" is not set to "077", "UMASK" is commented out, or "UMASK" is missing completely, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-248720`

### Rule: OL 8 must set the umask value to 077 for all local interactive user accounts.

**Rule ID:** `SV-248720r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 600 or less permissive. Although umask can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the default umask for all local interactive users is "077". Identify the locations of all local interactive user home directories by looking at the "/etc/passwd" file. Check all local interactive user initialization files for interactive users with the following command: Note: The example is for a system that is configured to create users home directories in the "/home" directory. $ sudo grep -ir ^umask /home | grep -v '.bash_history' If any local interactive user initialization files are found to have a umask statement that has a value less restrictive than "077", this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-248721`

### Rule: OL 8 must define default permissions for logon and non-logon shells.

**Rule ID:** `SV-248721r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 600 or less permissive. Although umask can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the umask default for installed shells is "077". Check for the value of the "UMASK" parameter in the "/etc/bashrc", "/etc/csh.cshrc", and "/etc/profile" files with the following command: Note: If the value of the "UMASK" parameter is set to "000" in the "/etc/bashrc", "/etc/csh.cshrc", or the "/etc/profile" files, the Severity is raised to a CAT I. $ sudo grep -i umask /etc/bashrc /etc/csh.cshrc /etc/profile /etc/bashrc: umask 077 /etc/bashrc: umask 077 /etc/csh.cshrc: umask 077 /etc/csh.cshrc: umask 077 /etc/profile: umask 077 /etc/profile: umask 077 If the value for the "UMASK" parameter is not "077", or the "UMASK" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-248722`

### Rule: The OL 8 audit system must be configured to audit the execution of privileged functions and prevent all software from executing at higher privilege levels than users executing the software.

**Rule ID:** `SV-248722r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000326-GPOS-00126, SRG-OS-000327-GPOS-00127</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 audits the execution of privileged functions. Check if OL 8 is configured to audit the execution of the "execve" system call, by running the following command: $ sudo grep execve /etc/audit/audit.rules -a always,exit -F arch=b32 -S execve -C uid!=euid -F key=execpriv -a always,exit -F arch=b64 -S execve -C uid!=euid -F key=execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F key=execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F key=execpriv If the command does not return all lines or the lines are commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248723`

### Rule: Cron logging must be implemented in OL 8.

**Rule ID:** `SV-248723r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron logging can be used to trace the successful or unsuccessful execution of cron jobs. It can also be used to spot intrusions into the use of the cron facility by unauthorized and malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "rsyslog" is configured to log cron events with the following command: Note: If another logging package is used, substitute the utility configuration file for "/etc/rsyslog.conf" or "/etc/rsyslog.d/*.conf" files. $ sudo grep cron /etc/rsyslog.conf /etc/rsyslog.d/*.conf cron.* /var/log/cron If the command does not return a response, check for cron logging all facilities by inspecting the "/etc/rsyslog.conf" or "/etc/rsyslog.d/*.conf" files. Look for the following entry: *.* /var/log/messages If "rsyslog" is not logging messages for the cron facility or all facilities, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-248724`

### Rule: The OL 8 System Administrator (SA) and Information System Security Officer (ISSO) (at a minimum) must be alerted of an audit processing failure event.

**Rule ID:** `SV-248724r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SA and ISSO (at a minimum) are notified in the event of an audit processing failure with the following command: $ sudo grep action_mail_acct /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the retuned line is commented out, ask the SA to indicate how they and the ISSO are notified of an audit process failure. If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-248725`

### Rule: The OL 8 Information System Security Officer (ISSO) and System Administrator (SA) (at a minimum) must have mail aliases to be notified of an audit processing failure.

**Rule ID:** `SV-248725r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the administrators are notified in the event of an audit processing failure. Check that the "/etc/aliases" file has a defined value for "root". $ sudo grep "postmaster:\s*root$" /etc/aliases postmaster: root If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-248726`

### Rule: The OL 8 System must take appropriate action when an audit processing failure occurs.

**Rule ID:** `SV-248726r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 takes the appropriate action when an audit processing failure occurs with the following command: $ sudo grep disk_error_action /etc/audit/auditd.conf disk_error_action = HALT If the value of the "disk_error_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-248728`

### Rule: The OL 8 audit system must take appropriate action when the audit storage volume is full.

**Rule ID:** `SV-248728r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when OL 8 is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend on the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, OL 8 must continue generating audit records if possible (automatically restarting the audit service if necessary) and overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, OL 8 must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 takes the appropriate action when the audit storage volume is full with the following command: $ sudo grep disk_full_action /etc/audit/auditd.conf disk_full_action = HALT If the value of the "disk_full_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248729`

### Rule: The OL 8 audit system must audit local events.

**Rule ID:** `SV-248729r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OL 8 Audit Daemon is configured to include local events, with the following command: $ sudo grep local_events /etc/audit/auditd.conf local_events = yes If the value of the "local_events" option is not set to "yes", or the line is commented out, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-248730`

### Rule: OL 8 must label all offloaded audit logs before sending them to the central log server.

**Rule ID:** `SV-248730r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred and their source, location, and outcome, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Enriched logging is needed to determine who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult. When audit logs are not labeled before they are sent to a central log server, the audit data will not be able to be analyzed and tied back to the correct system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OL 8 audit daemon is configured to label all offloaded audit logs with the following command: $ sudo grep "name_format" /etc/audit/auditd.conf name_format = hostname If the "name_format" option is not "hostname", "fqd", or "numeric", or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248731`

### Rule: OL 8 must resolve audit information before writing to disk.

**Rule ID:** `SV-248731r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred and their source, location, and outcome, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Enriched logging aids in making sense of who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OL 8 audit daemon is configured to resolve audit information before writing to disk, with the following command: $ sudo grep "log_format" /etc/audit/auditd.conf log_format = ENRICHED If the "log_format" option is not "ENRICHED", or the line is commented out, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-248732`

### Rule: OL 8 audit logs must have a mode of "0600" or less permissive to prevent unauthorized read access.

**Rule ID:** `SV-248732r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 8 activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs have a mode of "0600" or less permissive. Determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log file, determine if the audit log has a mode of "0600" or less permissive with the following command: $ sudo stat -c "%a %n" /var/log/audit/audit.log 600 /var/log/audit/audit.log If the audit log has a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-248733`

### Rule: OL 8 audit logs must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-248733r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 8 activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs are owned by "root". Determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log file, determine if the audit log is owned by "root" using the following command: $ sudo ls -al /var/log/audit/audit.log rw------- 2 root root 23 Jun 11 11:56 /var/log/audit/audit.log If the audit log is not owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-248734`

### Rule: OL 8 audit logs must be group-owned by root to prevent unauthorized read access.

**Rule ID:** `SV-248734r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 8 activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs are group-owned by "root". Determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log file, determine if the audit log is group-owned by "root" using the following command: $ sudo ls -al /var/log/audit/audit.log rw------- 2 root root 23 Jun 11 11:56 /var/log/audit/audit.log If the audit log is not group-owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-248735`

### Rule: The OL 8 audit log directory must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-248735r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 8 activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log directory is owned by "root" to prevent unauthorized read access. Determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Determine the owner of the audit log directory by using the output of the above command (ex: "/var/log/audit/"). Run the following command with the correct audit log directory path: $ sudo ls -ld /var/log/audit drwx------ 2 root root 23 Jun 11 11:56 /var/log/audit If the audit log directory is not owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-248736`

### Rule: The OL 8 audit log directory must be group-owned by root to prevent unauthorized read access.

**Rule ID:** `SV-248736r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 8 activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log directory is group-owned by "root" to prevent unauthorized read access. Determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Determine the group owner of the audit log directory by using the output of the above command (ex: "/var/log/audit/"). Run the following command with the correct audit log directory path: $ sudo ls -ld /var/log/audit drwx------ 2 root root 23 Jun 11 11:56 /var/log/audit If the audit log directory is not group-owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-248737`

### Rule: The OL 8 audit log directory must have a mode of 0700 or less permissive to prevent unauthorized read access.

**Rule ID:** `SV-248737r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 8 system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log directories have a mode of "0700" or less permissive by first determining where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log, determine the directory where the audit logs are stored (ex: "/var/log/audit"). Run the following command to determine the permissions for the audit log folder: $ sudo stat -c "%a %n" /var/log/audit 700 /var/log/audit If the audit log directory has a mode more permissive than "0700", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-248738`

### Rule: The OL 8 audit system must protect auditing rules from unauthorized change.

**Rule ID:** `SV-248738r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 8 system activity. In immutable mode, unauthorized users cannot execute changes to the audit system to potentially hide malicious activity and then put the audit rules back. A system reboot would be noticeable and a system administrator could then investigate the unauthorized changes. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes with the following command: $ sudo grep "^\s*[^#]" /etc/audit/audit.rules | tail -1 -e 2 If the audit system is not set to be immutable by adding the "-e 2" option to the "/etc/audit/audit.rules", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-248739`

### Rule: The OL 8 audit system must protect logon UIDs from unauthorized change.

**Rule ID:** `SV-248739r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 8 system activity. In immutable mode, unauthorized users cannot execute changes to the audit system to potentially hide malicious activity and then put the audit rules back. A system reboot would be noticeable and a system administrator could then investigate the unauthorized changes. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes to logon UIDs with the following command: $ sudo grep -i immutable /etc/audit/audit.rules --loginuid-immutable If the login UIDs are not set to be immutable by adding the "--loginuid-immutable" option to the "/etc/audit/audit.rules", this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-248740`

### Rule: OL 8 must generate audit records for all account creation events that affect "/etc/shadow".

**Rule ID:** `SV-248740r1015064_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/shadow /etc/audit/audit.rules -w /etc/shadow -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-248741`

### Rule: OL 8 must generate audit records for all account creation events that affect "/etc/security/opasswd".

**Rule ID:** `SV-248741r1015065_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/security/opasswd". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/security/opasswd /etc/audit/audit.rules -w /etc/security/opasswd -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-248742`

### Rule: OL 8 must generate audit records for all account creation events that affect "/etc/passwd".

**Rule ID:** `SV-248742r1015066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/passwd /etc/audit/audit.rules -w /etc/passwd -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-248743`

### Rule: OL 8 must generate audit records for all account creation events that affect "/etc/gshadow".

**Rule ID:** `SV-248743r1015067_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/gshadow /etc/audit/audit.rules -w /etc/gshadow -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-248744`

### Rule: OL 8 must generate audit records for all account creation events that affect "/etc/group".

**Rule ID:** `SV-248744r1015068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates audit records for all account creations events that affect "/etc/group". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/group /etc/audit/audit.rules -w /etc/group -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-248745`

### Rule: OL 8 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers".

**Rule ID:** `SV-248745r1015069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/sudoers /etc/audit/audit.rules -w /etc/sudoers -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-248746`

### Rule: OL 8 must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers.d/".

**Rule ID:** `SV-248746r1015070_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers.d/". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/sudoers.d/ /etc/audit/audit.rules -w /etc/sudoers.d/ -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248747`

### Rule: OL 8 must generate audit records for any use of the "su" command.

**Rule ID:** `SV-248747r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "su" command allows a user to run commands with a substitute user and group ID. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates audit records for any use of the "su" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw /usr/bin/su /etc/audit/audit.rules -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=unset -k privileged-priv_change If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248748`

### Rule: The OL 8 audit system must be configured to audit any use of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls.

**Rule ID:** `SV-248748r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). "Setxattr" is a system call used to set an extended attribute value. "Fsetxattr" is a system call used to set an extended attribute value. This is used to set extended attributes on a file. "Lsetxattr" is a system call used to set an extended attribute value. This is used to set extended attributes on a symbolic link. "Removexattr" is a system call that removes extended attributes. "Fremovexattr" is a system call that removes extended attributes. This is used for removal of extended attributes from a file. "Lremovexattr" is a system call that removes extended attributes. This is used for removal of extended attributes from symbolic links. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. Performance can be helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000458-GPOS-00203, SRG-OS-000462-GPOS-00206, SRG-OS-000463-GPOS-00207, SRG-OS-000466-GPOS-00210, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if OL 8 is configured to audit the execution of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls by running the following command: $ sudo grep xattr /etc/audit/audit.rules -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod If the command does not return an audit rule for "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" or any of the lines returned are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248753`

### Rule: OL 8 must generate audit records for any use of the "chage" command.

**Rule ID:** `SV-248753r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chage" command is used to change or view user password expiry information. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "chage" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chage /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-chage If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248754`

### Rule: OL 8 must generate audit records for any uses of the "chcon" command.

**Rule ID:** `SV-248754r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chcon" command is used to change file SELinux security context. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "chcon" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chcon /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=unset -k perm_chng If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248756`

### Rule: OL 8 must generate audit records for any use of the "ssh-agent" command.

**Rule ID:** `SV-248756r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "ssh-agent" is a program to hold private keys used for public key authentication. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "ssh-agent" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep ssh-agent /etc/audit/audit.rules -a always,exit -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=unset -k privileged-ssh If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248757`

### Rule: OL 8 must generate audit records for any use of the "passwd" command.

**Rule ID:** `SV-248757r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "passwd" command is used to change passwords for user accounts. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "passwd" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w passwd /etc/audit/audit.rules -a always,exit -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-passwd If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248758`

### Rule: OL 8 must generate audit records for any use of the "mount" command.

**Rule ID:** `SV-248758r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "mount" command is used to mount a filesystem. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "mount" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w /usr/bin/mount /etc/audit/audit.rules -a always,exit -F path=/usr/bin/mount -F perm=x -F auid>=1000 -F auid!=unset -k privileged-mount If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248759`

### Rule: OL 8 must generate audit records for any use of the "umount" command.

**Rule ID:** `SV-248759r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "mount" command is used to mount a filesystem. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "umount" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w /usr/bin/umount /etc/audit/audit.rules -a always,exit -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=unset -k privileged-mount If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248760`

### Rule: OL 8 must generate audit records for any use of the "mount" syscall.

**Rule ID:** `SV-248760r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "mount" command is used to mount a filesystem. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "mount" syscall by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w mount /etc/audit/audit.rules -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=unset -k privileged-mount -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=unset -k privileged-mount If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248761`

### Rule: OL 8 must generate audit records for any use of the "unix_update" command.

**Rule ID:** `SV-248761r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. "Unix_update" is a helper program for the "pam_unix" module that updates the password for a given user. It is not intended to be run directly from the command line and logs a security violation in that event. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "unix_update" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "unix_update" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248762`

### Rule: OL 8 must generate audit records for any use of the "postdrop" command.

**Rule ID:** `SV-248762r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "postdrop" command creates a file in the maildrop directory and copies its standard input to the file. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "postdrop" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "postdrop" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/postdrop -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248763`

### Rule: OL 8 must generate audit records for any use of the "postqueue" command.

**Rule ID:** `SV-248763r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "postqueue" command implements the Postfix user interface for queue management. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "postqueue" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "postqueue" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/postqueue -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-248764`

### Rule: OL 8 must generate audit records for any use of the "semanage" command.

**Rule ID:** `SV-248764r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "semanage" command is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if OL 8 is configured to audit the execution of the "semanage" command by running the following command: $ sudo grep -w semanage /etc/audit/audit.rules a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return all lines or the lines are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-248765`

### Rule: OL 8 must generate audit records for any use of the "setfiles" command.

**Rule ID:** `SV-248765r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "setfiles" command is primarily used to initialize the security context fields (extended attributes) on one or more filesystems (or parts of them). Usually it is initially run as part of the SELinux installation process (a step commonly known as labeling). When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is configured to audit the execution of the "setfiles" command by running the following command: $ sudo grep -w setfiles /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return all lines or the lines are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-248766`

### Rule: OL 8 must generate audit records for any use of the "userhelper" command.

**Rule ID:** `SV-248766r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "userhelper" command is not intended to be run interactively. "Userhelper" provides a basic interface to change a user's password, gecos information, and shell. The main difference between this program and its traditional equivalents (passwd, chfn, chsh) is that prompts are written to standard out to make it easy for a graphical user interface wrapper to interface to it as a child process. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is configured to audit the execution of the "userhelper" command by running the following command: $ sudo grep -w userhelper /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return all lines or the lines are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248767`

### Rule: OL 8 must generate audit records for any use of the "setsebool" command.

**Rule ID:** `SV-248767r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "setsebool" command sets the current state of a particular SELinux boolean or a list of booleans to a given value. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is configured to audit the execution of the "setsebool" command by running the following command: $ sudo grep -w setsebool /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return all lines or the lines are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248768`

### Rule: OL 8 must generate audit records for any use of the "unix_chkpwd" command.

**Rule ID:** `SV-248768r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "unix_chkpwd" command is a helper program for the pam_unix module that verifies the password of the current user. It also checks password and account expiration dates in shadow. It is not intended to be run directly from the command line and logs a security violation if done so. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is configured to audit the execution of the "unix_chkpwd" command by running the following command: $ sudo grep -w unix_chkpwd /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return all lines or the lines are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248769`

### Rule: OL 8 must generate audit records for any use of the "ssh-keysign" command.

**Rule ID:** `SV-248769r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "ssh-keysign" program is an SSH helper program for host-based authentication. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of "ssh-keysign" by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep ssh-keysign /etc/audit/audit.rules -a always,exit -F path=/usr/libexec/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=unset -k privileged-ssh If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248770`

### Rule: OL 8 must generate audit records for any use of the "setfacl" command.

**Rule ID:** `SV-248770r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "setfacl" command is used to set file access control lists. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "setfacl" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w setfacl /etc/audit/audit.rules -a always,exit -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=unset -k perm_chng If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248771`

### Rule: OL 8 must generate audit records for any use of the "pam_timestamp_check" command.

**Rule ID:** `SV-248771r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "pam_timestamp_check" command is used to check if the default timestamp is valid. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "pam_timestamp_check" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w pam_timestamp_check /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=unset -k privileged-pam_timestamp_check If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248772`

### Rule: OL 8 must generate audit records for any use of the "newgrp" command.

**Rule ID:** `SV-248772r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "newgrp" command is used to change the current group ID during a login session. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "newgrp" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w newgrp /etc/audit/audit.rules -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248773`

### Rule: OL 8 must generate audit records for any use of the "init_module" and "finit_module" system calls.

**Rule ID:** `SV-248773r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "init_module" and "finit_module" system calls are used to load a kernel module. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. Performance can be helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "init_module" and "finit_module" system calls by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep init_module /etc/audit/audit.rules -a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng If the command does not return an audit rule for "init_module" and "finit_module" or any of the lines returned are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248774`

### Rule: OL 8 must generate audit records for any use of the "rename", "unlink", "rmdir", "renameat", and "unlinkat" system calls.

**Rule ID:** `SV-248774r1069140_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "rename" system call will rename the specified files by replacing the first occurrence of expression in their name by replacement. The "unlink" system call deletes a name from the filesystem. If that name was the last link to a file and no processes have the file open, the file is deleted and the space it was using is made available for reuse. The "rmdir" system call removes empty directories. The "renameat" system call renames a file, moving it between directories, if required. The "unlinkat" system call operates in exactly the same way as either "unlink" or "rmdir" except for the differences described in the manual page. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. Performance can be helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is configured to generate audit records for any use of the "rename", "unlink", "rmdir", "renameat", and "unlinkat" system calls by running the following command: $ sudo grep 'rename\|unlink\|rmdir' /etc/audit/audit.rules -a always,exit -F arch=b32 -S rename,unlink,rmdir,renameat,unlinkat -F auid>=1000 -F auid!=unset -k delete -a always,exit -F arch=b64 -S rename,unlink,rmdir,renameat,unlinkat -F auid>=1000 -F auid!=unset -k delete If the command does not return an audit rule for "rename", "unlink", "rmdir", "renameat" and "unlinkat" or any of the lines returned are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248779`

### Rule: OL 8 must generate audit records for any use of the "gpasswd" command.

**Rule ID:** `SV-248779r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "gpasswd" command is used to administer "/etc/group" and "/etc/gshadow". Every group can have administrators, members, and a password. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "gpasswd" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w gpasswd /etc/audit/audit.rules -a always,exit -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-gpasswd If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248781`

### Rule: OL 8 must generate audit records for any use of the delete_module syscall.

**Rule ID:** `SV-248781r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "delete_module" command is used to unload a kernel module. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "delete_module" syscall by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "delete_module" /etc/audit/audit.rules -a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248782`

### Rule: OL 8 must generate audit records for any use of the "crontab" command.

**Rule ID:** `SV-248782r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "crontab" command is used to maintain crontab files for individual users. Crontab is the program used to install, remove, or list the tables used to drive the cron daemon. This is similar to the task scheduler used in other operating systems. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "crontab" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w crontab /etc/audit/audit.rules -a always,exit -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=unset -k privileged-crontab If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248783`

### Rule: OL 8 must generate audit records for any use of the "chsh" command.

**Rule ID:** `SV-248783r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chsh" command is used to change the login shell. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "chsh" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chsh /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248784`

### Rule: OL 8 must generate audit records for any use of the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls.

**Rule ID:** `SV-248784r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "truncate" and "ftruncate" functions are used to truncate a file to a specified length. The "creat" system call is used to open and possibly create a file or device. The "open" system call opens a file specified by a pathname. If the specified file does not exist, it may optionally be created by "open". The "openat" system call opens a file specified by a relative pathname. The "name_to_handle_at" and "open_by_handle_at" system calls split the functionality of openat into two parts: "name_to_handle_at" returns an opaque handle that corresponds to a specified file; "open_by_handle_at" opens the file corresponding to a handle returned by a previous call to "name_to_handle_at" and returns an open file descriptor. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. Performance can be helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep 'open\|truncate\|creat' /etc/audit/audit.rules -a always,exit -F arch=b32 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b32 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the output does not produce rules containing "-F exit=-EPERM", this is a finding. If the output does not produce rules containing "-F exit=-EACCES", this is a finding. If the command does not return an audit rule for "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" or any of the lines returned are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248790`

### Rule: OL 8 must generate audit records for any use of the "chown", "fchown", "fchownat", and "lchown" system calls.

**Rule ID:** `SV-248790r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chown" command is used to change file owner and group. The "fchown" system call is used to change the ownership of a file referred to by the open file descriptor. The "fchownat" system call is used to change ownership of a file relative to a directory file descriptor. The "lchown" system call is used to change the ownership of the file specified by a path, which does not dereference symbolic links. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. Performance can be helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "chown", "fchown", "fchownat", and "lchown" system calls by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep chown /etc/audit/audit.rules -a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_chng -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_chng If audit rules are not defined for "chown", "fchown", "fchownat", and "lchown" or any of the lines returned are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248791`

### Rule: OL 8 must generate audit records for any use of the "chmod", "fchmod", and "fchmodat" system calls.

**Rule ID:** `SV-248791r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chmod" system call changes the file mode bits of each given file according to mode, which can be either a symbolic representation of changes to make or an octal number representing the bit pattern for the new mode bits. The "fchmod" system call is used to change permissions of a file. The "fchmodat" system call is used to change permissions of a file relative to a directory file descriptor. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. Performance can be helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "chmod","fchmod", and "fchmodat" syscalls by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep chmod /etc/audit/audit.rules -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=unset -k perm_chng -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=unset -k perm_chng If the command does not return an audit rule for "chmod", "fchmod", and "fchmodat", or any of the lines returned are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248797`

### Rule: OL 8 must generate audit records for any use of the "sudo" command.

**Rule ID:** `SV-248797r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "sudo" command allows a permitted user to execute a command as the superuser or another user as specified by the security policy. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "sudo" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w sudo /etc/audit/audit.rules -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248798`

### Rule: OL 8 must generate audit records for any use of the "usermod" command.

**Rule ID:** `SV-248798r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "usermod" command modifies the system account files to reflect the changes that are specified on the command line. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit event for any use of the "usermod" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w usermod /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=unset -k privileged-usermod If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248799`

### Rule: OL 8 must generate audit records for any use of the "chacl" command.

**Rule ID:** `SV-248799r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chacl" command is used to change the access control list of a file or directory. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any use of the "chacl" command by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chacl /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=unset -k perm_chng If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248800`

### Rule: OL 8 must generate audit records for any use of the "kmod" command.

**Rule ID:** `SV-248800r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "kmod" command is used to control Linux Kernel modules. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which OL 8 will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is configured to audit the execution of the module management program "kmod" by running the following command: $ sudo grep "/usr/bin/kmod" /etc/audit/audit.rules -w /usr/bin/kmod -p x -k modules If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248801`

### Rule: OL 8 must generate audit records for any attempted modifications to the "faillock" log file.

**Rule ID:** `SV-248801r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which OL 8 will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions. From "Pam_Faillock man" pages: Note the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be reenabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any attempted modifications to the "faillock" file. Determine where the faillock tallies are stored with the following commands: For OL versions 8.0 and 8.1: $ sudo grep -i pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent deny=3 fail_interval=900 even_deny_root For OL versions 8.2 and newer: $ sudo grep dir /etc/security/faillock.conf dir=/var/log/faillock Using the location of the faillock log file, check that the following calls are being audited by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w faillock /etc/audit/audit.rules -w /var/log/faillock -p wa -k logins If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248802`

### Rule: OL 8 must generate audit records for any attempted modifications to the "lastlog" file.

**Rule ID:** `SV-248802r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which OL 8 will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 generates an audit record for any attempted modifications to the "lastlog" file by running the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248803`

### Rule: OL 8 must enable auditing of processes that start prior to the audit daemon.

**Rule ID:** `SV-248803r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which OL 8 will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 enables auditing of processes that start prior to the audit daemon with the following commands: $ sudo grub2-editenv list | grep audit kernelopts=root=/dev/mapper/ol-root ro crashkernel=auto resume=/dev/mapper/ol-swap rd.lvm.lv=ol/root rd.lvm.lv=ol/swap rhgb quiet fips=1 audit=1 audit_backlog_limit=8192 boot=UUID=8d171156-cd61-421c-ba41-1c021ac29e82 If the "audit" entry does not equal "1", is missing, or the line is commented out, this is a finding. Check that auditing is enabled by default to persist in kernel updates: $ sudo grep audit /etc/default/grub GRUB_CMDLINE_LINUX="audit=1" If "audit" is not set to "1", is missing or commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-248804`

### Rule: OL 8 must allocate an "audit_backlog_limit" of sufficient size to capture processes that start prior to the audit daemon.

**Rule ID:** `SV-248804r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Audit records can be generated from various components within the information system (e.g., module or policy filter). Allocating an "audit_backlog_limit" of sufficient size is critical in maintaining a stable boot process. With an insufficient limit allocated, the system is susceptible to boot failures and crashes. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 allocates a sufficient "audit_backlog_limit" to capture processes that start prior to the audit daemon with the following commands: $ sudo grub2-editenv list | grep audit kernelopts=root=/dev/mapper/ol-root ro crashkernel=auto resume=/dev/mapper/ol-swap rd.lvm.lv=ol/root rd.lvm.lv=ol/swap rhgb quiet fips=1 audit=1 audit_backlog_limit=8192 boot=UUID=8d171156-cd61-421c-ba41-1c021ac29e82 If the "audit_backlog_limit" entry does not equal "8192" or larger, is missing, or the line is commented out, this is a finding. Verify "audit_backlog_limit" is set to persist in kernel updates: $ sudo grep audit /etc/default/grub GRUB_CMDLINE_LINUX="audit_backlog_limit=8192" If "audit_backlog_limit" is not set to "8192" or larger or is missing or commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-248805`

### Rule: OL 8 must enable Linux audit logging for the USBGuard daemon.

**Rule ID:** `SV-248805r991579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 enables Linux audit logging of the USBGuard daemon with the following commands. Note: If the USBGuard daemon is not installed and enabled, this requirement is not applicable. $ sudo grep -i auditbackend /etc/usbguard/usbguard-daemon.conf AuditBackend=LinuxAudit If the "AuditBackend" entry does not equal "LinuxAudit", is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-248806`

### Rule: OL 8 must allow only the Information System Security Manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-248806r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/audit/rules.d/*.rules" and "/etc/audit/auditd.conf" file have a mode of "0640" or less permissive by using the following commands: $ sudo ls -al /etc/audit/rules.d/*.rules -rw-r----- 1 root root 1280 Feb 16 17:09 audit.rules $ sudo ls -al /etc/audit/auditd.conf -rw-r----- 1 root root 621 Sep 22 2014 auditd.conf If the "/etc/audit/rules.d/*.rules" or "/etc/audit/auditd.conf" files have a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-248807`

### Rule: OL 8 audit tools must have a mode of "0755" or less permissive.

**Rule ID:** `SV-248807r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. OL 8 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding user rights, to make access decisions regarding the access to audit tools. Audit tools include but are not limited to vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are protected from unauthorized access, deletion, or modification by checking the permissive mode. Check the octal permission of each audit tool by running the following command: $ sudo stat -c "%a %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules 755 /sbin/auditctl 755 /sbin/aureport 755 /sbin/ausearch 750 /sbin/autrace 755 /sbin/auditd 755 /sbin/rsyslogd 755 /sbin/augenrules If any of the audit tools has a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-248808`

### Rule: OL 8 audit tools must be owned by root.

**Rule ID:** `SV-248808r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. OL 8 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding user rights, to make access decisions regarding the access to audit tools. Audit tools include but are not limited to vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are owned by "root" to prevent any unauthorized access, deletion, or modification. Check the owner of each audit tool by running the following command: $ sudo stat -c "%U %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any of the audit tools are not owned by "root", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-248809`

### Rule: OL 8 audit tools must be group-owned by root.

**Rule ID:** `SV-248809r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. OL 8 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding user rights, to make access decisions regarding the access to audit tools. Audit tools include but are not limited to vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are group-owned by "root" to prevent any unauthorized access, deletion, or modification. Check the owner of each audit tool by running the following commands: $ sudo stat -c "%G %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any of the audit tools are not group-owned by "root", this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-248810`

### Rule: OL 8 must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-248810r991567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include but are not limited to vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools to provide the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is properly configured to use cryptographic mechanisms to protect the integrity of audit tools. Check the selection lines to ensure AIDE is configured to add/check with the following command: $ sudo grep -E '(\/usr\/sbin\/(audit|au|rsys))' /etc/aide.conf /usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/rsyslogd p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512 If any of the audit tools listed above do not have an appropriate selection line, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-248811`

### Rule: OL 8 must allocate audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-248811r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure OL 8 systems have a sufficient storage capacity in which to write the audit logs, OL 8 needs to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of OL 8.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 allocates audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility. Determine to which partition the audit records are being written with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition to which audit records are written (with the example being "/var/log/audit/") with the following command: $ sudo df -h /var/log/audit/ /dev/sda2 24G 10.4G 13.6G 43% /var/log/audit If the audit records are not written to a partition made specifically for audit records ("/var/log/audit" is a separate partition), determine the amount of space being used by other files in the partition with the following command: $ sudo du -sh [audit_partition] 1.8G /var/log/audit If the audit record partition is not allocated for sufficient storage capacity, this is a finding. Note: The partition size needed to capture a week of audit records is based on the activity level of the system and the total storage capacity available. Typically 10.0 GB of storage space for audit records should be sufficient.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248812`

### Rule: OL 8 must have the packages required for offloading audit logs installed.

**Rule ID:** `SV-248812r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 8 installation media provides "rsyslogd". This is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS, and DTLS protocols) provides a method to securely encrypt and offload auditing. Rsyslog provides three ways to forward message: the traditional UDP transport, which is extremely lossy but standard; the plain TCP based transport, which loses messages only during certain situations but is widely available; and the RELP transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above. Examples of each configuration follow: UDP *.* @remotesystemname TCP *.* @@remotesystemname RELP *.* :omrelp:remotesystemname:2514 Note that a port number was given as there is no standard port for RELP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system has the packages required for offloading audit logs installed with the following commands: $ sudo yum list installed rsyslog rsyslog.x86_64 8.1911.0-3.el8 @AppStream If the "rsyslog" package is not installed, ask the administrator to indicate how audit logs are being offloaded and what packages are installed to support it. If there is no evidence of audit logs being offloaded, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248813`

### Rule: OL 8 must have the packages required for encrypting offloaded audit logs installed.

**Rule ID:** `SV-248813r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 8 installation media provides "rsyslogd". This is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS and DTLS protocols) provides a method to securely encrypt and offload auditing. Rsyslog provides three ways to forward message: the traditional UDP transport, which is extremely lossy but standard; the plain TCP based transport, which loses messages only during certain situations but is widely available; and the RELP transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above. Examples of each configuration follow: UDP *.* @remotesystemname TCP *.* @@remotesystemname RELP *.* :omrelp:remotesystemname:2514 Note that a port number was given as there is no standard port for RELP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system has the packages required for encrypting offloaded audit logs installed with the following commands: $ sudo yum list installed rsyslog-gnutls rsyslog-gnutls.x86_64 8.1911.0-6.el8 @AppStream If the "rsyslog-gnutls" package is not installed, ask the administrator to indicate how audit logs are being encrypted during offloading and what packages are installed to support it. If there is no evidence of audit logs being encrypted during offloading, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-248814`

### Rule: The OL 8 audit records must be offloaded onto a different system or storage media from the system being audited.

**Rule ID:** `SV-248814r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 8 installation media provides "rsyslogd". This is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS and DTLS protocols) provides a method to securely encrypt and offload auditing. Rsyslog provides three ways to forward message: the traditional UDP transport, which is extremely lossy but standard; the plain TCP based transport, which loses messages only during certain situations but is widely available; and the RELP transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above. Examples of each configuration follow: UDP *.* @remotesystemname TCP *.* @@remotesystemname RELP *.* :omrelp:remotesystemname:2514 Note that a port number was given as there is no standard port for RELP. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system offloads audit records onto a different system or media from the system being audited with the following command: $ sudo grep @@ /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:*.* @@[logaggregationserver.example.mil]:[port] If a remote server is not configured or the line is commented out, ask the system administrator to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the audit logs are being offloaded to another system or media, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-248815`

### Rule: OL 8 must take appropriate action when the internal event queue is full.

**Rule ID:** `SV-248815r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 8 installation media provides "rsyslogd". This is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS and DTLS protocols) provides a method to securely encrypt and offload auditing. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system is configured to take an appropriate action when the internal event queue is full: $ sudo grep -i overflow_action /etc/audit/auditd.conf overflow_action = syslog If the value of the "overflow_action" option is not set to "syslog", "single", or "halt", or the line is commented out, ask the System Administrator to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the transfer of the audit logs being offloaded to another system or media takes appropriate action if the internal event queue becomes full, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-248816`

### Rule: OL 8 must encrypt the transfer of audit records offloaded onto a different system or media from the system being audited.

**Rule ID:** `SV-248816r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 8 installation media provides "rsyslogd". This is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS, and DTLS protocols) provides a method to securely encrypt and offload auditing. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system encrypts audit records offloaded onto a different system or media from the system being audited with the following commands: $ sudo grep -i '$DefaultNetstreamDriver' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$DefaultNetstreamDriver gtls If the value of the "$DefaultNetstreamDriver" option is not set to "gtls" or the line is commented out, this is a finding. $ sudo grep -i '$ActionSendStreamDriverMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$ActionSendStreamDriverMode 1 If the value of the "$ActionSendStreamDriverMode" option is not set to "1" or the line is commented out, this is a finding. If neither of the definitions above are set, ask the System Administrator to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the transfer of the audit logs being offloaded to another system or media is encrypted, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-248817`

### Rule: OL 8 must authenticate the remote logging server for offloading audit logs.

**Rule ID:** `SV-248817r1069157_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. OL 8 installation media provides "rsyslogd". This is a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS and DTLS protocols) provides a method to securely encrypt and offload auditing. "Rsyslog" supported authentication modes include the following: anon - anonymous authentication x509/fingerprint - certificate fingerprint authentication x509/certvalid - certificate validation only x509/name - certificate validation and subject name authentication Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system authenticates the remote logging server for offloading audit logs with the following command: $ sudo grep -i '$ActionSendStreamDriverAuthMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$ActionSendStreamDriverAuthMode x509/name If the value of the "$ActionSendStreamDriverAuthMode" option is not set to "x509/name" or the line is commented out, ask the system administrator to indicate how the audit logs are offloaded to a different system or media. If the variable name "StreamDriverAuthMode" is present in an omfwd statement block, this is not a finding. However, if the "StreamDriverAuthMode" variable is in a module block, this is a finding. If there is no evidence that the transfer of the audit logs being offloaded to another system or media is encrypted, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-248818`

### Rule: OL 8 must take action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-248818r1106143_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches a maximum of 75 percent utilization, they are unable to plan for audit record storage capacity expansion. The notification can be set to trigger at lower utilization thresholds at the information system security officer's (ISSO's) discretion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 takes action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following commands: $ sudo grep -w space_left /etc/audit/auditd.conf space_left = 25% If the value of the "space_left" keyword is not set to 25 percent or greater of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system is providing real-time alerts to the SA and ISSO. If the "space_left" value is not configured to the value 25 percent or more, this is a finding. If there is no evidence that real-time alerts are configured on the system, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-248819`

### Rule: OL 8 must notify the System Administrator (SA) and Information System Security Officer (ISSO) (at a minimum) when allocated audit record storage volume 75 percent utilization.

**Rule ID:** `SV-248819r971542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w space_left_action /etc/audit/auditd.conf space_left_action = email If the value of the "space_left_action" is not set to "email", or if the line is commented out, ask the System Administrator to indicate how the system is providing real-time alerts to the SA and ISSO. If there is no evidence that real-time alerts are configured on the system, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-248820`

### Rule: OL 8 must compare internal information system clocks at least every 24 hours with a server synchronized to an authoritative time source, such as the United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DOD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-248820r1038944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the operating system include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. OL 8 uses the "timedatectl" command to view the status of the "systemd-timesyncd.service". The "timedatectl" status will display the local time, UTC, and the offset from UTC. Note that USNO offers authenticated NTP service to DOD and U.S. Government agencies operating on the NIPR and SIPR networks. Visit https://www.usno.navy.mil/USNO/time/ntp/dod-customers for more information. Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000356-GPOS-00144, SRG-OS-000359-GPOS-00146</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is comparing internal information system clocks at least every 24 hours with an NTP server with the following command: $ sudo grep maxpoll /etc/chrony.conf server [ntp.server.name] iburst maxpoll 16 If the "maxpoll" option is set to a number greater than "16" or the line is commented out, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248821`

### Rule: OL 8 must disable the chrony daemon from acting as a server.

**Rule ID:** `SV-248821r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Minimizing the exposure of the server functionality of the chrony daemon diminishes the attack surface. Note that USNO offers authenticated NTP service to DOD and U.S. Government agencies operating on the NIPR and SIPR networks. Visit https://www.usno.navy.mil/USNO/time/ntp/DOD-customers for more information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system is approved and documented by the information system security officer (ISSO) to function as an NTP time server, this requirement is Not Applicable. Verify OL 8 disables the chrony daemon from acting as a server with the following command: $ sudo grep -w 'port' /etc/chrony.conf port 0 If the "port" option is not set to "0" or is commented out or missing, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248822`

### Rule: OL 8 must disable network management of the chrony daemon.

**Rule ID:** `SV-248822r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Minimizing the exposure of the server functionality of the chrony daemon diminishes the attack surface. Note that USNO offers authenticated NTP service to DOD and U.S. Government agencies operating on the NIPR and SIPR networks. Visit https://www.usno.navy.mil/USNO/time/ntp/DOD-customers for more information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system is approved and documented by the information system security officer (ISSO) to function as an NTP time server, this requirement is Not Applicable. Verify OL 8 disables network management of the chrony daemon with the following command: $ sudo grep -w 'cmdport' /etc/chrony.conf cmdport 0 If the "cmdport" option is not set to "0" or is commented out or missing, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248823`

### Rule: OL 8 must not have the telnet-server package installed.

**Rule ID:** `SV-248823r958478_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Verify the operating system is configured to disable non-essential capabilities. The most secure way of ensuring a non-essential capability is disabled is to not have the capability installed. The telnet service provides an unencrypted remote access service that does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to log on using this service, the privileged user password could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the telnet-server package is installed with the following command: $ sudo yum list installed telnet-server If the telnet-server package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248824`

### Rule: OL 8 must not have any automated bug reporting tools installed.

**Rule ID:** `SV-248824r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Verify the operating system is configured to disable non-essential capabilities. The most secure way of ensuring a non-essential capability is disabled is to not have the capability installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if any automated bug reporting packages are installed with the following command: $ sudo yum list installed abrt* If any automated bug reporting package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248825`

### Rule: OL 8 must not have the sendmail package installed.

**Rule ID:** `SV-248825r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Verify the operating system is configured to disable non-essential capabilities. The most secure way of ensuring a non-essential capability is disabled is to not have the capability installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the sendmail package is installed with the following command: $ sudo yum list installed sendmail If the sendmail package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248826`

### Rule: OL 8 must enable mitigations against processor-based vulnerabilities.

**Rule ID:** `SV-248826r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Verify the operating system is configured to disable non-essential capabilities. The most secure way of ensuring a non-essential capability is disabled is to not have the capability installed. Kernel page-table isolation is a kernel feature that mitigates the Meltdown security vulnerability and hardens the kernel against attempts to bypass kernel address space layout randomization (KASLR).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 enables kernel page-table isolation with the following commands: $ sudo grub2-editenv list | grep pti kernelopts=root=/dev/mapper/ol-root ro crashkernel=auto resume=/dev/mapper/ol-swap rd.lvm.lv=ol/root rd.lvm.lv=ol/swap rhgb quiet fips=1 audit=1 audit_backlog_limit=8192 pti=on boot=UUID=8d171156-cd61-421c-ba41-1c021ac29e82 If the "pti" entry does not equal "on", is missing, or the line is commented out, this is a finding. Check that kernel page-table isolation is enabled by default to persist in kernel updates: $ sudo grep pti /etc/default/grub GRUB_CMDLINE_LINUX="pti=on" If "pti" is not set to "on", is missing or commented out, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248827`

### Rule: OL 8 must not have the rsh-server package installed.

**Rule ID:** `SV-248827r958478_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). The rsh-server service provides an unencrypted remote access service that does not provide for the confidentiality and integrity of user passwords or the remote session and has very weak authentication. If a privileged user were to log on using this service, the privileged user password could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the rsh-server package is installed with the following command: $ sudo yum list installed rsh-server If the rsh-server package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248828`

### Rule: OL 8 must cover or disable the built-in or attached camera when not in use.

**Rule ID:** `SV-248828r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect from collaborative computing devices (i.e., cameras) can result in subsequent compromises of organizational information. Providing easy methods to physically disconnect from such devices after a collaborative computing session helps to ensure participants actually carry out the disconnect activity without having to go through complex and tedious procedures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device or operating system does not have a camera installed, this requirement is not applicable. This requirement is not applicable to mobile devices (smartphones and tablets), where the use of the camera is a local AO decision. This requirement is not applicable to dedicated VTC suites located in approved VTC locations that are centrally managed. For an external camera, if there is not a method for the operator to manually disconnect the camera at the end of collaborative computing sessions, this is a finding. For a built-in camera, the camera must be protected by a camera cover (e.g., laptop camera cover slide) when not in use. If the built-in camera is not protected with a camera cover or is not physically disabled, this is a finding. If the camera is not disconnected, covered, or physically disabled, determine if it is being disabled via software with the following commands: Verify the operating system disables the ability to load the uvcvideo kernel module. $ sudo grep -r uvcvideo /etc/modprobe.d/* | grep "/bin/false" install uvcvideo /bin/false If the command does not return any output, or the line is commented out, and the collaborative computing device has not been authorized for use, this is a finding. Verify the camera is disabled via blacklist with the following command: $ sudo grep -r uvcvideo /etc/modprobe.d/* | grep "blacklist" blacklist uvcvideo If the command does not return any output or the output is not "blacklist uvcvideo", and the collaborative computing device has not been authorized for use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248829`

### Rule: OL 8 must not have the asynchronous transfer mode (ATM) kernel module installed if not required for operational support.

**Rule ID:** `SV-248829r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ATM is a transport layer protocol designed for digital transmission of multiple types of traffic, including telephony (voice), data, and video signals, in one network without the use of separate overlay networks. Disabling ATM protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the "atm" kernel module. $ sudo grep -r atm /etc/modprobe.d/* | grep -i "/bin/false" | grep -v "^#" install atm /bin/false If the command does not return any output or the line is commented out, and use of ATM is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use ATM with the following command: $ sudo grep atm /etc/modprobe.d/* | grep -i "blacklist" | grep -v "^#" blacklist atm If the command does not return any output or the output is not "blacklist atm", and use of ATM is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248830`

### Rule: OL 8 must not have the Controller Area Network (CAN) kernel module installed if not required for operational support.

**Rule ID:** `SV-248830r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The CAN protocol is a robust vehicle bus standard designed to allow microcontrollers and devices to communicate with each other's applications without a host computer. Disabling CAN protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the "can" kernel module. $ sudo grep -r can /etc/modprobe.d/* | grep -i "/bin/false" | grep -v "^#" install can /bin/false If the command does not return any output or the line is commented out, and use of "can" is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use CAN with the following command: $ sudo grep can /etc/modprobe.d/* | grep -i "blacklist" | grep -v "^#" blacklist can If the command does not return any output or the output is not "blacklist can", and use of CAN is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248831`

### Rule: OL 8 must not have the stream control transmission protocol (SCTP) kernel module installed if not required for operational support.

**Rule ID:** `SV-248831r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SCTP is a transport layer protocol, designed to support the idea of message-oriented communication, with several streams of messages within one connection. Disabling SCTP protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the "sctp" kernel module. $ sudo grep -r sctp /etc/modprobe.d/* | grep -i "/bin/false" | grep -v "^#" install sctp /bin/false If the command does not return any output or the line is commented out, and use of SCTP is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use SCTP with the following command: $ sudo grep sctp /etc/modprobe.d/* | grep -i "blacklist" | grep -v "^#" blacklist sctp If the command does not return any output or the output is not "blacklist sctp", and use of SCTP is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248832`

### Rule: OL 8 must disable the transparent inter-process communication (TIPC) protocol.

**Rule ID:** `SV-248832r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect unused protocols can result in a system compromise. The Transparent Inter-Process Communication (TIPC) protocol is designed to provide communications between nodes in a cluster. Disabling TIPC protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the TIPC protocol kernel module. $ sudo grep -r tipc /etc/modprobe.d/* | grep "/bin/false" install tipc /bin/false If the command does not return any output, or the line is commented out, and use of the TIPC protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the TIPC protocol. Determine if the TIPC protocol is disabled with the following command: $ sudo grep -r tipc /etc/modprobe.d/* | grep "blacklist" blacklist tipc If the command does not return any output or the output is not "blacklist tipc", and use of the TIPC protocol is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248833`

### Rule: OL 8 must disable mounting of cramfs.

**Rule ID:** `SV-248833r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Removing support for unneeded filesystem types reduces the local attack surface of the server. Compressed ROM/RAM file system (or cramfs) is a read-only file system designed for simplicity and space-efficiency. It is mainly used in embedded and small-footprint systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the cramfs kernel module. $ sudo grep -ri cramfs /etc/modprobe.d/* | grep -i "/bin/false" install cramfs /bin/false If the command does not return any output, or the line is commented out, and use of the cramfs protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the cramfs kernel module. Determine if the cramfs kernel module is disabled with the following command: $ sudo grep -ri cramfs /etc/modprobe.d/* | grep -i "blacklist" blacklist cramfs If the command does not return any output or the output is not "blacklist cramfs", and use of the cramfs kernel module is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-248834`

### Rule: OL 8 must disable IEEE 1394 (FireWire) Support.

**Rule ID:** `SV-248834r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The IEEE 1394 (FireWire) is a serial bus standard for high-speed real-time communication. Disabling FireWire protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the firewire-core kernel module. $ sudo grep -ri firewire-core /etc/modprobe.d/* | grep -i "/bin/false" install firewire-core /bin/false If the command does not return any output, or the line is commented out, and use of the firewire-core protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the firewire-core kernel module. Determine if the firewire-core kernel module is disabled with the following command: $ sudo grep -ri firewire-core /etc/modprobe.d/* | grep -i "blacklist" blacklist firewire-core If the command does not return any output or the output is not "blacklist firewire-core", and use of the firewire-core kernel module is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-248835`

### Rule: OL 8 must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments.

**Rule ID:** `SV-248835r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality-of-life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the firewall configuration and running services to verify it is configured to prohibit or restrict the use of functions, ports, protocols, and/or services that are unnecessary or prohibited. Check which services are currently active with the following command: $ sudo firewall-cmd --list-all custom (active) target: DROP icmp-block-inversion: no interfaces: ens33 sources: services: dhcpv6-client dns http https ldaps rpc-bind ssh ports: masquerade: no forward-ports: icmp-blocks: rich rules: Ask the System Administrator for the site or program PPSM Component Local Service Assessment (CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-248836`

### Rule: The OL 8 file system automounter must be disabled unless required.

**Rule ID:** `SV-248836r958498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify the operating system disables the ability to automount devices. Determine if automounter service is active with the following command: $ sudo systemctl status autofs autofs.service - Automounts filesystems on demand Loaded: loaded (/usr/lib/systemd/system/autofs.service; disabled) Active: inactive (dead) If the "autofs" status is set to "active" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to automount devices. Determine if the automounter service is active with the following command: $ sudo systemctl status autofs autofs.service - Automounts filesystems on demand Loaded: loaded (/usr/lib/systemd/system/autofs.service; disabled) Active: inactive (dead) If the "autofs" status is set to "active" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-248837`

### Rule: OL 8 must be configured to disable the ability to use USB mass storage devices.

**Rule ID:** `SV-248837r986386_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB mass storage permits easy introduction of unknown devices, thereby facilitating malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the USB Storage kernel module. $ sudo grep -r usb-storage /etc/modprobe.d/* | grep -i "/bin/false" install usb-storage /bin/false If the command does not return any output, or the line is commented out, and use of USB Storage is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding. Determine if USB mass storage is disabled with the following command: $ sudo grep usb-storage /etc/modprobe.d/* | grep -i "blacklist" | grep -v "^#" /etc/modprobe.d/blacklist.conf:blacklist usb-storage If the command does not return any output or the output is not "blacklist usb-storage" and use of USB storage devices is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-248839`

### Rule: An OL 8 firewall must employ a deny-all, allow-by-exception policy for allowing connections to other systems.

**Rule ID:** `SV-248839r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to restrict network connectivity only to authorized systems permits inbound connections from malicious systems. It also permits outbound connections that may facilitate exfiltration of DoD data. OL 8 incorporates the "firewalld" daemon, which allows for many different configurations. One of these configurations is zones. Zones can be used in a deny-all, allow-by-exception approach. The default "drop" zone will drop all incoming network packets unless it is explicitly allowed by the configuration file or is related to an outgoing network connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "firewalld" is configured to employ a deny-all, allow-by-exception policy for allowing connections to other systems with the following commands: $ sudo firewall-cmd --state running $ sudo firewall-cmd --get-active-zones [custom] interfaces: ens33 $ sudo firewall-cmd --info-zone=[custom] | grep target target: DROP If no zones are active on the OL 8 interfaces or if the target is set to an option other than "DROP", this is a finding. If the "firewalld" package is not installed, ask the System Administrator if an alternate firewall (such as iptables) is installed and in use, and how is it configured to employ a deny-all, allow-by-exception policy. If the alternate firewall is not configured to employ a deny-all, allow-by-exception policy, this is a finding. If no firewall is installed, this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-248840`

### Rule: A firewall must be installed on OL 8.

**Rule ID:** `SV-248840r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"Firewalld" provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols. Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. OL 8 functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "firewalld" is installed with the following commands: $ sudo yum list installed firewalld firewalld.noarch 0.7.0-5.el8 If the "firewalld" package is not installed, ask the System Administrator if another firewall is installed. If no firewall is installed this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-248841`

### Rule: A firewall must be active on OL 8.

**Rule ID:** `SV-248841r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"Firewalld" provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols. Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. OL 8 functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "firewalld" is active with the following commands: $ sudo systemctl is-active firewalld active If the "firewalld" package is not "active", ask the System Administrator if another firewall is installed. If no firewall is installed and active this is a finding.

## Group: SRG-OS-000299-GPOS-00117

**Group ID:** `V-248842`

### Rule: OL 8 wireless network adapters must be disabled.

**Rule ID:** `SV-248842r991568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of communications with wireless peripherals, confidentiality and integrity may be compromised because unprotected communications can be intercepted and read, altered, or used to compromise the OL 8 operating system. This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with OL 8 systems. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice, and pointing devices and Near Field Communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DoD requirements for wireless data transmission and be approved for use by the Authorizing Official (AO). Although some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the OL 8 operating system. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of communications with wireless peripherals can be accomplished by physical means (e.g., employing physical barriers to wireless radio frequencies) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa. If the wireless peripheral is only passing telemetry data, encryption of the data may not be required. Satisfies: SRG-OS-000299-GPOS-00117, SRG-OS-000300-GPOS-00118, SRG-OS-000481-GPOS-000481</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no wireless interfaces configured on the system with the following command. Note: This requirement is not applicable for systems that do not have physical wireless network radios. $ sudo nmcli device status DEVICE TYPE STATE CONNECTION virbr0 bridge connected virbr0 wlp7s0 wifi connected wifiSSID enp6s0 ethernet disconnected -- p2p-dev-wlp7s0 wifi-p2p disconnected -- lo loopback unmanaged -- virbr0-nic tun unmanaged -- If a wireless interface is configured and has not been documented and approved by the Information System Security Officer (ISSO), this is a finding.

## Group: SRG-OS-000300-GPOS-00118

**Group ID:** `V-248843`

### Rule: OL 8 Bluetooth must be disabled.

**Rule ID:** `SV-248843r991569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of communications with wireless peripherals, confidentiality and integrity may be compromised because unprotected communications can be intercepted and read, altered, or used to compromise the OL 8 operating system. This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with OL 8 systems. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice, and pointing devices and Near Field Communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DoD requirements for wireless data transmission and be approved for use by the Authorizing Official (AO). Although some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the OL 8 operating system. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of communications with wireless peripherals can be accomplished by physical means (e.g., employing physical barriers to wireless radio frequencies) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa. If the wireless peripheral is only passing telemetry data, encryption of the data may not be required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device or operating system does not have a Bluetooth adapter installed, this requirement is not applicable. This requirement is not applicable to mobile devices (smartphones and tablets), where the use of Bluetooth is a local AO decision. Determine if Bluetooth is disabled with the following command: $ sudo grep -r bluetooth /etc/modprobe.d /etc/modprobe.d/bluetooth.conf:install bluetooth /bin/false If the command does not return any output or the line is commented out and the collaborative computing device has not been authorized for use, this is a finding. Verify the operating system disables the ability to use Bluetooth with the following command: $ sudo grep -r bluetooth /etc/modprobe.d | grep -i "blacklist" | grep -v "^#" blacklist bluetooth If the command does not return any output or the output is not "blacklist bluetooth", and use of Bluetooth is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248844`

### Rule: OL 8 must mount "/dev/shm" with the "nodev" option.

**Rule ID:** `SV-248844r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/dev/shm" is mounted with the "nodev" option: $ sudo mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nodev" option is configured for "/dev/shm": $ sudo cat /etc/fstab | grep /dev/shm tmpfs /dev/shm tmpfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nodev" option is missing, or if "/dev/shm" is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248845`

### Rule: OL 8 must mount "/dev/shm" with the "nosuid" option.

**Rule ID:** `SV-248845r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/dev/shm" is mounted with the "nosuid" option: $ sudo mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nosuid" option is configured for "/dev/shm": $ sudo cat /etc/fstab | grep /dev/shm tmpfs /dev/shm tmpfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nosuid" option is missing, or if "/dev/shm" is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248846`

### Rule: OL 8 must mount "/dev/shm" with the "noexec" option.

**Rule ID:** `SV-248846r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/dev/shm" is mounted with the "noexec" option: $ sudo mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "noexec" option is configured for "/dev/shm": $ sudo cat /etc/fstab | grep /dev/shm tmpfs /dev/shm tmpfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "noexec" option is missing, or if "/dev/shm" is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248847`

### Rule: OL 8 must mount "/tmp" with the "nodev" option.

**Rule ID:** `SV-248847r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/tmp" is mounted with the "nodev" option: $ sudo mount | grep /tmp /dev/mapper/ol-tmp on /tmp type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nodev" option is configured for /tmp: $ sudo cat /etc/fstab | grep /tmp /dev/mapper/ol-tmp /tmp xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nodev" option is missing, or if /tmp is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248848`

### Rule: OL 8 must mount "/tmp" with the "nosuid" option.

**Rule ID:** `SV-248848r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/tmp" is mounted with the "nosuid" option: $ sudo mount | grep /tmp /dev/mapper/ol-tmp on /tmp type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nosuid" option is configured for /tmp: $ sudo cat /etc/fstab | grep /tmp /dev/mapper/ol-tmp /tmp xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nosuid" option is missing, or if /tmp is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248849`

### Rule: OL 8 must mount "/tmp" with the "noexec" option.

**Rule ID:** `SV-248849r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/tmp" is mounted with the "noexec" option: $ sudo mount | grep /tmp /dev/mapper/ol-tmp on /tmp type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "noexec" option is configured for /tmp: $ sudo cat /etc/fstab | grep /tmp /dev/mapper/ol-tmp /tmp xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "noexec" option is missing, or if /tmp is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248850`

### Rule: OL 8 must mount "/var/log" with the "nodev" option.

**Rule ID:** `SV-248850r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log" is mounted with the "nodev" option: $ sudo mount | grep /var/log /dev/mapper/ol-var_log on /var/log type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nodev" option is configured for /var/log: $ sudo cat /etc/fstab | grep /var/log /dev/mapper/ol-var_log /var/log xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nodev" option is missing, or if /var/log is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248851`

### Rule: OL 8 must mount "/var/log" with the "nosuid" option.

**Rule ID:** `SV-248851r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log" is mounted with the "nosuid" option: $ sudo mount | grep /var/log /dev/mapper/ol-var_log on /var/log type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nosuid" option is configured for /var/log: $ sudo cat /etc/fstab | grep /var/log /dev/mapper/ol-var_log /var/log xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nosuid" option is missing, or if /var/log is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248852`

### Rule: OL 8 must mount "/var/log" with the "noexec" option.

**Rule ID:** `SV-248852r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log" is mounted with the "noexec" option: $ sudo mount | grep /var/log /dev/mapper/ol-var_log on /var/log type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "noexec" option is configured for /var/log: $ sudo cat /etc/fstab | grep /var/log /dev/mapper/ol-var_log /var/log xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "noexec" option is missing, or if /var/log is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248853`

### Rule: OL 8 must mount "/var/log/audit" with the "nodev" option.

**Rule ID:** `SV-248853r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log/audit" is mounted with the "nodev" option: $ sudo mount | grep /var/log/audit /dev/mapper/ol-var_log_audit on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nodev" option is configured for /var/log/audit: $ sudo cat /etc/fstab | grep /var/log/audit /dev/mapper/ol-var_log_audit /var/log/audit xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nodev" option is missing, or if /var/log/audit is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248854`

### Rule: OL 8 must mount "/var/log/audit" with the "nosuid" option.

**Rule ID:** `SV-248854r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log/audit" is mounted with the "nosuid" option: $ sudo mount | grep /var/log/audit /dev/mapper/ol-var_log_audit on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nosuid" option is configured for /var/log/audit: $ sudo cat /etc/fstab | grep /var/log/audit /dev/mapper/ol-var_log_audit /var/log/audit xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nosuid" option is missing, or if /var/log/audit is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248855`

### Rule: OL 8 must mount "/var/log/audit" with the "noexec" option.

**Rule ID:** `SV-248855r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log/audit" is mounted with the "noexec" option: $ sudo mount | grep /var/log/audit /dev/mapper/ol-var_log_audit on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "noexec" option is configured for /var/log/audit: $ sudo cat /etc/fstab | grep /var/log/audit /dev/mapper/ol-var_log_audit /var/log/audit xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "noexec" option is missing, or if /var/log/audit is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248856`

### Rule: OL 8 must mount "/var/tmp" with the "nodev" option.

**Rule ID:** `SV-248856r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/tmp" is mounted with the "nodev" option: $ sudo mount | grep /var/tmp /dev/mapper/ol-var_tmp on /var/tmp type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nodev" option is configured for /var/tmp: $ sudo cat /etc/fstab | grep /var/tmp /dev/mapper/ol-var_tmp /var/tmp xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nodev" option is missing, or if /var/tmp is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248857`

### Rule: OL 8 must mount "/var/tmp" with the "nosuid" option.

**Rule ID:** `SV-248857r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/tmp" is mounted with the "nosuid" option: $ sudo mount | grep /var/tmp /dev/mapper/ol-var_tmp on /var/tmp type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "nosuid" option is configured for /var/tmp: $ sudo cat /etc/fstab | grep /var/tmp /dev/mapper/ol-var_tmp /var/tmp xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "nosuid" option is missing, or if /var/tmp is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248858`

### Rule: OL 8 must mount "/var/tmp" with the "noexec" option.

**Rule ID:** `SV-248858r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access. The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/tmp" is mounted with the "noexec" option: $ sudo mount | grep /var/tmp /dev/mapper/ol-var_tmp on /var/tmp type xfs (rw,nodev,nosuid,noexec,seclabel) Verify that the "noexec" option is configured for /var/tmp: $ sudo cat /etc/fstab | grep /var/tmp /dev/mapper/ol-var_tmp /var/tmp xfs defaults,nodev,nosuid,noexec 0 0 If results are returned and the "noexec" option is missing, or if /var/tmp is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248859`

### Rule: The OL 8 "fapolicy" module must be installed.

**Rule ID:** `SV-248859r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. Using a whitelist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of whitelisted software occurs prior to execution or at system startup. Users' home directories/folders may contain information of a sensitive nature. Non-privileged users should coordinate any sharing of information with a System Administrator through shared resources. OL 8 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". This is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blacklist or whitelist processes or file access. Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system non-functional. The "fapolicyd" API is not namespace aware and can cause issues when launching or running containers. Satisfies: SRG-OS-000368-GPOS-00154, SRG-OS-000370-GPOS-00155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OL 8 "fapolicyd" is installed. Check that "fapolicyd" is installed with the following command: $ sudo yum list installed fapolicyd Installed Packages fapolicyd.x86_64 If "fapolicyd" is not installed, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248860`

### Rule: The OL 8 "fapolicy" module must be enabled.

**Rule ID:** `SV-248860r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. Using a whitelist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of whitelisted software occurs prior to execution or at system startup. Users' home directories/folders may contain information of a sensitive nature. Non-privileged users should coordinate any sharing of information with a System Administrator through shared resources. OL 8 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". This is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blacklist or whitelist processes or file access. Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system non-functional. The "fapolicyd" API is not namespace aware and can cause issues when launching or running containers. Satisfies: SRG-OS-000368-GPOS-00154, SRG-OS-000370-GPOS-00155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OL 8 "fapolicyd" is enabled and running with the following command: $ sudo systemctl status fapolicyd.service fapolicyd.service - File Access Policy Daemon Loaded: loaded (/usr/lib/systemd/system/fapolicyd.service; enabled; vendor preset: disabled) Active: active (running) If fapolicyd is not enabled and running, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-248861`

### Rule: The OL 8 fapolicy module must be configured to employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs.

**Rule ID:** `SV-248861r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. Using a whitelist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of whitelisted software occurs prior to execution or at system startup. Users' home directories/folders may contain information of a sensitive nature. Non-privileged users should coordinate any sharing of information with a System Administrator through shared resources. OL 8 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". This is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blacklist or whitelist processes or file access. Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system non-functional. The "fapolicyd" API is not namespace aware and can cause issues when launching or running containers. Satisfies: SRG-OS-000368-GPOS-00154, SRG-OS-000370-GPOS-00155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OL 8 "fapolicyd" employs a deny-all, permit-by-exception policy. Check that "fapolicyd" is in enforcement mode with the following command: $ sudo grep permissive /etc/fapolicyd/fapolicyd.conf permissive = 0 Check that fapolicyd employs a deny-all policy on system mounts with the following commands: For OL 8.4 systems and older: $ sudo tail /etc/fapolicyd/fapolicyd.rules For OL 8.5 systems and newer: $ sudo tail /etc/fapolicyd/compiled.rules allow exe=/usr/bin/python3.7 : ftype=text/x-python deny_audit perm=any pattern=ld_so : all deny perm=any all : all If fapolicyd is not running in enforcement mode with a deny-all, permit-by-exception policy, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-248862`

### Rule: OL 8 must have the USBGuard installed.

**Rule ID:** `SV-248862r986387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include but are not limited to such devices as flash drives, external storage, and printers. A new feature that OL 8 provides is the USBGuard software framework. The USBguard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the "usbguard-rules.conf" file. The policy and the authorization state of USB devices can be modified during runtime using the "usbguard" tool. The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify USBGuard is installed on the operating system with the following command: $ sudo yum list installed usbguard Installed Packages usbguard.x86_64 0.7.8-7.el8 @ol8_appstream If the USBGuard package is not installed, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-248863`

### Rule: OL 8 must block unauthorized peripherals before establishing a connection.

**Rule ID:** `SV-248863r958820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include but are not limited to such devices as flash drives, external storage, and printers. A new feature that OL 8 provides is the USBGuard software framework. The USBguard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the "usbguard-rules.conf" file. The policy and the authorization state of USB devices can be modified during runtime using the "usbguard" tool. The System Administrator (SA) must work with the site Information System Security Officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the USBGuard has a policy configured with the following command: $ sudo usbguard list-rules If the command does not return results or an error is returned, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-248864`

### Rule: OL 8 must enable the USBGuard.

**Rule ID:** `SV-248864r986388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include but are not limited to such devices as flash drives, external storage, and printers. A new feature that OL 8 provides is the USBGuard software framework. The USBguard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the "usbguard-rules.conf" file. The policy and the authorization state of USB devices can be modified during runtime using the "usbguard" tool. The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system has enabled the use of the USBGuard with the following command: $ sudo systemctl status usbguard.service usbguard.service - USBGuard daemon Loaded: loaded (/usr/lib/systemd/system/usbguard.service; enabled; vendor preset: disabled) Active: active (running) If the usbguard.service is not enabled and active, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-248865`

### Rule: A firewall must be able to protect against or limit the effects of denial-of-service (DoS) attacks by ensuring OL 8 can implement rate-limiting measures on impacted network interfaces.

**Rule ID:** `SV-248865r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of OL 8 to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exists to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. Since version 0.6.0, "firewalld" has incorporated "nftables" as its backend support. Using the limit statement in "nftables" can help to mitigate DoS attacks. Satisfies: SRG-OS-000142-GPOS-00071, SRG-OS-000298-GPOS-00116, SRG-OS-000420-GPOS-00186</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "nftables" is configured to allow rate limits on any connection to the system with the following command. Verify "firewalld" has "nftables" set as the default backend: $ sudo grep -i firewallbackend /etc/firewalld/firewalld.conf # FirewallBackend FirewallBackend=nftables If the "nftables" is not set as the "firewallbackend" default, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-248866`

### Rule: All OL 8 networked systems must have SSH installed.

**Rule ID:** `SV-248866r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH is installed with the following command: $ sudo yum list installed openssh-server openssh-server.x86_64 8.0p1-5.el8 @anaconda If the "SSH server" package is not installed, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-248867`

### Rule: All OL 8 networked systems must have and implement SSH to protect the confidentiality and integrity of transmitted and received information, as well as information during preparation for transmission.

**Rule ID:** `SV-248867r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH is loaded and active with the following command: $ sudo systemctl status sshd sshd.service - OpenSSH server daemon Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled) Active: active (running) since Tue 2015-11-17 15:17:22 EST; 4 weeks 0 days ago Main PID: 1348 (sshd) CGroup: /system.slice/sshd.service 1053 /usr/sbin/sshd -D If "sshd" does not show a status of "active" and "running", this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-248868`

### Rule: OL 8 must force a frequent session key renegotiation for SSH connections to the server.

**Rule ID:** `SV-248868r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DOD data may be compromised. Session key regeneration limits the chances of a session key becoming compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to force frequent session key renegotiation with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*rekeylimit' RekeyLimit 1G 1h If "RekeyLimit" does not have a maximum data amount and maximum time defined or is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248869`

### Rule: The x86 Ctrl-Alt-Delete key sequence must be disabled on OL 8.

**Rule ID:** `SV-248869r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user, who presses Ctrl-Alt-Delete when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of system availability due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is not configured to reboot the system when Ctrl-Alt-Delete is pressed with the following command: $ sudo systemctl status ctrl-alt-del.target | grep Loaded: Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) If the "ctrl-alt-del.target" Loaded: value is not set to "masked", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248870`

### Rule: The x86 Ctrl-Alt-Delete key sequence in OL 8 must be disabled if a graphical user interface is installed.

**Rule ID:** `SV-248870r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user, who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is not configured to reboot the system when Ctrl-Alt-Delete is pressed when using a graphical user interface with the following command: $ sudo grep logout /etc/dconf/db/local.d/* logout='' If the "logout" key is bound to an action, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248871`

### Rule: OL 8 must disable the systemd Ctrl-Alt-Delete burst key sequence.

**Rule ID:** `SV-248871r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is not configured to reboot the system when Ctrl-Alt-Delete is pressed seven times within two seconds with the following command: $ sudo grep -i ctrl /etc/systemd/system.conf CtrlAltDelBurstAction=none If the "CtrlAltDelBurstAction" is not set to "none" or is commented out or missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248872`

### Rule: OL 8 must disable the debug-shell systemd service.

**Rule ID:** `SV-248872r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The debug-shell requires no authentication and provides root privileges to anyone who has physical access to the machine. While this feature is disabled by default, masking it adds a layer of assurance that it will not be enabled via a dependency in "system". This also prevents attackers with physical access from trivially bypassing security on the machine through valid troubleshooting configurations and gaining root access when the system is rebooted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is configured to mask the "debug-shell systemd" service with the following command: $ sudo systemctl status debug-shell.service debug-shell.service Loaded: masked (Reason: Unit debug-shell.service is masked.) Active: inactive (dead) If the "debug-shell.service" is loaded and not masked, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248873`

### Rule: The Trivial File Transfer Protocol (TFTP) server package must not be installed if not required for OL 8 operational support.

**Rule ID:** `SV-248873r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If TFTP is required for operational support (such as the transmission of router configurations) its use must be documented with the Information System Security Officer (ISSO), restricted to only authorized personnel, and have access control rules established.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a TFTP server has not been installed on the system with the following command: $ sudo yum list installed tftp-server tftp-server.x86_64 5.2-24.el8 If TFTP is installed and the requirement for TFTP is not documented with the ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248874`

### Rule: The root account must be the only account having unrestricted access to the OL 8 system.

**Rule ID:** `SV-248874r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account other than root also has a User Identifier (UID) of "0", it has root authority, giving that account unrestricted access to the entire operating system. Multiple accounts with a UID of "0" afford an opportunity for potential intruders to guess a password for a privileged account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for duplicate UID "0" assignments with the following command: $ sudo awk -F: '$3 == 0 {print $1}' /etc/passwd If any accounts other than root have a UID of "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248875`

### Rule: OL 8 must prevent IPv4 Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-248875r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 will not accept IPv4 ICMP redirect messages. Check the value of the default "accept_redirects" variables with the following command: $ sudo sysctl net.ipv4.conf.default.accept_redirects net.ipv4.conf.default.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv4.conf.default.accept_redirects /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.conf.default.accept_redirects = 0 If "net.ipv4.conf.default.accept_redirects" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248876`

### Rule: OL 8 must prevent IPv6 Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-248876r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 will not accept IPv6 ICMP redirect messages. Note: IPv6 is disabled on the system, this requirement is Not Applicable. Check the value of the default "accept_redirects" variables with the following command: $ sudo sysctl net.ipv6.conf.default.accept_redirects net.ipv6.conf.default.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv6.conf.default.accept_redirects /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv6.conf.default.accept_redirects = 0 If "net.ipv6.conf.default.accept_redirects" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248877`

### Rule: OL 8 must not send Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-248877r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology. There are notable differences between Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). There is only a directive to disable sending of IPv4 redirected packets. Refer to RFC4294 for an explanation of "IPv6 Node Requirements", which resulted in this difference between IPv4 and IPv6. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not send IPv4 ICMP redirect messages. Check the value of the "all send_redirects" variables with the following command: $ sudo sysctl net.ipv4.conf.all.send_redirects net.ipv4.conf.all.send_redirects = 0 If the returned line does not have a value of "0" or a line is not returned, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv4.conf.all.send_redirects /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.conf.all.send_redirects = 0 If "net.ipv4.conf.all.send_redirects" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248878`

### Rule: OL 8 must not respond to Internet Control Message Protocol (ICMP) echoes sent to a broadcast address.

**Rule ID:** `SV-248878r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast ICMP echoes facilitates network mapping and provides a vector for amplification attacks. There are notable differences between Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). IPv6 does not implement the same method of broadcast as IPv4. Instead, IPv6 uses multicast addressing to the all-hosts multicast group. Refer to RFC4294 for an explanation of "IPv6 Node Requirements", which resulted in this difference between IPv4 and IPv6. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not respond to ICMP echoes sent to a broadcast address. Check the value of the "icmp_echo_ignore_broadcasts" variable with the following command: $ sudo sysctl net.ipv4.icmp_echo_ignore_broadcasts net.ipv4.icmp_echo_ignore_broadcasts = 1 If the returned line does not have a value of "1", a line is not returned, or the retuned line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv4.icmp_echo_ignore_broadcasts /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.icmp_echo_ignore_broadcasts = 1 If "net.ipv4.icmp_echo_ignore_broadcasts" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248879`

### Rule: OL 8 must not forward IPv4 source-routed packets.

**Rule ID:** `SV-248879r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not accept IPv4 source-routed packets. Check the value of the accept source route variable with the following command: $ sudo sysctl net.ipv4.conf.all.accept_source_route net.ipv4.conf.all.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv4.conf.all.accept_source_route /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.conf.all.accept_source_route = 0 If "net.ipv4.conf.all.accept_source_route" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248880`

### Rule: OL 8 must not forward IPv6 source-routed packets.

**Rule ID:** `SV-248880r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not accept IPv6 source-routed packets. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check the value of the accept source route variable with the following command: $ sudo sysctl net.ipv6.conf.all.accept_source_route net.ipv6.conf.all.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv6.conf.all.accept_source_route /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv6.conf.all.accept_source_route = 0 If "net.ipv6.conf.all.accept_source_route" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248881`

### Rule: OL 8 must not forward IPv4 source-routed packets by default.

**Rule ID:** `SV-248881r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not accept IPv4 source-routed packets by default. Check the value of the accept source route variable with the following command: $ sudo sysctl net.ipv4.conf.default.accept_source_route net.ipv4.conf.default.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv4.conf.default.accept_source_route /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.conf.default.accept_source_route = 0 If "net.ipv4.conf.default.accept_source_route" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248882`

### Rule: OL 8 must not forward IPv6 source-routed packets by default.

**Rule ID:** `SV-248882r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not accept IPv6 source-routed packets by default. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check the value of the accept source route variable with the following command: $ sudo sysctl net.ipv6.conf.default.accept_source_route net.ipv6.conf.default.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv6.conf.default.accept_source_route /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv6.conf.default.accept_source_route = 0 If "net.ipv6.conf.default.accept_source_route" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248883`

### Rule: OL 8 must not enable IPv6 packet forwarding unless the system is a router.

**Rule ID:** `SV-248883r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is not performing IPv6 packet forwarding unless the system is a router. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Determine if IPv6 forwarding is disabled using the following commands: $ sudo sysctl net.ipv6.conf.all.forwarding net.ipv6.conf.all.forwarding = 0 If the IPv6 forwarding value is "1" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv6.conf.all.forwarding /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv6.conf.all.forwarding = 0 If "net.ipv6.conf.all.forwarding" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248884`

### Rule: OL 8 must not accept router advertisements on all IPv6 interfaces.

**Rule ID:** `SV-248884r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network. An illicit router advertisement message could result in a man-in-the-middle attack. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not accept router advertisements on all IPv6 interfaces unless the system is a router. Note: If IPv6 is disabled on the system, this requirement is not applicable. Determine if router advertisements are not accepted by using the following command: $ sudo sysctl net.ipv6.conf.all.accept_ra net.ipv6.conf.all.accept_ra = 0 If the "accept_ra" value is not "0" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv6.conf.all.accept_ra /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv6.conf.all.accept_ra = 0 If "net.ipv6.conf.all.accept_ra" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248885`

### Rule: OL 8 must not accept router advertisements on all IPv6 interfaces by default.

**Rule ID:** `SV-248885r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network. An illicit router advertisement message could result in a man-in-the-middle attack. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not accept router advertisements on all IPv6 interfaces by default, unless the system is a router. Note: If IPv6 is disabled on the system, this requirement is not applicable. Determine if router advertisements are not accepted by using the following command: $ sudo sysctl net.ipv6.conf.default.accept_ra net.ipv6.conf.default.accept_ra = 0 If the "accept_ra" value is not "0" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv6.conf.default.accept_ra /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv6.conf.default.accept_ra = 0 If "net.ipv6.conf.default.accept_ra" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248886`

### Rule: OL 8 must not allow interfaces to perform Internet Control Message Protocol (ICMP) redirects by default.

**Rule ID:** `SV-248886r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology. There are notable differences between Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). There is only a directive to disable sending of IPv4 redirected packets. Refer to RFC4294 for an explanation of "IPv6 Node Requirements", which resulted in this difference between IPv4 and IPv6. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 does not allow interfaces to perform Internet Protocol version 4 (IPv4) ICMP redirects by default. Check the value of the "default send_redirects" variables with the following command: $ sudo sysctl net.ipv4.conf.default.send_redirects net.ipv4.conf.default.send_redirects=0 If the returned line does not have a value of "0" or a line is not returned, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv4.conf.default.send_redirects /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.conf.default.send_redirects = 0 If "net.ipv4.conf.default.send_redirects" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248887`

### Rule: OL 8 must ignore IPv4 Internet Control Message Protocol (ICMP) redirect messages.

**Rule ID:** `SV-248887r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 ignores IPv4 ICMP redirect messages. Check the value of the "accept_redirects" variables with the following command: $ sudo sysctl net.ipv4.conf.all.accept_redirects net.ipv4.conf.all.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv4.conf.all.accept_redirects /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.conf.all.accept_redirects = 0 If "net.ipv4.conf.all.accept_redirects" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248888`

### Rule: OL 8 must ignore IPv6 Internet Control Message Protocol (ICMP) redirect messages.

**Rule ID:** `SV-248888r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 ignores IPv6 ICMP redirect messages. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check the value of the "accept_redirects" variables with the following command: $ sudo sysctl net.ipv6.conf.all.accept_redirects net.ipv6.conf.all.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv6.conf.all.accept_redirects /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv6.conf.all.accept_redirects = 0 If "net.ipv6.conf.all.accept_redirects" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248889`

### Rule: OL 8 must disable access to the network "bpf" syscall from unprivileged processes.

**Rule ID:** `SV-248889r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 prevents privilege escalation through the kernel by disabling access to the "bpf" syscall with the following commands: $ sudo sysctl kernel.unprivileged_bpf_disabled kernel.unprivileged_bpf_disabled = 1 If the returned line does not have a value of "1" or a line is not returned, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r kernel.unprivileged_bpf_disabled /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: kernel.unprivileged_bpf_disabled = 1 If "kernel.unprivileged_bpf_disabled" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248890`

### Rule: OL 8 must restrict the use of "ptrace" to descendant processes.

**Rule ID:** `SV-248890r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 restricts the use of "ptrace" to descendant processes with the following commands: $ sudo sysctl kernel.yama.ptrace_scope kernel.yama.ptrace_scope = 1 If the returned line does not have a value of "1" or a line is not returned, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r kernel.yama.ptrace_scope /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: kernel.yama.ptrace_scope = 1 If "kernel.yama.ptrace_scope" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248891`

### Rule: OL 8 must restrict exposed kernel pointer addresses access.

**Rule ID:** `SV-248891r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 restricts exposed kernel pointer addresses access with the following commands: $ sudo sysctl kernel.kptr_restrict kernel.kptr_restrict = 1 If the returned line does not have a value of "1" or "2" or a line is not returned, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r kernel.kptr_restrict /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: kernel.kptr_restrict = 1 If "kernel.kptr_restrict" is not set to "1" or "2", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248892`

### Rule: OL 8 must disable the use of user namespaces.

**Rule ID:** `SV-248892r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. User namespaces are used primarily for Linux containers. "Rootful" containers run with root privileges on the host system and may pose a security risk if compromised. "Rootless" containers run without root privileges and allow for better isolation from the host system. The value "0" disallows the use of user namespaces. When containers are not in use, namespaces should be disallowed. When privileged user namespaces or "rootful" containers are in use, user namespaces should be disallowed. When unprivileged user namespaces or "rootless" containers are deployed on a system, the value should be set to a large non-zero value. The default value depends on the amount of memory in the system, approximately the total memory in kilobytes divided by 256. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 disables the use of user namespaces with the following commands. Note: If unprivileged user namespaces or "rootless" containers are in use, this requirement is not applicable. $ sudo sysctl user.max_user_namespaces user.max_user_namespaces = 0 If the returned line does not have a value of "0" or a line is not returned, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r user.max_user_namespaces /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: user.max_user_namespaces = 0 If "user.max_user_namespaces" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248893`

### Rule: OL 8 must use reverse path filtering on all IPv4 interfaces.

**Rule ID:** `SV-248893r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Enabling reverse path filtering drops packets with source addresses that are not routable. There is no equivalent filter for IPv6 traffic. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 uses reverse path filtering on all IPv4 interfaces with the following commands: $ sudo sysctl net.ipv4.conf.all.rp_filter net.ipv4.conf.all.rp_filter = 1 If the returned line does not have a value of "1" or "2" or a line is not returned, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.ipv4.conf.all.rp_filter /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.conf.all.rp_filter = 1 If "net.ipv4.conf.all.rp_filter" is not set to "1" or "2", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248894`

### Rule: OL 8 must enable hardening for the Berkeley Packet Filter Just-in-time compiler.

**Rule ID:** `SV-248894r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Enabling hardening for the Berkeley Packet Filter (BPF) Just-in-time (JIT) compiler aids in mitigating JIT spraying attacks. Setting the value to "2" enables JIT hardening for all users. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 enables hardening for the BPF JIT with the following commands: $ sudo sysctl net.core.bpf_jit_harden net.core.bpf_jit_harden = 2 If the returned line does not have a value of "2", or a line is not returned, this is a finding. Check that the configuration files are present to enable this network parameter. $ sudo grep -r net.core.bpf_jit_harden /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.core.bpf_jit_harden = 2 If "net.core.bpf_jit_harden" is not set to "2", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248895`

### Rule: OL 8 must be configured to prevent unrestricted mail relaying.

**Rule ID:** `SV-248895r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unrestricted mail relaying is permitted, unauthorized senders could use this host as a mail relay to send spam or for other unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is configured to prevent unrestricted mail relaying. Determine if "postfix" is installed with the following commands: $ sudo yum list installed postfix postfix.x86_64 2:3.3.1-9.el8 If postfix is not installed, this is not applicable. If postfix is installed, determine if it is configured to reject connections from unknown or untrusted networks with the following command: $ sudo postconf -n smtpd_client_restrictions smtpd_client_restrictions = permit_mynetworks, reject If the "smtpd_client_restrictions" parameter contains any entries other than "permit_mynetworks" and "reject", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248896`

### Rule: The OL 8 file integrity tool must be configured to verify extended attributes.

**Rule ID:** `SV-248896r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Extended attributes in file systems are used to contain arbitrary data and file metadata with security implications. OL 8 installation media come with a file integrity tool, Advanced Intrusion Detection Environment (AIDE).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the file integrity tool is configured to verify extended attributes. If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. Note: AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory. Use the following command to determine if the file is in another location: $ sudo find / -name aide.conf Check the "aide.conf" file to determine if the "xattrs" rule has been added to the rule list being applied to the files and directories selection lists. An example rule that includes the "xattrs" rule follows: All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux /bin All # apply the custom rule to the files in bin /sbin All # apply the same custom rule to the files in sbin If the "xattrs" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or extended attributes are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248897`

### Rule: The OL 8 file integrity tool must be configured to verify Access Control Lists (ACLs).

**Rule ID:** `SV-248897r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>ACLs can provide permissions beyond those permitted through the file mode and must be verified by file integrity tools. OL 8 installation media come with a file integrity tool, Advanced Intrusion Detection Environment (AIDE).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the file integrity tool is configured to verify ACLs. Use the following command to determine if the file is in a location other than "/etc/aide/aide.conf": $ sudo find / -name aide.conf Check the "aide.conf" file to determine if the "acl" rule has been added to the rule list being applied to the files and directories selection lists with the following command: $ sudo grep -E "[+]?acl" /etc/aide.conf VarFile = OwnerMode+n+l+X+acl If the "acl" rule is not being used on all selection lines in the "/etc/aide.conf" file or is commented out, or ACLs are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248898`

### Rule: The graphical display manager must not be installed on OL 8 unless approved.

**Rule ID:** `SV-248898r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet services that are not required for system or application processes must not be active to decrease the attack surface of the system. X Windows has a long history of security vulnerabilities and will not be used unless approved and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that if the system has a display server installed, it is authorized. Check for the display server package with the following example command: $ sudo rpm -qa | grep xorg | grep server Ask the System Administrator if use of the display server is an operational requirement. If the use of a display server on the system is not documented with the Information System Security Officer (ISSO), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248899`

### Rule: OL 8 network interfaces must not be in promiscuous mode.

**Rule ID:** `SV-248899r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network interfaces in promiscuous mode allow for the capture of all network traffic visible to the system. If unauthorized individuals can access these applications, it may allow them to collect information such as logon IDs, passwords, and key exchanges between systems. If the system is being used to perform a network troubleshooting function, the use of these tools must be documented with the Information System Security Officer (ISSO) and restricted to only authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify network interfaces are not in promiscuous mode unless approved by the ISSO and documented. Check for the status with the following command: $ sudo ip link | grep -i promisc If network interfaces are found on the system in promiscuous mode and their use has not been approved by the ISSO and documented, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248900`

### Rule: OL 8 remote X connections for interactive users must be disabled unless to fulfill documented and validated mission requirements.

**Rule ID:** `SV-248900r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security risk of using X11 forwarding is that the client's X11 display server may be exposed to attack when the SSH client requests forwarding. A System Administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a "no" setting. X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user's X11 authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring if the "ForwardX11Trusted" option is also enabled. If X11 services are not required for the system's intended function, they should be disabled or restricted as appropriate to the system’s needs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "X11Forwarding" is disabled with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11forwarding' X11Forwarding no If the "X11Forwarding" keyword is set to "yes" and is not documented with the information system security officer (ISSO) as an operational requirement or is missing, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248901`

### Rule: The OL 8 SSH daemon must prevent remote hosts from connecting to the proxy display.

**Rule ID:** `SV-248901r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the sshd proxy display is configured to listen on the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the DISPLAY environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OL 8 SSH daemon prevents remote hosts from connecting to the proxy display. Check the SSH "X11UseLocalhost" setting with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11uselocalhost' X11UseLocalhost yes If the "X11UseLocalhost" keyword is set to "no", is missing, or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248902`

### Rule: If the Trivial File Transfer Protocol (TFTP) server is required, the OL 8 TFTP daemon must be configured to operate in secure mode.

**Rule ID:** `SV-248902r1106146_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting TFTP to a specific directory prevents remote users from copying, transferring, or overwriting system files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If TFTP is not required, it must not be installed. If TFTP is not installed, this rule is not applicable. Check to see if TFTP server is installed with the following command: $ sudo dnf list installed | grep tftp-server tftp-server.x86_64 x.x-x.el8 Verify the TFTP daemon, if tftp.server is installed, is configured to operate in secure mode with the following command: $ grep -i execstart /usr/lib/systemd/system/tftp.service ExecStart=/usr/sbin/in.tftpd -s /var/lib/tftpboot Note: The "-s" option ensures the TFTP server only serves files from the specified directory, which is a security measure to prevent unauthorized access to other parts of the file system.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248903`

### Rule: A File Transfer Protocol (FTP) server package must not be installed unless mission essential on OL 8.

**Rule ID:** `SV-248903r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The FTP service provides an unencrypted remote access that does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to log on using this service, the privileged user password could be compromised. SSH or other encrypted file transfer methods must be used in place of this service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an FTP server has not been installed on the system with the following commands: $ sudo yum list installed | grep ftpd vsftpd-3.0.3.el8.x86_64.rpm If an FTP server is installed and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248904`

### Rule: OL 8 must not have the "gssproxy" package installed if not required for operational support.

**Rule ID:** `SV-248904r1069143_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify the operating system is configured to disable nonessential capabilities. The most secure way of ensuring a nonessential capability is disabled is to not have the capability installed. When an application uses Generic Security Services API (GSSAPI), typically it will have direct access to its security credentials, and all cryptographic operations are performed in the application's process. This is undesirable, but "gssproxy" can help in almost all use cases. It provides privilege separation to applications using the GSSAPI: The gssproxy daemon runs on the system, holds the application's credentials, and performs operations on behalf of the application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Oracle Linux systems, if there is an operational need for gssproxy to be installed, this requirement is Not Applicable. Determine if the "gssproxy" package is installed with the following command: $ sudo yum list installed gssproxy If the "gssproxy" package is installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248905`

### Rule: OL 8 must not have the "iprutils" package installed if not required for operational support.

**Rule ID:** `SV-248905r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "iprutils" package provides a suite of utilities to manage and configure IBM Power Linux RAID Adapters supported by the IPR SCSI storage device driver. Disabling the "iprutils" package protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the "iprutils" package is installed with the following command: $ sudo yum list installed iprutils If the "iprutils" package is installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-248906`

### Rule: OL 8 must not have the "tuned" package installed if not required for operational support.

**Rule ID:** `SV-248906r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"Tuned" is a daemon that uses "udev" to monitor connected devices and statically and dynamically tunes system settings according to a selected profile. Disabling the "tuned" package protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the "tuned" package is installed with the following command: $ sudo yum list installed tuned If the "tuned" package is installed, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-248907`

### Rule: OL 8 must prevent nonprivileged users from executing privileged functions, including disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-248907r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Nonprivileged users are individuals who do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from nonprivileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system prevents nonprivileged users from executing privileged functions, including disabling, circumventing, or altering implemented security safeguards/countermeasures. Obtain a list of authorized users (other than system administrator and guest accounts) for the system. Check the list against the system by using the following command: $ sudo semanage login -l | more Login Name SELinux User MLS/MCS Range Service __default__ user_u s0-s0:c0.c1023 * root unconfined_u s0-s0:c0.c1023 * system_u system_u s0-s0:c0.c1023 * joe staff_u s0-s0:c0.c1023 * All administrators must be mapped to the "sysadm_u", "staff_u", or an appropriately tailored confined role as defined by the organization. All authorized nonadministrative users must be mapped to the "user_u" role. If they are not mapped in this way, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252650`

### Rule: The OL 8 operating system must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-252650r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "/etc/shadow" file for blank passwords with the following command: $ sudo awk -F: '!$2 {print $1}' /etc/shadow If the command returns any results, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-252651`

### Rule: OL 8 library directories must have mode 755 or less permissive.

**Rule ID:** `SV-252651r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals will be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories within "/lib", "/lib64", "/usr/lib" and "/usr/lib64" have mode "755" or less permissive with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any system-wide shared library directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-252652`

### Rule: OL 8 library directories must be owned by root.

**Rule ID:** `SV-252652r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals will be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories are owned by "root" with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system wide shared library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-252653`

### Rule: OL 8 library directories must be group-owned by root or a system account.

**Rule ID:** `SV-252653r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 8 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 8 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals will be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories are group-owned by "root" with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system wide shared library directory is returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-252654`

### Rule: The OL 8 operating system must use a file integrity tool to verify correct operation of all security functions.

**Rule ID:** `SV-252654r958944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly, and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to the OL 8 operating system performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is installed and verifies the correct operation of all security functions. Check that the AIDE package is installed with the following command: $ sudo rpm -q aide aide-0.16-14.el8_5.1.x86_64 If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding. If AIDE is installed, check if it has been initialized with the following command: $ sudo /usr/sbin/aide --check If the output is "Couldn't open file /var/lib/aide/aide.db.gz for reading", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252655`

### Rule: OL 8 must specify the default "include" directory for the /etc/sudoers file.

**Rule ID:** `SV-252655r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "sudo" command allows authorized users to run programs (including shells) as other users, system users, and root. The "/etc/sudoers" file is used to configure authorized "sudo" users as well as the programs they are allowed to run. Some configuration options in the "/etc/sudoers" file allow configured users to run programs without re-authenticating. Use of these configuration options makes it easier for one compromised account to be used to compromise other accounts. It is possible to include other sudoers files from within the sudoers file currently being parsed using the #include and #includedir directives. When sudo reaches this line it will suspend processing of the current file (/etc/sudoers) and switch to the specified file/directory. Once the end of the included file(s) are reached, the rest of /etc/sudoers will be processed. Files that are included may themselves include other files. A hard limit of 128 nested include files is enforced to prevent include file loops.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the "include" and "includedir" directives are not present in the /etc/sudoers file, this requirement is not applicable. Verify the operating system specifies only the default "include" directory for the /etc/sudoers file with the following command: $ sudo grep include /etc/sudoers #includedir /etc/sudoers.d If the results are not "/etc/sudoers.d" or additional files or directories are specified, this is a finding. Verify the operating system does not have nested "include" files or directories within the /etc/sudoers.d directory with the following command: $ sudo grep -Er include /etc/sudoers.d If results are returned, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-252656`

### Rule: The OL 8 operating system must not be configured to bypass password requirements for privilege escalation.

**Rule ID:** `SV-252656r1050789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is not be configured to bypass password requirements for privilege escalation. Check the configuration of the "/etc/pam.d/sudo" file with the following command: $ sudo grep pam_succeed_if /etc/pam.d/sudo If any occurrences of "pam_succeed_if" is returned from the command, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252657`

### Rule: OL 8 must ensure the password complexity module is enabled in the system-auth file.

**Rule ID:** `SV-252657r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system. OL 8 utilizes "pwquality" as a mechanism to enforce password complexity. This is set in both: /etc/pam.d/password-auth /etc/pam.d/system-auth</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system uses "pwquality" to enforce the password complexity rules. Check for the use of "pwquality" in the system-auth file with the following command: $ sudo cat /etc/pam.d/system-auth | grep pam_pwquality password requisite pam_pwquality.so If the command does not return a line containing the value "pam_pwquality.so" as shown, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252658`

### Rule: OL 8 systems below version 8.4 must ensure the password complexity module in the system-auth file is configured for three retries or less.

**Rule ID:** `SV-252658r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system. OL 8 utilizes "pwquality" as a mechanism to enforce password complexity. This is set in both: /etc/pam.d/password-auth /etc/pam.d/system-auth By limiting the number of attempts to meet the pwquality module complexity requirements before returning with an error, the system will audit abnormal attempts at password changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement applies to OL versions 8.0 through 8.3. If the system is OL version 8.4 or newer, this requirement is not applicable. Verify the operating system is configured to limit the "pwquality" retry option to 3. Check for the use of the "pwquality" retry option in the system-auth file with the following command: $ sudo cat /etc/pam.d/system-auth | grep pam_pwquality password requisite pam_pwquality.so retry=3 If the value of "retry" is set to "0" or greater than "3", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252659`

### Rule: OL 8 systems below version 8.4 must ensure the password complexity module in the password-auth file is configured for three retries or less.

**Rule ID:** `SV-252659r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system. OL 8 utilizes "pwquality" as a mechanism to enforce password complexity. This is set in both: /etc/pam.d/password-auth /etc/pam.d/system-auth By limiting the number of attempts to meet the pwquality module complexity requirements before returning with an error, the system will audit abnormal attempts at password changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement applies to OL versions 8.0 through 8.3. If the system is OL version 8.4 or newer, this requirement is not applicable. Verify the operating system is configured to limit the "pwquality" retry option to 3. Check for the use of the "pwquality" retry option in the password-auth file with the following command: $ sudo cat /etc/pam.d/password-auth | grep pam_pwquality password requisite pam_pwquality.so retry=3 If the value of "retry" is set to "0" or greater than "3", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252660`

### Rule: OL 8 systems, version 8.4 and above, must ensure the password complexity module is configured for three retries or less.

**Rule ID:** `SV-252660r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system. OL 8 utilizes "pwquality" as a mechanism to enforce password complexity. This is set in both: /etc/pam.d/password-auth /etc/pam.d/system-auth By limiting the number of attempts to meet the pwquality module complexity requirements before returning with an error, the system will audit abnormal attempts at password changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement applies to OL versions 8.4 or newer. If the system is OL below version 8.4, this requirement is not applicable. Verify the operating system is configured to limit the "pwquality" retry option to 3. Check for the use of the "pwquality" retry option with the following command: $ sudo grep -r retry /etc/security/pwquality.conf* /etc/security/pwquality.conf:retry = 3 If the value of "retry" is set to "0" or greater than "3", is commented out or missing, this is a finding. If conflicting results are returned, this is a finding. Check for the use of the "pwquality" retry option in the system-auth and password-auth files with the following command: $ sudo grep pwquality /etc/pam.d/system-auth /etc/pam.d/password-auth | grep retry If the command returns any results, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252662`

### Rule: OL 8 must not enable IPv4 packet forwarding unless the system is a router.

**Rule ID:** `SV-252662r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network. The sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored. /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 8 is not performing IPv4 packet forwarding, unless the system is a router. Check that IPv4 forwarding is disabled using the following command: $ sudo sysctl net.ipv4.conf.all.forwarding net.ipv4.conf.all.forwarding = 0 If the IPv4 forwarding value is not "0" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Check that the configuration files are present to enable this network parameter: $ sudo grep -r net.ipv4.conf.all.forwarding /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf: net.ipv4.conf.all.forwarding = 0 If "net.ipv4.conf.all.forwarding" is not set to "0", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252663`

### Rule: The graphical display manager must not be the default target on OL 8 unless approved.

**Rule ID:** `SV-252663r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet services that are not required for system or application processes must not be active to decrease the attack surface of the system. Graphical display managers have a long history of security vulnerabilities and must not be used, unless approved and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system is configured to boot to the command line: $ systemctl get-default multi-user.target If the system default target is not set to "multi-user.target" and the Information System Security Officer (ISSO) lacks a documented requirement for a graphical user interface, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-255898`

### Rule: OL 8 SSH server must be configured to use only FIPS-validated key exchange algorithms.

**Rule ID:** `SV-255898r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections provided by FIPS-validated cryptographic algorithms, information can be viewed and altered by unauthorized users without detection. OL 8 incorporates system-wide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file. The system will attempt to use the first algorithm presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest algorithm available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSH server is configured to use only FIPS-validated key exchange algorithms: $ sudo grep -i kexalgorithms /etc/crypto-policies/back-ends/opensshserver.config CRYPTO_POLICY='-oKexAlgorithms=ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512' If the entries following "KexAlgorithms" have any algorithms defined other than "ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512", appear in a different order than shown, or are missing or commented out, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-256978`

### Rule: OL 8 must ensure cryptographic verification of vendor software packages.

**Rule ID:** `SV-256978r1015073_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptographic verification of vendor software packages ensures that all software packages are obtained from a valid source and protects against spoofing that could lead to installation of malware on the system. Oracle cryptographically signs all software packages, which includes updates, with a GPG key to verify that they are valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Oracle package-signing key is installed on the system and verify its fingerprint matches vendor value. Note: The GPG key is defined in key file "/etc/pki/rpm-gpg/RPM-GPG-KEY-oracle" by default. List Oracle GPG keys installed on the system: $ sudo rpm -q --queryformat "%{SUMMARY}\n" gpg-pubkey | grep -i "oracle" gpg(Oracle OSS group (Open Source Software group) <build@oss.oracle.com>) If Oracle GPG key is not installed, this is a finding. List key fingerprint of installed Oracle GPG key: $ sudo gpg -q --keyid-format short --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle If key file "/etc/pki/rpm-gpg/RPM-GPG-KEY-oracle" is missing, this is a finding. Example output: pub rsa4096/AD986DA3 2019-04-09 [SC] [expires: 2039-04-04] Key fingerprint = 76FD 3DB1 3AB6 7410 B89D B10E 8256 2EA9 AD98 6DA3 uid Oracle OSS group (Open Source Software group) <build@oss.oracle.com> sub rsa4096/D95DC12B 2019-04-09 [E] [expires: 2039-04-04] Compare key fingerprint of installed Oracle GPG key with fingerprint listed for OL 8 on Oracle verification webpage at https://linux.oracle.com/security/gpg/#gpg. If key fingerprint does not match, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-256979`

### Rule: OL 8 must be configured to allow sending email notifications of unauthorized configuration changes to designated personnel.

**Rule ID:** `SV-256979r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the operating system is configured to allow sending email notifications. Note: The "mailx" package provides the "mail" command that is used to send email messages. Verify that the "mailx" package is installed on the system: $ sudo yum list installed mailx mailx.x86_64 12.5-29.el8 @ol8_baseos_latest If "mailx" package is not installed, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-257259`

### Rule: OL 8 must terminate idle user sessions.

**Rule ID:** `SV-257259r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 logs out sessions that are idle for 15 minutes with the following command: $ sudo grep -i ^StopIdleSessionSec /etc/systemd/logind.conf StopIdleSessionSec=900 If "StopIdleSessionSec" is not configured to 900 seconds, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-274876`

### Rule: OL 8  must audit any script or executable called by cron as root or by any privileged user.

**Rule ID:** `SV-274876r1106141_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any script or executable called by cron as root or by any privileged user must be owned by that user and must have the permissions 755 or more restrictive and should have no extended rights that allow any nonprivileged user to modify the script or executable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 8 is configured to audit the execution of any system call made by cron as root or as any privileged user. $ sudo auditctl -l | grep /etc/cron.d -w /etc/cron.d -p wa -k cronjobs $ sudo auditctl -l | grep /var/spool/cron -w /var/spool/cron -p wa -k cronjobs If either of these commands do not return the expected output, or the lines are commented out, this is a finding.

