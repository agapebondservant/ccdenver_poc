# STIG Benchmark: IBM zVM Using CA VM:Secure Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-237897`

### Rule: CA VM:Secure product Rules Facility must be installed and operating.

**Rule ID:** `SV-237897r858923_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management for operating systems challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other errors. IBM z/VM requires an external security manager to assure proper account management. Satisfies: SRG-OS-000001-GPOS-00001, SRG-OS-000080-GPOS-00048</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an "ACCESS RULE" record exists on the system using the following command: VMSECURE CONFIG PRODUCT If there is no "ACCESS RULE" record, this is a finding. Verify that CA VM:SECURE RULES can be added using the following command: VMSECURE RULES USER If a rules file does not open, this is a finding.

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-237898`

### Rule: The IBM z/VM TCP/IP DTCPARMS files must be properly configured to connect to an external security manager.

**Rule ID:** `SV-237898r858925_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A comprehensive account management process such as provided by External Security Managers (ESM) which includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service. DTCPARMS setting assures that an ESM is enabled. Account management functions include: assigning group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine location of "DTCPARMS" File for each of the following installed servers: FTP (FTPSERVE) IMAP (IMAP) NFS (VMNFS) REXEC (REXECD) If each "DTCPARMS" file includes the following statements, this is not a finding. :ESM_Enable.YES :ESM_Racroute.YES (or a valid exit name) :ESM_Validate.YES (or a valid exit name)

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-237899`

### Rule: CA VM:Secure product must be installed and operating.

**Rule ID:** `SV-237899r858927_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process such as provided by an External Security Manager (ESM) which includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Account management functions include: assigning group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000032-GPOS-00013, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00020, SRG-OS-000042-GPOS-00021, SRG-OS-000062-GPOS-00031, SRG-OS-000255-GPOS-00096, SRG-OS-000365-GPOS-00152, SRG-OS-000327-GPOS-00127, SRG-OS-000462-GPOS-00206, SRG-OS-000064-GPOS-00033, SRG-OS-000458-GPOS-00203, SRG-OS-000461-GPOS-00205, SRG-OS-000463-GPOS-00207, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218, SRG-OS-000474-GPOS-00219, SRG-OS-000475-GPOS-00220, SRG-OS-000476-GPOS-00221, SRG-OS-000477-GPOS-00222, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000392-GPOS-00172, SRG-OS-000239-GPOS-00089, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the CA VM:Secure product is operational on the system by entering the following command. From the "CMS" command line enter: VMSECURE VERSION If there is no response, "VMSECURE" is not logged in, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-237900`

### Rule: The IBM z/VM JOURNALING LOGON parameter must be set for lockout after 3 attempts for 15 minutes.

**Rule ID:** `SV-237900r858930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Display the System Configuration File. If the "JOURNALING" statement is set to: Facility ON LOGON Lockout after three attempts for 15 minutes, this is not a finding. Note: Site may set Lockout value at 0, this will require system administrator action for reset. Issue "QUERY JOURNAL" command. If the response is as follows this is not a finding: Journal: LOGON-on

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-237901`

### Rule: The CA VM:Secure JOURNAL Facility parameters must be set for lockout after 3 attempts.

**Rule ID:** `SV-237901r649543_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine VM:Secure Security Config File. If there is no Journal record this is a finding. If the Journal record has a maximum consecutive invalid password attempts set to 3, this is not a finding. Note: The "warning" setting may be determined by the site but must be 3 or less. Example: JOURNAL 3 3

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-237902`

### Rule: The IBM z/VM LOGO Configuration file must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting local or remote access to the system.

**Rule ID:** `SV-237902r858933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Display the System Configuration file "LOGO_Config" statement. Determine the file name and file type of a LOGO configuration file. For each LOGO file Identified: If the file contains the following logon banner, this is not a finding. The below banner is mandatory and deviations are not permitted except as authorized in writing by the DoD Chief Information Officer. The thrust of this new policy is to make it clear that there is no expectation of privacy when using DoD information systems and all use of DoD information systems is subject to searching, auditing, inspecting, seizing, and monitoring, even if some personal use of a system is permitted: STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. If all the items above are true, this is not finding. If any item above is untrue, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-237903`

### Rule: The IBM z/VM TCP/IP FTP Server must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting local or remote access to the system and until users acknowledge the usage conditions and take explicit actions to log on for further access.

