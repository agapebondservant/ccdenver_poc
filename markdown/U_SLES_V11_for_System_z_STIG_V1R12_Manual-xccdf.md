# STIG Benchmark: SUSE Linux Enterprise Server v11 for System z Security Technical Implementation Guide

---

**Version:** 1

**Description:**
The SUSE Linux Enterprise Server Ver 11 for System z Security Technical Implementation Guide (STIG) is published as a tool to improve the security of Department of Defense (DoD) information systems. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil

## Group: GEN000020

**Group ID:** `V-756`

### Rule: The system must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-44760r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system does not require valid root authentication before it boots into single-user or maintenance mode, anyone who invokes single-user or maintenance mode is granted privileged access to all files on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the system requires a password for entering single-user mode. # grep '~:S:' /etc/inittab If /sbin/sulogin is not listed, this is a finding.

## Group: GEN000280

**Group ID:** `V-760`

### Rule: Direct logins must not be permitted to shared, default, application, or utility accounts.

**Rule ID:** `SV-44791r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shared accounts (accounts where two or more people log in with the same user identification) do not provide identification and authentication. There is no way to provide for non-repudiation or individual accountability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Use the last command to check for multiple accesses to an account from different workstations/IP addresses. # last -R If users log directly onto accounts, rather than using the switch user (su) command from their own named account to access them, this is a finding (such as logging directly on to oracle). Verify with the SA or the IAO on documentation for users/administrators to log into their own accounts first and then switch user (su) to the account to be shared has been maintained including requirements and procedures. If no such documentation exists, this is a finding.

## Group: GEN000300

**Group ID:** `V-761`

### Rule: All accounts on the system must have unique user or account names.

**Rule ID:** `SV-44807r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A unique user name is the first part of the identification and authentication process. If user names are not unique, there can be no accountability on the system for auditing purposes. Multiple accounts sharing the same name could result in the denial of service to one or both of the accounts or unauthorized access to files or privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for duplicate account names. Example: # pwck -r If any duplicate account names are found, this is a finding.

## Group: GEN000320

**Group ID:** `V-762`

### Rule: All accounts must be assigned unique User Identification Numbers (UIDs).

**Rule ID:** `SV-44821r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts sharing a UID have full access to each others' files. This has the same effect as sharing a login. There is no way to assure identification, authentication, and accountability because the system sees them as the same user. If the duplicate UID is 0, this gives potential intruders another privileged account to attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to ensure there are no duplicate UIDs: # pwck -r If any duplicate UIDs are found, this is a finding.

## Group: GEN000400

**Group ID:** `V-763`

### Rule: The Department of Defense (DoD) login banner must be displayed immediately prior to, or as part of, console login prompts.

**Rule ID:** `SV-44969r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Access the system console and make a login attempt. Check for either of the following login banners based on the character limitations imposed by the system. An exact match is required. If one of these banners is not displayed, this is a finding. You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests- -not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. OR I've read & consent to terms in IS user agreem't.

## Group: GEN000440

**Group ID:** `V-765`

### Rule: Successful and unsuccessful logins and logouts must be logged.

**Rule ID:** `SV-44830r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Monitoring and recording successful and unsuccessful logins assists in tracking unauthorized access to the system. Without this logging, the ability to track unauthorized activity to specific user accounts may be diminished.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if all logon attempts are being logged. Procedure: Verify successful logins are being logged: # last -R | more If the command does not return successful logins, this is a finding. Verify if unsuccessful logons are being logged: # lastb -R | more If the command does not return unsuccessful logins, this is a finding.

## Group: GEN000460

**Group ID:** `V-766`

### Rule: The system must disable accounts after three consecutive unsuccessful login attempts.

**Rule ID:** `SV-44834r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling accounts after a limited number of unsuccessful login attempts improves protection against password guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the pam_tally configuration. # more /etc/pam.d/login Confirm the following line is configured, before the "common-auth” file is included: auth required pam_tally.so deny=3 onerr=fail # more /etc/pam.d/sshd Confirm the following line is configured, before the "common-auth” file is included: auth required pam_tally.so deny=3 onerr=fail If no such line is found, this is a finding.

## Group: GEN000480

**Group ID:** `V-768`

### Rule: The delay between login prompts following a failed login attempt must be at least 4 seconds.

**Rule ID:** `SV-44838r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a delay between successive failed login attempts increases protection against automated password guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the value of the FAIL_DELAY variable and the ability to use it Procedure:. # grep FAIL_DELAY /etc/login.defs If the value does not exist, or is less than 4, this is a finding. Check for the use of pam_faildelay. # grep pam_faildelay /etc/pam.d/common-auth* If the pam_faildelay.so module is not listed, this is a finding.

## Group: GEN000520

**Group ID:** `V-769`

### Rule: The root user must not own the logon session for an application requiring a continuous display.

**Rule ID:** `SV-44858r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an application is providing a continuous display and is running with root privileges, unauthorized users could interrupt the process and gain root access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If there is an application running on the system continuously in use (such as a network monitoring application), ask the SA what the name of the application is. Verify documentation exists for the requirement and justification of the application. If no documentation exists, this is a finding. Execute "ps -ef | more" to determine which user owns the process(es) associated with the application. If the owner is root, this is a finding.

## Group: GEN000560

**Group ID:** `V-770`

### Rule: The system must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-44860r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account is configured for password authentication but does not have an assigned password, it may be possible to log into the account without authentication. If the root user is configured without a password, the entire system may be compromised. For user accounts not using password authentication, the account must be configured with a password lock value instead of a blank or null value. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system will not log in accounts with blank passwords. # grep nullok /etc/pam.d/common-auth # grep nullok /etc/pam.d/common-account # grep nullok /etc/pam.d/common-password # grep nullok /etc/pam.d/common-session If an entry for nullok is found, this is a finding on Linux.

## Group: GEN000880

**Group ID:** `V-773`

### Rule: The root account must be the only account having a UID of 0.

**Rule ID:** `SV-44900r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an account has a UID of 0, it has root authority. Multiple accounts with a UID of 0 afford more opportunity for potential intruders to guess a password for a privileged account. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for duplicate UID 0 assignments by listing all accounts assigned UID 0. Procedure: # cat /etc/passwd | awk -F":" '{print$1":"$3":"}' | grep ":0:" If any accounts other than root are assigned UID 0, this is a finding.

## Group: GEN000900

**Group ID:** `V-774`

### Rule: The root users home directory must not be the root directory (/).

**Rule ID:** `SV-44901r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Changing the root home directory to something other than / and assigning it a 0700 protection makes it more difficult for intruders to manipulate the system by reading the files root places in its default directory. It also gives root the same discretionary access control for root's home directory as for the other user home directories.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if root is assigned a home directory other than / by listing its home directory. Procedure: # grep "^root" /etc/passwd | awk -F":" '{print $6}' If the root user home directory is /, this is a finding.

## Group: GEN000920

**Group ID:** `V-775`

### Rule: The root accounts home directory (other than /) must have mode 0700.

**Rule ID:** `SV-44902r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permissions greater than 0700 could allow unauthorized users access to the root home directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the root home directory. Procedure: # grep "^root" /etc/passwd | awk -F":" '{print $6}' # ls -ld <root home directory> If the mode of the directory is not equal to 0700, this is a finding. If the home directory is /, this check will be marked "Not Applicable".

## Group: GEN000940

**Group ID:** `V-776`

### Rule: The root accounts executable search path must be the vendor default and must contain only absolute paths.

**Rule ID:** `SV-44905r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory or other relative paths, executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is interpreted as the current working directory. Entries starting with a slash (/) are absolute paths. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the root user's PATH, log in as the root user, and execute: # env | grep PATH OR # echo $PATH This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry starts with a character other than a slash (/), this is a finding. If directories beyond those in the vendor's default root path are present. This is a finding.

## Group: GEN000960

**Group ID:** `V-777`

### Rule: The root account must not have world-writable directories in its executable search path.

**Rule ID:** `SV-44912r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the root search path contains a world-writable directory, malicious software could be placed in the path by intruders and/or malicious users and inadvertently run by root with all of root's privileges. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for world-writable permissions on all directories in the root user's executable search path. Procedure: # ls -ld `echo $PATH | sed "s/:/ /g"` If any of the directories in the PATH variable are world-writable, this is a finding.

## Group: GEN000980

**Group ID:** `V-778`

### Rule: The system must prevent the root account from directly logging in except from the system console.

**Rule ID:** `SV-44913r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the root account direct logins to only system consoles protects the root account from direct unauthorized access from a non-console device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/securetty # more /etc/securetty If the file does not exist, or contains more than "console" or a single "tty" device this is a finding.

## Group: GEN000360

**Group ID:** `V-780`

### Rule: GIDs reserved for system accounts must not be assigned to non-system groups.

**Rule ID:** `SV-44826r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reserved GIDs are typically used by system software packages. If non-system groups have GIDs in this range, they may conflict with system software, possibly leading to the group having permissions to modify system files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Confirm all accounts with a GID of 499 and below are used by a system account. Procedure: List all the users with a GID of 0-499. # awk -F: '$4 <= 499 {printf "%15s:%4s\n", $1, $4}' /etc/passwd | sort -n -t: -k2 If a GID reserved for system accounts (0 - 499) is used by a non-system account, this is a finding.

## Group: GEN000380

**Group ID:** `V-781`

### Rule: All GIDs referenced in the /etc/passwd file must be defined in the /etc/group file.

**Rule ID:** `SV-44827r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If a user is assigned the GID of a group not existing on the system, and a group with the GID is subsequently created, the user may have unintended rights to the group. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to ensure there are no GIDs referenced in /etc/passwd not defined in /etc/group: # pwck -r If GIDs referenced in /etc/passwd are not defined in /etc/group are returned, this is a finding.

## Group: GEN006480

**Group ID:** `V-782`

### Rule: The system must have a host-based intrusion detection tool installed.

**Rule ID:** `SV-45912r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without a host-based intrusion detection tool, there is no system-level defense when an intruder gains access to a system or network. Additionally, a host-based intrusion detection tool can provide methods to immediately lock out detected intrusion attempts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA or IAO if a host-based intrusion detection application is loaded on the system. The preferred intrusion detection system is McAfee HBSS available through Cybercom. If another host-based intrusion detection application, such as SELinux, is used on the system, this is not a finding. Procedure: Examine the system to see if the Host Intrusion Prevention System (HIPS) is installed #rpm -qa | grep MFEhiplsm If the MFEhiplsm package is installed, HBSS is being used on the system. If another host-based intrusion detection system is loaded on the system # find / -name <daemon name> Where <daemon name> is the name of the primary application daemon to determine if the application is loaded on the system. Determine if the application is active on the system. Procedure: # ps -ef | grep <daemon name> If no host-based intrusion detection system is installed on the system, this is a finding.

## Group: GEN000120

**Group ID:** `V-783`

### Rule: System security patches and updates must be installed and up-to-date.

**Rule ID:** `SV-44762r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Timely patching is critical for maintaining the operational availability, confidentiality, and integrity of information technology (IT) systems. However, failure to keep operating system and application software patched is a common mistake made by IT professionals. New patches are released daily, and it is often difficult for even experienced system administrators to keep abreast of all the new patches. When new weaknesses in an operating system exist, patches are usually made available by the vendor to resolve the problems. If the most recent security patches and updates are not installed, unauthorized users may take advantage of weaknesses present in the unpatched software. The lack of prompt attention to patching could result in a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of available package security updates from Novell. Check the available package updates have been installed on the system. Use the "rpm" command to list the packages installed on the system. Example: # rpm -qa --last If updated packages are available and applicable to the system and have not been installed, this is a finding.

## Group: GEN001140

**Group ID:** `V-784`

### Rule: System files and directories must not have uneven access permissions.

**Rule ID:** `SV-44924r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary access control is undermined if users, other than a file owner, have greater access permissions to system files and directories than the owner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check system directories for uneven file permissions. Procedure: # ls –lL /etc /bin /usr/bin /usr/local/bin /sbin /usr/sbin /usr/local/sbin Uneven file permissions exist if the file owner has less permissions than the group or other user classes. If any of the files in the above listed directories contain uneven file permissions, this is a finding.

## Group: GEN001160

**Group ID:** `V-785`

### Rule: All files and directories must have a valid owner.

**Rule ID:** `SV-44926r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Un-owned files and directories may be unintentionally inherited if a user is assigned the same UID as the UID of the un-owned files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for files with no assigned owner. Procedure: # find / -nouser If any files have no assigned owner, this is a finding. Caution should be used when centralized authorization is used because valid files may appear as unowned due to communication issues.

## Group: GEN001180

**Group ID:** `V-786`

### Rule: All network services daemon files must have mode 0755 or less permissive.

**Rule ID:** `SV-44931r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permission on daemons will protect them from unauthorized modification and possible system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of network services daemons. # find /usr/sbin -type f -perm +022 -exec stat -c %a:%n {} \; This will return the octal permissions and name of all files that are group or world writable. If any network services daemon listed is world or group writable (either or both of the 2 lowest order digits contain a 2, 3 or 6), this is a finding. Note: Network daemons not residing in these directories (such as httpd or sshd) must also be checked for the correct permissions.

## Group: GEN001260

**Group ID:** `V-787`

### Rule: System log files must have mode 0640 or less permissive.

**Rule ID:** `SV-44946r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system log files are not protected, unauthorized users could change the logged data, eliminating its forensic value.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of log files. Procedure: # ls -lL /var/log /var/log/syslog /var/adm With the exception of /var/log/wtmp, if any of the log files have modes more permissive than 0640, this is a finding.

## Group: GEN001800

**Group ID:** `V-788`

### Rule: All skeleton files (typically those in /etc/skel) must have mode 0644 or less permissive.

**Rule ID:** `SV-45113r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the skeleton files are not protected, unauthorized personnel could change user startup parameters and possibly jeopardize user files. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check skeleton files permissions. # ls -alL /etc/skel If a skeleton file has a mode more permissive than 0644, this is a finding.

## Group: GEN001320

**Group ID:** `V-789`

### Rule: NIS/NIS+/yp files must be owned by root, sys, or bin.

**Rule ID:** `SV-44953r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIS/NIS+/yp files are part of the system's identification and authentication processes and are critical to system security. Failure to give ownership of sensitive files or utilities to root or bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to check NIS file ownership: # ls -la /var/yp/*; If the file ownership is not root, sys, or bin, this is a finding.

## Group: GEN001340

**Group ID:** `V-790`

### Rule: NIS/NIS+/yp files must be group-owned by root, sys, or bin.

**Rule ID:** `SV-46086r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIS/NIS+/yp files are part of the system's identification and authentication processes and are, therefore, critical to system security. Failure to give ownership of sensitive files or utilities to root or bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to check the group ownership of NIS files: # ls -la /var/yp/* If the file group ownership is not root, sys, or bin, this is a finding.

## Group: GEN001360

**Group ID:** `V-791`

### Rule: The NIS/NIS+/yp command files must have mode 0755 or less permissive.

**Rule ID:** `SV-44954r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIS/NIS+/yp files are part of the system's identification and authentication processes and are critical to system security. Unauthorized modification of these files could compromise these processes and the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to check NIS file premissions. # ls -la /var/yp/*; If the file's mode is more permissive than 0755, this is a finding.

## Group: GEN001280

**Group ID:** `V-792`

### Rule: Manual page files must have mode 0644 or less permissive.

**Rule ID:** `SV-44949r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If manual pages are compromised, misleading information could be inserted, causing actions to compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the manual page files. Procedure: # ls -lL /usr/share/man /usr/share/info /usr/share/man/man* If any of the manual page files have a mode more permissive than 0644, this is a finding.

## Group: GEN001300

**Group ID:** `V-793`

### Rule: Library files must have mode 0755 or less permissive.

**Rule ID:** `SV-44951r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized access could destroy the integrity of the library files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of library files. Procedure: # DIRS="/usr/lib /usr/lib64 /lib /lib64";for DIR in $DIRS;do find $DIR -type f -perm +022 -exec stat -c %a:%n {} \;;done This will return the octal permissions and name of all group or world writable files. If any file listed is world or group writable (either or both of the 2 lowest order digits contain a 2, 3 or 6), this is a finding.

## Group: GEN001200

**Group ID:** `V-794`

### Rule: All system command files must have mode 0755 or less permissive.

**Rule ID:** `SV-46272r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permissions will protect system command files from unauthorized modification. System command files include files present in directories used by the operating system for storing default system executables and files present in directories included in the system's default executable search paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance>Elevate to Severity Code I if any file listed world-writable.</SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions for files in /etc, /bin, /usr/bin, /usr/local/bin, /sbin, /usr/sbin and /usr/local/sbin. Procedure: # DIRS="/etc /bin /usr/bin /usr/local/bin /sbin /usr/sbin /usr/local/sbin";for DIR in $DIRS;do find $DIR -type f -perm +022 -exec stat -c %a:%n {} \;;done This will return the octal permissions and name of all group or world writable files. If any file listed is world or group writable (either or both of the 2 lowest order digits contain a 2, 3 or 6), this is a finding. Note: Elevate to Severity Code I if any file listed is world-writable.

## Group: GEN001220

**Group ID:** `V-795`

### Rule: All system files, programs, and directories must be owned by a system account.

**Rule ID:** `SV-44941r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permissions will protect the files from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of system files, programs, and directories. Procedure: # ls -lLa /etc /bin /usr/bin /usr/local/bin /sbin /usr/sbin /usr/local/sbin If any of the system files, programs, or directories are not owned by a system account, this is a finding.

## Group: GEN001240

**Group ID:** `V-796`

### Rule: System files, programs, and directories must be group-owned by a system group.

**Rule ID:** `SV-44944r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permissions will protect the files from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group-ownership of system files, programs, and directories. Procedure: # ls –lLa /etc /bin /usr/bin /usr/local/bin /sbin /usr/sbin /usr/local/sbin If any system file, program, or directory is not owned by a system group, this is a finding.

## Group: GEN001400

**Group ID:** `V-797`

### Rule: The /etc/shadow (or equivalent) file must be owned by root.

**Rule ID:** `SV-45000r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/shadow file contains the list of local system accounts. It is vital to system security and must be protected from unauthorized modification. Failure to give ownership of sensitive files or utilities to root or bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the /etc/shadow file. # ls -lL /etc/shadow If the /etc/shadow file is not owned by root, this is a finding.

## Group: GEN001380

**Group ID:** `V-798`

### Rule: The /etc/passwd file must have mode 0644 or less permissive.

**Rule ID:** `SV-44992r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the passwd file is writable by a group-owner or the world, the risk of passwd file compromise is increased. The passwd file contains the list of accounts on the system and associated information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the /etc/passwd file. Procedure: # ls -lL /etc/passwd If /etc/passwd has a mode more permissive than 0644, this is a finding.

## Group: GEN001420

**Group ID:** `V-800`

### Rule: The /etc/shadow (or equivalent) file must have mode 0400.

**Rule ID:** `SV-45003r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/shadow file contains the list of local system accounts. It is vital to system security and must be protected from unauthorized modification. The file also contains password hashes which must not be accessible to users other than root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the /etc/shadow file. # ls -lL /etc/shadow If the /etc/shadow file has a mode more permissive than 0400, this is a finding.

## Group: GEN002380

**Group ID:** `V-801`

### Rule: The owner, group-owner, mode, ACL, and location of files with the setuid bit set must be documented using site-defined procedures.

**Rule ID:** `SV-45184r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All files with the setuid bit set will allow anyone running these files to be temporarily assigned the UID of the file. While many system files depend on these attributes for proper operation, security problems can result if setuid is assigned to programs allowing reading and writing of files, or shell escapes. Only default vendor-supplied executables should have the setuid bit set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If STIGID GEN000220 is satisfied, this is not a finding. List all setuid files on the system. Procedure: # find / -perm -4000 -exec ls -l {} \; | more Note: Executing these commands may result in large listings of files; the output may be redirected to a file for easier analysis. Ask the SA or IAO if files with the suid bit set have been documented. If any undocumented file has its suid bit set, this is a finding.

## Group: GEN002440

**Group ID:** `V-802`

### Rule: The owner, group-owner, mode, ACL and location of files with the setgid bit set must be documented using site-defined procedures.

**Rule ID:** `SV-45192r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All files with the setgid bit set will allow anyone running these files to be temporarily assigned the GID of the file. While many system files depend on these attributes for proper operation, security problems can result if setgid is assigned to programs allowing reading and writing of files, or shell escapes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
List all setgid files on the system. Procedure: # find / -perm -2000 -exec ls -l {} \; | more Note: Executing these commands may result in large listings of files; the output may be redirected to a file for easier analysis. Ask the SA or IAO if files with the sgid bit set have been documented. If any undocumented file has its sgid bit set, this is a finding.

## Group: GEN002400

**Group ID:** `V-803`

### Rule: The system must be checked weekly for unauthorized setuid files as well as unauthorized modification to authorized setuid files.

**Rule ID:** `SV-45185r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files with the setuid bit set will allow anyone running these files to be temporarily assigned the UID of the file. While many system files depend on these attributes for proper operation, security problems can result if setuid is assigned to programs allowing reading and writing of files, or shell escapes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if a weekly automated or manual process is used to generate a list of suid files on the system and compare it with the prior list. If no such process is in place, this is a finding. NOTE: For MAC I systems, increase the frequency to daily.

## Group: GEN002460

**Group ID:** `V-804`

### Rule: The system must be checked weekly for unauthorized setgid files as well as unauthorized modification to authorized setgid files.

**Rule ID:** `SV-45200r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files with the setgid bit set will allow anyone running these files to be temporarily assigned the group id of the file. While many system files depend on these attributes for proper operation, security problems can result if setgid is assigned to programs allowing reading and writing of files, or shell escapes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if a weekly automated or manual process is used to generate a list of sgid files on the system and compare it with the prior list. If no such process is in place, this is a finding. NOTE: For MAC I systems, increase the frequency to daily.

## Group: GEN002420

**Group ID:** `V-805`

### Rule: Removable media, remote file systems, and any file system not containing approved setuid files must be mounted with the nosuid option.

**Rule ID:** `SV-45187r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute setuid files with owner privileges. This option must be used for mounting any file system not containing approved setuid files. Executing setuid files from untrusted file systems, or file systems not containing approved setuid files, increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/fstab and verify the "nosuid" mount option is used on file systems mounted from removable media, network shares, or any other file system not containing approved setuid or setgid files. If any of these files systems do not mount with the "nosuid" option, it is a finding.

## Group: GEN002500

**Group ID:** `V-806`

### Rule: The sticky bit must be set on all public directories.

**Rule ID:** `SV-45202r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Failing to set the sticky bit on the public directories allows unauthorized users to delete files in the directory structure. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check all world-writable directories have the sticky bit set. Procedure: # find / -type d -perm -002 ! -perm -1000 > wwlist If the sticky bit is not set on a world-writable directory, this is a finding.

## Group: GEN002520

**Group ID:** `V-807`

### Rule: All public directories must be owned by root or an application account.

**Rule ID:** `SV-45203r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public directory has the sticky bit set and is not owned by a privileged UID, unauthorized users may be able to modify files created by others. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of all public directories. Procedure: # find / -type d -perm -1002 -exec ls -ld {} \; If any public directory is not owned by root or an application user, this is a finding.

## Group: GEN002560

**Group ID:** `V-808`

### Rule: The system and user default umask must be 077.

**Rule ID:** `SV-45205r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. An umask of 077 limits new files to mode 700 or less permissive. Although umask can be represented as a 4-digit number, the first digit representing special access modes is typically ignored or required to be 0. This requirement applies to the globally configured system defaults and the user defaults for each account on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance>If the default umask is 000 or does not restrict the world-writable permission, this becomes a CAT I finding.</SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check global initialization files for the configured umask value. Procedure: # grep umask /etc/* Check local initialization files for the configured umask value. Procedure: # cut -d: -f6 /etc/passwd |xargs -n1 -IDIR find DIR -name ".*" -type f -maxdepth 1 -exec grep umask {} \; If the system and user default umask is not 077, this a finding. Note: If the default umask is 000 or allows for the creation of world-writable files this becomes a Severity Code I finding.

## Group: GEN002640

**Group ID:** `V-810`

### Rule: Default system accounts must be disabled or removed.

**Rule ID:** `SV-45206r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Vendor accounts and software may contain backdoors allowing unauthorized access to the system. These backdoors are common knowledge and present a threat to system security if the account is not disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if default system accounts (such as those for sys, bin, uucp, nuucp, daemon, smtp) have been disabled. # cat /etc/shadow If an account's password field is "*", "*LK*", or is prefixed with a '!', the account is locked or disabled. If there are any unlocked default system accounts this is a finding.

## Group: GEN002660

**Group ID:** `V-811`

### Rule: Auditing must be implemented.

**Rule ID:** `SV-45207r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked and malicious activity cannot be detected and traced back to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if auditing is enabled. # ps -ef |grep auditd If the auditd process is not found, this is a finding.

## Group: GEN002680

**Group ID:** `V-812`

### Rule: System audit logs must be owned by root.

**Rule ID:** `SV-45208r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of system audit log files to root provides the designated owner and unauthorized users with the potential to access sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to determine the location of audit logs and then check the ownership. Procedure: # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; ls -l ${audit_log_file%/*}; else printf "audit log file(s) not found\n"; fi) If any audit log file is not owned by root, this is a finding.

## Group: GEN002700

**Group ID:** `V-813`

### Rule: System audit logs must have mode 0640 or less permissive.

**Rule ID:** `SV-45210r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user can write to the audit logs, audit trails can be modified or destroyed and system intrusion may not be detected. System audit logs are those files generated from the audit system and do not include activity, error, or other log files created by application software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to determine the location of audit logs and then check the mode of the files. Procedure: # grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//|xargs stat -c %a:%n If any audit log file has a mode more permissive than 0640, this is a finding.

## Group: GEN002720

**Group ID:** `V-814`

### Rule: The audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-45295r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0) or there must both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S creat" | grep -e "-F success=0" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S creat" | grep -e "-F exit=-EPERM" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S creat" | grep -e "-F exit=-EACCES" If an "-S creat" audit rule with "-F success" does not exist and no separate rules containing "-F exit=-EPERM" and "-F exit=-EACCES" for "creat" exist, then this is a finding.

## Group: GEN002740

**Group ID:** `V-815`

### Rule: The audit system must be configured to audit file deletions.

**Rule ID:** `SV-45303r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system audit configuration to determine if file and directory deletions are audited. # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "unlink" If no results are returned, or the results do not contain "-S unlink", this is a finding.

## Group: GEN002760

**Group ID:** `V-816`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-46161r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -i "auditd.conf" If no results are returned, or the line does not start with "-w", this is a finding.

## Group: GEN002800

**Group ID:** `V-818`

### Rule: The audit system must be configured to audit login, logout, and session initiation.

**Rule ID:** `SV-45340r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The message types that are always recorded to /var/log/audit/audit.log include LOGIN,USER_LOGIN,USER_START,USER_END among others and do not need to be added to audit_rules. The log files /var/log/faillog and /var/log/lastlog must be protected from tampering of the login records. Procedure: # egrep "faillog|lastlog" /etc/audit/audit.rules|grep -e "-p (wa|aw)" If both /var/log/faillog and /var/log/lastlog entries do not exist, this is a finding.

## Group: GEN002820

**Group ID:** `V-819`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45447r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " chmod " If "-S chmod" is not in the result, this is a finding

## Group: GEN003720

**Group ID:** `V-821`

### Rule: The inetd.conf file, xinetd.conf file, and the xinetd.d directory must be owned by root or bin.

**Rule ID:** `SV-45757r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of sensitive files or utilities to root provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration possibly weakening the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the owner of the xinetd configuration files. Procedure: # ls -lL /etc/xinetd.conf # ls -laL /etc/xinetd.d This is a finding if any of the above files or directories are not owned by root or bin.

## Group: GEN003740

**Group ID:** `V-822`

### Rule: The xinetd.conf files must have mode 0640 or less permissive.

**Rule ID:** `SV-45759r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Internet service daemon configuration files must be protected as malicious modification could cause Denial of Service or increase the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the xinetd configuration files. Procedure: # ls -lL /etc/xinetd.conf # ls -lL /etc/xinetd.d If the mode of the file(s) is more permissive than 0640, this is a finding.

## Group: GEN003760

**Group ID:** `V-823`

### Rule: The services file must be owned by root or bin.

**Rule ID:** `SV-45763r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of sensitive files or utilities to root or bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration possibly weakening the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the services file. Procedure: # ls -lL /etc/services If the services file is not owned by root or bin, this is a finding.

## Group: GEN003780

**Group ID:** `V-824`

### Rule: The services file must have mode 0644 or less permissive.

**Rule ID:** `SV-45765r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The services file is critical to the proper operation of network services and must be protected from unauthorized modification. Unauthorized modification could result in the failure of network services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the services file. Procedure: # ls -lL /etc/services If the services file has a mode more permissive than 0644, this is a finding.

## Group: GEN001780

**Group ID:** `V-825`

### Rule: Global initialization files must contain the mesg -n or mesg n commands.

**Rule ID:** `SV-45106r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the "mesg -n" or "mesg n" command is not placed into the system profile, messaging can be used to cause a Denial of Service attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check global initialization files for the presence of "mesg -n" or "mesg n". Procedure: # grep "mesg" /etc/bash.bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc If no global initialization files contain "mesg -n" or "mesg n", this is a finding.

## Group: GEN003900

**Group ID:** `V-827`

### Rule: The hosts.lpd file (or equivalent) must not contain a + character.

**Rule ID:** `SV-45812r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having the '+' character in the hosts.lpd (or equivalent) file allows all hosts to use local system print resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Look for the presence of a print service configuration file. Procedure: # find /etc -name hosts.lpd -print # find /etc -name Systems -print # find /etc -name printers.conf If none of the files are found, this check should be marked Not Applicable. Otherwise, examine the configuration file. Procedure: # more <print service file> Check for entries that contain a ‘+’ or ‘_’ character. If any are found, this is a finding. For the "cups" print service, verify remote host access is limited. # grep -i Listen /etc/cups/cupsd.conf The /etc/cups/cupsd.conf file must not contain a Listen *:<port> or equivalent line. If the network address of the "Listen" line is unrestricted. This is a finding. # grep -i "Allow From" /etc/cups/cupsd.conf The "Allow From" line within the "<Location />" element should limit access to the printers to @LOCAL and specific hosts. If the "Allow From" line contains "All" this is a finding.

## Group: GEN003920

**Group ID:** `V-828`

### Rule: The hosts.lpd (or equivalent) file must be owned by root, bin, sys, or lp.

**Rule ID:** `SV-45813r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of the hosts.lpd file to root, bin, sys, or lp provides the designated owner, and possible unauthorized users, with the potential to modify the hosts.lpd file. Unauthorized modifications could disrupt access to local printers from authorized remote hosts or permit unauthorized remote access to local printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the print service configuration file. Procedure: # find /etc -name hosts.lpd -print # find /etc -name Systems –print # find /etc –name printers.conf -print If no print service configuration file is found, this is not applicable. Check the ownership of the print service configuration file(s). # ls –lL <print service file> If the owner of the file is not root, this is a finding.

## Group: GEN003940

**Group ID:** `V-829`

### Rule: The hosts.lpd (or equivalent) must have mode 0644 or less permissive.

**Rule ID:** `SV-45816r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the hosts.lpd (or equivalent) file may permit unauthorized modification. Unauthorized modifications could disrupt access to local printers from authorized remote hosts or permit unauthorized remote access to local printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate any print service configuration file on the system. Consult vendor documentation for the name and location of print service configuration files. Procedure: # find /etc -name hosts.lpd -print # find /etc -name Systems –print # find /etc -name printers.conf -print Check the mode of the print service configuration file. # ls -lL <print service file> If no print service configuration file is found, this is not applicable. If the mode of the print service configuration file is more permissive than 0644, this is a finding.

## Group: GEN004360

**Group ID:** `V-831`

### Rule: The alias file must be owned by root.

**Rule ID:** `SV-45827r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the alias file is not owned by root, an unauthorized user may modify the file adding aliases to run malicious code or redirect e-mail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the alias files. Procedure: for sendmail: # ls -lL /etc/aliases # ls -lL /etc/aliases.db If all the files are not owned by root, this is a finding. for postfix: Verify the location of the alias file. # postconf alias_maps This will return the location of the "aliases" file. # ls -lL <postfix aliases file> # ls -lL <postfix aliases.db file> If all the files are not owned by root, this is a finding.

## Group: GEN004380

**Group ID:** `V-832`

### Rule: The alias file must have mode 0644 or less permissive.

**Rule ID:** `SV-45849r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the aliases file may permit unauthorized modification. If the alias file is modified by an unauthorized user, they may modify the file to run malicious code or redirect e-mail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the alias file. Procedure: for sendmail: # ls -lL /etc/aliases /etc/aliases.db If an alias file has a mode more permissive than 0644, this is a finding. for postfix: Verify the location of the alias file. # postconf alias_maps This will return the location of the "aliases" file. # ls -lL <postfix aliases file> <postfix aliases.db file> If an alias file has a mode more permissive than 0644, this is a finding.

## Group: GEN004400

**Group ID:** `V-833`

### Rule: Files executed through a mail aliases file must be owned by root and must reside within a directory owned and writable only by root.

**Rule ID:** `SV-45851r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If a file executed through a mail aliases file is not owned and writable only by root, it may be subject to unauthorized modification. Unauthorized modification of files executed through aliases may allow unauthorized users to attain root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of files referenced within the sendmail aliases file. Procedure: # more /etc/aliases Examine the aliases file for any utilized directories or paths. # ls -lL <directory or file path> Check the owner for any paths referenced. Check if the file or parent directory is owned by root. If not, this is a finding.

## Group: GEN004420

**Group ID:** `V-834`

### Rule: Files executed through a mail aliases file must have mode 0755 or less permissive.

**Rule ID:** `SV-45853r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a file executed through a mail aliases file has permissions greater than 0755, it can be modified by an unauthorized user and may contain malicious code or instructions potentially compromising the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the “sendmail” package is not installed, this is not applicable. Examine the contents of the /etc/aliases file. Procedure: # more /etc/aliases Examine the aliases file for any utilized directories or paths. # ls -lL <file referenced from aliases> Check the permissions for any paths referenced. If any file referenced from the aliases file has a mode more permissive than 0755, this is a finding.

## Group: GEN004440

**Group ID:** `V-835`

### Rule: Sendmail logging must not be set to less than nine in the sendmail.cf file.

**Rule ID:** `SV-45856r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If Sendmail is not configured to log at level 9, system logs may not contain the information necessary for tracking unauthorized use of the sendmail service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the “sendmail” package is not installed, this is not applicable. Check if the sendmail package is installed: # rpm –q sendmail If it is installed, the logging level must be set to level nine: Procedure: for sendmail: # grep "O L" /etc/mail/sendmail.cf OR # grep LogLevel /etc/mail/sendmail.cf If logging is set to less than nine, this is a finding. for Postfix: This rule is not applicable to postfix which does not use "log levels" in the same fashion as sendmail.

## Group: GEN004460

**Group ID:** `V-836`

### Rule: The system syslog service must log informational and more severe SMTP service messages.

**Rule ID:** `SV-45858r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If informational and more severe SMTP service messages are not logged, malicious activity on the system may go unnoticed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for mail.crit logging configuration. Procedure: # grep "mail\." /etc/rsyslog.conf If syslog is not configured to log critical sendmail messages ("mail.crit" or "mail.*"), this is a finding.

## Group: GEN004480

**Group ID:** `V-837`

### Rule: The SMTP service log file must be owned by root.

