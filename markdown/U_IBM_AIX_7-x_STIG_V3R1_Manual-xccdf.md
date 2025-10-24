# STIG Benchmark: IBM AIX 7.x Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-215169`

### Rule: AIX /etc/security/mkuser.sys.custom file must not exist unless it is needed for customizing a new user account.

**Rule ID:** `SV-215169r958362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/security/mkuser.sys.custom" is called by "/etc/security/mkuser.sys" to customize the new user account when a new user is created, or a user is logging into the system without a home directory. An improper "/etc/security/mkuser.sys.custom" script increases the risk that non-privileged users may obtain elevated privileges. It must not exist unless it is needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the "/etc/security/mkuser.sys.custom" file exists: # ls /etc/security/mkuser.sys.custom If the above command shows the file exists, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-215170`

### Rule: AIX must automatically remove or disable temporary user accounts after 72 hours or sooner.

**Rule ID:** `SV-215170r958364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, the operating system must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. To address access requirements, many operating systems may be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # lsuser -a expires tmp_user The above command should yield the following output: tmp_user expires=0 Or tmp_user expires=1215103116 The "expires" value is in "MMDDhhmmyy" form, or the value is "0". If "expires" value is "0", or the expiration time is greater than "72" hours from the user creation time, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-215171`

### Rule: AIX must enforce the limit of three consecutive invalid login attempts by a user before the user account is locked and released by an administrator.

**Rule ID:** `SV-215171r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command to check the system default value for the maximum number of tries before the system will lock the account: # lssec -f /etc/security/user -s default -a loginretries The above command should yield the following output: default loginretries=0 If the default value is "0" or greater than "3", this is a finding. From the command prompt, execute the following command to check all active accounts on the system for the maximum number of tries before the system will lock the account: # lsuser -a loginretries ALL | more The above command should yield the following output: root loginretries=3 user1 loginretries=2 If a user has values set to "0" or greater than "3", this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-215172`

### Rule: AIX must limit the number of concurrent sessions to 10 for all accounts and/or account types.

**Rule ID:** `SV-215172r958398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command to display maxulogs values for all the user account: # lsuser -a maxulogs ALL The above command should yield the following output: root maxulogs=10 user_1 maxulogs=10 If the above command shows any user account that does not have the "maxulogs" attribute set, or its value is "0", or its value greater than "10", this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-215173`

### Rule: If the AIX system is using LDAP for authentication or account information, the LDAP SSL, or TLS connection must require the server provide a certificate and this certificate must have a valid path to a trusted CA.

**Rule ID:** `SV-215173r958448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If LDAP authentication is not used on AIX, this is Not Applicable. Note: Depending on which version of GSKit is installed on AIX, the GSK commands that are used to manage the Key Database (KDB) have different names. The possible GSK commands are: gsk8capicmd (used below), gsk8capicmd_64 and gsk7cmd. Check if the system is using LDAP authentication: # grep LDAP /etc/security/user If no lines are returned, this requirement is not applicable. Check if the useSSL option is enabled: # grep '^useSSL' /etc/security/ldap/ldap.cfg useSSL:yes If "yes" is not the returned value, this is a finding. Verify a certificate is used for client authentication to the server: # grep -i '^ldapsslkeyf' /etc/security/ldap/ldap.cfg ldapsslkeyf:/tmp/key.kdb If no line is found, this is a finding. Identify the Key Database (KDB), and its password, by asking the ISSO/SA. If no Key Database exists on the system, this is a finding. List the certificate issuer with GSK command: # gsk8capicmd -cert -list CA -db <KDB_FILE> -pw <KDB_PASSWORD> Make note of the client Key Label: # gsk8capicmd -cert -details -showOID -db <KDB_FILE> -pw <KDB_PASSWORD> -label <Key Label> If the certificate is not issued by DoD PKI or a DoD-approved external PKI, this is a finding The IBM GSK Database should only have certificates for the client system and for the LDAP server. If more certificates are in the key database than the LDAP server and the client, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-215174`

### Rule: If AIX is using LDAP for authentication or account information, the /etc/ldap.conf file (or equivalent) must not contain passwords.

**Rule ID:** `SV-215174r1009530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the LDAP configuration file "/etc/security/ldap/ldap.cfg" for possible clear-text password for "bindpwd". From the command prompt, run the following command: # grep ^bindpwd: /etc/security/ldap/ldap.cfg The above command should yield the following output: bindpwd:{DESv2}57AEE2BCED 764373462FC7B62736D9A If the returned entry has an unencrypted password (the output line does not start with "bindpwd:{DES"), this is a finding. Examine the LDAP configuration file "/etc/security/ldap/ldap.cfg" for using stashed password for SSL key database (KDB). Check for "ldapsslkeypwd" in LDAP config file using the follow command: # grep '^ldapsslkeypwd' /etc/security/ldap/ldap.cfg If the command returned a line, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-215175`

### Rule: All accounts on AIX system must have unique account names.

**Rule ID:** `SV-215175r958482_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check that there are no duplicate account names: # usrck -n ALL If any duplicate account names are found, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-215176`

### Rule: All accounts on AIX must be assigned unique User Identification Numbers (UIDs) and must authenticate organizational and non-organizational users (or processes acting on behalf of these users).

**Rule ID:** `SV-215176r958482_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Lack of authentication and identification enables non-organizational users to gain access to the application or possibly other information systems and provides an opportunity for intruders to compromise resources within the application or information system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to ensure there are no duplicate UIDs: # usrck -n ALL If any duplicate UIDs are found, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-215177`

### Rule: The AIX SYSTEM attribute must not be set to NONE for any account.

**Rule ID:** `SV-215177r958482_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "SYSTEM" attribute values for all users in the "/etc/security/user" file by running the following command: # lsuser -a SYSTEM ALL The above command should yield the following output: root SYSTEM=compat daemon SYSTEM=compat bin SYSTEM=compat sys SYSTEM=compat If the command displays SYSTEM=NONE for a user, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-215178`

### Rule: Direct logins to the AIX system must not be permitted to shared accounts, default accounts, application accounts, and utility accounts.

**Rule ID:** `SV-215178r1009531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shared accounts (accounts where two or more people log in with the same user identification) do not provide identification and authentication. There is no way to provide for non-repudiation or individual accountability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of Shared/Application/Default/Utility accounts from the ISSO/ISSM. Shared/Application/Default/Utility accounts can have direct login disabled by setting the "rlogin" parameter to "false" in the user’s stanza of the "/etc/security/user" file. From the command prompt, run the following command to check if shared account has "rlogin=true": # lsuser -a rlogin [shared_account] <shared_account> rlogin=true If a shared account is configured for "rlogin=true", this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-215179`

### Rule: AIX must use the SSH server to implement replay-resistant authentication mechanisms for network access to privileged and non-privileged accounts.

**Rule ID:** `SV-215179r1009532_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the operating system. Authentication sessions between the authenticator and the operating system validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A privileged account is any information system account with authorizations of a privileged user. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check if SSH server package is installed: # lslpp -i |grep -i ssh openssh.base.server 6.0.0.6201 If package "openssh.base.server" is not installed, this is a finding. Run the following command to check if SSH daemon is running: # lssrc -s sshd The above command should yield the following output: Subsystem Group PID Status sshd ssh 4325532 active If the "Status" is not "active", this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-215180`

### Rule: The AIX system must automatically remove or disable emergency accounts after the crisis is resolved or 72 hours.

**Rule ID:** `SV-215180r958508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local login accounts used by the organization's system administrators when network or normal login/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of emergency accounts from the ISSO/ISSM and then run this command against each of the identified accounts: # lsuser -a expires <emergency_user> The above command should yield the following output: <emergency_user> expires=0 Or <emergency_user> expires=1215103116 The "expires" value parameter is a 10-character string in the MMDDhhmmyy form, where MM = month, DD = day, hh = hour, mm = minute, and yy = last 2 digits of the years 1939 through 2038. All characters are numeric. If the Value parameter is 0, the account does not expire. If "expires" value is "0", or the expiration time is greater than "72" hours from the user creation time, this is a finding.

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-215181`

### Rule: The shipped /etc/security/mkuser.sys file on AIX must not be customized directly.

**Rule ID:** `SV-215181r958362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/security/mkuser.sys" script customizes the new user account when a new user is created, or a user is logging into the system without a home directory. An improper "/etc/security/mkuser.sys" script increases the risk that non-privileged users may obtain elevated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the "cat" command to show the content of "/etc/security/mkuser.sys" script: # cat /etc/security/mkuser.sys The cat command should display the following: # This file is no longer user customizable. To have a customized mkuser.sys script # create a file /etc/security/mkuser.sys.custom and the /etc/security/mkuser.sys # will run this script instead of the original mkuser.sys script. export PATH=/usr/bin:/usr/sbin:$PATH # # Check the number of arguments first # if [ $# -ne 4 ] then exit 1 fi # # If a customer mkuser.sys.custom script exists # then execute it instead and exit passing all arguments # and returning the return code from mkuser.sys.custom # if [ -x /etc/security/mkuser.sys.custom ] then /etc/security/mkuser.sys.custom $* exit $? fi # # Create the named directory if it does not already exist # and set the file ownership and permission # if [ ! -d $1 ] then last=$1 while [ 1 ] do dir=`dirname $last` if [ -d $last ] then break elif [ -d $dir ] then mkdir -p $1 chown -R bin:bin $last chmod -R 755 $last break else last=$dir fi done chgrp "$3" $1 chown $2 $1 fi # # Copy the user's default .profile if it does not already # exist and change the file ownership, etc. # if [ `basename $4` != "csh" ] && [ ! -f $1/.profile ] then cp /etc/security/.profile $1/.profile chmod u+rwx,go-w $1/.profile chgrp "$3" $1/.profile chown $2 $1/.profile else if [ `basename $4` = "csh" ] && [ ! -f $1/.login ] then echo "#!/bin/csh" > "$1"/.login echo "set path = ( /usr/bin /etc /usr/sbin /usr/ucb \$HOME/bin /usr/bin/X11 /sbin . )" >> "$1"/.login echo "setenv MAIL \"/var/spool/mail/\$LOGNAME\"" >> "$1"/.login echo "setenv MAILMSG \"[YOU HAVE NEW MAIL]\"" >> "$1"/.login echo "if ( -f \"\$MAIL\" && ! -z \"\$MAIL\") then" >> "$1"/.login echo " echo \"\$MAILMSG\"" >> "$1"/.login echo "endif" >> "$1"/.login chmod u+rwx,go-w $1/.login chgrp "$3" $1/.login chown $2 $1/.login fi fi If the "cat" command shows the script as different than the content listed above, this is a finding.

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-215182`

### Rule: The regular users default primary group must be staff (or equivalent) on AIX.

**Rule ID:** `SV-215182r958362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /usr/lib/security/mkuser.default file contains the default primary groups for regular and admin users. Setting a system group as the regular users' primary group increases the risk that the regular users can access privileged resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the default primary group for regular users: # lssec -f /etc/security/mkuser.default -s user -a pgrp The above command should yield the following output: user pgrp=staff If the above command shows that the primary group (pgrp) is not "staff", this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-215183`

### Rule: All system files, programs, and directories must be owned by a system account.

**Rule ID:** `SV-215183r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permissions will protect the files from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of system files, programs, and directories by running the following command: # ls -lLa /etc /bin /usr/bin /usr/lbin /usr/ucb /sbin /usr/sbin If any of the system files, programs, or directories are not owned by a system account, this is a finding. Note: For this check, the system-provided "ipsec" user is considered to be a system account.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-215184`

### Rule: AIX device files and directories must only be writable by users with a system account or as configured by the vendor.

**Rule ID:** `SV-215184r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System device files in writable directories could be modified, removed, or used by an unprivileged user to control system hardware.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Find all device files existing anywhere on the system using commands: # find / -type b -print | xargs ls -l > devicelistB # find / -type c -print | xargs ls -l > devicelistC Look at devicelistB and devicelistC files to check the permissions on the device files and directories above the subdirectories containing device files. If any of the device files or their parent directories are world-writable, excepting device files specifically intended to be world-writable, such as "/dev/null", this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-215186`

### Rule: AIX must configure the ttys value for all interactive users.

**Rule ID:** `SV-215186r958498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A user's "ttys" attribute controls from which device(s) the user can authenticate and log in. If the "ttys" attribute is not specified, all terminals can access the user account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the default "ttys" value is set for all users: # lssec -f /etc/security/user -s default -a ttys default ttys=ALL If the value returned is not "ttys=ALL", this is a finding. From the command prompt, run the following command to check "ttys" attribute value for all accounts: # lsuser -a ttys ALL The above command should yield the following output: root ttys=ALL user1 ttys=ALL user2 ttys=ALL user3 ttys=ALL If any interactive user account does not have "ttys=ALL", this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-215187`

### Rule: AIX must provide the lock command to let users retain their session lock until users are reauthenticated.

**Rule ID:** `SV-215187r958400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All systems are vulnerable if terminals are left logged in and unattended. Leaving system terminals unsecure poses a potential security hazard. To lock the terminal, use the lock command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system to determine if "bos.rte.security" is installed: # lslpp -L bos.rte.security Fileset Level State Type Description (Uninstaller) ---------------------------------------------------------------------------- bos.rte.security 7.2.1.1 C F Base Security Function If the "bos.rte.security" fileset is not installed, this is a finding. Check if lock command exist using the following command: # ls /usr/bin/lock The above command should display the following: /usr/bin/lock If the above command does not show that "/usr/bin/lock" exists, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-215188`

### Rule: AIX must provide xlock command in the CDE environment to let users retain their sessions lock until users are reauthenticated.

**Rule ID:** `SV-215188r958400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All systems are vulnerable if terminals are left logged in and unattended. Leaving system terminals unsecure poses a potential security hazard. If the interface is AIXwindows (CDE), use the xlock command to lock the sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If AIX CDE (X11) is not used, this is Not Applicable. Check the system to determine if "X11.apps.clients" is installed: # lslpp -L X11.apps.clients If the "X11.apps.clients" fileset is not installed, this is a finding. Check if "xlock" command exists using the following command: # ls /usr/bin/X11/xlock The above command should display the following: /usr/bin/X11/xlock If the above command does not show that "/usr/bin/X11/xlock" exists, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215189`

### Rule: AIX system must prevent the root account from directly logging in except from the system console.

**Rule ID:** `SV-215189r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the root account direct logins to only system consoles protects the root account from direct unauthorized access from a non-console device. A common attack method of potential hackers is to obtain the root password. To avoid this type of attack, disable direct access to the root ID and then require system administrators to obtain root privileges by using the su - command. In addition to permitting removal of the root user as a point of attack, restricting direct root access permits monitoring which users gained root access, as well as the time of their action. Do this by viewing the /var/adm/sulog file. Another alternative is to enable system auditing, which will report this type of activity. To disable remote login access for the root user, edit the /etc/security/user file. Specify False as the rlogin value on the entry for root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the remote login ability of the root account using command: # lsuser -a rlogin root root rlogin=false If the "rlogin" value is not "false", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215190`

### Rule: All AIX public directories must be owned by root or an application account.

**Rule ID:** `SV-215190r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public directory has the sticky bit set and is not owned by a privileged UID, unauthorized users may be able to modify files created by others. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of all public directories using command: # find / -type d -perm -1002 -exec ls -ld {} \; If any public directory is not owned by "root" or an application user, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215191`

### Rule: AIX administrative accounts must not run a web browser, except as needed for local service administration.

**Rule ID:** `SV-215191r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a web browser flaw is exploited while running as a privileged user, the entire system could be compromised. Specific exceptions for local service administration should be documented in site-defined policy. These exceptions may include HTTP(S)-based tools used for the administration of the local system, services, or attached devices. Examples of possible exceptions are HP’s System Management Homepage (SMH), the CUPS administrative interface, and Sun's StorageTek Common Array Manager (CAM) when these services are running on the local system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the root account home directory for a ".netscape" or a ".mozilla" directory using the following commands: # find /root -name .netscape # find /root -name .mozilla If none exists, this is not a finding. If a file exists, verify with the root users and the ISSO the intent of the browsing. If a file exists and use of a web browser has not been authorized, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215192`

### Rule: AIX default system accounts (with the exception of root) must not be listed in the cron.allow file or must be included in the cron.deny file, if cron.allow does not exist.

**Rule ID:** `SV-215192r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To centralize the management of privileged account crontabs, of the default system accounts, only root may have a crontab.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "cron.allow" and "cron.deny" files for the system using commands: # more /var/adm/cron/cron.allow # more /var/adm/cron/cron.deny If the "cron.allow" file exists and is empty, this is a finding. If a default system account (such as bin, sys, adm, or lpd) is listed in the "cron.allow" file, or not listed in the "cron.deny" file, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215193`

### Rule: The AIX root account must not have world-writable directories in its executable search path.

**Rule ID:** `SV-215193r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the root search path contains a world-writable directory, malicious software could be placed in the path by intruders and/or malicious users and inadvertently run by root with all of root's privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for world-writable permissions on all directories in the root user's executable search path: # ls -ld `echo $PATH | sed "s/:/ /g"` drwxr-xr-x 33 root system 8192 Nov 29 14:45 /etc drwxr-xr-x 3 bin bin 256 Aug 11 2017 /sbin drwxr-xr-x 4 bin bin 45056 Oct 31 12:59 /usr/bin drwxr-xr-x 1 bin bin 16 Aug 11 2017 /usr/bin/X11 drwxr-xr-x 2 bin bin 4096 Aug 11 2017 /usr/java7_64/bin drwxr-xr-x 4 bin bin 4096 Feb 17 2017 /usr/java7_64/jre/bin drwxr-xr-x 8 bin bin 49152 Oct 31 12:59 /usr/sbin drwxrwxr-x 2 bin bin 4096 Aug 11 2017 /usr/ucb If any of the directories in the "PATH" variable are world-writable, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215194`

### Rule: The Group Identifiers (GIDs) reserved for AIX system accounts must not be assigned to non-system accounts as their primary group GID.

**Rule ID:** `SV-215194r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reserved GIDs are typically used by system software packages. If non-system groups have GIDs in this range, they may conflict with system software, possibly leading to the group having permissions to modify system files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command: # more /etc/passwd root:!:0:0::/root:/usr/bin/ksh daemon:!:1:1::/etc: bin:!:2:2::/bin: sys:!:3:3::/usr/sys: adm:!:4:4::/var/adm: nobody:!:4294967294:4294967294::/: invscout:*:6:12::/var/adm/invscout:/usr/bin/ksh srvproxy:*:203:0:Service Proxy Daemon:/home/srvproxy:/usr/bin/ksh esaadmin:*:7:0::/var/esa:/usr/bin/ksh sshd:*:212:203::/var/empty:/usr/bin/ksh doejohn:*:704:1776::/home/doej:/usr/bin/ksh Confirm all accounts with a primary GID of 99 and below are used by a system account. If a GID reserved for system accounts, 0 - 99, is used by a non-system account, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215195`

### Rule: UIDs reserved for system accounts must not be assigned to non-system accounts on AIX systems.

**Rule ID:** `SV-215195r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reserved UIDs are typically used by system software packages. If non-system accounts have UIDs in this range, they may conflict with system software, possibly leading to the user having permissions to modify system files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the UID assignments of all accounts using: # more /etc/passwd root:!:0:0::/root:/usr/bin/ksh daemon:!:1:1::/etc: bin:!:2:2::/bin: sys:!:3:3::/usr/sys: adm:!:4:4::/var/adm: nobody:!:4294967294:4294967294::/: invscout:*:6:12::/var/adm/invscout:/usr/bin/ksh srvproxy:*:203:0:Service Proxy Daemon:/home/srvproxy:/usr/bin/ksh esaadmin:*:7:0::/var/esa:/usr/bin/ksh sshd:*:212:203::/var/empty:/usr/bin/ksh doej:*:704:1776::/home/doej:/usr/bin/ksh Confirm all accounts with a UID of 128 and below are used by a system account. If a UID reserved for system accounts (0-128) is used by a non-system account, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215196`

### Rule: The AIX root accounts list of preloaded libraries must be empty.

**Rule ID:** `SV-215196r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries relative to the current working directory, unintended libraries may be preloaded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "LDR_PRELOAD" environment variable is empty or not defined for the "root" user using command: # env | grep LDR_PRELOAD If a path is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-215197`

### Rule: AIX must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-215197r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account is configured for password authentication but does not have an assigned password, it may be possible to log into the account without authentication. If the root user is configured without a password, the entire system may be compromised. For user accounts not using password authentication, the account must be configured with a password lock value instead of a blank or null value.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify no interactive accounts have blank passwords by running the following command: # pwdck -n ALL If any interactive account with a blank password is found, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215198`

### Rule: The AIX root accounts home directory (other than /) must have mode 0700.

**Rule ID:** `SV-215198r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users' home directories/folders may contain information of a sensitive nature. Non-privileged users should coordinate any sharing of information with an SA through shared resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the root home directory by running the following commands: # ls -ld `grep "^root" /etc/passwd | awk -F":" '{print $6}'` The above command should yield the following output: drwx------ 22 root system 4096 Sep 06 18:00 /root If the mode of the directory is not equal to "0700", this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215199`

### Rule: The AIX root accounts home directory must not have an extended ACL.

**Rule ID:** `SV-215199r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on root home directories allow unauthorized access to root user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "root" account's home directory has no extended ACL using command: # aclget ~root * * ACL_type AIXC * attributes: base permissions owner(root): rwx group(system): --- others: --- extended permissions disabled If extended permissions are enabled, the directory has an extended ACL, and this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-215200`

### Rule: AIX must display the Standard Mandatory DoD Notice and Consent Banner before granting local or remote login access to the system.

**Rule ID:** `SV-215200r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the herald is set to have the Standard Mandatory DoD Notice and Consent Banner: # lssec -f /etc/security/login.cfg -s default -a herald The above command should display the herald setting like this: default herald="You are accessing a U.S. Government (USG) Information System (IS) that\n\ris provided for USG-authorized use only.\n\r\n\rBy using this IS (which includes any device attached to this IS), you\n\rconsent to the following conditions: \n\r\n\r-The USG routinely intercepts and monitors communications on this IS\n\rfor purposes including, but not limited to, penetration testing, COMSEC\n\rmonitoring, network operations and defense, personnel misconduct (PM),\n\rlaw enforcement (LE), and counterintelligence (CI) investigations. \n\r\n\r-At any time, the USG may inspect and seize data stored on this IS. \n\r\n\r-Communications using, or data stored on, this IS are not private, are\n\rsubject to routine monitoring, interception, and search, and may be\n\rdisclosed or used for any USG-authorized purpose. \n\r\n\r-This IS includes security measures (e.g., authentication and access\n\rcontrols) to protect USG interests--not for your personal benefit or\n\rprivacy. \n\r\n\r-Notwithstanding the above, using this IS does not constitute consent\n\rto PM, LE or CI investigative searching or monitoring of the content\n\rof privileged communications, or work product, related to personal\n\rrepresentation or services by attorneys, psychotherapists, or clergy,\n\rand their assistants. Such communications and work product are private\n\rand confidential. See User Agreement for details.\n\r\n\rlogin:" If the herald string is not set, or it does not contain the Standard Mandatory DoD Notice and Consent Banner listed above, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-215201`