**Rule ID:** `SV-237903r858936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the user prior to allowing the user access to the operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the application usage policy, a click-through banner at system logon is required. The system must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000024-GPOS-00007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the CMS search order. Verify the FTP Server access to a FTP BANNER file. If there is no accessible FTP BANNER file, this is a finding. Ensure that the "FTP Banner" file contains the following: The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If it does not, this is a finding.

## Group: SRG-OS-000024-GPOS-00007

**Group ID:** `V-237904`

### Rule: The IBM z/VM LOGO configuration file must be configured to display the Standard Mandatory DoD Notice and Consent Banner until users acknowledge the usage conditions and take explicit actions to log on for further access.

**Rule ID:** `SV-237904r858939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the user prior to allowing the user access to the operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "LOGO_CONFIG" settings for the file name of the logo configuration file. Ensure that the file name indicated in the statement contains the DoD official Logon Banner. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If it does not, this is a finding. If any item above is untrue, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-237905`

### Rule: For FTP processing Z/VM TCP/IP FTP server Exit must be enabled.

**Rule ID:** `SV-237905r858942_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no FTP servers active, this is not applicable. Issue "SMSG" command for each FTP Server. Query "FTAUDIT". If the "Exit" is not enabled, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-237906`

### Rule: The IBM z/VM TCP/IP configuration must include an SSLSERVERID statement.

**Rule ID:** `SV-237906r858945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Secure Socket Layer (SSL) server, provides processing support for secure (encrypted) communication between remote clients and z/VM TCP/IP application servers that are configured for secure communications The TCP/IP (stack) server routes requests for secure connections to an SSL server, which interacts with a client on behalf of an application server to perform handshake operations and the exchange of cryptographic parameters for a secure session. The SSL server then manages the encryption and decryption of data for an established, secure session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000250-GPOS-00093, SRG-OS-000424-GPOS-00188, SRG-OS-000426-GPOS-00190, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000423-GPOS-00187</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "SSLSERVERID" statement in the TCP/IP server configuration file. If the "SSLSERVERID" statement identifies at least one userID for an SSL server, this is not a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-237907`

### Rule: CA VM:Secure product AUDIT file must be restricted to authorized personnel.

**Rule ID:** `SV-237907r649561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the VMSECURE Audit disk. Note: Consult the z/VM system administrator for this information. Review all rules that grant access to the identified VM:Secure AUDIT disk. If any grant access to anyone other than a system administrator or security administrator, this is a finding.

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-237908`

### Rule: The IBM z/VM Journal option must be specified in the Product Configuration File.

**Rule ID:** `SV-237908r858948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The JOURNALING statement tells z/VM CP to include the journaling facility and to enable the system being initialized to set and query the journaling facility.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "Product Configuration" file. If the JOURNALING Statement does not specify "ON", this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-237909`

### Rule: All digital certificates in use must have a valid path to a trusted Certification authority.

**Rule ID:** `SV-237909r858951_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Invoke the "gskkyman" utility. From the "Key Management" Menu display Certificate Information. If no certificate information is found, this is not a finding. Note: Certificates are only valid when their status is "TRUST". Therefore, you may ignore certificates with the "NOTRUST" status during the following checks. If the digital certificate information indicates that the issuer's distinguished name leads to a DoD PKI Root Certificate Authority or External Certification Authority (ECA), this is not a finding. Reference the Cyber Exchange website for complete information as to which certificates are acceptable (https://cyber.mil/pki-pke/pkipke-document-library/).

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-237910`

### Rule: The IBM z/VM TCP/IP Key database for LDAP or SSL server must be created with the proper permissions.

**Rule ID:** `SV-237910r858954_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Issue command openvm list /etc./gskadm/ (own) If the file permissions are as displayed below, this is not a finding. User ID Group Name Permissions Type Path name component gskadmin security rw- r-- --- F 'Database.kdb' gskadmin security rw- --- --- F 'Database.rdb' gskadmin security rw- r-- --- F 'Database.sth'

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-237911`

### Rule: CA VM:Secure product Password Encryption (PEF) option must be properly configured to store and transmit cryptographically-protected passwords.

**Rule ID:** `SV-237911r858957_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000074-GPOS-00042</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "VMXRPI" Config file used for building the current nucleus. If the "ENCRYP" record is missing, this is a finding. If the "ENCRYPT" record does not specify "DES3", this is a finding. If the DES3KEY Record is missing, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-237912`

### Rule: CA VM:Secure product AUTOEXP record in the Security Config File must be properly set.

**Rule ID:** `SV-237912r858960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "SECURITY CONFIG" file. If there is no "AUTOEXP" record, this is a finding. If the "AUTOEXP" record is configured as below, this is not finding. AUTOEXP 50 60

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-237913`

### Rule: CA VM:Secure product PASSWORD user exit must be coded with the PWLIST option properly set.

**Rule ID:** `SV-237913r858963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there is no CA VM:Secure Product PASSWORD user exit in use, this is a finding. Examine the CA VM:Secure product PASSWORD user exit for requirement that uses a "PWLIST" option that prohibits password reuse for five generations. If this code is missing, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-237914`

### Rule: IBM zVM CA VM:Secure product PASSWORD user exit must be in use.

**Rule ID:** `SV-237914r649582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Satisfies: SRG-OS-000078-GPOS-00046, SRG-OS-000480-GPOS-00227, SRG-OS-000480-GPOS-00227, SRG-OS-000266-GPOS-00101, SRG-OS-000075-GPOS-00043, SRG-OS-000070-GPOS-00038, SRG-OS-000071-GPOS-00039, SRG-OS-000069-GPOS-00037, SRG-OS-000072-GPOS-00040</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there is no CA VM:Secure PASSWORD user exit in use, this is a finding. Review the CA VM:Secure Password user exit. If there is no code that enforces a minimum 8-character password, this is a finding. If there is no code that prohibits the use of all numbers in the new password, this is a finding. If there is no code that prohibits the use of user name in the new password, this is a finding. If there is no code that prohibits the use of userID in the new password, this is a finding. If there is no code that prohibits the use of consecutive repeated characters, this is a finding. If there is no code requiring that at least one special character be used in the new password, this is a finding. If there is no code that enforces 24 hours/1 day as the minimum password lifetime, this is a finding. If there is no code that enforces a minimum that at least one lowercase character is used in the new password, this is a finding. If there is no code that enforces a minimum that at least one numeric character is used in the new password, this is a finding. If there is no code that enforces a minimum that at least one uppercase character is used in the new password, this is a finding. If there is no code that enforces change of at least 50% of the total number of characters when passwords are changed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-237915`

### Rule: IBM z/VM must be configured to disable non-essential capabilities.

**Rule ID:** `SV-237915r649585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the System administrator has a documented manual process to review and disable non-essential capabilities for z/VM. If there is no policy and process to review and disable non-essential capabilities, this is a finding. If capabilities identified in the policy are not disabled, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-237916`

### Rule: CA VM:Secure product Config Delay LOG option must be set to 0.

**Rule ID:** `SV-237916r858966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM z/VM 6.4.0 made changes to obscure whether a logon is invalid due to the user ID or due to the password. Both the logon prompting sequence and the message HCPLGA050E were changed. However, DELAYLOG causes a delay for a logon with an invalid password that it does not cause when the user ID is invalid. Thus, if you are using DELAYLOG with z/VM 6.4.0, you can inadvertently let someone trying to break into your system know that it is the password that is invalid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Display the CA VM:Secure product Config file. If the "DELAYLOG" record does not exist, this is not a finding. If the "DELAYLOG" record is set to "0", this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-237917`

### Rule: CA VM:Secure product NORULE record in the SECURITY CONFIG file must be configured to REJECT.

**Rule ID:** `SV-237917r858969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000480-GPOS-00228, SRG-OS-000480-GPOS-00229, SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062, SRG-OS-000370-GPOS-00155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "SECURITY CONFIG" file. If a "NORULE" record exists and is set to "REJECT", this is not a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-237918`

### Rule: All IBM z/VM TCP/IP Ports must be restricted to ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-237918r649594_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each TCP/IP server defined examine the TCP/IP Configuration Port Statements. Consult DISA Ports, Protocols, and Services Management (PPSM) Category Assurance Levels (CAL). Verify that the ports and protocols being used are not prohibited and are necessary for the operation of the application server and the hosted applications. If any of the ports or protocols is prohibited or not necessary for the application server operation, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-237919`

