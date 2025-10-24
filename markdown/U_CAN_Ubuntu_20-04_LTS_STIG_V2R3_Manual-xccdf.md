# STIG Benchmark: Canonical Ubuntu 20.04 LTS Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-238196`

### Rule: The Ubuntu operating system must provision temporary user accounts with an expiration time of 72 hours or less.

**Rule ID:** `SV-238196r958364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, the operating system must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. To address access requirements, many operating systems may be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system expires temporary user accounts within 72 hours or less. For every existing temporary account, run the following command to obtain its account expiration information: $ sudo chage -l system_account_name | grep expires Password expires : Aug 07, 2019 Account expires : Aug 07, 2019 Verify that each of these accounts has an expiration date set within 72 hours of account creation. If any temporary account does not expire within 72 hours of that account's creation, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-238197`

### Rule: The Ubuntu operating system must enable the graphical user logon banner to display the Standard Mandatory DoD Notice and Consent Banner before granting local access to the system via a graphical user logon.

**Rule ID:** `SV-238197r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the Ubuntu operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the operating system via a graphical user logon. Note: If the system does not have a graphical user interface installed, this requirement is Not Applicable. Check that the operating banner message for the graphical user logon is enabled with the following command: $ grep ^banner-message-enable /etc/gdm3/greeter.dconf-defaults banner-message-enable=true If the line is commented out or set to "false", this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-238198`

### Rule: The Ubuntu operating system must display the Standard Mandatory DOD Notice and Consent Banner before granting local access to the system via a graphical user logon.

**Rule ID:** `SV-238198r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the Ubuntu operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the operating system via a graphical user logon. Note: If the system does not have a graphical user interface installed, this requirement is Not Applicable. Verify the operating system displays the exact approved Standard Mandatory DOD Notice and Consent Banner text with the command: $ grep ^banner-message-text /etc/gdm3/greeter.dconf-defaults banner-message-text='You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.\n\nBy using this IS (which includes any device attached to this IS), you consent to the following conditions:\n\n-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.\n\n-At any time, the USG may inspect and seize data stored on this IS.\n\n-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.\n\n-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.\n\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.' If the banner-message-text is missing, commented out, or does not match the Standard Mandatory DOD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-238199`

### Rule: The Ubuntu operating system must retain a user's session lock until that user reestablishes access using established identification and authentication procedures.

**Rule ID:** `SV-238199r958400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, a session lock of the Ubuntu operating system must remain in place until the user reauthenticates. No other activity aside from reauthentication must unlock the system. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000029-GPOS-00010</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operation system has a graphical user interface session lock enabled. Note: If the Ubuntu operating system does not have a graphical user interface installed, this requirement is Not Applicable. Get the "lock-enabled" setting to verify the graphical user interface session has the lock enabled with the following command: $ sudo gsettings get org.gnome.desktop.screensaver lock-enabled true If "lock-enabled" is not set to "true", this is a finding.

## Group: SRG-OS-000030-GPOS-00011

**Group ID:** `V-238200`

### Rule: The Ubuntu operating system must allow users to directly initiate a session lock for all connection types.

**Rule ID:** `SV-238200r1015139_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, the Ubuntu operating systems need to provide users with the ability to manually invoke a session lock so users may secure their session if they need to temporarily vacate the immediate physical vicinity. Satisfies: SRG-OS-000030-GPOS-00011, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has the "vlock" package installed by running the following command: $ dpkg -l | grep vlock If "vlock" is not installed, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-238201`

### Rule: The Ubuntu operating system must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-238201r958452_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "use_mappers" is set to "pwent" in "/etc/pam_pkcs11/pam_pkcs11.conf" file: $ grep use_mappers /etc/pam_pkcs11/pam_pkcs11.conf use_mappers = pwent If "use_mappers" is not found or the list does not contain "pwent" this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-238202`

### Rule: The Ubuntu operating system must enforce 24 hours/1 day as the minimum password lifetime. Passwords for new users must have a 24 hours/1 day minimum password lifetime restriction.

**Rule ID:** `SV-238202r1015140_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces a 24 hours/1 day minimum password lifetime for new user accounts by running the following command: $ grep -i ^pass_min_days /etc/login.defs PASS_MIN_DAYS 1 If the "PASS_MIN_DAYS" parameter value is less than "1" or is commented out, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-238203`

### Rule: The Ubuntu operating system must enforce a 60-day maximum password lifetime restriction. Passwords for new users must have a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-238203r1038967_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces a 60-day maximum password lifetime for new user accounts by running the following command: $ grep -i ^pass_max_days /etc/login.defs PASS_MAX_DAYS 60 If the "PASS_MAX_DAYS" parameter value is greater than 60, or commented out, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-238204`

### Rule: Ubuntu operating systems when booted must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-238204r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to verify the encrypted password is set: $ sudo grep -i password /boot/grub/grub.cfg password_pbkdf2 root grub.pbkdf2.sha512.10000.MFU48934NJA87HF8NSD34493GDHF84NG If the root password entry does not begin with "password_pbkdf2", this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-238205`

### Rule: The Ubuntu operating system must uniquely identify interactive users.

**Rule ID:** `SV-238205r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system contains no duplicate User IDs (UIDs) for interactive users with the following command: $ awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced and the accounts listed are interactive user accounts, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-238206`

### Rule: The Ubuntu operating system must ensure only users who need access to security functions are part of sudo group.

**Rule ID:** `SV-238206r958518_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. The Ubuntu operating system restricts access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the sudo group has only members who should have access to security functions. $ grep sudo /etc/group sudo:x:27:foo If the sudo group contains users not needing access to security functions, this is a finding.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-238207`

### Rule: The Ubuntu operating system must automatically terminate a user session after inactivity timeouts have expired.

**Rule ID:** `SV-238207r1069086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific operating system functionality where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system automatically terminates a user session after inactivity timeouts have expired. Check that the "TMOUT" environment variable is set in the "/etc/bash.bashrc" file or in any file inside the "/etc/profile.d/" directory by performing the following command: $ sudo grep -E "\bTMOUT=[0-9]+" /etc/bash.bashrc /etc/profile.d/* TMOUT=600 If "TMOUT" is not set, or if the value is "0" or is commented out, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-238208`

### Rule: The Ubuntu operating system must require users to reauthenticate for privilege escalation or when changing roles.

**Rule ID:** `SV-238208r1101674_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/sudoers" file has no occurrences of "!authenticate" by running the following command: $ sudo egrep -iR '!authenticate' /etc/sudoers /etc/sudoers.d/ If any occurrences of "!authenticate" return from the command, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-238209`

### Rule: The Ubuntu operating system default filesystem permissions must be defined in such a way that all authenticated users can read and modify only their own files.

**Rule ID:** `SV-238209r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system defines default permissions for all authenticated users in such a way that the user can read and modify only their own files. Verify the Ubuntu operating system defines default permissions for all authenticated users with the following command: $ grep -i "umask" /etc/login.defs UMASK 077 If the "UMASK" variable is set to "000", this is a finding with the severity raised to a CAT I. If the value of "UMASK" is not set to "077", is commented out, or is missing completely, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-238210`

### Rule: The Ubuntu operating system must implement smart card logins for multifactor authentication for local and network access to privileged and nonprivileged accounts.

**Rule ID:** `SV-238210r1015143_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) something a user knows (e.g., password/PIN); 2) something a user has (e.g., cryptographic identification device, token); and 3) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD CAC with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has the packages required for multifactor authentication installed with the following commands: $ dpkg -l | grep libpam-pkcs11 ii libpam-pkcs11 0.6.8-4 amd64 Fully featured PAM module for using PKCS#11 smart cards If the "libpam-pkcs11" package is not installed, this is a finding. Verify the sshd daemon allows public key authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*pubkeyauthentication' PubkeyAuthentication yes If this option is set to "no" or is missing, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-238211`

### Rule: The Ubuntu operating system must use strong authenticators in establishing nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-238211r958510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to use strong authenticators in the establishment of nonlocal maintenance and diagnostic maintenance. Verify that "UsePAM" is set to "yes" in "/etc/ssh/sshd_config: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*usepam' UsePAM yes If "UsePAM" is not set to "yes", this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-238212`

### Rule: The Ubuntu operating system must immediately terminate all network connections associated with SSH traffic after a period of inactivity.

**Rule ID:** `SV-238212r1015158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific Ubuntu operating system functionality where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all network connections associated with SSH traffic automatically terminate after a period of inactivity. Verify the "ClientAliveCountMax" variable is set in the "/etc/ssh/sshd_config" file by performing the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientalivecountmax' ClientAliveCountMax 1 If "ClientAliveCountMax" is not set, is not set to "1", or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-238213`

### Rule: The Ubuntu operating system must immediately terminate all network connections associated with SSH traffic at the end of the session or after 10 minutes of inactivity.

**Rule ID:** `SV-238213r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all network connections associated with SSH traffic are automatically terminated at the end of the session or after 10 minutes of inactivity. Verify the "ClientAliveInterval" variable is set to a value of "600" or less by performing the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientaliveinterval' ClientAliveInterval 600 If "ClientAliveInterval" does not exist, is not set to a value of "600" or less in "/etc/ssh/sshd_config", or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-238214`

### Rule: The Ubuntu operating system must display the Standard Mandatory DOD Notice and Consent Banner before granting any local or remote connection to the system.

**Rule ID:** `SV-238214r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-OS-000228-GPOS-00088, SRG-OS-000023-GPOS-00006</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the Ubuntu operating system via an SSH logon with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*banner' /etc/ssh/sshd_config:Banner /etc/issue.net The command will return the banner option along with the name of the file that contains the SSH banner. If the line is commented out, this is a finding. If conflicting results are returned, this is a finding. Verify the specified banner file matches the Standard Mandatory DOD Notice and Consent Banner exactly: $ cat /etc/issue.net "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the banner text does not match the Standard Mandatory DOD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-238215`