### Rule: The Department of Defense (DoD) login banner must be displayed immediately prior to, or as part of, graphical desktop environment login prompts on AIX.

**Rule ID:** `SV-215201r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If AIX CDE (X11) is not used, this is Not Applicable. Check if file "/etc/dt/config/en_US/Xresources" exists: # ls /etc/dt/config/en_US/Xresources If the file does not exist, this is a finding. Check if the "Dtlogin*greeting.labelString" is set to the Standard Mandatory DoD Notice and Consent Banner: # grep "Dtlogin*greeting.labelString" /etc/dt/config/en_US/Xresources The above command should display the following: Dtlogin*greeting.labelString: You are accessing a U.S. Government (USG) Information System (IS) that\nis provided for USG-authorized use only.\n\nBy using this IS (which includes any device attached to this IS), you\nconsent to the following conditions: \n\n-The USG routinely intercepts and monitors communications on this IS\nfor purposes including, but not limited to, penetration testing, COMSEC\nmonitoring, network operations and defense, personnel misconduct (PM),\nlaw enforcement (LE), and counterintelligence (CI) investigations. \n\n-At any time, the USG may inspect and seize data stored on this IS. \n\n-Communications using, or data stored on, this IS are not private, are\nsubject to routine monitoring, interception, and search, and may be\ndisclosed or used for any USG-authorized purpose. \n\n-This IS includes security measures (e.g., authentication and access\ncontrols) to protect USG interests--not for your personal benefit or\nprivacy. \n\n-Notwithstanding the above, using this IS does not constitute consent\nto PM, LE or CI investigative searching or monitoring of the content\nof privileged communications, or work product, related to personal\nrepresentation or services by attorneys, psychotherapists, or clergy,\nand their assistants. Such communications and work product are private\nand confidential. See User Agreement for details. If the "Dtlogin*greeting.labelString" variable is not set, or the label string does not contain the Standard Mandatory DoD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-215202`

### Rule: The Department of Defense (DoD) login banner must be displayed during SSH, sftp, and scp login sessions on AIX.

**Rule ID:** `SV-215202r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if file "/etc/motd.ssh" exists: # ls /etc/motd.ssh If the file does not exist, this is a finding. Check if "/etc/motd.ssh" contains The Standard Mandatory DoD Notice and Consent Banner: # cat /etc/motd.ssh The above command should display the following Standard Mandatory DoD Notice and Consent Banner: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the Standard Mandatory DoD Notice and Consent Banner is not displayed by the "cat" command, this is a finding. Check if /etc/motd.ssh is used as banner file in SSH config file: # grep -i "Banner /etc/motd.ssh" /etc/motd.ssh If the above grep command does not find "Banner /etc/motd.ssh" in the "/etc/motd.ssh" file, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-215203`

### Rule: Any publically accessible connection to AIX operating system must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-215203r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the herald is set to have the Standard Mandatory DoD Notice and Consent Banner: # lssec -f /etc/security/login.cfg -s default -a herald The above command should display the herald setting like this: default herald="You are accessing a U.S. Government (USG) Information System (IS) that\n\ris provided for USG-authorized use only.\n\r\n\rBy using this IS (which includes any device attached to this IS), you\n\rconsent to the following conditions: \n\r\n\r-The USG routinely intercepts and monitors communications on this IS\n\rfor purposes including, but not limited to, penetration testing, COMSEC\n\rmonitoring, network operations and defense, personnel misconduct (PM),\n\rlaw enforcement (LE), and counterintelligence (CI) investigations. \n\r\n\r-At any time, the USG may inspect and seize data stored on this IS. \n\r\n\r-Communications using, or data stored on, this IS are not private, are\n\rsubject to routine monitoring, interception, and search, and may be\n\rdisclosed or used for any USG-authorized purpose. \n\r\n\r-This IS includes security measures (e.g., authentication and access\n\rcontrols) to protect USG interests--not for your personal benefit or\n\rprivacy. \n\r\n\r-Notwithstanding the above, using this IS does not constitute consent\n\rto PM, LE or CI investigative searching or monitoring of the content\n\rof privileged communications, or work product, related to personal\n\rrepresentation or services by attorneys, psychotherapists, or clergy,\n\rand their assistants. Such communications and work product are private\n\rand confidential. See User Agreement for details.\n\r\n\rlogin:" If the herald string is not set, or it does not contain the Standard Mandatory DoD Notice and Consent Banner listed above, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-215204`

### Rule: IF LDAP is used, AIX LDAP client must use SSL to authenticate with LDAP server.

**Rule ID:** `SV-215204r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>While LDAP client's authentication type is ldap_auth (server-side authentication), the client sends password to the server in clear text for authentication. SSL must be used in this case.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check if "authtype" is "ldap_auth": # grep -iE "^authtype:[[:blank:]]*ldap_auth" /etc/security/ldap/ldap.cfg The above command should yield the following output: authtype:ldap_auth Run the following command to check if SSL is not used in the "/etc/security/ldap/ldap.cfg" file: # grep -iE "^useSSL:[[:blank:]]*yes" /etc/security/ldap/ldap.cfg The above command should yield the following output: useSSL:yes If the first command displays "authtype:ldap_auth" but the second command does not display "useSSL:yes", this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-215205`

### Rule: If LDAP authentication is required, AIX must setup LDAP client to refresh user and group caches less than a day.

**Rule ID:** `SV-215205r958828_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If LDAP authentication is not required, this is Not Applicable. Verify the "/etc/security/ldap/ldap.cfg" file to see if the following two keywords have a value that is greater than "900" seconds: # grep -i usercachetimeout /etc/security/ldap/ldap.cfg usercachetimeout: 900 # grep -i groupcachetimeout /etc/security/ldap/ldap.cfg groupcachetimeout: 900 If any of the above keywords does not exist, is commented out, or any value of the above keywords are greater than "900", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215206`

### Rule: The AIX /etc/passwd, /etc/security/passwd, and/or /etc/group files must not contain a plus (+) without defining entries for NIS+ netgroups or LDAP netgroups.

**Rule ID:** `SV-215206r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A plus (+) in system accounts files causes the system to lookup the specified entry using NIS. If the system is not using NIS, no such entries should exist.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check system configuration files for plus (+) entries using the following commands: # cat /etc/passwd | grep -v "^#" | grep "\+" # cat /etc/security/passwd | grep -v "^#" | grep "\+" # cat /etc/group | grep -v "^#" | grep "\+" If the "/etc/passwd", "/etc/security/passwd", and/or "/etc/group" files contain a plus (+) and do not define entries for NIS+ netgroups or LDAP netgroups, this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-215207`

### Rule: AIX must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-215207r958552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive and tape drive, when used for backups) within an operating system. This requirement addresses protection of user-generated data, as well as operating system-specific configuration data. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization does not require to encrypt the data at rest this is Not Applicable. Check if the "clic.rte" fileset is installed: # lslpp -l |grep clic The above command should yield the following output: clic.rte.kernext 4.10.0.1 COMMITTED CryptoLite for C Kernel clic.rte.lib 4.10.0.1 COMMITTED CryptoLite for C Library clic.rte.kernext 4.10.0.1 COMMITTED CryptoLite for C Kernel If the "clic.rte" fileset is not installed, this is a finding. To check if a JFS2 file system (mounted as /fs2_mnt) is EFS-enabled, use the following command: # lsfs -q /fs2_mnt Name Nodename Mount Pt VFS Size Options Auto Accounting /dev/fslv00 -- /fs2_mnt jfs2 262144 -- no no (lv size: 262144, fs size: 262144, block size: 4096, sparse files: yes, inline log: no, inline log size: 0, EAformat: v2, Quota: no, DMAPI: no, VIX: yes, EFS: no, ISNAPSHOT: no, MAXEXT: 0, MountGuard: no) If the above command shows "EFS: no", this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-215208`

### Rule: AIX must provide time synchronization applications that can synchronize the system clock to external time sources at least every 24 hours.

**Rule ID:** `SV-215208r1009533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000356-GPOS-00144</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if time synchronization application "ntpd" is running using the command: # lssrc -s xntpd Subsystem Group PID Status xntpd tcpip 4784536 active If "ntpd" is showing "inoperative", this is a finding. Check that "ntp" server is configured using command: # grep server /etc/ntp.conf server 10.110.20.10 If the command returns no output, this is a finding. Check the poll interval is less than 24 hours using command: # grep maxpoll /etc/ntp.conf maxpoll=16 If "maxpoll" is set to larger than "16" (2^16 seconds ~= 18hr), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215209`

### Rule: All AIX NFS anonymous UIDs and GIDs must be configured to values without permissions.

**Rule ID:** `SV-215209r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When an NFS server is configured to deny remote root access, a selected UID and GID are used to handle requests from the remote root user. The UID and GID should be chosen from the system to provide the appropriate level of non-privileged access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the "anon" option is set correctly for exported file systems. List exported file systems using command: # exportfs -v /home/doej rw,anon=-1,access=doej Note: Each of the exported file systems should include an entry for the "anon=" option set to "-1" or an equivalent (60001, 60002, 65534, or 65535). If an appropriate "anon=" setting is not present for an exported file system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215210`

### Rule: AIX nosuid option must be enabled on all NFS client mounts.

**Rule ID:** `SV-215210r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling the nosuid mount option prevents the system from granting owner or group-owner privileges to programs with the suid or sgid bit set. If the system does not restrict this access, users with unprivileged access to the local system may be able to acquire privileged access by executing suid or sgid files located on the mounted NFS file system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for NFS mounts not using the "nosuid" option using command: # lsfs -v nfs Name Nodename Mount Pt VFS Size Options Auto Accounting /home/doej -- /mount/doej nfs 786432 -- yes no If the "mounted" file systems do not have the "nosuid option", this is a finding.

## Group: SRG-OS-000030-GPOS-00011

**Group ID:** `V-215211`

### Rule: AIX must be configured to allow users to directly initiate a session lock for all connection types.

**Rule ID:** `SV-215211r1009534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, operating systems need to provide users with the ability to manually invoke a session lock so users may secure their session should the need arise for them to temporarily vacate the immediate physical vicinity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the "lock" command exists by using the following command: # ls /usr/bin/lock The above command should display the following: /usr/bin/lock If the above command does not show that "/usr/bin/lock" exists, this is a finding. Check if the "xlock" command exists by using the following command: # ls /usr/bin/X11/xlock The above command should display the following: /usr/bin/X11/xlock If the above command does not show that "/usr/bin/xlock" exists, this is a finding.

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-215212`

### Rule: AIX CDE must conceal, via the session lock, information previously visible on the display with a publicly viewable image.

**Rule ID:** `SV-215212r958404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. The operating system session lock event must include an obfuscation of the display screen so as to prevent other users from reading what was previously displayed. Publicly viewable images can include static or dynamic images, for example, patterns used with screen savers, photographic images, solid colors, a clock, a battery life indicator, or a blank screen, with the additional caveat that none of the images convey sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If CDE (X11) is not used on AIX, this is Not Applicable. Ensure that the screen saver and session timeout are not disabled. From the command prompt, run the following script: # AIX7-00-001101_Check.sh Note: This script is included in the STIG package. The above script should yield the following output: Checking config file /etc/dt/config/C/sys.resources... Missing config file /etc/dt/config/C/sys.resources Checking config file /etc/dt/config/POSIX/sys.resources... dtsession*saverTimeout: 15 dtsession*lockTimeout: 30 Checking config file /etc/dt/config/en_US/sys.resources... dtsession*saverTimeout: 15 dtsession*lockTimeout: 25 If the result of the script shows any config file missing, or any of the "dtsession*saverTimeout" or "dtsession*lockTimeout" values is greater than "15", this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-215213`

### Rule: AIX must employ strong authenticators in the establishment of nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-215213r958510_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. The act of managing systems and applications includes the ability to access sensitive application information, such as system configuration details, diagnostic information, user information, and potentially sensitive application data. Some maintenance and test tools are either standalone devices with their own operating systems or are applications bundled with an operating system. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following to check if "telnetd" is enabled. # lssrc -t telnet | grep active If the above command returns output, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-215214`

### Rule: If LDAP authentication is required on AIX, SSL must be used between LDAP clients and the LDAP servers to protect the integrity of remote access sessions.

**Rule ID:** `SV-215214r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If LDAP authentication is used, SSL must be used between LDAP clients and the LDAP servers to protect the integrity of remote access sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check if ldap_auth is used: # grep -iE "^authtype:[[:blank:]]*ldap_auth" /etc/security/ldap/ldap.cfg If the command has no output, this is Not Applicable. Run the following command to check if SSL is used: # grep -iE "^useSSL:[[:blank:]]*yes" /etc/security/ldap/ldap.cfg useSSL:yes If the command has no output, this is a finding.

## Group: SRG-OS-000403-GPOS-00182

**Group ID:** `V-215215`

### Rule: AIX must only allow the use of DoD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-215215r958868_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI-certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: Depending on which version of GSKit is installed on AIX, the GSK commands that are used to manage the Key Database (KDB) have different names. The possible GSK commands are: gsk8capicmd (used below), gsk8capicmd_64 and gsk7cmd. Check if the system is using LDAP authentication: # grep LDAP /etc/security/user If no lines are returned, this requirement is not applicable. Check if the useSSL option is enabled: # grep '^useSSL' /etc/security/ldap/ldap.cfg useSSL:yes If "yes" is not the returned value, this is a finding. Verify a certificate is used for client authentication to the server: # grep -i '^ldapsslkeyf' /etc/security/ldap/ldap.cfg ldapsslkeyf:/tmp/key.kdb If no line is found, this is a finding. Identify the Key Database (KDB), and its password, by asking the ISSO/SA). If no Key Database exists on the system, this is a finding. List the certificate issuer with IBM GSK: # gsk8capicmd -cert -list CA -db <KDB_FILE> -pw <KDB_PASSWORD> Make note of the client Key Label: # gsk8capicmd -cert -details -showOID -db <KDB_FILE> -pw <KDB_PASSWORD> -label <Key Label> If the certificate is not issued by DoD PKI or a DoD-approved external PKI, this is a finding. The IBM GSK Database should only have certificates for the client system and for the LDAP server. If more certificates are in the key database than the LDAP server and the client, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-215216`

### Rule: AIX must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-215216r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. AIX must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. OpenSSL FIPS object module is a cryptographic module that is designed to meet the requirements for FIPS 140-2 validation by CMVP and is compatible with OpenSSL libraries. The 2.0.13 FIPS object module version has been FIPS validated and certified by CMVP for multiple AIX versions on Power 7 and Power 8 platforms under certificate #2398. IBM has released a FIPS capable OpenSSL (Fileset VRMF: 20.13.102.1000), which is OpenSSL 1.0.2j version with 2.0.13 object module. The fileset is available in Web Download Pack. Satisfies: SRG-OS-000120-GPOS-00061, SRG-OS-000478-GPOS-00223, SRG-OS-000396-GPOS-00176</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to determine the version of OpenSSL that is installed: # lslpp -l | grep -i openssl openssl.base 20.13.704.1776 COMMITTED Open Secure Socket Layer If the OpenSSL version is older than "20.13.102.1000", this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-215217`

### Rule: AIX must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-215217r1009535_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check the system default "minupperalpha" attribute value: # lssec -f /etc/security/user -s default -a minupperalpha The above command should yield the following output: default minupperalpha=1 If the default "minupperalpha" value is not set, or its value is less than "1", this is a finding. From the command prompt, run the following command to check "minupperalpha" attribute value for all accounts: # lsuser -a minupperalpha ALL The above command should yield the following output: root minupperalpha=2 user2 minupperalpha=2 user3 minupperalpha=1 If any user's "minupperalpha" value is less than "1", this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-215218`

### Rule: AIX must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-215218r1009536_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check the system default "minloweralpha" attribute value: # lssec -f /etc/security/user -s default -a minloweralpha default minloweralpha=1 If the "default minloweralpha" value is not set, or its value is less than "1", this is a finding. From the command prompt, run the following command to check "minloweralpha" attribute value for all accounts: # lsuser -a minloweralpha ALL root minloweralpha=1 user2 minloweralpha=2 user3 minloweralpha=1 If any user's "minloweralpha" value is less than "1", this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-215219`

### Rule: AIX must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-215219r1009537_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check the system default "mindigit" attribute value: # lssec -f /etc/security/user -s default -a mindigit default mindigit=1 If the default "mindigit" value is not set, or its value is less than "1", this is a finding. From the command prompt, run the following command to check mindigit attribute value for all accounts: # lsuser -a mindigit ALL root mindigit=1 user2 mindigit=2 If any user's "mindigit" value is less than "1", this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-215220`

### Rule: AIX must require the change of at least 50% of the total number of characters when passwords are changed.

**Rule ID:** `SV-215220r1009538_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least 8 characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check the system default "mindiff" attribute value: # lssec -f /etc/security/user -s default -a mindiff default mindiff=8 If the default "mindiff" value is not set, or its value is less than "8", this is a finding. From the command prompt, run the following command to check "mindiff" attribute value for all accounts: # lsuser -a mindiff ALL root mindiff=9 user1 mindiff=8 user2 mindiff=8 user3 mindiff=10 If any user's "mindiff" value is less than "8", this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-215221`

### Rule: AIX root passwords must never be passed over a network in clear text form.

**Rule ID:** `SV-215221r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if root has logged in over an unencrypted network connection: # last | grep "root " | egrep -v "reboot|console" | more root pts/1 10.74.17.76 Jul 4 16:44 - 17:39 (00:54) Next, determine if the SSH daemon is running: # ps -ef |grep sshd root 3670408 6029762 0 Jan 24 - 0:00 /usr/sbin/sshd If root has logged in over the network and SSHD is not running, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-215222`

### Rule: AIX Operating systems must enforce 24 hours/1 day as the minimum password lifetime.

**Rule ID:** `SV-215222r1009539_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check the system default "minage" attribute value: # lssec -f /etc/security/user -s default -a minage default minage=1 If the default "minage" value is not set, or its value is less than "1", this is a finding. From the command prompt, run the following command to check "minage" attribute value for all accounts: # lsuser -a minage ALL root minage=1 user1 minage=1 user2 minage=2 If any user's "minage" value is less than "1", this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-215223`

### Rule: AIX Operating systems must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-215223r1009540_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check the system default "maxage" attribute value: # lssec -f /etc/security/user -s default -a maxage default maxage=8 If the default "maxage" value is not set, or its value is great than "8", or its value is set to "0", this is a finding. From the command prompt, run the following command to check "maxage" attribute value for all accounts: # lsuser -a maxage ALL root maxage=8 user1 maxage=8 user2 maxage=8 If any user does not have "maxage" set, or its "maxage" value is greater than "8", or its value is set to "0", this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-215225`

### Rule: AIX must use Loadable Password Algorithm  (LPA) password hashing algorithm.

**Rule ID:** `SV-215225r1009541_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The default legacy password hashing algorithm, crypt(), uses only the first 8 characters from the password string, meaning the user's password is truncated to eight characters. If the password is shorter than 8 characters, it is padded with zero bits on the right. The crypt() is a modified DES algorithm that is vulnerable to brute force password guessing attacks and also to cracking the DES-hashing algorithm by using techniques such as pre-computation. With the Loadable Password Algorithm (LPA) framework release, AIX implemented a set of LPAs using MD5, SHA2, and Blowfish algorithms. These IBM proprietary password algorithms support a password longer than 8 characters and Unicode characters in passwords.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check system wide password algorithm: # lssec -f /etc/security/login.cfg -s usw -a pwd_algorithm usw pwd_algorithm=ssha512 If the "pwd_algorithm" is not set to "ssha512", or "ssha256", this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-215226`

### Rule: AIX must enforce a minimum 15-character password length.

**Rule ID:** `SV-215226r1009542_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check the system default "minlen" attribute value: # lssec -f /etc/security/user -s default -a minlen default minlen=15 If the default "minlen" value is not set, or its value is less than "15", this is a finding. From the command prompt, run the following command to check "minlen" attribute value for all accounts: # lsuser -a minlen ALL root minlen=15 user1 minlen=20 user2 minlen=15 user3 minlen=15 If any users have "minlen" value less than "15", this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-215227`

### Rule: AIX must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-215227r1009543_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check the system default value for "minspecialchar" attribute: # lssec -f /etc/security/user -s default -a minspecialchar The above command should yield the following output: default minspecialchar=1 If the default value is "0", or the default value is empty, this is a finding. From the command prompt, run the following command to check "minspecialchar" attribute value for all accounts: # lsuser -a minspecialchar ALL The above command should yield the following output: root minspecialchar=1 user1 minspecialchar=1 user2 minspecialchar=2 user3 minspecialchar=1 If any account has "minspecialchar=0", or the "minspecialchar" value is not set, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-215229`

### Rule: AIX must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-215229r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check if the default "dictionlist" attribute is set: # lssec -f /etc/security/user -s default -a dictionlist The above command should yield the following output: dictionlist="/etc/security/ice/dictionary/English" If the above command shows an empty string for default "dictionlist" attribute, this is a finding. From the command prompt, run the following command to check if "dictionlist" attribute is set for all users: # lsuser -a dictionlist ALL The above command should yield the following output: root dictionlist=/etc/security/ice/dictionary/English daemon dictionlist=/etc/security/ice/dictionary/English bin dictionlist=/etc/security/ice/dictionary/English sys dictionlist=/etc/security/ice/dictionary/English If any user's "dictionlist" attribute is empty, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215230`

### Rule: The password hashes stored on AIX system must have been generated using a FIPS 140-2 approved cryptographic hashing algorithm.

**Rule ID:** `SV-215230r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Systems must employ cryptographic hashes for passwords using the SHA-2 family of algorithms or FIPS 140-2 approved successors. The use of unapproved algorithms may result in weak password hashes that are more vulnerable to compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system wide password algorithm is set to {ssha256} or {ssha512} by running the following command: # lssec -f /etc/security/login.cfg -s usw -a pwd_algorithm usw pwd_algorithm=ssha512 If the "pwd_algorithm" is not set to "ssha256" or "ssha512", this is a finding. Verify no password hashes in /etc/passwd by running the following command: # cat /etc/passwd | cut -f2,2 -d":" ! ! ! ! * * * * If there are password hashes present, this is a finding. Verify all password hashes in "/etc/security/passwd" begin with {ssha256} or {ssha512} by running commands: # cat /etc/security/passwd | grep password password = {ssha512}06$e58YOawe/7UhChqh$hZEWlP4040jarX1NeOujmcxd.7qerUvjW9lM9djJsDITtdjFvVpLX.r04xieOWrbH0qb0SJJ98a0tmgZBzPP.. password = {ssha512}06$Y6ztvMxKGdITxPex$B81/GDTEPt0xwp.BX1VhY9mAPaWHXdNoLI9D0T6dBExgo6r87X0etnfjxWODT73.udrbAY.F4HzaBR68lN5/.. password = {ssha512}06$iIXQQqs.mdGpC9Wu$cXSajikWYKAUacbF50FNlFgYYSgTklGf4uhXb1J/GyBGF5j5aWa4YG5Ah2uaAHv/Jmbmx.7yBm8iXz9Pz1LM.. password = {ssha512}06$3Sw24rPVdqDFFCIl$d1dZs7GYmTXnD9i270SxozIBxN0pqq/bNn0YbyKeDq0o6Y.j9qfkeH373DwkHBWgrifNcgj/K0pVyzjMg6QN.. If any password hashes are present not beginning with {ssha256} or {ssha512}, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215231`