### Rule: The IBM z/VM Security Manager must provide a procedure to disable userIDs after 35 days of inactivity.

**Rule ID:** `SV-237919r649597_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the procedure for disabling user accounts. If the procedure performs the following steps, this is not a finding. - Monitors the time since last logon. - Checks all userIDs for inactivity more than 35 days. - If found, the ISSO must suspend an account, but not delete it until it is verified by the local ISSO that the user no longer requires access. - If verification is not received within 60 days, the account may be deleted.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-237920`

### Rule: The IBM z/VM TCP/IP VMSSL command operands must be configured properly.

**Rule ID:** `SV-237920r858972_rule`
**Severity:** high

**Description:**
<VulnDiscussion>VMSSL services are initiated using the VMSSL command defined in the DTCPARMS file. Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine and examine the "DTCPARMS" file for each SSL server pool. If the "VMSSL" command is not included in a :PARMS tag, this is a finding. If the "VMSSL" command is not configured as follows, this is a finding. FIPS (Operand FIPS is equivalent to setting MODE FIPS-140-2.) MODE FIPS-140-2 (Operand MODE FIPS-140-2 is equivalent to setting operand FIPS.) PROTOcol TLSV1_2

## Group: SRG-OS-000121-GPOS-00062

**Group ID:** `V-237921`