### Rule: The Ubuntu operating system must use SSH to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-238215r958908_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH package is installed with the following command: $ sudo dpkg -l | grep openssh ii openssh-client 1:7.6p1-4ubuntu0.1 amd64 secure shell (SSH) client, for secure access to remote machines ii openssh-server 1:7.6p1-4ubuntu0.1 amd64 secure shell (SSH) server, for secure access from remote machines ii openssh-sftp-server 1:7.6p1-4ubuntu0.1 amd64 secure shell (SSH) sftp server module, for SFTP access from remote machines If the "openssh" server package is not installed, this is a finding. Verify the "sshd.service" is loaded and active with the following command: $ sudo systemctl status sshd.service | egrep -i "(active|loaded)" Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled) Active: active (running) since Thu 2019-01-24 22:52:58 UTC; 1 weeks 3 days ago If "sshd.service" is not active or loaded, this is a finding.

## Group: SRG-OS-000424-GPOS-00188

**Group ID:** `V-238216`

### Rule: The Ubuntu operating system must configure the SSH daemon to use Message Authentication Codes (MACs) employing FIPS 140-2 approved cryptographic hashes to prevent the unauthorized disclosure of information and/or detect changes to information during transmission.

**Rule ID:** `SV-238216r971547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Encrypting information for transmission protects information from unauthorized disclosure and modification. Cryptographic mechanisms implemented to protect information integrity include, for example, cryptographic hash functions which have common application in digital signatures, checksums, and message authentication codes. Satisfies: SRG-OS-000424-GPOS-00188, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon is configured to only use MACs that employ FIPS 140-2 approved ciphers with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*macs' MACs hmac-sha2-512,hmac-sha2-256 If any ciphers other than "hmac-sha2-512" or "hmac-sha2-256" are listed, the order differs from the example above, or the returned line is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000424-GPOS-00188

**Group ID:** `V-238217`

### Rule: The Ubuntu operating system must configure the SSH daemon to use FIPS 140-2 approved ciphers to prevent the unauthorized disclosure of information and/or detect changes to information during transmission.

**Rule ID:** `SV-238217r971547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Encrypting information for transmission protects information from unauthorized disclosure and modification. Cryptographic mechanisms implemented to protect information integrity include, for example, cryptographic hash functions which have common application in digital signatures, checksums, and message authentication codes. By specifying a cipher list with the order of ciphers being in a "strongest to weakest" orientation, the system will automatically attempt to use the strongest cipher for securing SSH connections. Satisfies: SRG-OS-000424-GPOS-00188, SRG-OS-000033-GPOS-00014, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon is configured to only implement FIPS-approved algorithms by running the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*ciphers' Ciphers aes256-ctr,aes192-ctr,aes128-ctr If any ciphers other than "aes256-ctr", "aes192-ctr", or "aes128-ctr" are listed, the order differs from the example above, the "Ciphers" keyword is missing, or the returned line is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-238218`

### Rule: The Ubuntu operating system must not allow unattended or automatic login via SSH.

**Rule ID:** `SV-238218r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts Ubuntu operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that unattended or automatic login via SSH is disabled with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iEH '^\s*(permit(.*?)(passwords|environment))' PermitEmptyPasswords no PermitUserEnvironment no If "PermitEmptyPasswords" or "PermitUserEnvironment" keywords are not set to "no", are missing completely, or are commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-238219`

### Rule: The Ubuntu operating system must be configured so that remote X connections are disabled, unless to fulfill documented and validated mission requirements.

**Rule ID:** `SV-238219r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The security risk of using X11 forwarding is that the client's X11 display server may be exposed to attack when the SSH client requests forwarding. A System Administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a ''no'' setting. X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user's X11 authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring if the ForwardX11Trusted option is also enabled. If X11 services are not required for the system's intended function, they should be disabled or restricted as appropriate to the system’s needs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that X11Forwarding is disabled with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11forwarding' X11Forwarding no If the "X11Forwarding" keyword is set to "yes" and is not documented with the information system security officer (ISSO) as an operational requirement or is missing, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-238220`

### Rule: The Ubuntu operating system SSH daemon must prevent remote hosts from connecting to the proxy display.

**Rule ID:** `SV-238220r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the sshd proxy display is configured to listen on the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the DISPLAY environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon prevents remote hosts from connecting to the proxy display. Check the SSH X11UseLocalhost setting with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11uselocalhost' X11UseLocalhost yes If the "X11UseLocalhost" keyword is set to "no", is missing, or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-238221`

### Rule: The Ubuntu operating system must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-238221r1015144_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces password complexity by requiring that at least one upper-case character be used. Determine if the field "ucredit" is set in the "/etc/security/pwquality.conf" file with the following command: $ grep -i "ucredit" /etc/security/pwquality.conf ucredit=-1 If the "ucredit" parameter is greater than "-1" or is commented out, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-238222`

### Rule: The Ubuntu operating system must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-238222r1015145_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces password complexity by requiring that at least one lower-case character be used. Determine if the field "lcredit" is set in the "/etc/security/pwquality.conf" file with the following command: $ grep -i "lcredit" /etc/security/pwquality.conf lcredit=-1 If the "lcredit" parameter is greater than "-1" or is commented out, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-238223`

### Rule: The Ubuntu operating system must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-238223r1015146_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces password complexity by requiring that at least one numeric character be used. Determine if the field "dcredit" is set in the "/etc/security/pwquality.conf" file with the following command: $ grep -i "dcredit" /etc/security/pwquality.conf dcredit=-1 If the "dcredit" parameter is greater than "-1" or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-238224`

### Rule: The Ubuntu operating system must require the change of at least 8 characters when passwords are changed.

**Rule ID:** `SV-238224r1015147_rule`
**Severity:** low

**Description:**
<VulnDiscussion> If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least 8 characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system requires the change of at least eight characters when passwords are changed. Determine if the field "difok" is set in the "/etc/security/pwquality.conf" file with the following command: $ grep -i "difok" /etc/security/pwquality.conf difok=8 If the "difok" parameter is less than "8" or is commented out, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-238225`

### Rule: The Ubuntu operating system must enforce a minimum 15-character password length.

**Rule ID:** `SV-238225r1015148_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the pwquality configuration file enforces a minimum 15-character password length by running the following command: $ grep -i minlen /etc/security/pwquality.conf minlen=15 If "minlen" parameter value is not "15" or higher or is commented out, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-238226`

### Rule: The Ubuntu operating system must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-238226r1015149_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the field "ocredit" is set in the "/etc/security/pwquality.conf" file with the following command: $ grep -i "ocredit" /etc/security/pwquality.conf ocredit=-1 If the "ocredit" parameter is greater than "-1" or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-238227`

### Rule: The Ubuntu operating system must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-238227r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system uses the "cracklib" library to prevent the use of dictionary words with the following command: $ grep dictcheck /etc/security/pwquality.conf dictcheck=1 If the "dictcheck" parameter is not set to "1" or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-238228`

### Rule: The Ubuntu operating system must be configured so that when passwords are changed or new passwords are established, pwquality must be used.

**Rule ID:** `SV-238228r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has the "libpam-pwquality" package installed by running the following command: $ dpkg -l libpam-pwquality ii libpam-pwquality:amd64 1.4.0-2 amd64 PAM module to check password strength If "libpam-pwquality" is not installed, this is a finding. Verify that the operating system uses "pwquality" to enforce the password complexity rules. Verify the pwquality module is being enforced by the Ubuntu operating system by running the following command: $ grep -i enforcing /etc/security/pwquality.conf enforcing = 1 If the value of "enforcing" is not "1" or the line is commented out, this is a finding. Check for the use of "pwquality" with the following command: $ cat /etc/pam.d/common-password | grep requisite | grep pam_pwquality password requisite pam_pwquality.so retry=3 If no output is returned or the line is commented out, this is a finding. If the value of "retry" is set to "0" or greater than "3", this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-238229`

### Rule: The Ubuntu operating system, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-238229r1069088_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system, for PKI-based authentication, has valid certificates by constructing a certification path to an accepted trust anchor. Determine which pkcs11 module is being used via the "use_pkcs11_module" in "/etc/pam_pkcs11/pam_pkcs11.conf", and then ensure "ca" is enabled in "cert_policy" with the following command: $ sudo grep use_pkcs11_module /etc/pam_pkcs11/pam_pkcs11.conf | sudo awk '/pkcs11_module opensc {/,/}/' /etc/pam_pkcs11/pam_pkcs11.conf | grep cert_policy | grep ca cert_policy = ca,signature,ocsp_on; If "cert_policy" is not set to "ca" or the line is commented out, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-238230`

### Rule: The Ubuntu operating system must implement multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-238230r1015150_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has the packages required for multifactor authentication installed with the following commands: $ dpkg -l | grep libpam-pkcs11 ii libpam-pkcs11 0.6.8-4 amd64 Fully featured PAM module for using PKCS#11 smart cards If the "libpam-pkcs11" package is not installed, this is a finding.

## Group: SRG-OS-000376-GPOS-00161

**Group ID:** `V-238231`

### Rule: The Ubuntu operating system must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-238231r958816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system accepts PIV credentials. Verify the "opensc-pcks11" package is installed on the system with the following command: $ dpkg -l | grep opensc-pkcs11 ii opensc-pkcs11:amd64 0.15.0-1Ubuntu1 amd64 Smart card utilities with support for PKCS#15 compatible cards If the "opensc-pcks11" package is not installed, this is a finding.

## Group: SRG-OS-000377-GPOS-00162

**Group ID:** `V-238232`

### Rule: The Ubuntu operating system must electronically verify Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-238232r1069954_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DOD has mandated the use of the CAC to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system electronically verifies PIV credentials. Verify that certificate status checking for multifactor authentication is implemented with the following command: $ sudo grep use_pkcs11_module /etc/pam_pkcs11/pam_pkcs11.conf | sudo awk '/pkcs11_module opensc {/,/}/' /etc/pam_pkcs11/pam_pkcs11.conf | grep cert_policy | grep ocsp_on cert_policy = ca,signature,ocsp_on; If "cert_policy" is not set to "ocsp_on", or the line is commented out, this is a finding.