**Rule ID:** `SV-45859r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SMTP service log file is not owned by root, then unauthorized personnel may modify or delete the file to hide a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate any mail log files by checking the syslog configuration file. Procedure: # more /etc/rsyslog.conf The check procedure is the same for both sendmail and Postfix. Identify any log files configured for the "mail" service (excluding mail.none) at any severity level and check the ownership Procedure: # ls -lL <file location> If any mail log file is not owned by root, this is a finding.

## Group: GEN004500

**Group ID:** `V-838`

### Rule: The SMTP service log file must have mode 0644 or less permissive.

**Rule ID:** `SV-45861r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SMTP service log file is more permissive than 0644, unauthorized users may be allowed to change the log file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the SMTP service log file. Procedure: # more /etc/rsyslog.conf Check the configuration to determine which log files contain logs for mail.crit, mail.debug, or *.crit. Procedure: # ls -lL <file location> The check procedure is the same for both sendmail and Postfix. Identify any log files configured for the "mail" service (excluding mail.none) at any severity level and check the permissions If the log file permissions are greater than 0644, this is a finding.

## Group: GEN004880

**Group ID:** `V-840`

### Rule: The ftpusers file must exist.

**Rule ID:** `SV-45879r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ftpusers file contains a list of accounts not allowed to use FTP to transfer files. If this file does not exist, then unauthorized accounts can utilize FTP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the ftpusers file. Procedure: For gssftp: # ls -l /etc/ftpusers For vsftp: # ls -l /etc/vsftpd.ftpusers or # ls -l /etc/vsftpd/ftpusers If the appropriate ftpusers file for the running FTP service does not exist, this is a finding.

## Group: GEN004900

**Group ID:** `V-841`

### Rule: The ftpusers file must contain account names not allowed to use FTP.

**Rule ID:** `SV-45880r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ftpusers file contains a list of accounts not allowed to use FTP to transfer files. If the file does not contain the names of all accounts not authorized to use FTP, then unauthorized use of FTP may take place.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of the ftpusers file. For gssftp: # more /etc/ftpusers For vsftp: # more /etc/vsftpd.ftpusers /etc/vfsftpd/ftpusers If the system has accounts not allowed to use FTP and not listed in the ftpusers file, this is a finding.

## Group: GEN004920

**Group ID:** `V-842`

### Rule: The ftpusers file must be owned by root.

**Rule ID:** `SV-45881r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the file ftpusers is not owned by root, an unauthorized user may modify the file to allow unauthorized accounts to use FTP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the ftpusers file. Procedure: For gssftp: # ls -l /etc/ftpusers For vsftp: # ls -l /etc/vsftpd.ftpusers /etc/vsftpd/ftpusers If the ftpusers file is not owned by root, this is a finding.

## Group: GEN004940

**Group ID:** `V-843`

### Rule: The ftpusers file must have mode 0640 or less permissive.

**Rule ID:** `SV-45883r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the ftpusers file could permit unauthorized modification. Unauthorized modification could result in Denial of Service to authorized FTP users or permit unauthorized users to access the FTP service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the ftpusers file. Procedure: For gssftp: # ls -l /etc/ftpusers For vsftp: # ls -l /etc/vsftpd.ftpusers /etc/vsftpd/ftpusers If the ftpusers file has a mode more permissive than 0640, this is a finding.

## Group: GEN004980

**Group ID:** `V-845`

### Rule: The FTP daemon must be configured for logging or verbose mode.

**Rule ID:** `SV-45885r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The -l option allows basic logging of connections. The verbose (on HP) and the debug (on Solaris) allow logging of what files the ftp session transferred. This extra logging makes it possible to easily track which files are being transferred onto or from a system. If they are not configured, the only option for tracking is the audit files. The audit files are much harder to read. If auditing is not properly configured, then there would be no record at all of the file transfer transactions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Find if logging is applied to the ftp daemon. The procedure depends on the implementation of ftpd used by the system. Procedures: For vsftpd: If vsftpd is started by xinetd: #grep vsftpd /etc/xinetd.d/* This will indicate the xinetd.d startup file #grep server_args <vsftpd xinetd.d startup file> This will indicate the vsftpd config file used when starting through xinetd. If the line is missing then "/etc/vsftpd.conf", the default config file, is used. #grep xferlog_enable <vsftpd config file> If "xferlog_enable" is missing or is not set to "yes", this is a finding. If vsftp is not started by xinetd: #grep xferlog_enable /etc/vsftpd.conf If "xferlog_enable" is missing or is not set to "yes", this is a finding. For gssftp: Find if the -l option will be applied when xinetd starts gssftp # grep server-args /etc/xinetd.d/gssftp If the line is missing or does not contain at least one -l, this is a finding.

## Group: GEN004820

**Group ID:** `V-846`

### Rule: Anonymous FTP must not be active on the system unless authorized.

**Rule ID:** `SV-45877r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Due to the numerous vulnerabilities inherent in anonymous FTP, it is not recommended. If anonymous FTP must be used on a system, the requirement must be authorized and approved in the system accreditation package.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Attempt to log into this host with a user name of anonymous and a password of guest (also try the password of guest@mail.com). If the logon is successful and the use of anonymous ftp has not been documented and approved by the IAO, this is a finding. Procedure: # ftp localhost Name: anonymous 530 Guest login not allowed on this machine.

## Group: GEN005080

**Group ID:** `V-847`

### Rule: The TFTP daemon must operate in secure mode which provides access only to a single directory on the host file system.

**Rule ID:** `SV-45888r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Secure mode limits TFTP requests to a specific directory. If TFTP is not running in secure mode, it may be able to write to any file or directory and may seriously impair system integrity, confidentiality, and availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# grep server_args /etc/xinetd.d/tftp If the "-s" parameter is not specified, this is a finding.

## Group: GEN005100

**Group ID:** `V-848`

### Rule: The TFTP daemon must have mode 0755 or less permissive.

**Rule ID:** `SV-45902r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If TFTP runs with the setuid or setgid bit set, it may be able to write to any file or directory and may seriously impair system integrity, confidentiality, and availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the TFTP daemon. Procedure: # grep "server " /etc/xinetd.d/tftp # ls -lL <in.tftpd binary> If the mode of the file is more permissive than 0755, this is a finding.

## Group: GEN005120

**Group ID:** `V-849`

### Rule: The TFTP daemon must be configured to vendor specifications, including a dedicated TFTP user account, a non-login shell such as /bin/false, and a home directory owned by the TFTP user.

**Rule ID:** `SV-45906r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If TFTP has a valid shell, it increases the likelihood someone could log on to the TFTP account and compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the /etc/passwd file to determine if TFTP is configured properly. Procedure: Check if TFTP if used. # grep disable /etc/xinetd.d/tftp If the file does not exist or the returned line indicates "yes", then this is not a finding. Otherwise, if the returned line indicates "no" then TFTP is enabled and must use a dedicated "tftp" user. # grep user /etc/xinetd.d/tftp If the returned line indicates a user other than the dedicated "tftp" user, this is a finding. # grep tftp /etc/passwd If a "tftp" user account does not exist and TFTP is active, this is a finding. Check the user shell for the "tftp" user. If it is not /bin/false or equivalent, this is a finding. Check the home directory assigned to the "tftp" user. If no home directory is set, or the directory specified is not dedicated to the use of the TFTP service, this is a finding.

## Group: GEN005160

**Group ID:** `V-850`

### Rule: Any X Windows host must write .Xauthority files.

**Rule ID:** `SV-45911r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.Xauthority files ensure the user is authorized to access specific X Windows host. If .Xauthority files are not used, it may be possible to obtain unauthorized access to the X Windows host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the ‘xorg-x11’ package is installed: # rpm –q xorg-x11 If the xorg-x11 package is not installed this finding does not apply. Check for .Xauthority or .xauth files being utilized by looking for such files in the home directory of a user. Procedure: Verify Xwindows is used on the system. # egrep "^x:5.*X11" /etc/inittab If no line is returned the boot process does not start Xwindows. If Xwindows is not configured to run, this rule is not applicable. Look for xauthority files in user home directory. # cd ~someuser # ls -la|egrep "(\.Xauthority|\.xauth) " If the .Xauthority or .xauth (followed by apparently random characters) files do not exist, ask the SA if the user is using Xwindows. If the user is utilizing Xwindows and none of these files exist, this is a finding.

## Group: GEN006400

**Group ID:** `V-867`

### Rule: The Network Information System (NIS) protocol must not be used.

**Rule ID:** `SV-46282r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Due to numerous security vulnerabilities existing within NIS, it must not be used. Possible alternative directory services are NIS+ and LDAP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to determine if NIS is active on the system: # ps -ef | grep ypbind If NIS is found active on the system, this is a finding.

## Group: GEN001440

**Group ID:** `V-899`

### Rule: All interactive users must be assigned a home directory in the /etc/passwd file.

**Rule ID:** `SV-45010r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If users do not have a valid home directory, there is no place for the storage and control of files they own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Use pwck to verify home directory assignments are present. # pwck If any user is not assigned a home directory, this is a finding.

## Group: GEN001460

**Group ID:** `V-900`

### Rule: All interactive user home directories defined in the /etc/passwd file must exist.

**Rule ID:** `SV-45014r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If a user has a home directory defined that does not exist, the user may be given the / directory, by default, as the current working directory upon logon. This could create a Denial of Service because the user would not be able to perform useful tasks in this location.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Use pwck to verify assigned home directories exist. # pwck If any user's assigned home directory does not exist, this is a finding.

## Group: GEN001480

**Group ID:** `V-901`

### Rule: All user home directories must have mode 0750 or less permissive.

**Rule ID:** `SV-45028r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on home directories allow unauthorized access to user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the home directory mode of each user in /etc/passwd. Procedure: # cut -d: -f6 /etc/passwd|sort|uniq|xargs -n1 ls -ld If a user home directory's mode is more permissive than 0750, this is a finding. Note: Application directories are allowed and may need 0755 permissions (or greater) for correct operation.

## Group: GEN001500

**Group ID:** `V-902`

### Rule: All interactive user home directories must be owned by their respective users.

**Rule ID:** `SV-45030r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If users do not own their home directories, unauthorized users could access user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of each user home directory listed in the /etc/passwd file. Procedure: # cut -d : -f 6 /etc/passwd | xargs -n1 ls -ld If any user home directory is not owned by the assigned user, this is a finding.

## Group: GEN001520

**Group ID:** `V-903`

### Rule: All interactive user home directories must be group-owned by the home directory owners primary group.

**Rule ID:** `SV-46273r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of the home directory is not the same as the GID of the user, this would allow unauthorized access to files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership for each user in the /etc/passwd file. Procedure: # cut -d : -f 6 /etc/passwd | xargs -n1 ls -ld If any user home directory is not group-owned by the assigned user's primary group, this is a finding. Home directories for application accounts requiring different group ownership must be documented using site-defined procedures.

## Group: GEN001860

**Group ID:** `V-904`

### Rule: All local initialization files must be owned by the home directorys user or root.

**Rule ID:** `SV-45151r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of local initialization files. Procedure: # ls –a /<users home directory> | grep “^\.” | awk '{if ((!($1=="."))&&(!($1==".."))) print}' | xargs ls -ld If local initialization files are not owned by the home directory's user, this is a finding.

## Group: GEN001880

**Group ID:** `V-905`

### Rule: All local initialization files must have mode 0740 or less permissive.

**Rule ID:** `SV-45154r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the modes of local initialization files. Procedure: # for HOMEDIR in $(cut -d: -f6 /etc/passwd); do find ${HOMEDIR} ! -fstype nfs -type f -name '\.*' \( -perm -0002 -o -perm -0020 \); done If local initialization files are more permissive than 0740 or the .dt directory is more permissive than 0755 or the .dtprofile file is more permissive than 0755, this is a finding.

## Group: GEN001580

**Group ID:** `V-906`

### Rule: All run control scripts must have mode 0755 or less permissive.

**Rule ID:** `SV-45043r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the startup files are writable by other users, they could modify the startup files to insert malicious commands into the startup files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check run control script modes. – # ls -lL /etc/rc* /etc/init.d If any run control script has a mode more permissive than 0755, this is a finding.

## Group: GEN001600

**Group ID:** `V-907`

### Rule: Run control scripts executable search paths must contain only absolute paths.

**Rule ID:** `SV-45064r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory or other relative paths, executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' library search paths. # grep -r PATH /etc/rc* /etc/init.d This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/), this is a relative path, this is a finding.

## Group: GEN001640

**Group ID:** `V-910`

### Rule: Run control scripts must not execute world-writable programs or scripts.


**Rule ID:** `SV-45068r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>World-writable files could be modified accidentally or maliciously to compromise system integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions on the files or scripts executed from system startup scripts to see if they are world-writable. Procedure: # more <startup script> # ls -lL <script or executable referenced by startup script> Alternatively, obtain a list of all world-writable files on the system and check system startup scripts to determine if any are referenced. Procedure: # find / -perm -0002 -type f | grep –v ‘^/proc’ > wwlist If any system startup script executes any file or script that is world-writable, this is a finding.

## Group: GEN002000

**Group ID:** `V-913`

### Rule: There must be no .netrc files on the system.


**Rule ID:** `SV-45165r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unencrypted passwords for remote FTP servers may be stored in .netrc files. Policy requires passwords be encrypted in storage and not used in access scripts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for the existence of any .netrc files. Procedure: # find / -name .netrc If any .netrc file exists, this is a finding.

## Group: GEN001540

**Group ID:** `V-914`

### Rule: All files and directories contained in interactive user home directories must be owned by the home directorys owner.

**Rule ID:** `SV-45035r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If users do not own the files in their directories, unauthorized users may be able to access them. Additionally, if files are not owned by the user, this could be an indication of system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
For each user in the /etc/passwd file, check for the presence of files and directories within the user's home directory not owned by the home directory owner. Procedure: # find /<usershomedirectory> ! -fstype nfs ! -user <username> ! \( -name .bashrc -o -name .bash_login -o -name .bash_logout -o -name .bash_profile -o -name .cshrc -o -name .kshrc -o -name .login -o -name .logout -o -name .profile -o -name .tcshrc -o -name .env -o -name .dtprofile -o -name .dispatch -o -name .emacs -o -name .exrc \) -exec ls -ld {} \; If user home directories contain files or directories not owned by the home directory owner, this is a finding.

## Group: GEN001560

**Group ID:** `V-915`

### Rule: All files and directories contained in user home directories must have mode 0750 or less permissive.

**Rule ID:** `SV-45040r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Excessive permissions allow unauthorized access to user files. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
For each user in the /etc/passwd file, check for files and directories with a mode more permissive than 0750. Procedure: # find /<usershomedirectory> ! -fstype nfs ! \( -name .bashrc -o -name .bash_login -o -name .bash_logout -o -name .bash_profile -o -name .cshrc -o -name .kshrc -o -name .login -o -name .logout -o -name .profile -o -name .tcshrc -o -name .env -o -name .dtprofile -o -name .dispatch -o -name .emacs -o -name .exrc \) \( -perm -0001 -o -perm -0002 -o -perm -0004 -o -perm -0020 -o -perm -2000 -o -perm -4000 \) -exec ls -ld {} \; If user home directories contain files or directories more permissive than 0750, this is a finding.

## Group: GEN002120

**Group ID:** `V-916`

### Rule: The /etc/shells (or equivalent) file must exist.

**Rule ID:** `SV-45170r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shells file (or equivalent) lists approved default shells. It helps provide layered defense to the security approach by ensuring users cannot change their default shell to an unauthorized unsecure shell.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify /etc/shells exists. # ls -l /etc/shells If the file does not exist, this is a finding.

## Group: GEN002140

**Group ID:** `V-917`

### Rule: All shells referenced in /etc/passwd must be listed in the /etc/shells file, except any shells specified for the purpose of preventing logins.

**Rule ID:** `SV-45171r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shells file lists approved default shells. It helps provide layered defense to the security approach by ensuring users cannot change their default shell to an unauthorized unsecure shell.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Confirm the login shells referenced in the /etc/passwd file are listed in the /etc/shells file. Procedure: # for USHELL in `cut -d: -f7 /etc/passwd`; do if [ $(grep -c "${USHELL}" /etc/shells) == 0 ]; then echo "${USHELL} not in /etc/shells"; fi; done The /usr/bin/false, /bin/false, /dev/null, /sbin/nologin, /bin/sync, /sbin/halt, /sbin/shutdown, (and equivalents), and sdshell will be considered valid shells for use in the /etc/passwd file, but will not be listed in the /etc/shells file. If a shell referenced in /etc/passwd is not listed in the shells file, excluding the above mentioned shells, this is a finding.

## Group: GEN000760

**Group ID:** `V-918`

### Rule: Accounts must be locked upon 35 days of inactivity.

**Rule ID:** `SV-44882r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>On some systems, accounts with disabled passwords still allow access using rcp, remsh, or rlogin through equivalent remote hosts. All that is required is the remote host name and the user name match an entry in a hosts.equiv file and have a .rhosts file in the user directory. Using a shell called /bin/false or /dev/null (or an equivalent) will add a layered defense. Non-interactive accounts on the system, such as application accounts, may be documented exceptions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Indications of inactive accounts are those that have no entries in the last log. Check the date in the last log to verify it is within the last 35 days or the maximum number of days set by the site if more restrictive. If an inactive account is not disabled via an entry in the password field in the /etc/passwd or /etc/shadow (or equivalent), check the /etc/passwd file to check if the account has a valid shell. If an inactive account is found not disabled, this is a finding. Procedure: Obtain a list of all active(not locked) accounts: # for ACCT in $(cut -d: -f1 /etc/passwd) do if [ "$(passwd -S ${ACCT}| awk '{print $2}')" != "LK" ] then lastlog -u ${ACCT} | awk '{ if(NR>1) printf "%-23s %3s %2s %4s\n", $1, $4, $5, $8}' fi done Obtain a list of all accounts that have logged in during the past 35 days: # lastlog -t 35 | awk '{if(NR>1) printf "%-23s %3s %2s %4s\n", $1, $4, $5, $8}’ Compare the results of the two commands. Any account listed by the first command that is not also listed by the second command has been inactive for 35 days.

## Group: GEN002200

**Group ID:** `V-921`

### Rule: All shell files must be owned by root or bin.

**Rule ID:** `SV-45172r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If shell files are owned by users other than root or bin, they could be modified by intruders or malicious users to perform unauthorized actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the system shells. # cat /etc/shells | xargs -n1 ls -l If any shell is not owned by root or bin, this is a finding.

## Group: GEN002220

**Group ID:** `V-922`

### Rule: All shell files must have mode 0755 or less permissive.

**Rule ID:** `SV-45174r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Shells with world/group write permissions give the ability to maliciously modify the shell to obtain unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If /etc/shells exists, check the group ownership of each shell referenced. # cat /etc/shells | xargs -n1 ls -l Otherwise, check any shells found on the system. # find / -name "*sh" | xargs -n1 ls -l If a shell has a mode more permissive than 0755, this is a finding.

## Group: GEN002260

**Group ID:** `V-923`

### Rule: The system must be checked for extraneous device files at least weekly.

**Rule ID:** `SV-45176r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If an unauthorized device is allowed to exist on the system, there is the possibility the system may perform unauthorized operations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for an automated job, or check with the SA, to determine if the system is checked for extraneous device files on a weekly basis. If no automated or manual process is in place, this is a finding.

## Group: GEN002280

**Group ID:** `V-924`

### Rule: Device files and directories must only be writable by users with a system account or as configured by the vendor.

**Rule ID:** `SV-45177r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System device files in writable directories could be modified, removed, or used by an unprivileged user to control system hardware.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Find all world-writable device files existing anywhere on the system. Procedure: # find / -perm -2 -a \( -type b -o -type c \) > devicelist Check the permissions on the directories above subdirectories containing device files. If any of the device files or their parent directories are world-writable, excepting device files specifically intended to be world-writable such as /dev/null, this is a finding.

## Group: GEN002300

**Group ID:** `V-925`

### Rule: Device files used for backup must only be readable and/or writable by root or the backup user.

**Rule ID:** `SV-45178r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System backups could be accidentally or maliciously overwritten and destroy the ability to recover the system if a compromise should occur. Unauthorized users could also copy system files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for world-writable device files. Procedure: # find / -perm -2 -a \( -type b -o -type c \) -exec ls -ld {} \; If any device file(s) used for backup are writable by users other than root, this is a finding.

## Group: GEN005740

**Group ID:** `V-928`

### Rule: The Network File System (NFS) export configuration file must be owned by root.

**Rule ID:** `SV-46117r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of the NFS export configuration file to root provides the designated owner and possible unauthorized users with the potential to change system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the owner of the exports file. Example: # ls -lL /etc/exports If the export configuration file is not owned by root, this is a finding.

## Group: GEN005760

**Group ID:** `V-929`

### Rule: The Network File System (NFS) export configuration file must have mode 0644 or less permissive.

**Rule ID:** `SV-46119r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Excessive permissions on the NFS export configuration file could allow unauthorized modification of the file, which could result in Denial of Service to authorized NFS exports and the creation of additional unauthorized exports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ls -lL /etc/exports If the file has a mode more permissive than 0644, this is a finding.

## Group: GEN005800

**Group ID:** `V-931`

### Rule: All Network File System (NFS) exported system files and system directories must be owned by root.

**Rule ID:** `SV-46121r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of sensitive files or directories to root provides the designated owner and possible unauthorized users with the potential to access sensitive information or change system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the nfs-kernel-server package is installed. It contains the exportfs command as well as the nfsserver process itself. # rpm –q nfs-kernel-server If the package is not installed, this check does not apply. If it is installed, check for NFS exported file systems. Procedure: # cat /etc/exports For each file system displayed, check the ownership. # ls -lLa <exported file system path> If the files and directories are not owned by root, this is a finding.

## Group: GEN005820

**Group ID:** `V-932`

### Rule: The Network File System (NFS) anonymous UID and GID must be configured to values without permissions.

**Rule ID:** `SV-46123r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When an NFS server is configured to deny remote root access, a selected UID and GID are used to handle requests from the remote root user. The UID and GID should be chosen from the system to provide the appropriate level of non-privileged access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the nfs-kernel-server package is installed. It contains the exportfs command as well as the nfsserver process itself. # rpm –q nfs-kernel-server If the package is not installed, this check does not apply. If it is installed, check if the 'anonuid' and 'anongid' options are set correctly for exported file systems. List exported filesystems: # exportfs -v Each of the exported file systems should include an entry for the 'anonuid=' and 'anongid=' options set to "-1" or an equivalent (60001, 65534, or 65535). If appropriate values for 'anonuid' or 'anongid' are not set, this is a finding.

## Group: GEN005840

**Group ID:** `V-933`

### Rule: The Network File System (NFS) server must be configured to restrict file system access to local hosts.

**Rule ID:** `SV-46124r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The NFS access option limits user access to the specified level. This assists in protecting exported file systems. If access is not restricted, unauthorized hosts may be able to access the system's NFS exports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the nfs-kernel-server package is installed. It contains the exportfs command as well as the nfsserver process itself. # rpm –q nfs-kernel-server If the package is not installed, this check does not apply. If it is installed, check the permissions on exported NFS file systems. Procedure: # exportfs -v If the exported file systems do not contain the ‘rw’ or ‘ro’ options specifying a list of hosts or networks, this is a finding.

## Group: GEN005880

**Group ID:** `V-935`

### Rule: The Network File System (NFS) server must not allow remote root access.

**Rule ID:** `SV-46125r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the NFS server allows root access to local file systems from remote hosts, this access could be used to compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Information Assurance Manager</Responsibility><IAControls></IAControls>

**Check Text:**
List the exports. # cat /etc/exports If any export contains "no_root_squash" or does not contain "root_squash" or "all_squash", this is a finding.

## Group: GEN005900

**Group ID:** `V-936`

### Rule: The nosuid option must be enabled on all Network File System (NFS) client mounts.

**Rule ID:** `SV-46126r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling the nosuid mount option prevents the system from granting owner or group-owner privileges to programs with the suid or sgid bit set. If the system does not restrict this access, users with unprivileged access to the local system may be able to acquire privileged access by executing suid or sgid files located on the mounted NFS file system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Information Assurance Manager</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for NFS mounts not using the "nosuid" option. Procedure: # mount -v | grep " type nfs " | egrep -v "nosuid" If the mounted file systems do not have the "nosuid" option, this is a finding.

## Group: GEN006580

**Group ID:** `V-940`

### Rule: The system must use an access control program.

**Rule ID:** `SV-45929r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access control programs (such as TCP_WRAPPERS) provide the ability to enhance system security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The tcp_wrappers package is provided with the SLES mainframe distribution. Other access control programs may be available but will need to be checked manually. Determine if tcp_wrappers (i.e. TCPd) is installed. # rpm -qa | grep tcpd If no package is listed, this is a finding.

## Group: GEN006600

**Group ID:** `V-941`

### Rule: The systems access control program must log each system access attempt.

**Rule ID:** `SV-45930r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If access attempts are not logged, then multiple attempts to log on to the system by an unauthorized user may go undetected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The tcp_wrappers package (i.e. tcpd) is provided with the SLES mainframe distribution. Other access control programs may be available but will need to be checked manually. Normally, tcpd logs to the mail facility in "/etc/syslog.conf". Determine if syslog is configured to log events by tcpd. Procedure: # more /etc/syslog.conf Look for entries similar to the following: mail.debug /var/adm/maillog mail.none /var/adm/maillog mail.* /var/log/mail authpriv.info /var/log/messages The above entries would indicate mail alerts are being logged. If no entries for mail exist, then tcpd is not logging this is a finding. If an alternate access control program is used and it does not provide logging of access attempts, this is a finding.

## Group: GEN002960

**Group ID:** `V-974`

### Rule: Access to the cron utility must be controlled using the cron.allow and/or cron.deny file(s).

**Rule ID:** `SV-45568r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The cron facility allows users to execute recurring jobs on a regular and unattended basis. The cron.allow file designates accounts allowed to enter and execute jobs using the cron facility. If neither cron.allow nor cron.deny exists, then any account may use the cron facility. This may open the facility up for abuse by system intruders and malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the cron.allow and cron.deny files. # ls -lL /etc/cron.allow # ls -lL /etc/cron.deny If neither file exists, this is a finding.

## Group: GEN002980

**Group ID:** `V-975`

### Rule: The cron.allow file must have mode 0600 or less permissive.

**Rule ID:** `SV-45573r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A readable and/or writable cron.allow file by users other than root could allow potential intruders and malicious users to use the file contents to help discern information, such as who is allowed to execute cron programs, which could be harmful to overall system and network security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check mode of the cron.allow file. Procedure: # ls -lL /etc/cron.allow If the file has a mode more permissive than 0600, this is a finding.

## Group: GEN003000

**Group ID:** `V-976`

### Rule: Cron must not execute group-writable or world-writable programs.

**Rule ID:** `SV-45576r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cron executes group-writable or world-writable programs, there is a possibility that unauthorized users could manipulate the programs with malicious intent. This could compromise system and network security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
List all cronjobs on the system. Procedure: # ls /var/spool/cron /var/spool/cron/tabs # ls /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls /etc/cron*|grep -v deny If cron jobs exist under any of the above directories, use the following command to search for programs executed by cron: # more <cron job file> Perform a long listing of each program file found in the cron file to determine if the file is group-writable or world-writable. # ls -la <cron program file> If cron executes group-writable or world-writable files, this is a finding.

## Group: GEN003020

**Group ID:** `V-977`

### Rule: Cron must not execute programs in, or subordinate to, world-writable directories.

**Rule ID:** `SV-45580r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cron programs are located in or subordinate to world-writable directories, they become vulnerable to removal and replacement by malicious users or system intruders.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
List all cronjobs on the system. Procedure: # ls /var/spool/cron /var/spool/cron/tabs # ls /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls /etc/cron*|grep -v deny If cron jobs exist under any of the above directories, use the following command to search for programs executed by at: # more <cron job file> Perform a long listing of each directory containing program files found in the cron file to determine if the directory is world-writable. # ls -ld <cron program directory> If cron executes programs in world-writable directories, this is a finding.

## Group: GEN003080

**Group ID:** `V-978`

### Rule: Crontab files must have mode 0600 or less permissive.

**Rule ID:** `SV-45600r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of scheduled system jobs and prevent malicious modification to these jobs, crontab files must be secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the crontab files. # ls -lL /etc/crontab /var/spool/cron/ /var/spool/cron/tabs/ If any crontab file has a mode more permissive than 0600, this is a finding.

## Group: GEN003100

**Group ID:** `V-979`

### Rule: Cron and crontab directories must have mode 0755 or less permissive.

**Rule ID:** `SV-45602r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of scheduled system jobs and to prevent malicious modification to these jobs, crontab files must be secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the crontab directories. Procedure: # ls -ld /var/spool/cron /var/spool/cron/tabs ls -ld /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls -ld /etc/cron*|grep -v deny If the mode of any of the crontab directories is more permissive than 0755, this is a finding.

## Group: GEN003120

**Group ID:** `V-980`

### Rule: Cron and crontab directories must be owned by root or bin.

**Rule ID:** `SV-45604r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incorrect ownership of the cron or crontab directories could permit unauthorized users the ability to alter cron jobs and run automated jobs as privileged users. Failure to give ownership of cron or crontab directories to root or to bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the owner of the crontab directories. Procedure: # ls -ld /var/spool/cron /var/spool/cron/tabs ls -ld /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls -ld /etc/cron*|grep -v deny If the owner of any of the crontab directories is not root or bin, this is a finding.

## Group: GEN003140

**Group ID:** `V-981`

### Rule: Cron and crontab directories must be group-owned by root, sys, bin or cron.