### Rule: The IBM z/VM TCP/IP ANONYMOU statement must not be coded in FTP configuration.

**Rule ID:** `SV-237921r858975_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there is no FTP Server active, this is not applicable. Examine the "DTCPARMS" file for each active FTP server. If there is ":ANONYMOUS" or ":ANONYMOU" statement, this is a finding. Examine the "SRVRFTP" command. If "ANONYMOU" is coded, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-237922`

### Rule: CA VM:Secure product ADMIN GLOBALS command must be restricted to systems programming personnel.

**Rule ID:** `SV-237922r858978_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating system management functionality includes functions necessary for administration and requires privileged user access. Allowing non-privileged users to access operating system management functionality capabilities increases the risk that non-privileged users may obtain elevated privileges. Operating system management functionality includes functions necessary to administer console, network components, workstations, or servers and typically requires privileged user access. The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, different TCP/UDP ports, virtualization techniques, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different security domain and with additional access controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "AUTHORIZ" config file. If authorization to "ADMIN GLOBALS" is granted to "SYS Admin", this is not a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-237923`

### Rule: CA VM:Secure must have a security group for Security Administrators only.

**Rule ID:** `SV-237923r649609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from non-security functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Operating systems restrict access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Security Administrator for the defined groups that have authorization to perform security tasks, i.e., create and change rules for any userID in the Rules Facility. Examine the members (users) in each of these groups. If any user does not have the role of Security Administrator, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-237924`

### Rule: The IBM z/VM SYSTEM CONFIG file must be configured to clear TDISK on IPL.

**Rule ID:** `SV-237924r858980_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the SYSTEM CONFIG file. If the "Feature" statement specifies ENABLE CLEAR_TDISK, this is not a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-237925`

### Rule: The IBM z/VM TCP/IP FOREIGNIPCONLIMIT statement must be properly configured.

**Rule ID:** `SV-237925r858983_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning. Use the FOREIGNIPCONLIMIT statement to define the maximum number of connections that a foreign IP address is allowed to have open at the same time. If this value would be exceeded, an SSTRESS denial-of-service attack is declared.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine "TCP/IP" configuration file. If there is no "FOREIGNIPCONLIMIT" statement, this is a finding. If the "FOREIGNIPCONLIMIT" has a value of "0", this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-237926`

### Rule: The IBM z/VM TCP/IP PERSISTCONNECTIONLIMIT statement must be properly configured.

**Rule ID:** `SV-237926r858986_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning. The PERSISTCONNECTIONLIMIT statement defines the maximum number of connections in TCP persist state at any given time. When a new connection in persist state causes this limit to be exceeded, the oldest current connection in persist state is dropped and a ZeroWin denial-of-service attack is declared.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "TCP/IP" configuration file. If there is no "PERSISTCONNECTIONLIMIT" statement, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-237927`

### Rule: The IBM z/VM TCP/IP PENDINGCONNECTIONLIMIT statement must be properly configured.

**Rule ID:** `SV-237927r858989_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning. The PENDINGCONNECTIONLIMIT statement defines the maximum number of half-open connections that are allowed at any given time. When a new half-open connection causes this limit to be exceeded, a random current half-open connection is dropped and a SynFlood denial-of-service attack is declared.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "TCP/IP" configuration file. If there is no "PENDINGCONNECTIONLIMIT" statement, this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-237928`

### Rule: IBM z/VM tapes must use Tape Encryption.

**Rule ID:** `SV-237928r858991_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive and tape drive, when used for backups) within an operating system. Guest operating systems, such as CMS, that are not capable of enabling the hardware encryption available with the 3592 Model E05 tape drive are able to use z/VM facilities that enable the encryption on behalf of the guest. Guest operating systems that do support tape encryption, such as z/OS with proper service, will be able to do so without interference from z/VM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Tape Encryption is in use. For IBM drives issue the following command: Class B: QUERY TAPES DETAIL or Class G: QUERY VIRTUAL TAPES If resulting text includes "ACTIVE KEY LABELS", this is not a finding. Regardless of the drive type if there is no encryption available, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-237929`

### Rule: The IBM z/VM TCP/IP must be configured to display the mandatory DoD Notice and Consent banner before granting access to the system.

**Rule ID:** `SV-237929r649627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the TELNET connection exit. If there is no TELNET connection exit, this is a finding. If the TELNET connection exit does not send a Notice and Consent message before access is granted, this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-237930`

### Rule: The IBM z/VM JOURNALING statement must be coded on the configuration file.

**Rule ID:** `SV-237930r858994_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the start-up process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the Product configuration file. If the "JOURNALING" statement does not specify "ON", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-237931`

### Rule: CA VM:Secure product SECURITY CONFIG file must be restricted to appropriate personnel.