## Group: SRG-OS-000384-GPOS-00167

**Group ID:** `V-238233`

### Rule: The Ubuntu operating system for PKI-based authentication, must implement a local cache of revocation data in case of the inability to access revocation information via the network.

**Rule ID:** `SV-238233r1015151_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without configuring a local cache of revocation data, there is the potential to allow access to users who are no longer authorized (users with revoked certificates).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system, for PKI-based authentication, uses local revocation data when unable to access it from the network. Verify that "crl_offline" or "crl_auto" is part of the "cert_policy" definition in "/etc/pam_pkcs11/pam_pkcs11.conf" using the following command: # sudo grep cert_policy /etc/pam_pkcs11/pam_pkcs11.conf | grep -E -- 'crl_auto|crl_offline' cert_policy = ca,signature,ocsp_on,crl_auto; If "cert_policy" is not set to include "crl_auto" or "crl_offline", this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-238234`

### Rule: The Ubuntu operating system must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-238234r1015152_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. Satisfies: SRG-OS-000077-GPOS-00045, SRG-OS-000073-GPOS-00041</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system prevents passwords from being reused for a minimum of five generations by running the following command: $ grep -i remember /etc/pam.d/common-password password [success=1 default=ignore] pam_unix.so obscure sha512 shadow remember=5 rounds=5000 If the "remember" parameter value is not greater than or equal to "5", is commented out, or is not set at all, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-238235`

### Rule: The Ubuntu operating system must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts have been made.

**Rule ID:** `SV-238235r1069092_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system utilizes the "pam_faillock" module with the following command: $ grep faillock /etc/pam.d/common-auth auth [default=die] pam_faillock.so authfail auth sufficient pam_faillock.so authsucc If the pam_faillock.so module is not present in the "/etc/pam.d/common-auth" file, this is a finding. Verify the pam_faillock module is configured to use the following options: $ sudo egrep 'silent|audit|deny|fail_interval|unlock_time' /etc/security/faillock.conf audit silent deny = 3 fail_interval = 900 unlock_time = 0 If the "silent" keyword is missing or commented out, this is a finding. If the "audit" keyword is missing or commented out, this is a finding. If the "deny" keyword is missing, commented out, or set to a value greater than "3", this is a finding. If the "fail_interval" keyword is missing, commented out, or set to a value greater than "900", this is a finding. If the "unlock_time" keyword is missing, commented out, or not set to "0", this is a finding.

## Group: SRG-OS-000446-GPOS-00200

**Group ID:** `V-238236`

### Rule: The Ubuntu operating system must be configured so that the script which runs each 30 days or less to check file integrity is the default one.

**Rule ID:** `SV-238236r958946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include, for example, electronic alerts to System Administrators, messages to local computer consoles, and/or hardware indications, such as lights. This requirement applies to the Ubuntu operating system performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Advanced Intrusion Detection Environment (AIDE) default script used to check file integrity each 30 days or less is unchanged. Download the original aide-common package in the /tmp directory: $ cd /tmp; apt download aide-common Fetch the SHA1 of the original script file: $ dpkg-deb --fsys-tarfile /tmp/aide-common_*.deb | tar -xO ./usr/share/aide/config/cron.daily/aide | sha1sum 32958374f18871e3f7dda27a58d721f471843e26 - Compare with the SHA1 of the file in the daily or monthly cron directory: $ sha1sum /etc/cron.{daily,monthly}/aide 2>/dev/null 32958374f18871e3f7dda27a58d721f471843e26 /etc/cron.daily/aide If there is no AIDE script file in the cron directories, or the SHA1 value of at least one file in the daily or monthly cron directory does not match the SHA1 of the original, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-238237`

### Rule: The Ubuntu operating system must enforce a delay of at least 4 seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-238237r991588_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces a delay of at least 4 seconds between logon prompts following a failed logon attempt with the following command: $ grep pam_faildelay /etc/pam.d/common-auth auth required pam_faildelay.so delay=4000000 If the line is not present or is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-238238`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-238238r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd". Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep passwd -w /etc/passwd -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-238239`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.

**Rule ID:** `SV-238239r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group". Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep group -w /etc/group -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-238240`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-238240r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow". Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep shadow -w /etc/shadow -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-238241`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow.

**Rule ID:** `SV-238241r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow". Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep gshadow -w /etc/gshadow -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-238242`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/opasswd.

**Rule ID:** `SV-238242r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/security/opasswd". Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep opasswd -w /etc/security/opasswd -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-238243`

### Rule: The Ubuntu operating system must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-238243r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SA and ISSO (at a minimum) are notified in the event of an audit processing failure with the following command: $ sudo grep '^action_mail_acct = root' /etc/audit/auditd.conf action_mail_acct = <administrator_account> If the value of the "action_mail_acct" keyword is not set to an accounts for security personnel, the "action_mail_acct" keyword is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-238244`

### Rule: The Ubuntu operating system must shut down by default upon audit failure (unless availability is an overriding concern).

**Rule ID:** `SV-238244r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system takes the appropriate action when the audit storage volume is full with the following command: $ sudo grep '^disk_full_action' /etc/audit/auditd.conf disk_full_action = HALT If the value of the "disk_full_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-238245`

### Rule: The Ubuntu operating system must be configured so that audit log files are not read or write-accessible by unauthorized users.

**Rule ID:** `SV-238245r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log files have a mode of "0600" or less permissive. Determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, determine if the audit log files have a mode of "0600" or less by using the following command: $ sudo stat -c "%n %a" /var/log/audit/* /var/log/audit/audit.log 600 If the audit log files have a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-238246`

### Rule: The Ubuntu operating system must be configured to permit only authorized users ownership of the audit log files.

**Rule ID:** `SV-238246r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log files are owned by "root" account. Determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, determine if the audit log files are owned by the "root" user by using the following command: $ sudo stat -c "%n %U" /var/log/audit/* /var/log/audit/audit.log root If the audit log files are owned by an user other than "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-238247`

### Rule: The Ubuntu operating system must permit only authorized groups ownership of the audit log files.