### Rule: If SNMP service is enabled on AIX, the default SNMP password must not be used in the /etc/snmpd.conf config file.

**Rule ID:** `SV-215231r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use default SNMP password increases the chance of security vulnerability on SNMP service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect "/etc/snmpd.conf" to find all the passwords that are used in the config file: # grep -v "^#" /etc/snmpd.conf | grep -E "public|private|password" If any results are returned, default passwords are being used and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215232`

### Rule: AIX must require passwords to contain no more than three consecutive repeating characters.

**Rule ID:** `SV-215232r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords with excessive repeating characters may be more vulnerable to password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check system default for "maxrepeats" attribute: # lssec -f /etc/security/user -s default -a maxrepeats default maxrepeats=3 If the default "maxrepeats" is greater than "3", or its value is not set, or its value is set to "0", this is a finding. Check the "maxrepeats" setting for all users using: # lsuser -a maxrepeats ALL The above command should yield the following output: root maxrepeats=3 daemon maxrepeats=3 bin maxrepeats=3 sys maxrepeats=3 If the "maxrepeats" setting for any user is greater than "3", or its value is set to "0", this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-215233`

### Rule: AIX must be able to control the ability of remote login for users.

**Rule ID:** `SV-215233r958672_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For users who are authorized to remote login through SSH, etc., this is Not Applicable. Ask ISSO/SA to obtain a list of users who are not authorized to remotely log in to AIX system. From the command prompt, run the following command to check if remote login is disabled for all individual users who are not authorized to remotely login to AIX: # lsuser -a rlogin ALL root rlogin=true daemon rlogin=true bin rlogin=true sys rlogin=true adm rlogin=true If "rlogin=true" for any user who should not login remotely, this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-215234`

### Rule: NFS file systems on AIX must be mounted with the nosuid option unless the NFS file systems contain approved setuid or setgid programs.

**Rule ID:** `SV-215234r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The nosuid mount option causes the system to not execute setuid files with owner privileges. This option must be used for mounting any file system not containing approved setuid files. Executing setuid files from untrusted file systems, or file systems not containing approved setuid files, increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of NFS file systems that contain approved "setuid" or "setgid" files from the ISSO/ISSM. Check the "nosuid" mount option is used on all NFS file systems that do not contain approved "setuid" or "setgid" files: # mount | grep -E "options|nfs|---" node mounted mounted over vfs date options -------- --------------- --------------- ------ ------------ --------------- ausgsa.ibm.com /gsa/ausgsa/projects/a/aix/71 /mnt_1 nfs3 Nov 05 14:11 ro,bg,hard,intr,nosuid,sec=sys ausgsa.ibm.com /gsa/ausgsa/projects/a/aix/72 /mnt_2 nfs3 Nov 05 14:12 ro,bg,hard,intr,sec=sys If the NFS mounts do not show the "nosuid" setting in their "options" fields, along with other mount options, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215235`

### Rule: AIX removable media, remote file systems, and any file system not containing approved device files must be mounted with the nodev option.

**Rule ID:** `SV-215235r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The nodev (or equivalent) mount option causes the system to not handle device files as system devices. This option must be used for mounting any file system not containing approved device files. Device files can provide direct access to system hardware and can compromise security if not protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify any file system mounted from removable media, network shares, or file systems not containing any approved device files: # cat /etc/filesystems /: dev = /dev/hd4 vfs = jfs2 log = /dev/hd8 mount = automatic check = false type = bootfs vol = root free = true /home: dev = /dev/hd1 vol = "/home" mount = true check = true free = false vfs = jfs2 log = /dev/hd8 10.17.76.74:/opt/nfs /home/doejohn vfs = nfs log = /dev/hd8 mount = true options = nodev account = false If any file system mounted from removable media, network shares, or file systems not containing any approved device files is not using the "nodev" option, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-215236`

### Rule: AIX must produce audit records containing information to establish what the date, time, and type of events that occurred.

**Rule ID:** `SV-215236r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in AIX audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if audit is turned on by running the following command: # audit query | grep -i auditing auditing on The command should yield the following output: auditing on If the command shows "auditing off", this is a finding. The log file can be set by the "trail" variable in /etc/security/audit/config. # grep trail /etc/security/audit/config trail = /audit/trail Note: The default log file is "/audit/trail". Use the following command to display the audit events: # /usr/sbin/auditpr -i <audit log file> -helRtcp event login status time command process --------------- -------- ----------- ------------------------ ------------------------------- -------- PROC_Delete root OK Wed Oct 31 23:01:37 2018 audit 9437656 FILE_Close root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Open root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Read root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Close root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 PROC_Create root OK Wed Oct 31 23:01:44 2018 ksh 12976466 FILE_Close root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Open root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Read root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Close root OK Wed Oct 31 23:01:44 2018 ksh 9437658 PROC_Execute root OK Wed Oct 31 23:01:44 2018 ls 9437658 FILE_Open root OK Wed Oct 31 23:01:44 2018 ls 9437658 If event type is not displayed, this is a finding. More information on the command options used above: -e the audit event. -l the login name of the user. -R the audit status. -t the time the record was written. -c the command name. -p the process ID.

## Group: SRG-OS-000039-GPOS-00017

**Group ID:** `V-215237`

### Rule: AIX must produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-215237r958416_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as operating system components, modules, device identifiers, node names, file names, and functionality. Associating information about where the event occurred within AIX provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify audit event detailed information is displayed: The log file can be set by the "trail" variable in /etc/security/audit/config. # grep trail /etc/security/audit/config trail = /audit/trail Note: The default log file is /audit/trail. Use the following command to display the audit events: # /usr/sbin/auditpr -i <audit log file> -v event login status time command wpar name --------------- -------- ----------- ------------------------ ------------------ ------------- ------------------------- FS_Chdir root OK Sat Aug 26 19:31:37 2017 ps Global change current directory to: /dev FS_Chdir root OK Sat Aug 26 19:31:47 2017 ps Global change current directory to: /dev FS_Chdir root OK Sat Aug 26 19:31:57 2017 ps Global change current directory to: /dev FS_Chdir root OK Sat Aug 26 19:32:07 2017 ps Global change current directory to: /dev FS_Chdir root OK Sat Aug 26 19:32:17 2017 ps Global change current directory to: /dev If event detailed information is not displayed, this is a finding. More information on the command options used above: - v detailed information for the event

## Group: SRG-OS-000040-GPOS-00018

**Group ID:** `V-215238`

### Rule: AIX must produce audit records containing information to establish the source and the identity of any individual or process associated with an event.

**Rule ID:** `SV-215238r958418_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event. In addition to logging where events occur within AIX, AIX must also generate audit records that identify sources of events. Sources of operating system events include, but are not limited to, processes and services. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event. Satisfies: SRG-OS-000040-GPOS-00018, SRG-OS-000255-GPOS-00096</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit event "process id" is displayed: The log file can be set by the "trail" variable in /etc/security/audit/config. # grep trail /etc/security/audit/config trail = /audit/trail Note: The default log file is /audit/trail. Use the following command to display the audit events: # /usr/sbin/auditpr -i <audit log file> -helRtcp event login status time command process --------------- -------- ----------- ------------------------ ------------------ ------------- -------- PROC_Delete root OK Wed Oct 31 23:01:37 2018 audit 9437656 FILE_Close root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Open root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Read root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Close root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 PROC_Create root OK Wed Oct 31 23:01:44 2018 ksh 12976466 FILE_Close root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Open root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Read root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Close root OK Wed Oct 31 23:01:44 2018 ksh 9437658 PROC_Execute root OK Wed Oct 31 23:01:44 2018 ls 9437658 FILE_Open root OK Wed Oct 31 23:01:44 2018 ls 9437658 If user id or process id is not displayed, this is a finding. More information on the command options used above: -e the audit event. -l the login name of the user. -R the audit status. -t the time the record was written. -c the command name. -p the process ID.

## Group: SRG-OS-000041-GPOS-00019

**Group ID:** `V-215239`

### Rule: AIX must produce audit records containing information to establish the outcome of the events.

**Rule ID:** `SV-215239r958420_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit event "status" is displayed: The log file can be set by the "trail" variable in /etc/security/audit/config. # grep trail /etc/security/audit/config trail = /audit/trail Note: The default log file is /audit/trail. Use the following command to display the audit events: # /usr/sbin/auditpr -i <audit log file> -helRtcp event login status time command process --------------- -------- ----------- ------------------------ ------------------ ------------- -------- PROC_Delete root OK Wed Oct 31 23:01:37 2018 audit 9437656 FILE_Close root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Open root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Read root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 FILE_Close root OK Wed Oct 31 23:01:37 2018 auditbin 12255562 PROC_Create root OK Wed Oct 31 23:01:44 2018 ksh 12976466 FILE_Close root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Open root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Read root OK Wed Oct 31 23:01:44 2018 ksh 9437658 FILE_Close root OK Wed Oct 31 23:01:44 2018 ksh 9437658 PROC_Execute root OK Wed Oct 31 23:01:44 2018 ls 9437658 FILE_Open root OK Wed Oct 31 23:01:44 2018 ls 9437658 If audit status is not displayed, this is a finding. More information on the command options used above: -e the audit event. -l the login name of the user. -R the audit status. -t the time the record was written. -c the command name. -p the process ID.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-215240`

### Rule: AIX must produce audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-215240r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit daemon is configured for full-text recording of privileged commands: The log file can be set by the "trail" variable in /etc/security/audit/config. # grep trail /etc/security/audit/config trail = /audit/trail Note: The default log file is /audit/trail. Use the following command to display the audit events: # /usr/sbin/auditpr -i <audit log file> -v event login status time command wpar name --------------- -------- ----------- ------------------------ ------------------ ------------- ------------------------- S_PASSWD_READ root OK Sat Aug 26 19:35:00 2017 cron Global audit object read event detected /etc/security/passwd S_PASSWD_READ root OK Sat Aug 26 19:35:00 2017 cron Global audit object read event detected /etc/security/passwd CRON_Start root OK Sat Aug 26 19:35:00 2017 cron Global event = start cron job cmd = /usr/sbin/dumpctrl -k >/dev/null 2>/dev/nul l time = Sat Aug 26 19:35:00 2017 FS_Chdir root OK Sat Aug 26 19:35:00 2017 cron Global change current directory to: / If the full-text recording of privileged command is not displayed, this is a finding. More information on the command options used above: - v detailed information for the event

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-215241`

### Rule: AIX must be configured to generate an audit record when 75% of the audit file system is full.

**Rule ID:** `SV-215241r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if "freespace" is configured for the audit subsystem: # grep -E freespace* /etc/security/audit/config freespace = 65536 If the above command returns empty, or if the value is less than 25% of the filesystem size, this is a finding.

## Group: SRG-OS-000054-GPOS-00025

**Group ID:** `V-215242`

### Rule: AIX must provide the function to filter audit records for events of interest based upon all audit fields within audit records, support on-demand reporting requirements, and an audit reduction function that supports on-demand audit review and analysis and after-the-fact investigations of security incidents.

**Rule ID:** `SV-215242r958430_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to specify the event criteria that are of interest provides the individuals reviewing the logs with the ability to quickly isolate and identify these events without having to review entries that are of little or no consequence to the investigation. Without this capability, forensic investigations are impeded. Events of interest can be identified by the content of specific audit record fields, including, for example, identities of individuals, event types, event locations, event times, event dates, system resources involved, IP addresses involved, or information objects accessed. Organizations may define audit event criteria to any degree of granularity required, for example, locations selectable by general networking location (e.g., by network or subnetwork) or selectable by specific information system component. The ability to generate on-demand reports, including after the audit data has been subjected to audit reduction, greatly facilitates the organization's ability to generate incident reports as needed to better handle larger-scale or more complex security incidents. The ability to perform on-demand audit review and analysis, including after the audit data has been subjected to audit reduction, greatly facilitates the organization's ability to generate incident reports, as needed, to better handle larger-scale or more complex security incidents. If the audit reduction capability does not support after-the-fact investigations, it is difficult to establish, correlate, and investigate the events leading up to an outage or attack, or identify those responses for one. This capability is also required to comply with applicable Federal laws and DoD policies. Audit reduction is a process that manipulates collected audit information and organizes such information in a summary format that is more meaningful to analysts. The report generation capability provided by the application must support on-demand (i.e., customizable, ad hoc, and as-needed) reports. This requires operating systems to provide the capability to customize audit record reports based on all available criteria. Satisfies: SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The application file "/usr/sbin/auditselect" provides the audit filtering function. Check if it exists: # ls -l /usr/sbin/auditselect -r-sr-x--- 1 root audit 36240 Jul 4 1776 /usr/sbin/auditselect If the "/usr/sbin/auditselect" file does not exist, this is a finding

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-215243`

### Rule: Audit logs on the AIX system must be owned by root.

**Rule ID:** `SV-215243r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the log files under the audit logging directory have correct ownership. The default log file is /audit/trail. The log file can be set by the "trail" variable in /etc/security/audit/config. # grep trail /etc/security/audit/config trail = /audit/trail # ls -l <auditlog dir> total 240 -rw-rw---- 1 root system 0 Feb 23 08:44 bin1 -rw-rw---- 1 root system 0 Feb 23 08:44 bin2 -rw-r----- 1 root system 116273 Feb 23 08:44 trail If any file's ownership is not "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-215244`

### Rule: Audit logs on the AIX system must be group-owned by system.

**Rule ID:** `SV-215244r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the log files under the audit logging directory have correct group ownership. The default log file is /audit/trail. The log file can be set by the "trail" variable in /etc/security/audit/config. # grep trail /etc/security/audit/config trail = /audit/trail # ls -l <auditlog dir> total 240 -rw-rw---- 1 root system 0 Feb 23 08:44 bin1 -rw-rw---- 1 root system 0 Feb 23 08:44 bin2 -rw-r----- 1 root system 116273 Feb 23 08:44 trail If any file's group ownership is not "system", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-215245`

### Rule: Audit logs on the AIX system must be set to 660 or less permissive.

**Rule ID:** `SV-215245r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the log files under the audit logging directory have correct permissions. The default log file is /audit/trail. The log file can be set by the "trail" variable in /etc/security/audit/config. # grep trail /etc/security/audit/config trail = /audit/trail # ls -l <auditlog dir> total 240 -rw-rw---- 1 root system 0 Feb 23 08:44 bin1 -rw-rw---- 1 root system 0 Feb 23 08:44 bin2 -rw-r----- 1 root system 116273 Feb 23 08:44 trail If any file has a mode more permissive than "660", this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-215246`

### Rule: AIX must provide audit record generation functionality for DoD-defined auditable events.

**Rule ID:** `SV-215246r1013689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which AIX will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful login attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logins from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions. Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000004-GPOS-00004, SRG-OS-000051-GPOS-00024, SRG-OS-000064-GPOS-00033, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000277-GPOS-00107, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000327-GPOS-00127, SRG-OS-000327-GPOS-00127, SRG-OS-000364-GPOS-00151, SRG-OS-000392-GPOS-00172, SRG-OS-000458-GPOS-00203, SRG-OS-000461-GPOS-00205, SRG-OS-000462-GPOS-00206, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209, SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000468-GPOS-00212, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218, SRG-OS-000474-GPOS-00219, SRG-OS-000475-GPOS-00220, SRG-OS-000476-GPOS-00221, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that auditing is properly configured. Run the "stig_audit_check.sh" script. If any results are returned from the script, this is a finding. Verify that the file "/etc/security/audit/objects" includes the following objects: /etc/security/environ: w = "S_ENVIRON_WRITE" /etc/security/group: w = "S_GROUP_WRITE" /etc/group: w = "S_GROUP_WRITE" /etc/security/limits: w = "S_LIMITS_WRITE" /etc/security/login.cfg: w = "S_LOGIN_WRITE" /etc/security/passwd: r = "S_PASSWD_READ" w = "S_PASSWD_WRITE" /etc/security/user: w = "S_USER_WRITE" /etc/security/audit/config: w = "AUD_CONFIG_WR" If any of the objects listed above are missing from "/etc/security/audit/objects", this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-215247`

### Rule: AIX must start audit at boot.

**Rule ID:** `SV-215247r991555_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the start-up process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if /etc/rc contains the following line: /usr/sbin/audit start # grep "audit start" /etc/rc /usr/sbin/audit start If a result is not returned, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-215248`

### Rule: AIX audit tools must be owned by root.

**Rule ID:** `SV-215248r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the following audit tools are owned by "root": /usr/sbin/audit /usr/sbin/auditbin /usr/sbin/auditcat /usr/sbin/auditconv /usr/sbin/auditmerge /usr/sbin/auditpr /usr/sbin/auditselect /usr/sbin/auditstream /usr/sbin/auditldap # ls -l /usr/sbin/audit*|grep -v ldap -r-sr-x--- 1 root audit 64926 Mar 30 2016 /usr/sbin/audit -r-sr-x--- 1 root audit 41240 Mar 30 2016 /usr/sbin/auditbin -r-sr-x--- 1 root audit 40700 Mar 30 2016 /usr/sbin/auditcat -r-sr-x--- 1 root audit 13072 Mar 30 2016 /usr/sbin/auditconv -r-sr-x--- 1 root audit 11328 Mar 30 2016 /usr/sbin/auditmerge -r-sr-x--- 1 root audit 53466 Mar 30 2016 /usr/sbin/auditpr -r-sr-x--- 1 root audit 33128 Mar 30 2016 /usr/sbin/auditselect -r-sr-x--- 1 root audit 29952 Mar 30 2016 /usr/sbin/auditstream -r-x------ 1 root security 12204 Mar 30 2016 /usr/sbin/auditldap If any above file's ownership is not "root", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-215249`

### Rule: AIX audit tools must be group-owned by audit.

**Rule ID:** `SV-215249r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the following audit tools are group-owned by "audit": /usr/sbin/audit /usr/sbin/auditbin /usr/sbin/auditcat /usr/sbin/auditconv /usr/sbin/auditmerge /usr/sbin/auditpr /usr/sbin/auditselect /usr/sbin/auditstream # ls -l /usr/sbin/audit*|grep -v ldap -r-sr-x--- 1 root audit 64926 Mar 30 2016 /usr/sbin/audit -r-sr-x--- 1 root audit 41240 Mar 30 2016 /usr/sbin/auditbin -r-sr-x--- 1 root audit 40700 Mar 30 2016 /usr/sbin/auditcat -r-sr-x--- 1 root audit 13072 Mar 30 2016 /usr/sbin/auditconv -r-sr-x--- 1 root audit 11328 Mar 30 2016 /usr/sbin/auditmerge -r-sr-x--- 1 root audit 53466 Mar 30 2016 /usr/sbin/auditpr -r-sr-x--- 1 root audit 33128 Mar 30 2016 /usr/sbin/auditselect -r-sr-x--- 1 root audit 29952 Mar 30 2016 /usr/sbin/auditstream If any above file's are not group-owned by "audit", this is a finding. Verify that "/usr/sbin/auditldap" group-owned by "security": # ls -l /usr/sbin/auditldap -r-x------ 1 root security 12204 Mar 30 2016 /usr/sbin/auditldap If the group-owner of "/usr/sbin/auditldap" is not "security", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-215250`

### Rule: AIX audit tools must be set to 4550 or less permissive.

**Rule ID:** `SV-215250r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the following audit tools are set to "4550" or less permissive: /usr/sbin/audit /usr/sbin/auditbin /usr/sbin/auditcat /usr/sbin/auditconv /usr/sbin/auditmerge /usr/sbin/auditpr /usr/sbin/auditselect /usr/sbin/auditstream # ls -l /usr/sbin/audit*|grep -v ldap -r-sr-x--- 1 root audit 64926 Mar 30 2016 /usr/sbin/audit -r-sr-x--- 1 root audit 41240 Mar 30 2016 /usr/sbin/auditbin -r-sr-x--- 1 root audit 40700 Mar 30 2016 /usr/sbin/auditcat -r-sr-x--- 1 root audit 13072 Mar 30 2016 /usr/sbin/auditconv -r-sr-x--- 1 root audit 11328 Mar 30 2016 /usr/sbin/auditmerge -r-sr-x--- 1 root audit 53466 Mar 30 2016 /usr/sbin/auditpr -r-sr-x--- 1 root audit 33128 Mar 30 2016 /usr/sbin/auditselect -r-sr-x--- 1 root audit 29952 Mar 30 2016 /usr/sbin/auditstream If any above file's permission is greater than "4550", this is a finding. Verify that "/usr/sbin/auditldap" is set to "500" or less permissive: # ls -l /usr/sbin/auditldap -r-x------ 1 root security 12204 Mar 30 2016 /usr/sbin/auditldap If the permission of "/usr/sbin/auditldap" is greater than "500", this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-215251`

### Rule: AIX must verify the hash of audit tools.