**Rule ID:** `SV-237931r858997_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000480-GPOS-00227</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Query the CA VM:Secure product rules. If there are product rules granting access to the disk on which the "SECURITY CONFIG" file resides for auditors, system administrators or security administrators only, this is not a finding.

## Group: SRG-OS-000257-GPOS-00098

**Group ID:** `V-237932`

### Rule: The IBM z/VM AUDT and Journal Mini Disks must be restricted to the appropriate system administrators.

**Rule ID:** `SV-237932r649636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the CA VM:Secure rules. If there are Link rules for audit disk granted to anyone other than system administrators, security administrators, or system auditors, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-237933`

### Rule: IBM z/VM must remove or disable emergency accounts after the crisis is resolved or 72 hours.

**Rule ID:** `SV-237933r649639_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by the organization's system administrators when network or normal logon/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator (SA) for a documented process to remove or disable emergency accounts after a crisis has been resolved or 72 hours. If there is no documented process, this is a finding. If there are emergency accounts enabled check date/time of resolution of last crisis event. If date/time is greater than 72 hours, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237934`

### Rule: The IBM z/VM must restrict link access to the disk on which system software resides.

**Rule ID:** `SV-237934r649642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the CA VM:Secure rules. If there are Link rules for system software disks granted to anyone other than system administrators, this is a finding.

## Group: SRG-OS-000362-GPOS-00149

**Group ID:** `V-237935`

### Rule: The IBM z/VM Privilege command class A and Class B must be properly assigned.

**Rule ID:** `SV-237935r851943_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceeds the rights of a regular user. Operating system functionality will vary, and while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages, such as from an approved software repository. The operating system or software configuration management utility must enforce control of software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine CP Directory. If Privilege CLASS A or B is granted to anyone other than systems administrators or systems operators, this is a finding. Note: Restrict link to disk where system software resides.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-237936`

### Rule: CA VM:Secure AUTHORIZ CONFIG file must be properly configured.

**Rule ID:** `SV-237936r859000_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to system configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the operating system can have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to operating system components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine "AUTHORIZ CONFIG" file. If Authorizations are granted as follows, this is not a finding. Grant the CA VM:Secure system administrator authorization to use all commands and menu selections. Grant directory managers authorization to use a particular command, group of commands, or menu selection. By carefully planning these authorizations, you can delegate many of the daily directory and disk space management tasks to the directory managers. Plan these authorizations carefully to cover all aspects of your site's VM installation. Grant general users authorization to use those commands and menu selections that enable them to manage their own virtual machine. Users can then perform tasks such as maintaining their own system password and controlling access to their minidisks by others.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-237937`

### Rule: The IBM z/VM journal minidisk space allocation must be large enough for one weeks worth of audit records.

**Rule ID:** `SV-237937r859002_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "MDISK" statement for journaling. If the space allocations are not large enough for one weeks' worth of audit records, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-237938`

### Rule: CA VM:Secure product audit records must offload audit records to a different system or media.

**Rule ID:** `SV-237938r851946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there is no documented process for audit offload, this is a finding. Examine the documented user process for audit record offload. If the procedure does not offload to a different system or media, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-237939`

### Rule: CA VM:Secure product audit records must be offloaded on a weekly basis.

**Rule ID:** `SV-237939r851947_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check audit offload procedure. If it can be determined that the audit records are being offloaded on a weekly basis, this is not a finding.

## Group: SRG-OS-000379-GPOS-00164

**Group ID:** `V-237940`

### Rule: The IBM z/VM Portmapper server virtual machine userID must be included in the AUTOLOG statement of the TCP/IP server configuration file.

**Rule ID:** `SV-237940r859005_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Bidirectional authentication solutions include, but are not limited to, IEEE 802.1x and Extensible Authentication Protocol [EAP], RADIUS server with EAP-Transport Layer Security [TLS] authentication, Kerberos, and SSL mutual authentication. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area network, wide area network, or the Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply this requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the TCP/IP configuration for "AUTOLOG". If the userID for auto logger is not in the "AUTOLOG" statement of the TCP/IP server configuration file, this is a finding.

## Group: SRG-OS-000312-GPOS-00124

**Group ID:** `V-237941`

### Rule: CA VM:Secure product MANAGE command must be restricted to system administrators.

**Rule ID:** `SV-237941r859008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine "AUTHORIZ CONFIG" file. If the "MANAGE" command is only granted to system administrators, this is not a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-237942`

### Rule: The CA VM:Secure LOGONBY command must be restricted to system administrators.

**Rule ID:** `SV-237942r859011_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. The LOGONBY statement designates up to eight user IDs that can use their own passwords to log on to and use the virtual machine.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the CA VM:Secure Rules facility for "LOGONBY" rules. If the "LOGONBY" rules specifies users that are not system administrators, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-237943`