**Rule ID:** `SV-238247r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group owner is set to own newly created audit logs in the audit configuration file with the following command: $ sudo grep -iw log_group /etc/audit/auditd.conf log_group = root If the value of the "log_group" parameter is other than "root", this is a finding. Determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, determine if the audit log files are owned by the "root" group by using the following command: $ sudo stat -c "%n %G" /var/log/audit/* /var/log/audit/audit.log root If the audit log files are owned by a group other than "root", this is a finding.

## Group: SRG-OS-000059-GPOS-00029

**Group ID:** `V-238248`

### Rule: The Ubuntu operating system must be configured so that the audit log directory is not write-accessible by unauthorized users.

**Rule ID:** `SV-238248r958438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the operating system must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log directory has a mode of "0750" or less permissive. Determine where the audit logs are stored with the following command: $ sudo grep -iw ^log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, determine if the directory has a mode of "0750" or less by using the following command: $ sudo stat -c "%n %a" /var/log/audit /var/log/audit/* /var/log/audit 750 /var/log/audit/audit.log 600 If the audit log directory has a mode more permissive than "0750", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-238249`

### Rule: The Ubuntu operating system must be configured so that audit configuration files are not write-accessible by unauthorized users.

**Rule ID:** `SV-238249r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/rules.d/*", and "/etc/audit/auditd.conf" files have a mode of "0640" or less permissive by using the following command: $ sudo ls -al /etc/audit/ /etc/audit/rules.d/ /etc/audit/: -rw-r----- 1 root root 804 Nov 25 11:01 auditd.conf -rw-r----- 1 root root 9128 Dec 27 09:56 audit.rules -rw-r----- 1 root root 9373 Dec 27 09:56 audit.rules.prev -rw-r----- 1 root root 127 Feb 7 2018 audit-stop.rules drwxr-x--- 2 root root 4096 Dec 27 09:56 rules.d /etc/audit/rules.d/: -rw-r----- 1 root root 10357 Dec 27 09:56 stig.rules If "/etc/audit/audit.rule","/etc/audit/rules.d/*", or "/etc/audit/auditd.conf" file have a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-238250`

### Rule: The Ubuntu operating system must permit only authorized accounts to own the audit configuration files.

**Rule ID:** `SV-238250r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/rules.d/*" and "/etc/audit/auditd.conf" files are owned by root account by using the following command: $ sudo ls -al /etc/audit/ /etc/audit/rules.d/ /etc/audit/: drwxr-x--- 3 root root 4096 Nov 25 11:02 . drwxr-xr-x 130 root root 12288 Dec 19 13:42 .. -rw-r----- 1 root root 804 Nov 25 11:01 auditd.conf -rw-r----- 1 root root 9128 Dec 27 09:56 audit.rules -rw-r----- 1 root root 9373 Dec 27 09:56 audit.rules.prev -rw-r----- 1 root root 127 Feb 7 2018 audit-stop.rules drwxr-x--- 2 root root 4096 Dec 27 09:56 rules.d /etc/audit/rules.d/: drwxr-x--- 2 root root 4096 Dec 27 09:56 . drwxr-x--- 3 root root 4096 Nov 25 11:02 .. -rw-r----- 1 root root 10357 Dec 27 09:56 stig.rules If the "/etc/audit/audit.rules", "/etc/audit/rules.d/*", or "/etc/audit/auditd.conf" file is owned by a user other than "root", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-238251`

### Rule: The Ubuntu operating system must permit only authorized groups to own the audit configuration files.

**Rule ID:** `SV-238251r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/rules.d/*", and "/etc/audit/auditd.conf" files are owned by root group by using the following command: $ sudo ls -al /etc/audit/ /etc/audit/rules.d/ /etc/audit/: -rw-r----- 1 root root 804 Nov 25 11:01 auditd.conf -rw-r----- 1 root root 9128 Dec 27 09:56 audit.rules -rw-r----- 1 root root 9373 Dec 27 09:56 audit.rules.prev -rw-r----- 1 root root 127 Feb 7 2018 audit-stop.rules drwxr-x--- 2 root root 4096 Dec 27 09:56 rules.d /etc/audit/rules.d/: -rw-r----- 1 root root 10357 Dec 27 09:56 stig.rules If the "/etc/audit/audit.rules", "/etc/audit/rules.d/*", or "/etc/audit/auditd.conf" file is owned by a group other than "root", this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238252`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the su command.

**Rule ID:** `SV-238252r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records upon successful/unsuccessful attempts to use the "su" command. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep '/bin/su' -a always,exit -S all -F path=/bin/su -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-priv_change If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238253`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chfn command.

**Rule ID:** `SV-238253r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records upon successful/unsuccessful attempts to use the "chfn" command. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep '/usr/bin/chfn' -a always,exit -S all -F path=/usr/bin/chfn -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-chfn If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238254`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the mount command.

**Rule ID:** `SV-238254r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records upon successful/unsuccessful attempts to use the "mount" command. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep '/usr/bin/mount' -a always,exit -S all -F path=/usr/bin/mount -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-mount If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238255`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the umount command.

**Rule ID:** `SV-238255r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records upon successful/unsuccessful attempts to use the "umount" command Check the configured audit rules with the following commands: $ sudo auditctl -l | grep '/usr/bin/umount' -a always,exit -S all -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-umount If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238256`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the ssh-agent command.

**Rule ID:** `SV-238256r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "ssh-agent" command. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep '/usr/bin/ssh-agent' -a always,exit -S all -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-ssh If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238257`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the ssh-keysign command.

**Rule ID:** `SV-238257r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "ssh-keysign" command. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep ssh-keysign -a always,exit -S all -F path=/usr/lib/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-ssh If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238258`

### Rule: The Ubuntu operating system must generate audit records for any use of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls.

**Rule ID:** `SV-238258r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep xattr -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -k perm_mod -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod If the command does not return audit rules for the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr" and "lremovexattr" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238264`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chown, fchown, fchownat, and lchown system calls.

**Rule ID:** `SV-238264r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "chown", "fchown", "fchownat", and "lchown" system calls. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep chown -a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=-1 -k perm_chng -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=-1 -k perm_chng If the command does not return audit rules for the "chown", "fchown", "fchownat", and "lchown" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238268`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chmod, fchmod, and fchmodat system calls.

**Rule ID:** `SV-238268r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "chmod", "fchmod", and "fchmodat" system calls. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep chmod -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -k perm_chng -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -k perm_chng If the command does not return audit rules for the "chmod", "fchmod" and "fchmodat" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238271`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the creat, open, openat, open_by_handle_at, truncate, and ftruncate system calls.

**Rule ID:** `SV-238271r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon unsuccessful attempts to use the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" system calls. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep 'open\|truncate\|creat' -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=-1 -k perm_access -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=-1 -k perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=-1 -k perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=-1 -k perm_access If the command does not return audit rules for the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238277`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the sudo command.

**Rule ID:** `SV-238277r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "sudo" command. Check the configured audit rules with the following command: $ sudo auditctl -l | grep /usr/bin/sudo -a always,exit -S all -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238278`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the sudoedit command.

**Rule ID:** `SV-238278r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "sudoedit" command. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep /usr/bin/sudoedit -a always,exit -S all -F path=/usr/bin/sudoedit -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238279`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chsh command.

**Rule ID:** `SV-238279r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "chsh" command. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep chsh -a always,exit -S all -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Notes: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238280`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the newgrp command.

**Rule ID:** `SV-238280r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "newgrp" command. Check the configured audit rules with the following commands: $ sudo auditctl -l | grep newgrp -a always,exit -S all -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238281`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chcon command.

**Rule ID:** `SV-238281r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "chcon" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep chcon -a always,exit -S all -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238282`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the apparmor_parser command.

**Rule ID:** `SV-238282r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "apparmor_parser" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep apparmor_parser -a always,exit -S all -F path=/sbin/apparmor_parser -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238283`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the setfacl command.

**Rule ID:** `SV-238283r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "setfacl" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep setfacl -a always,exit -S all -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238284`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chacl command.

**Rule ID:** `SV-238284r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "chacl" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep chacl -a always,exit -S all -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238285`

### Rule: The Ubuntu operating system must generate audit records for the use and modification of the tallylog file.

**Rule ID:** `SV-238285r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful modifications to the "tallylog" file. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep tallylog -w /var/log/tallylog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238286`

### Rule: The Ubuntu operating system must generate audit records for the use and modification of faillog file.

**Rule ID:** `SV-238286r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful modifications to the "faillog" file. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep faillog -w /var/log/faillog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238287`

### Rule: The Ubuntu operating system must generate audit records for the use and modification of the lastlog file.

**Rule ID:** `SV-238287r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful modifications to the "lastlog" file occur. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep lastlog -w /var/log/lastlog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238288`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the passwd command.

**Rule ID:** `SV-238288r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "passwd" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep -w passwd -a always,exit -S all -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-passwd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238289`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the unix_update command.

**Rule ID:** `SV-238289r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "unix_update" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep -w unix_update -a always,exit -S all -F path=/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238290`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the gpasswd command.

**Rule ID:** `SV-238290r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "gpasswd" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep -w gpasswd -a always,exit -S all -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-gpasswd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238291`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chage command.

**Rule ID:** `SV-238291r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "chage" command Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep -w chage -a always,exit -S all -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-chage If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238292`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the usermod command.

**Rule ID:** `SV-238292r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "usermod" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep -w usermod -a always,exit -S all -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-usermod If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238293`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the crontab command.

**Rule ID:** `SV-238293r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "crontab" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep -w crontab -a always,exit -S all -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-crontab If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238294`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the pam_timestamp_check command.

**Rule ID:** `SV-238294r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "pam_timestamp_check" command. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep -w pam_timestamp_check -a always,exit -S all -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-pam_timestamp_check If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238295`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the init_module and finit_module syscalls.

**Rule ID:** `SV-238295r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000471-GPOS-00216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record for any successful/unsuccessful attempts to use the "init_module" and "finit_module" syscalls. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep init_module -a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=-1 -k module_chng -a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=-1 -k module_chng If the command does not return audit rules for the "init_module" and "finit_module" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-238297`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the delete_module syscall.

**Rule ID:** `SV-238297r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record for any successful/unsuccessful attempts to use the "delete_module" syscall. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep -w delete_module -a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=-1 -k module_chng -a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=-1 -k module_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Notes: - For 32-bit architectures, only the 32-bit specific output lines from the commands are required. - The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000122-GPOS-00063

**Group ID:** `V-238298`

### Rule: The Ubuntu operating system must produce audit records and reports containing information to establish when, where, what type, the source, and the outcome for all DoD-defined auditable events and actions in near real time.

**Rule ID:** `SV-238298r958506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the when, where, type, source, and outcome of events that occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Successful incident response and auditing relies on timely, accurate system information and analysis in order to allow the organization to identify and respond to potential incidents in a proficient manner. If the operating system does not provide the ability to centrally review the operating system logs, forensic analysis is negatively impacted. Associating event types with detected events in the Ubuntu operating system audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system. Satisfies: SRG-OS-000122-GPOS-00063, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00020, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000062-GPOS-00031, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit service is configured to produce audit records with the following command: $ dpkg -l | grep auditd If the "auditd" package is not installed, this is a finding. Verify the audit service is enabled with the following command: $ systemctl is-enabled auditd.service If the command above returns "disabled", this is a finding. Verify the audit service is properly running and active on the system with the following command: $ systemctl is-active auditd.service active If the command above returns "inactive", this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-238299`

### Rule: The Ubuntu operating system must initiate session audits at system start-up.

**Rule ID:** `SV-238299r1069095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the start-up process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enables auditing at system startup. Verify the auditing is enabled in grub with the following command: $ sudo grep "^\s*linux" /boot/grub/grub.cfg linux /boot/vmlinuz-5.4.0-31-generic root=UUID=74d13bcd-6ebd-4493-b5d2-3ebc37d01702 ro audit=1 linux /boot/vmlinuz-5.4.0-31-generic root=UUID=74d13bcd-6ebd-4493-b5d2-3ebc37d01702 ro recovery nomodeset audit=1 If any linux lines do not contain "audit=1", this is a finding. Note: Output may vary by system.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-238300`

### Rule: The Ubuntu operating system must configure audit tools with a mode of 0755 or less permissive.

**Rule ID:** `SV-238300r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the audit tools to have a file permission of 0755 or less to prevent unauthorized access by running the following command: $ stat -c "%n %a" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/audispd /sbin/augenrules /sbin/auditctl 755 /sbin/aureport 755 /sbin/ausearch 755 /sbin/autrace 755 /sbin/auditd 755 /sbin/audispd 755 /sbin/augenrules 755 If any of the audit tools have a mode more permissive than 0755, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-238301`

### Rule: The Ubuntu operating system must configure audit tools to be owned by root.

**Rule ID:** `SV-238301r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the audit tools to be owned by root to prevent any unauthorized access. Check the ownership by running the following command: $ stat -c "%n %U" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/audispd /sbin/augenrules /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/audispd root /sbin/augenrules root If any of the audit tools are not owned by root, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-238302`

### Rule: The Ubuntu operating system must configure the audit tools to be group-owned by root.

**Rule ID:** `SV-238302r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the audit tools to be group-owned by root to prevent any unauthorized access. Check the group ownership by running the following command: $ stat -c "%n %G" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/audispd /sbin/augenrules /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/audispd root /sbin/augenrules root If any of the audit tools are not group-owned by root, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-238303`

### Rule: The Ubuntu operating system must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-238303r991567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed in order to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is properly configured to use cryptographic mechanisms to protect the integrity of audit tools. Check the selection lines that AIDE is configured to add/check with the following command: $ egrep '(\/sbin\/(audit|au))' /etc/aide/aide.conf /sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/audispd p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512 If any of the seven audit tools do not have appropriate selection lines, this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-238304`

### Rule: The Ubuntu operating system must prevent all software from executing at higher privilege levels than users executing the software and the audit system must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-238304r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review. Satisfies: SRG-OS-000326-GPOS-00126, SRG-OS-000327-GPOS-00127</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system audits the execution of privilege functions by auditing the "execve" system call. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep execve -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=execpriv If the command does not return lines that match the example or the lines are commented out, this is a finding. Notes: - For 32-bit architectures, only the 32-bit specific output lines from the commands are required. - The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-238305`

### Rule: The Ubuntu operating system must allocate audit record storage capacity to store at least one weeks' worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-238305r958752_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system allocates audit record storage capacity to store at least one week's worth of audit records when audit records are not immediately sent to a central audit record storage facility. Determine which partition the audit records are being written to with the following command: $ sudo grep ^log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition that audit records are written to (with the example being "/var/log/audit/") with the following command: $ sudo df –h /var/log/audit/ /dev/sda2 24G 10.4G 13.6G 43% /var/log/audit If the audit records are not written to a partition made specifically for audit records ("/var/log/audit" is a separate partition), determine the amount of space being used by other files in the partition with the following command: $ sudo du –sh [audit_partition] 1.8G /var/log/audit Note: The partition size needed to capture a week's worth of audit records is based on the activity level of the system and the total storage capacity available. In normal circumstances, 10.0 GB of storage space for audit records will be sufficient. If the audit record partition is not allocated for sufficient storage capacity, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-238306`

### Rule: The Ubuntu operating system audit event multiplexor must be configured to off-load audit logs onto a different system or storage media from the system being audited.

**Rule ID:** `SV-238306r958754_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit event multiplexor is configured to offload audit records to a different system or storage media from the system being audited. Check that audisp-remote plugin is installed: $ sudo dpkg -s audispd-plugins If status is "not installed", this is a finding. Check that the records are being offloaded to a remote server with the following command: $ sudo grep -i active /etc/audisp/plugins.d/au-remote.conf active = yes If "active" is not set to "yes", or the line is commented out, this is a finding. Check that audisp-remote plugin is configured to send audit logs to a different system: $ sudo grep -i ^remote_server /etc/audisp/audisp-remote.conf remote_server = 192.168.122.126 If the "remote_server" parameter is not set, is set with a local address, or is set with an invalid address, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-238307`

### Rule: The Ubuntu operating system must immediately notify the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of the repository maximum audit record storage capacity.

**Rule ID:** `SV-238307r971542_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75% utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of the repository maximum audit record storage capacity with the following command: $ sudo grep ^space_left_action /etc/audit/auditd.conf space_left_action email $ sudo grep ^space_left /etc/audit/auditd.conf space_left 250000 If the "space_left" parameter is missing, set to blanks, or set to a value less than 25% of the space free in the allocated audit record storage, this is a finding. If the "space_left_action" parameter is missing or set to blanks, this is a finding. If the "space_left_action" is set to "syslog", the system logs the event but does not generate a notification, and this is a finding. If the "space_left_action" is set to "exec", the system executes a designated script. If this script informs the SA of the event, this is not a finding. If the "space_left_action" is set to "email", check the value of the "action_mail_acct" parameter with the following command: $ sudo grep ^action_mail_acct /etc/audit/auditd.conf action_mail_acct root@localhost The "action_mail_acct" parameter, if missing, defaults to "root". If the "action_mail_acct parameter" is not set to the email address of the SA(s) and/or ISSO, this is a finding. Note: If the email address of the System Administrator is on a remote system, a mail package must be available.

## Group: SRG-OS-000359-GPOS-00146

**Group ID:** `V-238308`

### Rule: The Ubuntu operating system must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-238308r958788_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the operating system include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the time zone is configured to use UTC or GMT, run the following command. $ timedatectl status | grep -i "time zone" Timezone: UTC (UTC, +0000) If "Timezone" is not set to UTC or GMT, this is a finding.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-238309`

### Rule: The Ubuntu operating system must generate audit records for privileged activities, nonlocal maintenance, diagnostic sessions and other system-level access.

**Rule ID:** `SV-238309r958846_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If events associated with nonlocal administrative access or diagnostic sessions are not logged, a major tool for assessing and investigating attacks would not be available. This requirement addresses auditing-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational information systems. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system, for example, the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch. Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system audits activities performed during nonlocal maintenance and diagnostic sessions. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep sudo.log -w /var/log/sudo.log -p wa -k maintenance If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-238310`

### Rule: The Ubuntu operating system must generate audit records for any successful/unsuccessful use of unlink, unlinkat, rename, renameat, and rmdir system calls.

**Rule ID:** `SV-238310r991577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for any successful/unsuccessful use of "unlink", "unlinkat", "rename", "renameat", and "rmdir" system calls. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep 'unlink\|rename\|rmdir' -a always,exit -F arch=b64 -S unlink,unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=-1 -F key=delete -a always,exit -F arch=b32 -S unlink,unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=-1 -F key=delete If the command does not return audit rules for the "unlink", "unlinkat", "rename", "renameat", and "rmdir" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "key" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-238315`

### Rule: The Ubuntu operating system must generate audit records for the /var/log/wtmp file.

**Rule ID:** `SV-238315r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records showing start and stop times for user access to the system via the "/var/log/wtmp" file. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep '/var/log/wtmp' -w /var/log/wtmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-238316`

### Rule: The Ubuntu operating system must generate audit records for the /var/run/utmp file.

**Rule ID:** `SV-238316r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records showing start and stop times for user access to the system via the "/var/run/utmp" file. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep '/var/run/utmp' -w /var/run/utmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-238317`

### Rule: The Ubuntu operating system must generate audit records for the /var/log/btmp file.

**Rule ID:** `SV-238317r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records showing start and stop times for user access to the system via the "/var/log/btmp" file. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep '/var/log/btmp' -w /var/log/btmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-238318`

### Rule: The Ubuntu operating system must generate audit records when successful/unsuccessful attempts to use modprobe command.

**Rule ID:** `SV-238318r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system is configured to audit the execution of the module management program "modprobe" by running the following command: $ sudo auditctl -l | grep "/sbin/modprobe" -w /sbin/modprobe -p x -k modules If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-238319`

### Rule: The Ubuntu operating system must generate audit records when successful/unsuccessful attempts to use the kmod command.

**Rule ID:** `SV-238319r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to audit the execution of the module management program "kmod". Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep kmod -w /bin/kmod -p x -k module If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-238320`

### Rule: The Ubuntu operating system must generate audit records when successful/unsuccessful attempts to use the fdisk command.

**Rule ID:** `SV-238320r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to audit the execution of the partition management program "fdisk". Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep fdisk -w /usr/sbin/fdisk -p x -k fdisk If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-238321`

### Rule: The Ubuntu operating system must have a crontab script running weekly to offload audit events of standalone systems.

**Rule ID:** `SV-238321r959008_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If this is an interconnected system, this is Not Applicable. Verify there is a script that offloads audit data and that script runs weekly. Check if there is a script in the "/etc/cron.weekly" directory that offloads audit data: # sudo ls /etc/cron.weekly audit-offload Check if the script inside the file does offloading of audit logs to external media. If the script file does not exist or does not offload audit logs, this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-238323`

### Rule: The Ubuntu operating system must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-238323r1101671_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Ubuntu operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system limits the number of concurrent sessions to 10 for all accounts and/or account types by running the following command: $ grep maxlogins /etc/security/limits.conf /etc/security/limits.d/*.conf | grep -v '^#' * hard maxlogins 10 If the "maxlogins" item is missing, or the value is not set to 10 or less, or is commented out, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-238324`

### Rule: The Ubuntu operating system must monitor remote access methods.

**Rule ID:** `SV-238324r1069955_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system monitors all remote access methods. Check that remote access methods are being logged by running the following command: $ grep -E -r '^(auth,authpriv\.\*|daemon\.\*)' /etc/rsyslog.* /etc/rsyslog.d/50-default.conf:auth,authpriv.* /var/log/auth.log /etc/rsyslog.d/50-default.conf:daemon.* /var/log/messages If "auth.*", "authpriv.*", or "daemon.*" are not configured to be logged in at least one of the config files, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-238325`

### Rule: The Ubuntu operating system must encrypt all stored passwords with a FIPS 140-2 approved cryptographic hashing algorithm.

**Rule ID:** `SV-238325r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the shadow password suite configuration is set to encrypt passwords with a FIPS 140-2 approved cryptographic hashing algorithm. Check the hashing algorithm that is being used to hash passwords with the following command: $ cat /etc/login.defs | grep -i encrypt_method ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" does not equal SHA512 or greater, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-238326`

### Rule: The Ubuntu operating system must not have the telnet package installed.

**Rule ID:** `SV-238326r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the telnet package is not installed on the Ubuntu operating system by running the following command: $ dpkg -l | grep telnetd If the package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-238327`

### Rule: The Ubuntu operating system must not have the rsh-server package installed.

**Rule ID:** `SV-238327r958478_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the rsh-server package is installed with the following command: $ dpkg -l | grep rsh-server If the rsh-server package is installed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-238328`

### Rule: The Ubuntu operating system must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-238328r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments. Check the firewall configuration for any unnecessary or prohibited functions, ports, protocols, and/or services by running the following command: $ sudo ufw show raw Chain OUTPUT (policy ACCEPT) target prot opt sources destination Chain INPUT (policy ACCEPT 1 packets, 40 bytes) pkts bytes target prot opt in out source destination Chain FORWARD (policy ACCEPT 0 packets, 0 bytes) pkts bytes target prot opt in out source destination Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes) pkts bytes target prot opt in out source destination Ask the System Administrator for the site or program PPSM CLSA. Verify the services allowed by the firewall match the PPSM CLSA. If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-238329`

### Rule: The Ubuntu operating system must prevent direct login into the root account.

**Rule ID:** `SV-238329r1015153_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the UNIX OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the UNIX and Windows operating systems offer a 'switch user' capability allowing users to authenticate with their individual credentials and, when needed, 'switch' to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system prevents direct logins to the root account with the following command: $ sudo passwd -S root root L 04/23/2020 0 99999 7 -1 If the output does not contain "L" in the second field to indicate the account is locked, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-238330`

### Rule: The Ubuntu operating system must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-238330r1015154_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity with the following command: Check the account inactivity value by performing the following command: $ sudo grep INACTIVE /etc/default/useradd INACTIVE=35 If "INACTIVE" is not set to a value 0<[VALUE]<=35, or is commented out, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-238331`

### Rule: The Ubuntu operating system must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-238331r958508_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Temporary accounts are privileged or nonprivileged accounts that are established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not either manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to exploitation by unauthorized users or insider threat actors. Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements. The automatic expiration of temporary accounts may be extended as needed by the circumstances but it must not be extended indefinitely. A documented permanent account should be established for privileged users who need long-term maintenance accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information: $ sudo chage -l <temporary_account_name> | grep -i "account expires" Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-238332`

### Rule: The Ubuntu operating system must set a sticky bit  on all public directories to prevent unauthorized and unintended information transferred via shared system resources.

**Rule ID:** `SV-238332r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all public (world-writeable) directories have the public sticky bit set. Find world-writable directories that lack the sticky bit by running the following command: $ sudo find / -type d -perm -002 ! -perm -1000 If any world-writable directories are found missing the sticky bit, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-238333`

### Rule: The Ubuntu operating system must be configured to use TCP syncookies.

**Rule ID:** `SV-238333r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to use TCP syncookies. Check the value of TCP syncookies with the following command: $ sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 If the value is not "1", this is a finding. Check the saved value of TCP syncookies with the following command: $ sudo grep -i net.ipv4.tcp_syncookies /etc/sysctl.conf /etc/sysctl.d/* | grep -v '#' If no output is returned, this is a finding.

## Group: SRG-OS-000184-GPOS-00078

**Group ID:** `V-238334`

### Rule: The Ubuntu operating system must disable kernel core dumps  so that it can fail to a secure state if system initialization fails, shutdown fails or aborts fail.

**Rule ID:** `SV-238334r958550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system partition.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that kernel core dumps are disabled unless needed. Check if "kdump" service is active with the following command: $ systemctl is-active kdump.service inactive If the "kdump" service is active, ask the SA if the use of the service is required and documented with the ISSO. If the service is active and is not documented, this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-238335`

### Rule: Ubuntu operating systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest.

**Rule ID:** `SV-238335r958552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive and tape drive, when used for backups) within an operating system. This requirement addresses protection of user-generated data, as well as operating system-specific configuration data. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information. Satisfies: SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there is a documented and approved reason for not having data-at-rest encryption, this requirement is Not Applicable. Verify the Ubuntu operating system prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption. Determine the partition layout for the system with the following command: #sudo fdisk -l (..) Disk /dev/vda: 15 GiB, 16106127360 bytes, 31457280 sectors Units: sectors of 1 * 512 = 512 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disklabel type: gpt Disk identifier: 83298450-B4E3-4B19-A9E4-7DF147A5FEFB Device Start End Sectors Size Type /dev/vda1 2048 4095 2048 1M BIOS boot /dev/vda2 4096 2101247 2097152 1G Linux filesystem /dev/vda3 2101248 31455231 29353984 14G Linux filesystem (...) Verify the system partitions are all encrypted with the following command: # more /etc/crypttab Every persistent disk partition present must have an entry in the file. If any partitions other than the boot partition or pseudo file systems (such as /proc or /sys) are not listed, this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-238337`

### Rule: The Ubuntu operating system must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-238337r958564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. The /var/log/btmp, /var/log/wtmp, and /var/log/lastlog files have group write and global read permissions to allow for the lastlog function to perform. Limiting the permissions beyond this configuration will result in the failure of functions that rely on the lastlog database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has all system log files under the "/var/log" directory with a permission set to "640" or less permissive by using the following command: Note: The btmp, wtmp, and lastlog files are excluded. Refer to the Discussion for details. $ sudo find /var/log -perm /137 ! -name '*[bw]tmp' ! -name '*lastlog' -type f -exec stat -c "%n %a" {} \; If the command displays any output, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-238338`

### Rule: The Ubuntu operating system must configure the /var/log directory to be group-owned by syslog.

**Rule ID:** `SV-238338r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the "/var/log" directory to be group-owned by syslog with the following command: $ sudo stat -c "%n %G" /var/log /var/log syslog If the "/var/log" directory is not group-owned by syslog, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-238339`

### Rule: The Ubuntu operating system must configure the /var/log directory to be owned by root.

**Rule ID:** `SV-238339r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the "/var/log" directory to be owned by root with the following command: $ sudo stat -c "%n %U" /var/log /var/log root If the "/var/log" directory is not owned by root, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-238340`

### Rule: The Ubuntu operating system must configure the /var/log directory to have mode "0755" or less permissive.

**Rule ID:** `SV-238340r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the "/var/log" directory with a mode of "755" or less permissive with the following command: Note: If rsyslog is active and enabled on the operating system, this requirement is not applicable. $ stat -c "%n %a" /var/log /var/log 755 If a value of "755" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-238341`

### Rule: The Ubuntu operating system must configure the /var/log/syslog file to be group-owned by adm.

**Rule ID:** `SV-238341r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the "/var/log/syslog" file to be group-owned by adm with the following command: $ sudo stat -c "%n %G" /var/log/syslog /var/log/syslog adm If the "/var/log/syslog" file is not group-owned by adm, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-238342`

### Rule: The Ubuntu operating system must configure /var/log/syslog file to be owned by syslog.

**Rule ID:** `SV-238342r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the "/var/log/syslog" file to be owned by syslog with the following command: $ sudo stat -c "%n %U" /var/log/syslog /var/log/syslog syslog If the "/var/log/syslog" file is not owned by syslog, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-238343`

### Rule: The Ubuntu operating system must configure /var/log/syslog file with mode 0640 or less permissive.

**Rule ID:** `SV-238343r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the "/var/log/syslog" file with mode 0640 or less permissive by running the following command: $ sudo stat -c "%n %a" /var/log/syslog /var/log/syslog 640 If a value of "640" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000258-GPOS-00099

**Group ID:** `V-238344`

### Rule: The Ubuntu operating system must have directories that contain system commands set to a mode of 0755 or less permissive.

**Rule ID:** `SV-238344r991559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories have mode 0755 or less permissive: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Check that the system command directories have mode 0755 or less permissive with the following command: $ find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000258-GPOS-00099

**Group ID:** `V-238345`

### Rule: The Ubuntu operating system must have directories that contain system commands owned by root.

**Rule ID:** `SV-238345r991559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories are owned by root: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Use the following command for the check: $ sudo find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system commands directories are returned, this is a finding.

## Group: SRG-OS-000258-GPOS-00099

**Group ID:** `V-238346`

### Rule: The Ubuntu operating system must have directories that contain system commands group-owned by root.

**Rule ID:** `SV-238346r991559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories are group-owned by root: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Run the check with the following command: $ sudo find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system commands directories are returned that are not Set Group ID up on execution (SGID) files and owned by a privileged account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238347`

### Rule: The Ubuntu operating system library files must have mode 0755 or less permissive.

**Rule ID:** `SV-238347r1106136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" have mode 0755 or less permissive. Check that the systemwide shared library files have mode 0755 or less permissive with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' -perm /022 -exec stat -c "%n %a" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238348`

### Rule: The Ubuntu operating system library directories must have mode 0755 or less permissive.

**Rule ID:** `SV-238348r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories "/lib", "/lib64", and "/usr/lib have mode 0755 or less permissive with the following command: $ sudo find /lib /lib64 /usr/lib -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any of the aforementioned directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238349`

### Rule: The Ubuntu operating system library files must be owned by root.

**Rule ID:** `SV-238349r1106138_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are owned by root with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -user root -exec stat -c "%n %U" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238350`

### Rule: The Ubuntu operating system library directories must be owned by root.

**Rule ID:** `SV-238350r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories "/lib", "/lib64", and "/usr/lib" are owned by root with the following command: $ sudo find /lib /usr/lib /lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system-wide library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238351`

### Rule: The Ubuntu operating system library files must be group-owned by root or a system account.

**Rule ID:** `SV-238351r1106140_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are group owned by root with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -group root -exec stat -c "%n %G" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238352`

### Rule: The Ubuntu operating system library directories must be group-owned by root.

**Rule ID:** `SV-238352r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide library directories "/lib", "/lib64", and "/usr/lib" are group-owned by root with the following command: $ sudo find /lib /usr/lib /lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system-wide shared library directory is returned, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-238353`

### Rule: The Ubuntu operating system must be configured to preserve log records from failure events.

**Rule ID:** `SV-238353r991562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving operating system state information helps to facilitate operating system restart and return to the operational mode of the organization with least disruption to mission/business processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the log service is configured to collect system failure events. Check that the log service is installed properly with the following command: $ dpkg -l | grep rsyslog ii rsyslog 8.32.0-1ubuntu4 amd64 reliable system and kernel logging daemon If the "rsyslog" package is not installed, this is a finding. Check that the log service is enabled with the following command: $ systemctl is-enabled rsyslog enabled If the command above returns "disabled", this is a finding. Check that the log service is properly running and active on the system with the following command: $ systemctl is-active rsyslog active If the command above returns "inactive", this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-238354`

### Rule: The Ubuntu operating system must have an application firewall installed in order to control remote access methods.

**Rule ID:** `SV-238354r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Ubuntu operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Uncomplicated Firewall is installed with the following command: $ dpkg -l | grep ufw ii ufw 0.36-6 If the "ufw" package is not installed, ask the System Administrator if another application firewall is installed. If no application firewall is installed, this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-238355`

### Rule: The Ubuntu operating system must enable and run the uncomplicated firewall(ufw).

**Rule ID:** `SV-238355r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Ubuntu operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Uncomplicated Firewall is enabled on the system by running the following command: $ systemctl is-enabled ufw If the above command returns the status as "disabled", this is a finding. Verify the Uncomplicated Firewall is active on the system by running the following command: $ systemctl is-active ufw If the above command returns "inactive" or any kind of error, this is a finding. If the Uncomplicated Firewall is not installed, ask the System Administrator if another application firewall is installed. If no application firewall is installed, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-238356`

### Rule: The Ubuntu operating system must, for networked systems, compare internal information system clocks at least every 24 hours with a server which is synchronized to one of the redundant United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DoD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-238356r1038944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not networked, this requirement is Not Applicable. The system clock must be configured to compare the system clock at least every 24 hours to the authoritative time source. Check the value of "maxpoll" in the "/etc/chrony/chrony.conf" file with the following command: $ sudo grep maxpoll /etc/chrony/chrony.conf server tick.usno.navy.mil iburst maxpoll 16 If the "maxpoll" option is set to a number greater than 16 or the line is commented out, this is a finding. Verify that the "chrony.conf" file is configured to an authoritative DoD time source by running the following command: $ grep -i server /etc/chrony/chrony.conf server tick.usno.navy.mil iburst maxpoll 16 server tock.usno.navy.mil iburst maxpoll 16 server ntp2.usno.navy.mil iburst maxpoll 16 If the parameter "server" is not set, is not set to an authoritative DoD time source, or is commented out, this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-238357`

### Rule: The Ubuntu operating system must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second.

**Rule ID:** `SV-238357r1015156_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done in order to determine the time difference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system synchronizes internal system clocks to the authoritative time source when the time difference is greater than one second. Check the value of "makestep" by running the following command: $ sudo grep makestep /etc/chrony/chrony.conf makestep 1 -1 If the makestep option is commented out or is not set to "1 -1", this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-238359`

### Rule: The Ubuntu operating system's Advance Package Tool (APT) must be configured to prevent the installation of patches, service packs, device drivers, or Ubuntu operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-238359r1015157_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that APT is configured to prevent the installation of patches, service packs, device drivers, or Ubuntu operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization. Check that the "AllowUnauthenticated" variable is not set at all or is set to "false" with the following command: $ grep AllowUnauthenticated /etc/apt/apt.conf.d/* /etc/apt/apt.conf.d/01-vendor-Ubuntu:APT::Get::AllowUnauthenticated "false"; If any of the files returned from the command with "AllowUnauthenticated" are set to "true", this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-238360`

### Rule: The Ubuntu operating system must be configured to use AppArmor.

**Rule ID:** `SV-238360r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system-level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles). Satisfies: SRG-OS-000368-GPOS-00154, SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000312-GPOS-00124, SRG-OS-000324-GPOS-00125, SRG-OS-000370-GPOS-00155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system prevents program execution in accordance with local policies. Check that AppArmor is installed and active by running the following command, $ dpkg -l | grep apparmor If the "apparmor" package is not installed, this is a finding. $ systemctl is-active apparmor.service active If "active" is not returned, this is a finding. $ systemctl is-enabled apparmor.service enabled If "enabled" is not returned, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-238362`

### Rule: The Ubuntu operating system must be configured such that Pluggable Authentication Module (PAM) prohibits the use of cached authentications after one day.

**Rule ID:** `SV-238362r958828_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If smart card authentication is not being used on the system, this s Not Applicable. Verify that PAM prohibits the use of cached authentications after one day with the following command: $ sudo grep offline_credentials_expiration /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1" in "/etc/sssd/sssd.conf" or in a file with a name ending in .conf in the "/etc/sssd/conf.d/" directory, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-238363`

### Rule: The Ubuntu operating system must implement NIST FIPS-validated cryptography to protect classified information and for the following: To provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-238363r1014774_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is configured to run in FIPS mode with the following command: $ grep -i 1 /proc/sys/crypto/fips_enabled 1 If a value of "1" is not returned, this is a finding.

## Group: SRG-OS-000403-GPOS-00182

**Group ID:** `V-238364`

### Rule: The Ubuntu operating system must use DoD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-238364r958868_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI-certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the directory containing the root certificates for the Ubuntu operating system contains certificate files for DoD PKI-established certificate authorities by iterating over all files in the "/etc/ssl/certs" directory and checking if, at least one, has the subject matching "DOD ROOT CA". If none is found, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-238367`

### Rule: The Ubuntu operating system must configure the uncomplicated firewall to rate-limit impacted network interfaces.

**Rule ID:** `SV-238367r958902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of the operating system to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an application firewall is configured to rate limit any connection to the system. Check all the services listening to the ports with the following command: $ sudo ss -l46ut Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port Process tcp LISTEN 0 128 [::]:ssh [::]:* For each entry, verify that the Uncomplicated Firewall is configured to rate limit the service ports with the following command: $ sudo ufw status Status: active To Action From -- ------ ---- 22/tcp LIMIT Anywhere 22/tcp (v6) LIMIT Anywhere (v6) If any port with a state of "LISTEN" is not marked with the "LIMIT" action, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-238368`

### Rule: The Ubuntu operating system must implement nonexecutable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-238368r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NX (no-execution) bit flag is set on the system with the following commands: $ sudo dmesg | grep -i "execute disable" [ 0.000000] NX (Execute Disable) protection: active If "dmesg" does not show "NX (Execute Disable) protection: active", check the cpuinfo settings with the following command: $ grep flags /proc/cpuinfo | grep -w nx | sort -u flags : fpu vme de pse tsc ms nx rdtscp lm constant_tsc If "flags" does not contain the "nx" flag, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-238369`

### Rule: The Ubuntu operating system must implement address space layout randomization to protect its memory from unauthorized code execution.

**Rule ID:** `SV-238369r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system implements address space layout randomization (ASLR) with the following command: $ sudo sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If nothing is returned, verify the kernel parameter "randomize_va_space" is set to "2" with the following command: $ cat /proc/sys/kernel/randomize_va_space 2 If "kernel.randomize_va_space" is not set to "2", this is a finding. Verify that a saved value of the "kernel.randomize_va_space" variable is not defined. $ sudo egrep -R "^kernel.randomize_va_space=[^2]" /etc/sysctl.conf /etc/sysctl.d If this returns a result, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-238370`

### Rule: The Ubuntu operating system must be configured so that Advance Package Tool (APT) removes all software components after updated versions have been installed.

**Rule ID:** `SV-238370r958936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify is configured to remove all software components after updated versions have been installed with the following command: $ grep -i remove-unused /etc/apt/apt.conf.d/50unattended-upgrades Unattended-Upgrade::Remove-Unused-Dependencies "true"; Unattended-Upgrade::Remove-Unused-Kernel-Packages "true"; If the "::Remove-Unused-Dependencies" and "::Remove-Unused-Kernel-Packages" parameters are not set to "true" or are missing or commented out, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-238371`

### Rule: The Ubuntu operating system must use a file integrity tool to verify correct operation of all security functions.

**Rule ID:** `SV-238371r958944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to the Ubuntu operating system performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is installed and verifies the correct operation of all security functions. Check that the AIDE package is installed with the following command: $ sudo dpkg -l | grep aide ii aide 0.16.1-1build2 amd64 Advanced Intrusion Detection Environment - static binary If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding. If AIDE is installed, check if it has been initialized with the following command: $ sudo aide.wrapper --check If the output is "Couldn't open file /var/lib/aide/aide.db for reading", this is a finding.

## Group: SRG-OS-000447-GPOS-00201

**Group ID:** `V-238372`

### Rule: The Ubuntu operating system must notify designated personnel if baseline configurations are changed in an unauthorized manner. The file integrity tool must notify the System Administrator when changes to the baseline configuration or anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-238372r958948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the Ubuntu operating system. Changes to Ubuntu operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the Ubuntu operating system. The Ubuntu operating system's IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) notifies the System Administrator when anomalies in the operation of any security functions are discovered with the following command: $ sudo grep SILENTREPORTS /etc/default/aide SILENTREPORTS=no If SILENTREPORTS is uncommented and set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-238373`

### Rule: The Ubuntu operating system must display the date and time of the last successful account logon upon logon.

**Rule ID:** `SV-238373r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify users are provided with feedback on when account accesses last occurred. Check that "pam_lastlog" is used and not silent with the following command: $ grep pam_lastlog /etc/pam.d/login session required pam_lastlog.so showfailed If "pam_lastlog" is missing from "/etc/pam.d/login" file, is not "required", or the "silent" option is present, this is a finding.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-238374`

### Rule: The Ubuntu operating system must have an application firewall enabled.

**Rule ID:** `SV-238374r991593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewalls protect computers from network attacks by blocking or limiting access to open network ports. Application firewalls limit which applications are allowed to communicate over the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Uncomplicated Firewall is enabled on the system by running the following command: $ systemctl status ufw.service | grep -i "active:" Active: active (exited) since Mon 2016-10-17 12:30:29 CDT; 1s ago If the above command returns the status as "inactive", this is a finding. If the Uncomplicated Firewall is not installed, ask the System Administrator if another application firewall is installed. If no application firewall is installed, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238376`

### Rule: The Ubuntu operating system must have system commands set to a mode of 0755 or less permissive.

**Rule ID:** `SV-238376r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories have mode 0755 or less permissive: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Check that the system command files have mode 0755 or less permissive with the following command: $ sudo find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type f -exec stat -c "%n %a" '{}' \; If any files are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238377`

### Rule: The Ubuntu operating system must have system commands owned by root or a system account.

**Rule ID:** `SV-238377r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are owned by root, or a required system account: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Use the following command for the check: $ sudo find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type f -exec stat -c "%n %U" '{}' \; If any system commands are returned and are not owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-238378`

### Rule: The Ubuntu operating system must have system commands group-owned by root or a system account.

**Rule ID:** `SV-238378r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are group-owned by root or a required system account: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Run the check with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type f ! -perm /2000 -exec stat -c "%n %G" '{}' \; If any system commands are returned that are not Set Group ID upon execution (SGID) files and group-owned by a required system account, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-238379`

### Rule: The Ubuntu operating system must disable the x86 Ctrl-Alt-Delete key sequence if a graphical user interface is installed.

**Rule ID:** `SV-238379r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In the graphical environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is not configured to reboot the system when Ctrl-Alt-Delete is pressed when using a graphical user interface. Check that the "logout" target is not bound to an action with the following command: # grep logout /etc/dconf/db/local.d/* logout='' If the "logout" key is bound to an action, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-238380`

### Rule: The Ubuntu operating system must disable the x86 Ctrl-Alt-Delete key sequence.

**Rule ID:** `SV-238380r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is not configured to reboot the system when Ctrl-Alt-Delete is pressed. Check that the "ctrl-alt-del.target" (otherwise also known as reboot.target) is not active with the following command: $ sudo systemctl status ctrl-alt-del.target ctrl-alt-del.target Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) Active: inactive (dead) If the "ctrl-alt-del.target" is not masked, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-251503`

### Rule: The Ubuntu operating system must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-251503r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "/etc/shadow" file for blank passwords with the following command: $ sudo awk -F: '!$2 {print $1}' /etc/shadow If the command returns any results, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-251504`

### Rule: The Ubuntu operating system must not allow accounts configured with blank or null passwords.

**Rule ID:** `SV-251504r1082230_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify null passwords cannot be used. Run the following command: $ grep nullok /etc/pam.d/common-auth /etc/pam.d/common-password If this produces any output, it may be possible to log on with accounts with empty passwords. If null passwords can be used, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-251505`

### Rule: The Ubuntu operating system must disable automatic mounting of Universal Serial Bus (USB) mass storage driver.

**Rule ID:** `SV-251505r958820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include, but are not limited to, such devices as flash drives, external storage, and printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu operating system disables ability to load the USB storage kernel module. # grep usb-storage /etc/modprobe.d/* | grep "/bin/false" install usb-storage /bin/false If the command does not return any output, or the line is commented out, this is a finding. Verify the operating system disables the ability to use USB mass storage device. # grep usb-storage /etc/modprobe.d/* | grep -i "blacklist" blacklist usb-storage If the command does not return any output, or the line is commented out, this is a finding.

## Group: SRG-OS-000481-GPOS-00481

**Group ID:** `V-252704`

### Rule: The Ubuntu operating system must disable all wireless network adapters.

**Rule ID:** `SV-252704r958358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of communications with wireless peripherals, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read, altered, or used to compromise the operating system. This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with an operating system. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR Keyboards, Mice, and Pointing Devices and Near Field Communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DoD requirements for wireless data transmission and be approved for use by the AO. Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the operating system. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of communications with wireless peripherals can be accomplished by physical means (e.g., employing physical barriers to wireless radio frequencies) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. If the wireless peripheral is only passing telemetry data, encryption of the data may not be required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is Not Applicable for systems that do not have physical wireless network radios. Verify that there are no wireless interfaces configured on the system with the following command: $ ls -L -d /sys/class/net/*/wireless | xargs dirname | xargs basename If a wireless interface is configured and has not been documented and approved by the ISSO, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-255912`

### Rule: The Ubuntu operating system SSH server must be configured to use only FIPS-validated key exchange algorithms.

**Rule ID:** `SV-255912r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections provided by FIPS-validated cryptographic algorithms, information can be viewed and altered by unauthorized users without detection. The system will attempt to use the first algorithm presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest algorithm available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to use only FIPS-validated key exchange algorithms: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*kexalgorithms' KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256 If "KexAlgorithms" is not configured, is commented out, or does not contain only the algorithms "ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256" in exact order, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-255913`