**Rule ID:** `SV-45609r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of scheduled system jobs and to prevent malicious modification to these jobs, crontab files must be secured. Failure to give group-ownership of cron or crontab directories to a system group provides the designated group and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group owner of cron and crontab directories. Procedure: # ls -ld /var/spool/cron /var/spool/cron/tabs ls -ld /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls -ld /etc/cron*|grep -v deny If a directory is not group-owned by root, sys, bin, or cron, this is a finding.

## Group: GEN003160

**Group ID:** `V-982`

### Rule: Cron logging must be implemented.

**Rule ID:** `SV-45615r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron logging can be used to trace the successful or unsuccessful execution of cron jobs. It can also be used to spot intrusions into the use of the cron facility by unauthorized and malicious users. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
By default, rsyslog includes configuration files found in the /etc/rsyslog.d directory. Check for the include directive” $IncludeConfig /etc/rsyslog.d/*.conf” in /etc/rsyslog.conf and then for the cron log configuration file. # grep rsyslog.d /etc/rsyslog.conf # grep cron /etc/rsyslog.d/*.conf OR # grep cron /etc/rsyslog.conf If cron logging is not configured, this is a finding. Check the configured cron log file found in the cron entry of /etc/syslog (normally /var/log/cron). # ls -lL /var/log/cron If this file does not exist, or is older than the last cron job, this is a finding.

## Group: GEN003180

**Group ID:** `V-983`

### Rule: The cronlog file must have mode 0600 or less permissive.

**Rule ID:** `SV-45619r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron logs contain reports of scheduled system activities and must be protected from unauthorized access or manipulation. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the cron log file. Procedure: Check the configured cron log file found in the cron entry of the rsyslog configuration (normally /var/log/cron). # grep cron /etc/rsyslog.conf /etc/rsyslog.d/*.conf # ls -lL /var/log/cron If the mode is more permissive than 0600, this is a finding.

## Group: GEN003280

**Group ID:** `V-984`

### Rule: Access to the at utility must be controlled via the at.allow and/or at.deny file(s).

**Rule ID:** `SV-45648r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "at" facility selectively allows users to execute jobs at deferred times. It is usually used for one-time jobs. The at.allow file selectively allows access to the "at" facility. If there is no at.allow file, there is no ready documentation of who is allowed to submit "at" jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the “at” package is not installed, this is not applicable. Check for the existence of at.allow and at.deny files. # ls -lL /etc/at.allow # ls -lL /etc/at.deny If neither file exists, this is a finding.

## Group: GEN003300

**Group ID:** `V-985`

### Rule: The at.deny file must not be empty if it exists.

**Rule ID:** `SV-45649r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>On some systems, if there is no at.allow file and there is an empty at.deny file, then the system assumes everyone has permission to use the "at" facility. This could create an insecure setting in the case of malicious users or system intruders.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
# more /etc/at.deny If the at.deny file exists and is empty, this is a finding.

## Group: GEN003320

**Group ID:** `V-986`

### Rule: Default system accounts (with the exception of root) must not be listed in the at.allow file or must be included in the at.deny file if the at.allow file does not exist.

**Rule ID:** `SV-45656r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Default accounts, such as bin, sys, adm, uucp, daemon, and others, should never have access to the "at" facility. This would create a possible vulnerability open to intruders or malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# more /etc/at.allow If default accounts (such as bin, sys, adm, and others) are listed in the at.allow file, this is a finding.

## Group: GEN003340

**Group ID:** `V-987`

### Rule: The at.allow file must have mode 0600 or less permissive.

**Rule ID:** `SV-45667r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permissions more permissive than 0600 (read, write and execute for the owner) may allow unauthorized or malicious access to the at.allow and/or at.deny files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the at.allow file. # ls -lL /etc/at.allow If the at.allow file has a mode more permissive than 0600, this is a finding.

## Group: GEN003360

**Group ID:** `V-988`

### Rule: The at daemon must not execute group-writable or world-writable programs.

**Rule ID:** `SV-45668r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "at" facility executes world-writable or group-writable programs, it is possible for the programs to be accidentally or maliciously changed or replaced without the owner's intent or knowledge. This would cause a system security breach.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
List the "at" jobs on the system. Procedure: # ls -la /var/spool/at /var/spool/atjobs For each "at" job file, determine which programs are executed. Procedure: # more <at job file> Check the each program executed by "at" for group- or world-writable permissions. Procedure: # ls -la <at program file> If "at" executes group or world-writable programs, this is a finding.

## Group: GEN003380

**Group ID:** `V-989`

### Rule: The at daemon must not execute programs in, or subordinate to, world-writable directories.

**Rule ID:** `SV-45669r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If "at" programs are located in, or subordinate, to world-writable directories, they become vulnerable to removal and replacement by malicious users or system intruders.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
List any "at" jobs on the system. Procedure: # ls /var/spool/at /var/spool/atjobs For each "at" job, determine which programs are executed by "at." Procedure: # more <at job file> Check the directory containing each program executed by "at" for world-writable permissions. Procedure: # ls -la <at program file directory> If "at" executes programs in world-writable directories, this is a finding.

## Group: GEN005300

**Group ID:** `V-993`

### Rule: SNMP communities, users, and passphrases must be changed from the default.

**Rule ID:** `SV-45941r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Whether active or not, default SNMP passwords, users, and passphrases must be changed to maintain security. If the service is running with the default authenticators, then anyone can gather data about the system and the network and use the information to potentially compromise the integrity of the system or network(s).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SNMP configuration for default passwords. Procedure: Examine the default install location /etc/snmp/snmpd.conf or: # find / -name snmpd.conf # more <snmpd.conf file> Identify any community names or user password configuration. If any community name or password is set to a default value such as "public", "private", "snmp-trap", or "password", or any value which does not meet DISA password requirements, this is a finding.

## Group: GEN005320

**Group ID:** `V-994`

### Rule: The snmpd.conf file must have mode 0600 or less permissive.

**Rule ID:** `SV-45955r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The snmpd.conf file contains authenticators and must be protected from unauthorized access and modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the SNMP daemon configuration file. Procedure: Examine the default install location /etc/snmp/snmpd.conf or: # find / -name snmpd.conf # ls -lL <snmpd.conf file> If the snmpd.conf file has a mode more permissive than 0600, this is a finding.

## Group: GEN005340

**Group ID:** `V-995`

### Rule: Management Information Base (MIB) files must have mode 0640 or less permissive.

**Rule ID:** `SV-45961r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to read the MIB file could impart special knowledge to an intruder or malicious user about the ability to extract compromising information about the system or network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the modes for all Management Information Base (MIB) files on the system. Procedure: # find / -name *mib* -o -name *MIB* | xargs ls -lL Any file returned with a mode 0640 or less permissive is a finding.

## Group: GEN002480

**Group ID:** `V-1010`

### Rule: Public directories must be the only world-writable directories and world-writable files must be located only in public directories.

**Rule ID:** `SV-45201r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>World-writable files and directories make it easy for a malicious user to place potentially compromising files on the system. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for world-writable files. Procedure: # find / -perm -2 -a \( -type d -o -type f \) -exec ls -ld {} \; If any world-writable files are located, except those required for system operation such as /tmp and /dev/null, this is a finding.

## Group: GEN003800

**Group ID:** `V-1011`

### Rule: Inetd or xinetd logging/tracing must be enabled.

**Rule ID:** `SV-45783r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inetd or xinetd logging and tracing allows the system administrators to observe the IP addresses connecting to their machines and what network services are being sought. This provides valuable information when trying to find the source of malicious users and potential malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The /etc/xinetd.conf file and each file in the /etc/xinetd.d directory file should be examined for the following: Procedure: log_type = SYSLOG authpriv log_on_success = HOST PID USERID EXIT log_on_failure = HOST USERID If xinetd is running and logging is not enabled, this is a finding.

## Group: GEN006240

**Group ID:** `V-1023`

### Rule: The system must not run an Internet Network News (INN) server.

**Rule ID:** `SV-46142r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>INN servers access Usenet newsfeeds and store newsgroup articles. INN servers use the Network News Transfer Protocol (NNTP) to transfer information from the Usenet to the server and from the server to authorized remote hosts. If this function is necessary to support a valid mission requirement, its use must be authorized and approved in the system accreditation package.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
# ps -ef | egrep "innd|nntpd" If an Internet Network News server is running, this is a finding.

## Group: GEN000000-LNX00400

**Group ID:** `V-1025`

### Rule: The /etc/access.conf file must be owned by root.

**Rule ID:** `SV-44652r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/access.conf file contains entries restricting access from the system console by authorized System Administrators. If the file is owned by a user other than root, it could compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check access configuration ownership: # ls -lL /etc/security/access.conf If this file exists and is not owned by root, this is a finding.

## Group: GEN006080

**Group ID:** `V-1026`

### Rule: The Samba Web Administration Tool (SWAT) must be restricted to the local host or require SSL.

**Rule ID:** `SV-46130r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SWAT is a tool used to configure Samba. It modifies Samba configuration, which can impact system security, and must be protected from unauthorized access. SWAT authentication may involve the root password, which must be protected by encryption when traversing the network. Restricting access to the local host allows for the use of SSH TCP forwarding, if configured, or administration by a web browser on the local system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
SWAT is a tool for configuring Samba and should only be found on a system with a requirement for Samba. If SWAT is used, it must be utilized with SSH to ensure a secure connection between the client and the server. Procedure: # grep -H "bin/swat" /etc/xinetd.d/*|cut -d: -f1 |xargs grep "only_from" If the value of the "only_from" line in the "xinetd.d" file which starts with "/usr/sbin/swat" does not contain "localhost" or the equivalent, this is a finding.

## Group: GEN006100

**Group ID:** `V-1027`

### Rule: The /etc/smb.conf file must be owned by root.

**Rule ID:** `SV-46131r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/smb.conf file allows access to other machines on the network and grants permissions to certain users. If it is owned by another user, the file may be maliciously modified and the Samba configuration could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the /etc/samba/smb.conf file. Procedure: # ls -l /etc/samba/smb.conf If an smb.conf file is not owned by root, this is a finding.

## Group: GEN006140

**Group ID:** `V-1028`

### Rule: The /etc/smb.conf file must have mode 0644 or less permissive.

**Rule ID:** `SV-46133r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "smb.conf" file has excessive permissions, the file may be maliciously modified and the Samba configuration could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the smb.conf file. Procedure: # ls -lL /etc/samba/smb.conf If the "smb.conf" has a mode more permissive than 0644, this is a finding.

## Group: GEN006160

**Group ID:** `V-1029`

### Rule: The /etc/smbpasswd file must be owned by root.

**Rule ID:** `SV-46135r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "smbpasswd" file is not owned by root, it may be maliciously accessed or modified, potentially resulting in the compromise of Samba accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the "smbpasswd" file. # ls -l /etc/samba/passdb.tdb /etc/samba/secrets.tdb If the "smbpasswd" file is not owned by root, this is a finding.

## Group: GEN006220

**Group ID:** `V-1030`

### Rule: The smb.conf file must use the hosts option to restrict access to Samba.

**Rule ID:** `SV-46139r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Samba increases the attack surface of the system and must be restricted to communicate only with systems requiring access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "smb.conf" file. # more /etc/samba/smb.conf If the "hosts" option is not present to restrict access to a list of authorized hosts and networks, this is a finding.

## Group: GEN000540

**Group ID:** `V-1032`

### Rule: Users must not be able to change passwords more than once every 24 hours.

**Rule ID:** `SV-44859r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to change passwords frequently facilitates users reusing the same password. This can result in users effectively never changing their passwords. This would be accomplished by users changing their passwords when required and then immediately changing it to the original value. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the minimum time period between password changes for each user account is 1 day. # cat /etc/shadow | cut -d ':' -f 4 | grep -v 1 If any results are returned, this is a finding.

## Group: GEN001100

**Group ID:** `V-1046`

### Rule: Root passwords must never be passed over a network in clear text form.

**Rule ID:** `SV-44919r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If a user accesses the root account (or any account) using an unencrypted connection, the password is passed over the network in clear text form and is subject to interception and misuse. This is true even if recommended procedures are followed by logging on to a named account and using the su command to access root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if root has logged in over an unencrypted network connection. First determine if root has logged in over a network. Procedure: # last | grep "^root " | egrep -v "reboot| |ttyS0" | more If root has logged in over the network, this is a finding.

## Group: GEN001120

**Group ID:** `V-1047`

### Rule: The system must not permit root logins using remote access programs such as ssh.


**Rule ID:** `SV-44922r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Even though communications are encrypted, an additional layer of security may be gained by extending the policy of not logging directly on as root. In addition, logging in with a user-specific account preserves the audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the SSH daemon is configured to permit root logins. Procedure: # grep -v "^#" /etc/ssh/sshd_config | grep -i permitrootlogin If the PermitRootLogin entry is not found or is not set to "no", this is a finding.

## Group: GEN000000-LNX00420

**Group ID:** `V-1054`

### Rule: The /etc/access.conf file must have a privileged group owner.

**Rule ID:** `SV-44653r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Depending on the access restrictions of the /etc/access.conf file, if the group owner were not a privileged group, it could endanger system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check access configuration group ownership: # ls -lL /etc/security/access.conf If this file exists and has a group-owner that is not a privileged user, this is a finding.

## Group: GEN000000-LNX00440

**Group ID:** `V-1055`

### Rule: The /etc/security/access.conf file must have mode 0640 or less permissive.

**Rule ID:** `SV-46089r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the access permissions are more permissive than 0640, system security could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check access configuration mode: # ls -lL /etc/security/access.conf If this file exists and has a mode more permissive than 0640, this is a finding.

## Group: GEN006120

**Group ID:** `V-1056`

### Rule: The /etc/smb.conf file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46132r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the group owner of the "smb.conf" file is not root or a system group, the file may be maliciously modified and the Samba configuration could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the "smb.conf" file. Procedure: # ls -lL /etc/samba/smb.conf If the "smb.conf" file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN006180

**Group ID:** `V-1058`

### Rule: The smbpasswd file must be group-owned by root.

**Rule ID:** `SV-46136r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the smbpasswd file is not group-owned by root, the smbpasswd file may be maliciously accessed or modified, potentially resulting in the compromise of Samba accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check "smbpasswd" ownership: # ls -lL /etc/samba/passdb.tdb /etc/samba/secrets.tdb If the "smbpasswd" file is not group-owned by root, this is a finding.

## Group: GEN006200

**Group ID:** `V-1059`

### Rule: The smbpasswd file must have mode 0600 or less permissive.

**Rule ID:** `SV-46137r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the smbpasswd file has a mode more permissive than 0600, the smbpasswd file may be maliciously accessed or modified, potentially resulting in the compromise of Samba accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of files maintained using "smbpasswd". Procedure: # ls -lL /etc/samba/passdb.tdb /etc/samba/secrets.tdb If a "smbpasswd" maintained file has a mode more permissive than 0600, this is a finding.

## Group: GEN001080

**Group ID:** `V-1062`

### Rule: The root shell must be located in the / file system.


**Rule ID:** `SV-44918r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To ensure the root shell is available in repair and administrative modes, the root shell must be located in the / file system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if roots shell executable resides on a dedicated file system. Procedure: Find the location of the root users shell # grep "^root" /etc/passwd|cut -d: -f7|cut -d/ -f2 The result is the top level directory under / where the shell resides (ie. usr) Check if it is on a dedicated file system. # grep /<top level directory> /etc/fstab If /<top level directory> is on a dedicated file system, this is a finding.

## Group: GEN000800

**Group ID:** `V-4084`

### Rule: The system must prohibit the reuse of passwords within five iterations.

**Rule ID:** `SV-44884r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user, or root, used the same password continuously or was allowed to change it back shortly after being forced to change it to something else, it would provide a potential intruder with the opportunity to keep guessing at one user's password until it was guessed correctly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# pam-config -q --pwhistory If the result is not’ password: remember=5’ or higher, then this is a finding. # ls /etc/security/opasswd If /etc/security/opasswd does not exist, then this is a finding. # grep password /etc/pam.d/common-password| grep pam_pwhistory.so | grep remember If the "remember" option in /etc/pam.d/common-password is not 5 or greater, this is a finding.

## Group: GEN001940

**Group ID:** `V-4087`

### Rule: User start-up files must not execute world-writable programs.

**Rule ID:** `SV-45162r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If start-up files execute world-writable programs, especially in unprotected directories, they could be maliciously modified to become trojans that destroy user files or otherwise compromise the system at the user, or higher, level. If the system is compromised at the user level, it is much easier to eventually compromise the system at the root and network level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check local initialization files for any executed world-writable programs or scripts and scripts executing from world writable directories. Procedure: For each home directory on the system make a list of files referenced within any local initialization script. Show the mode for each file and its parent directory. # FILES=".bashrc .bash_login .bash_logout .bash_profile .cshrc .kshrc .login .logout .profile .tcshrc .env .dtprofile .dispatch .emacs .exrc"; # for HOMEDIR in `cut -d: -f6 /etc/passwd|sort|uniq`;do for INIFILE in $FILES;do REFLIST=`egrep " [\"~]?/" ${HOMEDIR}/${INIFILE} 2>/dev/null|sed "s/.*\([~ \"]\/[\.0-9A-Za-z_\/\-]*\).*/\1/"`;for REFFILE in $REFLIST;do FULLREF=`echo $REFFILE|sed "s:\~:${HOMEDIR}:g"|sed "s:^\s*::g"`;dirname $FULLREF|xargs stat -c "dir:%a:%n";stat -c "file:%:%n" $FULLREF;done;done; done|sort|uniq If any local initialization file executes a world-writable program or script or a script from a world-writable directory, this is a finding.

## Group: GEN001660

**Group ID:** `V-4089`

### Rule: All system start-up files must be owned by root.

**Rule ID:** `SV-45073r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System start-up files not owned by root could lead to system compromise by allowing malicious users or applications to modify them for unauthorized purposes. This could lead to system and network compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check run control scripts' ownership. # ls -lL /etc/rc* /etc/init.d Alternatively: # find /etc -name "[SK][0-9]*"|xargs stat -L -c %U:%n If any run control script is not owned by root or bin, this is a finding.

## Group: GEN001680

**Group ID:** `V-4090`

### Rule: All system start-up files must be group-owned by root, sys, bin, other, or system.

**Rule ID:** `SV-45091r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If system start-up files do not have a group owner of root or a system group, the files may be modified by malicious users or intruders.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check run control scripts' group ownership. Procedure: # ls -lL /etc/rc* /etc/init.d Alternatively: # find /etc -name "[SK][0-9]*"|xargs stat -L -c %G:%n|egrep -v "^(root|sys|bin|other):" If any run control script is not group-owned by root, sys, bin, or other system groups, this is a finding.

## Group: GEN001700

**Group ID:** `V-4091`

### Rule: System start-up files must only execute programs owned by a privileged UID or an application.

**Rule ID:** `SV-45092r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System start-up files executing programs owned by other than root (or another privileged user) or an application indicating the system may have been compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the programs executed by system start-up files. Determine the ownership of the executed programs. # cat /etc/rc*/* /etc/init.d/* | more # ls -l <executed program> Alternatively: # for FILE in `egrep -r "/" /etc/rc.* /etc/init.d|awk '/^.*[^\/][0-9A-Za-z_\/]*/{print $2}'|egrep "^/"|sort|uniq`;do if [ -e $FILE ]; then stat -L -c '%U:%n' $FILE;fi;done This provides a list of files referenced by initialization scripts and their associated UIDs. If any file is run by an initialization file and is not owned by root, sys, bin, or in rare cases, an application account, this is a finding.

## Group: GEN008720

**Group ID:** `V-4250`

### Rule: The systems boot loader configuration file(s) must have mode 0600 or less permissive.

**Rule ID:** `SV-46075r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File permissions greater than 0600 on boot loader configuration files could allow an unauthorized user to view or modify sensitive information pertaining to system boot instructions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/zipl.conf permissions: # ls –lL /etc/zipl.conf If /etc/zipl.conf has a mode more permissive than 0600, then this is a finding.

## Group: GEN000000-LNX00320

**Group ID:** `V-4268`

### Rule: The system must not have special privilege accounts, such as shutdown and halt.

**Rule ID:** `SV-44654r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If special privilege accounts are compromised, the accounts could provide privileges to execute malicious commands on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to check for unnecessary privileged accounts: # grep "^shutdown" /etc/passwd # grep "^halt" /etc/passwd # grep "^reboot" /etc/passwd If any unnecessary privileged accounts exist this is a finding.

## Group: GEN000290

**Group ID:** `V-4269`

### Rule: The system must not have unnecessary accounts.

**Rule ID:** `SV-44804r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for unnecessary user accounts. Procedure: # more /etc/passwd If any unnecessary accounts are found, this is a finding.

## Group: GEN006260

**Group ID:** `V-4273`

### Rule: The /etc/news/incoming.conf (or equivalent) must have mode 0600 or less permissive.

**Rule ID:** `SV-46143r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the "incoming.conf" file may allow unauthorized modification which could lead to Denial-of-Service to authorized users or provide access to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
SUSE ships the InternetNewsDaemon (innd) news server. The file corresponding to "/etc/news/hosts.nntp" is "/etc/news/incoming.conf". Check the permissions for "/etc/news/incoming.conf". # ls -lL /etc/news/incoming.conf If "/etc/news/incoming.conf" has a mode more permissive than 0600, this is a finding.

## Group: GEN006280

**Group ID:** `V-4274`

### Rule: The /etc/news/infeed.conf (or equivalent) must have mode 0600 or less permissive.

**Rule ID:** `SV-46145r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the "" file may allow unauthorized modification which could lead to Denial of Service to authorized users or provide access to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
SUSE ships the InternetNewsDaemon (innd) news server. The file that corresponds to "/etc/news/hosts.nntp.nolimit" is "/etc/news/innfeed.conf". Check the permissions for "/etc/news/innfeed.conf". # ls -lL /etc/news/innfeed.conf If "/etc/news/innfeed.conf" has a mode more permissive than 0600, this is a finding.

## Group: GEN006300

**Group ID:** `V-4275`

### Rule: The /etc/news/readers.conf (or equivalent) must have mode 0600 or less permissive.

**Rule ID:** `SV-45896r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the readers.conf file may allow unauthorized modification which could lead to Denial of Service to authorized users or provide access to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions for "/etc/news/readers.conf". # ls -lL /etc/news/readers.conf If /etc/news/readers.conf has a mode more permissive than 0600, this is a finding.

## Group: GEN006320

**Group ID:** `V-4276`

### Rule: The /etc/news/passwd.nntp file (or equivalent) must have mode 0600 or less permissive.

**Rule ID:** `SV-45898r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File permissions more permissive than 0600 for "/etc/news/passwd.nntp" may allow access to privileged information by system intruders or malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check "/etc/news/passwd.nntp" permissions: # ls -lL /etc/news/passwd.nntp If "/etc/news/passwd.nntp" has a mode more permissive than 0600, this is a finding.

## Group: GEN006340

**Group ID:** `V-4277`

### Rule: Files in /etc/news must be owned by root or news.

**Rule ID:** `SV-45901r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If critical system files are not owned by a privileged user, system integrity could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the files in "/etc/news". Procedure: # ls -al /etc/news If any files are not owned by root or news, this is a finding.

## Group: GEN006360

**Group ID:** `V-4278`

### Rule: The files in /etc/news must be group-owned by root or news.

**Rule ID:** `SV-45905r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If critical system files do not have a privileged group-owner, system integrity could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check "/etc/news" files group ownership: Procedure: # ls -al /etc/news If "/etc/news" files are not group-owned by root or news, this is a finding.

## Group: GEN005500

**Group ID:** `V-4295`

### Rule: The SSH daemon must be configured to only use the SSHv2 protocol.

**Rule ID:** `SV-45997r2_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SSHv1 is not a DoD-approved protocol and has many well-known vulnerability exploits. Exploits of the SSH daemon could provide immediate root access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the sshd_config file: # more /etc/ssh/sshd_config Examine the file. If the variables 'Protocol 2,1’ or ‘Protocol 1’ are defined on a line without a leading comment, this is a finding.

## Group: GEN001000

**Group ID:** `V-4298`

### Rule: Remote consoles must be disabled or protected from unauthorized access.

**Rule ID:** `SV-44914r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The remote console feature provides an additional means of access to the system which could allow unauthorized access if not disabled or properly secured. With virtualization technologies, remote console access is essential as there is no physical console for virtual machines. Remote console access must be protected in the same manner as any other remote privileged access method.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/securetty # more /etc/securetty If the file does not exist, or contains more than "console" or a single "tty" device this is a finding.

## Group: GEN000240

**Group ID:** `V-4301`

### Rule: The system clock must be synchronized to an authoritative DoD time source.

**Rule ID:** `SV-44771r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure the accuracy of the system clock, it must be synchronized with an authoritative time source within DoD. Many system functions, including time-based login and activity restrictions, automated reports, system logs, and audit records depend on an accurate system clock. If there is no confidence in the correctness of the system clock, time-based functions may not operate as intended and records may be of diminished value. Authoritative time sources include authorized time servers within the enclave that synchronize with upstream authoritative sources. Specific requirements for the upstream synchronization of network time protocol (NTP) servers are covered in the Network Other Devices STIG. For systems located on isolated or closed networks, it is not necessary to synchronize with a global authoritative time source. If a global authoritative time source is not available to systems on an isolated network, a local authoritative time source must be established on this network and used by the systems connected to this network. This is necessary to provide the ability to correlate events and allow for the correct operation of time-dependent protocols between systems on the isolated network. If the system is completely isolated (i.e., it has no connections to networks or other systems), time synchronization is not required as no correlation of events between systems will be necessary. If the system is completely isolated, this requirement is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if NTP running: # ps -ef | egrep "xntpd|ntpd" Check if "ntpd -qg" is scheduled to run: # grep "ntpd -qg" /var/spool/cron/* # grep "ntpd -qg" /var/spool/cron/tabs/* # grep "ntpd -qg" /etc/cron.d/* # grep "ntpd -qg" /etc/cron.daily/* # grep "ntpd -qg" /etc/cron.hourly/* # grep "ntpd -qg" /etc/cron.monthly/* # grep "ntpd -qg" /etc/cron.weekly/* If NTP is running or "ntpd -qg" is found: # more /etc/ntp.conf Confirm the timeservers and peers or multicast client (as applicable) are local or authoritative U.S. DoD sources appropriate for the level of classification which the network operates. If a non-local/non-authoritative time-server is used, this is a finding.

## Group: GEN003640

**Group ID:** `V-4304`

### Rule: The root file system must employ journaling or another mechanism ensuring file system consistency.

**Rule ID:** `SV-45753r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File system journaling, or logging, can allow reconstruction of file system data after a system crash, preserving the integrity of data that may have otherwise been lost. Journaling file systems typically do not require consistency checks upon booting after a crash, which can improve system availability. Some file systems employ other mechanisms to ensure consistency also satisfying this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Logging should be enabled for those types of file systems not turning on logging by default. Procedure: # mount JFS, VXFS, HFS, XFS, reiserfs, EXT3 and EXT4 all turn logging on by default and will not be a finding. The ZFS file system uses other mechanisms to provide for file system consistency, and will not be a finding. For other file systems types, if the root file system does not support journaling this is a finding. If the ‘nolog’ option is set on the root file system that does support journaling, this is a finding.

## Group: GEN006060

**Group ID:** `V-4321`

### Rule: The system must not run Samba unless needed.

**Rule ID:** `SV-46129r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Samba is a tool used for the sharing of files and printers between Windows and UNIX operating systems. It provides access to sensitive files and, therefore, poses a security risk if compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for a running Samba server. Procedure: # ps -ef |grep smbd If the Samba server is running, ask the SA if the Samba server is operationally required. If it is not, this is a finding.

## Group: GEN000000-LNX00480

**Group ID:** `V-4334`

### Rule: The /etc/sysctl.conf file must be owned by root.

**Rule ID:** `SV-44655r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sysctl.conf file specifies the values for kernel parameters to be set on boot. These settings can affect the system's security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/sysctl.conf ownership. # ls -lL /etc/sysctl.conf If /etc/sysctl.conf is not owned by root, this is a finding.

## Group: GEN000000-LNX00500

**Group ID:** `V-4335`

### Rule: The /etc/sysctl.conf file must be group-owned by root.

**Rule ID:** `SV-44656r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sysctl.conf file specifies the values for kernel parameters to be set on boot. These settings can affect the system's security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/sysctl.conf group ownership: # ls -lL /etc/sysctl.conf If /etc/sysctl.conf is not group-owned by root, this is a finding.

## Group: GEN000000-LNX00520

**Group ID:** `V-4336`

### Rule: The /etc/sysctl.conf file must have mode 0600 or less permissive.

**Rule ID:** `SV-44657r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sysctl.conf file specifies the values for kernel parameters to be set on boot. These settings can affect the system's security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/sysctl.conf permissions: # ls -lL /etc/sysctl.conf If /etc/sysctl.conf has a mode more permissive than 0600, this is a finding.

## Group: GEN000000-LNX00560

**Group ID:** `V-4339`

### Rule: The Linux NFS Server must not have the insecure file locking option.

**Rule ID:** `SV-44658r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Insecure file locking could allow for sensitive data to be viewed or edited by an unauthorized user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if an NFS server is running on the system by: # ps -ef |grep nfsd If an NFS server is running, confirm it is not configured with the insecure_locks option by: # exportfs -v The example below would be a finding: /misc/export speedy.example.com(rw,insecure_locks)

## Group: GEN000000-LNX00600

**Group ID:** `V-4346`

### Rule: The Linux PAM system must not grant sole access to admin privileges to the first user who logs into the console.

**Rule ID:** `SV-44665r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user has been granted privileged access while logged in at the console, the security posture of a system could be greatly compromised. Additionally, such a situation could deny legitimate root access from another terminal.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the pam_console.so module is not configured in any files in /etc/pam.d by: # cd /etc/pam.d # grep pam_console.so * Or # ls –la /etc/security/console.perms If either the pam_console.so entry or the file /etc/security/console.perms is found then this is a finding.

## Group: GEN002860

**Group ID:** `V-4357`

### Rule: Audit logs must be rotated daily.

**Rule ID:** `SV-45560r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Rotate audit logs daily to preserve audit file system space and to conform to the DoD/DISA requirement. If it is not rotated daily and moved to another location, then there is more of a chance for the compromise of audit data by malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for any crontab entries that rotate audit logs. Procedure: # crontab -l If such a cron job is found, this is not a finding. Otherwise, query the SA. If there is a process automatically rotating audit logs, this is not a finding. If the SA manually rotates audit logs, this is a finding, because if the SA is not there, it will not be accomplished. If the audit output is not archived daily, to tape or disk, this is a finding. This can be ascertained by looking at the audit log directory and, if more than one file is there, or if the file does not have today’s date, this is a finding.

## Group: GEN003200

**Group ID:** `V-4358`

### Rule: The cron.deny file must have mode 0600 or less permissive.

**Rule ID:** `SV-45626r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If file permissions for cron.deny are more permissive than 0600, sensitive information could be viewed or edited by unauthorized users. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the cron.deny file. # ls -lL /etc/cron.deny If the cron.deny file does not exist this is not a finding. If the cron.deny file exists and the mode is more permissive than 0600, this is a finding.

## Group: GEN003220

**Group ID:** `V-4360`

### Rule: Cron programs must not set the umask to a value less restrictive than 077.

**Rule ID:** `SV-45633r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 700 or less permissive. Although umask is often represented as a 4-digit octal number, the first digit representing special access modes is typically ignored or required to be 0.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance>If a cron program sets the umask to 000 or does not restrict the world-writable permission, this becomes a CAT I finding.</SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if there are any crontabs by viewing a long listing of the directory. If there are crontabs, examine them to determine what cron jobs exist. Check for any programs specifying an umask more permissive than 077: Procedure: # ls -lL /var/spool/cron /var/spool/cron/tabs # ls -lL /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls -lL /etc/cron.*|grep -v deny # cat <crontab file> # grep umask <cron program> If there are no cron jobs present, this vulnerability is not applicable. If any cron job contains an umask more permissive than 077, this is a finding.

## Group: GEN003240

**Group ID:** `V-4361`

### Rule: The cron.allow file must be owned by root, bin, or sys.

**Rule ID:** `SV-45637r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the owner of the cron.allow file is not set to root, bin, or sys, the possibility exists for an unauthorized user to view or to edit sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ls -lL /etc/cron.allow If the cron.allow file is not owned by root, sys, or bin, this is a finding.

## Group: GEN003400

**Group ID:** `V-4364`

### Rule: The at directory must have mode 0755 or less permissive.

**Rule ID:** `SV-45670r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "at" directory has a mode more permissive than 0755, unauthorized users could be allowed to view or to edit files containing sensitive information within the "at" directory. Unauthorized modifications could result in Denial of Service to authorized "at" jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the "at" directory. Procedure: # ls -ld /var/spool/at /var/spool/atjobs If the directory mode is more permissive than 0755, this is a finding.

## Group: GEN003420

**Group ID:** `V-4365`

### Rule: The atjobs directory must be owned by root, bin, daemon or at.

**Rule ID:** `SV-45672r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the owner of the "atjobs" directory is not root, bin, daemon or at, unauthorized users could be allowed to view or edit files containing sensitive information within the directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the "at" directory: Procedure: # ls -ld /var/spool/atjobs If the directory is not owned by root, bin, daemon, or at, this is a finding.

## Group: GEN003440

**Group ID:** `V-4366`

### Rule: At jobs must not set the umask to a value less restrictive than 077.

**Rule ID:** `SV-45674r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 700 or less permissive. Although umask is often represented as a 4-digit number, the first digit representing special access modes is typically ignored or required to be 0.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Determine what "at" jobs exist on the system. Procedure: # ls /var/spool/at /var/spool/atjobs If there are no "at" jobs present, this is not applicable. Determine if any of the "at" jobs or any scripts referenced execute the "umask" command. Check for any umask setting more permissive than 077. # grep umask <at job or referenced script> If any "at" job or referenced script sets umask to a value more permissive than 077, this is a finding.

## Group: GEN003460

**Group ID:** `V-4367`

### Rule: The at.allow file must be owned by root, bin, or sys.

**Rule ID:** `SV-45675r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the owner of the at.allow file is not set to root, bin, or sys, unauthorized users could be allowed to view or edit sensitive information contained within the file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ls -lL /etc/at.allow If the at.allow file is not owned by root, sys, or bin, this is a finding.

## Group: GEN003480

**Group ID:** `V-4368`

### Rule: The at.deny file must be owned by root, bin, or sys.

**Rule ID:** `SV-45677r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the owner of the at.deny file is not set to root, bin, or sys, unauthorized users could be allowed to view or edit sensitive information contained within the file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ls -lL /etc/at.deny If the at.deny file is not owned by root, sys, or bin, this is a finding.

## Group: GEN003960

**Group ID:** `V-4369`

### Rule: The traceroute command owner must be root.

**Rule ID:** `SV-45818r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the traceroute command owner has not been set to root, an unauthorized user could use this command to obtain knowledge of the network topology inside the firewall. This information may allow an attacker to determine trusted routers and other network information potentially leading to system and network compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ls -lL /usr/sbin/traceroute If the traceroute command is not owned by root, this is a finding.

## Group: GEN003980

**Group ID:** `V-4370`

### Rule: The traceroute command must be group-owned by sys, bin, root, or system.

**Rule ID:** `SV-45819r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the group owner of the traceroute command has not been set to a system group, unauthorized users could have access to the command and use it to gain information regarding a network's topology inside of the firewall. This information may allow an attacker to determine trusted routers and other network information potentially leading to system and network compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the traceroute file. Procedure: # ls -lL /usr/sbin/traceroute If the traceroute command is not group-owned by root, sys, bin, or system, this is a finding.

## Group: GEN004000

**Group ID:** `V-4371`

### Rule: The traceroute file must have mode 0700 or less permissive.

**Rule ID:** `SV-45822r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the mode of the traceroute executable is more permissive than 0700, malicious code could be inserted by an attacker and triggered whenever the traceroute command is executed by authorized users. Additionally, if an unauthorized user is granted executable permissions to the traceroute command, it could be used to gain information about the network topology behind the firewall. This information may allow an attacker to determine trusted routers and other network information potentially leading to system and network compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ls -lL /usr/sbin/traceroute If the traceroute command has a mode more permissive than 0700, this is a finding.

## Group: GEN004220

**Group ID:** `V-4382`

### Rule: Administrative accounts must not run a web browser, except as needed for local service administration.

**Rule ID:** `SV-45825r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If a web browser flaw is exploited while running as a privileged user, the entire system could be compromised. Specific exceptions for local service administration should be documented in site-defined policy. These exceptions may include HTTP(S)-based tools used for the administration of the local system, services, or attached devices. Examples of possible exceptions are HP’s System Management Homepage (SMH), the CUPS administrative interface, and Sun's StorageTek Common Array Manager (CAM) when these services are running on the local system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to determine if a site-defined policy exists which requires administrative accounts to use web browsers only for local service administration. If a site-defined policy does not exist this is a finding.

## Group: GEN004560

**Group ID:** `V-4384`

### Rule: The SMTP services SMTP greeting must not provide version information.

**Rule ID:** `SV-46278r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The version of the SMTP service can be used by attackers to plan an attack based on vulnerabilities present in the specific version.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To check for the version of either sendmail or Postfix being displayed in the greeting: # telnet localhost 25 If a version number is displayed, this is a finding.

## Group: GEN004580

**Group ID:** `V-4385`

### Rule: The system must not use .forward files.

**Rule ID:** `SV-45868r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The .forward file allows users to automatically forward mail to another system. Use of .forward files could allow the unauthorized forwarding of mail and could potentially create mail loops which could degrade system performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if sendmail is installed # rpm -qa | grep -i sendmail This check only applies to systems that have the sendmail package installed. Check forwarding capability from sendmail. Procedure: grep "0 ForwardPath" /etc/mail/sendmail.cf If the entry contains a file path, this is a finding. Search for any .forward in users home directories on the system by: # for pwline in `cut -d: -f1,6 /etc/passwd`; do homedir=`echo ${pwline}|cut -d: -f2`;username=`echo ${pwline} | cut -d: -f1`;echo $username `stat -c %n $homedir/.forward 2>/dev/null`; done|egrep "\.forward" If any users have a .forward file in their home directory, this is a finding.

## Group: GEN005000

**Group ID:** `V-4387`

### Rule: Anonymous FTP accounts must not have a functional shell.

**Rule ID:** `SV-45886r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an anonymous FTP account has been configured to use a functional shell, attackers could gain access to the shell if the account is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the shell for the anonymous FTP account. Procedure: # grep "^ftp" /etc/passwd This is a finding if the seventh field is empty (the entry ends with a ':') or if the seventh field does not contain one of the following: /bin/false /dev/null /usr/bin/false /bin/true /sbin/nologin

## Group: GEN005020

**Group ID:** `V-4388`

### Rule: The anonymous FTP account must be configured to use chroot or a similarly isolated environment.

**Rule ID:** `SV-46157r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an anonymous FTP account does not use a chroot or similarly isolated environment, the system may be more vulnerable to exploits against the FTP service. Such exploits could allow an attacker to gain shell access to the system and view, edit, or remove sensitive files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
For vsftp: The FTP anonymous user is, by default, chrooted to the ftp users home directory as defined in the /etc/passwd file. This is integral to the server and may not be disabled.

## Group: GEN005380

**Group ID:** `V-4392`

### Rule: If the system is a Network Management System (NMS) server, it must only run the NMS and any software required by the NMS.

**Rule ID:** `SV-45971r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installing extraneous software on a system designated as a dedicated Network Management System (NMS) server poses a security threat to the system and the network. Should an attacker gain access to the NMS through unauthorized software, the entire network may be susceptible to malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if this is an NMS server. If it is an NMS server, then ask what other applications run on it. If there is anything other than network management software and DBMS software used only for the storage and inquiry of NMS data, this is a finding.

## Group: GEN005400

**Group ID:** `V-4393`

### Rule: The /etc/rsyslog.conf file must be owned by root.

**Rule ID:** `SV-45976r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the /etc/syslog.conf file is not owned by root, unauthorized users could be allowed to view, edit, or delete important system messages handled by the syslog facility.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/rsyslog.conf ownership: # ls –lL /etc/rsyslog* If any rsyslog configuration file is not owned by root, this is a finding.

## Group: GEN005420

**Group ID:** `V-4394`

### Rule: The /etc/rsyslog.conf file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45978r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the group owner of /etc/syslog.conf is not root, bin, or sys, unauthorized users could be permitted to view, edit, or delete important system messages handled by the syslog facility.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/rsyslog.conf group ownership. Procedure: # ls -lL /etc/rsyslog* If any rsyslog.conf file is not group owned by root, sys, bin, or system, this is a finding.

## Group: GEN005460

**Group ID:** `V-4395`

### Rule: The system must only use remote syslog servers (log hosts) that is justified and documented using site-defined procedures.

**Rule ID:** `SV-45989r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a remote log host is in use and it has not been justified and documented with the IAO, sensitive information could be obtained by unauthorized users without the SA's knowledge. A remote log host is any host to which the system is sending syslog messages over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Examine the rsyslog.conf file for any references to remote log hosts. # grep -v "^#" /etc/rsyslog* | grep '@' # grep -v "^#" /etc/rsyslog.d/* | grep '@' Destination locations beginning with an '@' represent log hosts. If the log host name is a local alias such as "loghost", consult the /etc/hosts or other name databases as necessary to obtain the canonical name or address for the log host. Determine if the host referenced is a log host documented using site-defined procedures. If an undocumented log host is referenced, this is a finding.