**Rule ID:** `SV-215251r991567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed in order to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Trusted Execution (TE) is "on" and "CHKEXEC" is "on" by running the following command: # trustchk -p TE=ON CHKEXEC=ON CHKSHLIB=OFF CHKSCRIPT=OFF CHKKERNEXT=OFF STOP_UNTRUSTD=OFF STOP_ON_CHKFAIL=OFF LOCK_KERN_POLICIES=OFF TSD_FILES_LOCK=OFF TSD_LOCK=OFF TEP=OFF TLP=OFF If the result show "TE=OFF" or "CHKEXEC=OFF", this is a finding. Verify that TSD (Trusted Signature Database) contains all the audit tools and their signatures by running the following command: # awk '/\/usr\/sbin\/audit/ {print; for(i=1; i<=10; i++) {getline; print}}' /etc/security/tsd/tsd.dat |grep -E "\/usr\/sbin\/audit|cert_tag|signature|hash_value" /usr/sbin/auditselect: cert_tag = 00d3cbd2922627b209 signature = 8f6044a166ad7d1256a2798432dcb06b528eb6c515f4d2d0af90dd17e6ba05665bd8d39ee8f15e8872e90d3b52e0e25c7be9d62c9c5d71cd16b662fb8511f168b6facb4105cc0e9c19c316e37459ad739b75b6037827f3ba60896eeeec62cf47e7514b10d4813c48cacd76b75dc5b0e1a87f7cd10552992021efb5b44eb33a1a hash_value = 002e02eda12663a2c9478e1b5154cc97452c07a68a8b9d5a6ca3408b008d95bb /usr/sbin/auditstream: cert_tag = 00d3cbd2922627b209 signature = 3d5a678962b684208f3996262a997d8838012c1625d83b7df75d9bb3a83065819ae476a21ada2ec7afd683828d9ce5c9d3eb829ed907d11fc2713d895419cbec5855e96b4a3b36a4f5b3c44a801555727b1ca799026262120b18fe2d93f53da8e95f6560c0cf5ea73dccd7daa9ec3df7e24ede0201b9d632becfb58a8f81fee4 hash_value = 5c434a89bf2fb50a2c21734a5ecd3c4e0a92c34d6685633d59a93caf1684e515 /usr/sbin/auditpr: cert_tag = 00d3cbd2922627b209 signature = 8356f57d227a85037620ec6f357204a9dd3ceeb89fab2ea8b4dea5529a37d290e111a46e9deca8ebd86b37c50b8b2d27599d09a02353081db9f7140780ace0d9986c8f7265d3d91eed7a2502050a6342c79cf1fd6c9b2633e353fdc3603de3b6fc341b2b7a0c6eb286155ae9542bdbbcc29eba84a50f1f8c4f6f5924403f6556 hash_value = 34bf3b145327d33f810e939d15ae084711dcd0eb7e7f3ebcb135f5ff7b3ba776 /usr/sbin/auditcat: cert_tag = 00d3cbd2922627b209 signature = abf001ee98c5e81ec730552cd26473221ee14694a7fea06d97ae030f1b8603bafdb3f4917cb50c87c90fc8ff03e8762b05c6b21d1907a05288736fa820fd4a05d38f236fec5cfc3813aeb5b0618294effe0356ac26be0e6701398cf181fb38897c5a2496154bba3eab513caaa74a9abb230ad6948190d24907a107d8968a0c27 hash_value = 78febbeb1e7e4ca1ed4015fb147d27bd451814ed8c81429b42ee9e2f8301bf58 /usr/sbin/auditbin: cert_tag = 00d3cbd2922627b209 signature = 9bb3fde97a70dd3ee93ecf556cf13e3981d1f0794c7a253701e011956574754eb17922525092f38a3b0f9375aef8fadfe3cb6e47f6aa7424e3449910af6cc6e1754f6fe8c2fb20867af7f9a048485ea2dfcd7b8f718d350d21ec2ffe394423f4c513b22ff9a654f1ef55f6e679424ad0e630404fcfd707ed91d542d64564c601 hash_value = 2deb07bbdf5b744168bb9484b25c0e61813b546f0dd0555d9b9ebcb8cf17272d /usr/sbin/auditldap: cert_tag = 00d3cbd2922627b209 signature = ab3ea5ba592ef8d1576f632c6154e10a172fbdad1c6379954a48d76bd2c365848a208dfa698e828008fa73b60daf0ad0ab9ad08035f9df2d39ac21a67873cfac3eb07103858903c47e5d1e264ace01de9599ff3c966b12d8cbc6c2b6e3c97f8c56b7a5a4fa33f15bbe472319266854f83fad57917d9dd0c09383fd2b5df41e6d hash_value = f929ca078995a6b2a28d1247e9837e03d06fa2c5b12a6c86e679201192694c8c /usr/sbin/auditconv: cert_tag = 00d3cbd2922627b209 signature = ab7a0e0e5aa62ec741db601cc1609bf7db6006705a3d6b7001b3aa4da5ab6bcfecea569d6891b67088b2033045fdf6532a24433711c74fcffc92744884f0f14211a7625c168f11d4b3de2e7083e57a5063933c0eea5b92c6ab9ea1b131ca8fe85143f616887e4d60cfb534da8b3a920c428279ea8eee04bf57ad70da3c69104c hash_value = 0d2a989fa77df6984348f5c66d20af1e71aebd5a0d9f85551873563ee9d851d7 /usr/sbin/audit: cert_tag = 00d3cbd2922627b209 signature = 2b6ed42788eca469aaaf960d4ea9956793182cdbf6b8570ded724762701354f62d003a3ed99db9b4fbb670c5864c9a641d485083789840c71005bbdcc4659dbbfbec0e8c63c8223be9e54f46240e3a5ebed8647fbd9e0e9f2db0d046e0cd73e72c87977c9dc394b61027c2856a27db0e51afb05e07c2d4f8ea3bc33564f2e7a6 hash_value = 0c5d10f7c7cefec133bee45bd0d30933b18041438a7c7b15b8aa7de60ce208af /usr/sbin/auditmerge: cert_tag = 00d3cbd2922627b209 signature = 64e0f95c1efa90f34b6ddd370fc0a277db2858b01b993a2f32eb9f0c86e6d901675f67f42158015ceafa37507a0bc36bbd58aca6685464f8b43edb099db670aa497db349c51fc0ed6066da43e2eb5529af8bbdd0c30b66b22158261c224213fc406ffee36e4df476107f867d8f7c09c24e4318a13e2b279d200a9fa4a8b515e4 hash_value = 6b4a1d1288a1d7e987ad14b395d0067890574a09956171bb32b9a022dc975015 If any of the cert_tag, signature, or hash values is missing or “= VOLATILE", this is a finding.

## Group: SRG-OS-000337-GPOS-00129

**Group ID:** `V-215252`

### Rule: AIX must provide the function for assigned ISSOs or designated SAs to change the auditing to be performed on all operating system components, based on all selectable event criteria in near real time.

**Rule ID:** `SV-215252r971541_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If authorized individuals do not have the ability to modify auditing parameters in response to a changing threat environment, the organization may not be able to effectively respond, and important forensic information may be lost. This requirement enables organizations to extend or limit auditing as necessary to meet organizational requirements. Auditing that is limited to conserve information system resources may be extended to address certain threat situations. In addition, auditing may be limited to a specific set of events to facilitate audit reduction, analysis, and reporting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit admin role has been configured to include the authorizations for auditing, namely "aix.security.audit,aix.security.user.audit,aix.security.role.audit": # lsrole ALL |grep "aix.security.audit" |grep "aix.security.user.audit" |grep "aix.security.role.audit" auditadm authorizations=aix.security.audit,aix.security.user.audit,aix.security.role.audit rolelist= groups= visibility=1 screens=* dfltmsg=Audit Administrator msgcat=role_desc.cat msgnum=15 msgset=1 auth_mode=INVOKER id=16 If the above command has no output, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-215253`

### Rule: AIX must allocate audit record storage capacity to store at least one weeks worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-215253r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of AIX.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the file system size where the log file resides is greater than the organizationally defined size of audit logs for one week (1GB). Find out where the audit log resides: # grep trail /etc/security/audit/config trail = /audit/trail Find out the available space in the file system hosting the audit logs. # df /audit/trail Filesystem 512-blocks Free %Used Iused %Iused Mounted on /dev/hd4 1966080 1792872 9% 3913 2% / If the "512-blocks" multiplied by "Free" is less than the required size for the audit logs, this is a finding.

## Group: SRG-OS-000350-GPOS-00138

**Group ID:** `V-215254`

### Rule: AIX must provide a report generation function that supports on-demand audit review and analysis, on-demand reporting requirements, and after-the-fact investigations of security incidents.

**Rule ID:** `SV-215254r958770_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The report generation capability must support on-demand review and analysis in order to facilitate the organization's ability to generate incident reports, as needed, to better handle larger-scale or more complex security incidents. If the report generation capability does not support after-the-fact investigations, it is difficult to establish, correlate, and investigate the events leading up to an outage or attack, or identify those responses for one. This capability is also required to comply with applicable Federal laws and DoD policies. Report generation must be capable of generating on-demand (i.e., customizable, ad hoc, and as-needed) reports. On-demand reporting allows personnel to report issues more rapidly to more effectively meet reporting requirements. Collecting log data and aggregating it to present the data in a single, consolidated report achieves this objective. Satisfies: SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if the application for generating audit reports exists ("/usr/sbin/auditpr"): # ls -l /usr/sbin/auditpr -r-sr-x--- 1 root audit 54793 Feb 14 2017 /usr/sbin/auditpr If the file does not exist, this is a finding.

## Group: SRG-OS-000359-GPOS-00146

**Group ID:** `V-215255`

### Rule: AIX must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-215255r958788_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by AIX include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the time zone setting by the following command: # echo $TZ UTC If the result is not UTC, GMT, or an offset from UTC, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215256`

### Rule: AIX audit logs must be rotated daily.

**Rule ID:** `SV-215256r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Rotate audit logs daily to preserve audit file system space and to conform to the DoD/DISA requirement. If it is not rotated daily and moved to another location, then there is more of a chance for the compromise of audit data by malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for any "crontab" entries that rotate audit logs: # crontab -l 30 23 * * * /root/logrotate.sh #Daily log rotation script If such a cron job is found, this is not a finding. Otherwise, query the SA. If there is a process automatically rotating audit logs, this is not a finding. If the SA manually rotates audit logs, this is a finding. If the audit output is not archived daily, to tape or disk, this is a finding. Review the audit log directory. If more than one file is there, or if the file does not have today's date, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-215257`

### Rule: The AIX rexec daemon must not be running.

**Rule ID:** `SV-215257r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The exec service is used to execute a command sent from a remote server. The username and passwords are passed over the network in clear text and therefore insecurely. Unless required the rexecd daemon will be disabled. This function, if required, should be facilitated through SSH.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the "rexec" daemon is running by running the following command: # grep "^exec[[:blank:]]" /etc/inetd.conf If the above grep command returned a line that contains "rexecd", this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-215258`

### Rule: AIX telnet daemon must not be running.

**Rule ID:** `SV-215258r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This telnet service is used to service remote user connections. This is historically the most commonly used remote access method for UNIX servers. The username and passwords are passed over the network in clear text and therefore insecurely. Unless required the telnetd daemon will be disabled. This function, if required, should be facilitated through SSH.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the "telnet" daemon is running by running the following command: # grep -v '^#' /etc/inetd.conf | grep telnet If an entry is returned, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-215259`

### Rule: AIX ftpd daemon must not be running.

**Rule ID:** `SV-215259r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The ftp service is used to transfer files from or to a remote machine. The username and passwords are passed over the network in clear text and therefore insecurely. Remote file transfer, if required, should be facilitated through SSH.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the "ftp" daemon is running by running the following command: # grep "^ftp[[:blank:]]" /etc/inetd.conf If an entry is returned like the following line, the "ftp" daemon is running: ftp stream tcp6 nowait root /usr/sbin/ftpd ftpd If the above grep command returned a line that contains "ftpd", this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-215260`

### Rule: AIX must remove NOPASSWD tag from sudo config files.

**Rule ID:** `SV-215260r1009545_rule`
**Severity:** high

**Description:**
<VulnDiscussion>sudo command does not require reauthentication if NOPASSWD tag is specified in /etc/sudoers config file, or sudoers files in /etc/sudoers.d/ directory. With this tag in sudoers file, users are not required to reauthenticate for privilege escalation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If sudo is not used on AIX, this is Not Applicable. Run the following command to find the "NOPASSWD" tag in "/etc/sudoers" file: # grep NOPASSWD /etc/sudoers If there is a "NOPASSWD" tag found in "/etc/sudoers" file, this is a finding. Run the following command to find the "NOPASSWD" tag in one of the sudo config files in "/etc/sudoers.d/" directory: # find /etc/sudoers.d -type f -exec grep -l NOPASSWD {} \; The above command displays all sudo config files that are in "/etc/sudoers.d/" directory and they contain the "NOPASSWD" tag. If above command found a config file that is in "/etc/sudoers.d/" directory and contains the "NOPASSWD" tag, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-215261`

### Rule: AIX must remove !authenticate option from sudo config files.

**Rule ID:** `SV-215261r1009546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>sudo command does not require reauthentication if !authenticate option is specified in /etc/sudoers config file, or config files in /etc/sudoers.d/ directory. With this tag in sudoers, users are not required to reauthenticate for privilege escalation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If sudo is not used on AIX, this is Not Applicable. Run the following command to find "!authenticate" option in "/etc/sudoers" file: # grep "!authenticate" /etc/sudoers If there is a "!authenticate" option found in "/etc/sudoers" file, this is a finding. Run the following command to find "!authenticate" option in one of the sudo config files in "/etc/sudoers.d/" directory: # find /etc/sudoers.d -type f -exec grep -l "!authenticate" {} \; The above command displays all sudo config files that are in "/etc/sudoers.d/" directory and they contain the "!authenticate" option. If above command found a config file that is in "/etc/sudoers.d/" directory and that contains the "!authenticate" option, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215262`

### Rule: AIX must be configured with a default gateway for IPv4 if the system uses IPv4, unless the system is a router.

**Rule ID:** `SV-215262r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a system has no default gateway defined, the system is at increased risk of man-in-the-middle, monitoring, and Denial of Service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for an IPv4 default route using command: # netstat -r |grep default default 10.11.20.1 UG 1 1811 en0 - - If a default route is not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215263`

### Rule: IP forwarding for IPv4 must not be enabled on AIX unless the system is a router.

**Rule ID:** `SV-215263r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP forwarding permits the kernel to forward packets from one network interface to another. The ability to forward packets between two networks is only appropriate for systems acting as routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command: # no -o ipforwarding ipforwarding = 0 If the value returned is not "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215264`

### Rule: AIX must be configured with a default gateway for IPv6 if the system uses IPv6 unless the system is a router.

**Rule ID:** `SV-215264r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a system has no default gateway defined, the system is at increased risk of man-in-the-middle, monitoring, and Denial of Service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is a router, this is Not Applicable. If the system does not use IPv6, this is Not Applicable. Determine if the system has a default route configured for IPv6 by running: # netstat -r | grep default default 10.11.20.1 UG 1 1823 en0 - - If a default route is not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215265`

### Rule: AIX must not have IP forwarding for IPv6 enabled unless the system is an IPv6 router.

**Rule ID:** `SV-215265r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system is configured for IP forwarding and is not a designated router, it could be used to bypass network security by providing a path for communication not filtered by network devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command: # /usr/sbin/no -o ip6forwarding ip6forwarding = 0 If the value returned is not "0", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-215266`

### Rule: AIX log files must be owned by a system account.

**Rule ID:** `SV-215266r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify AIX or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the owner of log files: # ls -lL /var/log /var/log/syslog /var/adm /var/adm: total 376 drw-r----- 2 root system 256 Jan 24 12:31 SRC drwx------ 4 root system 256 Jan 24 07:28 config -rw-r----- 1 root system 1081 Jan 24 09:05 dev_pkg.fail -rw-r----- 1 root system 250 Jan 24 09:05 dev_pkg.success -rw------- 1 root system 64 Jan 24 09:43 sulog drwxr-xr-x 3 root system 256 Jan 24 12:28 sw drwx------ 2 root system 256 Jan 24 08:06 wpars -rw-r----- 1 adm adm 7517448 Apr 29 14:10 wtmp /var/log: total 8 drwxr-xr-x 2 root system 256 Jan 24 08:44 aso -rw-r----- 1 root system 603 Jan 24 10:30 cache_mgt.dr.log If any of the log files are not owned by a system account, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-215267`

### Rule: AIX log files must be owned by a system group.

**Rule ID:** `SV-215267r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify AIX or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group of log files: # ls -lL /var/log /var/log/syslog /var/adm /var/adm: total 376 drw-r----- 2 root system 256 Jan 24 12:31 SRC drwx------ 4 root system 256 Jan 24 07:28 config -rw-r----- 1 root system 1081 Jan 24 09:05 dev_pkg.fail -rw-r----- 1 root system 250 Jan 24 09:05 dev_pkg.success -rw------- 1 root system 64 Jan 24 09:43 sulog drwxr-xr-x 3 root system 256 Jan 24 12:28 sw drwx------ 2 root system 256 Jan 24 08:06 wpars -rw-r----- 1 adm adm 7517448 Apr 29 14:10 wtmp /var/log: total 8 drwxr-xr-x 2 root system 256 Jan 24 08:44 aso -rw-r----- 1 root system 603 Jan 24 10:30 cache_mgt.dr.log If any of the log files have group other than a system group, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-215268`

### Rule: AIX system files, programs, and directories must be group-owned by a system group.

**Rule ID:** `SV-215268r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permissions will protect the files from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of system files, programs, and directories run the following command: # ls -lLa /etc /bin /usr/bin /usr/lbin /usr/ucb /sbin /usr/sbin If any system file, program, or directory is not group-owned by a system group, this is a finding. Note: For this check, the system-provided "ipsec" group is also acceptable.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215269`

### Rule: The inetd.conf file on AIX must be owned by root.

**Rule ID:** `SV-215269r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of sensitive files or utilities to system groups may provide unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of "/etc/inetd.conf": # ls -al /etc/inetd.conf The above command should yield the following output: -rw-r----- root system 993 Mar 11 07:04 /etc/inetd.conf If the file is not owned by root, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215270`

### Rule: AIX cron and crontab directories must be owned by root or bin.

**Rule ID:** `SV-215270r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incorrect ownership of the cron or crontab directories could permit unauthorized users the ability to alter cron jobs and run automated jobs as privileged users. Failure to give ownership of cron or crontab directories to root or to bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the owner of the "crontab" directory using command: # ls -ld /var/spool/cron/crontabs drwxrwx--- 2 bin cron 256 Jan 25 12:33 /var/spool/cron/crontabs If the owner of the "crontab" directory is not "root" or "bin", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215271`

### Rule: AIX audio devices must be group-owned by root, sys, bin, or system.

**Rule ID:** `SV-215271r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without privileged group owners, audio devices will be vulnerable to being used as eaves-dropping devices by malicious users or intruders to possibly listen to conversations containing sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group owner of audio devices using commands: # /usr/sbin/lsdev -C | grep -i audio aud0 Available USB Audio Device # ls -lL /dev/*aud0 cr--r--r-- 1 root system 16, 0 Jan 24 07:25 aud0 If the group owner of an audio device is not "root", "sys", "bin", or "system", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215272`

### Rule: AIX time synchronization configuration file must be owned by root.

**Rule ID:** `SV-215272r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not owned by a system account, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of /etc/ntp.conf using command: # ls -al /etc/ntp.conf The above command should yield the following output: -rw-r----- 1 root system 993 Aug 25 18:26 /etc/ntp.conf If the file is not owned by root, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215273`

### Rule: AIX time synchronization configuration file must be group-owned by bin, or system.

**Rule ID:** `SV-215273r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not owned by a system group, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check "/etc/ntp.conf" file group ownership: # ls -al /etc/ntp.conf The above command should yield the following output: -rw-r----- 1 root system 993 Aug 25 18:26 /etc/ntp.conf If the file is not group-owned by "system", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215274`

### Rule: The AIX /etc/group file must be owned by root.

**Rule ID:** `SV-215274r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/group" file is owned by "root" using command: # ls -l /etc/group The above command should yield the following output: -rw-r--r-- 1 root security 387 Sep 06 11:40 /etc/group If the file is not owned by "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215275`

### Rule: The AIX /etc/group file must be group-owned by security.

**Rule ID:** `SV-215275r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/group" file is group-owned by "security" using command: # ls -l /etc/group The above command should yield the following output: -rw-r--r-- 1 root security 387 Sep 06 11:40 /etc/group If the file is not group-owned by "security", this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215276`

### Rule: All AIX interactive users home directories must be owned by their respective users.

**Rule ID:** `SV-215276r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System binaries are executed by privileged users as well as system services, and restrictive permissions are necessary to ensure that their execution of these programs cannot be co-opted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of each user's home directory listed in the "/etc/passwd file": # cut -d: -f6 /etc/passwd | xargs ls -lLd drwxr-xr-x 21 root system 4096 Jan 29 09:58 / drwxr-xr-x 4 bin bin 45056 Jan 24 12:31 /bin drwxr-xr-x 2 doejohn staff 256 Jan 25 13:18 /home/doejohn drwxr-xr-x 2 sshd system 256 Aug 11 2017 /home/srvproxy drwx------ 2 root system 256 Jan 30 12:54 /root drwxrwxr-x 4 bin bin 256 Mar 23 2017 /usr/sys drwxrwxr-x 15 root adm 4096 Jan 24 12:26 /var/adm drwxr-xr-x 6 root system 4096 Jan 24 07:34 /var/adm/invscout drwxr-xr-x 8 esaadmin system 256 Jan 24 09:02 /var/esa If any user's home directory is not owned by the assigned user, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215277`

### Rule: All AIX interactive users home directories must be group-owned by the home directory owner primary group.

**Rule ID:** `SV-215277r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of the home directory is not the same as the GID of the user, this would allow unauthorized access to files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership for each user in the "/etc/passwd" file using command: # cut -d: -f6 /etc/passwd | xargs ls -lLd drwxr-xr-x 21 root system 4096 Jan 29 09:58 / drwxr-xr-x 4 bin bin 45056 Jan 24 12:31 /bin drwxr-xr-x 2 doejohn staff 256 Jan 25 13:18 /home/doejohn drwxr-xr-x 2 sshd system 256 Aug 11 2017 /home/srvproxy drwx------ 2 root system 256 Jan 30 12:54 /root drwxrwxr-x 4 bin bin 256 Mar 23 2017 /usr/sys drwxrwxr-x 15 root adm 4096 Jan 24 12:26 /var/adm drwxr-xr-x 6 root system 4096 Jan 24 07:34 /var/adm/invscout drwxr-xr-x 8 esaadmin system 256 Jan 24 09:02 /var/esa If any user's home directory is not group-owned by the assigned user's primary group, this is a finding. Home directories for application accounts requiring different group ownership must be documented using site-defined procedures.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215278`

### Rule: All files and directories contained in users home directories on AIX must be group-owned by a group in which the home directory owner is a member.

**Rule ID:** `SV-215278r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of the home directory is not the same as the GID of the user, this would allow unauthorized access to files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of user home directories for files group-owned by a group of which the home directory's owner is not a member. List the user accounts: # cut -d : -f 1 /etc/passwd root daemon bin sys adm uucp nobody invscout snapp ipsec srvproxy esaadmin sshd doejohn dirtjoe For each user account, get a list of group names for files in the user's home directory: # find < users home directory > -exec ls -lLd {} \; Obtain the list of group names associated with the user's account: # lsuser -a groups < user name > doejohn groups=staff Check the group name lists: # cat /etc/group system:!:0:root,srvproxy,esaadmin staff:!:1:ipsec,srvproxy,esaadmin,sshd,doejohn bin:!:2:root,bin sys:!:3:root,bin,sys adm:!:4:bin,adm mail:!:6: security:!:7:root cron:!:8:root audit:!:10:root ecs:!:28: nobody:!:4294967294:nobody,lpd usr:!:100:dirtjoe perf:!:20: shutdown:!:21: invscout:!:12:invscout snapp:!:13:snapp ipsec:!:200: sshd:!:201:sshd If there are group names in the file list not present in the user list, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-215279`

### Rule: AIX library files must have mode 0755 or less permissive.

**Rule ID:** `SV-215279r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized access could destroy the integrity of the library files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of library files by running the following command: # ls -lLR /usr/lib /lib If any of the library files have a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215280`

### Rule: Samba packages must be removed from AIX.

**Rule ID:** `SV-215280r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the smbpasswd file has a mode more permissive than 0600, the smbpasswd file may be maliciously accessed or modified, potentially resulting in the compromise of Samba accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check if samba packages are installed on AIX: # lslpp -l samba* If the above command shows that samba packages are installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215281`

### Rule: AIX time synchronization configuration file must have mode 0640 or less permissive.

**Rule ID:** `SV-215281r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. File permissions more permissive than 0640 for time synchronization configuration file may allow access and change the config file by system intruders or malicious users, could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the mode of the ntp.conf file: # ls -l /etc/ntp.conf The above command should yield the following output: -rw-r----- 1 root system 993 Aug 25 18:26 /etc/ntp.conf If the mode is more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215282`

### Rule: The AIX /etc/group file must have mode 0644 or less permissive.