### Rule: The Ubuntu operating system must restrict access to the kernel message buffer.

**Rule ID:** `SV-255913r958524_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Restricting access to the kernel message buffer limits access only to root. This prevents attackers from gaining additional system information as a nonprivileged user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to restrict access to the kernel message buffer with the following commands: $ sudo sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r kernel.dmesg_restrict /run/sysctl.d/* /etc/sysctl.d/* /usr/local/lib/sysctl.d/* /usr/lib/sysctl.d/* /lib/sysctl.d/* /etc/sysctl.conf 2> /dev/null /etc/sysctl.conf:kernel.dmesg_restrict = 1 /etc/sysctl.d/99-sysctl.conf:kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-274852`

### Rule: Ubuntu 20.04 LTS must audit any script or executable called by cron as root or by any privileged user.

**Rule ID:** `SV-274852r1106134_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any script or executable called by cron as root or by any privileged user must be owned by that user, must have the permissions 755 or more restrictive, and should have no extended rights that allow any nonprivileged user to modify the script or executable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system is configured to audit the execution of any system call made by cron as root or as any privileged user. $ sudo auditctl -l | grep /etc/cron.d -w /etc/cron.d -p wa -k cronjobs $ sudo auditctl -l | grep /var/spool/cron -w /var/spool/cron -p wa -k cronjobs If either of these commands does not return the expected output, or the lines are commented out, this is a finding.

## Group: SRG-OS-000705-GPOS-00150

**Group ID:** `V-274853`

### Rule: Ubuntu 20.04 LTS must have the "SSSD" package installed.

**Rule ID:** `SV-274853r1106127_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) Something a user knows (e.g., password/PIN); 2) Something a user has (e.g., cryptographic identification device, token); and 3) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD common access card (CAC) with DOD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 20.04 LTS has the packages required for multifactor authentication installed with the following command: $ dpkg -l | grep sssd ii sssd 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- metapackage ii sssd-ad 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- Active Directory back end ii sssd-ad-common 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- PAC responder ii sssd-common 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- common files ii sssd-ipa 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- IPA back end ii sssd-krb5 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- Kerberos back end ii sssd-krb5-common 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- Kerberos helpers ii sssd-ldap 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- LDAP back end ii sssd-proxy 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- proxy back end If the "sssd" package is not installed, this is a finding. The additional sssd components listed by the command may differ from configuration to configuration. Verify that "libpam-sss" (the PAM integration module for SSSD) is installed with the following command: $ dpkg -l | grep libpam-sss i libpam-sss:amd64 2.9.4-1.1ubuntu6.1 amd64 Pam module for the System Security Services Daemon Verify that "libnss-sss" (the NSS module for retrieving user and group information) is installed with the following command: $ dpkg -l | grep libnss-sss ii libnss-sss:amd64 2.9.4-1.1ubuntu6.1 amd64 Nss library for the System Security Services Daemon