## Group: GEN005560

**Group ID:** `V-4397`

### Rule: The system must be configured with a default gateway for IPv4 if the system uses IPv4, unless the system is a router.

**Rule ID:** `SV-46110r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a system has no default gateway defined, the system is at increased risk of man-in-the-middle, monitoring, and Denial of Service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for an IPv4 default route Procedure: # netstat -r |grep default If a default route is not defined, this is a finding.

## Group: GEN005580

**Group ID:** `V-4398`

### Rule: A system used for routing must not run other network services or applications.

**Rule ID:** `SV-46112r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installing extraneous software on a system designated as a dedicated router poses a security threat to the system and the network. Should an attacker gain access to the router through the unauthorized software, the entire network is susceptible to malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the system is a VM host and acts as a router solely for the benefit of its client systems, then this rule is not applicable. Ask the SA if the system is a designated router. If it is not, this is not applicable. Check the system for non-routing network services. Procedure: # netstat -a | grep -i listen # ps -ef If non-routing services, including Web servers, file servers, DNS servers, or applications servers, but excluding management services such as SSH and SNMP, are running on the system, this is a finding.

## Group: GEN006380

**Group ID:** `V-4399`

### Rule: The system must not use UDP for NIS/NIS+.

**Rule ID:** `SV-45908r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Implementing Network Information Service (NIS) or NIS+ under UDP may make the system more susceptible to a Denial of Service attack and does not provide the same quality of service as TCP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the system does not use NIS or NIS+, this is not applicable. Check if NIS or NIS+ is implemented using UDP. Procedure: # rpcinfo -p | grep yp | grep udp If NIS or NIS+ is implemented using UDP, this is a finding.

## Group: GEN002020

**Group ID:** `V-4427`

### Rule: All .rhosts, .shosts, or host.equiv files must only contain trusted host-user pairs.

**Rule ID:** `SV-45166r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If these files are not properly configured, they could allow malicious access by unknown malicious users from untrusted hosts who could compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate and examine all r-commands access control files. Procedure: # find / -name .rhosts # more /<directorylocation>/.rhosts # find / -name .shosts # more /<directorylocation>/.shosts # find / -name hosts.equiv # more /<directorylocation>/hosts.equiv # find / -name shosts.equiv # more /<directorylocation>/shosts.equiv If any .rhosts, .shosts, hosts.equiv, or shosts.equiv file contains other than host-user pairs, this is a finding.

## Group: GEN002060

**Group ID:** `V-4428`

### Rule: All .rhosts, .shosts, .netrc, or hosts.equiv files must be accessible by only root or the owner.

**Rule ID:** `SV-45168r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If these files are accessible by users other than root or the owner, they could be used by a malicious user to set up a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Procedure: # ls -l /etc/hosts.equiv # ls -l /etc/ssh/shosts.equiv # find / -name .rhosts # ls -al <home directory>/.rhosts # find / -name .shosts # ls -al <home directory>/.shosts # find / -name .netrc # ls -al <home directory>/.netrc If the .rhosts, .shosts, hosts.equiv, or shosts.equiv files have permissions greater than 600, then this is a finding. If the /etc/hosts.equiv, or /etc/ssh/shosts.equiv files are not owned by root, this is a finding. Any .rhosts, .shosts and .netrc files outside of home directories have no meaning and are not subject to this rule If the ~/.rhosts or ~/.shosts are not owned by the owner of the home directory where they are immediately located or by root, this is a finding.

## Group: GEN003260

**Group ID:** `V-4430`

### Rule: The cron.deny file must be owned by root, bin, or sys.

**Rule ID:** `SV-45644r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron daemon control files restrict the scheduling of automated tasks and must be protected. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ls -lL /etc/cron.deny If the cron.deny file is not owned by root, sys, or bin, this is a finding.

## Group: GEN003820

**Group ID:** `V-4687`

### Rule: The rsh daemon must not be running.

**Rule ID:** `SV-45787r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The rshd process provides a typically unencrypted, host-authenticated remote access service. SSH should be used in place of this service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if rshd is configured to run on startup. Procedure: # grep disable /etc/xinetd.d/rsh If /etc/xinetd.d/rsh exists and rsh is found to be enabled, this is a finding.

## Group: GEN003840

**Group ID:** `V-4688`

### Rule: The rexec daemon must not be running.

**Rule ID:** `SV-45807r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The rexecd process provides a typically unencrypted, host-authenticated remote access service. SSH should be used in place of this service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
# grep disable /etc/xinetd.d/rexec If the service file exists and is not disabled, this is a finding.

## Group: GEN004600

**Group ID:** `V-4689`

### Rule: The SMTP service must be an up-to-date version.

**Rule ID:** `SV-45869r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The SMTP service version on the system must be current to avoid exposing vulnerabilities present in unpatched versions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the version of the SMTP service software. Procedure: #rpm -q sendmail SUSE sendmail 8.14.3-50.20.1is the latest required version. If SUSE sendmail is installed and the version is not at least8.14.3.-50.20.1, this is a finding. #rpm -q postfix SUSE postfix-2.5.6-5.8.1 is the latest required version. If postfix is installed and the version is not at least2.5.6-5.8.1, this is a finding.

## Group: GEN004620

**Group ID:** `V-4690`

### Rule: The sendmail server must have the debug feature disabled.

**Rule ID:** `SV-45870r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Debug mode is a feature present in older versions of sendmail which, if not disabled, may allow an attacker to gain access to a system through the sendmail service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for an enabled "debug" command provided by the SMTP service. Procedure: # telnet localhost 25 debug If the command does not return a 500 error code of "command unrecognized", this is a finding. The SLES mainframe distribution ships with sendmail Version 8.14.3.-50.20.1 which is not vulnerable. This should never be a finding.

## Group: GEN004640

**Group ID:** `V-4691`

### Rule: The SMTP service must not have a uudecode alias active.

**Rule ID:** `SV-45871r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A common configuration for older Mail Transfer Agents (MTAs) is to include an alias for the decode user. All mail sent to this user is sent to the uudecode program, which automatically converts and stores files. By sending mail to the decode or the uudecode aliases present on some systems, a remote attacker may be able to create or overwrite files on the remote host. This could possibly be used to gain remote access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SMTP service for an active "decode" command. Procedure: # telnet localhost 25 decode If the command does not return a 500 error code of "command unrecognized", this is a finding.

## Group: GEN004660

**Group ID:** `V-4692`

### Rule: The SMTP service must not have the EXPN feature active.

**Rule ID:** `SV-45872r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The SMTP EXPN function allows an attacker to determine if an account exists on a system, providing significant assistance to a brute force attack on user accounts. EXPN may also provide additional information concerning users on the system, such as the full names of account owners.</VulnDiscussion><FalsePositives>False positives may occur with the SMTP EXPN check. According to RFC821, it is acceptable for a server to respond with a 250 (success) or 550 (failure) when the server supports the EXPN command. For example, some servers return 550 EXPN command not available, meaning the command is not supported and the machine is not vulnerable. However, a result of 550 that is a mailing list, not a user would be a failure code, but not an indication of an error, and the machine would be vulnerable. If a false positive is suspected, check the log file for the response from the server.</FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
This vulnerability is applicable only to sendmail. If Postfix is the SMTP service for the system this will never be a finding. Procedure: Determine if EXPN is disabled. # grep -v "^#" /etc/mail/sendmail.cf |grep -i PrivacyOptions If nothing is returned or the returned line does not contain "noexpn", this is a finding.

## Group: GEN004680

**Group ID:** `V-4693`

### Rule: The SMTP service must not have the Verify (VRFY) feature active.

**Rule ID:** `SV-45873r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The VRFY command allows an attacker to determine if an account exists on a system, providing significant assistance to a brute force attack on user accounts. VRFY may provide additional information about users on the system, such as the full names of account owners.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if VRFY is disabled. Procedure: for sendmail: # telnet localhost 25 vrfy root If the command does not return a 500 error code of "command unrecognized", this is a finding. or: # grep -v "^#" /etc/mail/sendmail.cf |grep -i vrfy Verify the VRFY command is disabled with an entry in the sendmail.cf file. The entry could be any one of "Opnovrfy", "novrfy", or "goaway", which could also have other options included, such as "noexpn". The "goaway" argument encompasses many things, such as "novrfy" and "noexpn". If no setting to disable VRFY is found, this is a finding. For Postfix: Check if the VRFY command has been disabled: # postconf disable_vrfy_command If the command output is not “disable_vrfy_command = yes”, this is a finding.

## Group: GEN004700

**Group ID:** `V-4694`

### Rule: The sendmail service must not have the wizard backdoor active.

**Rule ID:** `SV-45874r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Very old installations of the Sendmail mailing system contained a feature whereby a remote user connecting to the SMTP port can enter the WIZ command and be given an interactive shell with root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Log into the sendmail server with telnet and test the "wiz" commmand" Procedure: # telnet localhost 25 Trying 127.0.0.1... Connected to locahost.localdomain (127.0.0.1). Escape character ... Once the telnet greeting is complete type: wiz If you do not get a "Command unrecognized: " message, this is a finding.

## Group: GEN005140

**Group ID:** `V-4695`

### Rule: Any active TFTP daemon must be authorized and approved in the system accreditation package.

**Rule ID:** `SV-45909r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>TFTP is a file transfer protocol often used by embedded systems to obtain configuration data or software. The service is unencrypted and does not require authentication of requests. Data available using this service may be subject to unauthorized access or interception.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the TFTP daemon is active. # chkconfig --list | grep tftp Or # chkconfig tftp If TFTP is found enabled and not documented using site-defined procedures, it is a finding.

## Group: GEN005280

**Group ID:** `V-4696`

### Rule: The system must not have the UUCP service active.

**Rule ID:** `SV-45938r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UUCP utility is designed to assist in transferring files, executing remote commands, and sending e-mail between UNIX systems over phone lines and direct connections between systems. The UUCP utility is a primitive and arcane system with many security issues. There are alternate data transfer utilities/products that can be configured to more securely transfer data by providing for authentication as well as encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# chkconfig uucp or: # chkconfig --list | grep uucp If UUCP is found enabled, this is a finding.

## Group: GEN005200

**Group ID:** `V-4697`

### Rule: X displays must not be exported to the world.

**Rule ID:** `SV-45920r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Open X displays allow an attacker to capture keystrokes and to execute commands remotely. Many users have their X Server set to “xhost +”, permitting access to the X Server by anyone, from anywhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If Xwindows is not used on the system, this is not applicable. Check the output of the "xhost" command from an X terminal. Procedure: # xhost If the output reports access control is enabled (and possibly lists the hosts able to receive X window logins), this is not a finding. If the xhost command returns a line indicating access control is disabled, this is a finding. Note: It may be necessary to define the display if the command reports it cannot open the display. Procedure: $ DISPLAY=MachineName:0.0; export DISPLAY MachineName may be replaced with an Internet Protocol Address. Repeat the check procedure after setting the display.

## Group: GEN003860

**Group ID:** `V-4701`

### Rule: The system must not have the finger service active.

**Rule ID:** `SV-45810r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The finger service provides information about the system's users to network clients. This information could expose more information for potential used in subsequent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# grep disable /etc/xinetd.d/finger If the finger service is not disabled, this is a finding.

## Group: GEN004840

**Group ID:** `V-4702`

### Rule: If the system is an anonymous FTP server, it must be isolated to the DMZ network.

**Rule ID:** `SV-45878r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anonymous FTP is a public data service which is only permitted in a server capacity when located on the DMZ network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Use the command "ftp" to connect the system's FTP service. Attempt to log into this host with a user name of anonymous and a password of guest (also try the password of guest@mail.com). If the logon is not successful, this check is Not Applicable. Ask the SA if the system is located on a DMZ network. If the system is not located on a DMZ network, this is a finding.

## Group: GEN000100

**Group ID:** `V-11940`

### Rule: The operating system must be a supported release.

**Rule ID:** `SV-44761r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An operating system release is considered "supported" if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance>If an extended support agreement provides security patches for the unsupported product is procured from the vendor, this finding may be downgraded to a CAT III.</SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the version of the operating system. Example: # cat /etc/SuSE-release - OR – (if more detail is required) # sam --no-rpm-verify-md5 --spreport Vendor End-of-Support Information: SUSE Linux Enterprise Server 9: 31 Aug 2011 SUSE Linux Enterprise Server 10: 31 Jul 2013 SUSE Linux Enterprise Server 11: 31 Mar 2016 Check with the vendor for additional information. If the version installed is not supported, this is a finding.

## Group: GEN000220

**Group ID:** `V-11945`

### Rule: A file integrity tool must be used at least weekly to check for unauthorized file changes, particularly the addition of unauthorized system libraries or binaries, or for unauthorized modification to authorized system libraries or binaries.

**Rule ID:** `SV-44765r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in system libraries, binaries and other critical system files can indicate compromise or significant system events such as patching needing to be checked by automated processes and the results reviewed by the SA. NOTE: For MAC I systems, increase the frequency to daily.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if there is an automated job, scheduled to run weekly or more frequently, to run the file integrity tool to check for unauthorized additions to system libraries. The check can be done using Advanced Intrusion Detection Environment (AIDE) which is part of the SUSE Linux Enterprise Server (SLES) distribution. Other file integrity software may be used but must be checked manually. Procedure: Check the root crontab (crontab -l) and the global crontabs in /etc/crontab, /etc/cron.d/* for the presence of an "aide" job to run at least weekly, which should have asterisks (*) in columns 3, 4, and 5. Check the weekly cron directory (/etc/cron.weekly) for any script running "aide --check" or "aide -C" or simply "aide". If one does not exist, this is a finding.

## Group: GEN000340

**Group ID:** `V-11946`

### Rule: UIDs reserved for system accounts must not be assigned to non-system accounts.

**Rule ID:** `SV-44825r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reserved UIDs are typically used by system software packages. If non-system accounts have UIDs in this range, they may conflict with system software, possibly leading to the user having permissions to modify system files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the UID assignments for all accounts. # awk -F: '$3 <= 499 {printf "%15s:%4s\n", $1, $3}' /etc/passwd | sort -n -t: -k2 Confirm all accounts with a UID of 499 and below are used by a system account. If a UID reserved for system accounts (0 - 499) is used by a non-system account, then this is a finding.

## Group: GEN000580

**Group ID:** `V-11947`

### Rule: The system must require passwords contain a minimum of 15 characters.

**Rule ID:** `SV-46194r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of longer passwords reduces the ability of attackers to successfully obtain valid passwords using guessing or exhaustive search techniques by increasing the password search space.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system password length setting. Procedure: Check the password minlen option # grep pam_cracklib.so /etc/pam.d/ common-{auth,account,password,session} Confirm the minlen option is set to at least 15 as in the example below: password required pam_cracklib.so minlen=15 There may be other options on the line. If no such line is found, or the minlen is less than 15 this is a finding.

## Group: GEN000600

**Group ID:** `V-11948`

### Rule: The system must require passwords contain at least one uppercase alphabetic character.

**Rule ID:** `SV-44866r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enforce the use of complex passwords, minimum numbers of characters of different classes are mandated. The use of complex passwords reduces the ability of attackers to successfully obtain valid passwords using guessing or exhaustive search techniques. Complexity requirements increase the password search space by requiring users to construct passwords from a larger character set than they may otherwise use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ucredit setting. # grep ucredit /etc/pam.d/common-password-pc If ucredit is not set to -1, this is a finding.

## Group: GEN000620

**Group ID:** `V-11972`

### Rule: The system must require passwords contain at least one numeric character.

**Rule ID:** `SV-44875r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enforce the use of complex passwords, minimum numbers of characters of different classes are mandated. The use of complex passwords reduces the ability of attackers to successfully obtain valid passwords using guessing or exhaustive search techniques. Complexity requirements increase the password search space by requiring users to construct passwords from a larger character set than they may otherwise use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the dcredit setting. Procedure: Check the password dcredit option # grep pam_cracklib.so /etc/pam.d/common-password-pc Confirm the dcredit option is set to -1 as in the example: password required pam_cracklib.so dcredit=-1 There may be other options on the line. If no such line is found, or the dcredit option is not -1 this is a finding.

## Group: GEN000640

**Group ID:** `V-11973`

### Rule: The system must require passwords contain at least one special character.

**Rule ID:** `SV-44876r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enforce the use of complex passwords, minimum numbers of characters of different classes are mandated. The use of complex passwords reduces the ability of attackers to successfully obtain valid passwords using guessing or exhaustive search techniques. Complexity requirements increase the password search space by requiring users to construct passwords from a larger character set than they may otherwise use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ocredit setting. Procedure: Check the password ocredit option # grep pam_cracklib.so /etc/pam.d/common-password-pc Confirm the ocredit option is set to -1 as in the example: password required pam_cracklib.so ocredit=-1 There may be other options on the line. If no such line is found, or the ocredit is not -1 this is a finding.

## Group: GEN000680

**Group ID:** `V-11975`

### Rule: The system must require passwords contain no more than three consecutive repeating characters.

**Rule ID:** `SV-44877r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enforce the use of complex passwords, the number of consecutive repeating characters is limited. Passwords with excessive repeated characters may be more vulnerable to password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system password maxrepeat setting. Procedure: Check the password maxrepeat option # grep pam_cracklib.so /etc/pam.d/common-password Confirm the maxrepeat option is set to 3 or less as in the example below: password required pam_cracklib.so maxrepeat=3 There may be other options on the line. If no such line is found, or the maxrepeat option is more than 3 this is a finding. A setting of zero disables this option. NOTE: This option was not available in SLES 11 until service pack 2(SP2).

## Group: GEN000700

**Group ID:** `V-11976`

### Rule: User passwords must be changed at least every 60 days.

**Rule ID:** `SV-44879r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the lifespan of authenticators limits the period of time an unauthorized user has access to the system while using compromised credentials and reduces the period of time available for password-guessing attacks to run against a single password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the max days field (the 5th field) of /etc/shadow. # more /etc/shadow If the max days field is equal to 0 or greater than 60 for any user, this is a finding.

## Group: GEN000740

**Group ID:** `V-11977`

### Rule: All non-interactive/automated processing account passwords must be changed at least once per year or be locked.

**Rule ID:** `SV-44880r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the lifespan of authenticators limits the period of time an unauthorized user has access to the system while using compromised credentials and reduces the period of time available for password-guessing attacks to run against a single password. Locking the password for non-interactive and automated processing accounts is preferred as it removes the possibility of accessing the account by a password. On some systems, locking the passwords of these accounts may prevent the account from functioning properly. Passwords for non-interactive/automated processing accounts must not be used for direct logon to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if there are any automated processing accounts on the system. If there are automated processing accounts on the system, ask the SA if the passwords for those automated accounts are changed at least once a year. If SA indicates passwords for automated processing accounts are not changed once per year, this is a finding.

## Group: GEN001020

**Group ID:** `V-11979`

### Rule: The root account must not be used for direct log in.

**Rule ID:** `SV-44915r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Direct login with the root account prevents individual user accountability. Acceptable non-routine uses of the root account for direct login are limited to emergency maintenance, the use of single-user mode for maintenance, and situations where individual administrator accounts are not available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the root is used for direct logins. Procedure: # last root | grep -v reboot If any direct login records for root exist, this is a finding.

## Group: GEN001060

**Group ID:** `V-11980`

### Rule: The system must log successful and unsuccessful access to the root account.

**Rule ID:** `SV-44916r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If successful and unsuccessful logins and logouts are not monitored or recorded, access attempts cannot be tracked. Without this logging, it may be impossible to track unauthorized access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the log files to determine if access to the root account is being logged. Procedure: Examine /etc/rsyslog.conf to confirm the location to which "auth" messages will be directed. The default rsyslog.conf uses /var/log/messages but, this needs to be confirmed. # grep @@ /etc/rsyslog.d/remote.conf If a line starting with "*.*" is returned then all rsyslog messages will be sent to system whose address appears after the "@@". In this case rsyslog may or may not be configured to also log "auth" messages locally. # grep auth /etc/rsyslog.conf If any lines are returned which do not start with "#" the "auth" messages will be sent to the indicated files or remote systems. Try to "su -" and enter an incorrect password. #more /var/log/messages Or #more /var/log/secure If there are no records indicating the authentication failure, this is a finding.

## Group: GEN001720

**Group ID:** `V-11981`

### Rule: All global initialization files must have mode 0644 or less permissive.

**Rule ID:** `SV-45095r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Global initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check global initialization files permissions: # ls -l /etc/bash.bashrc # ls -l /etc/csh.cshrc # ls -l /etc/csh.login # ls -l /etc/environment # ls -l /etc/ksh.kshrc # ls -l /etc/profile # ls -l /etc/profile.d/* # ls -l /etc/zshrc If global initialization files are more permissive than 0644, this is a finding.

## Group: GEN001740

**Group ID:** `V-11982`

### Rule: All global initialization files must be owned by root.

**Rule ID:** `SV-45104r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Global initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon logon. Failure to give ownership of sensitive files or utilities to root or bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of global initialization files. Procedure: # ls -lL /etc/bash.bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc This should show information for each file. Examine to ensure the owner is always root or: # ls /etc/bash.bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc 2>/dev/null|xargs stat -L -c %U:%n|egrep -v "^root" This will show you only the owner and filename of files not owned by root. If any global initialization file is not owned by root, this is a finding.

## Group: GEN001760

**Group ID:** `V-11983`

### Rule: All global initialization files must be group-owned by root, sys, bin, other, system, or the system default.

**Rule ID:** `SV-45105r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Global initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon logon. Failure to give ownership of sensitive files or utilities to root or bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of global initialization files. Procedure: # ls -lL /etc/bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc This should show information for each file. Examine to ensure the group is always root or: # ls -lL /etc/bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc 2>/dev/null|sed "s/^[^\/]*//"|xargs stat -L -c %G:%n|egrep -v "^(root|sys|bin|other):" will show you only the group and filename of files not owned by one of the approved groups. If any global initialization file is not group-owned by root, sys, bin, other, system, or the system default, this is a finding.

## Group: GEN001820

**Group ID:** `V-11984`

### Rule: All skeleton files and directories (typically in /etc/skel) must be owned by root or bin.

**Rule ID:** `SV-45136r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the skeleton files are not protected, unauthorized personnel could change user startup parameters and possibly jeopardize user files. Failure to give ownership of sensitive files or utilities to root or bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check skeleton files ownership. # ls -alL /etc/skel If a skeleton file is not owned by root or bin, this is a finding.

## Group: GEN001840

**Group ID:** `V-11985`

### Rule: All global initialization files executable search paths must contain only absolute paths.

**Rule ID:** `SV-45141r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory or other relative paths, executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the global initialization files' executable search paths. Procedure: # grep PATH /etc/bash.bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) this is a relative path, this is a finding.

## Group: GEN001900

**Group ID:** `V-11986`

### Rule: All local initialization files executable search paths must contain only absolute paths.

**Rule ID:** `SV-46274r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory or other relative paths, executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify local initialization files have executable search paths containing only absolute paths or relative paths that have been documented by the ISSO. Procedure: NOTE: This must be done in the BASH shell. # cut -d: -f6 /etc/passwd |xargs -n1 -IDIR find DIR -name ".*" -type f -maxdepth 1 -exec grep -l PATH {} \; This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/), or has not been documented with the ISSO, this is a finding.

## Group: GEN001980

**Group ID:** `V-11987`

### Rule: The .rhosts, .shosts, hosts.equiv, shosts.equiv, /etc/passwd, /etc/shadow, and/or /etc/group files must not contain a plus (+) without defining entries for NIS+ netgroups.

**Rule ID:** `SV-45164r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A plus (+) in system accounts files causes the system to lookup the specified entry using NIS. If the system is not using NIS, no such entries should exist.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check system configuration files for plus (+) entries. Procedure: # find / -name .rhosts # grep + /<directorylocation>/.rhosts # find / -name .shosts # grep + /<directorylocation>/.shosts # find / -name hosts.equiv # grep + /<directorylocation>/hosts.equiv # find / -name shosts.equiv # grep + /<directorylocation>/shosts.equiv # grep + /etc/passwd # grep + /etc/shadow # grep + /etc/group If the .rhosts, .shosts, hosts.equiv, shosts.equiv, /etc/passwd, /etc/shadow, and/or /etc/group files contain a plus (+) and do not define entries for NIS+ netgroups, this is a finding.

## Group: GEN002040

**Group ID:** `V-11988`

### Rule: There must be no .rhosts, .shosts, hosts.equiv, or shosts.equiv files on the system.

**Rule ID:** `SV-45167r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The .rhosts, .shosts, hosts.equiv, and shosts.equiv files are used to configure host-based authentication for individual users or the system. Host-based authentication is not sufficient for preventing unauthorized access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the files. # find / -name .rhosts # find / -name .shosts # find / -name hosts.equiv # find / -name shosts.equiv If .rhosts, .shosts, hosts.equiv, or shosts.equiv are found and their use has not been documented and approved by the IAO, this is a finding.

## Group: GEN002100

**Group ID:** `V-11989`

### Rule: The .rhosts file must not be supported in PAM.

**Rule ID:** `SV-45169r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.rhosts files are used to specify a list of hosts permitted remote access to a particular account without authenticating. The use of such a mechanism defeats strong identification and authentication requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the PAM configuration for rhosts_auth. Example: # grep rhosts_auth /etc/pam.d/* If a rhosts_auth entry is found, this is a finding.

## Group: GEN002540

**Group ID:** `V-11990`

### Rule: All public directories must be group-owned by root or an application group.

**Rule ID:** `SV-45204r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public directory has the sticky bit set and is not group-owned by a privileged GID, unauthorized users may be able to modify files created by others. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group-ownership of public directories. Procedure: # find / -type d -perm -1002 -exec ls -ld {} \; If any public directory is not group-owned by root, sys, bin, or an application group, this is a finding.

## Group: GEN003040

**Group ID:** `V-11994`

### Rule: Crontabs must be owned by root or the crontab creator.

**Rule ID:** `SV-45585r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of scheduled system jobs and prevent malicious modification to these jobs, crontab files must be secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
List all crontabs on the system. # ls -lL /var/spool/cron /var/spool/cron/tabs # ls -lL /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls -lL /etc/cron*|grep -v deny If any crontab is not owned by root or the creating user, this is a finding

## Group: GEN003060

**Group ID:** `V-11995`

### Rule: Default system accounts (with the exception of root) must not be listed in the cron.allow file or must be included in the cron.deny file, if cron.allow does not exist.

**Rule ID:** `SV-46275r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To centralize the management of privileged account crontabs, of the default system accounts, only root may have a crontab.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the cron.allow and cron.deny files for the system. # more /etc/cron.allow # more /etc/cron.deny If a default system account (such as bin, sys, adm, or others, traditionally UID less than 500) is listed in the cron.allow file, or not listed in the cron.deny file and if no cron.allow file exists, this is a finding.

## Group: GEN003500

**Group ID:** `V-11996`

### Rule: Process core dumps must be disabled unless needed.

**Rule ID:** `SV-45679r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Process core dump files can be of significant size and their use can result in file systems filling to capacity, which may result in Denial of Service. Process core dumps can be useful for software debugging. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ulimit -c If the above command does not return 0 and the enabling of core dumps has not been documented and approved by the IAO, this a finding.

## Group: GEN003520

**Group ID:** `V-11997`

### Rule: The kernel core dump data directory must be owned by root.

**Rule ID:** `SV-45704r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. As the system memory may contain sensitive information, it must be protected accordingly. If the kernel core dump data directory is not owned by root, the core dumps contained in the directory may be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the kernel core dump data directory. # ls -ld /var/crash If the kernel core dump data directory is not owned by root, this is a finding.

## Group: GEN003540

**Group ID:** `V-11999`

### Rule: The system must implement non-executable program stacks.

**Rule ID:** `SV-45717r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common type of exploit is the stack buffer overflow. An application receives, from an attacker, more data than it is prepared for and stores this information on its stack, writing beyond the space reserved for it. This can be designed to cause execution of the data written on the stack. One mechanism to mitigate this vulnerability is for the system to not allow the execution of instructions in sections of memory identified as part of the stack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The stock kernel has support for non-executable program stacks compiled in by default. The kernel build options can be found in the /boot/config-<kernel version>-default file. Verify that the option was specified when the kernel was built: # grep –i CONFIG_S390_EXEC /boot/config-<kernel version>-default The value “CONFIG_S390_EXEC_PROTECT=y” should be returned. To activate this support, the “noexec=on” kernel parameter must be specified at boot time. The message: “Execute protection active, mvcos available” will be written in the boot log when this feature has been configured successfully. Check for the message with the following command: # grep –i “execute protect” /var/log/boot.msg If non-executable program stacks have not been configured, this is a finding. Verify "randomize_va_space" has not been changed from the default "1" setting. Procedure: #sysctl kernel.randomize_va_space If the return value is not: kernel.randomize_va_space = 1 this is a finding.

## Group: GEN003600

**Group ID:** `V-12002`

### Rule: The system must not forward IPv4 source-routed packets.

**Rule ID:** `SV-45719r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not accept source-routed IPv4 packets. Procedure: # grep [01] /proc/sys/net/ipv4/conf/*/accept_source_route|egrep "default|all" If all of the returned lines do not end with 0, this is a finding. Note: The same setting is used by Linux for both the local acceptance and forwarding of source-routed IPv4 packets.

## Group: GEN003620

**Group ID:** `V-12003`

### Rule: A separate file system must be used for user home directories (such as /home or an equivalent).

**Rule ID:** `SV-45739r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the /home path is a separate filesystem. # grep "/home " /etc/fstab If no result is returned, /home is not on a separate filesystem this is a finding.

## Group: GEN003660

**Group ID:** `V-12004`

### Rule: The system must log informational authentication data.

**Rule ID:** `SV-45755r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Monitoring and recording successful and unsuccessful logins assists in tracking unauthorized access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/rsyslog.conf and verify the auth facility is logging both the notice and info level messages by: # grep “auth.notice” /etc/rsyslog.conf # grep “auth.info” /etc/rsyslog.conf or # grep 'auth.*' /etc/rsyslog.conf If auth.* is not found, and either auth.notice or auth.info is not found, this is a finding.

## Group: GEN003700

**Group ID:** `V-12005`

### Rule: Inetd and xinetd must be disabled or removed if no network services utilizing them are enabled.

**Rule ID:** `SV-45756r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary services should be disabled to decrease the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# ps -ef |grep xinetd If xinetd is not running, this check is not a finding. # grep -v "^#" /etc/xinetd.conf # grep disable /etc/xinetd.d/* |grep no If no active services are found, and the inetd daemon is running, this is a finding.

## Group: GEN004540

**Group ID:** `V-12006`

### Rule: The SMTP service HELP command must not be enabled.

**Rule ID:** `SV-45863r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HELP command should be disabled to mask version information. The version of the SMTP service software could be used by attackers to target vulnerabilities present in specific software versions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the sendmail package is installed: # rpm –q sendmail If sendmail is not installed, this check is not applicable. Check if Help is disabled. This rule is for “sendmail” only and not applicable to “Postfix”. Procedure: # telnet <host> 25 > help If the help command returns any sendmail version information, this is a finding.

## Group: GEN004800

**Group ID:** `V-12010`

### Rule: Unencrypted FTP must not be used on the system.

**Rule ID:** `SV-45876r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>FTP is typically unencrypted and presents confidentiality and integrity risks. FTP may be protected by encryption in certain cases, such as when used in a Kerberos environment. SFTP and FTPS are encrypted alternatives to FTP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to determine if unencrypted FTP is enabled: # chkconfig --list pure-ftpd # chkconfig --list gssftp # chkconfig --list vsftpd If any of these services are found, ask the SA if these services are encrypted. If they are not, this is a finding.

## Group: GEN005040

**Group ID:** `V-12011`

### Rule: All FTP users must have a default umask of 077.

**Rule ID:** `SV-45887r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. An umask of 077 limits new files to mode 700 or less permissive. Although umask is stored as a 4-digit number, the first digit representing special access modes is typically ignored or required to be zero (0).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the umask setting for FTP users. Procedure: For gssftp: Assuming an anonymous ftp user has been defined with no user initialization script invoked to change the umask # ftp localhost Name: (localhost:root): anonymous Password: anything ftp>umask If the umask value returned is not 077, this is a finding. or: # grep "server_args" /etc/xinetd.d/gssftp The default umask for FTP is "023" if the server _args entry does not contain "-u 077" this is a finding. For vsftp: # grep "_mask" /etc/vsftpd/vsftpd.conf The default "local_umask" setting is 077. If this has been changed, or the "anon_umask" setting is not 077, this is a finding.

## Group: GEN005360

**Group ID:** `V-12019`

### Rule: The snmpd.conf file must be owned by root.

**Rule ID:** `SV-45965r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The snmpd.conf file contains authenticators and must be protected from unauthorized access and modification. If the file is not owned by root, it may be subject to access and modification from unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the owner of the SNMP configuration file. Procedure: Find the snmpd.conf file. The default install location is /etc/snmp/snmpd.conf but may be different depending on the SNMP agent installed. # find / -name snmpd.conf # ls -lL <snmpd.conf> If the snmpd.conf file is not owned by root, this is a finding.

## Group: GEN005440

**Group ID:** `V-12020`

### Rule: The system must not be used as a syslog server (loghost) for systems external to the enclave.

**Rule ID:** `SV-45984r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Syslog messages are typically unencrypted, may contain sensitive information, and are restricted to the enclave.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if the loghost server is collecting data for hosts outside the local enclave. If it is, this is a finding.

## Group: GEN005480

**Group ID:** `V-12021`

### Rule: The syslog daemon must not accept remote messages unless it is a syslog server documented using site-defined procedures.

**Rule ID:** `SV-45991r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unintentionally running a syslog server accepting remote messages puts the system at increased risk. Malicious syslog messages sent to the server could exploit vulnerabilities in the server software itself, could introduce misleading information in to the system's logs, or could fill the system's storage leading to a Denial of Service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
#ps -ef | grep syslogd If the '-r' option is present. This is a finding.

## Group: GEN005540

**Group ID:** `V-12022`

### Rule: The SSH daemon must be configured for IP filtering.

**Rule ID:** `SV-46108r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SSH daemon must be configured for IP filtering to provide a layered defense against connection attempts from unauthorized addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the TCP wrappers configuration files to determine if sshd is configured to use TCP wrappers. Procedure: # grep sshd /etc/hosts.deny # grep sshd /etc/hosts.allow If no entries are returned, the TCP wrappers are not configured for sshd, this is a finding.

## Group: GEN005600

**Group ID:** `V-12023`

### Rule: IP forwarding for IPv4 must not be enabled, unless the system is a router.

**Rule ID:** `SV-46114r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is configured for IP forwarding and is not a designated router, it could be used to bypass network security by providing a path for communication not filtered by network devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the system is configured for IPv4 forwarding. If the system is a VM host and acts as a router solely for the benefits of its client systems, then this rule is not applicable. Procedure: # cat /proc/sys/net/ipv4/ip_forward If the value is set to "1", IPv4 forwarding is enabled this is a finding.

## Group: GEN006000

**Group ID:** `V-12024`

### Rule: The system must not have a public Instant Messaging (IM) client installed.