**Rule ID:** `SV-215282r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/group" file has the mode "0644" using command: # ls -l /etc/group The above command should yield the following output: -rw-r--r-- 1 root security 387 Sep 06 11:40 /etc/group If the file does not have mode "0644" or less permissive, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215283`

### Rule: AIX must encrypt user data at rest using AIX Encrypted File System (EFS) if it is required.

**Rule ID:** `SV-215283r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The AIX Encrypted File System (EFS) is a J2 filesystem-level encryption through individual key stores. This allows for file encryption in order to protect confidential data from attackers with physical access to the computer. User authentication and access control lists can protect files from unauthorized access (even from root user) while the operating system is running. Operating systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000405-GPOS-00184, SRG-OS-000404-GPOS-00183</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization does not require to encrypt the data at rest, this is Not Applicable. Check if "clic.rte" fileset is installed: # lslpp -l |grep clic The above command should yield the following output: clic.rte.kernext 4.10.0.1 COMMITTED CryptoLite for C Kernel clic.rte.lib 4.10.0.1 COMMITTED CryptoLite for C Library clic.rte.kernext 4.10.0.1 COMMITTED CryptoLite for C Kernel If the "clic.rte.lib", or the "clic.rte.kernext", fileset is not installed, this is a finding. To check if a JFS2 file system (mounted as /fs2_mnt) is EFS-enabled, use the following command: # lsfs -q /fs2_mnt Name Nodename Mount Pt VFS Size Options Auto Accounting /dev/fslv00 -- /fs2_mnt jfs2 262144 -- no no (lv size: 262144, fs size: 262144, block size: 4096, sparse files: yes, inline log: no, inline log size: 0, EAformat: v2, Quota: no, DMAPI: no, VIX: yes, EFS: no, ISNAPSHOT: no, MAXEXT: 0, MountGuard: no) If the above command shows "EFS: no", this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-215284`

### Rule: AIX must protect the confidentiality and integrity of transmitted information during preparation for transmission and maintain the confidentiality and integrity of information during reception and disable all non-encryption network access methods.

**Rule ID:** `SV-215284r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted or received information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check if SSH server package is installed: # lslpp -l | grep -i ssh openssh.base.client 6.0.0.6201 COMMITTED Open Secure Shell Commands openssh.base.server 6.0.0.6201 COMMITTED Open Secure Shell Server openssh.man.en_US 6.0.0.6201 COMMITTED Open Secure Shell If package "openssh.base.server" is not installed, this is a finding. Run the following command to check if the SSH daemon is running: # lssrc -s sshd | grep active sshd ssh 3670408 active If "sshd" is "inoperative", this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-215285`

### Rule: AIX must monitor and record successful remote logins.

**Rule ID:** `SV-215285r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the file "/var/adm/wtmp" is a symlink by using the following command: # ls -al /var/adm/wtmp The above command should yield the following output: -rw-rw-r-- 1 adm adm 45360 Sep 05 15:00 /var/adm/wtmp If the file "/var/adm/wtmp" is a symlink, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-215286`

### Rule: AIX must monitor and record unsuccessful remote logins.

**Rule ID:** `SV-215286r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the file "/etc/security/failedlogin" is a symlink by using the following command: # ls -al /etc/security/failedlogin The above command should yield the following output: -rw------- 1 root system 648 Sep 05 14:59 /etc/security/failedlogin If the file "/etc/security/failedlogin" is a symlink, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215287`

### Rule: On AIX, the SSH server must not permit root logins using remote access programs.

**Rule ID:** `SV-215287r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permitting direct root login reduces auditable information about who ran privileged commands on the system and also allows direct attack attempts on root's password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the SSH daemon is configured to disable root logins: # grep -iE "PermitRootLogin[[:blank:]]*no" /etc/ssh/sshd_config | grep -v \# If the above command displays a line, the root login is disabled. If the root login is not disabled, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215288`

### Rule: All AIX shells referenced in passwd file must be listed in /etc/shells file, except any shells specified for the purpose of preventing logins.

**Rule ID:** `SV-215288r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /etc/shells file lists approved default shells. It helps provide layered defense to the security approach by ensuring users cannot change their default shell to an unauthorized unsecure shell.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm the login shells referenced in the "/etc/passwd" file are listed in the "/etc/security/login.cfg" file's "shells =variable" in the usw stanza by running commands: # more /etc/security/login.cfg | grep shells | grep -v '*' shells = /bin/sh,/bin/bsh,/bin/csh,/bin/ksh,/bin/tsh,/bin/ksh93,/usr/bin/sh,/usr/bin/bsh,/usr/bin/csh,/usr/bin/ksh,/usr/bin/tsh # more /etc/shells /bin/csh /bin/ksh /bin/psh /bin/tsh /bin/bsh /usr/bin/csh /usr/bin/ksh /usr/bin/psh /usr/bin/tsh /usr/bin/bsh The "/usr/bin/false", "/bin/false", "/dev/null", "/sbin/nologin" (and equivalents), and "sdshell" will be considered valid shells for use in the "/etc/passwd" file, but will not be listed in the shells stanza. If a shell referenced in "/etc/passwd" is not listed in the shells stanza, excluding the above mentioned shells, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-215289`

### Rule: The AIX SSH server must use SSH Protocol 2.

**Rule ID:** `SV-215289r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command: # grep ^Protocol /etc/ssh/sshd_config The above command should yield the following output: Protocol 2 If the above command does not show the ssh server supporting "Protocol 2" only, this is a finding.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-215290`

### Rule: AIX must config the SSH idle timeout interval.

**Rule ID:** `SV-215290r958636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific operating system functionality where the system owner, data owner, or organization requires additional assurance. Satisfies: SRG-OS-000163-GPOS-00072</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check if "ClientAliveInterval" and "ClientAliveCountMax" are set for SSH server: # grep -E "^ClientAliveInterval|^ClientAliveCountMax" /etc/ssh/sshd_config ClientAliveInterval 600 ClientAliveCountMax 0 If "ClientAliveCountMax" is not set or its value is not "0", this is a finding. If "ClientAliveInterval" is not set, or its value is not "600" (10-minutes) or less, this is a finding.

## Group: SRG-OS-000365-GPOS-00152

**Group ID:** `V-215291`

### Rule: AIX must disable Kerberos Authentication in ssh config file to enforce access restrictions.

**Rule ID:** `SV-215291r1009547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the application configuration, it will be difficult to identify attempted attacks and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the Kerberos authentication setting: # grep -i KerberosAuthentication /etc/ssh/sshd_config | grep -v '^#' If the setting is present and set to "yes", this is a finding.

## Group: SRG-OS-000373-GPOS-00158

**Group ID:** `V-215292`

### Rule: If GSSAPI authentication is not required on AIX, the SSH daemon must disable GSSAPI authentication.

**Rule ID:** `SV-215292r1009548_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through SSH exposes the system's GSSAPI to remote hosts, increasing the attack surface of the system. GSSAPI authentication must be disabled unless needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if GSSAPI authentication is used for SSH authentication to the system. If so, this is not applicable. Check the SSH daemon configuration for the GSSAPI authentication setting: # grep -i GSSAPIAuthentication /etc/ssh/sshd_config | grep -v '^#' GSSAPIAuthentication no If the setting is not set to "no", this is a finding.

## Group: SRG-OS-000384-GPOS-00167

**Group ID:** `V-215293`

### Rule: AIX must setup SSH daemon to disable revoked public keys.

**Rule ID:** `SV-215293r1009549_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without configuring a local cache of revocation data, there is the potential to allow access to users who are no longer authorized (users with revoked certificates).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If public keys are not used for SSH authentication, this is Not Applicable. Run the following command: # grep "^RevokedKeys" /etc/ssh/sshd_config RevokedKeys /etc/ssh/RevokedKeys.txt If the command does not find the "RevokedKeys" setting, or the value for "RevokedKeys" is set to "none", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215294`

### Rule: AIX SSH daemon must be configured to only use Message Authentication Codes (MACs) employing FIPS 140-2 approved cryptographic hash algorithms.

**Rule ID:** `SV-215294r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD information systems are required to use FIPS 140-2 approved cryptographic hash functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed MACs by running the following command: # grep -i macs /etc/ssh/sshd_config | grep -v '^#' MACs hmac-sha1,hmac-sha1-96,hmac-sha2-256,hmac-sha2-256-96,hmac-sha2-512,hmac-sha2-512-96 If no lines are returned, or the returned MAC list contains any MAC that is not FIPS 140-2 approved, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215295`

### Rule: The AIX SSH daemon must be configured for IP filtering.

**Rule ID:** `SV-215295r1009551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SSH daemon must be configured for IP filtering to provide a layered defense against connection attempts from unauthorized addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the installed version of OpenSSH is 6.7 or above, this requirement is not applicable. Check the TCP wrappers configuration files to determine if SSHD is configured to use TCP wrappers using commands: # grep sshd /etc/hosts.deny sshd : ALL # grep sshd /etc/hosts.allow sshd : 10.10.20.* If no entries are returned, the TCP wrappers are not configured for SSHD, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215296`

### Rule: The AIX SSH daemon must not allow compression.

**Rule ID:** `SV-215296r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in an SSH connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection, potentially with root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the installed version of OpenSSH is 7.4 or above, this requirement is not applicable. Check the SSH daemon configuration for the Compression setting by running: # grep -i Compression /etc/ssh/sshd_config | grep -v '^#' Compression no If the setting is not present, or it is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215297`

### Rule: AIX must turn on SSH daemon privilege separation.

**Rule ID:** `SV-215297r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH daemon privilege separation causes the SSH process to drop root privileges when not needed, which would decrease the impact of software vulnerabilities in the unprivileged section.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the "UsePrivilegeSeparation" setting using command: # grep -i UsePrivilegeSeparation /etc/ssh/sshd_config | grep -v '^#' UsePrivilegeSeparation yes If the setting is not present or the setting is "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215298`

### Rule: AIX must turn on SSH daemon reverse name checking.

**Rule ID:** `SV-215298r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If reverse name checking is off, SSH may allow a remote attacker to circumvent security policies and attempt to or actually login from IP addresses that are not permitted to access resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the "VerifyReverseMapping" setting using command: # grep -i VerifyReverseMapping /etc/ssh/sshd_config | grep -v '^#' VerifyReverseMapping yes If the setting is not present or the setting is "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215299`

### Rule: AIX SSH daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-215299r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log into the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the "StrictModes" setting using command: # grep -i StrictModes /etc/ssh/sshd_config | grep -v '^#' StrictModes yes If the setting is missing or is set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215300`

### Rule: AIX must turn off X11 forwarding for the SSH daemon.

**Rule ID:** `SV-215300r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>X11 forwarding over SSH allows for the secure remote execution of X11-based applications. This feature can increase the attack surface of an SSH connection and should not be enabled unless needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If X11 forwarding has been authorized for use, this is Not Applicable. Check the SSH daemon configuration for the "X11Forwarding" directive using command: # grep -i X11Forwarding /etc/ssh/sshd_config | grep -v '^#' X11Forwarding no If the setting is not present or the setting is "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215301`

### Rule: AIX must turn off TCP forwarding for the SSH daemon.

**Rule ID:** `SV-215301r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH TCP connection forwarding provides a mechanism to establish TCP connections proxied by the SSH server. This function can provide similar convenience to a Virtual Private Network (VPN) with the similar risk of providing a path to circumvent firewalls and network ACLs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If TCP forwarding is approved for use by the ISSO, this is not applicable. Check the SSH daemon configuration for the "AllowTcpForwarding" directive using command: # grep -i AllowTcpForwarding /etc/ssh/sshd_config | grep -v '^#' AllowTcpForwarding no If the setting is not present or the setting is "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-215302`

### Rule: The AIX SSH daemon must be configured to disable empty passwords.

**Rule ID:** `SV-215302r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When password authentication is allowed, PermitEmptyPasswords specifies whether the server allows login to accounts with empty password strings. If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed empty passwords using command: # grep -i PermitEmptyPasswords /etc/ssh/sshd_config | grep -v '^#' PermitEmptyPasswords no If no lines are returned, or the returned "PermitEmptyPasswords" directive contains "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-215303`

### Rule: The AIX SSH daemon must be configured to disable user .rhosts files.

**Rule ID:** `SV-215303r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trust .rhost file means a compromise on one host can allow an attacker to move trivially to other hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed ".rhosts" using command: # grep -i IgnoreRhosts /etc/ssh/sshd_config | grep -v '^#' IgnoreRhosts yes If no lines are returned, or the returned "IgnoreRhosts" directive is not set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-215304`

### Rule: The AIX SSH daemon must be configured to not use host-based authentication.

**Rule ID:** `SV-215304r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed host-based authentication using command: # grep -i HostbasedAuthentication /etc/ssh/sshd_config | grep -v '^#' HostbasedAuthentication no If no lines are returned, or the returned "HostbasedAuthentication" directive contains "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-215305`

### Rule: The AIX SSH daemon must not allow RhostsRSAAuthentication.

**Rule ID:** `SV-215305r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SSH permits rhosts RSA authentication, a user may be able to log in based on the keys of the host originating the request and not any user-specific authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for the "RhostsRSAAuthentication" setting by running: # grep -i RhostsRSAAuthentication /etc/ssh/sshd_config | grep -v '^#' The above command should yield the following output: RhostsRSAAuthentication no If the setting is present and set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-215306`

### Rule: If AIX SSH daemon is required, the SSH daemon must only listen on the approved listening IP addresses.

**Rule ID:** `SV-215306r991593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SSH daemon should only listen on the approved listening IP addresses. Otherwise the SSH service could be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check if "ListenAddress" is defined in SSH config file: # grep -i ListenAddress /etc/ssh/sshd_config | grep -v '^#' ListenAddress 10.17.76.74 If no configuration is returned, or if a returned listen configuration contains addresses not permitted, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215308`

### Rule: AIX system must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-215308r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This prevents attackers with physical access from trivially bypassing security on the machine and gaining root access. Such accesses are further prevented by configuring the bootloader password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "root" account has a password assigned: # cut -d: -f1,2 /etc/passwd | grep root root:! If the "root" account is not listed with an "!", this is a finding.

## Group: SRG-OS-000281-GPOS-00111

**Group ID:** `V-215309`

### Rule: If bash is used, AIX must display logout messages.

**Rule ID:** `SV-215309r958640_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If a user cannot explicitly end an operating system session, the session may remain open and be exploited by an attacker; this is referred to as a zombie session. Users need to be aware of whether or not the session has been terminated. Information resources to which users gain access via authentication include, for example, local workstations and remote services. Logoff messages can be displayed after authenticated sessions have been terminated. However, for some types of interactive sessions, including, for example, remote login, information systems typically send logoff messages as final messages prior to terminating sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify any users that are using the BASH shell: # cut -d: -f1,7 /etc/passwd | grep -i bash doejohn:/bin/bash If no users are assigned the BASH shell, this is Not Applicable Verify that each BASH shell user has a ".bash_logout" file: # for home in `cut -d: -f6 /etc/passwd`; do ls -alL $home/.bash_logout; done -rwxr----- 1 doejohn staff 297 Jan 29 09:47 /home/doejohn/.bash_logout If a user does not have their ".bash_logout" file, this is a finding. Verify that each ".bash_logout" file identified above contains a logout message: # cat <user_home_directory>/.bash_logout echo "You are being disconnected." sleep 5 If the ".bash_logout" file is not configured to display a logout message, this is a finding.

## Group: SRG-OS-000281-GPOS-00111

**Group ID:** `V-215310`

### Rule: If Bourne / ksh shell is used, AIX must display logout messages.

**Rule ID:** `SV-215310r958640_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If a user cannot explicitly end an operating system session, the session may remain open and be exploited by an attacker; this is referred to as a zombie session. Users need to be aware of whether or not the session has been terminated. Information resources to which users gain access via authentication include, for example, local workstations and remote services. Logoff messages can be displayed after authenticated sessions have been terminated. However, for some types of interactive sessions, including, for example, remote login, information systems typically send logoff messages as final messages prior to terminating sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify users have a ".logout" file in their home directory: # for home in `cut -d: -f6 /etc/passwd`; do ls -alL $home/.logout; done -rwxr----- 1 root system 297 Jan 29 09:47 /root/.logout -rwxr----- 1 doejohn staff 297 Jul 4 00:47 /home/doejohn/.logout If an interactive user does not have their ".logout" file, this is a finding. Verify that each ".logout" file identified above contains a logout message: # cat <user_home_directory>/.logout echo "You are being disconnected." sleep 5 If the ".logout" file does not display a logout message, this is a finding. Verify each users' ".profile" file calls "$HOME/.logout" while logging out: # grep "trap '$HOME/.logout' EXIT " <user_home_directory>/.profile trap '$HOME/.logout' EXIT If the ".profile" file does not call "$HOME/.logout", this is a finding.

## Group: SRG-OS-000281-GPOS-00111

**Group ID:** `V-215311`

### Rule: If csh/tcsh shell is used, AIX must display logout messages.

**Rule ID:** `SV-215311r958640_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If a user cannot explicitly end an operating system session, the session may remain open and be exploited by an attacker; this is referred to as a zombie session. Users need to be aware of whether or not the session has been terminated. Information resources to which users gain access via authentication include, for example, local workstations and remote services. Logoff messages can be displayed after authenticated sessions have been terminated. However, for some types of interactive sessions, including, for example, remote login, information systems typically send logoff messages as final messages prior to terminating sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if users have their "$HOME/.logout" files. If a user does not have their ".logout" file, or the ".logout" file does not display a logout message, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215312`

### Rule: AIX must implement a remote syslog server that is documented using site-defined procedures.

**Rule ID:** `SV-215312r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a remote log host is in use and it has not been justified and documented, sensitive information could be obtained by unauthorized users without the administrator’s knowledge. Satisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "syslog.conf" file for any references to remote log hosts using command: # grep -v "^#" /etc/syslog.conf | grep '@' @<loghost> Ask ISSO/SA for a list of valid remote syslog servers justified and documented using site-defined procedures. Destination locations beginning with "@" represent log hosts. If the log host name is a local alias, such as log host, consult the "/etc/hosts" or other name databases as necessary to obtain the canonical name or address for the log host. Determine if the host referenced is a syslog host documented using site-defined procedures. If a loghost is not defined, not documented, or is commented out this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215313`

### Rule: The AIX syslog daemon must not accept remote messages unless it is a syslog server documented using site-defined procedures.

**Rule ID:** `SV-215313r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unintentionally running a syslog server accepting remote messages puts the system at increased risk. Malicious syslog messages sent to the server could exploit vulnerabilities in the server software itself, could introduce misleading information in to the system's logs, or could fill the system's storage leading to a Denial of Service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "syslogd" is running with the "-R" option using command: # ps -ef | grep syslogd | grep -v grep The above command should yield the following output: root 4063356 3342368 0 Sep 11 - 0:01 /usr/sbin/syslogd -R If the "-R" option is not present with the syslogd process, this is a finding.

## Group: SRG-OS-000365-GPOS-00152

**Group ID:** `V-215314`

### Rule: AIX must be configured to use syslogd to log events by TCPD.

**Rule ID:** `SV-215314r1009552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the application configuration, it will be difficult to identify attempted attacks and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Normally, TCPD logs to the "mail" facility in "/etc/syslog.conf". Determine if syslog is configured to log events by TCPD. Procedure: # more /etc/syslog.conf Look for entries similar to the following: mail.debug /var/adm/maillog mail.none /var/adm/maillog mail.* /var/log/mail auth.info /var/log/messages The above entries would indicate mail alerts are being logged. If no entries for "mail" exist, then TCPD is not logging and this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-215315`

### Rule: The AIX audit configuration files must be owned by root.

**Rule ID:** `SV-215315r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that all the audit configuration files under /etc/security/audit/* have correct ownership. # ls -l /etc/security/audit/* -rw-r----- 1 root audit 37 Oct 10 2016 /etc/security/audit/bincmds -rw-r----- 1 root audit 2838 Sep 05 16:33 /etc/security/audit/config -rw-r----- 1 root audit 26793 Oct 10 2016 /etc/security/audit/events -rw-r----- 1 root audit 340 Oct 10 2016 /etc/security/audit/objects -rw-r----- 1 root audit 54 Oct 10 2016 /etc/security/audit/streamcmds If any file's ownership is not "root", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-215316`

### Rule: The AIX audit configuration files must be group-owned by audit.

**Rule ID:** `SV-215316r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that all the audit configuration files under /etc/security/audit/* have group ownership. # ls -l /etc/security/audit/* -rw-r----- 1 root audit 37 Oct 10 2016 /etc/security/audit/bincmds -rw-r----- 1 root audit 2838 Sep 05 16:33 /etc/security/audit/config -rw-r----- 1 root audit 26793 Oct 10 2016 /etc/security/audit/events -rw-r----- 1 root audit 340 Oct 10 2016 /etc/security/audit/objects -rw-r----- 1 root audit 54 Oct 10 2016 /etc/security/audit/streamcmds If any file's group ownership is not "audit", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-215317`

### Rule: The AIX audit configuration files must be set to 640 or less permissive.

**Rule ID:** `SV-215317r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that all the audit configuration files under /etc/security/audit/* have correct permissions. # ls -l /etc/security/audit/* -rw-r----- 1 root audit 37 Oct 10 2016 /etc/security/audit/bincmds -rw-r----- 1 root audit 2838 Sep 05 16:33 /etc/security/audit/config -rw-r----- 1 root audit 26793 Oct 10 2016 /etc/security/audit/events -rw-r----- 1 root audit 340 Oct 10 2016 /etc/security/audit/objects -rw-r----- 1 root audit 54 Oct 10 2016 /etc/security/audit/streamcmds If any file has a mode more permissive than "640", this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-215318`

### Rule: AIX must automatically lock after 15 minutes of inactivity in the CDE Graphical desktop environment.

**Rule ID:** `SV-215318r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If CDE (X11) is not used on AIX, this is Not Applicable. From the command prompt, run the following script: for file in /usr/dt/config/*/sys.resources; do etc_file=`echo $file | sed -e s/usr/etc/` echo "\nChecking config file "$etc_file"..." if [[ ! -f $etc_file ]]; then echo "Missing config file "$etc_file else cat $etc_file |grep 'dtsession\*saverTimeout:' cat $etc_file |grep 'dtsession\*lockTimeout:' fi done The above script should yield the following output: Checking config file /etc/dt/config/C/sys.resources... Missing config file /etc/dt/config/C/sys.resources Checking config file /etc/dt/config/POSIX/sys.resources... dtsession*saverTimeout: 15 dtsession*lockTimeout: 30 Checking config file /etc/dt/config/en_US/sys.resources... dtsession*saverTimeout: 15 dtsession*lockTimeout: 25 If the result of the script shows any config file missing, or any of the "dtsession*saverTimeout" or "dtsession*lockTimeout" values are greater than "15", this is a finding.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-215320`

### Rule: AIX must set inactivity time-out on login sessions and terminate all login sessions after 10 minutes of inactivity.