### Rule: The IBM z/VM CP Privilege Class A, B, and D must be restricted to appropriate system operators.

**Rule ID:** `SV-237943r851951_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine user directory definitions to determine CP Privilege class. If CP Privilege Class A, B, or D is assigned to non-privilege users, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-237944`

### Rule: The IBM z/VM JOURNALING statement must be properly configured.

**Rule ID:** `SV-237944r859014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View system config "JOURNALING" statement. If the "JOURNALING" statement "LOGON" operand is configured as below, this is not a finding. Logon, Account after 3 attempts, See IBMZ-VM-000040 for LOCKOUT setting. Link, Account after 3 attempts, Disable after 3 attempts

## Group: SRG-OS-000425-GPOS-00189

**Group ID:** `V-237945`

### Rule: The IBM z/VM TCP/IP SECUREDATA option for FTP must be set to REQUIRED.

**Rule ID:** `SV-237945r859017_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Ensuring the confidentiality of transmitted information requires the operating system to take measures in preparing information for transmission. This can be accomplished via access control and encryption. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, operating systems need to support transmission protection mechanisms such as TLS, SSL VPNs, or IPsec. The SECUREDATA statement specifies the FTP server-wide minimum security level for data connections. Satisfies: SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the FTP Server configuration file. If there is no "SECUREDATA" statement, this is a finding. If the "SECUREDATA" statement specifies "REQUIRED", this is not a finding. Note: If there is no "SECUREDATA" or the "SECUREDATA" specifies "ALLOWED" but there is a documented implementation plan with a definite completion date for setting "SECUREDATA" to "REQUIRED" on file with the ISSM, this can be downgraded to a CAT III.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-237946`

### Rule: IBM z/VM TCP/IP config file INTERNALCLIENTPARMS statement must be properly configured.

**Rule ID:** `SV-237946r859020_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). The INTERNALCLIENTPARMS statement is used to configure the Telnet server, an internal client of the TCPIP virtual machine.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the TCP/IP config file "INTERNALCLIENTPARMS" statement. If the following "INTERNALCLIENTPARMS" sub statement are included, this is not a finding. PORT Num not 20 or 21 SECURECONNECTION REQUIRED CLIENTCERTCHECK FULL

## Group: SRG-OS-000425-GPOS-00189

**Group ID:** `V-237947`

### Rule: All IBM z/VM TCP/IP servers must be configured for SSL/TLS connection.