**Rule ID:** `SV-46127r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Public (IM) systems are not approved for use and may result in the unauthorized distribution of information. IM clients provide a way for a user to send a message to one or more other users in real time. Additional capabilities may include file transfer and support for distributed game playing. Communication between clients and associated directory services are managed through messaging servers. Commercial IM clients include AOL Instant Messenger (AIM), MSN Messenger, and Yahoo! Messenger. IM clients present a security issue when the clients route messages through public servers. The obvious implication is potentially sensitive information could be intercepted or altered in the course of transmission. This same issue is associated with the use of public e-mail servers. In order to reduce the potential for disclosure of sensitive Government information and to ensure the validity of official government information, IM clients connecting to public IM services will not be installed. Clients use to access internal or DoD-controlled IM services are permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If an IM client is installed, ask the SA if it has access to any public domain IM servers. If it does have access to public servers, this is a finding.

## Group: GEN006040

**Group ID:** `V-12025`

### Rule: The system must not have any peer-to-peer file-sharing application installed.

**Rule ID:** `SV-46128r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Peer-to-peer file-sharing software can result in the unintentional exfiltration of information. There are also many legal issues associated with these types of utilities including copyright infringement or other intellectual property issues. The ASD Memo "Use of Peer-to-Peer (P2P) File-Sharing Applications across the DoD" states the following: “P2P file-sharing applications are authorized for use on DOD networks with approval by the appropriate Designated Approval Authority (DAA). Documented requirements, security architecture, configuration management process, and a training program for users are all requirements within the approval process. The unauthorized use of application or services, including P2P applications, is prohibited, and such applications or services must be eliminated.” P2P applications include, but are not limited to, the following: -Napster -Kazaa -ARES -Limewire -IRC Chat Relay -BitTorrent</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Designated Approving Authority</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if any peer-to-peer file-sharing applications are installed. Some examples of these applications include: - Napster - Kazaa - ARES - Limewire - IRC Chat Relay - BitTorrent If any of these applications are installed, this is a finding.

## Group: GEN006420

**Group ID:** `V-12026`

### Rule: NIS maps must be protected through hard-to-guess domain names.

**Rule ID:** `SV-45910r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of hard-to-guess NIS domain names provides additional protection from unauthorized access to the NIS directory information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the domain name for NIS maps. Procedure: # domainname If the name returned is simple to guess, such as the organization name, building or room name, etc., this is a finding.

## Group: GEN006560

**Group ID:** `V-12028`

### Rule: The system vulnerability assessment tool, host-based intrusion detection tool, and file integrity tool must notify the SA and the IAO of a security breach or a suspected security breach.

**Rule ID:** `SV-45913r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Timely notifications of potential security compromises minimize the potential damage. Minimally, the system must log these events and the SA and the IAO will receive the notifications during the daily system log review. If feasible, active alerting (such as e-mail or paging) should be employed consistent with the site’s established operations management systems and procedures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
For each security tool on the system, determine if the tool is configured to notify the IAO and SA of any detected security problem. If such notifications are not configured, this is a finding.

## Group: GEN006620

**Group ID:** `V-12030`

### Rule: The systems access control program must be configured to grant or deny system access to specific hosts.

**Rule ID:** `SV-45931r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system's access control program is not configured with appropriate rules for allowing and denying access to system network resources, services may be accessible to unauthorized hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the "/etc/hosts.allow" and "/etc/hosts.deny" files. Procedure: # ls -la /etc/hosts.allow # ls -la /etc/hosts.deny If either file does not exist, this is a finding. Check for the presence of a "default deny" entry. Procedure: # grep "ALL: ALL" /etc/hosts.deny If the "ALL: ALL" entry is not present the "/etc/hosts.deny" file, any TCP service from a host or network not matching other rules will be allowed access. If the entry is not in "/etc/hosts.deny", this is a finding.

## Group: GEN000000-LNX00620

**Group ID:** `V-12038`

### Rule: The /etc/securetty file must be group-owned by root, sys, or bin.

**Rule ID:** `SV-44669r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The securetty file contains the list of terminals permitting direct root logins. It must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/securetty group ownership: # ls –lL /etc/securetty If /etc/securetty is not group owned by root, sys, or bin, then this is a finding.

## Group: GEN000000-LNX00640

**Group ID:** `V-12039`

### Rule: The /etc/securetty file must be owned by root.

**Rule ID:** `SV-44672r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The securetty file contains the list of terminals permitting direct root logins. It must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/securetty ownership. Procedure: # ls –lL /etc/securetty If /etc/securetty is not owned by root, this is a finding.

## Group: GEN000000-LNX00660

**Group ID:** `V-12040`

### Rule: The /etc/securetty file must have mode 0600 or less permissive.

**Rule ID:** `SV-44700r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The securetty file contains the list of terminals permitting direct root logins. It must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/securetty permissions. Procedure: # ls -lL /etc/securetty If /etc/securetty has a mode more permissive than 0600, this is a finding.

## Group: GEN003865

**Group ID:** `V-12049`

### Rule: Network analysis tools must not be installed.

**Rule ID:** `SV-45811r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network analysis tools allow for the capture of network traffic visible to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if any network analysis tools are installed. Procedure: # find / -name ethereal # find / -name wireshark # find / -name tshark # find / -name netcat # find / -name tcpdump # find / -name snoop If any network analysis tools are found, this is a finding.

## Group: GEN006640

**Group ID:** `V-12765`

### Rule: The system must use and update a virus scan program.

**Rule ID:** `SV-45967r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virus scanning software can be used to protect a system from penetration by computer viruses and to limit their spread through intermediate systems. The virus scanning software should be configured to perform scans dynamically on accessed files. If this capability is not available, the system must be configured to scan, at a minimum, all altered files on the system on a daily basis. If the system processes inbound SMTP mail, the virus scanner must be configured to scan all received mail. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of a virus scan tool to be executed daily in the cron file: # crontab -l With the assistance of the system administrator, ensure the virus definition signature files are not older than seven (7) days. If a virus scanner is not being run daily or the virus definitions are older than seven (7) days, this is a finding.

## Group: GEN000241

**Group ID:** `V-22290`

### Rule: The system clock must be synchronized continuously, or at least daily.


**Rule ID:** `SV-44772r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. Internal system clocks tend to drift and require periodic resynchronization to ensure their accuracy. Software, such as ntpd, can be used to continuously synchronize the system clock with authoritative sources. Alternatively, the system may be synchronized periodically, with a maximum of one day between synchronizations. If the system is completely isolated (i.e., it has no connections to networks or other systems), time synchronization is not required as no correlation of events or operation of time-dependent protocols between systems will be necessary. If the system is completely isolated, this requirement is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the root crontab (crontab -l) and the global crontabs in /etc/crontab, /etc/cron.d/* for the presence of an "ntpd -qg" job to run at least daily, which should have asterisks (*) in columns 3, 4, and 5. Check the daily cron directory (/etc/cron.daily) for any script running "ntpd -qg". Check for a running NTP daemon. # ps ax | grep ntpd If none of the above checks are successful, this is a finding.

## Group: GEN000242

**Group ID:** `V-22291`

### Rule: The system must use at least two time sources for clock synchronization.

**Rule ID:** `SV-44773r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. For redundancy, two time sources are required so synchronization continues to function if one source fails. If the system is completely isolated (i.e., it has no connections to networks or other systems), time synchronization is not required as no correlation of events or operation of time-dependent protocols between systems will be necessary. If the system is completely isolated, this requirement is not applicable. Note: For the network time protocol (NTP), the requirement is two servers, but it is recommended to configure at least four distinct time servers which allow NTP to effectively exclude a time source not consistent with the others. The system's local clock must be excluded from the count of time sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the root crontab (crontab -l) and the global crontabs in /etc/crontab, /etc/cron.d/*, or scripts in the /etc/cron.daily directory for the presence of an "ntpd -qg" job. If the "ntpd -qg" command is not invoked with at least two external NTP servers listed, this is a finding. Check the NTP daemon configuration for at least two external servers. # grep ^server /etc/ntp.conf | egrep -v '(127.127.1.0|127.127.1.1)' If less than two servers or external reference clocks (127.127.x.x other than 127.127.1.0 or 127.127.1.1) are listed, this is a finding.

## Group: GEN000244

**Group ID:** `V-22292`

### Rule: The system must use time sources that are local to the enclave.

**Rule ID:** `SV-44774r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. The network architecture should provide multiple time servers within an enclave providing local service to the enclave and synchronize with time sources outside of the enclave. If this server is an enclave time server, this requirement is not applicable. If the system is completely isolated (i.e., it has no connections to networks or other systems), time synchronization is not required as no correlation of events or operation of time-dependent protocols between systems will be necessary. If the system is completely isolated, this requirement is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the root crontab (crontab -l) and the global crontabs in /etc/crontab, /etc/cron.d/*, or scripts in the /etc/cron.daily directory for the presence of an "ntpd -qg" job. If the "ntpd -qg" command is invoked with NTP servers outside of the enclave, this is a finding. Check the NTP daemon configuration for NTP servers. # grep ^server /etc/ntp.conf | grep -v 127.127.1.1 If an NTP server is listed outside of the enclave, this is a finding.

## Group: GEN000250

**Group ID:** `V-22294`

### Rule: The time synchronization configuration file (such as /etc/ntp.conf) must be owned by root.

**Rule ID:** `SV-44776r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not owned by a system account, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the NTP configuration file. # ls -l /etc/ntp.conf If the owner is not root, this is a finding.

## Group: GEN000251

**Group ID:** `V-22295`

### Rule: The time synchronization file (such as /etc/ntp.conf) must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-44779r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not owned by a system group, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the NTP configuration file. Procedure: # ls -lL /etc/ntp.conf If the group owner is not root, bin, sys, or system, this is a finding.

## Group: GEN000252

**Group ID:** `V-22296`

### Rule: The time synchronization configuration file (such as /etc/ntp.conf) must have mode 0640 or less permissive.

**Rule ID:** `SV-44782r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not protected, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode for the NTP configuration file is not more permissive than 0640. # ls -l /etc/ntp.conf If the mode is more permissive than 0640, this is a finding.

## Group: GEN000253

**Group ID:** `V-22297`

### Rule: The time synchronization configuration file (such as /etc/ntp.conf) must not have an extended ACL.

**Rule ID:** `SV-44788r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not protected, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the NTP configuration file has no extended ACL. # ls -l /etc/ntp.conf If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN000450

**Group ID:** `V-22298`

### Rule: The system must limit users to 10 simultaneous system logins, or a site-defined number, in accordance with operational requirements.

**Rule ID:** `SV-44832r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Limiting simultaneous user logins can insulate the system from denial of service problems caused by excessive logins. Automated login processes operating improperly or maliciously may result in an exceptional number of simultaneous login sessions. If the defined value of 10 logins does not meet operational requirements, the site may define the permitted number of simultaneous login sessions based on operational requirements. This limit is for the number of simultaneous login sessions for EACH user account. This is NOT a limit on the total number of simultaneous login sessions on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for a default maxlogins line in the /etc/security/limits.conf and /etc/security/limits.d/* files. Procedure: #grep maxlogins /etc/security/limits.conf /etc/security/limits.d/* The default maxlimits should be set to a max of 10 or a documented site defined number: * - maxlogins 10 If no such line exists, this is a finding.

## Group: GEN000452

**Group ID:** `V-22299`

### Rule: The system must display the date and time of the last successful account login upon login.

**Rule ID:** `SV-44833r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Providing users with feedback on when account accesses last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check that pam_lastlog is used and not silent, or that the SSH daemon is configured to display last login information. # grep pam_lastlog /etc/pam.d/sshd If pam_lastlog is present, and does not have the "silent" option, this is not a finding. # grep -i PrintLastLog /etc/ssh/sshd_config If PrintLastLog is not enabled in the configuration either explicitly or by default, this is a finding.

## Group: GEN000585

**Group ID:** `V-22302`

### Rule: The system must enforce compliance of the entire password during authentification.

**Rule ID:** `SV-44862r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some common password hashing schemes only process the first eight characters of a user's password, which reduces the effective strength of the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify no password hash in /etc/passwd or /etc/shadow begins with a character other than an underscore (_) or dollar sign ($). # cut -d ':' -f2 /etc/passwd # cut -d ':' -f2 /etc/shadow If any password hash is present that does not have an initial underscore (_) or dollar sign ($) character, this is a finding.

## Group: GEN000590

**Group ID:** `V-22303`

### Rule: The system must use a FIPS 140-2 approved cryptographic hashing algorithm for generating account password hashes.

**Rule ID:** `SV-44864r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Systems must employ cryptographic hashes for passwords using the SHA-2 family of algorithms or FIPS 140-2 approved successors. The use of unapproved algorithms may result in weak password hashes more vulnerable to compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the /etc/default/passwd file for the CRYPT_FILES variable setting. Procedure: # grep -v '^#' /etc/default/passwd | grep -i crypt_files CRYPT_FILES must be set to SHA256 or SHA512. If it is not set, or it is set to some other value this is a finding.

## Group: GEN000595

**Group ID:** `V-22304`

### Rule: The password hashes stored on the system must have been generated using a FIPS 140-2 approved cryptographic hashing algorithm.

**Rule ID:** `SV-44865r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Systems must employ cryptographic hashes for passwords using the SHA-2 family of algorithms or FIPS 140-2 approved successors. The use of unapproved algorithms may result in weak password hashes more vulnerable to compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check all password hashes in /etc/passwd or /etc/shadow begin with '$5$' or '$6$'. Procedure: # cut -d ':' -f2 /etc/passwd # cut -d ':' -f2 /etc/shadow Any password hashes present not beginning with '$5$' or '$6$', is a finding.

## Group: GEN000610

**Group ID:** `V-22305`

### Rule: The system must require passwords contain at least one lowercase alphabetic character.

**Rule ID:** `SV-44867r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enforce the use of complex passwords, minimum numbers of characters of different classes are mandated. The use of complex passwords reduces the ability of attackers to successfully obtain valid passwords using guessing or exhaustive search techniques. Complexity requirements increase the password search space by requiring users to construct passwords from a larger character set than they may otherwise use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/pam.d/common-password for lcredit setting. Procedure: Check the password lcredit option # grep pam_cracklib.so /etc/pam.d/common-password Confirm the lcredit option is set to -1 as in the example: password required pam_cracklib.so lcredit=-1 There may be other options on the line. If no such line is found, or the lcredit is not -1 this is a finding.

## Group: GEN000750

**Group ID:** `V-22306`

### Rule: The system must require at least eight characters be changed between the old and new passwords during a password change.

**Rule ID:** `SV-44881r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure password changes are effective in their goals, the system must ensure that old and new passwords have significant differences. Without significant changes, new passwords may be easily guessed based on the value of a previously compromised password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/pam.d/common-{auth,account,password,session} for a ‘difok’ parameter on the pam_cracklib.so line. Procedure: # grep difok /etc/pam.d/common-{auth,account,password,session} If difok is not present, or has a value less than 8, this is a finding. Check for common-password inclusions. # grep -c common-password /etc/pam.d/* If the common-password file is included anywhere # grep difok /etc/pam.d/common-password If common-password is included anywhere and difok is not present, or has a value less than 8, this is a finding. Ensure the passwd command uses the common-password settings. # grep common-password /etc/pam.d/passwd If a line "password include common-password" is not found then the password checks in common-password will not be applied to new passwords and this is a finding.

## Group: GEN000790

**Group ID:** `V-22307`

### Rule: The system must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-44883r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An easily guessable password provides an open door to any external or internal malicious intruder. Many computer compromises occur as the result of account name and password guessing. This is generally done by someone with an automated script that uses repeated logon attempts until the correct account and password pair is guessed. Utilities, such as cracklib, can be used to validate passwords are not dictionary words and meet other criteria during password changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/pam.d/common-password for pam_cracklib configuration. # grep pam_cracklib /etc/pam.d/common-password* If pam_cracklib is not present, this is a finding. Ensure the passwd command uses the common-password settings. # grep common-password /etc/pam.d/passwd If a line "password include common-password" is not found then the password checks in common-password will not be applied to new passwords, this is a finding.

## Group: GEN000850

**Group ID:** `V-22308`

### Rule: The system must restrict the ability to switch to the root user to members of a defined group.

**Rule ID:** `SV-44899r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring a supplemental group for users permitted to switch to the root user prevents unauthorized users from accessing the root account, even with knowledge of the root credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check that /etc/pam.d/su and /etc/pam.d/su-l use pam_wheel. # grep pam_wheel /etc/pam.d/su /etc/pam.d/su-l If pam_wheel is not present, or is commented out, this is a finding.

## Group: GEN000930

**Group ID:** `V-22309`

### Rule: The root accounts home directory must not have an extended ACL.

**Rule ID:** `SV-44903r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File system extended ACLs provide access to files beyond what is allowed by the unix permissions of the files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the root account's home directory has no extended ACL. # grep "^root" /etc/passwd | awk -F":" ‘{print $6}’ # ls -ld <root home directory> If the permissions include a '+' the directory has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN000945

**Group ID:** `V-22310`

### Rule: The root accounts library search path must be the system default and must contain only absolute paths.

**Rule ID:** `SV-44906r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library search path environment variable(s) contain a list of directories for the dynamic linker to search to find libraries. If this path includes the current working directory or other relative paths, libraries in these directories may be loaded instead of system libraries. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is interpreted as the current working directory. Entries starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the LD_LIBRARY_PATH environment variable is empty or not defined for the root user. # echo $LD_LIBRARY_PATH If a path list is returned, this is a finding.

## Group: GEN000950

**Group ID:** `V-22311`

### Rule: The root accounts list of preloaded libraries must be empty.

**Rule ID:** `SV-44911r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries relative to the current working directory, unintended libraries may be preloaded. This variable is formatted as a space-separated list of libraries. Paths starting with (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the LD_PRELOAD environment variable is empty or not defined for the root user. # echo $LD_PRELOAD If a path list is returned, this is a finding.

## Group: GEN001170

**Group ID:** `V-22312`

### Rule: All files and directories must have a valid group-owner.

**Rule ID:** `SV-44927r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files without a valid group owner may be unintentionally inherited if a group is assigned the same GID as the GID of the files without a valid group-owner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Search the system for files without a valid group-owner. # find / -nogroup If any files are found, this is a finding.

## Group: GEN001190

**Group ID:** `V-22313`

### Rule: All network services daemon files must not have extended ACLs.

**Rule ID:** `SV-44934r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permission on daemons will protect them from unauthorized modification and possible system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check that network services daemon files have no extended ACLs. # ls -la /usr/sbin If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001210

**Group ID:** `V-22314`

### Rule: All system command files must not have extended ACLs.

**Rule ID:** `SV-44938r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permissions will protect system command files from unauthorized modification. System command files include files present in directories used by the operating system for storing default system executables and files present in directories included in the system's default executable search paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check all system command files have no extended ACLs. # ls -lL /etc /bin /usr/bin /usr/local/bin /sbin /usr/sbin /usr/local/sbin If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001270

**Group ID:** `V-22315`

### Rule: System log files must not have extended ACLs, except as needed to support authorized software.

**Rule ID:** `SV-44948r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system log files are not protected, unauthorized users could change the logged data, eliminating its forensic value. Authorized software may be given log file access through the use of extended ACLs when needed and configured to provide the least privileges required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify system log files have no extended ACLs. Procedure: # ls -lL /var/log If the permissions include a '+', the file has an extended ACL. If an extended ACL exists, verify with the SA if the ACL is required to support authorized software and provides the minimum necessary permissions. If an extended ACL exists providing access beyond the needs of authorized software, this is a finding.

## Group: GEN001290

**Group ID:** `V-22316`

### Rule: All manual page files must not have extended ACLs.

**Rule ID:** `SV-44950r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If manual pages are compromised, misleading information could be inserted, causing actions to compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify all manual page files have no extended ACLs. # ls -lL /usr/share/man /usr/share/man/man* /usr/share/info If the permissions include a '+', the file has an extended ACL this is a finding.

## Group: GEN001310

**Group ID:** `V-22317`

### Rule: All library files must not have extended ACLs.

**Rule ID:** `SV-44952r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized access could destroy the integrity of the library files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify system libraries have no extended ACLs. # ls -lL /usr/lib/* /usr/lib64/* /lib/* /lib64/* | grep "+ " If the permissions include a '+', the file has an extended ACL and has not been approved by the IAO, this is a finding.

## Group: GEN001361

**Group ID:** `V-22318`

### Rule: NIS/NIS+/yp command files must not have extended ACLs.

**Rule ID:** `SV-44964r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIS/NIS+/yp files are part of the system's identification and authentication processes and are critical to system security. ACLs on these files could result in unauthorized modification, which could compromise these processes and the system. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify NIS/NIS+/yp files have no extended ACLs. # ls -lL /var/yp/* If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001362

**Group ID:** `V-22319`

### Rule: The /etc/resolv.conf file must be owned by root.

**Rule ID:** `SV-44972r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The resolv.conf (or equivalent) file configures the system's DNS resolver. DNS is used to resolve host names to IP addresses. If DNS configuration is modified maliciously, host name resolution may fail or return incorrect information. DNS may be used by a variety of system security functions such as time synchronization, centralized authentication, and remote system logging. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /etc/resolv.conf file is owned by root. # ls -l /etc/resolv.conf If the file is not owned by root, this is a finding.

## Group: GEN001363

**Group ID:** `V-22320`

### Rule: The /etc/resolve.conf file must be group-owned by root, bin, sys or system.

**Rule ID:** `SV-44974r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The resolv.conf (or equivalent) file configures the system's DNS resolver. DNS is used to resolve host names to IP addresses. If DNS configuration is modified maliciously, host name resolution may fail or return incorrect information. DNS may be used by a variety of system security functions such as time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the resolv.conf file. Procedure: # ls -lL /etc/resolv.conf If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN001364

**Group ID:** `V-22321`

### Rule: The /etc/resolv.conf file must have mode 0644 or less permissive.

**Rule ID:** `SV-44976r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The resolv.conf (or equivalent) file configures the system's DNS resolver. DNS is used to resolve host names to IP addresses. If DNS configuration is modified maliciously, host name resolution may fail or return incorrect information. DNS may be used by a variety of system security functions such as time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the /etc/resolv.conf file. # ls -l /etc/resolv.conf If the file mode is not 0644, this is a finding.

## Group: GEN001365

**Group ID:** `V-22322`

### Rule: The /etc/resolv.conf file must not have an extended ACL.

**Rule ID:** `SV-44978r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The resolv.conf (or equivalent) file configures the system's DNS resolver. DNS is used to resolve host names to IP addresses. If DNS configuration is modified maliciously, host name resolution may fail or return incorrect information. DNS may be used by a variety of system security functions such as time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify /etc/resolv.conf has no extended ACL. # ls -l /etc/resolv.conf If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001366

**Group ID:** `V-22323`

### Rule: The /etc/hosts file must be owned by root.

**Rule ID:** `SV-44981r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/hosts file (or equivalent) configures local host name to IP address mappings that typically take precedence over DNS resolution. If this file is maliciously modified, it could cause the failure or compromise of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /etc/hosts file is owned by root. # ls -l /etc/hosts If the file is not owned by root, this is a finding.

## Group: GEN001367

**Group ID:** `V-22324`

### Rule: The /etc/hosts file must be group-owned by root, bin, sys or system.

**Rule ID:** `SV-44982r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/hosts file (or equivalent) configures local host name to IP address mappings that typically take precedence over DNS resolution. If this file is maliciously modified, it could cause the failure or compromise of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the /etc/hosts file's group ownership. Procedure: # ls -lL /etc/hosts If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN001368

**Group ID:** `V-22325`

### Rule: The /etc/hosts file must have mode 0644 or less permissive.

**Rule ID:** `SV-44983r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/hosts file (or equivalent) configures local host name to IP address mappings that typically take precedence over DNS resolution. If this file is maliciously modified, it could cause the failure or compromise of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the /etc/hosts file. # ls -l /etc/hosts If the file mode is not 0644, this is a finding.

## Group: GEN001369

**Group ID:** `V-22326`

### Rule: The /etc/hosts file must not have an extended ACL.

**Rule ID:** `SV-44984r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/hosts file (or equivalent) configures local host name to IP address mappings that typically take precedence over DNS resolution. If this file is maliciously modified, it could cause the failure or compromise of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify /etc/hosts has no extended ACL. # ls -l /etc/hosts If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001371

**Group ID:** `V-22327`

### Rule: The /etc/nsswitch.conf file must be owned by root.


**Rule ID:** `SV-44985r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The nsswitch.conf file (or equivalent) configures the source of a variety of system security information including account, group, and host lookups. Malicious changes could prevent the system from functioning or compromise system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /etc/nsswitch.conf file is owned by root. # ls -l /etc/nsswitch.conf If the file is not owned by root, this is a finding.

## Group: GEN001372

**Group ID:** `V-22328`

### Rule: The /etc/nsswitch.conf file must be group-owned by root, bin, sys or system.

**Rule ID:** `SV-44986r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The nsswitch.conf file (or equivalent) configures the source of a variety of system security information including account, group, and host lookups. Malicious changes could prevent the system from functioning or compromise system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the nsswitch.conf file. Procedure: # ls -lL /etc/nsswitch.conf If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN001373

**Group ID:** `V-22329`

### Rule: The /etc/nsswitch.conf file must have mode 0644 or less permissive.

**Rule ID:** `SV-44987r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The nsswitch.conf file (or equivalent) configures the source of a variety of system security information including account, group, and host lookups. Malicious changes could prevent the system from functioning or compromise system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the /etc/nsswitch.conf file. # ls -l /etc/nsswitch.conf If the file mode is not 0644, this is a finding.

## Group: GEN001374

**Group ID:** `V-22330`

### Rule: The /etc/nsswitch.conf file must not have an extended ACL.

**Rule ID:** `SV-44988r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The nsswitch.conf file (or equivalent) configures the source of a variety of system security information including account, group, and host lookups. Malicious changes could prevent the system from functioning or compromise system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify /etc/nsswitch.conf has no extended ACL. # ls -l /etc/nsswitch.conf If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001375

**Group ID:** `V-22331`

### Rule: For systems using DNS resolution, at least two name servers must be configured.

**Rule ID:** `SV-44989r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To provide availability for name resolution services, multiple redundant name servers are mandated. A failure in name resolution could lead to the failure of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if DNS is enabled on the system. # grep dns /etc/nsswitch.conf If no line is returned, or any returned line is commented out, the system does not use DNS, and this is not applicable. Determine the name servers used by the system. # grep nameserver /etc/resolv.conf If less than two lines are returned that are not commented out, this is a finding.

## Group: GEN001378

**Group ID:** `V-22332`

### Rule: The /etc/passwd file must be owned by root.

**Rule ID:** `SV-44990r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/passwd file contains the list of local system accounts. It is vital to system security and must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /etc/passwd file is owned by root. # ls -l /etc/passwd If the file is not owned by root, this is a finding.

## Group: GEN001379

**Group ID:** `V-22333`

### Rule: The /etc/passwd file must be group-owned by root, bin, sys or system.

**Rule ID:** `SV-44991r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/passwd file contains the list of local system accounts. It is vital to system security and must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the passwd file. Procedure: # ls -lL /etc/passwd If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN001390

**Group ID:** `V-22334`

### Rule: The /etc/passwd file must not have an extended ACL.

**Rule ID:** `SV-44993r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File system ACLs can provide access to files beyond what is allowed by the mode numbers of the files. The /etc/passwd file contains the list of local system accounts. It is vital to system security and must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify /etc/passwd has no extended ACL. # ls -l /etc/passwd If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001391

**Group ID:** `V-22335`

### Rule: The /etc/group file must be owned by root.

**Rule ID:** `SV-44995r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/group file is critical to system security and must be owned by a privileged user. The group file contains a list of system groups and associated information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /etc/group file is owned by root. # ls -l /etc/group If the file is not owned by root, this is a finding.

## Group: GEN001392

**Group ID:** `V-22336`

### Rule: The /etc/group file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-44997r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/group file is critical to system security and must be protected from unauthorized modification. The group file contains a list of system groups and associated information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the /etc/group file. Procedure: # ls -lL /etc/group If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN001393

**Group ID:** `V-22337`

### Rule: The /etc/group file must have mode 0644 or less permissive.

**Rule ID:** `SV-44998r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/group file is critical to system security and must be protected from unauthorized modification. The group file contains a list of system groups and associated information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the /etc/group file. # ls -l /etc/group If the file mode is more permissive than 0644, this is a finding.

## Group: GEN001394

**Group ID:** `V-22338`

### Rule: The /etc/group file must not have an extended ACL.

**Rule ID:** `SV-44999r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/group file is critical to system security and must be protected from unauthorized modification. The group file contains a list of system groups and associated information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify /etc/group has no extended ACL. # ls -l /etc/group If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001410

**Group ID:** `V-22339`

### Rule: The /etc/shadow file (or equivalent) must be group-owned by root, bin, sys, or shadow.

**Rule ID:** `SV-45001r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/shadow file contains the list of local system accounts. It is vital to system security and must be protected from unauthorized modification. The file also contains password hashes which must not be accessible to users other than root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the /etc/shadow file. Procedure: # ls -lL /etc/shadow If the file is not group-owned by root, bin, sys, or shadow, this is a finding.

## Group: GEN001430

**Group ID:** `V-22340`

### Rule: The /etc/shadow file must not have an extended ACL.

**Rule ID:** `SV-45006r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/shadow file contains the list of local system accounts. It is vital to system security and must be protected from unauthorized modification. The file also contains password hashes which must not be accessible to users other than root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify /etc/shadow has no extended ACL. # ls -l /etc/shadow If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001470

**Group ID:** `V-22347`

### Rule: The /etc/passwd file must not contain password hashes.

**Rule ID:** `SV-45016r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If password hashes are readable by non-administrators, the passwords are subject to attack through lookup tables or cryptographic weaknesses in the hashes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify no password hashes are present in /etc/passwd. # cut -d : -f 2 /etc/passwd | egrep -v '^(x|\*)$' If any password hashes are returned, this is a finding.

## Group: GEN001475

**Group ID:** `V-22348`

### Rule: The /etc/group file must not contain any group password hashes.

**Rule ID:** `SV-45017r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Group passwords are typically shared and should not be used. Additionally, if password hashes are readable by non-administrators, the passwords are subject to attack through lookup tables or cryptographic weaknesses in the hashes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the /etc/group file for password hashes. # cut -d : -f 2 /etc/group | egrep -v '^(x|!)$' If any password hashes are returned, this is a finding.

## Group: GEN001490

**Group ID:** `V-22350`

### Rule: User home directories must not have extended ACLs.

**Rule ID:** `SV-45029r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Excessive permissions on home directories allow unauthorized access to user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify user home directories have no extended ACLs. # cut -d : -f 6 /etc/passwd | xargs -n1 ls -ld If the permissions include a '+', the file has an extended ACL this is a finding.

## Group: GEN001550

**Group ID:** `V-22351`

### Rule: All files and directories contained in user home directories must be group-owned by a group of which the home directorys owner is a member.

**Rule ID:** `SV-45038r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user's files are group-owned by a group of which the user is not a member, unintended users may be able to access them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of user home directories for files group-owned by a group of which the home directory's owner is not a member. 1. List the user accounts. # cut -d : -f 1 /etc/passwd 2. For each user account, get a list of GIDs for files in the user's home directory. # find ~username -printf %G\\n | sort | uniq 3. Obtain the list of GIDs where the user is a member. # id -G username 4. Check the GID lists. If there are GIDs in the file list not present in the user list, this is a finding.

## Group: GEN001570

**Group ID:** `V-22352`

### Rule: All files and directories contained in user home directories must not have extended ACLs.

**Rule ID:** `SV-45042r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions allow unauthorized access to user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of user home directories for files with extended ACLs. # cut -d : -f 6 /etc/passwd | xargs -n1 -IDIR ls -alLR DIR If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001590

**Group ID:** `V-22353`

### Rule: All run control scripts must have no extended ACLs.

**Rule ID:** `SV-45059r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the startup files are writable by other users, they could modify the startup files to insert malicious commands into the startup files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts have no extended ACLs. # ls -lL /etc/rc* /etc/init.d If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001605

**Group ID:** `V-22354`

### Rule: Run control scripts library search paths must contain only absolute paths.

**Rule ID:** `SV-45066r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library search path environment variable(s) contain a list of directories for the dynamic linker to search to find libraries. If this path includes the current working directory or other relative paths, libraries in these directories may be loaded instead of system libraries. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' library search paths. # grep -r LD_LIBRARY_PATH /etc/rc* /etc/init.d This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) this is a relative path, this is a finding.

## Group: GEN001610

**Group ID:** `V-22355`

### Rule: Run control scripts lists of preloaded libraries must contain only absolute paths.

**Rule ID:** `SV-45067r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries relative to the current working directory, unintended libraries may be preloaded. This variable is formatted as a space-separated list of libraries. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' library preload list. # grep -r LD_PRELOAD /etc/rc* /etc/init.d This variable is formatted as a colon-separated list of paths. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) this is a relative path, this is a finding.

## Group: GEN001730

**Group ID:** `V-22356`

### Rule: All global initialization files must not have extended ACLs.

**Rule ID:** `SV-45102r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Global initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check global initialization files for extended ACLs: # ls -l /etc/bash.bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc 2>/dev/null|grep "\+ " If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001810

**Group ID:** `V-22357`

### Rule: Skeleton files must not have extended ACLs.

**Rule ID:** `SV-45134r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the skeleton files are not protected, unauthorized personnel could change user startup parameters and possibly jeopardize user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check skeleton files for extended ACLs: # ls -alL /etc/skel. If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001830

**Group ID:** `V-22358`

### Rule: All skeleton files (typically in /etc/skel) must be group-owned by root, bin or sys.

**Rule ID:** `SV-45139r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the skeleton files are not protected, unauthorized personnel could change user startup parameters and possibly jeopardize user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the skeleton files are group-owned by root, bin or sys. Procedure: # ls -alL /etc/skel If a skeleton file is not group-owned by root, bin or sys this is a finding.

## Group: GEN001845

**Group ID:** `V-22359`

### Rule: Global initialization files library search paths must contain only absolute paths.

**Rule ID:** `SV-45145r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library search path environment variable(s) contain a list of directories for the dynamic linker to search to find libraries. If this path includes the current working directory or other relative paths, libraries in these directories may be loaded instead of system libraries. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the global initialization files' library search paths. Procedure: # grep LD_LIBRARY_PATH /etc/bash.bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) this is a relative path, this is a finding.

## Group: GEN001850

**Group ID:** `V-22360`

### Rule: Global initialization files lists of preloaded libraries must contain only absolute paths.

**Rule ID:** `SV-45149r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries relative to the current working directory, unintended libraries may be preloaded. This variable is formatted as a space-separated list of libraries. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the global initialization files' library preload list. # grep -r LD_PRELOAD /etc/bash.bashrc /etc/csh.cshrc /etc/csh.login /etc/environment /etc/ksh.kshrc /etc/profile /etc/profile.d/* /etc/zshrc This variable is formatted as a colon-separated list of paths. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) this is a relative path, this is a finding.

## Group: GEN001870

**Group ID:** `V-22361`

### Rule: Local initialization files must be group-owned by the users primary group or root.

**Rule ID:** `SV-45153r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check user home directories for local initialization files group-owned by a group other than the user's primary group or root. Procedure: # ls –a /<users home directory> | grep “^\.” | awk '{if ((!($1=="."))&&(!($1==".."))) print}' | xargs ls –ld If any file is not group-owned by root or the user's primary GID, this is a finding.

## Group: GEN001890

**Group ID:** `V-22362`

### Rule: Local initialization files must not have extended ACLs.

**Rule ID:** `SV-45156r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check user home directories for local initialization files with extended ACLs. # for HOMEDIR in $(cut -d: -f6 /etc/passwd); do find ${HOMEDIR} -type f -name '\.*' | xargs ls -ld | grep '\+'; done If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN001901

**Group ID:** `V-22363`

### Rule: Local initialization files library search paths must contain only absolute paths.