**Rule ID:** `SV-215320r1009553_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. If a maintenance session or connection remains open after maintenance is completed, it may be hijacked by an attacker and used to compromise or damage the system. Some maintenance and test tools are either standalone devices with their own operating systems or are applications bundled with an operating system. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific operating system functionality where the system owner, data owner, or organization requires additional assurance. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at AIX level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that AIX terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000279-GPOS-00109, SRG-OS-000163-GPOS-00072, SRG-OS-000126-GPOS-00066</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if "TMOUT" and "TIMEOUT" environment variables are set to "600" (in seconds) in "/etc/profile" file: # grep -E " TMOUT|TIMEOUT" /etc/profile readonly TMOUT=600; readonly TIMEOUT=600; export TMOUT TIMEOUT If they are not set in "/etc/profile" file, are commented out, or their values are greater than "600", this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-215321`

### Rule: AIX SSH private host key files must have mode 0600 or less permissive.

**Rule ID:** `SV-215321r958450_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions for SSH private host key files: # ls -lL /etc/ssh/*key The above command should yield the following output: -rw------- 1 root system 668 Jan 18 2017 /etc/ssh/ssh_host_dsa_key -rw------- 1 root system 227 Jan 18 2017 /etc/ssh/ssh_host_ecdsa_key -rw------- 1 root system 965 Jan 18 2017 /etc/ssh/ssh_host_key -rw------- 1 root system 1675 Jan 18 2017 /etc/ssh/ssh_host_rsa_key If any file has a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-215322`

### Rule: AIX must disable /usr/bin/rcp,
/usr/bin/rlogin,
/usr/bin/rsh, /usr/bin/rexec and /usr/bin/telnet commands.

**Rule ID:** `SV-215322r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The listed applications permit the transmission of passwords in plain text. Alternative applications such as SSH, which encrypt data, should be use instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following commands: # ls -l /usr/bin/rcp | awk '{print $1}' # ls -l /usr/bin/rlogin | awk '{print $1}' # ls -l /usr/bin/rsh | awk '{print $1}' # ls -l /usr/bin/telnet | awk '{print $1}' # ls -l /usr/bin/rexec | awk '{print $1}' Each of the above commands should return with the following permissions: ---------- If the permissions are more permissive, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-215323`

### Rule: AIX log files must have mode 0640 or less permissive.

**Rule ID:** `SV-215323r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify AIX or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of log files: # ls -lL /var/log /var/log/syslog /var/adm /var/adm: total 376 drw-r----- 2 root system 256 Jan 24 12:31 SRC drwx------ 4 root system 256 Jan 24 07:28 config -rw-r----- 1 root system 1081 Jan 24 09:05 dev_pkg.fail -rw-r----- 1 root system 250 Jan 24 09:05 dev_pkg.success -rw------- 1 root system 64 Jan 24 09:43 sulog drwxr-xr-x 3 root system 256 Jan 24 12:28 sw drwx------ 2 root system 256 Jan 24 08:06 wpars /var/log: total 8 drwxr-xr-x 2 root system 256 Jan 24 08:44 aso -rw-r----- 1 root system 603 Jan 24 10:30 cache_mgt.dr.log If any of the log files have modes more permissive than "0640", this is a finding. NOTE: Do not confuse system logfiles with audit logs. Any subsystems that require less stringent permissions must be documented.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-215324`

### Rule: AIX log files must not have extended ACLs, except as needed to support authorized software.

**Rule ID:** `SV-215324r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify AIX or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the system administrator, identify all of the system log files. For each system log file identified, verify that extended ACL's are disabled: #aclget <system_log_file> * * ACL_type AIXC * attributes: base permissions owner(root): rw- group(system): r-- others: r-- extended permissions disabled If "extended permissions" is set to "enabled" and is not documented, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-215325`

### Rule: All system command files must not have extended ACLs.

**Rule ID:** `SV-215325r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting permissions will protect system command files from unauthorized modification. System command files include files present in directories used by the operating system for storing default system executables and files present in directories included in the system's default executable search paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all system command files have no extended ACLs by running the following commands: # aclget /etc # aclget /bin # aclget /usr/bin # aclget /usr/lbin # aclget /usr/ucb # aclget /sbin # aclget /usr/sbin If any of the command files have extended permissions enabled, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-215326`

### Rule: All library files must not have extended ACLs.

**Rule ID:** `SV-215326r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized access could destroy the integrity of the library files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following system library directories need to be checked: /usr/lib/security/ /usr/lib/methods/ Determine if any system library file has an extended ACL by running the follow script: find /usr/lib/security /usr/lib/methods/ -type f | while read file do aclget -o /tmp/111.acl $file > /dev/null 2>&1 if [ $? -eq 0 ]; then grep -e "[[:space:]]enabled$" /tmp/111.acl > /dev/null 2>&1 if [ $? -eq 0 ]; then echo "$file has ACL" fi fi done If the above script yield any output, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215327`

### Rule: AIX passwd.nntp file must have mode 0600 or less permissive.

**Rule ID:** `SV-215327r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File permissions more permissive than 0600 for /etc/news/passwd.nntp may allow access to privileged information by system intruders or malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If NNTP is not being used, this is Not Applicable. Check passwd.nntp file permissions using command: # find / -name passwd.nntp -exec ls -lL {} \; The above command may yield the following output: -rw------- 1 root system 19 Oct 16 10:46 /etc/news/passwd.nntp If a "passwd.nntp" file has a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215328`

### Rule: The AIX /etc/group file must not have an extended ACL.

**Rule ID:** `SV-215328r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ACL of the "/etc/group" file: # aclget /etc/group The above command should yield the following output: * * ACL_type AIXC * attributes: base permissions owner(root): rw- group(security): r-- others: r-- extended permissions disabled If the extended ACL are not "disabled", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215329`

### Rule: The AIX ldd command must be disabled.

**Rule ID:** `SV-215329r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ldd command provides a list of dependent libraries needed by a given binary, which is useful for troubleshooting software. Instead of parsing the binary file, some ldd implementations invoke the program with a special environment variable set, which causes the system dynamic linker to display the list of libraries. Specially crafted binaries can specify an alternate dynamic linker which may cause a program to be executed instead of examined. If the program is from an untrusted source, such as in a user home directory, or a file suspected of involvement in a system compromise, unauthorized software may be executed with the rights of the user running ldd.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult vendor documentation concerning the "ldd" command. If the command provides protection from the execution of untrusted executables, this is not a finding. Determine the location of the system's "ldd" command: # find / -name ldd If no file exists, this is not a finding. Check the permissions of the found "ldd" file: # ls -lL <path to ldd> ---------- 1 bin bin 6289 Feb 28 2017 /usr/bin/ldd If the file mode of the file is more permissive than "0000", this is a finding

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215330`

### Rule: AIX NFS server must be configured to restrict file system access to local hosts.

**Rule ID:** `SV-215330r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The NFS access option limits user access to the specified level. This assists in protecting exported file systems. If access is not restricted, unauthorized hosts may be able to access the system's NFS exports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions on exported NFS file systems by running command: # exportfs -v /export/shared -ro,access=10.17.76.74 If the exported file systems do not contain the "rw" or "ro" options specifying a list of hosts or networks, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215331`

### Rule: All AIX users home directories must have mode 0750 or less permissive.

**Rule ID:** `SV-215331r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on home directories allow unauthorized access to user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the home directory mode of each interactive user in "/etc/passwd": #cut -d : -f 6 /etc/passwd | xargs -n1 ls -ld | more drwxr-xr-x 20 root system 4096 Jan 28 13:46 / drwxr-xr-x 33 root system 8192 Jan 28 13:51 /etc lrwxrwxrwx 1 bin bin 8 Jan 24 07:23 /bin -> /usr/bin drwxrwxr-x 4 bin bin 256 Mar 23 2017 /usr/sys drwxrwxr-x 15 root adm 4096 Jan 24 12:26 /var/adm drwxr-xr-x 2 root sys 4096 Jan 24 08:43 /usr/lib/uucp drwxr-xr-x 6 root system 4096 Jan 24 07:34 /var/adm/invscout drwxr-xr-x 3 ipsec ipsec 256 Jan 24 08:43 /etc/ipsec drwxr-xr-x 2 sshd system 256 Aug 11 2017 /home/srvproxy drwxr-xr-x 8 esaadmin system 256 Jan 24 09:02 /var/esa drwxr-x--- 2 doejohn staff 256 Jan 25 13:18 /home/doejohn If an interactive user's home directory's mode is more permissive than "0750", this is a finding. NOTE: Application directories are allowed and may need "0755" permissions (or greater) for correct operation.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215332`

### Rule: The AIX user home directories must not have extended ACLs.

**Rule ID:** `SV-215332r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on home directories allow unauthorized access to user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify user home directories have no extended ACLs using command: # cat /etc/passwd | cut -f 6,6 -d ":" | xargs -n1 aclget * * ACL_type AIXC * attributes: base permissions owner(root): rwx group(system): r-x others: r--- extended permissions disabled If extended permissions are not disabled, this is a finding.

## Group: SRG-OS-000312-GPOS-00124

**Group ID:** `V-215333`

### Rule: AIX must use Trusted Execution (TE) Check policy.

**Rule ID:** `SV-215333r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to show the current status of the "TE", "CHKEXEC", and "CHKKERNEXT" on the system: # trustchk -p 2>&1 | egrep -e "TE=|CHKEXEC|CHKKERNEXT" The above command should yield the following output: TE=ON CHKEXEC=ON CHKKERNEXT=ON If "TE", "CHKEXEC", or "CHKKERNEXT" is "OFF", this is a finding.

## Group: SRG-OS-000365-GPOS-00152

**Group ID:** `V-215334`

### Rule: AIX must disable trivial file transfer protocol.

**Rule ID:** `SV-215334r1009554_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the application configuration, it will be difficult to identify attempted attacks and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^tftp[[:blank:]]" /etc/inetd.conf If there is any output from the command, it is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-215335`

### Rule: AIX must employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs.

**Rule ID:** `SV-215335r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at AIX-level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles). The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. Verification of white-listed software occurs prior to execution or at system startup. This requirement applies to operating system programs, functions, and services designed to manage system processes and configurations (e.g., group policies). Satisfies: SRG-OS-000368-GPOS-00154, SRG-OS-000370-GPOS-00155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to show the current status of the "TE" running on the system: # trustchk -p The above command should yield the following output: TE=ON If the output is "TE=OFF", this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-215336`

### Rule: AIX must remove all software components after updated versions have been installed.

**Rule ID:** `SV-215336r958936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check any installed components that are in APPLY state: # lslpp -cl | grep :APPLIED: If the command returns any entries, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-215337`

### Rule: AIX must enforce a delay of at least 4 seconds between login prompts following a failed login attempt.

**Rule ID:** `SV-215337r991588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of login attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check the default "logindelay" value: # lssec -f /etc/security/login.cfg -s default -a logindelay The above command should yield the following output: default logindelay=4 If the above command displays the "logindelay" value less than "4", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215338`

### Rule: AIX system must restrict the ability to switch to the root user to members of a defined group.

**Rule ID:** `SV-215338r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring a supplemental group for users permitted to switch to the root user prevents unauthorized users from accessing the root account, even with knowledge of the root credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "sugroups" of the root user. Generally only users in the adm group should have su to root capacity. Run the following command: # lsuser -a sugroups root root sugroups=system,staff,security If "sugroups" is blank or "ALL", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215339`

### Rule: All AIX Group Identifiers (GIDs) referenced in the /etc/passwd file must be defined in the /etc/group file.

**Rule ID:** `SV-215339r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is assigned the GID of a group not existing on the system, and a group with that GID is subsequently created, the user may have unintended rights to the group.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that there are no GIDs referenced in "/etc/passwd" that are not defined in "/etc/group": # cut -d: -f4 /etc/passwd 0 1 2 3 4 203 204 # cut -d: -f3 /etc/group 0 1 2 3 4 203 204 If there are GID's listed in the "/etc/passwd" file that are not listed in the "/etc/group" file, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215340`

### Rule: All AIX files and directories must have a valid owner.

**Rule ID:** `SV-215340r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unowned files do not directly imply a security problem, but they are generally a sign that something is amiss. They may be caused by an intruder, by incorrect software installation or draft software removal, or by failure to remove all files belonging to a deleted account. The files should be repaired so they will not cause problems when accounts are created in the future, and the cause should be discovered and addressed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for files with no assigned owner using the following command: # find / -nouser -print If any files have no assigned owner, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215341`

### Rule: The sticky bit must be set on all public directories on AIX systems.

**Rule ID:** `SV-215341r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to set the sticky bit on public directories allows unauthorized users to delete files in the directory structure. The only authorized public directories are those temporary directories supplied with the system, or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system, and by users for temporary file storage - such as /tmp - and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all world-writable directories have the sticky bit set by running the command: # find / -type d -perm -002 ! -perm -1000 > wwlist # cat wwlist If any directories are listed in the "wwlist" file, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215342`

### Rule: The AIX global initialization files must contain the mesg -n or mesg n commands.

**Rule ID:** `SV-215342r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Command "mesg -n" allows only the root user the permission to send messages to your workstation to avoid having others clutter your display with incoming messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check global initialization files for the presence of "mesg n" command by running: # grep "mesg" /etc/profile /etc/environment /etc/security/environ /etc/security/.profile /etc/csh.login /etc/csh.cshrc /etc/profile:mesg n /etc/environment:mesg n If any global initialization file does not contain "mesg n", or it contains the "mesg y" command, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215343`

### Rule: The AIX hosts.lpd file must not contain a + character.

**Rule ID:** `SV-215343r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having the '+' character in the hosts.lpd (or equivalent) file allows all hosts to use local system print resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Look for the presence of a print service configuration file by running the following commands: # find /etc -name hosts.lpd -print # find /etc -name Systems -print # find /etc -name printers.conf If none of the files are found, this is not applicable. Otherwise, examine the configuration file by running: # more <print service file> | grep "+" @+hamlet +lear @+prospero If any lines are found that contain only a "+" character, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215344`

### Rule: AIX sendmail logging must not be set to less than nine in the sendmail.cf file.

**Rule ID:** `SV-215344r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Sendmail is not configured to log at level 9, system logs may not contain the information necessary for tracking unauthorized use of the sendmail service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if "Sendmail" logging is set to level "9" by running command: # grep "^O LogLevel" /etc/mail/sendmail.cf O LogLevel=9 If logging is set to less than "9", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215345`

### Rule: AIX run control scripts executable search paths must contain only absolute paths.

**Rule ID:** `SV-215345r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory or other relative paths, executables in these directories may be executed instead of system commands.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' library search paths by running: # grep -r PATH /etc/rc* /etc/rc:PATH=/usr/sbin:/usr/bin:/usr/ucb:/etc /etc/rc:export PATH ODMDIR /etc/rc.C2:export PATH=/usr/bin:/etc:/usr/sbin:/sbin:/usr/ucb /etc/rc.CC:export PATH=/usr/bin:/etc:/usr/sbin:/sbin:/usr/ucb /etc/rc.bsdnet:export PATH=/usr/bin:/usr/sbin:$PATH This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) or other than "$PATH", it is a relative path, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-215346`

### Rule: The AIX rsh daemon must be disabled.

**Rule ID:** `SV-215346r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The rsh daemon permits username and passwords to be passed over the network in clear text.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command: # grep -v "^#" /etc/inetd.conf |grep rshd The above command may show the daemon is enabled like this: shell stream tcp6 nowait root /usr/sbin/rshd rshd If the above grep command returned a line that contains "rshd", this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-215347`

### Rule: The AIX rlogind service must be disabled.

**Rule ID:** `SV-215347r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The rlogin daemon permits username and passwords to be passed over the network in clear text.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the "rlogind" service is running by running the following command: # grep -v "^#" /etc/inetd.conf |grep rlogin If the above grep command returned a line that contains "rlogin", this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215348`

### Rule: The AIX qdaemon must be disabled if local or remote printing is not required.

**Rule ID:** `SV-215348r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The qdaemon program is the printing scheduling daemon that manages the submission of print jobs to the piobe service. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # lsitab qdaemon If the command yields any output, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215349`

### Rule: If AIX system does not act as a remote print server for other servers, the lpd daemon must be disabled.

**Rule ID:** `SV-215349r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The lpd daemon accepts remote print jobs from other systems. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # lsitab lpd If the command yields any output, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215350`

### Rule: If AIX system does not support either local or remote printing, the piobe service must be disabled.

**Rule ID:** `SV-215350r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The piobe daemon is the I/O back end for the printing process, handling the job scheduling and spooling. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # lsitab piobe If the command yields any output, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215351`

### Rule: If there are no X11 clients that require CDE on AIX, the dt service must be disabled.

**Rule ID:** `SV-215351r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This entry executes the CDE startup script which starts the AIX Common Desktop Environment. To prevent attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # lsitab dt If the command yields any output, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215352`

### Rule: If NFS is not required on AIX, the NFS daemon must be disabled.

**Rule ID:** `SV-215352r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rcnfs entry starts the NFS daemons during system boot. NFS is a service with numerous historical vulnerabilities and should not be enabled unless there is no alternative. If NFS serving is required, then read-only exports are recommended and no filesystem or directory should be exported with root access. Unless otherwise required the NFS daemons (rcnfs) will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # lsitab rcnfs If the command yields any output, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215353`

### Rule: If sendmail is not required on AIX, the sendmail service must be disabled.

**Rule ID:** `SV-215353r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sendmail service has many historical vulnerabilities and, where possible, should be disabled. If the system is not required to operate as a mail server i.e. sending, receiving or processing e-mail, disable the sendmail daemon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/lib/sendmail" /etc/rc.tcpip If the above command produces any output, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215354`

### Rule: If SNMP is not required on AIX, the snmpd service must be disabled.

**Rule ID:** `SV-215354r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The snmpd daemon is used by many 3rd party applications to monitor the health of the system. This allows remote monitoring of network and server configuration. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there is no "snmpd" service running on the AIX by doing the following: From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/snmpd" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215355`

### Rule: The AIX DHCP client must be disabled.

**Rule ID:** `SV-215355r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The dhcpcd daemon receives address and configuration information from the DHCP server. DHCP relies on trusting the local network. If the local network is not trusted, then it should not be used. To prevent remote attacks this daemon should not be enabled unless there is no alternative. Satisfies: SRG-OS-000095-GPOS-00049, SRG-OS-000480-GPOS-00227</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the DHCP client is needed by the system and is documented, this is Not Applicable. Determine if the DHCP client is running: # ps -ef |grep dhcpcd If "dhcpcd" is running, this is a finding. Verify that DHCP is disabled on startup: # grep "^start[[:blank:]]/usr/sbin/dhcpcd" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215356`

### Rule: If DHCP is not enabled in the network on AIX, the dhcprd daemon must be disabled.

**Rule ID:** `SV-215356r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The dhcprd daemon listens for broadcast packets, receives them, and forwards them to the appropriate server. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/dhcprd" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215357`

### Rule: If IPv6 is not utilized on AIX server, the autoconf6 daemon must be disabled.

**Rule ID:** `SV-215357r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"autoconf6" is used to automatically configure IPv6 interfaces at boot time. Running this service may allow other hosts on the same physical subnet to connect via IPv6, even when the network does not support it. Disable this unless you use IPv6 on the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/autoconf6" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215358`

### Rule: If AIX server is not functioning as a network router, the gated daemon must be disabled.

**Rule ID:** `SV-215358r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This daemon provides gateway routing functions for protocols such as RIP and SNMP. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/gated" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215359`

### Rule: If AIX server is not functioning as a multicast router, the mrouted daemon must be disabled.

**Rule ID:** `SV-215359r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This daemon is an implementation of the multicast routing protocol. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/mrouted" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215360`

### Rule: If AIX server is not functioning as a DNS server, the named daemon must be disabled.

**Rule ID:** `SV-215360r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This is the server for the DNS protocol and controls domain name resolution for its clients. To prevent attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/named" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215361`

### Rule: If AIX server is not functioning as a network router, the routed daemon must be disabled.

**Rule ID:** `SV-215361r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The routed daemon manages the network routing tables in the kernel. To prevent attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/routed" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215362`

### Rule: If rwhod is not required on AIX, the rwhod daemon must be disabled.

**Rule ID:** `SV-215362r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This is the remote WHO service. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/rwhod" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215363`

### Rule: The timed daemon must be disabled on AIX.

**Rule ID:** `SV-215363r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This is the old UNIX time service. The timed daemon is the old UNIX time service. Disable this service and use xntp, if time synchronization is required in the environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/timed" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215364`

### Rule: If AIX server does not host an SNMP agent, the dpid2 daemon must be disabled.

**Rule ID:** `SV-215364r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The dpid2 daemon acts as a protocol converter, which enables DPI (SNMP v2) sub-agents, such as hostmibd, to talk to a SNMP v1 agent that follows SNMP MUX protocol. To prevent attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/dpid2" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215365`

### Rule: If SNMP is not required on AIX, the snmpmibd daemon must be disabled.

**Rule ID:** `SV-215365r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The snmpmibd daemon is a dpi2 sub-agent which manages a number of MIB variables. If snmpd is not required, it is recommended that it is disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/snmpmibd" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215366`

### Rule: The aixmibd daemon must be disabled on AIX.

**Rule ID:** `SV-215366r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The aixmibd daemon is a dpi2 sub-agent which manages a number of MIB variables. To prevent attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/aixmibd" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215367`

### Rule: The ndpd-host daemon must be disabled on AIX.

**Rule ID:** `SV-215367r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This is the Neighbor Discovery Protocol (NDP) daemon, required in IPv6. The ndpd-host is the NDP daemon for the server. Unless the server utilizes IPv6, this is not required and should be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is using IPv6, this is Not Applicable. From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/ndpd-host" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215368`

### Rule: The ndpd-router must be disabled on AIX.

**Rule ID:** `SV-215368r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This manages the Neighbor Discovery Protocol (NDP) for non-kernel activities, required in IPv6. The ndpd-router manages NDP for non-kernel activities. Unless the server utilizes IPv6, this is not required and should be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/ndpd-router" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215369`

### Rule: The daytime daemon must be disabled on AIX.

**Rule ID:** `SV-215369r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The daytime service provides the current date and time to other servers on a network. This daytime service is a defunct time service, typically used for testing purposes only. The service should be disabled as it can leave the system vulnerable to DoS ping attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^daytime[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215370`

### Rule: The cmsd daemon must be disabled on AIX.

**Rule ID:** `SV-215370r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This is a calendar and appointment service for CDE. The cmsd service is utilized by CDE to provide calendar functionality. If CDE is not required, this service should be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^#cmsd[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215371`

### Rule: The ttdbserver daemon must be disabled on AIX.

**Rule ID:** `SV-215371r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ttdbserver service is the tool-talk database service for CDE. This service runs as root and should be disabled. Unless required the ttdbserver service will be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^#ttdbserver[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215372`

### Rule: The uucp (UNIX to UNIX Copy Program) daemon must be disabled on AIX.

**Rule ID:** `SV-215372r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This service facilitates file copying between networked servers. The uucp (UNIX to UNIX Copy Program), service allows users to copy files between networked machines. Unless an application or process requires UUCP this should be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^uucp[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215373`

### Rule: The time daemon must be disabled on AIX.

**Rule ID:** `SV-215373r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This service can be used to synchronize system clocks. The time service is an obsolete process used to synchronize system clocks at boot time. This has been superseded by NTP, which should be used if time synchronization is necessary. Unless required the time service must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^time[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215374`

### Rule: The talk daemon must be disabled on AIX.