## Group: SRG-OS-000705-GPOS-00150

**Group ID:** `V-274854`

### Rule: Ubuntu 20.04 LTS must use the "SSSD" package for multifactor authentication services.

**Rule ID:** `SV-274854r1106129_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) Something a user knows (e.g., password/PIN); 2) Something a user has (e.g., cryptographic identification device, token); and 3) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD common access card (CAC) with DOD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "sssd.service" is enabled and active with the following commands: $ sudo systemctl is-enabled sssd enabled $ sudo systemctl is-active sssd active If "sssd.service" is not active or enabled, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-274855`

### Rule: Ubuntu 20.04 LTS must ensure SSSD performs certificate path validation, including revocation checking, against a trusted anchor for PKI-based authentication.

**Rule ID:** `SV-274855r1107182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a certification authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 20.04 LTS, for PKI-based authentication, has valid certificates by constructing a certification path to an accepted trust anchor. Verify the pam service is listed under [sssd] with the following command: $ sudo grep -A 1 '^\[sssd\]' /etc/sssd/sssd.conf [sssd] services = nss,pam,ssh If "pam" is not listed in services, this is a finding. Verify the pam service is set to use pam for smart card authentication in the [pam] section of /etc/sssd/sssd.conf with the following command: $ sudo grep -A 1 '^\[pam]' /etc/sssd/sssd.conf [pam] pam_cert_auth = True If "pam_cert_auth = True" is not returned, this is a finding. Verify "ca" is enabled in "certificate_verification" with the following command: $ sudo grep certificate_verification /etc/sssd/sssd.conf certificate_verification = ca_cert,ocsp If "certificate_verification" is not set to "ca" or the line is commented out, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-274856`