**Rule ID:** `SV-45160r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library search path environment variable(s) contain a list of directories for the dynamic linker to search to find libraries. If this path includes the current working directory or other relative paths, libraries in these directories may be loaded instead of system libraries. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify local initialization files have library search path containing only absolute paths. Procedure: # cut -d: -f6 /etc/passwd |xargs -n1 -IDIR find DIR -name ".*" -type f -maxdepth 1 -exec grep -H LD_LIBRARY_PATH {} \; This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) this is a relative path, this is a finding.

## Group: GEN001902

**Group ID:** `V-22364`

### Rule: Local initialization files lists of preloaded libraries must contain only absolute paths.

**Rule ID:** `SV-45161r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries relative to the current working directory, unintended libraries may be preloaded. This variable is formatted as a space-separated list of libraries. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify local initialization files have library preload list containing only absolute paths. Procedure: # cut -d: -f6 /etc/passwd |xargs -n1 -IDIR find DIR -name ".*" -type f -maxdepth 1 -exec grep -H LD_PRELOAD {} \; This variable is formatted as a colon-separated list of paths. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) this is a relative path, this is a finding.

## Group: GEN002210

**Group ID:** `V-22365`

### Rule: All shell files must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45173r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If shell files are group-owned by users other than root or a system group, they could be modified by intruders or malicious users to perform unauthorized actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If /etc/shells exists, check the group ownership of each shell referenced. Procedure: # cat /etc/shells | xargs -n1 ls -l Otherwise, check any shells found on the system. Procedure: # find / -name "*sh" | xargs -n1 ls -l If a shell is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN002230

**Group ID:** `V-22366`

### Rule: All shell files must not have extended ACLs.

**Rule ID:** `SV-45175r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shells with world/group write permissions give the ability to maliciously modify the shell to obtain unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If /etc/shells exists, check the permissions of each shell referenced. # cat /etc/shells | xargs -n1 ls -lL Otherwise, check any shells found on the system. # find / -name "*sh" | xargs -n1 ls -lL If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN002430

**Group ID:** `V-22368`

### Rule: Removable media, remote file systems, and any file system not containing approved device files must be mounted with the nodev option.

**Rule ID:** `SV-45190r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" (or equivalent) mount option causes the system to not handle device files as system devices. This option must be used for mounting any file system not containing approved device files. Device files can provide direct access to system hardware and can compromise security if not protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/fstab and verify the "nodev" mount option is used on any filesystems mounted from removable media or network shares. If any filesystem mounted from removable media or network shares does not have this option, this is a finding.

## Group: GEN002710

**Group ID:** `V-22369`

### Rule: All system audit files must not have extended ACLs.

**Rule ID:** `SV-45211r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user can write to the audit logs, then audit trails can be modified or destroyed and system intrusion may not be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system audit log files for extended ACLs. Procedure: # grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//|xargs ls -l If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN002715

**Group ID:** `V-22370`

### Rule: System audit tool executables must be owned by root.

**Rule ID:** `SV-45272r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To prevent unauthorized access or manipulation of system audit logs, the tools for manipulating those logs must be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tool executables are owned by root. # ls -l /sbin/auditctl /sbin/auditd /sbin/ausearch /sbin/aureport /sbin/autrace /sbin/audispd If any listed file is not owned by root, this is a finding.

## Group: GEN002716

**Group ID:** `V-22371`

### Rule: System audit tool executables must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45274r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To prevent unauthorized access or manipulation of system audit logs, the tools for manipulating those logs must be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tool executables are group-owned by root, bin, sys, or system. Procedure: # ls -lL /sbin/auditctl /sbin/auditd /sbin/ausearch /sbin/aureport /sbin/autrace /sbin/audispd If any listed file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN002717

**Group ID:** `V-22372`

### Rule: System audit tool executables must have mode 0750 or less permissive.

**Rule ID:** `SV-45277r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To prevent unauthorized access or manipulation of system audit logs, the tools for manipulating those logs must be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of audit tool executables. # ls -l /sbin/auditctl /sbin/auditd /sbin/ausearch /sbin/aureport /sbin/autrace /sbin/audispd If any listed file has a mode more permissive than 0750, this is a finding.

## Group: GEN002718

**Group ID:** `V-22373`

### Rule: System audit tool executables must not have extended ACLs.

**Rule ID:** `SV-45279r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To prevent unauthorized access or manipulation of system audit logs, the tools for manipulating those logs must be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of audit tool executables. # ls -l /sbin/auditctl /sbin/auditd /sbin/ausearch /sbin/aureport /sbin/autrace /sbin/audispd If the permissions include a '+' the file has an extended ACL, this is a finding.

## Group: GEN002719

**Group ID:** `V-22374`

### Rule: The audit system must alert the SA in the event of an audit processing failure.

**Rule ID:** `SV-45285r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An accurate and current audit trail is essential for maintaining a record of system activity. If the system fails, the SA must be notified and must take prompt action to correct the problem. Minimally, the system must log this event and the SA will receive this notification during the daily system log review. If feasible, active alerting (such as e-mail or paging) should be employed consistent with the site’s established operations management systems and procedures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /etc/audit/auditd.conf has the disk_full_action and disk_error_action parameters set. Procedure: # grep disk_full_action /etc/audit/auditd.conf If the disk_full_action parameter is missing or set to "suspend" or "ignore" this is a finding. # grep disk_error_action /etc/audit/auditd.conf If the disk_error_action parameter is missing or set to "suspend" or "ignore" this is a finding.

## Group: GEN002730

**Group ID:** `V-22375`

### Rule: The audit system must alert the SA when the audit storage volume approaches its capacity.

**Rule ID:** `SV-45298r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An accurate and current audit trail is essential for maintaining a record of system activity. If the system fails, the SA must be notified and must take prompt action to correct the problem. Minimally, the system must log this event and the SA will receive this notification during the daily system log review. If feasible, active alerting (such as e-mail or paging) should be employed consistent with the site’s established operations management systems and procedures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/audit/auditd.conf for the space_left_action and action_mail_acct parameters. # egrep 'space_left_action|action_mail_acct' /etc/audit/auditd.conf If the space_left_action or the action_mail_acct parameters are set to blanks, this is a finding. If the space_left_action is set to "syslog" the system logs the event, this is not a finding. If the space_left_action is set to "exec" the system executes a designated script. If this script informs the SA of the event, this is not a finding. If the space_left_action parameter is missing, this is a finding. If the space_left_action parameter is set to "ignore" or "suspend" no logging would be performed after the event, this is a finding. If the space_left_action parameter is set to "single" or "halt" this effectively stops the system causing a Denial of Service, this is a finding. If the space_left_action is set to "email" and the action_mail_acct parameter is not set to the e-mail address of the system administrator, this is a finding. The action_mail_acct parameter, if missing, defaults to "root". Note that if the email address of the system administrator is on a remote system "sendmail" must be available.

## Group: GEN002750

**Group ID:** `V-22376`

### Rule: The audit system must be configured to audit account creation.

**Rule ID:** `SV-45305r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises, and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the useradd and groupadd executable are audited. # auditctl -l | egrep '(useradd|groupadd)' If either useradd or groupadd are not listed with a permissions filter of at least 'x', this is a finding. Determine if /etc/passwd, /etc/shadow, /etc/group, and /etc/gshadow are audited for appending. # auditctl -l | egrep '(/etc/passwd|/etc/shadow|/etc/group|/etc/gshadow)' If any of these are not listed with a permissions filter of at least 'a', this is a finding.

## Group: GEN002751

**Group ID:** `V-22377`

### Rule: The audit system must be configured to audit account modification.

**Rule ID:** `SV-45308r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the usermod and groupmod executable are audited. # auditctl -l | egrep '(usermod|groupmod)' If either usermod or groupmod are not listed with a permissions filter of at least 'x', this is a finding. Determine if /etc/passwd, /etc/shadow, /etc/group, and /etc/gshadow are audited for writing. # auditctl -l | egrep '(/etc/passwd|/etc/shadow|/etc/group|/etc/gshadow)' If any of these are not listed with a permissions filter of at least 'w', this is a finding.

## Group: GEN002752

**Group ID:** `V-22378`

### Rule: The audit system must be configured to audit account disabling.

**Rule ID:** `SV-45319r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the passwd executable is audited. # auditctl -l | grep /usr/bin/passwd If passwd is not listed with a permissions filter of at least 'x', this is a finding.

## Group: GEN002753

**Group ID:** `V-22382`

### Rule: The audit system must be configured to audit account termination.

**Rule ID:** `SV-45323r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the userdel and groupdel executable are audited. # auditctl -l | egrep '(userdel|groupdel)' If either userdel or groupdel are not listed with a permissions filter of at least 'x', this is a finding.

## Group: GEN002825

**Group ID:** `V-22383`

### Rule: The audit system must be configured to audit the loading and unloading of dynamic kernel modules.

**Rule ID:** `SV-45556r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Actions concerning dynamic kernel modules must be recorded as they are substantial events. Dynamic kernel modules can increase the attack surface of a system. A malicious kernel module can be used to substantially alter the functioning of a system, often with the purpose of hiding a compromise from the SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the init_module and delete_module syscalls are audited. # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "init_module" If the result does not contain "-S init_module" ,this is a finding.

## Group: GEN002990

**Group ID:** `V-22384`

### Rule: The cron.allow file must not have an extended ACL.

**Rule ID:** `SV-45574r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A readable and/or writeable cron.allow file by other users than root could allow potential intruders and malicious users to use the file contents to help discern information, such as who is allowed to execute cron programs, which could be harmful to overall system and network security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the cron.allow file. # ls -l /etc/cron.allow If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003050

**Group ID:** `V-22385`

### Rule: Crontab files must be group-owned by root, cron, or the crontab creators primary group.

**Rule ID:** `SV-45596r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of scheduled system jobs and prevent malicious modification to these jobs, crontab files must be secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the crontab files. Procedure: # ls -lL /var/spool/cron /var/spool/cron/tabs # ls -lL /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls -lL /etc/cron*|grep -v deny If the group owner is not root or the crontab owner's primary group, this is a finding.

## Group: GEN003090

**Group ID:** `V-22386`

### Rule: Crontab files must not have extended ACLs.

**Rule ID:** `SV-45601r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of scheduled system jobs and to prevent malicious modification to these jobs, crontab files must be secured. ACLs on crontab files may provide unauthorized access to the files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the crontab files. Procedure: # ls -lL /var/spool/cron /var/spool/cron/tabs ls –lL /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls -lL /etc/cron*|grep -v deny If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003110

**Group ID:** `V-22387`

### Rule: Cron and crontab directories must not have extended ACLs.

**Rule ID:** `SV-45603r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of scheduled system jobs and to prevent malicious modification to these jobs, crontab files must be secured. ACLs on cron and crontab directories may provide unauthorized access to these directories. Unauthorized modifications to these directories or their contents may result in the addition of unauthorized cron jobs or deny service to authorized cron jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the crontab directories. Procedure: # ls -ld /var/spool/cron /var/spool/cron/tabs ls -ld /etc/crontab /etc/cron.{d,daily,hourly,monthly,weekly} or # ls -ld /etc/cron*|grep -v deny If the permissions include a '+' the directory has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding

## Group: GEN003190

**Group ID:** `V-22388`

### Rule: The cron log files must not have extended ACLs.

**Rule ID:** `SV-45622r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron logs contain reports of scheduled system activities and must be protected from unauthorized access or manipulation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. Procedure: Check the configured cron log file found in the cron entry of the rsyslog configuration (normally /var/log/cron). # grep cron /etc/rsyslog.conf /etc/rsyslog.d/*.conf # ls -lL /var/log/cron If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003210

**Group ID:** `V-22389`

### Rule: The cron.deny file must not have an extended ACL.

**Rule ID:** `SV-45628r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If there are excessive file permissions for the cron.deny file, sensitive information could be viewed or edited by unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/cron.deny If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003245

**Group ID:** `V-22390`

### Rule: The at.allow file must not have an extended ACL.

**Rule ID:** `SV-45639r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File system extended ACLs provide access to files beyond what is allowed by the mode numbers of the files. Unauthorized modification of the at.allow file could result in Denial of Service to authorized "at" users and the granting of the ability to run "at" jobs to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/at.allow If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003250

**Group ID:** `V-22391`

### Rule: The cron.allow file must be group-owned by root, bin, sys, or cron.

**Rule ID:** `SV-45640r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the group of the cron.allow is not set to root, bin, sys, or cron, the possibility exists for an unauthorized user to view or edit the list of users permitted to use cron. Unauthorized modification of this file could cause Denial of Service to authorized cron users or provide unauthorized users with the ability to run cron jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the file. Procedure: # ls -lL /etc/cron.allow If the file is not group-owned by root, bin, sys, or cron, this is a finding.

## Group: GEN003252

**Group ID:** `V-22392`

### Rule: The at.deny file must have mode 0600 or less permissive.

**Rule ID:** `SV-45641r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "at" daemon control files restrict access to scheduled job manipulation and must be protected. Unauthorized modification of the at.deny file could result in Denial of Service to authorized "at" users or provide unauthorized users with the ability to run "at" jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/at.deny If the file has a mode more permissive than 0600, this is a finding.

## Group: GEN003255

**Group ID:** `V-22393`

### Rule: The at.deny file must not have an extended ACL.

**Rule ID:** `SV-45642r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "at" daemon control files restrict access to scheduled job manipulation and must be protected. Unauthorized modification of the at.deny file could result in Denial of Service to authorized "at" users or provide unauthorized users with the ability to run "at" jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/at.deny If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003270

**Group ID:** `V-22394`

### Rule: The cron.deny file must be group-owned by root, bin, sys.

**Rule ID:** `SV-45645r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron daemon control files restrict the scheduling of automated tasks and must be protected. Unauthorized modification of the cron.deny file could result in Denial of Service to authorized cron users or could provide unauthorized users with the ability to run cron jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the file. Procedure: # ls -lL /etc/cron.deny If the file is not group-owned by root, bin or sys this is a finding.

## Group: GEN003410

**Group ID:** `V-22395`

### Rule: The at directory must not have an extended ACL.

**Rule ID:** `SV-45671r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "at" directory has an extended ACL, unauthorized users could be allowed to view or to edit files containing sensitive information within the "at" directory. Unauthorized modifications could result in Denial of Service to authorized "at" jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the directory. # ls -lLd /var/spool/at /var/spool/atjobs If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003430

**Group ID:** `V-22396`

### Rule: The atjobs directory must be group-owned by root, bin, daemon, sys, or at.

**Rule ID:** `SV-45673r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the group of the "atjobs" directory is not root, bin, daemon, sys, or at, unauthorized users could be allowed to view or edit files containing sensitive information within the directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the directory. Procedure: # ls -ld /var/spool/atjobs If the file is not group-owned by root, bin, daemon, sys, or at, this is a finding.

## Group: GEN003470

**Group ID:** `V-22397`

### Rule: The at.allow file must be group-owned by root, bin, sys, or cron.

**Rule ID:** `SV-45676r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the group owner of the at.allow file is not set to root, bin, sys, or cron, unauthorized users could be allowed to view or edit the list of users permitted to run "at" jobs. Unauthorized modification could result in Denial of Service to authorized "at" users or provide unauthorized users with the ability to run "at" jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the file. Procedure: # ls -lL /etc/at.allow If the file is not group-owned by root, bin, sys, or cron, this is a finding.

## Group: GEN003490

**Group ID:** `V-22398`

### Rule: The at.deny file must be group-owned by root, bin, sys, or cron.

**Rule ID:** `SV-45678r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the group owner of the at.deny file is not set to root, bin, sys, or cron, unauthorized users could be allowed to view or edit sensitive information contained within the file. Unauthorized modification could result in Denial of Service to authorized "at" users or provide unauthorized users with the ability to run "at" jobs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the file. Procedure: # ls -lL /etc/at.deny If the file is not group-owned by root, bin, sys, or cron, this is a finding.

## Group: GEN003501

**Group ID:** `V-22399`

### Rule: The system must be configured to store any process core dumps in a specific, centralized directory.

**Rule ID:** `SV-46151r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Specifying a centralized location for core file creation allows for the centralized protection of core files. Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If process core dump creation is not configured to use a centralized directory, core dumps may be created in a directory that does not have appropriate ownership or permissions configured, which could result in unauthorized access to the core dumps.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify a directory is defined for process core dumps. # cat /proc/sys/kernel/core_pattern If the parameter is not an absolute path (does not start with a slash [/]), this is a finding.

## Group: GEN003502

**Group ID:** `V-22400`

### Rule: The centralized process core dump data directory must be owned by root.

**Rule ID:** `SV-46152r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If the centralized process core dump data directory is not owned by root, the core dumps contained in the directory may be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Procedure: Check the defined directory for process core dumps. # cat /proc/sys/kernel/core_pattern|xargs -n1 -IPATTERN dirname PATTERN Check the existence and ownership of the directory # ls -lLd <core file directory> If the directory does not exist or is not owned by root, this is a finding.

## Group: GEN003503

**Group ID:** `V-22401`

### Rule: The centralized process core dump data directory must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46153r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If the centralized process core dump data directory is not group-owned by a system group, the core dumps contained in the directory may be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the defined directory for process core dumps. Procedure: # cat /proc/sys/kernel/core_pattern Check the group ownership of the directory # ls -lLd <core file directory> If the directory is not group-owned by root, bin, sys, or system this is a finding.

## Group: GEN003504

**Group ID:** `V-22402`

### Rule: The centralized process core dump data directory must have mode 0700 or less permissive.

**Rule ID:** `SV-46154r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If the process core dump data directory has a mode more permissive than 0700, unauthorized users may be able to view or to modify sensitive information contained any process core dumps in the directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Procedure: Check the defined directory for process core dumps. # cat /proc/sys/kernel/core_pattern|xargs -n1 -IPATTERN dirname PATTERN Check the permissions of the directory. # ls -lLd <core file directory> If the has a mode more permissive than 0700, this is a finding.

## Group: GEN003505

**Group ID:** `V-22403`

### Rule: The centralized process core dump data directory must not have an extended ACL.

**Rule ID:** `SV-46155r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If the process core dump data directory has an extended ACL, unauthorized users may be able to view or to modify sensitive information contained in any process core dumps in the directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the defined directory for process core dumps. Procedure: Check the defined directory for process core dumps. # cat /proc/sys/kernel/core_pattern|xargs -n1 -IPATTERN dirname PATTERN Check the permissions of the directory. # ls -lLd <core file directory> If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003510

**Group ID:** `V-22404`

### Rule: Kernel core dumps must be disabled unless needed.

**Rule ID:** `SV-45680r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system. The kernel core dump process may increase the amount of time a system is unavailable due to a crash. Kernel core dumps can be useful for kernel debugging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check that the dumpconf service is not running. # /etc/init.d/dumpconf status If a status of “running" is returned, this is a finding.

## Group: GEN003521

**Group ID:** `V-22405`

### Rule: The kernel core dump data directory must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45708r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. As the system memory may contain sensitive information, it must be protected accordingly. If the kernel core dump data directory is not group-owned by a system group, the core dumps contained in the directory may be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the kernel core dump data directory and check its ownership. # ls -ld /var/crash If the directory is not group-owned by root, this is a finding.

## Group: GEN003522

**Group ID:** `V-22406`

### Rule: The kernel core dump data directory must have mode 0700 or less permissive.

**Rule ID:** `SV-45711r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. As the system memory may contain sensitive information, it must be protected accordingly. If the mode of the kernel core dump data directory is more permissive than 0700, unauthorized users may be able to view or to modify kernel core dump data files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the kernel core dump data directory and check its permissions. # ls -ld /var/crash If the directory has a mode more permissive than 0700, this is a finding.

## Group: GEN003523

**Group ID:** `V-22407`

### Rule: The kernel core dump data directory must not have an extended ACL.

**Rule ID:** `SV-45715r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. As the system memory may contain sensitive information, it must be protected accordingly. If there is an extended ACL for the kernel core dump data directory, unauthorized users may be able to view or to modify kernel core dump data files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the kernel core dump data directory and check its permissions. # ls -ld /var/crash If the permissions include a '+' the file has an extended ACL, this is a finding.

## Group: GEN003581

**Group ID:** `V-22408`

### Rule: Network interfaces must not be configured to allow user control.

**Rule ID:** `SV-45718r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration of network interfaces should be limited to privileged users. Manipulation of network interfaces may result in a Denial of Service or bypass of network security mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for user-controlled network interfaces. # grep -i '^USERCONTROL=' /etc/sysconfig/network/ifcfg* | grep -i yes If any results are returned with USERCONTROL set to yes, this is a finding.

## Group: GEN003602

**Group ID:** `V-22409`

### Rule: The system must not process Internet Control Message Protocol (ICMP)  timestamp requests.

**Rule ID:** `SV-45721r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The processing of (ICMP) timestamp requests increases the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not respond to ICMP TIMESTAMP_REQUESTs Procedure: # iptables -L INPUT | grep "timestamp" This should return the following entries for "timestamp-reply" and "timestamp_request": DROP icmp -- anywhere anywhere icmp timestamp-request DROP icmp -- anywhere anywhere icmp timestamp-reply If either does not exist or does not "DROP" the message, this is a finding.

## Group: GEN003603

**Group ID:** `V-22410`

### Rule: The system must not respond to Internet Control Message Protocol v4 (ICMPv4) echoes sent to a broadcast address.

**Rule ID:** `SV-45722r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast (ICMP) echoes facilitates network mapping and provides a vector for amplification attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not respond to ICMP ECHO_REQUESTs set to broadcast addresses. Procedure: # cat /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts If the result is not 1, this is a finding.

## Group: GEN003604

**Group ID:** `V-22411`

### Rule: The system must not respond to Internet Control Message Protocol (ICMP) timestamp requests sent to a broadcast address.

**Rule ID:** `SV-45723r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The processing of (ICMP) timestamp requests increases the attack surface of the system. Responding to broadcast ICMP timestamp requests facilitates network mapping and provides a vector for amplification attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations>GEN000000-FW</Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl>The system's firewall default-deny policy mitigates the risk from this vulnerability.</MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not respond to ICMP TIMESTAMP_REQUESTs set to broadcast addresses. Procedure: # cat /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts If the result is not 1, this is a finding. Note: The same parameter controls both ICMP ECHO_REQUESTs and TIMESTAMP_REQUESTs.

## Group: GEN003605

**Group ID:** `V-22412`

### Rule: The system must not apply reversed source routing to TCP responses.

**Rule ID:** `SV-46156r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the reverse source route settings for the system: # sysctl net.ipv4.conf.all.accept_source_route # sysctl net.ipv4.conf.default.accept_source_route If either setting has a value other than zero, this is a finding.

## Group: GEN003606

**Group ID:** `V-22413`

### Rule: The system must prevent local applications from generating source-routed packets.

**Rule ID:** `SV-46276r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the reverse source route settings for the system: # sysctl net.ipv4.conf.all.accept_source_route # sysctl net.ipv4.conf.default.accept_source_route If either setting has a value other than zero, this is a finding.

## Group: GEN003607

**Group ID:** `V-22414`

### Rule: The system must not accept source-routed IPv4 packets.

**Rule ID:** `SV-45724r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the handling of source-routed traffic destined to the system itself, not to traffic forwarded by the system to another system, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not accept source-routed IPv4 packets. Procedure: # grep [01] /proc/sys/net/ipv4/conf/*/accept_source_route|egrep "default|all" If all of the resulting lines do not end with "0", this is a finding.

## Group: GEN003608

**Group ID:** `V-22415`

### Rule: Proxy Address Resolution Protocol (Proxy ARP) must not be enabled on the system.

**Rule ID:** `SV-45725r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Proxy ARP allows a system to respond to ARP requests on one interface on behalf of hosts connected to another interface. If this function is enabled when not required, addressing information may be leaked between the attached network segments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not use proxy ARP. # grep [01] /proc/sys/net/ipv4/conf/*/proxy_arp|egrep "default|all" If all of the resulting lines do not end with "0", this is a finding.

## Group: GEN003609

**Group ID:** `V-22416`

### Rule: The system must ignore IPv4 Internet Control Message Protocol (ICMP) redirect messages.

**Rule ID:** `SV-45726r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not accept IPv4 ICMP redirect messages. # grep [01] /proc/sys/net/ipv4/conf/*/accept_redirects|egrep "default|all" If all of the resulting lines do not end with "0", this is a finding.

## Group: GEN003610

**Group ID:** `V-22417`

### Rule: The system must not send IPv4 Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-45727r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table possibly revealing portions of the network topology.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not send IPv4 ICMP redirect messages. # grep [01] /proc/sys/net/ipv4/conf/*/send_redirects|egrep "default|all" If all of the resulting lines do not end with "0", this is a finding.

## Group: GEN003611

**Group ID:** `V-22418`

### Rule: The system must log martian packets.

**Rule ID:** `SV-45728r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Martian packets are packets containing addresses known by the system to be invalid. Logging these messages allows the SA to identify misconfigurations or attacks in progress.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system logs martian packets. # grep [01] /proc/sys/net/ipv4/conf/*/log_martians|egrep "default|all" If all of the resulting lines do not end with "1", this is a finding.

## Group: GEN003612

**Group ID:** `V-22419`

### Rule: The system must be configured to use TCP syncookies when experiencing a TCP SYN flood.

**Rule ID:** `SV-46277r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A TCP SYN flood attack can cause Denial of Service by filling a system's TCP connection table with connections in the SYN_RCVD state. Syncookies are a mechanism used to only track a connection when a subsequent ACK is received, verifying the initiator is attempting a valid connection and is not a flood source. This technique does not operate in a fully standards-compliant manner, but is only activated when a flood condition is detected, and allows defense of the system while continuing to service valid requests.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system configured to use TCP syncookies when experiencing a TCP SYN flood. # cat /proc/sys/net/ipv4/tcp_syncookies If the result is not "1", this is a finding.

## Group: GEN003619

**Group ID:** `V-22421`

### Rule: The system must not be configured for network bridging.

**Rule ID:** `SV-45738r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some systems have the ability to bridge or switch frames (link-layer forwarding) between multiple interfaces. This can be useful in a variety of situations but, if enabled when not needed, has the potential to bypass network partitioning and security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is not configured for bridging. # ls /proc/sys/net/bridge If the directory exists, this is a finding. # lsmod | grep '^bridge ' If any results are returned, this is a finding.

## Group: GEN003650

**Group ID:** `V-22422`

### Rule: All local file systems must employ journaling or another mechanism ensuring file system consistency.

**Rule ID:** `SV-45754r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>File system journaling, or logging, can allow reconstruction of file system data after a system crash preserving the integrity of data that may have otherwise been lost. Journaling file systems typically do not require consistency checks upon booting after a crash, which can improve system availability. Some file systems employ other mechanisms to ensure consistency also satisfying this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify local filesystems use journaling. # mount | grep '^/dev/' | egrep -v 'type (ext3|ext4|jfs|reiserfs|xfs|iso9660|udf)' If a mount is listed, this is a finding.

## Group: GEN003730

**Group ID:** `V-22423`

### Rule: The inetd.conf file, xinetd.conf file, and the xinetd.d directory must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45758r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of sensitive files or utilities to system groups may provide unauthorized users with the potential to access sensitive information or change the system configuration possibly weakening the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the xinetd configuration files and directories. Procedure: # ls -alL /etc/xinetd.conf /etc/xinetd.d If a file or directory is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN003745

**Group ID:** `V-22424`

### Rule: The inetd.conf and xinetd.conf files must not have extended ACLs.

**Rule ID:** `SV-45760r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Internet service daemon configuration files must be protected as malicious modification could cause Denial of Service or increase the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the xinetd configuration files. Procedure: # ls -alL /etc/xinetd.conf If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003750

**Group ID:** `V-22425`

### Rule: The xinetd.d directory must have mode 0755 or less permissive.

**Rule ID:** `SV-45761r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Internet service daemon configuration files must be protected as malicious modification could cause Denial of Service or increase the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the xinetd configuration directories. # ls -dlL /etc/xinetd.d If the mode of the directory is more permissive than 0755, this is a finding.

## Group: GEN003755

**Group ID:** `V-22426`

### Rule: The xinetd.d directory must not have an extended ACL.

**Rule ID:** `SV-45762r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Internet service daemon configuration files must be protected as malicious modification could cause Denial of Service or increase the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the xinetd configuration files and directories. # ls -alL /etc/xinetd.conf /etc/xinetd.d If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003770

**Group ID:** `V-22427`

### Rule: The services file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45764r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of system configuration files to root or a system group provides the designated owner and unauthorized users with the potential to change the system configuration possibly weakening the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the services file. Procedure: # ls -lL /etc/services If the file is not group-owned by root, bin, sys, or system, this is a finding

## Group: GEN003790

**Group ID:** `V-22428`

### Rule: The services file must not have an extended ACL.

**Rule ID:** `SV-45782r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The services file is critical to the proper operation of network services and must be protected from unauthorized modification. If the services file has an extended ACL, it may be possible for unauthorized users to modify the file. Unauthorized modification could result in the failure of network services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the /etc/services file. # ls -lL /etc/services If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN003810

**Group ID:** `V-22429`

### Rule: The portmap or rpcbind service must not be running unless needed.