**Rule ID:** `SV-215374r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This talk service is used to establish an interactive two-way communication link between two UNIX users. Unless required the talk service will be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^talk[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215375`

### Rule: The ntalk daemon must be disabled on AIX.

**Rule ID:** `SV-215375r958478_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This service establishes a two-way communication link between two users, either locally or remotely. Unless required the ntalk service will be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^ntalk[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215376`

### Rule: The chargen daemon must be disabled on AIX.

**Rule ID:** `SV-215376r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This service is used to test the integrity of TCP/IP packets arriving at the destination. This chargen service is a character generator service and is used for testing the integrity of TCP/IP packets arriving at the destination. An attacker may spoof packets between machines running the chargen service and thus provide an opportunity for DoS attacks. Disable this service to prevent attacks unless testing the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^chargen[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215377`

### Rule: The discard daemon must be disabled on AIX.

**Rule ID:** `SV-215377r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The discard service is used as a debugging and measurement tool. It sets up a listening socket and ignores data that it receives. This is a /dev/null service and is obsolete. This can be used in DoS attacks and therefore, must be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^discard[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215378`

### Rule: The dtspc daemon must be disabled on AIX.

**Rule ID:** `SV-215378r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The dtspc service deals with the CDE interface of the X11 daemon. It is started automatically by the inetd daemon in response to a CDE client requesting a process to be started on the daemon's host. This makes it vulnerable to buffer overflow attacks, which may allow an attacker to gain root privileges on a host. This service must be disabled unless it is absolutely required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^dtspc[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215379`

### Rule: The pcnfsd daemon must be disabled on AIX.

**Rule ID:** `SV-215379r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The pcnfsd service is an authentication and printing program, which uses NFS to provide file transfer services. This service is vulnerable and exploitable and permits the machine to be compromised both locally and remotely. If PC NFS clients are required within the environment, Samba is recommended as an alternative software solution. The pcnfsd daemon predates Microsoft's release of SMB specifications. This service should therefore be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^pcnfsd[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215380`

### Rule: The rstatd daemon must be disabled on AIX.

**Rule ID:** `SV-215380r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rstatd service is used to provide kernel statistics and other monitorable parameters pertinent to the system such as: CPU usage, system uptime, network usage etc. An attacker may use this information in a DoS attack. This service should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^rstatd[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215381`

### Rule: The rusersd daemon must be disabled on AIX.

**Rule ID:** `SV-215381r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rusersd service runs as root and provides a list of current users active on a system. An attacker may use this service to learn valid account names on the system. This is not an essential service and should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^rusersd[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215382`

### Rule: The sprayd daemon must be disabled on AIX.

**Rule ID:** `SV-215382r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sprayd service is used as a tool to generate UDP packets for testing and diagnosing network problems. The service must be disabled if NFS is not in use, as it can be used by attackers in a Distributed Denial of Service (DDoS) attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^sprayd[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215383`

### Rule: The klogin daemon must be disabled on AIX.

**Rule ID:** `SV-215383r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The klogin service offers a higher degree of security than traditional rlogin or telnet by eliminating most clear-text password exchanges on the network. However, it is still not as secure as SSH, which encrypts all traffic. If using klogin to log in to a system, the password is not sent in clear text; however, if using "su" to another user, that password exchange is open to detection from network-sniffing programs. The recommendation is to use SSH wherever possible instead of klogin. If the klogin service is used, use the latest Kerberos version available and make sure that all the latest patches are installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^klogin[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215384`

### Rule: The kshell daemon must be disabled on AIX.

**Rule ID:** `SV-215384r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The kshell service offers a higher degree of security than traditional rsh services. However, it still does not use encrypted communications. The recommendation is to use SSH wherever possible instead of kshell. If the kshell service is used, you should use the latest Kerberos version available and must make sure that all the latest patches are installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^kshell[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215385`

### Rule: The rquotad daemon must be disabled on AIX.

**Rule ID:** `SV-215385r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rquotad service allows NFS clients to enforce disk quotas on file systems that are mounted on the local system. This service should be disabled if to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^rquotad[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215386`

### Rule: The tftp daemon must be disabled on AIX.

**Rule ID:** `SV-215386r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The tftp service allows remote systems to download or upload files to the tftp server without any authentication. It is therefore a service that should not run, unless needed. One of the main reasons for requiring this service to be activated is if the host is a NIM master. However, the service can be enabled and then disabled once a NIM operation has completed, rather than left running permanently.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^tftp[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215387`

### Rule: The imap2 service must be disabled on AIX.

**Rule ID:** `SV-215387r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The imap2 service or Internet Message Access Protocol (IMAP) supports the IMAP4 remote mail access protocol. It works with sendmail and bellmail. This service should be disabled if it is not required to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^imap2[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215388`

### Rule: The pop3 daemon must be disabled on AIX.

**Rule ID:** `SV-215388r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The pop3 service provides a pop3 server. It supports the pop3 remote mail access protocol. It works with sendmail and bellmail. This service should be disabled if it is not required to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^pop3[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215389`

### Rule: The finger daemon must be disabled on AIX.

**Rule ID:** `SV-215389r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The fingerd daemon provides the server function for the finger command. This allows users to view real-time pertinent user login information on other remote systems. This service should be disabled as it may provide an attacker with a valid user list to target.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^finger[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215390`

### Rule: The instsrv daemon must be disabled on AIX.

**Rule ID:** `SV-215390r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The instsrv service is part of the Network Installation Tools, used for servicing servers running AIX 3.2. This service should be disabled to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^instsrv[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215391`

### Rule: The echo daemon must be disabled on AIX.

**Rule ID:** `SV-215391r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The echo service can be used in Denial of Service or SMURF attacks. It can also be used by someone else to get through a firewall or start a data storm. The echo service is unnecessary and it increases the attack vector of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the /etc/inetd.conf for TCP and UDP echo service entries using command: # grep echo /etc/inetd.conf | grep -v \# If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215392`

### Rule: The Internet Network News (INN) server must be disabled on AIX.

**Rule ID:** `SV-215392r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Network News (INN) servers access Usenet newsfeeds and store newsgroup articles. INN servers use the Network News Transfer Protocol (NNTP) to transfer information from the Usenet to the server and from the server to authorized remote hosts. If this function is necessary to support a valid mission requirement, its use must be authorized and approved in the system accreditation package.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command: # ps -ef | egrep "innd|nntpd" If the above command produced any result, this is a finding. Check if "innd" or "nntpd" is started from "/etc/onetd.conf" using the following command: # egrep "innd|nntpd" /etc/inetd.conf | grep -v ^# If the above command produced any result, this is a finding. Check if "innd" or "nntpd" is added as a subsystem to the System Resource Controller (SRC): # lssrc -s innd # lssrc -s nntpd If the above commands found that "innd" or "nntpd" is defined in SRC, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-215393`

### Rule: If Stream Control Transmission Protocol (SCTP) must be disabled on AIX.

**Rule ID:** `SV-215393r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Stream Control Transmission Protocol (SCTP) is an IETF-standardized transport layer protocol. This protocol is not yet widely used. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system to determine if SCTP is installed: # lslpp -L bos.net.sctp Fileset Level State Type Description (Uninstaller) ---------------------------------------------------------------------------- lslpp: 0504-132 Fileset bos.net.sctp not installed. If the "bos.net.sctp" fileset is not listed, SCTP is not installed, this is not a finding. If the "bos.net.sctp" fileset is listed then SCTP is installed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-215394`

### Rule: The Reliable Datagram Sockets (RDS) protocol must be disabled on AIX.

**Rule ID:** `SV-215394r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Reliable Datagram Sockets (RDS) protocol is a relatively new protocol developed by Oracle for communication between the nodes of a cluster. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol. AIX has RDS protocol installed as part of the 'bos.net.tcp.client' fileset. The RDS protocol in primarily used for communication on INFI-Band interfaces. The protocol is manually loaded with the bypassctrl command. To prevent possible attacks this protocol must be disabled unless required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if RDS is currently loaded: # genkex | grep rds If there is any output from the command, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-215395`

### Rule: If automated file system mounting tool is not required on AIX, it must be disabled.

**Rule ID:** `SV-215395r958820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated file system mounting tools may provide unprivileged users with the ability to access local media and network shares. If this access is not necessary for the system’s operation, it must be disabled to reduce the risk of unauthorized access to these resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system uses "automated" by using command: # lssrc -s automountd Subsystem Group PID Status automountd autofs inoperative If the automountd process is active, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215396`

### Rule: AIX process core dumps must be disabled.

**Rule ID:** `SV-215396r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command: # lsuser -a core ALL root core=0 daemon core=0 bin core=0 sys core=0 adm core=0 uucp core=0 snapp core=0 ipsec core=0 srvproxy core=0 esaadmin core=0 sshd core=0 doejohn core=0 If any user does not have a value of "core = 0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215397`

### Rule: AIX kernel core dumps must be disabled unless needed.

**Rule ID:** `SV-215397r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in Denial of Service by exhausting the available space on the target file system. The kernel core dump process may increase the amount of time a system is unavailable due to a crash. Kernel core dumps can be useful for kernel debugging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if kernel core dumps are enabled on the system using command: # sysdumpdev -l primary /dev/sysdumpnull secondary /dev/sysdumpnull Look at both the primary and secondary dump devices. If either the primary or secondary dump device is not "/dev/sysdumpnull", this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-215398`

### Rule: AIX must set Stack Execution Disable (SED) system wide mode to all.

**Rule ID:** `SV-215398r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning. Satisfies: SRG-OS-000142-GPOS-00071, SRG-OS-000480-GPOS-00227, SRG-OS-000433-GPOS-00192</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to display SED systemwide mode: # sedmgr Stack Execution Disable (SED) mode: all SED configured in kernel: all If the above command shows a systemwide SED mode other than "all", this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-215399`

### Rule: AIX must protect against or limit the effects of Denial of Service (DoS) attacks by ensuring AIX is implementing rate-limiting measures on impacted network interfaces.

**Rule ID:** `SV-215399r958902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of AIX to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if bos.net.tcp.client_core package is installed: # lslpp -l | grep bos.net.tcp.client_core bos.net.tcp.client_core 7.2.1.1 COMMITTED TCP/IP Client Core Support bos.net.tcp.client_core 7.2.1.1 COMMITTED TCP/IP Client Core Support If the packages are not "COMMITTED", this is a finding. Check that the value set for "clean_partial_conns" is "1": # /usr/sbin/no -o clean_partial_conns clean_partial_conns = 1 If the value returned is "0", this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-215400`

### Rule: AIX must allow admins to send a message to all the users who logged in currently.

**Rule ID:** `SV-215400r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run following command to see if wall command is installed: # ls -al /usr/sbin/wall If "/usr/sbin/wall" does not exist, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-215401`

### Rule: AIX must allow admins to send a message to a user who logged in currently.

**Rule ID:** `SV-215401r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run following command to see if the "write" command is installed: # ls -al /usr/bin/write If "/usr/bin/write" does not exist, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-215402`

### Rule: The AIX SSH daemon must be configured to only use FIPS 140-2 approved ciphers.

**Rule ID:** `SV-215402r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed ciphers by running the following command: # grep -i ciphers /etc/ssh/sshd_config | grep -v '^#' The above command should yield the following output: Ciphers aes128-ctr,aes192-ctr,aes256-ctr If any of the following conditions are true, this is a finding. 1. No line is returned (default ciphers); 2. The returned ciphers list contains any cipher not starting with aes; 3. The returned ciphers list contains any cipher ending with cbc.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-215403`

### Rule: The AIX system must have no .netrc files on the system.

**Rule ID:** `SV-215403r1009555_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unencrypted passwords for remote FTP servers may be stored in .netrc files. Policy requires passwords be encrypted in storage and not used in access scripts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for the existence of any ".netrc" files by running the following command: # find / -name .netrc If any ".netrc" file exists, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-215404`

### Rule: AIX must turn on enhanced Role-Based Access Control (RBAC) to isolate security functions from nonsecurity functions, to grant system privileges to other operating system admins, and prohibit user installation of system software without explicit privileged status.

**Rule ID:** `SV-215404r1009556_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. Operating system functionality will vary, and while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages, such as from an approved software repository. AIX or software configuration management utility must enforce control of software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000134-GPOS-00068, SRG-OS-000312-GPOS-00123, SRG-OS-000362-GPOS-00149</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to retrieve the system RBAC mode: # lsattr -E -l sys0 -a enhanced_RBAC enhanced_RBAC true Enhanced RBAC Mode If the RBAC mode is not "true", this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215405`

### Rule: If DHCP server is not required on AIX, the DHCP server must be disabled.

**Rule ID:** `SV-215405r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The dhcpsd daemon is the DHCP server that serves addresses and configuration information to DHCP clients in the network. To prevent remote attacks this daemon should not be enabled unless there is no alternative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^start[[:blank:]]/usr/sbin/dhcpsd" /etc/rc.tcpip If there is any output from the command, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-215406`

### Rule: The rwalld daemon must be disabled on AIX.

**Rule ID:** `SV-215406r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rwalld service allows remote users to broadcast system wide messages. The service runs as root and should be disabled unless absolutely necessary to prevent attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, execute the following command: # grep "^rwalld[[:blank:]]" /etc/inetd.conf If there is any output from the command, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-215407`

### Rule: In the event of a system failure, AIX must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to mission processes.

**Rule ID:** `SV-215407r991562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving operating system state information helps to facilitate operating system restart and return to the operational mode of the organization with least disruption to mission/business processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To display the current dump device settings enter the following command: #sysdumpdev -l primary /dev/lg_dumplv secondary /dev/sysdumpnull copy directory /var/adm/ras forced copy flag TRUE always allow dump FALSE dump compression ON type of dump fw-assisted full memory dump disallow If the primary device and copy directory is not configured, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215408`

### Rule: The /etc/shells file must exist on AIX systems.

**Rule ID:** `SV-215408r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shells file (or equivalent) lists approved default shells. It helps provide layered defense to the security approach by ensuring users cannot change their default shell to an unauthorized unsecure shell.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
AIX ships the following shells that should be considered as "approved" shells: /bin/sh /bin/bsh /bin/csh /bin/ksh /bin/tsh /bin/ksh93 /usr/bin/sh /usr/bin/bsh /usr/bin/csh /usr/bin/ksh /usr/bin/tsh /usr/bin/ksh93 /usr/bin/rksh /usr/bin/rksh93 /usr/sbin/uucp/uucico /usr/sbin/sliplogin /usr/sbin/snappd ISSO/SA may install other shells. Ask ISSO/SA for other approved shells other than the shells shipped by AIX. Check if file "/etc/shells" exists by running: # ls -la /etc/shells rw-r--r-- 1 bin bin 111 Jun 01 2015 /etc/shells If "/etc/shells" file does not exist, this is a finding. Verify that "/etc/shells" only contains approved shells: # cat /etc/shells /bin/csh /bin/ksh /bin/psh /bin/tsh /bin/bsh /usr/bin/csh /usr/bin/ksh /usr/bin/tsh /usr/bin/bsh If "/etc/shells" file contains a non-approved shell, this is a finding. Check "/etc/security/login.cfg" for the shells attribute value of "usw:" stanza: # lssec -f /etc/security/login.cfg -s usw -a shells usw shells=/bin/sh,/bin/bsh,/bin/csh,/bin/ksh,/bin/tsh,/bin/ksh93,/usr/bin/sh,/usr/bin/bsh,/usr/bin/csh,/usr/bin/ksh,/usr/bin/tsh,/usr/bin/ksh93,/usr/bin/rksh,/usr/bin/rksh93,/usr/sbin/uucp/uucico,/usr/sbin/sliplogin,/usr/sbin/snappd If the shells attribute value does not exist or is empty, this is a finding. If the returned shells attribute value contains a shell that is not defined in "/etc/shells" file, this is a finding. If the returned shells attribute value contains a non-approved shell, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215409`

### Rule: AIX public directories must be the only world-writable directories and world-writable files must be located only in public directories.

**Rule ID:** `SV-215409r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>World-writable files and directories make it easy for a malicious user to place potentially compromising files on the system. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage (e.g., /tmp) and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for world-writable files and directories by running command: # find / -perm -2 -a \( -type d -o -type f \) -exec ls -ld {} \; If any world-writable files or directories are located, except those required for proper system or application operation, such as "/tmp" and "/dev/null", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215410`

### Rule: AIX must be configured to only boot from the system boot device.

**Rule ID:** `SV-215410r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to boot from removable media is the same as being able to boot into single user or maintenance mode without a password. This ability could allow a malicious user to boot the system and perform changes possibly compromising or damaging the system. It could also allow the system to be used for malicious purposes by a malicious anonymous user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system is configured to boot from devices other than the system startup media by running command: # bootlist -m normal -o The returned values should be "hdisk{x}". If the system is setup to boot from a non-hard disk device, this is a finding. Additionally, ask the SA if the machine is setup for "multi-boot" in the SMS application. If multi-boot is enabled, the firmware will stop at boot time and request which image to boot from the user. If "multi-boot" is enabled, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215411`

### Rule: AIX must not use removable media as the boot loader.

**Rule ID:** `SV-215411r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious users with removable boot media can gain access to a system configured to use removable media as the boot loader.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the servers boot lists for the "normal", "service", "both", or "prevboot" modes by command: # bootlist -m <mode> -o Ensure "hdisk{x}" is the only devices listed. If boot devices, such as "cd{x}", "fd{x}", "rmt{x}", or "ent{x}" are used, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215412`

### Rule: If the AIX host is running an SMTP service, the SMTP greeting must not provide version information.

**Rule ID:** `SV-215412r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The version of the SMTP service can be used by attackers to plan an attack based on vulnerabilities present in the specific version.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the AIX host is not running an SMTP service, this is Not Applicable. Check the value of the "SmtpGreetingMessage" parameter in the "sendmail.cf" file: # grep SmtpGreetingMessage /etc/mail/sendmail.cf If the value of the "SmtpGreetingMessage" parameter contains the "$v" or "$Z" macros, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215413`

### Rule: AIX must contain no .forward files.

**Rule ID:** `SV-215413r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The .forward file allows users to automatically forward mail to another system. Use of .forward files could allow the unauthorized forwarding of mail and could potentially create mail loops which could degrade system performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search for any ".forward" files on the system using command: # find / -name .forward -print If any ".forward" files are found on the system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215414`

### Rule: The sendmail server must have the debug feature disabled on AIX systems.

**Rule ID:** `SV-215414r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Debug mode is a feature present in older versions of Sendmail which, if not disabled, may allow an attacker to gain access to a system through the Sendmail service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the version of "sendmail" installed on the system using: # echo \$Z | /usr/sbin/sendmail -bt -d0 The above command should yield the following output: Version AIX7.2/8.14.4 Compiled with: DNSMAP LDAPMAP LDAP_REFERRALS LOG MAP_REGEX MATCHGECOS MILTER MIME7TO8 MIME8TO7 NAMED_BIND NDBM NETINET NETINET6 NETUNIX NEWDB NIS NISPLUS PIPELINING SCANF USERDB USE_LDAP_INIT USE_TTYPATH XDEBUG If the "sendmail" reported version is less than "8.6", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215415`

### Rule: SMTP service must not have the EXPN or VRFY features active on AIX systems.

**Rule ID:** `SV-215415r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SMTP EXPN function allows an attacker to determine if an account exists on a system, providing significant assistance to a brute force attack on user accounts. EXPN may also provide additional information concerning users on the system, such as the full names of account owners. The VRFY (Verify) command allows an attacker to determine if an account exists on a system, providing significant assistance to a brute force attack on user accounts. VRFY may provide additional information about users on the system, such as the full names of account owners.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "PrivacyOptions" parameter in "/etc/mail/sendmail.cf": # grep -v "^#" /etc/mail/sendmail.cf |grep -i privacyoptions The above command should yield the following output: O PrivacyOptions=goaway The "O PrivacyOptions" should have the "goaway" option (covering both noexpn and novrfy). If the "O PrivacyOptions" value does not contain "goaway", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215416`

### Rule: All global initialization file executable search paths must contain only absolute paths.

**Rule ID:** `SV-215416r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the global initialization files' executable search paths using: # grep -i PATH /etc/profile /etc/bashrc /etc/csh.login /etc/csh.cshrc /etc/environment /etc/.login /etc/security/environ /etc/environment:PATH=/usr/bin:/etc:/usr/sbin:/usr/ucb:/usr/bin/X11:/sbin:/usr/java7_64/jre/bin:/usr/java7_64/bin /etc/environment:LOCPATH=/usr/lib/nls/loc /etc/environment:NLSPATH=/usr/lib/nls/msg/%L/%N:/usr/lib/nls/msg/%L/%N.cat:/usr/lib/nls/msg/%l.%c/%N:/usr/lib/nls/msg/%l.%c/%N.cat This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) or other than "$PATH", it is a relative path, and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215417`

### Rule: The SMTP service HELP command must not be enabled on AIX.

**Rule ID:** `SV-215417r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HELP command should be disabled to mask version information. The version of the SMTP service software could be used by attackers to target vulnerabilities present in specific software versions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to get the "HELP" file location: # grep "^O HelpFile" /etc/mail/sendmail.cf The above command should yield the following output: O HelpFile=/etc/mail/helpfile If the above command does not yield any output, this is not a finding. The "HELP" file should be referenced by the "HelpFile" option. Check to see if the "HELP" file exists: # ls <helpfile_path> If the "HELP" file exists, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215418`

### Rule: NIS maps must be protected through hard-to-guess domain names on AIX.

**Rule ID:** `SV-215418r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of hard-to-guess NIS domain names provides additional protection from unauthorized access to the NIS directory information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the domain name for NIS maps using command: # domainname If no ouput is returned or the name returned is simple to guess, such as the organization name, building, or room name, etc., this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215419`

### Rule: The AIX systems access control program must be configured to grant or deny system access to specific hosts.

**Rule ID:** `SV-215419r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system's access control program is not configured with appropriate rules for allowing and denying access to system network resources, services may be accessible to unauthorized hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the "/etc/hosts.allow" and "/etc/hosts.deny" files using commands: # ls -la /etc/hosts.allow -rw-r--r-- 1 root system 11 Jan 28 11:09 /etc/hosts.allow # ls -la /etc/hosts.deny -rw-r--r-- 1 root system 0 Jan 28 11:02 /etc/hosts.deny If either file does not exist, this is a finding. Check for the presence of a default deny entry using command: # grep -E "ALL:[[:blank:]]*ALL" /etc/hosts.deny ALL:ALL If the "ALL: ALL" entry is not present in the "/etc/hosts.deny" file, any TCP service from a host or network not matching other rules will be allowed access. If the entry is not in "/etc/hosts.deny", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215420`

### Rule: All AIX files and directories must have a valid group owner.

**Rule ID:** `SV-215420r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if any file on the system does not have a valid group owner using command: # find / -nogroup -print If any such files are found, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215421`

### Rule: AIX control scripts library search paths must contain only absolute paths.

**Rule ID:** `SV-215421r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library search path environment variable(s) contain a list of directories for the dynamic linker to search to find libraries. If this path includes the current working directory or other relative paths, libraries in these directories may be loaded instead of system libraries. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' library search paths: # grep -r LIBPATH /etc/rc* /etc/rc.teboot:export LIBPATH=/../usr/lib /etc/rc.teboot:export LIBPATH=/usr/lib This variable is formatted as a colon-separated list of paths. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) or other than "$PATH", it is a relative path, and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215422`