**Rule ID:** `SV-237947r859023_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Ensuring the confidentiality of transmitted information requires the operating system to take measures in preparing information for transmission. This can be accomplished via access control and encryption. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, operating systems need to support transmission protection mechanisms such as TLS, SSL VPNs, or IPsec.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine SSL/TLS capability. Examine the TCP/IP config file. If the "SSLSERVERID" statement identifies at least one userID for SSL server, this is not a finding.

## Group: SRG-OS-000426-GPOS-00190

**Group ID:** `V-237948`

### Rule: The IBM z/VM TCP/IP SECURETELNETCLIENT option for telnet must be set to YES.

**Rule ID:** `SV-237948r859026_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Ensuring the confidentiality of transmitted information requires the operating system to take measures in preparing information for transmission. This can be accomplished via access control and encryption. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, operating systems need to support transmission protection mechanisms such as TLS, SSL VPNs, or IPsec. The SECUREDATA statement specifies the FTP server-wide minimum security level for data connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the TCP/IP DATA file. If "SECURETELNETCLIENT" option is set to "YES", this is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-237954`

### Rule: The IBM z/VM Privilege Classes C and E must be restricted to appropriate system administrators.

**Rule ID:** `SV-237954r853071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine user directory definitions to determine privilege class. If the CP privilege Class C is assigned to system programmers only, this is not a finding. If the CP privilege Class E is assigned to system analyst only, this is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-237955`

### Rule: The IBM z/VM Privilege Class F must be restricted to service representatives and system administrators only.

**Rule ID:** `SV-237955r853071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users. Privilege Class F can obtain, and examine in detail, data about input and output devices connected to the z/VM system. This privilege class is reserved for IBM use only.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine user directory definitions to determine Privilege Class. If CP Privilege Class F is assigned to anyone other than a service representative or system administrator, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-237956`

### Rule: The IBM z/VM ANY Privilege Class must not be listed for privilege commands.

**Rule ID:** `SV-237956r859044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine defined-privileged commands. If any of the defined-privileged commands are defined with Privilege Class "ANY", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237957`

### Rule: CA VM:Secure product VMXRPI configuration file must be restricted to authorized personnel.

**Rule ID:** `SV-237957r859047_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections. The VMXRPI CONFIG file contains records that determine the activity that can occur when the Rules Facility is not available, and provides the configuration information for the Rules Facility.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Query the CA VM:Secure rules. If there are product rules granting access to the disk on which the "VMXRPI" configuration file resides for system administrators only, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237958`

### Rule: CA VM:Secure product DASD CONFIG file must be restricted to appropriate personnel.

**Rule ID:** `SV-237958r859050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Query the CA VM:Secure product rules. If there are product rules granting access to the disk on which the "DASD CONFIG" file resides for system administrators or DASD administrators only, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237959`

### Rule: CA VM:Secure product AUTHORIZ CONFIG file must be restricted to appropriate personnel.

**Rule ID:** `SV-237959r859053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections. The AUTHORIZ CONFIG file is used to tailor user authorizations for CA VM:Secure commands.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Query the CA VM:Secure product rules. If there are product rules granting access to the disk on which the "AUTHORIZ CONFIG" file resides for system administrators or security administrators only, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237960`

### Rule: CA VM:Secure product CONFIG file must be restricted to appropriate personnel.

**Rule ID:** `SV-237960r859056_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Query the CA VM:Secure Product rules. If there are product rules granting access to the disk on which the product "CONFIG" file resides for system administrators only, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237961`

### Rule: CA VM:Secure Product SFS configuration file must be restricted to appropriate personnel.

**Rule ID:** `SV-237961r859059_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections. The SFS Configuration file is used to control the addition/deletion of file pools and user storage groups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Query the CA VM:Secure product rules. If there are product rules granting access to the disk on which the "SFS" configuration file resides for system administrators or DASD administrators only, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237962`

### Rule: CA VM:Secure product Rules Facility must be restricted to appropriate personnel.

**Rule ID:** `SV-237962r649726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Issue Command: VMSECURE CONFIG AUTHORIZ Inspect the "GRANT" statements. If there are statements that grant the authority to create system rules or rules that apply to other users is only granted to appropriate personnel, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237963`

### Rule: IBM z/VM must employ a Session manager.

**Rule ID:** `SV-237963r649729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session manager controls the semi-permanent interactive information interchange, also known as a dialogue, between a user and z/VM. Without the use of a session manager these semi-permanent interchanges can be open to compromise and attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine running systems. If access is gained to the z/VM system without going through a session manager, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237964`

### Rule: The IBM z/VM System administrator must develop a notification routine for account management.

**Rule ID:** `SV-237964r649732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system accounts are utilized for identifying individual users or for identifying the operating system processes themselves. In order to detect and respond to events affecting user accessibility and system processing, operating systems must not only audit vital account actions but, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator (SA) for documented procedures and routines for account management. If there is no procedure or the procedure is not documented and filed with the ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237965`

### Rule: The IBM z/VM system administrator must develop routines and processes for the proper configuration and maintenance of Software.

**Rule ID:** `SV-237965r649735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Proper configuration management procedures for information systems provide for the proper configuration and maintenance in accordance with local policies restrictions and/or rules. Failure to properly configure and maintain system software and applications on the information system could result in a weakened security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator (SA) for documented procedures and routines for proper configuration management of software. If there are no procedures or the procedures are not documented and on file with the ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237966`

### Rule: IBM z/VM must be protected by an external firewall that has a deny-all, allow-by-exception policy.

**Rule ID:** `SV-237966r649738_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewalls protect computers from network attacks by blocking or limiting access to open network ports. Firewalls provide monitoring and control of communications at the external boundary of an information system to prevent and detect malicious and other unauthorized communications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for a network system plan. If there is no firewall defined for the IBM z/VM system, this is a finding. If the firewall does not have a deny-all, allow-by-exception policy, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237967`

### Rule: The IBM z/VM System administrator must develop routines and processes for notification in the event of audit failure.

**Rule ID:** `SV-237967r649741_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit processing failures include, for example, software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Without proper notification vital audit records may be lost.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator (SA) for documented routines and procures for notification in the event of audit failure. If there are no routines or procedures or they are not documented and filed with the ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237968`

### Rule: The IBM z/VM system administrator must develop procedures maintaining information system operation in the event of anomalies.

**Rule ID:** `SV-237968r649744_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If anomalies are not acted upon, security functions may fail to secure the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for a procedure to notify appropriate personnel in the event of system anomalies or failure. If there is no procedure for notification and resolution or they are not documented and on file with the ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237969`

### Rule: IBM z/VM system administrator must develop procedures to manually control temporary, interactive, and emergency accounts.

**Rule ID:** `SV-237969r649747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Proper handling of temporary, inactive, and emergency accounts require automatic notification and action rather than at the convenience of the systems administrator. However in the absence of automated process manual procedures must be in place to assure that possible sensitive accounts are not compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator (SA) for documented manual procedures to handle temporary, inactive, and emergency accounts. If there are no procedures or they are not documented and filed with the ISSM/ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237970`

### Rule: IBM z/VM must have access to an audit reduction tool that allows for central data review and analysis.

**Rule ID:** `SV-237970r649750_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit reduction is a process that manipulates collected audit information and organizes such information in a summary format that is more meaningful to analysts. Audit reduction and report generation capabilities do not always emanate from the same information system or from the same organizational entities conducting auditing activities. Audit reduction capability can include, for example, modern data mining techniques with advanced data filters to identify anomalous behavior in audit records. Audit records may at times be voluminous. Without a reduction tool crucial information may be overlooked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator if there is an audit reduction tool available for use with IBM z/VM. Determine if a process is established to route audit records to the tool. If there is no audit tool available, this is a finding. If a procedure for routing audit records to the tool is not documented and on file with the ISSM/ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237971`

### Rule: The IBM z/VM system administrator must develop and perform a procedure to validate the correct operation of security functions.

**Rule ID:** `SV-237971r649753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator (SA) if there is a documented procedure for validation of security functions on file with the ISSM/ISSO. If there is none, this is a finding. Ask for evidence that the procedures are performed. If there is no evidentiary proof, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237972`

### Rule: IBM z/VM must employ Clock synchronization software.

**Rule ID:** `SV-237972r649756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Clock synchronization software is use. If there is no Clock synchronization software in use, this is a finding. Determine if configuration allows for the synchronizing internal Clock to authoritative source. If software is improperly configured, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237973`

### Rule: The IBM z/VM systems requiring data at rest must employ IBMs DS8000 for full disk encryption.

**Rule ID:** `SV-237973r649759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if IBM's DS8000 Disks are in use. If they are not in use for systems that require "data at rest", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245530`