### Rule: Ubuntu 20.04 LTS must be configured such that Pluggable Authentication Module (PAM) prohibits the use of cached authentications after one day.

**Rule ID:** `SV-274856r1106132_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If smart card authentication is not being used on the system, this is not applicable. Verify that PAM prohibits the use of cached authentications after one day with the following command: $ sudo grep offline_credentials_expiration /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1" in "/etc/sssd/sssd.conf" or in a file with a name ending in .conf in the "/etc/sssd/conf.d/" directory, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-274857`

### Rule: Ubuntu 20.04 LTS must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-274857r1101692_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that authenticated certificates are mapped to the appropriate user group in the "/etc/sssd/sssd.conf" file with the following command: $ grep -i ldap_user_certificate /etc/sssd/sssd.conf ldap_user_certificate=userCertificate;binary

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-274858`

### Rule: Ubuntu 20.04 LTS must restrict privilege elevation to authorized personnel.

**Rule ID:** `SV-274858r1106125_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "sudoers" file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system restricts privilege elevation to authorized personnel with the following command: $ sudo grep -iwR 'ALL' /etc/sudoers /etc/sudoers.d/ | grep -v '#' If either of the following entries are returned, this is a finding: ALL ALL=(ALL) ALL ALL ALL=(ALL:ALL) ALL

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-274859`

### Rule: Ubuntu 20.04 LTS must require users to provide a password for privilege escalation.

**Rule ID:** `SV-274859r1101698_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical that the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/sudoers" has no occurrences of "NOPASSWD" with the following command: $ sudo egrep -iR 'NOPASSWD' /etc/sudoers /etc/sudoers.d/ If any occurrences of "NOPASSWD" are returned from the command and have not been documented with the information system security officer (ISSO) as an organizationally defined administrative group using multifactor authentication (MFA), this is a finding.