### Rule: The control script lists of preloaded libraries must contain only absolute paths on AIX systems.

**Rule ID:** `SV-215422r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries relative to the current working directory, unintended libraries may be preloaded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' library preload list using command: # grep -r LDR_PRELOAD /etc/rc* /etc/rc.teboot:export LDR_PRELOAD=/../usr/bin /etc/rc.teboot:export LDR_PRELOAD=/usr/bin This variable is formatted as a colon-separated list of paths. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) or other than "$PATH", it is a relative path, and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215423`

### Rule: The global initialization file lists of preloaded libraries must contain only absolute paths on AIX.

**Rule ID:** `SV-215423r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries relative to the current working directory, unintended libraries may be preloaded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the global initialization files' library preload list using command: # grep LDR_PRELOAD /etc/profile /etc/bashrc /etc/security/.login /etc/environment /etc/security/environ /etc/environment:LDR_PRELOAD=:/usr/bin/X11:/sbin:/usr/java7_64/jre/bin:/usr/java7_64/bin This variable is formatted as a colon-separated list of paths. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) or other than "$PATH", it is a relative path, and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215424`

### Rule: The local initialization file library search paths must contain only absolute paths on AIX.

**Rule ID:** `SV-215424r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library search path environment variable(s) contain a list of directories for the dynamic linker to search to find libraries. If this path includes the current working directory or other relative paths, libraries in these directories may be loaded instead of system libraries. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is interpreted as the current working directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify local initialization files that have library search paths: # cat /etc/passwd | cut -f 1,1 -d ":" | xargs -n1 -IUSER sh -c 'grep -l LIB ~USER/.*' /root/.sh_history /home/doejohn/.profile /home/doejane/.profile For each file identified above, verify the search path contains only absolute paths: Note: The "LIBPATH" and "LD_LIBRARY_PATH" variables are formatted as a colon-separated list of directories. # cat <local_initilization_file> | grep -Ei 'lib|library' LD_LIBRARY_PATH=/usr/lib LIBPATH=/usr/lib If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) or other than "$PATH", it is a relative path, and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215425`

### Rule: The local initialization file lists of preloaded libraries must contain only absolute paths on AIX.

**Rule ID:** `SV-215425r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries relative to the current working directory, unintended libraries may be preloaded. This variable is formatted as a space-separated list of libraries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify local initialization files that have library search paths: # cat /etc/passwd | cut -f 1,1 -d ":" | xargs -n1 -IUSER sh -c 'grep -l LDR_PRELOAD ~USER/.*' /root/.sh_history /home/doejohn/.profile /home/doejane/.profile For each file identified above, verify the search path contains only absolute paths: Note: This variable is formatted as a colon-separated list of paths. # cat <local_initilization_file> | grep -Ei 'ldr|preload' LDR_PRELOAD=/usr/lib If the paths listed have not been documented and authorized by the ISSO/ISSM, this is a finding. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/) or other than "$PATH", it is a relative path, and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215426`

### Rule: AIX package management tool must be used daily to verify system software.

**Rule ID:** `SV-215426r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verification using the system package management tool can be used to determine that system software has not been tampered with. This requirement is not applicable to systems not using package management tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the root crontab for a daily job invoking the system package management tool to verify the integrity of installed packages. From the command prompt, run the following command: # crontab -l | grep lppchk 55 22 * * * /lppchk.sh # Daily LPP check script If no such job exists, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215427`

### Rule: The AIX DHCP client must not send dynamic DNS updates.

**Rule ID:** `SV-215427r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Dynamic DNS updates transmit unencrypted information about a system including its name and address and should not be used unless needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If AIX does not use DHCP client, this is Not Applicable. Determine if the system's DHCP client is configured to send dynamic DNS updates: # grep "^updateDNS" /etc/dhcpc.opt /etc/dhcpcd.ini If any lines are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215428`

### Rule: AIX must not run any routing protocol daemons unless the system is a router.

**Rule ID:** `SV-215428r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for any running routing protocol daemons by running: # ps -ef | egrep '(ospf|route|bgp|zebra|quagga|gate)' If any routing protocol daemons are listed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215429`

### Rule: AIX must not process ICMP timestamp requests.

**Rule ID:** `SV-215429r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The processing of Internet Control Message Protocol (ICMP) timestamp requests increases the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command to check if "ipsec_v4" and "ipsec_v6" devices are active: # lsdev -Cc ipsec The above command should yield the following output: ipsec_v4 Available IP Version 4 Security Extension ipsec_v6 Available IP Version 6 Security Extension If "ipsec_v4" or "ipsec_v6" is not displayed, or it is not in "Available" state, this is a finding. Determine if the system is configured to respond to ICMP Timestamp requests using the following command: # lsfilt Beginning of IPv4 filter rules. Rule 1: Rule action : permit Source Address : 0.0.0.0 Source Mask : 0.0.0.0 Destination Address : 0.0.0.0 Destination Mask : 0.0.0.0 Source Routing : no Protocol : udp Source Port : eq 4001 Destination Port : eq 4001 Scope : both Direction : both Logging control : no Fragment control : all packets Tunnel ID number : 0 Interface : all Auto-Generated : yes Expiration Time : 0 Description : Default Rule Rule 2: *** Dynamic filter placement rule for IKE tunnels *** Logging control : no Rule 3: Rule action : deny Source Address : 0.0.0.0 Source Mask : 0.0.0.0 Destination Address : 0.0.0.0 Destination Mask : 0.0.0.0 Source Routing : yes Protocol : icmp ICMP type : any 0 ICMP code : eq 13 Scope : both Direction : inbound Logging control : no Fragment control : all packets Tunnel ID number : 0 Interface : all Auto-Generated : no Expiration Time : 0 Description : Rule 4: Rule action : deny Source Address : 0.0.0.0 Source Mask : 0.0.0.0 Destination Address : 0.0.0.0 Destination Mask : 0.0.0.0 Source Routing : yes Protocol : icmp ICMP type : eq 14 ICMP code : any 0 Scope : both Direction : outbound Logging control : no Fragment control : all packets Tunnel ID number : 0 Interface : all Auto-Generated : no Expiration Time : 0 Description : Rule 0: Rule action : permit Source Address : 0.0.0.0 Source Mask : 0.0.0.0 Destination Address : 0.0.0.0 Destination Mask : 0.0.0.0 Source Routing : yes Protocol : all Source Port : any 0 Destination Port : any 0 Scope : both Direction : both Logging control : no Fragment control : all packets Tunnel ID number : 0 Interface : all Auto-Generated : no Expiration Time : 0 Description : Default Rule End of IPv4 filter rules. If there is no rule blocking ICMP packet type of "13" and ICMP packet type of "14" (rule #3 and rule #4 above), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215430`

### Rule: AIX must not respond to ICMPv6 echo requests sent to a broadcast address.

**Rule ID:** `SV-215430r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast ICMP echo requests facilitates network mapping and provides a vector for amplification attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following command: # /usr/sbin/no -o bcastping bcastping = 0 If the value returned is not "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-215431`

### Rule: AIX must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-215431r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if "/etc/security/.profile" contains the proper "umask" setting by running the following command: # grep "umask 077" /etc/security/.profile umask 077 If the above command does not output the "umask 077", this is a finding. From the command prompt, run the following command to check if "umask=077" for the default stanza in "/etc/security/user": # lssec -f /etc/security/user -s default -a umask default umask=077 If the "umask" for the default stanza is not "077", or the "umask" is not set, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-215432`

### Rule: There must be no .rhosts, .shosts, hosts.equiv, or shosts.equiv files on the AIX system.

**Rule ID:** `SV-215432r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trust files are convenient, but when used in conjunction with the remote login services, they can allow unauthenticated access to a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the files using: # find / -name .rhosts # find / -name .shosts # find / -name hosts.equiv # find / -name shosts.equiv If ".rhosts", ".shosts", "hosts.equiv", or "shosts.equiv" are found, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-215433`

### Rule: The .rhosts file must not be supported in AIX PAM.

**Rule ID:** `SV-215433r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.rhosts files are used to specify a list of hosts permitted remote access to a particular account without authenticating. The use of such a mechanism defeats strong identification and authentication requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the PAM configuration for "rhosts_auth" using command: # grep rhosts_auth /etc/pam.conf |grep -v \# If a "rhosts_auth" entry is found, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215434`

### Rule: The AIX root user home directory must not be the root directory (/).

**Rule ID:** `SV-215434r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changing the root home directory to something other than / and assigning it a 0700 protection makes it more difficult for intruders to manipulate the system by reading the files that root places in its default directory. It also gives root the same discretionary access control for root's home directory as for the other plain user home directories.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if root is assigned a home directory other than "/" by listing its home directory by running command: # grep "^root" /etc/passwd | awk -F":" '{print $6}' /root If the root user's home directory is "/", this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-215435`

### Rule: All AIX interactive users must be assigned a home directory in the passwd file and the directory must exist.

**Rule ID:** `SV-215435r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All users must be assigned a home directory in the passwd file. Failure to have a home directory may result in the user being put in the root directory. This could create a Denial of Service because the user would not be able to perform useful tasks in this location.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify each interactive user is assigned a home directory: # cut -d: -f1,6 /etc/passwd root srvproxy doejohn If an interactive user is not assigned a home directory, this is a finding. Verify that the interactive user home directories exist on the system: # cut -d: -f6 /etc/passwd | xargs -n1 ls -ld drwxr-xr-x 2 doejohn staff 256 Jan 25 13:18 /home/doejohn drwxr-xr-x 2 sshd system 256 Aug 11 2017 /home/srvproxy drwx------ 2 root system 256 Jan 30 12:54 /root If any interactive user home directory does not exist, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-215436`

### Rule: The AIX operating system must use Multi Factor Authentication.

**Rule ID:** `SV-215436r1009557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, privileged and non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1. Something you know (e.g., password/PIN); 2. Something you have (e.g., cryptographic identification device, token); and 3. Something you are (e.g., biometric). The DoD CAC with DoD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055, SRG-OS-000375-GPOS-00160</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all required packages are installed: # lslpp -l |grep -i powerscmfa powerscMFA.license 1.2.0.1 COMMITTED PowerSC MFA license files powerscMFA.pam.base 1.2.0.1 COMMITTED PowerSC MFA standard inband powerscMFA.pam.fallback 1.2.0.1 COMMITTED PowerSC MFA Password fallback powerscMFA.pam.pmfamapper 1.2.0.1 COMMITTED USB Smartcard Interface to powerscMFA.pam.usbsmartcard If any of the above packages are not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215437`

### Rule: The AIX operating system must be configured to authenticate using Multi Factor Authentication.

**Rule ID:** `SV-215437r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, privileged and non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1. Something you know (e.g., password/PIN); 2. Something you have (e.g., cryptographic identification device, token); and 3. Something you are (e.g., biometric). The DoD CAC with DoD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the global "auth_type" is configured to use PAM: # grep auth_type /etc/security/login.cfg |grep AUTH auth_type = PAM_AUTH If "auth_type" is not set to "PAM_AUTH", this is a finding. Verify that the user stanza is configured to use PAM: # lssec -f /etc/security/login.cfg -susw -a auth_type usw auth_type=PAM_AUTH If "auth_type" is not set to "PAM_AUTH", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215438`

### Rule: The AIX operating system must be configured to use Multi Factor Authentication for remote connections.

**Rule ID:** `SV-215438r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, privileged and non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1. Something you know (e.g., password/PIN); 2. Something you have (e.g., cryptographic identification device, token); and 3. Something you are (e.g., biometric). The DoD CAC with DoD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH is configured to use multi factor authentication: # grep ^sshd /etc/pam.conf | head -3 sshd auth required pam_ckfile sshd auth required pam_permission file=/etc/security/access.conf found=allow sshd auth required pam_pmfa /etc/security/pmfa/pam_pmfa.conf If the output does not match the above lines, any lines are missing, or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215439`

### Rule: AIX must have the have the PowerSC Multi Factor Authentication Product configured.

**Rule ID:** `SV-215439r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, privileged and non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1. Something you know (e.g., password/PIN); 2. Something you have (e.g., cryptographic identification device, token); and 3. Something you are (e.g., biometric). The DoD CAC with DoD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify /etc/security/pmfa/pam_pmfa.conf is configured correctly. # grep -i "trustedcas" /etc/security/pmfa/pam_pmfa.conf | grep -v '#' TRUSTEDCAS = /<path_to_file>/server_ca.pem Note: Verify with the SA/ISSO as to the location of the "server_ca.pem" file. If "TRUSTEDCAS" is not configured to point to a valid "server_ca.pem" file or is missing, this is a finding. # grep -i "mfa-url" /etc/security/pmfa/pam_pmfa.conf | grep -v '#' MFA-URL = https://pmfa.example.com:6793/policyAuth/ If the "MFA-URL" is missing or does not point to a valid address, this is a finding. # grep -i "server-version" /etc/security/pmfa/pam_pmfa.conf | grep -v '#' SERVER-VERSION = 2 If "SERVER-VERSION" is missing or is not set to "2", this is a finding. # grep -i "ctc-prompt" /etc/security/pmfa/pam_pmfa.conf | grep -v '#' CTC-PROMPT-ONLY = Y If "CTC-PROMPT-ONLY" is missing or is not set to "Y", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-215440`

### Rule: The AIX operating system must be configured to use a valid server_ca.pem file.

**Rule ID:** `SV-215440r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, privileged and non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1. Something you know (e.g., password/PIN); 2. Something you have (e.g., cryptographic identification device, token); and 3. Something you are (e.g., biometric). The DoD CAC with DoD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the location of the "server_ca.pem" file: # grep -i "trustedcas" /etc/security/pmfa/pam_pmfa.conf | grep -v '#' TRUSTEDCAS = /<path_to_file>/server_ca.pem Verify that the configured "server_ca.pem" file exists in the defined location: # ls -la /<path_to_file>/server_ca.pem If the file does not exist, this is a finding.

## Group: SRG-OS-000376-GPOS-00161

**Group ID:** `V-215441`

### Rule: The AIX operating system must accept and verify Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-215441r958816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems. Satisfies: SRG-OS-000376-GPOS-00161, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the " bos.ahafs" package is installed: # lslpp -l |grep bos.ahafs bos.ahafs 7.1.5.15 COMMITTED Aha File System If the "bos.ahafs" package is not installed, this is a finding. Verify "pmfahotplugd" service is running: # lssrc -s pmfahotplugd If the " pmfahotplugd" service is not running, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-219057`

### Rule: AIX must employ a deny-all, allow-by-exception firewall policy for allowing connections to other systems.

**Rule ID:** `SV-219057r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to restrict network connectivity only to authorized systems permits inbound connections from malicious systems. It also permits outbound connections that may facilitate exfiltration of DoD data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the command prompt, run the following commands to check if the "all traffic" filter rules, the predefined rule with Rule-ID 0, are defined to deny all packages: # lsfilt -v4 -n0 # lsfilt -v6 -n0 Rule 0: Rule action : deny Source Address : 0.0.0.0 Source Mask : 0.0.0.0 Destination Address : 0.0.0.0 Destination Mask : 0.0.0.0 Source Routing : yes Protocol : all Source Port : any 0 Destination Port : any 0 Scope : both Direction : both Logging control : no Fragment control : all packets Tunnel ID number : 0 Interface : all Auto-Generated : no Expiration Time : 0 Description : Default Rule Rule 0: Rule action : deny Source Address : :: Source Mask : 0 Destination Address : :: Destination Mask : 0 Source Routing : yes Protocol : all Source Port : any 0 Destination Port : any 0 Scope : both Direction : both Logging control : no Fragment control : all packets Tunnel ID number : 0 Interface : all Auto-Generated : no Expiration Time : 0 Description : Default Rule If any of the "all traffic" rules has "Rule action : permit", this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-219956`

### Rule: AIX must be configured so that the audit system takes appropriate action when the audit storage volume is full.

**Rule ID:** `SV-219956r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Taking appropriate action in case of a filled audit storage volume will minimize the possibility of losing audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the action the operating system takes if the disk the audit records are written to becomes full. Verify that the file "/etc/security/audit/config" includes the required settings with the following command: # cat /etc/security/audit/config bin: trail = /audit/trail bin1 = /audit/bin1 bin2 = /audit/bin2 binsize = 25000 cmds = /etc/security/audit/bincmds freespace = 65536 backuppath = /audit backupsize = 0 bincompact = off If any of the configurations listed above is missing or not set to the listed value or greater, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245557`

### Rule: The AIX /etc/hosts file must be owned by root.

**Rule ID:** `SV-245557r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized ownership of the /etc/hosts file can lead to the ability for a malicious actor to redirect traffic to servers of their choice. It is also possible to use the /etc/hosts file to block detection by security software by blocking the traffic to all the download or update servers of well-known security vendors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of /etc/hosts using command: # ls -al /etc/hosts The above command should yield the following output: -rw-r----- 1 root system 993 Mar 11 07:04 /etc/hosts If the file is not owned by root, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245558`

### Rule: The AIX /etc/hosts file must be group-owned by system.

**Rule ID:** `SV-245558r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized group ownership of the /etc/hosts file can lead to the ability for a malicious actor to redirect traffic to servers of their choice. It is also possible to use the /etc/hosts file to block detection by security software by blocking the traffic to all the download or update servers of well-known security vendors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of /etc/hosts using command: # ls -al /etc/hosts The above command should yield the following output: -rw-r----- 1 root system 993 Mar 11 07:04 /etc/hosts If the file is not group-owned by system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245559`

### Rule: The AIX /etc/hosts file must have a mode of 0640 or less permissive.

**Rule ID:** `SV-245559r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized permissions of the /etc/hosts file can lead to the ability for a malicious actor to redirect traffic to servers of their choice. It is also possible to use the /etc/hosts file to block detection by security software by blocking the traffic to all the download or update servers of well-known security vendors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of /etc/hosts using command: # ls -al /etc/hosts The above command should yield the following output: -rw-r----- 1 root system 993 Mar 11 07:04 /etc/hosts If the file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245560`

### Rule: AIX cron and crontab directories must have a mode of 0640 or less permissive.

**Rule ID:** `SV-245560r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incorrect permissions of the cron or crontab directories could permit unauthorized users the ability to alter cron jobs and run automated jobs as privileged users. Failure to set proper permissions of cron or crontab directories provides unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the "crontab" directory using command: # ls -ld /var/spool/cron/crontabs drw-r----- 2 bin cron 256 Jan 25 12:33 /var/spool/cron/crontabs If the file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245561`

### Rule: The AIX /etc/syslog.conf file must be owned by root.

**Rule ID:** `SV-245561r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized ownership of the /etc/syslog.conf file can lead to the ability for a malicious actor to alter or disrupt system logging activities. This can aid the malicious actor in avoiding detection and further their ability to conduct malicious activities on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of /etc/syslog.conf using command: # ls -al /etc/syslog.conf The above command should yield the following output: -rw-r----- 1 root system 993 Mar 11 07:04 /etc/syslog.conf If the file is not owned by root, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245562`

### Rule: The AIX /etc/syslog.conf file must be group-owned by system.

**Rule ID:** `SV-245562r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized group ownership of the /etc/syslog.conf file can lead to the ability for a malicious actor to alter or disrupt system logging activities. This can aid the malicious actor in avoiding detection and further their ability to conduct malicious activities on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of /etc/syslog.conf using command: # ls -al /etc/syslog.conf The above command should yield the following output: -rw-r----- 1 root system 993 Mar 11 07:04 /etc/syslog.conf If the file is not group-owned by system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245563`

### Rule: The AIX /etc/syslog.conf file must have a mode of 0640 or less permissive.

**Rule ID:** `SV-245563r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized permissions of the /etc/syslog.conf file can lead to the ability for a malicious actor to alter or disrupt system logging activities. This can aid the malicious actor in avoiding detection and further their ability to conduct malicious activities on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of /etc/syslog.conf using command: # ls -al /etc/syslog.conf The above command should yield the following output: -rw-r----- 1 root system 993 Mar 11 07:04 /etc/syslog.conf If the file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245564`

### Rule: The inetd.conf file on AIX must be group owned by the "system" group.

**Rule ID:** `SV-245564r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to give ownership of sensitive files or utilities to system groups may provide unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of "/etc/inetd.conf": # ls -al /etc/inetd.conf The above command should yield the following output: -rw-r----- root system /etc/inetd.conf If the file is not group owned by system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245565`

### Rule: The AIX /etc/inetd.conf file must have a mode of 0640 or less permissive.

**Rule ID:** `SV-245565r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to set proper permissions of sensitive files or utilities may provide unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of "/etc/inetd.conf": # ls -al /etc/inetd.conf The above command should yield the following output: -rw-r----- root system /etc/inetd.conf If the file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245566`

### Rule: The AIX /var/spool/cron/atjobs directory must be owned by root or bin.

**Rule ID:** `SV-245566r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized ownership of the /var/spool/cron/atjobs directory could permit unauthorized users the ability to alter atjobs and run automated jobs as privileged users. Failure to set proper permissions of the /var/spool/cron/atjobs directory provides unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the /var/spool/cron/atjobs directory using command: # ls -ld /var/spool/cron/atjobs The above command should yield the following output: drw-r----- 1 bin cron 993 Mar 11 07:04 /var/spool/cron/atjobs If the owner of the "atjobs" directory is not "root" or "bin", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245567`

### Rule: The AIX /var/spool/cron/atjobs directory must be group-owned by cron.

**Rule ID:** `SV-245567r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized group ownership of the /var/spool/cron/atjobs directory could permit unauthorized users the ability to alter atjobs and run automated jobs as privileged users. Failure to set proper permissions of the /var/spool/cron/atjobs directory provides unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the /var/spool/cron/atjobs directory using command: # ls -ld /var/spool/cron/atjobs The above command should yield the following output: drw-r----- 1 bin cron 993 Mar 11 07:04 /var/spool/cron/atjobs If the group owner of the "atjobs" directory is not "cron", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245568`

### Rule: The AIX /var/spool/cron/atjobs directory must have a mode of 0640 or less permissive.

**Rule ID:** `SV-245568r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incorrect permissions of the /var/spool/cron/atjobs directory could permit unauthorized users the ability to alter atjobs and run automated jobs as privileged users. Failure to set proper permissions of the /var/spool/cron/atjobs directory provides unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the mode of the /var/spool/cron/atjobs directory using command: # ls -ld /var/spool/cron/atjobs drw-r----- 1 daemon daemon 993 Mar 11 07:04 /var/spool/cron/atjobs If the directory has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245569`

### Rule: The AIX cron and crontab directories must be group-owned by cron.

**Rule ID:** `SV-245569r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incorrect group ownership of the cron or crontab directories could permit unauthorized users the ability to alter cron jobs and run automated jobs as privileged users. Failure to give ownership of cron or crontab directories to root or to bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group owner of the "crontab" directory using command: # ls -ld /var/spool/cron/crontabs drwxrwx--- 2 bin cron 256 Jan 25 12:33 /var/spool/cron/crontabs If the group owner of the "crontab" directory is not "cron", this is a finding.