**Rule ID:** `SV-45785r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The portmap and rpcbind services increase the attack surface of the system and should only be used when needed. The portmap or rpcbind services are used by a variety of services using Remote Procedure Calls (RPCs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the status of the portmap and/or rpcbind service. # rcportmap status # rcrpcbind status If the service is running, this is a finding.

## Group: GEN003815

**Group ID:** `V-22430`

### Rule: The portmap or rpcbind service must not be installed unless needed.

**Rule ID:** `SV-45786r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The portmap and rpcbind services increase the attack surface of the system and should only be used when needed. The portmap or rpcbind services are used by a variety of services using Remote Procedure Calls (RPCs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the portmap and/or rpcbind packages are installed. # rpm –q portmap rpcbind If a package is found, this is a finding.

## Group: GEN003825

**Group ID:** `V-22431`

### Rule: The rshd service must not be installed.

**Rule ID:** `SV-45789r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rshd process provides a typically unencrypted, host-authenticated remote access service. SSH should be used in place of this service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the rsh-server package is installed. Procedure: # rpm -qa | grep rsh-server If a package is found, this is a finding.

## Group: GEN003830

**Group ID:** `V-22432`

### Rule: The rlogind service must not be running.

**Rule ID:** `SV-45805r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rlogind process provides a typically unencrypted, host-authenticated remote access service. SSH should be used in place of this service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the rlogind configuration. # cat /etc/xinetd.d/rlogin If the file exists and does not contain "disable = yes" this is a finding.

## Group: GEN003835

**Group ID:** `V-22433`

### Rule: The rlogind service must not be installed.

**Rule ID:** `SV-45806r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rlogind process provides a typically unencrypted, host-authenticated remote access service. SSH should be used in place of this service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the rsh-server package is installed. Procedure: # rpm -qa | grep rsh-server If a package is found, this is a finding.

## Group: GEN003845

**Group ID:** `V-22434`

### Rule: The rexecd service must not be installed.

**Rule ID:** `SV-45808r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rexecd process provides a typically unencrypted, host-authenticated remote access service. SSH should be used in place of this service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the rsh-server package is installed. Procedure: # rpm -qa | grep rsh-server If a package is found, this is a finding.

## Group: GEN003930

**Group ID:** `V-22435`

### Rule: The hosts.lpd (or equivalent) file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45814r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give group-ownership of the hosts.lpd file to root, bin, sys, or system provides the members of the owning group and possible unauthorized users, with the potential to modify the hosts.lpd file. Unauthorized modifications could disrupt access to local printers from authorized remote hosts or permit unauthorized remote access to local printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the /etc/hosts.lpd(or equivalent) file. Procedure: # ls -lL /etc/hosts.lpd If the file is not group-owned by root, bin, sys, or system, this is a finding. Check the group ownership of the /etc/cups/printers.conf file. # ls -lL /etc/cups/printers.conf If the file is not group-owned by lp, this is a finding.

## Group: GEN003950

**Group ID:** `V-22436`

### Rule: The hosts.lpd (or equivalent) file must not have an extended ACL.

**Rule ID:** `SV-45817r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the hosts.lpd (or equivalent) file may permit unauthorized modification. Unauthorized modifications could disrupt access to local printers from authorized remote hosts or permit unauthorized remote access to local printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the /etc/hosts.lpd (or equivalent) file. # find /etc -name hosts.lpd -print # find /etc -name Systems –print # find /etc -name printers.conf -print # ls -lL <print service file> If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN004010

**Group ID:** `V-22437`

### Rule: The traceroute file must not have an extended ACL.

**Rule ID:** `SV-45824r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an extended ACL exists on the traceroute executable file, it may provide unauthorized users with access to the file. Malicious code could be inserted by an attacker and triggered whenever the traceroute command is executed by authorized users. Additionally, if an unauthorized user is granted executable permissions to the traceroute command, it could be used to gain information about the network topology behind the firewall. This information may allow an attacker to determine trusted routers and other network information potentially leading to system and network compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the /usr/sbin/traceroute file. # ls -lL /usr/sbin/traceroute If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN004370

**Group ID:** `V-22438`

### Rule: The aliases file must be group-owned by root, sys, bin, or system.

**Rule ID:** `SV-45848r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the alias file is not group-owned by root or a system group, an unauthorized user may modify the file adding aliases to run malicious code or redirect e-mail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the “sendmail” or “postfix” packages are not installed, this is not applicable. Check the group ownership of the alias files. Procedure: for sendmail: # ls -lL /etc/aliases If the file is not group-owned by root, this is a finding. # ls -lL /etc/aliases.db If the file is not group-owned by root, this is a finding. for postfix: Verify the location of the alias file. # postconf alias_maps This will return the location of the "aliases" file, by default "/etc/aliases". # ls -lL <postfix aliases file> If the file is not group-owned by root, this is a finding. # ls -lL <postfix aliases.db file> If the file is not group-owned by root, this is a finding.

## Group: GEN004390

**Group ID:** `V-22439`

### Rule: The alias file must not have an extended ACL.

**Rule ID:** `SV-45850r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the aliases file may permit unauthorized modification. If the alias file is modified by an unauthorized user, they may modify the file to run malicious code or redirect e-mail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the alias file. Procedure: for sendmail: # ls -lL /etc/aliases /etc/aliases.db If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding. for postfix: Verify the location of the alias file. # postconf alias_maps This will return the location of the "aliases" file. # ls -lL <postfix aliases file> <postfix aliases.db file> If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN004410

**Group ID:** `V-22440`

### Rule: Files executed through a mail aliases file must be group-owned by root, bin, sys, or system, and must reside within a directory group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45852r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a file executed through a mail aliases file is not group-owned by root or a system group, it may be subject to unauthorized modification. Unauthorized modification of files executed through aliases may allow unauthorized users to attain root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Examine the contents of the /etc/aliases file. Procedure: # more /etc/aliases Examine the aliases file for any utilized directories or paths. # ls -lL <file referenced from aliases> Check the permissions for any paths referenced. If the group owner of any file is not root, bin, sys, or system, this is a finding.

## Group: GEN004430

**Group ID:** `V-22441`

### Rule: Files executed through a mail aliases file must not have extended ACLs.

**Rule ID:** `SV-45854r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on files executed through a mail aliases file could result in modification by an unauthorized user, execution of malicious code, and/or system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Examine the contents of the /etc/aliases file. Procedure: # more /etc/aliases Examine the aliases file for any utilized directories or paths. # ls -lL <file referenced from aliases> Check the permissions for any paths referenced. If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN004510

**Group ID:** `V-22442`

### Rule: The SMTP service log file must not have an extended ACL.

**Rule ID:** `SV-45862r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SMTP service log file has an extended ACL, unauthorized users may be allowed to access or to modify the log file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# more /etc/rsyslog.conf Examine /etc/rsyslog.conf and determine the log file(s) receiving logs for "mail.crit", "mail.debug", mail.*, or "*.crit". Check the permissions on these log files. # ls -lL <log file> If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN004930

**Group ID:** `V-22444`

### Rule: The ftpusers file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45882r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the ftpusers file is not group-owned by root or a system group, an unauthorized user may modify the file to allow unauthorized accounts to use FTP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the ftpusers file. Procedure: # ls -lL /etc/ftpusers /etc/vsftpd.ftpusers /etc/vsftpd/ftpusers If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN004950

**Group ID:** `V-22445`

### Rule: The ftpusers file must not have an extended ACL.

**Rule ID:** `SV-45884r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the ftpusers file could permit unauthorized modification. Unauthorized modification could result in Denial of Service to authorized FTP users or permit unauthorized users to access the FTP service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the /etc/ftpusers file. # ls -lL /etc/ftpusers /etc/vsftpd.ftpusers /etc/vsftpd/ftpusers If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN005190

**Group ID:** `V-22446`

### Rule: The .Xauthority files must not have extended ACLs.

**Rule ID:** `SV-45919r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.Xauthority files ensure the user is authorized to access specific X Windows host. Extended ACLs may permit unauthorized modification of these files, which could lead to Denial of Service to authorized access or allow unauthorized access to be obtained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the file permissions for the .Xauthority files. Procedure: # ls -la |egrep "(\.Xauthority|\.xauth)" If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN005305

**Group ID:** `V-22447`

### Rule: The SNMP service must use only SNMPv3 or its successors.

**Rule ID:** `SV-45944r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SNMP Versions 1 and 2 are not considered secure. Without the strong authentication and privacy provided by the SNMP Version 3 User-based Security Model (USM), an attacker or other unauthorized users may gain access to detailed system management information and use the information to launch attacks against the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SNMP daemon is not configured to use the v1 or v2c security models. Procedure: Examine the default install location /etc/snmp/snmpd.conf or: # find / -name snmpd.conf # grep -E '(v1|v2c|community|com2sec)' <snmp.conf file> | grep -v '^#' If any configuration is found, this is a finding.

## Group: GEN005306

**Group ID:** `V-22448`

### Rule: The SNMP service must require the use of a FIPS 140-2 approved cryptographic hash algorithm as part of its authentication and integrity methods.

**Rule ID:** `SV-45948r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SNMP service must use SHA-1 or a FIPS 140-2 approved successor for authentication and integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SNMP daemon uses SHA for SNMPv3 users. Procedure: Examine the default install location /etc/snmp/snmpd.conf or: # find / -name snmpd.conf # grep -v '^#' <snmpd.conf file> | grep -i createuser | grep -vi SHA If any line is present this is a finding.

## Group: GEN005307

**Group ID:** `V-22449`

### Rule: The SNMP service must require the use of a FIPS 140-2 approved encryption algorithm for protecting the privacy of SNMP messages.

**Rule ID:** `SV-45952r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SNMP service must use AES or a FIPS 140-2 approved successor algorithm for protecting the privacy of communications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SNMP daemon uses AES for SNMPv3 users. Procedure: Examine the default install location /etc/snmp/snmpd.conf or: # find / -name snmpd.conf # grep -v '^#' <snmpd.conf file> | grep -i createuser | grep -vi AES If any line is present this is a finding.

## Group: GEN005350

**Group ID:** `V-22450`

### Rule: Management Information Base (MIB) files must not have extended ACLs.

**Rule ID:** `SV-45964r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to read the MIB file could impart special knowledge to an intruder or malicious user about the ability to extract compromising information about the system or network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the file permissions for the MIB files. # find / -name *mib* -o -name *MIB* | xargs ls -lL If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN005365

**Group ID:** `V-22451`

### Rule: The snmpd.conf file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45966r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The snmpd.conf file contains authenticators and must be protected from unauthorized access and modification. If the file is not group-owned by a system group, it may be subject to access and modification from unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the SNMP configuration file. Procedure: Examine the default install location /etc/snmp/snmpd.conf or: # find / -name snmpd.conf # ls -lL <snmpd.conf> If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN005375

**Group ID:** `V-22452`

### Rule: The snmpd.conf file must not have an extended ACL.

**Rule ID:** `SV-45969r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The snmpd.conf file contains authenticators and must be protected from unauthorized access and modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the SNMP configuration file. Procedure: Examine the default install location /etc/snmp/snmpd.conf or: # find / -name snmpd.conf # ls -lL <snmpd.conf> If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN005390

**Group ID:** `V-22453`

### Rule: The /etc/syslog.conf file must have mode 0640 or less permissive.

**Rule ID:** `SV-45972r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized users must not be allowed to access or modify the /etc/syslog.conf file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the rsyslog configuration file(s). # ls -lL /etc/rsyslog.conf /etc/rsyslog.d If the mode of the file is more permissive than 0640, this is a finding.

## Group: GEN005395

**Group ID:** `V-22454`

### Rule: The /etc/syslog.conf file must not have an extended ACL.

**Rule ID:** `SV-45974r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized users must not be allowed to access or modify the /etc/syslog.conf file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the syslog configuration file. # ls -lL /etc/rsyslog.conf /etc/rsyslog.d/ If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN005450

**Group ID:** `V-22455`

### Rule: The system must use a remote syslog server (loghost).

**Rule ID:** `SV-45985r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A syslog server (loghost) receives syslog messages from one or more systems. This data can be used as an authoritative log source in the event a system is compromised and its local logs are suspect.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for remote syslog servers. # grep '@' /etc/rsyslog.conf /etc/rsyslog.d/*.conf | grep -v '^#' If no line is returned, this is a finding.

## Group: GEN005501

**Group ID:** `V-22456`

### Rule: The SSH client must be configured to only use the SSHv2 protocol.

**Rule ID:** `SV-45999r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSHv1 is not a DoD-approved protocol and has many well-known vulnerability exploits. Exploits of the SSH client could provide access to the system with the privileges of the user running the client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH client configuration for allowed protocol versions. # grep -i protocol /etc/ssh/ssh_config | grep -v '^#' If the returned protocol configuration allows versions less than 2, this is a finding

## Group: GEN005504

**Group ID:** `V-22457`

### Rule: The SSH daemon must only listen on management network addresses unless authorized for uses other than management.

**Rule ID:** `SV-46002r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SSH daemon should only listen on network addresses designated for management traffic. If the system has multiple network interfaces and SSH listens on addresses not designated for management traffic, the SSH service could be subject to unauthorized access. If SSH is used for purposes other than management, such as providing an SFTP service, the list of approved listening addresses may be documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA to identify which interfaces on the system are designated for management traffic. If all interfaces on the system are authorized for management traffic, this is not applicable. Check the SSH daemon configuration for listening network addresses. # grep -i Listen /etc/ssh/sshd_config | grep -v '^#' If no configuration is returned, or if a returned 'Listen' configuration contains addresses not designated for management traffic, this is a finding.

## Group: GEN005505

**Group ID:** `V-22458`

### Rule: The SSH daemon must be configured to only use FIPS 140-2 approved ciphers.

**Rule ID:** `SV-46004r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD information systems are required to use FIPS 140-2 approved ciphers. SSHv2 ciphers meeting this requirement are 3DES and AES.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed ciphers. # grep -i ciphers /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, or the returned ciphers list contains any cipher not starting with "3des" or "aes", this is a finding.

## Group: GEN005506

**Group ID:** `V-22459`

### Rule: The SSH daemon must be configured to not use Cipher-Block Chaining (CBC) ciphers.

**Rule ID:** `SV-46010r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Cipher-Block Chaining (CBC) mode of encryption as implemented in the SSHv2 protocol is vulnerable to chosen plain text attacks and must not be used. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed ciphers. # grep -i ciphers /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, or the returned ciphers list contains any cipher ending with "cbc", this is a finding.

## Group: GEN005507

**Group ID:** `V-22460`

### Rule: The SSH daemon must be configured to only use Message Authentication Codes (MACs) employing FIPS 140-2 approved cryptographic hash algorithms.

**Rule ID:** `SV-46012r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD information systems are required to use FIPS 140-2 approved cryptographic hash functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed MACs. Procedure: # grep -i macs /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, or the returned MACs list contains any MAC less than "hmac-sha1", this is a finding.

## Group: GEN005510

**Group ID:** `V-22461`

### Rule: The SSH client must be configured to only use FIPS 140-2 approved ciphers.

**Rule ID:** `SV-46015r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD information systems are required to use FIPS 140-2 approved ciphers. SSHv2 ciphers meeting this requirement are 3DES and AES.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH client configuration for allowed ciphers. # grep -i ciphers /etc/ssh/ssh_config | grep -v '^#' If no lines are returned, or the returned ciphers list contains any cipher not starting with "3des" or "aes", this is a finding.

## Group: GEN005511

**Group ID:** `V-22462`

### Rule: The SSH client must be configured to not use Cipher-Block Chaining (CBC)-based ciphers.

**Rule ID:** `SV-46017r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The (CBC) mode of encryption as implemented in the SSHv2 protocol is vulnerable to chosen-plaintext attacks and must not be used. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH client configuration for allowed ciphers. # grep -i ciphers /etc/ssh/ssh_config | grep -v '^#' If no lines are returned, or the returned ciphers list contains any cipher ending with "cbc", this is a finding.

## Group: GEN005512

**Group ID:** `V-22463`

### Rule: The SSH client must be configured to only use Message Authentication Codes (MACs) employing FIPS 140-2 approved cryptographic hash algorithms.

**Rule ID:** `SV-46020r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD information systems are required to use FIPS 140-2 approved cryptographic hash functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH client configuration for allowed MACs. # grep -i macs /etc/ssh/ssh_config | grep -v '^#' If no lines are returned, or the returned MACs list contains any MAC less than "hmac-sha1", this is a finding.

## Group: GEN005521

**Group ID:** `V-22470`

### Rule: The SSH daemon must restrict login ability to specific users and/or groups.

**Rule ID:** `SV-46033r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting SSH logins to a limited group of users, such as system administrators, prevents password-guessing and other SSH attacks from reaching system accounts and other accounts not authorized for SSH access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
There are two ways in which access to SSH may restrict users or groups. Check if /etc/pam.d/sshd is configured to require daemon style login control. # grep pam_access.so /etc/pam.d/sshd|grep "required"|grep "account"| grep -v '^#' If no lines are returned, sshd is not configured to use pam_access. Check the SSH daemon configuration for the AllowGroups setting. # egrep -i "AllowGroups|AllowUsers" /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, sshd is not configured to limit access to users/groups. If sshd is not configured to limit access either through pam_access or the use "AllowUsers" or "Allowgroups", this is a finding.

## Group: GEN005522

**Group ID:** `V-22471`

### Rule: The SSH public host key files must have mode 0644 or less permissive.

**Rule ID:** `SV-46050r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions for SSH public host key files. # ls -lL /etc/ssh/*key.pub If any file has a mode more permissive than 0644, this is a finding.

## Group: GEN005523

**Group ID:** `V-22472`

### Rule: The SSH private host key files must have mode 0600 or less permissive.

**Rule ID:** `SV-46051r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions for SSH private host key files. # ls -lL /etc/ssh/*key If any file has a mode more permissive than 0600, this is a finding.

## Group: GEN005524

**Group ID:** `V-22473`

### Rule: The SSH daemon must not permit GSSAPI authentication unless needed.

**Rule ID:** `SV-46052r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through SSH exposes the system’s GSSAPI to remote hosts, increasing the attack surface of the system. GSSAPI authentication must be disabled unless needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if GSSAPI authentication is used for SSH authentication to the system. If so, this is not applicable. Check the SSH daemon configuration for the GSSAPIAuthentication setting. # grep -i GSSAPIAuthentication /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, or the setting is set to "yes", this is a finding.

## Group: GEN005525

**Group ID:** `V-22474`

### Rule: The SSH client must not permit GSSAPI authentication unless needed.

**Rule ID:** `SV-46053r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through SSH exposes the system’s GSSAPI to remote hosts, increasing the attack surface of the system. GSSAPI authentication must be disabled unless needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH clients configuration for the GSSAPIAuthentication setting. # grep -i GSSAPIAuthentication /etc/ssh/ssh_config | grep -v '^#' If no lines are returned, or the setting is set to "yes", this is a finding.

## Group: GEN005526

**Group ID:** `V-22475`

### Rule: The SSH daemon must not permit Kerberos authentication unless needed.

**Rule ID:** `SV-46087r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Kerberos authentication for SSH is often implemented using GSSAPI. If Kerberos is enabled through SSH, the SSH daemon provides a means of access to the system's Kerberos implementation. Vulnerabilities in the system's Kerberos implementation may then be subject to exploitation. To reduce the attack surface of the system, the Kerberos authentication mechanism within SSH must be disabled for systems not using this capability. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if Kerberos authentication is used by the system. If it is, this is not applicable. Check the SSH daemon configuration for the KerberosAuthentication setting. # grep -i KerberosAuthentication /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, or the setting is set to "yes", this is a finding.

## Group: GEN005533

**Group ID:** `V-22482`

### Rule: The SSH daemon must limit connections to a single session.

**Rule ID:** `SV-46097r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The SSH protocol has the ability to provide multiple sessions over a single connection without reauthentication. A compromised client could use this feature to establish additional sessions to a system without consent or knowledge of the user. Alternate per-connection session limits may be documented if needed for a valid mission requirement. Greater limits are expected to be necessary in situations where TCP or X11 forwarding are used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>true</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the MaxSessions setting. # grep -i MaxSessions /etc/ssh/sshd_config | grep -v '^#' If the setting is not present, or not set to "1", this is a finding.

## Group: GEN005536

**Group ID:** `V-22485`

### Rule: The SSH daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-46098r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log into the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the StrictModes setting. # grep -i StrictModes /etc/ssh/sshd_config | grep -v '^#' If the setting is not present, or not set to "yes", this is a finding.

## Group: GEN005537

**Group ID:** `V-22486`

### Rule: The SSH daemon must use privilege separation.

**Rule ID:** `SV-46100r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH daemon privilege separation causes the SSH process to drop root privileges when not needed, which would decrease the impact of software vulnerabilities in the unprivileged section.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the UsePrivilegeSeparation setting. # grep -i UsePrivilegeSeparation /etc/ssh/sshd_config | grep -v '^#' If the setting is not present, or not set to "yes", this is a finding.

## Group: GEN005538

**Group ID:** `V-22487`

### Rule: The SSH daemon must not allow rhosts RSA authentication.


**Rule ID:** `SV-46105r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SSH permits rhosts RSA authentication, a user may be able to log in based on the keys of the host originating the request and not any user-specific authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the RhostsRSAAuthentication setting. # grep -i RhostsRSAAuthentication /etc/ssh/sshd_config | grep -v '^#' If the setting is set to "yes", this is a finding.

## Group: GEN005539

**Group ID:** `V-22488`

### Rule: The SSH daemon must not allow compression or must only allow compression after successful authentication.

**Rule ID:** `SV-46107r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in an SSH connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection, potentially with root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the compression setting. # grep -i Compression /etc/ssh/sshd_config | egrep "no|delayed" If the setting is missing or is commented out, this is a finding. If the setting is present but is not set to "no" or "delayed", this is a finding.

## Group: GEN005550

**Group ID:** `V-22489`

### Rule: The SSH daemon must be configured with the Department of Defense (DoD) logon banner.

**Rule ID:** `SV-46109r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to display the DoD logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources. The SSH service must be configured to display the DoD logon warning banner either through the SSH configuration or a wrapper program such as TCP_WRAPPERS. The SSH daemon may also be used to provide SFTP service. The warning banner configuration for SSH will apply to SFTP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon is configured for logon warning banners. Procedure: An exact match is required to have a valid warning banner. Check for the following login banner. You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.

## Group: GEN005570

**Group ID:** `V-22490`

### Rule: The system must be configured with a default gateway for IPv6 if the system uses IPv6, unless the system is a router.

**Rule ID:** `SV-46111r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a system has no default gateway defined, the system is at increased risk of man-in-the-middle, monitoring, and Denial of Service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for a default route for IPv6. If the system is a VM host and acts as a router solely for the benefit of its client systems, then this rule is not applicable. # ip -6 route list | grep default If the system uses IPv6, and no results are returned, this is a finding.

## Group: GEN005610

**Group ID:** `V-22491`

### Rule: The system must not have IP forwarding for IPv6 enabled, unless the system is an IPv6 router.

**Rule ID:** `SV-46115r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is configured for IP forwarding and is not a designated router, it could be used to bypass network security by providing a path for communication not filtered by network devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the system is configured for IPv6 forwarding. # grep [01] /proc/sys/net/ipv6/conf/*/forwarding|egrep "default|all" If the /proc/sys/net/ipv6/conf/*/forwarding entries do not exist because of compliance with GEN007720, this is not a finding. If all of the resulting lines do not end with 0, this is a finding.

## Group: GEN005750

**Group ID:** `V-22492`

### Rule: The Network File System (NFS) export configuration file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46118r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give group-ownership of the NFS export configuration file to root or a system group provides the designated group-owner and possible unauthorized users with the potential to change system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the NFS export configuration file. Procedure: # ls -lL /etc/exports If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN005770

**Group ID:** `V-22493`

### Rule: The Network File System (NFS) exports configuration file must not have an extended ACL.

**Rule ID:** `SV-46120r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>File system extended ACLs provide access to files beyond what is allowed by the mode numbers of the files. Excessive permissions on the NFS export configuration file could allow unauthorized modification of the file, which could result in Denial of Service to authorized NFS exports and the creation of additional unauthorized exports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the NFS export configuration file. # ls -lL /etc/exports If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN005810

**Group ID:** `V-22496`

### Rule: All Network File System (NFS) exported system files and system directories must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46122r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give group-ownership of sensitive files or directories to root provides the members of the owning group with the potential to access sensitive information or change system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
List the exports. # cat /etc/exports For each file system displayed, check the ownership. # ls -ldL <exported file system path> If the directory is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN006150

**Group ID:** `V-22497`

### Rule: The /etc/smb.conf file must not have an extended ACL.

**Rule ID:** `SV-46134r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions could endanger the security of the Samba configuration file and, ultimately, the system and network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the Samba configuration file. # ls -lL /etc/samba/smb.conf If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN006210

**Group ID:** `V-22498`

### Rule: The /etc/smbpasswd file must not have an extended ACL.

**Rule ID:** `SV-46138r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the permissions of the "smbpasswd" file are too permissive, it may be maliciously accessed or modified, potentially resulting in the compromise of Samba accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the Samba password files. Procedure: # ls -lL /etc/samba/passdb.tdb /etc/samba/secrets.tdb If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN006225

**Group ID:** `V-22499`

### Rule: Samba must be configured to use an authentication mechanism other than share.

**Rule ID:** `SV-46140r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Samba share authentication does not provide for individual user identification and must not be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the security mode of the Samba configuration. # grep -i security /etc/samba/smb.conf If the security mode is "share", this is a finding.

## Group: GEN006230

**Group ID:** `V-22500`

### Rule: Samba must be configured to use encrypted passwords.

**Rule ID:** `SV-46281r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Samba must be configured to protect authenticators. If Samba passwords are not encrypted for storage, plain-text user passwords may be read by those with access to the Samba password file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the "samba-common" package is not installed, this is not applicable. Check the encryption setting of Samba. # grep -i 'encrypt passwords' /etc/samba/smb.conf If the setting is not present, or not set to 'yes', this is a finding.

## Group: GEN006235

**Group ID:** `V-22501`

### Rule: Samba must be configured to not allow guest access to shares.

**Rule ID:** `SV-46141r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Guest access to shares permits anonymous access and is not permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the access to shares for Samba. # grep -i 'guest ok' /etc/samba/smb.conf If the setting exists and is set to 'yes', this is a finding.

## Group: GEN006270

**Group ID:** `V-22502`

### Rule: The /etc/news/incoming.conf file must not have an extended ACL.

**Rule ID:** `SV-46144r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File system extended ACLs provide access to files beyond what is allowed by the mode numbers of the files. Excessive permissions on the "incoming.conf" file may allow unauthorized modification which could lead to Denial of Service to authorized users or provide access to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/news/incoming.conf If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN006290

**Group ID:** `V-22503`

### Rule: The /etc/news/hosts.nntp.nolimit file must not have an extended ACL.

**Rule ID:** `SV-45894r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File system extended ACLs provide access to files beyond what is allowed by the mode numbers of the files. Excessive permissions on the hosts.nntp.nolimit file may allow unauthorized modification which could lead to Denial of Service to authorized users or provide access to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions for "/etc/news/hosts.nntp.nolimit". # ls -lL /etc/news/hosts.nntp.nolimit If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN006310

**Group ID:** `V-22504`

### Rule: The /etc/news/nnrp.access file must not have an extended ACL.

**Rule ID:** `SV-45897r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File system extended ACLs provide access to files beyond what is allowed by the mode numbers of the files. Excessive permissions on the nnrp.access file may allow unauthorized modification which could lead to Denial of Service to authorized users or provide access to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/news/nnrp.access If the permissions include a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN006330

**Group ID:** `V-22505`

### Rule: The /etc/news/passwd.nntp file must not have an extended ACL.

**Rule ID:** `SV-45899r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Extended ACLs may provide excessive permissions on the /etc/news/passwd.nntp file, which may permit unauthorized access or modification to the NNTP configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/news/passwd.nntp If the mode includes a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN006565

**Group ID:** `V-22506`

### Rule: The system package management tool must be used to verify system software periodically.

**Rule ID:** `SV-45914r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verification using the system package management tool can be used to determine that system software has not been tampered with. This requirement is not applicable to systems not using package management tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the root crontab (crontab -l) and the global crontabs in "/etc/crontab", "/etc/cron.d/*" for the presence of an rpm verification command such as: rpm -qVa | awk '$2!="c" {print $0}' If no such cron job is found, this is a finding. If the result of the cron job indicates packages which do not pass verification exist, this is a finding unless the changes were made due to another STIG entry.

## Group: GEN006570

**Group ID:** `V-22507`

### Rule: The file integrity tool must be configured to verify ACLs.

**Rule ID:** `SV-45915r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>ACLs can provide permissions beyond those permitted through the file mode and must be verified by file integrity tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If using an Advanced Intrusion Detection Environment (AIDE), verify that the configuration contains the "ACL" option for all monitored files and directories. Procedure: Check for the default location /etc/aide/aide.conf or: # find / -name aide.conf # egrep "[+]?acl" <aide.conf file> If the option is not present. This is a finding. If using a different file integrity tool, check the configuration per tool documentation.

## Group: GEN006571

**Group ID:** `V-22508`

### Rule: The file integrity tool must be configured to verify extended attributes.

**Rule ID:** `SV-45918r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Extended attributes in file systems are used to contain arbitrary data and file metadata with security implications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If using an Advanced Intrusion Detection Environment (AIDE), verify the configuration contains the "xattrs" option for all monitored files and directories. Procedure: Check for the default location /etc/aide/aide.conf or: # find / -name aide.conf # egrep "[+]?xattrs" <aide.conf file> If the option is not present. This is a finding. If using a different file integrity tool, check the configuration per tool documentation.

## Group: GEN006575

**Group ID:** `V-22509`

### Rule: The file integrity tool must use FIPS 140-2 approved cryptographic hashes for validating file contents.

**Rule ID:** `SV-45928r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>File integrity tools often use cryptographic hashes for verifying that file contents have not been altered. These hashes must be FIPS 140-2 approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If using an Advanced Intrusion Detection Environment (AIDE), verify the configuration contains the "sha256" or "sha512" options for all monitored files and directories. Procedure: Check for the default location /etc/aide/aide.conf or: # find / -name aide.conf # egrep "[+]?(sha256|sha512)" <aide.conf file> If the option is not present. This is a finding. If one of these options is not present. This is a finding. If using a different file integrity tool, check the configuration per tool documentation.

## Group: GEN007020

**Group ID:** `V-22511`

### Rule: The Stream Control Transmission Protocol (SCTP) must be disabled unless required.

**Rule ID:** `SV-45968r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Stream Control Transmission Protocol (SCTP) is an Internet Engineering Task Force (IETF)-standardized transport layer protocol. This protocol is not yet widely used. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SCTP protocol handler is prevented from dynamic loading. # grep 'install sctp' /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep ‘/bin/true’ If no result is returned, this is a finding.

## Group: GEN007080

**Group ID:** `V-22514`

### Rule: The Datagram Congestion Control Protocol (DCCP) must be disabled unless required.

**Rule ID:** `SV-45970r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DCCP is a proposed transport layer protocol. This protocol is not yet widely used. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DCCP protocol handler is prevented from dynamic loading. # grep 'install dccp' /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep ‘/bin/true’ If no result is returned, this is a finding. # grep 'install dccp_ipv4' /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep /bin/true’ If no result is returned, this is a finding. # grep 'install dccp_ipv6' /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep ‘bin/true’ If no result is returned, this is a finding.

## Group: GEN007140

**Group ID:** `V-22517`

### Rule: The Lightweight User Datagram Protocol (UDP-Lite) must be disabled unless required.

**Rule ID:** `SV-46099r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UDP-Lite is a proposed transport layer protocol. This protocol is not yet widely used. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If there is no UDP-Lite protocol handler available for the system, this is not applicable. Determine if the UDP-Lite protocol handler is prevented from dynamic loading. If it is not, this is a finding.

## Group: GEN007200

**Group ID:** `V-22520`

### Rule: The Internetwork Packet Exchange (IPX) protocol must be disabled or not installed.

**Rule ID:** `SV-46101r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IPX protocol is a network-layer protocol no longer in common use. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check that the IPX protocol handler is prevented from dynamic loading. # grep 'install ipx' /etc/modprobe.conf /etc/modprbe.conf.local /etc/modprobe.d/* | grep ‘/bin/true’ If no result is returned, this is a finding.

## Group: GEN007260

**Group ID:** `V-22524`

### Rule: The AppleTalk protocol must be disabled or not installed.

**Rule ID:** `SV-45973r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The AppleTalk suite of protocols is no longer in common use. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AppleTalk protocol handler is prevented from dynamic loading. # grep 'install appletalk' /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep ‘/bin/true’ If no result is returned, this is a finding.

## Group: GEN007480

**Group ID:** `V-22530`

### Rule: The Reliable Datagram Sockets (RDS) protocol must be disabled or not installed unless required.

**Rule ID:** `SV-45975r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The RDS protocol is a relatively new protocol developed by Oracle for communication between the nodes of a cluster. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if RDS is required by application software running on the system. If so, this is not applicable. Verify the RDS protocol handler is prevented from dynamic loading. # grep 'install rds' /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep ‘/bin/true’ If no result is returned, this is a finding.

## Group: GEN007540

**Group ID:** `V-22533`

### Rule: The Transparent Inter-Process Communication (TIPC) protocol must be disabled or uninstalled.

**Rule ID:** `SV-45977r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The TIPC protocol is a relatively new cluster communications protocol developed by Ericsson. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the TIPC protocol handler is prevented from dynamic loading. # grep 'install tipc' /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep ‘/bin/true’ If no result is returned, this is a finding.

## Group: GEN007660

**Group ID:** `V-22539`

### Rule: The Bluetooth protocol handler must be disabled or not installed.

**Rule ID:** `SV-45979r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Bluetooth is a Personal Area Network (PAN) technology. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the kernel to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Bluetooth protocol handler is prevented from dynamic loading. # grep 'install bluetooth' /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep ‘/bin/true’ If no result is returned, this is a finding.

## Group: GEN007700

**Group ID:** `V-22541`

### Rule: The IPv6 protocol handler must not be bound to the network stack unless needed.

**Rule ID:** `SV-45980r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IPv6 is the next version of the Internet protocol. Binding this protocol to the network stack increases the attack surface of the host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Use the ifconfig command to determine if any network interface has an IPv6 address bound to it: # /sbin/ifconfig | grep inet6 If any lines are returned that indicate IPv6 is active and the system does not need IPv6, this is a finding.

## Group: GEN007720

**Group ID:** `V-22542`

### Rule: The IPv6 protocol handler must be prevented from dynamic loading unless needed.

**Rule ID:** `SV-45981r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IPv6 is the next generation of the Internet protocol. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If this system uses IPv6, this is not applicable. Verify the IPv6 protocol handler is prevented from dynamic loading. # /sbin/ifconfig | grep –i inet6 This command should not return any output. If any lines are returned that display IPv6 addresses associated with the TCP/IP stack, this is a finding.

## Group: GEN007780

**Group ID:** `V-22545`

### Rule: The system must not have 6to4 enabled.

**Rule ID:** `SV-45982r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>6to4 is an IPv6 transition mechanism involving tunneling IPv6 packets encapsulated in IPv4 packets on an ad-hoc basis. This is not a preferred transition strategy and increases the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for any active 6to4 tunnels without specific remote addresses. # ip tun list | grep "remote any" | grep "ipv6/ip" If any results are returned the "tunnel" is the first field. If any results are returned, this is a finding.

## Group: GEN007800

**Group ID:** `V-22546`

### Rule: The system must not have Teredo enabled.

**Rule ID:** `SV-45983r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Teredo is an IPv6 transition mechanism involving tunneling IPv6 packets encapsulated in IPv4 packets. Unauthorized tunneling may circumvent network security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Miredo service is not running. # ps ax | grep miredo | grep -v grep If the miredo process is running, this is a finding.

## Group: GEN007820

**Group ID:** `V-22547`

### Rule: The system must not have IP tunnels configured.

**Rule ID:** `SV-45986r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP tunneling mechanisms can be used to bypass network filtering.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for any IP tunnels. # ip tun list # ip -6 tun list If any tunnels are listed, this is a finding.

## Group: GEN007840

**Group ID:** `V-22548`

### Rule: The DHCP client must be disabled if not needed.

**Rule ID:** `SV-45987r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DHCP allows for the unauthenticated configuration of network parameters on the system by exchanging information with a DHCP server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify no interface is configured to use DHCP. # grep -i bootproto=dhcp /etc/sysconfig/network/ifcfg-* If any configuration is found, this is a finding.

## Group: GEN007850

**Group ID:** `V-22549`

### Rule: The DHCP client must not send dynamic DNS updates.

**Rule ID:** `SV-45988r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Dynamic DNS updates transmit unencrypted information about a system including its name and address and should not be used unless needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the "dhcp-client" package is not installed, this is not applicable. Verify the DHCP client is configured to not send dynamic DNS updates. Procedure: # rpm –q dhcp-client If DHCP client is found then issue following command to determine if the DHCP client sends dynamic DNS updates: # grep do-forward-updates /etc/dhclient.conf If the DHCP client is installed and the configuration file is not present, or contains do-forward-updates = “true”, then this is a finding

## Group: GEN007860

**Group ID:** `V-22550`

### Rule: The system must ignore IPv6 ICMP redirect messages.

**Rule ID:** `SV-45990r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is configured to ignore IPv6 ICMP redirect messages. # cat /proc/sys/net/ipv6/conf/all/accept_redirects If the /proc/sys/net/ipv6/conf/all/accept_redirects entry does not exist because of compliance with GEN007720, this is not a finding. If the returned value is not "0", this is a finding.

## Group: GEN007900

**Group ID:** `V-22552`

### Rule: The system must use an appropriate reverse-path filter for IPv6 network traffic, if the system uses IPv6.

**Rule ID:** `SV-46104r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reverse-path filtering provides protection against spoofed source addresses by causing the system to discard packets with source addresses for which the system has no route or if the route does not point towards the interface on which the packet arrived. Depending on the role of the system, reverse-path filtering may cause legitimate traffic to be discarded and, therefore, should be used with a more permissive mode or filter, or not at all. Whenever possible, reverse-path filtering should be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Reverse Path filtering for IPv6 is not implemented in SLES.

## Group: GEN007920

**Group ID:** `V-22553`

### Rule: The system must not forward IPv6 source-routed packets.

**Rule ID:** `SV-45992r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv6 forwarding is enabled and the system is functioning as a router. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system is configured to forward IPv6 source-routed packets. Procedure: # sysctl net.ipv6.conf.all.forwarding # sysctl net.ipv6.conf.default.forwarding If any value of the entries is not = "0", this is a finding.

## Group: GEN007940

**Group ID:** `V-22554`

### Rule: The system must not accept source-routed IPv6 packets.

**Rule ID:** `SV-46106r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the handling of source-routed traffic destined to the system itself, not to traffic forwarded by the system to another, such as when IPv6 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The ability to control the acceptance of source-routed packets is not inherent to IPv6.

## Group: GEN007980

**Group ID:** `V-22555`

### Rule: If the system is using LDAP for authentication or account information, the system must use a TLS connection using FIPS 140-2 approved cryptographic algorithms.

**Rule ID:** `SV-45996r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. Communication between an LDAP server and a host using LDAP requires protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the system is using NSS LDAP. # grep -v '^#' /etc/nsswitch.conf | grep ldap If no lines are returned, this vulnerability is not applicable. Check if NSS LDAP is using TLS. # grep '^ssl start_tls' /etc/ldap.conf If no lines are returned, this is a finding. Check if NSS LDAP TLS is using only FIPS 140-2 approved cryptographic algorithms. # grep '^tls_ciphers' /etc/ldap.conf If the line is not present, or contains ciphers not approved by FIPS 140-2, this is a finding.

## Group: GEN008000

**Group ID:** `V-22556`

### Rule: If the system is using LDAP for authentication or account information, certificates used to authenticate to the LDAP server must be provided from DoD PKI or a DoD-approved external PKI.

**Rule ID:** `SV-45998r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. Communication between an LDAP server and a host using LDAP requires authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the source of the LDAP certificates Check if the system is using NSS LDAP. # grep -v '^#' /etc/nsswitch.conf | grep ldap If no lines are returned, this vulnerability is not applicable. Verify with the SA that the system is connected to the GIG. If the system part of a stand alone network which is not connected to the GIG this vulnerability is not applicable. Verify a certificate is used for client authentication to the server. # grep -i '^tls_cert' /etc/ldap.conf If no line is found, this is a finding. List the certificate issuer. # openssl x509 -text -in <cert> If the certificate is not issued by DoD PKI or a DoD-approved external PKI, this is a finding.

## Group: GEN008020

**Group ID:** `V-22557`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS connection must require the server provide a certificate with a valid trust path to a trusted CA.

**Rule ID:** `SV-46000r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The NSS LDAP service provides user mappings which are a vital component of system security. Communication between an LDAP server and a host using LDAP for NSS require authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the system is using NSS LDAP. # grep -v '^#' /etc/nsswitch.conf | grep ldap If no lines are returned, this vulnerability is not applicable. Verify a server certificate is required and verified by the NSS LDAP configuration. # grep -i '^tls_checkpeer' /etc/ldap.conf If no line is returned, or the value is not "yes", this is a finding.

## Group: GEN008040

**Group ID:** `V-22558`

### Rule: If the system is using LDAP for authentication or account information, the system must verify the LDAP servers certificate has not been revoked.

**Rule ID:** `SV-46285r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. Communication between an LDAP server and a host using LDAP requires authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the system is using NSS LDAP. # grep -v '^#' /etc/nsswitch.conf | grep ldap If no lines are returned, this vulnerability is not applicable. Verify the NSS LDAP client is configured to check certificates against a certificate revocation list. # grep -i '^tls_crlcheck' /etc/ldap.conf If the setting does not exist, or the value is not "all", this is a finding.

## Group: GEN008060

**Group ID:** `V-22559`

### Rule: If the system is using LDAP for authentication or account information the /etc/ldap.conf (or equivalent) file must have mode 0644 or less permissive.

**Rule ID:** `SV-46005r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/ldap.conf If the mode of the file is more permissive than 0644, this is a finding.

## Group: GEN008080

**Group ID:** `V-22560`

### Rule: If the system is using LDAP for authentication or account information, the /etc/ldap.conf (or equivalent) file must be owned by root.

**Rule ID:** `SV-46006r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the file. # ls -lL /etc/ldap.conf If the file is not owned by root, this is a finding.

## Group: GEN008100

**Group ID:** `V-22561`

### Rule: If the system is using LDAP for authentication or account information, the /etc/ldap.conf (or equivalent) file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46007r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the file. Procedure: # ls -lL /etc/ldap.conf If the file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN008120

**Group ID:** `V-22562`

### Rule: If the system is using LDAP for authentication or account information, the /etc/ldap.conf (or equivalent) file must not have an extended ACL.

**Rule ID:** `SV-46018r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lL /etc/ldap.conf If the mode includes a '+', the file has an extended ACL. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN008140

**Group ID:** `V-22563`

### Rule: If the system is using LDAP for authentication or account information, the TLS certificate authority file and/or directory (as appropriate) must be owned by root.

**Rule ID:** `SV-46092r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the certificate authority file and/or directory. # grep -i '^tls_cacert' /etc/ldap.conf For each file or directory returned, check the ownership. # ls -lLd <certpath> If the owner of any file or directory is not root, this is a finding.

## Group: GEN008160

**Group ID:** `V-22564`

### Rule: If the system is using LDAP for authentication or account information, the TLS certificate authority file and/or directory (as appropriate) must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46030r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the certificate authority file and/or directory. # grep -i '^tls_cacert' /etc/ldap.conf For each file or directory returned, check the group ownership. # ls -lLd <certpath> If the group-owner of any file or directory is not root, bin, sys, or system, this is a finding.

## Group: GEN008180

**Group ID:** `V-22565`

### Rule: If the system is using LDAP for authentication or account information, the TLS certificate authority file and/or directory (as appropriate) must have mode 0644 (0755 for directories) or less permissive.

**Rule ID:** `SV-46093r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the certificate authority file and/or directory. Procedure: # grep -i '^tls_cacert' /etc/ldap.conf For each file or directory returned, check the permissions. Procedure: # ls -lLd <certpath> If the mode of the file is more permissive than 0644 (or 0755 for directories), this is a finding.

## Group: GEN008200

**Group ID:** `V-22566`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS certificate authority file and/or directory (as appropriate) must not have an extended ACL.

**Rule ID:** `SV-46095r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the certificate authority file and/or directory. # grep -i '^tls_cacert' /etc/ldap.conf For each file or directory returned, check the permissions. # ls -lLd <certpath> If the mode of the file or directory contains a '+', an extended ACL is present. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN008220

**Group ID:** `V-22567`

### Rule: For systems using NSS LDAP, the TLS certificate file must be owned by root.

**Rule ID:** `SV-46034r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The NSS LDAP service provides user mappings which are a vital component of system security. Its configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the certificate file. # grep -i '^tls_cert' /etc/ldap.conf Check the ownership. # ls -lL <certpath> If the owner of the file is not root, this is a finding.

## Group: GEN008240

**Group ID:** `V-22568`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS certificate file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46035r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the certificate file. Procedure: # grep -i '^tls_cert' /etc/ldap.conf Check the group ownership. Procedure: # ls -lL <certpath> If the group owner of the file is not root, bin, sys, or system, this is a finding.

## Group: GEN008260

**Group ID:** `V-22569`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS certificate file must have mode 0644 or less permissive.

**Rule ID:** `SV-46036r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Identify the LDAP TLS Certificate file: # cat <ldap_config_file> | grep -i “^tls” TLSCACertificatePath <path> TLSCACertificateFile <filename> TLSCertificateFile <filename> For each TLSCACertificateFile and TLSCertificateFile defined in the configuration file, verify the file permissions: # ls -la <tls_certificate_file> If the mode of the file is more permissive than 0644, this is a finding.

## Group: GEN008280

**Group ID:** `V-22570`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS certificate file must not have an extended ACL.

**Rule ID:** `SV-46037r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the certificate file. # grep -i '^tls_cert' /etc/ldap.conf Check the permissions. # ls -lL <certpath> If the mode of the file contains a '+', an extended ACL is present. This is a finding.

## Group: GEN008300

**Group ID:** `V-22571`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS key file must be owned by root.

**Rule ID:** `SV-46038r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the key file. # grep -i '^tls_key' /etc/ldap.conf Check the ownership. # ls -lL <keypath> If the owner of the file is not root, this is a finding.

## Group: GEN008320

**Group ID:** `V-22572`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS key file must be group-owned by root, bin, or sys.

**Rule ID:** `SV-46039r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the key file. # grep -i '^tls_key' /etc/ldap.conf Check the group ownership. # ls -lL <keypath> If the group wner of the file is not root, this is a finding.

## Group: GEN008340

**Group ID:** `V-22573`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS key file must have mode 0600 or less permissive.

**Rule ID:** `SV-46041r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification. Note: Depending on the particular implementation, group and other read permission may be necessary for unprivileged users to successfully resolve account information using LDAP. This will still be a finding, as these permissions provide users with access to system authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the key file. # grep -i '^tls_key' /etc/ldap.conf Check the permissions. # ls -lL <keypath> If the mode of the file is more permissive than 0600, this is a finding.

## Group: GEN008360

**Group ID:** `V-22574`

### Rule: If the system is using LDAP for authentication or account information, the LDAP TLS key file must not have an extended ACL.

**Rule ID:** `SV-46042r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP can be used to provide user authentication and account information, which are vital to system security. The LDAP client configuration must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the key file. # grep -i '^tls_key' /etc/ldap.conf Check the permissions. # ls -lL <keypath> If the mode the file contains a '+', an extended ACL is present. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN008440

**Group ID:** `V-22577`

### Rule: Automated file system mounting tools must not be enabled unless needed.

**Rule ID:** `SV-46045r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Automated file system mounting tools may provide unprivileged users with the ability to access local media and network shares. If this access is not necessary for the system’s operation, it must be disabled to reduce the risk of unauthorized access to these resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check if the autofs service is running. # rcautofs status OR # service autofs status If the service is running, this is a finding.

## Group: GEN008520

**Group ID:** `V-22582`

### Rule: The system must employ a local firewall.

**Rule ID:** `SV-46049r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A local firewall protects the system from exposing unnecessary or undocumented network services to the local enclave. If a system within the enclave is compromised, firewall protection on an individual system continues to protect it from attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system is using a local firewall. # rcSuSEfirewall2 status If the service is not "running”, this is a finding.

## Group: GEN008540

**Group ID:** `V-22583`

### Rule: The systems local firewall must implement a deny-all, allow-by-exception policy.

**Rule ID:** `SV-46060r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A local firewall protects the system from exposing unnecessary or undocumented network services to the local enclave. If a system within the enclave is compromised, firewall protection on an individual system continues to protect it from attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the firewall rules for a default deny rule. # iptables --list If there is no default deny rule, this is a finding.

## Group: GEN008740

**Group ID:** `V-22585`

### Rule: The systems boot loader configuration file(s) must not have extended ACLs.

**Rule ID:** `SV-46076r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File system extended ACLs provide access to files beyond what is allowed by the mode numbers of the files. If extended ACLs are present on the system's boot loader configuration file(s), these files may be vulnerable to unauthorized access or modification, which could compromise the system's boot process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lLd /etc/zipl.conf If the mode the file or directory contains a '+', an extended ACL is present. This is a finding.

## Group: GEN008760

**Group ID:** `V-22586`

### Rule: The systems boot loader configuration files must be owned by root.

**Rule ID:** `SV-46077r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system's boot loader configuration files are critical to the integrity of the system and must be protected. Unauthorized modification of these files resulting from improper ownership could compromise the system's boot loader configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the file. # ls -lLd /etc/zipl.conf If the owner of the file is not root, this is a finding.

## Group: GEN008780

**Group ID:** `V-22587`

### Rule: The systems boot loader configuration file(s) must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46078r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system's boot loader configuration files are critical to the integrity of the system and must be protected. Unauthorized modifications resulting from improper group ownership may compromise the boot loader configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the file. # ls -lLd /etc/zipl.conf If the group-owner of the file is not root, bin, sys, or system this is a finding.

## Group: GEN008800

**Group ID:** `V-22588`

### Rule: The system package management tool must cryptographically verify the authenticity of software packages during installation.

**Rule ID:** `SV-46080r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To prevent the installation of software from unauthorized sources, the system package management tool must use cryptographic algorithms to verify the packages are authentic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that the suse-build-key package is installed and the build-key file exists: # rpm –ql suse-build-key # ls –l /usr/lib/rpm/gnupg/suse-build-key.gpg Ensure that the value of the CHECK_SIGNATURES variable is set to “yes” # grep –i check_signature /etc/sysconfig/security If the /usr/lib/rpm/gnupg/suse-build-key.gpg file does not exist or CHECK_SIGNATURES is not set to “yes”, this is a finding.

## Group: GEN008820

**Group ID:** `V-22589`

### Rule: The system package management tool must not automatically obtain updates.

**Rule ID:** `SV-46084r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>System package management tools can obtain a list of updates and patches from a package repository and make this information available to the SA for review and action. Using a package repository outside of the organization's control presents a risk of malicious packages being introduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of a cron job called opensuse.org-online_update # find /etc/cron* -name opensuse* If a symlink or executable script is found, this is a finding.

## Group: GEN000000-LNX00450

**Group ID:** `V-22595`

### Rule: The /etc/security/access.conf file must not have an extended ACL.

**Rule ID:** `SV-44757r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the access permissions are more permissive than 0640, system security could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lLd /etc/security/access.conf If the permissions of the file or directory contains a '+', an extended ACL is present. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN000000-LNX00530

**Group ID:** `V-22596`

### Rule: The /etc/sysctl.conf file must not have an extended ACL.

**Rule ID:** `SV-44758r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sysctl.conf file specifies the values for kernel parameters to be set on boot. These settings can affect the system's security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the file. # ls -lLd /etc/sysctl.conf If the permissions of the file or directory contains a '+', an extended ACL is present. If the file has an extended ACL and it has not been documented with the IAO, this is a finding.

## Group: GEN005590

**Group ID:** `V-22665`

### Rule: The system must not be running any routing protocol daemons, unless the system is a router.

**Rule ID:** `SV-46113r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for any running routing protocol daemons. If the system is a VM host and acts as a router solely for the benefits of its client systems, then this rule is not applicable. # ps ax | egrep '(ospf|route|bgp|zebra|quagga)' If any routing protocol daemons are listed, this is a finding.

## Group: GEN002690

**Group ID:** `V-22702`

### Rule: System audit logs must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-45209r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sensitive system and user information could provide a malicious user with enough information to penetrate further into the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the audit logs. Procedure: # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; ls -l ${audit_log_file%/*}; else printf "audit log file(s) not found\n"; fi) If any audit log file is not group-owned by root, bin, sys, or system, this is a finding.

## Group: GEN000410

**Group ID:** `V-23732`

### Rule: The FTPS/FTP service on the system must be configured with the Department of Defense (DoD) login banner.

**Rule ID:** `SV-44829r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources. Note: SFTP and FTPS are encrypted alternatives to FTP to be used in place of FTP. SFTP is implemented by the SSH service and uses its banner configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
FTP to the system. # ftp localhost Check for either of the following login banners based on the character limitations imposed by the system. An exact match is required. If one of these banners is not displayed, this is a finding. If the system does not run the FTP service, this is not applicable. DoD Login Banners: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. OR I've read & consent to terms in IS user agreem't.

## Group: GEN003621

**Group ID:** `V-23736`

### Rule: The system must use a separate file system for /var.

**Rule ID:** `SV-45743r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the /var path is a separate filesystem. # grep "/var " /etc/fstab If no result is returned, /var is not on a separate filesystem this is a finding

## Group: GEN003623

**Group ID:** `V-23738`

### Rule: The system must use a separate file system for the system audit data path.

**Rule ID:** `SV-45745r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the /var/log/audit path is a separate filesystem. # grep "/var/log/audit " /etc/fstab If no result is returned, /var/log/audit is not on a separate filesystem this is a finding.

## Group: GEN003624

**Group ID:** `V-23739`

### Rule: The system must use a separate file system for /tmp (or equivalent).

**Rule ID:** `SV-45752r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the /tmp path is a separate filesystem. # grep "/tmp " /etc/fstab If no result is returned, /tmp is not on a separate filesystem this is a finding.

## Group: GEN003601

**Group ID:** `V-23741`

### Rule: TCP backlog queue sizes must be set appropriately.

**Rule ID:** `SV-45720r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To provide some mitigation to TCP Denial of Service attacks, the TCP backlog queue sizes must be set to at least 1280 or in accordance with product-specific guidelines.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# cat /proc/sys/net/ipv4/tcp_max_syn_backlog If the result is not 1280 or greater, this is a finding.

## Group: GEN004710

**Group ID:** `V-23952`

### Rule: Mail relaying must be restricted.

**Rule ID:** `SV-45875r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unrestricted mail relaying is permitted, unauthorized senders could use this host as a mail relay for the purpose of sending SPAM or other unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the system uses sendmail, locate the sendmail.cf file. Procedure: # find / -name sendmail.cf Determine if sendmail only binds to loopback addresses by examining the “DaemonPortOptions” configuration options. Procedure: # grep -i “O DaemonPortOptions” </path/to/sendmail.cf> If there are uncommented DaemonPortOptions lines, and all such lines specify system loopback addresses, this is not a finding. Otherwise, determine if sendmail is configured to allow open relay operation. Procedure: # find / -name sendmail.mc # grep -i promiscuous_relay </path/to/sendmail.mc> If the promiscuous relay feature is enabled, this is a finding. If the system uses Postfix, locate the main.cf file. Procedure: # find / -name main.cf Determine if Postfix only binds to loopback addresses by examining the “inet_interfaces” line. Procedure: # grep inet_interfaces </path/to/main.cf> If “inet_interfaces” is set to “loopback-only” or contains only loopback addresses such as 127.0.0.1 and [::1], Postfix is not listening on external network interfaces, and this is not a finding. Otherwise, determine if Postfix is configured to restrict clients permitted to relay mail by examining the “smtpd_client_restrictions” line. Procedure: # grep smtpd_client_restrictions </path/to/main.cf> If the “smtpd_client_restrictions” line is missing, or does not contain “reject”, this is a finding. If the line contains “permit” before “reject”, this is a finding. If the system is using other SMTP software, consult the software’s documentation for procedures to verify mail relaying is restricted.

## Group: GEN007960

**Group ID:** `V-23953`

### Rule: The ldd command must be disabled unless it protects against the execution of untrusted files.

**Rule ID:** `SV-46283r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The 'ldd' command provides a list of dependent libraries needed by a given binary, which is useful for troubleshooting software. Instead of parsing the binary file, some 'ldd' implementations invoke the program with a special environment variable set, which causes the system dynamic linker to display the list of libraries. Specially crafted binaries can specify an alternate dynamic linker which may cause a program to be executed instead of examined. If the program is from an untrusted source, such as in a user home directory, or a file suspected of involvement in a system compromise, unauthorized software may be executed with the rights of the user running 'ldd'. Some 'ldd' implementations include protections that prevent the execution of untrusted files. If such protections exist, this requirement is not applicable. An acceptable method of disabling 'ldd' is changing its mode to 0000. The SA may conduct troubleshooting by temporarily changing the mode to allow execution and running the 'ldd' command as an unprivileged user upon trusted system binaries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for the 'ldd' executable. Procedure: # ls -lL /usr/bin/ldd If the file exists and has any execute permissions, this is a finding.

## Group: GEN007950

**Group ID:** `V-23972`

### Rule: The system must not respond to ICMPv6 echo requests sent to a broadcast address.

**Rule ID:** `SV-45993r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast ICMP echo requests facilitates network mapping and provides a vector for amplification attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for an ip6tables rule that drops inbound IPv6 ICMP ECHO_REQUESTs sent to the all-hosts multicast address. Procedure: # less /etc/sysconfig/scripts/SuSEfirewall2-custom Check for a rule in, or referenced by, the INPUT chain such as: ip6tables -A INPUT -p icmpv6 -d ff02::1 --icmpv6-type 128 -j DROP If such a rule does not exist, this is a finding.

## Group: GEN002870

**Group ID:** `V-24357`

### Rule: The system must be configured to send audit records to a remote audit server.

**Rule ID:** `SV-45564r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Audit records contain evidence that can be used in the investigation of compromised systems. To prevent this evidence from compromise, it must be sent to a separate system continuously. Methods for sending audit records include, but are not limited to, system audit tools used to send logs directly to another host or through the system's syslog service to another host. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is configured to forward all audit records to a remote server. If the system is not configured to provide this function, this is a finding. Procedure: Ensure the audit option for the kernel is enabled. # cat /proc/cmdline | tr ' ' '\n' | grep -i audit If the kernel does not have the "audit=1" option specified, this is a finding. Ensure the kernel auditing is active. # /sbin/auditctl -s | tr ' ' '\n' | egrep 'enabled|pid' When auditing is active, the “enabled” value is set to 1 and the “pid” value will be greater than 0. If the "enabled" setting is either missing or not set to "1", this is a finding. If the “pid” setting is 0, the audit daemon is not running and this is also a finding. Ensure the syslog plugin is active for the audit dispatch daemon. # grep "active" /etc/audisp/plugins.d/syslog.conf | grep -v "^#" If the "active" setting is either missing or not set to "yes", this is a finding. Ensure all audit records are fowarded to a remote server. # grep "\*.\*" /etc/syslog.conf |grep "@" | grep -v "^#" (for syslog) or: # grep "\*.\*" /etc/rsyslog.conf | grep "@" | grep -v "^#" (for rsyslog) If neither of these lines exist, it is a finding.

## Group: GEN008050

**Group ID:** `V-24384`

### Rule: If the system is using LDAP for authentication or account information, the /etc/ldap.conf file (or equivalent) must not contain passwords.

**Rule ID:** `SV-45865r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The authentication of automated LDAP connections between systems must not use passwords since more secure methods are available, such as PKI and Kerberos. Additionally, the storage of unencrypted passwords on the system is not permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check for the "bindpw" option being used in the "/etc/ldap.conf" file. # grep bindpw /etc/ldap.conf If an uncommented "bindpw" option is returned then a cleartext password is in the file, this is a finding.

## Group: GEN003850

**Group ID:** `V-24386`

### Rule: The telnet daemon must not be running.

**Rule ID:** `SV-45809r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The telnet daemon provides a typically unencrypted remote access service which does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to log on using this service, the privileged user password could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations>GEN003850</Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl>If an enabled telnet daemon is configured to only allow encrypted sessions, such as with Kerberos or the use of encrypted network tunnels, the risk of exposing sensitive information is mitigated, and this is not a finding.</MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
# chkconfig --list | grep telnet If an entry is returned and any run level is “on” telnet is running. If the telnet daemon is running, this is a finding.

## Group: GEN000140-2

**Group ID:** `V-27250`

### Rule: A file integrity baseline including cryptographic hashes must be created.

**Rule ID:** `SV-44763r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A file integrity baseline is a collection of file metadata which is to evaluate the integrity of the system. A minimal baseline must contain metadata for all device files, setuid files, setgid files, system libraries, system binaries, and system configuration files. The minimal metadata must consist of the mode, owner, group owner, and modification times. For regular files, metadata must also include file size and a cryptographic hash of the file’s contents. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify a system integrity baseline exists. The Advanced Intrusion Detection Environment (AIDE) is included in the distribution of SLES. Other host intrusion detection system (HIDS) software is available but must be checked manually. Procedure: # grep DB /etc/aide.conf If /etc/aide.conf does not exist AIDE has not been installed. Unless another HIDS is used on the system, this is a finding. Examine the response for "database". This indicates the location of the system integrity baseline database used as input to a comparison. # ls -la <DBDIR> If no "database" file as defined in /etc/aide.conf exists, a system integrity baseline has not been created.This is a finding. Examine /etc/aide.conf to ensure some form of cryptographic hash (ie. md5,rmd160,sha256) are used for files. In the default /etc/aide.conf the "NORMAL" or "LSPP" rules which are used for virtually all files DO include some form of cryptographic hash. If the site has defined rules to replace the functionality provided by the default "NORMAL" and "LSPP" rules but DOES NOT include cryptographic hashes, this is a finding. Otherwise, if any element used to define the "NORMAL" and "LSPP" rules has been modified resulting in cryptographic hashes not being used, this is a finding. If any other modification to the default /etc/aide.conf file have been made resulting in rules which do not include cryptographic hashes on appropriate files, this is a finding.

## Group: GEN000140-3

**Group ID:** `V-27251`

### Rule: A file integrity baseline including cryptographic hashes must be maintained.



**Rule ID:** `SV-44764r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A file integrity baseline is a collection of file metadata which is to evaluate the integrity of the system. A minimal baseline must contain metadata for all device files, setuid files, setgid files, system libraries, system binaries, and system configuration files. The minimal metadata must consist of the mode, owner, group owner, and modification times. For regular files, metadata must also include file size and a cryptographic hash of the file’s contents. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify a system integrity baseline is maintained. The baseline has been updated to be consistent with the latest approved system configuration changes. The Advanced Intrusion Detection Environment (AIDE) is included in the distribution of SLES. Other host intrusion detection system (HIDS) software is available but must be checked manually. Procedure: # grep DB /etc/aide.conf If /etc/aide.conf does not exist AIDE has not been installed. Unless another HIDS is used on the system, this is a finding. Examine the response for "database". This indicates the location of the system integrity baseline database used as input to a comparison. # ls -la <DB> If no "database" file as defined in /etc/aide.conf exists, a system integrity baseline has not been created. This is a finding. Ask the SA when the last approved system configuration changes occurred. If the modification date of the AIDE database is prior to the last approved configuration change, this is a finding.

## Group: GEN000290-2

**Group ID:** `V-27275`

### Rule: The system must not have the unnecessary news account.

**Rule ID:** `SV-44796r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts that provide no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for the unnecessary "news" accounts. Procedure: # rpm -q inn If the "inn" is installed the "news" user is necessary and this is not a finding. # grep ^news /etc/passwd If this account exists and "inn" is not installed, this is a finding.

## Group: GEN000290-3

**Group ID:** `V-27276`

### Rule: The system must not have the unnecessary gopher account.

**Rule ID:** `SV-44800r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts that provide no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for the unnecessary "gopher" accounts. Procedure: # grep ^gopher /etc/passwd If this account exists, it is a finding.

## Group: GEN000290-4

**Group ID:** `V-27279`

### Rule: The system must not have the unnecessary ftp account.

**Rule ID:** `SV-44802r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts that provide no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for the unnecessary "ftp" accounts. Procedure: # rpm -q vsftp If the "vsftp" ftp server is installed the "ftp" user is necessary and this is not a finding. # grep ^ftp /etc/passwd If this account exists and no ftp server is installed which requires it, this is a finding.

## Group: GEN002720-2

**Group ID:** `V-29236`

### Rule: The audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-45286r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls>ECAR-1, ECAR-2, ECAR-3</IAControls>

**Check Text:**
Check that auditd is configured to audit failed file access attempts. There must be an audit rule for each of the access syscalls that logs all failed accesses (-F success=0) or there must both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S open" | grep -e "-F success=0" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S open" | grep -e "-F exit=-EPERM" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S open" | grep -e "-F exit=-EACCES" If an "-S open" audit rule with "-F success" does not exist and no separate rules containing "-F exit=-EPERM" and "-F exit=-EACCES" for "open" exist, then this is a finding.

## Group: GEN002720-3

**Group ID:** `V-29237`

### Rule: The audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-45287r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0) or there must both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S openat" | grep -e "-F success=0" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S openat" | grep -e "-F exit=-EPERM" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S openat" | grep -e "-F exit=-EACCES" If an "-S openat" audit rule with "-F success" does not exist and no separate rules containing "-F exit=-EPERM" and "-F exit=-EACCES" for "openat" exist, then this is a finding.

## Group: GEN002720-4

**Group ID:** `V-29238`

### Rule: The audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-45289r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0) or there must both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S truncate" | grep -e "-F success=0" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S truncate" | grep -e "-F exit=-EPERM" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S truncate" | grep -e "-F exit=-EACCES" If an "-S truncate" audit rule with "-F success" does not exist and no separate rules containing "-F exit=-EPERM" and "-F exit=-EACCES" for "truncate" exist, then this is a finding.

## Group: GEN002720-5

**Group ID:** `V-29239`

### Rule: The audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-45292r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0) or there must both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S ftruncate" | grep -e "-F success=0" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S ftruncate" | grep -e "-F exit=-EPERM" # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S ftruncate" | grep -e "-F exit=-EACCES" If an "-S ftruncate" audit rule with "-F success" does not exist and no separate rules containing "-F exit=-EPERM" and "-F exit=-EACCES" for "ftruncate" exist, then this is a finding.

## Group: GEN002740-2

**Group ID:** `V-29240`

### Rule: The audit system must be configured to audit file deletions.

**Rule ID:** `SV-45300r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system audit configuration to determine if file and directory deletions are audited. # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "rmdir" If no results are returned, or the results do not contain "-S rmdir", this is a finding.

## Group: GEN002760-2

**Group ID:** `V-29241`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-45331r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -i "audit.rules" If no results are returned, or the line does not start with "-w", this is a finding.

## Group: GEN002760-3

**Group ID:** `V-29242`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-45332r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "adjtimex " If the result does not contain "-S adjtimex", this is a finding.

## Group: GEN002760-4

**Group ID:** `V-29243`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-45333r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "settimeofday" If the result does not contain "-S settimeofday", this is a finding.

## Group: GEN002760-6

**Group ID:** `V-29245`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-45336r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "clock_settime" If the result does not contain "-S clock_settime", this is a finding.

## Group: GEN002760-7

**Group ID:** `V-29246`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-45337r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "sethostname" If the result does not contain "-S sethostname", this is a finding.

## Group: GEN002760-8

**Group ID:** `V-29247`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-45338r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " setdomainname " If the result does not contain "-S setdomainname ", this is a finding.

## Group: GEN002760-9

**Group ID:** `V-29248`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-45339r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "sched_setparam" If the result does not contain "-S sched_setparam", this is a finding.

## Group: GEN002760-10

**Group ID:** `V-29249`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-45328r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "sched_setscheduler" If the result does not contain "-S sched_setscheduler", this is a finding.

## Group: GEN002820-2

**Group ID:** `V-29250`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45345r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " fchmod " If "-S fchmod" is not in the result, this is a finding

## Group: GEN002820-3

**Group ID:** `V-29251`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45401r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " fchmodat " If "-S fchmodat" is not in the result, this is a finding.

## Group: GEN002820-4

**Group ID:** `V-29252`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45407r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " chown " If "-S chown" is not in the result, this is a finding. Additionally, the following rule is required in systems supporting the 32-bit syscall table (such as i686 and x86_64): # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " chown32 " If "-S chown32" is not in the result, this is a finding.

## Group: GEN002820-5

**Group ID:** `V-29253`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45409r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " fchown " If "-S fchown" is not in the result, this is a finding. Additionally, the following rule is required in systems supporting the 32-bit syscall table (such as i686 and x86_64): # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " fchown32 " If "-S fchown32" is not in the result, this is a finding.

## Group: GEN002820-6

**Group ID:** `V-29255`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45421r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " fchownat " If "-S fchownat" is not in the result, this is a finding.

## Group: GEN002820-7

**Group ID:** `V-29257`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45426r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " lchown " If "-S lchown" is not in the result, this is a finding. Additionally, the following rule is required in systems supporting the 32-bit syscall table (such as i686 and x86_64): # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " lchown32 " If "-S lchown32" is not in the result, this is a finding.

## Group: GEN002820-8

**Group ID:** `V-29259`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45433r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " setxattr " If "-S setxattr" is not in the result, this is a finding.

## Group: GEN002820-9

**Group ID:** `V-29261`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45442r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " lsetxattr " If "-S lsetxattr" is not in the result, this is a finding.

## Group: GEN002820-10

**Group ID:** `V-29272`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45341r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " fsetxattr " If "-S fsetxattr" is not in the result, this is a finding.

## Group: GEN002820-11

**Group ID:** `V-29274`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45342r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " removexattr " If "-S removexattr" is not in the result, this is a finding.

## Group: GEN002820-12

**Group ID:** `V-29275`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45343r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " lremovexattr " If "-S lremovexattr" is not in the result, this is a finding.

## Group: GEN002820-13

**Group ID:** `V-29279`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-45344r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system's audit configuration. Procedure: # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i " fremovexattr " If "-S fremovexattr" is not in the result, this is a finding.

## Group: GEN002825-2

**Group ID:** `V-29281`

### Rule: The audit system must be configured to audit the loading and unloading of dynamic kernel modules - delete_module.

**Rule ID:** `SV-45451r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Actions concerning dynamic kernel modules must be recorded as they are substantial events. Dynamic kernel modules can increase the attack surface of a system. A malicious kernel module can be used to substantially alter the functioning of a system, often with the purpose of hiding a compromise from the SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the delete_module syscall is audited. # cat /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "delete_module" If the result does not contain "-S delete_module", this is a finding.

## Group: GEN002825-3

**Group ID:** `V-29284`

### Rule: The audit system must be configured to audit the loading and unloading of dynamic kernel modules - /sbin/insmod.

**Rule ID:** `SV-45462r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Actions concerning dynamic kernel modules must be recorded as they are substantial events. Dynamic kernel modules can increase the attack surface of a system. A malicious kernel module can be used to substantially alter the functioning of a system, often with the purpose of hiding a compromise from the SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if /sbin/insmod is audited. # cat /etc/audit/audit.rules | grep "/sbin/insmod" If the result does not start with "-w" and contain "-p x", this is a finding.

## Group: GEN002825-4

**Group ID:** `V-29286`

### Rule: The audit system must be configured to audit the loading and unloading of dynamic kernel modules -/sbin/modprobe.

**Rule ID:** `SV-45549r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Actions concerning dynamic kernel modules must be recorded as they are substantial events. Dynamic kernel modules can increase the attack surface of a system. A malicious kernel module can be used to substantially alter the functioning of a system, often with the purpose of hiding a compromise from the SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the /sbin/modprobe file is audited. # cat /etc/audit/audit.rules | grep "/sbin/modprobe" If the result does not start with "-w" and contain "-p x" ,this is a finding.

## Group: GEN002825-5

**Group ID:** `V-29288`

### Rule: The audit system must be configured to audit the loading and unloading of dynamic kernel modules - /sbin/rmmod

**Rule ID:** `SV-45552r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Actions concerning dynamic kernel modules must be recorded as they are substantial events. Dynamic kernel modules can increase the attack surface of a system. A malicious kernel module can be used to substantially alter the functioning of a system, often with the purpose of hiding a compromise from the SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the /sbin/rmmod file is audited. # cat /etc/audit/audit.rules | grep "/sbin/rmmod" If the result does not start with "-w" and contain "-p x", this is a finding.

## Group: GEN003080-2

**Group ID:** `V-29289`

### Rule: Files in cron script directories must have mode 0700 or less permissive.

**Rule ID:** `SV-45599r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of scheduled system jobs and prevent malicious modification to these jobs, crontab files must be secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of scripts in cron job directories. ls -lL /etc/cron.{d,daily,hourly,monthly,weekly} If any cron script has a mode more permissive than 0700, this is a finding.

## Group: GEN000290-1

**Group ID:** `V-29376`

### Rule: The system must not have the unnecessary games account.

**Rule ID:** `SV-44795r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts that provide no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for the unnecessary "games" accounts. Procedure: # grep ^games /etc/passwd If this account exists, it is a finding.

## Group: GEN000000-ZSLE0002

**Group ID:** `V-34936`

### Rule: Global settings defined in common-{account,auth,password,session} must be applied in the pam.d definition files.

**Rule ID:** `SV-46164r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Pam global requirements are generally defined in the common-account, common-auth, common- password and common-session files located in the /etc/pam.d directory In order for the requirements to be applied the file(s) containing them must be included directly or indirectly in each program's definition file in /etc/pam.d</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls>ECSC-1</IAControls>

**Check Text:**
Verify that common-{account,auth,password,session} settings are being applied. Procedure: Verify that local customization has occurred in the common-{account,auth,password,session}-pc file(s) by some method other than the use of the pam-config utility. The files "/etc/pam.d/common-{account,auth,password,session} -pc " are autogenerated by "pam-config". Any manual changes made to them will be lost the next time "pam-config" is run. Check to see if the system default for any of the symlinks pointing to the "/etc/pam.d/common-{account,auth,password,session} -pc" files have been changed. # ls -l /etc/pam.d/common-{account,auth,password,session} If the symlinks point to "/etc/pam.d/common-{account,auth,password,session}-pc" and manual updates have been made in these files, the updates can not be protected. This is a finding.

## Group: GEN005400-ZSLE0001

**Group ID:** `V-35025`

### Rule: The /etc/rsyslog.conf file must be owned by root.

**Rule ID:** `SV-46279r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the /etc/rsyslog.conf file is not owned by root, unauthorized users could be allowed to view, edit, or delete important system messages handled by the syslog facility.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/rsyslog.conf ownership: # ls –lL /etc/rsyslog* If any rsyslog configuration file is not owned by root, this is a finding.

## Group: GEN005420-ZSLE0003

**Group ID:** `V-35026`

### Rule: The /etc/rsyslog.conf file must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-46280r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the group owner of /etc/rsyslog.conf is not root, bin, or sys, unauthorized users could be permitted to view, edit, or delete important system messages handled by the syslog facility.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/rsyslog.conf group ownership. Procedure: # ls -lL /etc/rsyslog* If any rsyslog.conf file is not group owned by root, sys, bin, or system, this is a finding.

## Group: GEN007841

**Group ID:** `V-72825`

### Rule: Wireless network adapters must be disabled.

**Rule ID:** `SV-87473r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of wireless networking can introduce many different attack vectors into the organization’s network. Common attack vectors such as malicious association and ad hoc networks will allow an attacker to spoof a wireless access point (AP), allowing validated systems to connect to the malicious AP and enabling the attacker to monitor and record network traffic. These malicious APs can also serve to create a man-in-the-middle attack or be used to create a denial-of-service to valid network resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is N/A for systems that do not have wireless network adapters. Verify that there are no wireless interfaces configured on the system: # ifconfig -a eth0 Link encap:Ethernet HWaddr b8:ac:6f:65:31:e5 inet addr:192.168.2.100 Bcast:192.168.2.255 Mask:255.255.255.0 inet6 addr: fe80::baac:6fff:fe65:31e5/64 Scope:Link UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1 RX packets:2697529 errors:0 dropped:0 overruns:0 frame:0 TX packets:2630541 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 RX bytes:2159382827 (2.0 GiB) TX bytes:1389552776 (1.2 GiB) Interrupt:17 lo Link encap:Local Loopback inet addr:127.0.0.1 Mask:255.0.0.0 inet6 addr: ::1/128 Scope:Host UP LOOPBACK RUNNING MTU:16436 Metric:1 RX packets:2849 errors:0 dropped:0 overruns:0 frame:0 TX packets:2849 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:0 RX bytes:2778290 (2.6 MiB) TX bytes:2778290 (2.6 MiB) If a wireless interface is configured, it must be documented and approved by the local Authorizing Official. If a wireless interface is configured and has not been documented and approved, this is a finding.