### Rule: The IBM z/VM TCP/IP NSLOOKUP statement for UFT servers must be properly configured.

**Rule ID:** `SV-245530r859029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed, which would result in query failure or DoS. Data origin authentication must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching Domain Name System (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. Information systems that use technologies other than the DNS to map between host/service names and network addresses provide other means to enable clients to verify the authenticity of response data. This is not applicable if DNSSEC is not implemented on the local network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "UFTD CONFIG" file. If "NSLOOKUP" statement is "YES", this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245531`

### Rule: The IBM z/VM TCP/IP DOMAINLOOKUP statement must be properly configured.

**Rule ID:** `SV-245531r859032_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed, which would result in query failure or DoS. Data origin authentication must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching Domain Name System (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. Information systems that use technologies other than the DNS to map between host/service names and network addresses provide other means to enable clients to verify the authenticity of response data. This is not applicable if DNSSEC is not implemented on the local network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "TCPIP DATA" configuration file. If "DOMAINLOOKUP" statement is configured to "DNS", this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245532`

### Rule: The IBM z/VM TCP/IP NSINTERADDR statement must be present in the TCPIP DATA configuration.

**Rule ID:** `SV-245532r859035_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed, which would result in query failure or DoS. Data origin authentication must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching Domain Name System (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. Information systems that use technologies other than the DNS to map between host/service names and network addresses provide other means to enable clients to verify the authenticity of response data. This is not applicable if DNSSEC is not implemented on the local network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "TCPIP DATA" configuration file. If there is no "NSINTERADDR" statement in the "TCPIP DATA" configuration file, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245533`

### Rule: The IBM z/VM CHECKSUM statement must be included in the TCP/IP configuration file.

**Rule ID:** `SV-245533r859038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed which would result in query failure or denial of service. Data integrity verification must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching Domain Name System (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. The CHECKSUM statement is a TCP/IP configuration file statement that instructs the TCPIP virtual machine to reenable TCP checksum testing on incoming messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "TCP/IP" configuration file. If there is no "CHECKSUM" statement in the "TCP/IP" configuration file, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245534`

### Rule: The IBM z/VM DOMAINSEARCH statement in the TCPIP DATA file must be configured with proper domain names for name resolution.

**Rule ID:** `SV-245534r859041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed which would result in query failure or denial of service. Data origin authentication verification must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching Domain Name System (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. This is not applicable if DNSSEC is not implemented on the local network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "TCPIP DATA" file. The domain specified for the "DOMAINORIGIN" statement is also used for host name resolution, as if it appeared in a "DOMAINSEARCH" statement. If there is no "DOMAINORIGIN" or "DOMAINSEARCH" statement, this is a finding. If the "DOMAINSEARCH" statement does not specify a proper domain, this is a finding. If the "DOMAINORIGIN" statement does not specify a proper domain, this is a finding.

