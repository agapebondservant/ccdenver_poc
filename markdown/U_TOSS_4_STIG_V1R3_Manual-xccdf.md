# STIG Benchmark: Tri-Lab Operating System Stack (TOSS) 4 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-252911`

### Rule: TOSS must display the Standard Mandatory DoD Notice and Consent Banner or equivalent US Government Agency Notice and Consent Banner before granting local or remote access to the system.

**Rule ID:** `SV-252911r824057_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD or other US Government Agency policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS displays the Standard Mandatory DoD Notice and Consent Banner or equivalent US Government Agency Notice and Consent Banner before granting access to the system. Check that TOSS displays a banner at the command line login screen with the following command: $ sudo cat /etc/issue "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the system has a graphical logon capability and does not display a graphical logon banner, this is a finding. If the text in the file does not match the Standard Mandatory DoD Notice and Consent Banner or equivalent US Government Agency Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-252912`

### Rule: TOSS, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-252912r824060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000384-GPOS-00167</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS for PKI-based authentication has valid certificates by constructing a certification path (which includes status information) to an accepted trust anchor. Check that the system has a valid DoD root CA installed with the following command: Note: If the system does not support PKI authentication, this requirement is Not Applicable. $ sudo openssl x509 -text -in /etc/sssd/pki/sssd_auth_ca_db.pem Certificate: Data: Version: 3 (0x2) Serial Number: 1 (0x1) Signature Algorithm: sha256WithRSAEncryption Issuer: C = US, O = U.S. Government, OU = DoD, OU = PKI, CN = DoD Root CA 3 Validity Not Before: Mar 20 18:46:41 2012 GMT Not After : Dec 30 18:46:41 2029 GMT Subject: C = US, O = U.S. Government, OU = DoD, OU = PKI, CN = DoD Root CA 3 Subject Public Key Info: Public Key Algorithm: rsaEncryption If the root ca file is not a DoD-issued certificate with a valid date and installed in the /etc/sssd/pki/sssd_auth_ca_db.pem location, this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-252913`

### Rule: TOSS, for PKI-based authentication, must enforce authorized access to the corresponding private key.

**Rule ID:** `SV-252913r824063_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system, for PKI-based authentication, enforces authorized access to the corresponding private key. If the system does not allow PKI authentication, this requirement is Not Applicable. Verify the SSH private key files have a passphrase. For each private key stored on the system, use the following command: $ sudo ssh-keygen -y -f /path/to/file If the contents of the key are displayed, and use of un-passphrased SSH keys is not documented with the Information System Security Officer (ISSO), this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-252914`

### Rule: TOSS must require authentication upon booting into emergency or rescue modes.

**Rule ID:** `SV-252914r824066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if the system requires authentication for rescue or emergency mode with the following command: $ sudo grep sulogin-shell /usr/lib/systemd/system/rescue.service ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue If the "ExecStart" line is configured for anything other than "/usr/lib/systemd/systemd-sulogin-shell rescue", commented out, or missing, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-252915`

### Rule: TOSS must not permit direct logons to the root account using remote access from outside of the system via SSH.

**Rule ID:** `SV-252915r824069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Even though the communications channel may be encrypted, an additional layer of security is gained by extending the policy of not logging on directly as root. In addition, logging on with a user-specific account provides individual accountability of actions performed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify remote access from outside the system using SSH prevents users from logging on directly as "root." Check that SSH prevents users from logging on directly as "root" with the following command: $ sudo grep -i PermitRootLogin /etc/ssh/sshd_config PermitRootLogin no If the "PermitRootLogin" keyword is set to "yes", is missing, or is commented out, and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-252916`

### Rule: The TOSS file system automounter must be disabled unless required.

**Rule ID:** `SV-252916r824072_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatically mounting file systems permits easy introduction of unknown devices, thereby facilitating malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to automount devices. Check to see if automounter service is active with the following command: Note: If the autofs service is not installed, this requirement is Not Applicable. $ sudo systemctl status autofs autofs.service - Automounts filesystems on demand Loaded: loaded (/usr/lib/systemd/system/autofs.service; disabled) Active: inactive (dead) If the "autofs" status is set to "active" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-252917`

### Rule: The TOSS pam_unix.so module must be configured in the password-auth file to use a FIPS 140-2-approved cryptographic hashing algorithm for system authentication.

**Rule ID:** `SV-252917r824075_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. TOSS systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the pam_unix.so module is configured to use sha512. Check that the pam_unix.so module is configured to use sha512 in /etc/pam.d/password-auth with the following command: $ sudo grep password /etc/pam.d/password-auth | grep pam_unix password sufficient pam_unix.so sha512 If "sha512" is missing, or is commented out, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-252918`

### Rule: The TOSS pam_unix.so module must be configured in the system-auth file to use a FIPS 140-2-approved cryptographic hashing algorithm for system authentication.

**Rule ID:** `SV-252918r824078_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. TOSS systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the pam_unix.so module is configured to use sha512. Check that the pam_unix.so module is configured to use sha512 in /etc/pam.d/system-auth with the following command: $ sudo grep password /etc/pam.d/system-auth | grep pam_unix password sufficient pam_unix.so sha512 If "sha512" is missing, or is commented out, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-252919`

### Rule: The TOSS operating system must implement DoD-approved encryption in the OpenSSL package.

**Rule ID:** `SV-252919r877395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. TOSS incorporates system-wide crypto policies by default. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/openssl.config file. Satisfies: SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OpenSSL library is configured to use only DoD-approved TLS encryption: $ sudo grep -i MinProtocol /etc/crypto-policies/back-ends/opensslcnf.config TLS.MinProtocol = TLSv1.2 DTLS.MinProtocol = DTLSv1.2 If the "TLS.MinProtocol" is set to anything older than "TLSv1.2" or the "DTLS.MinProtocol" is set to anything older than DTLSv1.2, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-252920`

### Rule: TOSS must use a Linux Security Module configured to enforce limits on system services.

**Rule ID:** `SV-252920r824084_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from non-security functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Operating systems restrict access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that TOSS verifies the correct operation of all security functions. Check if "SELinux" is active and in "Enforcing" mode with the following command: $ sudo getenforce Enforcing If "SELinux" is not active or not in "Enforcing" mode, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-252921`

### Rule: TOSS must prevent unauthorized and unintended information transfer via shared system resources.

**Rule ID:** `SV-252921r824087_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see that all public directories are owned by root or a system account with the following command: $ sudo find / -type d -perm -0002 -exec ls -lLd {} \; drwxrwxrwxt 7 root root 4096 Jul 26 11:19 /tmp If any of the returned directories are not owned by root or a system account, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-252922`

### Rule: The TOSS operating system must be configured to use TCP syncookies.

**Rule ID:** `SV-252922r824090_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of Service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify The TOSS operating system is configured to use TCP syncookies. Check the value of TCP syncookies with the following command: $ sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 If the value is not "1", this is a finding. Check the saved value of TCP syncookies with the following command: $ sudo grep -i net.ipv4.tcp_syncookies /etc/sysctl.conf /etc/sysctl.d/* | grep -v '#' If no output is returned, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-252923`

### Rule: TOSS must display the Standard Mandatory DoD Notice and Consent Banner or equivalent US Government Agency Notice and Consent Banner before granting local or remote access to the system via a ssh logon.

**Rule ID:** `SV-252923r824093_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to TOSS ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD or other US Government Agency policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that TOSS displays the Standard Mandatory DoD Notice and Consent Banner or equivalent US Government Agency Notice and Consent Banner before granting access to the system when connecting from outside of the cluster. Check for the location of the banner file being used with the following command: $ sudo grep -i banner /etc/ssh/sshd_config banner /etc/issue This command will return the banner keyword and the name of the file that contains the ssh banner (in this case "/etc/issue"). If the line is commented out, this is a finding. For nodes of the cluster that are only privately (within the cluster) accessible, this requirement is Not Applicable. View the file specified by the banner keyword to check that it matches the text of the Standard Mandatory DoD Notice and Consent Banner: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the system has a graphical logon capability and does not display a graphical logon banner, this is a finding. If the text in the file does not match the Standard Mandatory DoD Notice and Consent Banner or equivalent US Government Agency Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-252924`

### Rule: The TOSS operating system must implement DoD-approved encryption to protect the confidentiality of SSH connections.

**Rule ID:** `SV-252924r877394_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. TOSS incorporates system-wide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/openssh.config file. By specifying a cipher list with the order of ciphers being in a "strongest to weakest" orientation, the system will automatically attempt to use the strongest cipher for securing SSH connections. Satisfies: SRG-OS-000250-GPOS-00093, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon is configured to use only ciphers employing FIPS 140-2-approved algorithms: Verify that system-wide crypto policies are in effect: $ sudo grep CRYPTO_POLICY /etc/sysconfig/sshd # CRYPTO_POLICY= If the "CRYPTO_POLICY" is uncommented, this is a finding. Verify which system-wide crypto policy is in use: $ sudo update-crypto-policies --show FIPS Check that the ciphers in the back-end configurations are FIPS 140-2-approved algorithms with the following command: $ sudo grep -i ciphers /etc/crypto-policies/back-ends/openssh.config /etc/crypto-policies/back-ends/opensshserver.config /etc/crypto-policies/back-ends/openssh.config:Ciphers aes256-ctr,aes192-ctr,aes128-ctr /etc/crypto-policies/back-ends/opensshserver.config:CRYPTO_POLICY='-oCiphers=aes256-ctr,aes192-ctr,aes128-ctr' /etc/crypto-policies/back-ends/opensshserver.config:CRYPTO_POLICY='-oCiphers=aes256-ctr,aes192-ctr,aes128-ctr' If the cipher entries in the "openssh.config" and "opensshserver.config" files have any ciphers other than "aes256-ctr,aes192-ctr,aes128-ctr", the order differs from the example above, if they are missing, or commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-252925`

### Rule: The TOSS operating system must implement DoD-approved TLS encryption in the GnuTLS package.

**Rule ID:** `SV-252925r877394_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Transport Layer Security (TLS) encryption is a required security setting as a number of known vulnerabilities have been reported against Secure Sockets Layer (SSL) and earlier versions of TLS. Encryption of private information is essential to ensuring data confidentiality. If private information is not encrypted, it can be intercepted and easily read by an unauthorized party. SQL Server must use a minimum of FIPS 140-2-approved TLS version 1.2, and all non-FIPS-approved SSL and TLS versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. The GnuTLS library offers an API to access secure communications protocols. SSLv2 is not available in the GnuTLS library. The TOSS system-wide crypto policy defines employed algorithms in the /etc/crypto-policies/back-ends/gnutls.config file.5</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the GnuTLS library is configured to only allow DoD-approved SSL/TLS Versions: $ sudo grep -io +vers.* /etc/crypto-policies/back-ends/gnutls.config +VERS-ALL:-VERS-DTLS0.9:-VERS-SSL3.0:-VERS-TLS1.0:-VERS-TLS1.1:-VERS-DTLS1.0:+COMP-NULL:%PROFILE_MEDIUM If the "gnutls.config" does not list "-VERS-DTLS0.9:-VERS-SSL3.0:-VERS-TLS1.0:-VERS-TLS1.1:-VERS-DTLS1.0" to disable unapproved SSL/TLS versions, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-252926`

### Rule: The TOSS SSH daemon must be configured to use only Message Authentication Codes (MACs) employing FIPS 140-2 validated cryptographic hash algorithms.

**Rule ID:** `SV-252926r877394_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. TOSS incorporates system-wide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/openssh.config file. By specifying a hash algorithm list with the order of hashes being in a "strongest to weakest" orientation, the system will automatically attempt to use the strongest hash for securing SSH connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon is configured to use only MACs employing FIPS 140-2-approved algorithms: Check that the MACs in the back-end configurations are FIPS 140-2-approved algorithms with the following command: $ sudo grep -i macs /etc/crypto-policies/back-ends/openssh.config /etc/crypto-policies/back-ends/opensshserver.config /etc/crypto-policies/back-ends/openssh.config:MACs hmac-sha2-512,hmac-sha2-256 /etc/crypto-policies/back-ends/opensshserver.config:-oMACs=hmac-sha2-512,hmac-sha2-256' /etc/crypto-policies/back-ends/opensshserver.config:-oMACs=hmac-sha2-512,hmac-sha2-256' If the MAC entries in the "openssh.config" and "opensshserver.config" files have any hashes other than "hmac-sha2-512" and "hmac-sha2-256", the order differs from the example above, if they are missing, or commented out, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-252927`

### Rule: The TOSS operating system must be configured to preserve log records from failure events.

**Rule ID:** `SV-252927r824105_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving operating system state information helps to facilitate operating system restart and return to the operational mode of the organization with least disruption to mission/business processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the rsyslog service is enabled and active with the following commands: $ sudo systemctl is-enabled rsyslog enabled $ sudo systemctl is-active rsyslog active If the service is not "enabled" and "active", this is a finding. If "rsyslog" is not enabled, ask the System Administrator how system error logging is performed on the system. If there is no evidence of system logging being performed on the system, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-252928`

### Rule: TOSS must, for networked systems, compare internal information system clocks at least every 24 hours with a server which is synchronized to one of the redundant United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DoD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-252928r877038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time that a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the operating system include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. TOSS utilizes the "timedatectl" command to view the status of the "systemd-timesyncd.service." The "timedatectl" status will display the local time, UTC, and the offset from UTC. Note that USNO offers authenticated NTP service to DoD and U.S. Government agencies operating on the NIPR and SIPR networks. Visit https://www.usno.navy.mil/USNO/time/ntp/dod-customers for more information. Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000356-GPOS-00144, SRG-OS-000359-GPOS-00146</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not networked, this requirement is Not Applicable. The system clock must be configured to compare the system clock at least every 24 hours to the authoritative time source. Check the value of "maxpoll" in the "/etc/chrony/chrony.conf" file with the following command: $ sudo grep maxpoll /etc/chrony/chrony.conf server tick.usno.navy.mil iburst maxpoll 16 If "maxpoll" is not set to "16" or does not exist, this is a finding. Verify that the "chrony.conf" file is configured to an authoritative DoD time source by running the following command: $ grep -i server /etc/chrony.conf server tick.usno.navy.mil iburst maxpoll 16 server tock.usno.navy.mil iburst maxpoll 16 server ntp2.usno.navy.mil iburst maxpoll 16 If the parameter "server" is not set, is not set to an authoritative DoD time source, or is commented out, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-252929`

### Rule: The TOSS file integrity tool must notify the system administrator when changes to the baseline configuration or anomalies in the operation of any security functions are discovered within an organizationally defined frequency.

**Rule ID:** `SV-252929r824111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's Information Management Officer (IMO)/Information System Security Officer (ISSO) and System Administrators (SAs) must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection. TOSS 4 comes with many optional software packages. A file integrity tool called Advanced Intrusion Detection Environment (AIDE) is one of those optional packages. This requirement assumes the use of AIDE; however, a different tool may be used if the requirements are met. Note that AIDE does not have a configuration that will send a notification, so a cron job is recommended that uses the mail application on the system to email the results of the file integrity check. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000446-GPOS-00200, SRG-OS-000447-GPOS-00201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system routinely checks the baseline configuration for unauthorized changes and notifies the system administrator when anomalies in the operation of any security functions are discovered. Check to see if AIDE is installed on the system with the following command: $ sudo yum list installed aide If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. Check that TOSS routinely executes a file integrity scan for changes to the system baseline. The command used in the example will use a daily occurrence. Check the cron directories for scripts controlling the execution and notification of results of the file integrity application. For example, if AIDE is installed on the system, use the following commands: $ sudo ls -al /etc/cron.* | grep aide -rwxr-xr-x 1 root root 29 Nov 22 2015 aide $ sudo grep aide /etc/crontab /var/spool/cron/root /etc/crontab: 30 04 * * * root usr/sbin/aide /var/spool/cron/root: 30 04 * * * root usr/sbin/aide $ sudo more /etc/cron.daily/aide #!/bin/bash /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily aide integrity check run" root@sysname.mil Here the use of /bin/mail is one example of how to notify designated personnel. There may be other methods available to a system, such as notifications from an external log aggregation service (e.g., SIEM). If the file integrity application does not exist, or a script file controlling the execution of the file integrity application does not exist, or the file integrity application does not notify designated personnel of changes, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-252930`

### Rule: TOSS must prevent the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-252930r877463_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS prevents the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization. Check that YUM verifies the signature of packages from a repository prior to install with the following command: $ sudo egrep '^\[.*\]|gpgcheck' /etc/yum.repos.d/*.repo /etc/yum.repos.d/appstream.repo:[appstream] /etc/yum.repos.d/appstream.repo:gpgcheck=1 /etc/yum.repos.d/baseos.repo:[baseos] /etc/yum.repos.d/baseos.repo:gpgcheck=1 If "gpgcheck" is not set to "1", or if options are missing or commented out, ask the System Administrator how the certificates for patches and other operating system components are verified. If there is no process to validate certificates that is approved by the organization, this is a finding.

## Group: SRG-OS-000373-GPOS-00158

**Group ID:** `V-252931`

### Rule: TOSS must require re-authentication when using the "sudo" command.

**Rule ID:** `SV-252931r824117_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the organization requires the user to re-authenticate when using the "sudo" command. If the value is set to an integer less than 0, the user's time stamp will not expire and the user will not have to re-authenticate for privileged actions until the user's session is terminated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system requires re-authentication when using the "sudo" command to elevate privileges. $ sudo egrep -ir 'timestamp_timeout' /etc/sudoers /etc/sudoers.d /etc/sudoers:Defaults timestamp_timeout=0 If "timestamp_timeout" is set to a negative number, is commented out, or no results are returned, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-252932`

### Rule: TOSS must have the packages required for multifactor authentication installed.

**Rule ID:** `SV-252932r824120_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a DoD Common Access Card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, credentials stored on the authentication device will not be affected. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DoD CAC. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS has the packages required for multifactor authentication installed with the following commands: $ sudo yum list installed openssl-pkcs11 openssl-pkcs11.x86_64 0.4.10-2.el8 @anaconda If the "openssl-pkcs11" package is not installed, ask the administrator to indicate what type of multifactor authentication is being utilized and what packages are installed to support it. If there is no evidence of multifactor authentication being used, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-252933`

### Rule: TOSS must prohibit the use of cached authentications after one day.

**Rule ID:** `SV-252933r824123_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable. TOSS includes multiple options for configuring authentication, but this requirement will be focus on the System Security Services Daemon (SSSD). By default, sssd does not cache credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSSD prohibits the use of cached authentications after one day. Note: If smart card authentication is not being used on the system, this item is Not Applicable. Check that SSSD allows cached authentications with the following command: $ sudo grep cache_credentials /etc/sssd/sssd.conf cache_credentials = true If "cache_credentials" is set to "false" or missing from the configuration file, this is not a finding and no further checks are required. If "cache_credentials" is set to "true", check that SSSD prohibits the use of cached authentications after one day with the following command: $ sudo grep offline_credentials_expiration /etc/sssd/sssd.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1", this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-252934`

### Rule: All TOSS networked systems must have and implement SSH to protect the confidentiality and integrity of transmitted and received information, as well as information during preparation for transmission.

**Rule ID:** `SV-252934r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSH package is installed: $ rpm -q openssh-server openssh-server-8.0p1-10.el8_4.2.x86_64 If the "SSH server" package is not installed, this is a finding. Verify SSH is loaded and active with the following commands: $ sudo systemctl is-active sshd active $ sudo systemctl is-enabled sshd enabled If "sshd" does not show a status of "active" and "enabled", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252935`

### Rule: For TOSS systems using Domain Name Servers (DNS) resolution, at least two name servers must be configured.

**Rule ID:** `SV-252935r824129_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To provide availability for name resolution services, multiple redundant name servers are mandated. A failure in name resolution could lead to the failure of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the system is using local or DNS name resolution with the following command: $ sudo grep hosts /etc/nsswitch.conf hosts: files dns If the DNS entry is missing from the host's line in the "/etc/nsswitch.conf" file, the "/etc/resolv.conf" file must be empty. Verify the "/etc/resolv.conf" file is empty with the following command: $ sudo ls -al /etc/resolv.conf -rw-r--r-- 1 root root 0 Aug 19 08:31 resolv.conf If local host authentication is being used and the "/etc/resolv.conf" file is not empty, this is a finding. If the DNS entry is found on the host's line of the "/etc/nsswitch.conf" file, verify the operating system is configured to use two or more name servers for DNS resolution. Determine the name servers used by the system with the following command: $ sudo grep nameserver /etc/resolv.conf nameserver 192.168.1.2 nameserver 192.168.1.3 If less than two lines are returned that are not commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252936`

### Rule: The debug-shell systemd service must be disabled on TOSS.

**Rule ID:** `SV-252936r824132_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The debug-shell requires no authentication and provides root privileges to anyone who has physical access to the machine. While this feature is disabled by default, masking it adds an additional layer of assurance that it will not be enabled via a dependency in systemd. This also prevents attackers with physical access from trivially bypassing security on the machine through valid troubleshooting configurations and gaining root access when the system is rebooted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS is configured to mask the debug-shell systemd service with the following command: $ sudo systemctl status debug-shell.service debug-shell.service Loaded: masked (Reason: Unit debug-shell.service is masked.) Active: inactive (dead) If the "debug-shell.service" is loaded and not masked, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252937`

### Rule: The root account must be the only account having unrestricted access to the TOSS system.

**Rule ID:** `SV-252937r824135_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account other than root also has a User Identifier (UID) of "0", it has root authority, giving that account unrestricted access to the entire operating system. Multiple accounts with a UID of "0" afford an opportunity for potential intruders to guess a password for a privileged account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for duplicate UID "0" assignments with the following command: $ sudo awk -F: '$3 == 0 {print $1}' /etc/passwd If any accounts other than root have a UID of "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252938`

### Rule: The systemd Ctrl-Alt-Delete burst key sequence in TOSS must be disabled.

**Rule ID:** `SV-252938r824138_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS is not configured to reboot the system when Ctrl-Alt-Delete is pressed seven times within two seconds with the following command: $ sudo grep -i ctrl /etc/systemd/system.conf CtrlAltDelBurstAction=none If the "CtrlAltDelBurstAction" is not set to "none", commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252939`

### Rule: There must be no ".shosts" files on The TOSS operating system.

**Rule ID:** `SV-252939r824141_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ."shosts" files are used to configure host-based authentication for individual users or the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no ."shosts" files on TOSS with the following command: $ sudo find / -name '*.shosts' If any ."shosts" files are found, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252940`

### Rule: TOSS must not allow blank or null passwords in the system-auth file.

**Rule ID:** `SV-252940r824144_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that null passwords cannot be used, run the following command: $ sudo grep -i nullok /etc/pam.d/system-auth If output is produced, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252941`

### Rule: TOSS must not be performing packet forwarding unless the system is a router.

**Rule ID:** `SV-252941r824147_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS is not performing packet forwarding unless the system is a router. If the system is a router (sometimes called a gateway) this requirement is Not Applicable. Note: If either IPv4 or IPv6 is disabled on the system, this requirement only applies to the active internet protocol version. Check to see if IP forwarding is enabled using the following commands: $ sudo sysctl net.ipv4.ip_forward net.ipv4.ip_forward = 0 $ sudo sysctl net.ipv6.conf.all.forwarding net.ipv6.conf.all.forwarding = 0 If IP forwarding value is not "0" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252942`

### Rule: The TOSS SSH daemon must not allow authentication using known host's authentication.

**Rule ID:** `SV-252942r824150_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring this setting for the SSH daemon provides additional assurance that remote logon via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow authentication using known host's authentication with the following command: $ sudo grep -i IgnoreUserKnownHosts /etc/ssh/sshd_config IgnoreUserKnownHosts yes If the value is returned as "no", the returned line is commented out, or no output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252943`

### Rule: The TOSS SSH daemon must not allow compression or must only allow compression after successful authentication.

**Rule ID:** `SV-252943r824153_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in an SSH connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection, potentially with root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon performs compression after a user successfully authenticates with the following command: $ sudo grep -i compression /etc/ssh/sshd_config Compression delayed If the "Compression" keyword is set to "yes", is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252944`

### Rule: The TOSS SSH daemon must not allow Kerberos authentication, except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-252944r824156_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring these settings for the SSH daemon provides additional assurance that remote logon via SSH will not use unused methods of authentication, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow Kerberos authentication with the following command: $ sudo grep -i KerberosAuthentication /etc/ssh/sshd_config KerberosAuthentication no If the value is returned as "yes", the returned line is commented out, no output is returned, or has not been documented with the ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-252945`

### Rule: TOSS must not allow an unattended or automatic logon to the system.

**Rule ID:** `SV-252945r877377_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not allow an unattended or automatic logon to the system via a graphical user interface. Note: This requirement assumes the use of the TOSS default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Check for the value of the "AutomaticLoginEnable" in the "/etc/gdm/custom.conf" file with the following command: $ sudo grep -i automaticloginenable /etc/gdm/custom.conf AutomaticLoginEnable=false If the value of "AutomaticLoginEnable" is missing or is not set to "false", this is a finding. If it does, this is a finding. Automatic logon as an authorized user allows access to any user with physical access to the operating system.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-252946`

### Rule: TOSS must enforce the limit of five consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-252946r824162_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/security/faillock.conf" file is configured to lock an account after three unsuccessful logon attempts within 15 minutes: $ sudo grep -e "deny =" -e "fail_interval =" /etc/security/faillock.conf deny = 3 fail_interval = 900 If the "deny" option is set to "0", more than "3", is missing, or is commented out, this is a finding. If the "fail_interval" option is set to less than "900", is missing, or is commented out, this is a finding. Note: If the System Administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is Not Applicable.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-252947`

### Rule: TOSS must limit the number of concurrent sessions to 256 for all accounts and/or account types.

**Rule ID:** `SV-252947r877399_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to Denial of Service (DoS) attacks. TOSS as an HPC operating system, is capable of supporting a large number of sessions, as well as tools which presume a larger number of concurrent sessions will be allowed. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS limits the number of concurrent sessions to less than or equal to 256 for all accounts and/or account types by issuing the following command: $ sudo grep -r -s '^[^#].*maxlogins' /etc/security/limits.conf /etc/security/limits.d/*.conf * hard maxlogins 256 This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains. If the "maxlogins" item is missing, commented out, or the value is set greater than "256" and is not documented with the Information System Security Officer (ISSO) as an operational requirement for all domains that have the "maxlogins" item assigned, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-252948`

### Rule: TOSS must retain a user's session lock until that user reestablishes access using established identification and authentication procedures.

**Rule ID:** `SV-252948r824168_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock shall remain in place until the user re-authenticates. No other activity aside from re-authentication shall unlock the system. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS retains a user's session lock until that user reestablishes access using established identification and authentication procedures with the following command: Note: This requirement assumes the use of the TOSS default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. $ sudo gsettings get org.gnome.desktop.screensaver lock-enabled true If the setting is "false", this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-252949`

### Rule: TOSS must automatically lock graphical user sessions after 15 minutes of inactivity.

**Rule ID:** `SV-252949r824171_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS initiates a session lock after at most a 15-minute period of inactivity for graphical user interfaces with the following commands: Note: This requirement assumes the use of the TOSS default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. $ sudo gsettings get org.gnome.desktop.session idle-delay uint32 900 If "idle-delay" is set to "0" or a value greater than "900", this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-252950`

### Rule: TOSS must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-252950r824174_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis. There are various methods of mapping certificates to user/group accounts for TOSS. For the purposes of this requirement, the check and fix will account for Active Directory mapping. Some of the other possible methods include joining the system to a domain and utilizing a TOSS idM server, or a local system mapping, where the system is not part of a domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the certificate of the user or group is mapped to the corresponding user or group in the "sssd.conf" file with the following command: Note: If the system does not support PKI authentication, this requirement is Not Applicable. $ sudo cat /etc/sssd/sssd.conf [sssd] config_file_version = 2 services = pam, sudo, ssh domains = testing.test [pam] pam_cert_auth = True [domain/testing.test] id_provider = ldap [certmap/testing.test/rule_name] matchrule =<SAN>.*EDIPI@mil maprule = (userCertificate;binary={cert!bin}) domains = testing.test If the certmap section does not exist, ask the System Administrator to indicate how certificates are mapped to accounts. If there is no evidence of certificate mapping, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-252951`

### Rule: TOSS duplicate User IDs (UIDs) must not exist for interactive users.

**Rule ID:** `SV-252951r824177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, interactive users must be identified and authenticated to prevent potential misuse and compromise of the system. Interactive users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Interactive users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that TOSS contains no duplicate User IDs (UIDs) for interactive users. Check that the operating system contains no duplicate UIDs for interactive users with the following command: $ sudo awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced, and the accounts listed are interactive user accounts, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-252952`

### Rule: TOSS must use multifactor authentication for network and local access to privileged and non-privileged accounts.

**Rule ID:** `SV-252952r824180_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) something a user knows (e.g., password/PIN); 2) something a user has (e.g., cryptographic identification device, token); and 3) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the Internet). The DoD CAC with DoD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system uses multifactor authentication for network access to privileged accounts. If it does not, this is a finding. Note: This requirement is applicable to any externally accessible nodes of the TOSS system. For compute or other intra-cluster only accessible nodes, this requirement is Not Applicable. One possible method for meeting this requirement is to require smart card logon for access to interactive accounts. Check that the "pam_cert_auth" setting is set to "true" in the "/etc/sssd/sssd.conf" file. Check that the "try_cert_auth" or "require_cert_auth" options are configured in both "/etc/pam.d/system-auth" and "/etc/pam.d/smartcard-auth" files with the following command: $ sudo grep cert_auth /etc/sssd/sssd.conf /etc/pam.d/* /etc/sssd/sssd.conf:pam_cert_auth = True /etc/pam.d/smartcard-auth:auth sufficient pam_sss.so try_cert_auth /etc/pam.d/system-auth:auth [success=done authinfo_unavail=ignore ignore=ignore default=die] pam_sss.so try_cert_auth If "pam_cert_auth" is not set to "true" in "/etc/sssd/sssd.conf", this is a finding. If "pam_sss.so" is not set to "try_cert_auth" or "require_cert_auth" in both the "/etc/pam.d/smartcard-auth" and "/etc/pam.d/system-auth" files, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-252953`

### Rule: TOSS must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-252953r824183_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity with the following command: Check the account inactivity value by performing the following command: $ sudo grep -i inactive /etc/default/useradd INACTIVE=35 If "INACTIVE" is set to "-1", a value greater than "35", or is commented out, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-252954`

### Rule: TOSS must automatically remove or disable emergency accounts after the crisis is resolved or 72 hours.

**Rule ID:** `SV-252954r824186_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by the organization's system administrators when network or normal logon/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements, TOSS can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify emergency accounts have been provisioned with an expiration date of 72 hours. For every existing emergency account, run the following command to obtain its account expiration information. $ sudo chage -l system_account_name Verify each of these accounts has an expiration date set within 72 hours. If any emergency accounts have no expiration date set or do not expire within 72 hours, this is a finding. If there are no emergency accounts configured, this requirement is Not Applicable.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-252955`

### Rule: TOSS must reveal error messages only to authorized users.

**Rule ID:** `SV-252955r824189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log/messages" file has a mode of "0640" or less permissive and is owned by the root user with the following command: $ sudo ls -l /var/log/messages -rw-r----- 1 root root 59782947 Jul 20 01:36 /var/log/messages If the "/var/log/messages" file has a mode more permissive than "0640", this is a finding. If the "/var/log/messages" file is not owned by "root", this is a finding. Verify the "/var/log" directory has a mode of "0755" or less permissive and is owned by the root user with the following command: $ sudo ls -ld /var/log/ drwxr-xr-x 1 root root 1200 Jul 19 03:39 /var/log If the "/var/log/" directory has a mode more permissive than "0755", this is a finding. If the "/var/log/" directory is not owned by "root", this is a finding.

## Group: SRG-OS-000299-GPOS-00117

**Group ID:** `V-252956`

### Rule: TOSS must protect wireless access to the system using authentication of users and/or devices.

**Rule ID:** `SV-252956r824192_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing devices and users to connect to the system without first authenticating them allows untrusted access and can lead to a compromise or attack. Wireless technologies include, for example, microwave, packet radio (UHF/VHF), 802.11x, and Bluetooth. Wireless networks use authentication protocols (e.g., EAP/TLS, PEAP), which provide credential protection and mutual authentication. This requirement applies to those operating systems that control wireless devices. Satisfies: SRG-OS-000299-GPOS-00117, SRG-OS-000300-GPOS-00118, SRG-OS-000481-GPOS-00481</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no wireless interfaces configured on the system with the following command: Note: This requirement is Not Applicable for systems that do not have physical wireless network radios. $ sudo nmcli device status DEVICE TYPE STATE CONNECTION virbr0 bridge connected virbr0 wlp7s0 wifi connected wifiSSID enp6s0 ethernet disconnected -- p2p-dev-wlp7s0 wifi-p2p disconnected -- lo loopback unmanaged -- virbr0-nic tun unmanaged -- If a wireless interface is configured and has not been documented and approved by the Information System Security Officer (ISSO), this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-252957`

### Rule: TOSS must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes occur.

**Rule ID:** `SV-252957r824195_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. Due to the scale of HPC systems and the number of users in question, it is impractical to require an administrator to unlock the user's account manually. Strong controls around automatic lock out, and typical (though not universal) use of strong MFA to enter an HPC system mitigate the concerns of a brute force attack being successful.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the system locks an account after three unsuccessful logon attempts within a period of 15 minutes until released by an administrator with the following commands. Note: If a centralized authentication platform (AD, IdM, LDAP, etc) is utilized for authentication, then this requirement is not applicable, to allow the centralized platform to solely manage user lockout. Verify the pam_faillock.so module is present in the "/etc/pam.d/system-auth" and " /etc/pam.d/password-auth" files: $ sudo grep pam_faillock.so /etc/pam.d/system-auth /etc/pam.d/password-auth /etc/pam.d/system-auth:auth required pam_faillock.so preauth /etc/pam.d/system-auth:auth required pam_faillock.so authfail /etc/pam.d/system-auth:account required pam_faillock.so /etc/pam.d/password-auth:auth required pam_faillock.so preauth /etc/pam.d/password-auth:auth required pam_faillock.so authfail /etc/pam.d/password-auth:account required pam_faillock.so preauth If the pam_failllock.so module is not present in the "/etc/pam.d/system-auth" and " /etc/pam.d/password-auth" files, this is a finding. Verify the "/etc/security/faillock.conf" file is configured to lock an account until released by an administrator after three unsuccessful logon attempts: $ sudo grep 'unlock_time =' /etc/security/faillock.conf unlock_time = 0 If the "unlock_time" option is not set to "0", is missing or commented out, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-252958`

### Rule: TOSS must require users to reauthenticate for privilege escalation.

**Rule ID:** `SV-252958r824198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user re-authenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/sudoers" has no occurrences of "!authenticate." Check that the "/etc/sudoers" file has no occurrences of "!authenticate" by running the following command: $ sudo grep -i authenticate /etc/sudoers /etc/sudoers.d/* If any occurrences of "!authenticate" return from the command, this is a finding.

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-252959`

### Rule: TOSS must require users to provide a password for privilege escalation.

**Rule ID:** `SV-252959r824201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/sudoers" has no occurrences of "NOPASSWD." Check that the "/etc/sudoers" file has no occurrences of "NOPASSWD" by running the following command: $ sudo grep -i nopasswd /etc/sudoers /etc/sudoers.d/* %admin ALL=(ALL) NOPASSWD: ALL If any occurrences of "NOPASSWD" are returned from the command and have not been documented with the ISSO as an organizationally defined administrative group utilizing MFA, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252960`

### Rule: All TOSS local interactive user accounts must be assigned a home directory upon creation.

**Rule ID:** `SV-252960r824204_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all local interactive users on TOSS are assigned a home directory upon creation with the following command: $ sudo grep -i create_home /etc/login.defs CREATE_HOME yes If the value for "CREATE_HOME" parameter is not set to "yes", the line is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252961`

### Rule: All TOSS local interactive user home directories must be group-owned by the home directory owner's primary group.

**Rule ID:** `SV-252961r824207_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of a local interactive user's home directory is not the same as the primary GID of the user, this would allow unauthorized access to the user's files, and users that share the same group may not be able to access files that they legitimately should.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all local interactive users is group-owned by that user's primary GID with the following command: Note: This may miss local interactive users that have been assigned a privileged UID. Evidence of interactive use may be obtained from a number of log files containing system logon information. The returned directory "/home/smithj" is used as an example. $ sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) drwxr-x--- 2 smithj admin 4096 Jun 5 12:41 smithj Check the user's primary group with the following command: $ sudo grep $(grep smithj /etc/passwd | awk -F: '{print $4}') /etc/group admin:x:250:smithj,jonesj,jacksons If the user home directory referenced in "/etc/passwd" is not group-owned by that user's primary GID, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252962`

### Rule: All TOSS local interactive users must have a home directory assigned in the /etc/passwd file.

**Rule ID:** `SV-252962r824210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify local interactive users on TOSS have a home directory assigned with the following command: $ sudo pwck -r user 'lp': directory '/var/spool/lpd' does not exist user 'news': directory '/var/spool/news' does not exist user 'uucp': directory '/var/spool/uucp' does not exist user 'www-data': directory '/var/www' does not exist Ask the System Administrator (SA) if any users found without home directories are local interactive users. If the SA is unable to provide a response, check for users with a User Identifier (UID) of 1000 or greater with the following command: $ sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6}' /etc/passwd If any interactive users do not have a home directory assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252963`

### Rule: The x86 Ctrl-Alt-Delete key sequence in TOSS must be disabled if a graphical user interface is installed.

**Rule ID:** `SV-252963r824213_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user, who presses Ctrl-Alt-Delete when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS is not configured to reboot the system when Ctrl-Alt-Delete is pressed when using a graphical user interface with the following command: Note: This requirement assumes the use of the TOSS default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. $ sudo grep logout /etc/dconf/db/local.d/* logout='' If the "logout" key is bound to an action, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252964`

### Rule: TOSS must disable the user list at logon for graphical user interfaces.

**Rule ID:** `SV-252964r824216_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving the user list enabled is a security risk since it allows anyone with physical access to the system to enumerate known user accounts without authenticated access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the user logon list for graphical user interfaces with the following command: Note: This requirement assumes the use of the TOSS default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. $ sudo gsettings get org.gnome.login-screen disable-user-list true If the setting is "false", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252965`

### Rule: TOSS must display the date and time of the last successful account logon upon an SSH logon.

**Rule ID:** `SV-252965r824219_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users with feedback on when account accesses via SSH last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH provides users with feedback on when account accesses last occurred with the following command: $ sudo grep -i printlastlog /etc/ssh/sshd_config PrintLastLog yes If the "PrintLastLog" keyword is set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252966`

### Rule: TOSS must not allow accounts configured with blank or null passwords.

**Rule ID:** `SV-252966r824222_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that null passwords cannot be used, run the following command: $ sudo grep -i permitemptypasswords /etc/ssh/sshd_config PermitEmptyPasswords no If "PermitEmptyPasswords" is set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-252967`

### Rule: TOSS must not have unnecessary accounts.

**Rule ID:** `SV-252967r824225_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all accounts on the system are assigned to an active system, application, or user account. Obtain the list of authorized system accounts from the Information System Security Officer (ISSO). Check the system accounts on the system with the following command: $ sudo more /etc/passwd root:x:0:0:root:/root:/bin/bash bin:x:1:1:bin:/bin:/sbin/nologin daemon:x:2:2:daemon:/sbin:/sbin/nologin sync:x:5:0:sync:/sbin:/bin/sync shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown halt:x:7:0:halt:/sbin:/sbin/halt games:x:12:100:games:/usr/games:/sbin/nologin gopher:x:13:30:gopher:/var/gopher:/sbin/nologin Accounts such as "games" and "gopher" are not authorized accounts as they do not support authorized system functions. If the accounts on the system do not match the provided documentation, or accounts that do not support an authorized system function are present, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-252968`

### Rule: TOSS must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-252968r824228_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created, they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS defines default permissions for all authenticated users in such a way that the user can only read and modify their own files. Check for the value of the "UMASK" parameter in "/etc/login.defs" file with the following command: Note: If the value of the "UMASK" parameter is set to "000" in "/etc/login.defs" file, the Severity is raised to a CAT I. $ grep -i umask /etc/login.defs UMASK 077 If the value for the "UMASK" parameter is not "077", or the "UMASK" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-252969`

### Rule: All TOSS local interactive user home directories must have mode 0770 or less permissive.

**Rule ID:** `SV-252969r824231_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users' home directories/folders may contain information of a sensitive nature. Non-privileged users should coordinate any sharing of information with an SA through shared resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system limits the ability of non-privileged users to grant other users direct access to the contents of their home directories/folders. Ensure that the user permissions on all user home directories is set to 770 permissions with the following command: $ find $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) -maxdepth 0 -not -perm 770 -ls If there is any output, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-252970`

### Rule: All TOSS local interactive user home directories must be owned by root.

**Rule ID:** `SV-252970r824234_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users' home directories/folders may contain information of a sensitive nature. Non-privileged users should coordinate any sharing of information with an SA through shared resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that all user home directories are owned by the root user with the following command: $ find $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) -maxdepth 0 -not -user root -ls If there is any output, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-252971`

### Rule: All TOSS local interactive user home directories must be owned by the user's primary group.

**Rule ID:** `SV-252971r824237_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users' home directories/folders may contain information of a sensitive nature. Non-privileged users should coordinate any sharing of information with an SA through shared resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that all user home directories are owned by the user's primary group with the following command: $ awk -F: '($3>=1000)&&($7 !~ /nologin/)&&("stat -c '%g' " $6 | getline dir_group)&&(dir_group!=$4){print $1,$6}' /etc/passwd admin /home/admin Check each user's primary group with the following command (example command is for the "admin" user): $ sudo grep "^admin" /etc/group admin:x:250:smithj,jonesj,jacksons If the user home directory referenced in "/etc/passwd" is not group-owned by that user's primary GID, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-252972`

### Rule: TOSS must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-252972r824240_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to modify an existing account. Auditing account modification actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow." Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/shadow /etc/audit/audit.rules -w /etc/shadow -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252973`

### Rule: TOSS audit records must contain information to establish what type of events occurred, when the events occurred, the source of events, where events occurred, and the outcome of events.

**Rule ID:** `SV-252973r824243_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, when events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in TOSS audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured TOSS system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000047-GPOS-00023, SRG-OS-000051-GPOS-00024, SRG-OS-000064-GPOS-00033, SRG-OS-000241-GPOS-00091, SRG-OS-000254-GPOS-00095, SRG-OS-000327-GPOS-00127, SRG-OS-000342-GPOS-00133, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000365-GPOS-00152, SRG-OS-000474-GPOS-00219, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit service is configured to produce audit records. Check that the audit service is installed properly with the following command: $ sudo yum list installed audit If the "audit" package is not installed, this is a finding. Check that the audit service is properly running and active on the system with the following command: $ sudo systemctl is-active auditd.service active If the command above returns "inactive", this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-252974`

### Rule: TOSS must generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-252974r824246_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "sudo" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w sudo /etc/audit/audit.rules -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-252975`

### Rule: TOSS must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-252975r824249_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SA and ISSO (at a minimum) are notified in the event of an audit processing failure. Check that TOSS notifies the SA and ISSO (at a minimum) in the event of an audit processing failure with the following command: $ sudo grep action_mail_acct /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the retuned line is commented out, ask the system administrator to indicate how they and the ISSO are notified of an audit process failure. If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-252976`

### Rule: TOSS must take appropriate action when an audit processing failure occurs.

**Rule ID:** `SV-252976r824252_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS takes the appropriate action when an audit processing failure occurs. Check that TOSS takes the appropriate action when an audit processing failure occurs with the following command: $ sudo grep disk_error_action /etc/audit/auditd.conf disk_error_action = HALT If the value of the "disk_error_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, ask the system administrator to indicate how the system takes appropriate action when an audit process failure occurs. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-252977`

### Rule: TOSS audit logs must have a mode of 0600 or less permissive to prevent unauthorized read access.

**Rule ID:** `SV-252977r824255_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs have a mode of "0600" or less permissive. First, determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log file, check if the audit log has a mode of "0600" or less permissive with the following command: $ sudo ls -l /var/log/audit/audit.log -rw------- 1 root root 908084 Jul 19 23:10 /var/log/audit/audit.log If the audit log has a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-252978`

### Rule: TOSS audit log directory must have a mode of 0700 or less permissive to prevent unauthorized read access.

**Rule ID:** `SV-252978r824258_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log directory has a mode of "0700" or less permissive. First, determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the directory where the audit log file is located, check if the audit log directory has a mode of "0700" or less permissive with the following command: $ sudo ls -ld /var/log/audit/ drwx------. 2 root root 99 Jul 19 07:32 /var/log/audit/ If the audit log directory has a mode more permissive than "0700", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-252979`

### Rule: TOSS audit logs must be owned by user root to prevent unauthorized read access.

**Rule ID:** `SV-252979r824261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs are owned by user root. First, determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log file, check if the audit log is owned by user "root" with the following command: $ sudo ls -l /var/log/audit/audit.log -rw------- 1 root root 908084 Jul 19 23:10 /var/log/audit/audit.log If the audit log is not owned by user "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-252980`

### Rule: TOSS audit logs must be owned by group root to prevent unauthorized read access.

**Rule ID:** `SV-252980r824264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs are owned by group root. First, determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log file, check if the audit log is owned by group "root" with the following command: $ sudo ls -l /var/log/audit/audit.log -rw------- 1 root root 908084 Jul 19 23:10 /var/log/audit/audit.log If the audit log is not owned by group "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-252981`

### Rule: TOSS audit log directory must be owned by user root to prevent unauthorized read access.

**Rule ID:** `SV-252981r824267_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log directory is owned by user root. First, determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the directory where the audit log file is located, check if the directory is owned by user "root" with the following command: $ sudo ls -ld /var/log/audit/ drwx------. 2 root root 99 Jul 19 07:32 /var/log/audit/ If the audit log directory is not owned by user "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-252982`

### Rule: TOSS audit log directory must be owned by group root to prevent unauthorized read access.

**Rule ID:** `SV-252982r824270_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log directory is owned by group root. First, determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the directory where the audit log file is located, check if the directory is owned by group "root" with the following command: $ sudo ls -ld /var/log/audit/ drwx------. 2 root root 99 Jul 19 07:32 /var/log/audit/ If the audit log directory is not owned by group "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-252983`

### Rule: The TOSS audit system must protect auditing rules from unauthorized change.

**Rule ID:** `SV-252983r824273_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit TOSS system activity. In immutable mode, unauthorized users cannot execute changes to the audit system to potentially hide malicious activity and then put the audit rules back. A system reboot would be noticeable and a system administrator could then investigate the unauthorized changes. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes with the following command: $ sudo grep "^\s*[^#]" /etc/audit/audit.rules | tail -1 -e 2 If the audit system is not set to be immutable by adding the "-e 2" option to the "/etc/audit/audit.rules", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-252984`

### Rule: The TOSS audit system must protect logon UIDs from unauthorized change.

**Rule ID:** `SV-252984r824276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit TOSS system activity. In immutable mode, unauthorized users cannot execute changes to the audit system to potentially hide malicious activity and then put the audit rules back. A system reboot would be noticeable and a system administrator could then investigate the unauthorized changes. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes to logon UIDs with the following command: $ sudo grep -i immutable /etc/audit/audit.rules --loginuid-immutable If the login UIDs are not set to be immutable by adding the "--loginuid-immutable" option to the "/etc/audit/audit.rules", this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252985`

### Rule: Successful/unsuccessful uses of the "chage" command in TOSS must generate an audit record.

**Rule ID:** `SV-252985r824279_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chage" command is used to change or view user password expiry information. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "chage" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chage /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-chage If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252986`

### Rule: Successful/unsuccessful uses of the "chcon" command in TOSS must generate an audit record.

**Rule ID:** `SV-252986r824282_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chcon" command is used to change file SELinux security context. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "chcon" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chcon /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252987`

### Rule: Successful/unsuccessful uses of the ssh-agent in TOSS must generate an audit record.

**Rule ID:** `SV-252987r824285_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "ssh-agent" is a program to hold private keys used for public key authentication. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "ssh-agent" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep ssh-agent /etc/audit/audit.rules -a always,exit -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=unset -k privileged-ssh If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252988`

### Rule: Successful/unsuccessful uses of the "passwd" command in TOSS must generate an audit record.

**Rule ID:** `SV-252988r824288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "passwd" command is used to change passwords for user accounts. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "passwd" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w passwd /etc/audit/audit.rules -a always,exit -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-passwd If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252989`

### Rule: Successful/unsuccessful uses of postdrop in TOSS must generate an audit record.

**Rule ID:** `SV-252989r824291_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "postdrop" command creates a file in the maildrop directory and copies its standard input to the file. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "postdrop" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "postdrop" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/postdrop -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252990`

### Rule: Successful/unsuccessful uses of postqueue in TOSS must generate an audit record.

**Rule ID:** `SV-252990r824294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "postqueue" command implements the Postfix user interface for queue management. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "postqueue" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "postqueue" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/postqueue -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252991`

### Rule: Successful/unsuccessful uses of setsebool in TOSS must generate an audit record.

**Rule ID:** `SV-252991r824297_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "setsebool" command sets the current state of a particular SELinux boolean or a list of booleans to a given value. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "setsebool" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "setsebool" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252992`

### Rule: Successful/unsuccessful uses of the ssh-keysign in TOSS must generate an audit record.

**Rule ID:** `SV-252992r824300_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "ssh-keysign" program is an SSH helper program for host-based authentication. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "ssh-keysign" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep ssh-keysign /etc/audit/audit.rules -a always,exit -F path=/usr/libexec/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=unset -k privileged-ssh If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252993`

### Rule: Successful/unsuccessful uses of the "setfacl" command in RTOSS must generate an audit record.

**Rule ID:** `SV-252993r824303_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "setfacl" command is used to set file access control lists. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "setfacl" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w setfacl /etc/audit/audit.rules -a always,exit -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252994`

### Rule: Successful/unsuccessful uses of the "pam_timestamp_check" command in TOSS must generate an audit record.

**Rule ID:** `SV-252994r824306_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "pam_timestamp_check" command is used to check if the default timestamp is valid. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "pam_timestamp_check" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w pam_timestamp_check /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=unset -k privileged-pam_timestamp_check If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252995`

### Rule: Successful/unsuccessful uses of the "newgrp" command in TOSS must generate an audit record.

**Rule ID:** `SV-252995r824309_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "newgrp" command is used to change the current group ID during a login session. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "newgrp" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w newgrp /etc/audit/audit.rules -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252996`

### Rule: Successful/unsuccessful uses of the "init_module" command in TOSS must generate an audit record.

**Rule ID:** `SV-252996r824312_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "init_module" command is used to load a kernel module. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "init_module" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "init_module" /etc/audit/audit.rules -a always,exit -F arch=b32 -S init_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S init_module -F auid>=1000 -F auid!=unset -k module_chng If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252997`

### Rule: Successful/unsuccessful uses of the "rename" command in TOSS must generate an audit record.

**Rule ID:** `SV-252997r824315_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "rename" command will rename the specified files by replacing the first occurrence of expression in their name by replacement. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "rename" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "rename" /etc/audit/audit.rules -a always,exit -F arch=b32 -S rename -F auid>=1000 -F auid!=unset -k delete -a always,exit -F arch=b64 -S rename -F auid>=1000 -F auid!=unset -k delete If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252998`

### Rule: Successful/unsuccessful uses of the "renameat" command in TOSS must generate an audit record.

**Rule ID:** `SV-252998r824318_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "renameat" command renames a file, moving it between directories if required. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "renameat" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "renameat" /etc/audit/audit.rules -a always,exit -F arch=b32 -S renameat -F auid>=1000 -F auid!=unset -k delete -a always,exit -F arch=b64 -S renameat -F auid>=1000 -F auid!=unset -k delete If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-252999`

### Rule: Successful/unsuccessful uses of the "rmdir" command in TOSS must generate an audit record.

**Rule ID:** `SV-252999r824321_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "rmdir" command removes empty directories. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "rmdir" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "rmdir" /etc/audit/audit.rules -a always,exit -F arch=b32 -S rmdir -F auid>=1000 -F auid!=unset -k delete -a always,exit -F arch=b64 -S rmdir -F auid>=1000 -F auid!=unset -k delete If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253000`

### Rule: Successful/unsuccessful uses of the "unlink" command in TOSS must generate an audit record.

**Rule ID:** `SV-253000r824324_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "unlink" command deletes a name from the filesystem. If that name was the last link to a file and no processes have the file open, the file is deleted and the space it was using is made available for reuse. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "unlink" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "unlink" /etc/audit/audit.rules -a always,exit -F arch=b32 -S unlink -F auid>=1000 -F auid!=unset -k delete -a always,exit -F arch=b64 -S unlink -F auid>=1000 -F auid!=unset -k delete If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253001`

### Rule: Successful/unsuccessful uses of the "unlinkat" command in TOSS must generate an audit record.

**Rule ID:** `SV-253001r824327_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "unlinkat" system call operates in exactly the same way as either "unlink" or "rmdir" except for the differences described in the manual page. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "unlinkat" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "unlinkat" /etc/audit/audit.rules -a always,exit -F arch=b32 -S unlinkat -F auid>=1000 -F auid!=unset -k delete -a always,exit -F arch=b64 -S unlinkat -F auid>=1000 -F auid!=unset -k delete If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253002`

### Rule: Successful/unsuccessful uses of the "finit_module" command in TOSS must generate an audit record.

**Rule ID:** `SV-253002r824330_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "finit_module" command is used to load a kernel module. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "finit_module" syscall by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "finit_module" /etc/audit/audit.rules -a always,exit -F arch=b32 -S finit_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S finit_module -F auid>=1000 -F auid!=unset -k module_chng If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253003`

### Rule: Successful/unsuccessful uses of the "delete_module" command in TOSS must generate an audit record.

**Rule ID:** `SV-253003r824333_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "delete_module" command is used to unload a kernel module. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "delete_module" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "delete_module" /etc/audit/audit.rules -a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253004`

### Rule: Successful/unsuccessful uses of the "crontab" command in TOSS must generate an audit record.

**Rule ID:** `SV-253004r824336_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "crontab" command is used to maintain crontab files for individual users. Crontab is the program used to install, remove, or list the tables used to drive the cron daemon. This is similar to the task scheduler used in other operating systems. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "crontab" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w crontab /etc/audit/audit.rules -a always,exit -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=unset -k privileged-crontab If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253005`

### Rule: Successful/unsuccessful uses of the "chsh" command in TOSS must generate an audit record.

**Rule ID:** `SV-253005r824339_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chsh" command is used to change the login shell. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "chsh" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chsh /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253006`

### Rule: Successful/unsuccessful uses of setfiles in TOSS must generate an audit record.

**Rule ID:** `SV-253006r824342_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "setfiles" command is primarily used to initialize the security context fields (extended attributes) on one or more filesystems (or parts of them). Usually, it is initially run as part of the SELinux installation process (a step commonly known as labeling). When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "setfiles" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "setfiles" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253007`

### Rule: Successful/unsuccessful uses of the "chacl" command in TOSS must generate an audit record.

**Rule ID:** `SV-253007r824345_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chacl" command is used to change the access control list of a file or directory. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "chacl" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chacl /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-253008`

### Rule: TOSS must allow only the Information System Security Manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-253008r824348_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the files in directory "/etc/audit/rules.d/" and "/etc/audit/auditd.conf" file have a mode of "0640" or less permissive by using the following commands: $ sudo ls -l /etc/audit/rules.d -rw-r----- 1 root root 1280 Feb 16 17:09 audit.rules $ sudo ls -l /etc/audit/auditd.conf -rw-r----- 1 root root 621 Sep 22 17:19 auditd.conf If the files in the "/etc/audit/rules.d/" directory or the "/etc/audit/auditd.conf" file have a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253009`

### Rule: Successful/unsuccessful uses of the chmod system call in TOSS must generate an audit record.

**Rule ID:** `SV-253009r824351_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chmod" system calls are used to change file permissions. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "chmod" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chmod /etc/audit/audit.rules -a always,exit -F arch=b32 -S chmod -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253010`

### Rule: Successful/unsuccessful uses of the chown system call in TOSS must generate an audit record.

**Rule ID:** `SV-253010r824354_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chown" system call is used to change file owner and group. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "chown" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chown /etc/audit/audit.rules -a always,exit -F arch=b32 -S chown -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253011`

### Rule: Successful/unsuccessful uses of the creat system call in TOSS must generate an audit record.

**Rule ID:** `SV-253011r824357_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "creat" system call is used to open and possibly create a file or device. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "creat" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw creat /etc/audit/audit.rules -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253012`

### Rule: Successful/unsuccessful uses of the fchmod system call in TOSS must generate an audit record.

**Rule ID:** `SV-253012r824360_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "fchmod" system call is used to change permissions of a file. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "fchmod" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w fchmod /etc/audit/audit.rules -a always,exit -F arch=b32 -S fchmod -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S fchmod -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253013`

### Rule: Successful/unsuccessful uses of the fchmodat system call in TOSS must generate an audit record.

**Rule ID:** `SV-253013r824363_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "fchmodat" system call is used to change permissions of a file relative to a directory file descriptor. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "fchmodat" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w fchmodat /etc/audit/audit.rules -a always,exit -F arch=b32 -S fchmodat -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S fchmodat -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253014`

### Rule: Successful/unsuccessful uses of the fchown system call in TOSS must generate an audit record.

**Rule ID:** `SV-253014r824366_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "fchown" system call is used to change the ownership of a file referred to by the open file descriptor. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "fchown" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w fchown /etc/audit/audit.rules -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253015`

### Rule: Successful/unsuccessful uses of the fchownat system call in TOSS must generate an audit record.

**Rule ID:** `SV-253015r824369_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "fchownat" system call is used to change ownership of a file relative to a directory file descriptor. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "fchownat" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w fchownat /etc/audit/audit.rules -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253016`

### Rule: Successful/unsuccessful uses of the ftruncate system call system call in TOSS must generate an audit record.

**Rule ID:** `SV-253016r824372_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "truncate" and "ftruncate" system calls are used to truncate a file to a specified length. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "ftruncate" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw ftruncate /etc/audit/audit.rules -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b32 -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253017`

### Rule: Successful/unsuccessful uses of the lchown system call in TOSS must generate an audit record.

**Rule ID:** `SV-253017r824375_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "lchown" system call is used to change the ownership of the file specified by a path, which does not dereference symbolic links. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "lchown" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w lchown /etc/audit/audit.rules -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253018`

### Rule: Successful/unsuccessful uses of the open system call in TOSS must generate an audit record.

**Rule ID:** `SV-253018r824378_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "open system" call opens a file specified by a pathname. If the specified file does not exist, it may optionally be created by "open." When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "open" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw open /etc/audit/audit.rules -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S open -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b32 -S open -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S open -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253019`

### Rule: Successful/unsuccessful uses of the open_by_handle_at system call system call in TOSS must generate an audit record.

**Rule ID:** `SV-253019r824381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "name_to_handle_at" and "open_by_handle_at" system calls split the functionality of openat into two parts: "name_to_handle_at" returns an opaque handle that corresponds to a specified file; "open_by_handle_at" opens the file corresponding to a handle returned by a previous call to "name_to_handle_at" and returns an open file descriptor. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "open_by_handle_at" system call by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw open_by_handle_at /etc/audit/audit.rules -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253020`

### Rule: Successful/unsuccessful uses of the openat system call in TOSS must generate an audit record.

**Rule ID:** `SV-253020r824384_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "openat" system call opens a file specified by a relative pathname. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "openat" system calls by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw openat /etc/audit/audit.rules -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b32 -S openat -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S openat -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253021`

### Rule: Successful/unsuccessful uses of the truncate system call in TOSS must generate an audit record.

**Rule ID:** `SV-253021r824387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "truncate" system calls are used to truncate a file to a specified length. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful attempts to use the "truncate" system calls by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw truncate /etc/audit/audit.rules -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b32 -S truncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S truncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-253022`

### Rule: TOSS audit tools must be owned by "root".

**Rule ID:** `SV-253022r825980_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are owned by "root" to prevent any unauthorized access, deletion, or modification. Check the owner of each audit tool by running the following command: $ sudo stat -c "%U %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any of the audit tools are not owned by "root", this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-253023`

### Rule: TOSS must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-253023r877393_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed in order to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is properly configured to use cryptographic mechanisms to protect the integrity of audit tools. If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. Check the selection lines to ensure AIDE is configured to add/check with the following command: $ sudo egrep '(\/usr\/sbin\/(audit|au|rsys))' /etc/aide.conf /usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/rsyslogd p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512 If any of the audit tools listed above do not have an appropriate selection line, ask the system administrator to indicate what cryptographic mechanisms are being used to protect the integrity of the audit tools. If there is no evidence of integrity protection, this is a finding. If any of the audit tools are not installed on the system, the corresponding AIDE rule is not applicable.

## Group: SRG-OS-000303-GPOS-00120

**Group ID:** `V-253024`

### Rule: TOSS must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group".

**Rule ID:** `SV-253024r825983_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable a new or disabled account. Auditing account modification actions provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/group /etc/audit/audit.rules -w /etc/group -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000303-GPOS-00120

**Group ID:** `V-253025`

### Rule: TOSS must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow".

**Rule ID:** `SV-253025r825986_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable a new or disabled account. Auditing account modification actions provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/gshadow /etc/audit/audit.rules -w /etc/gshadow -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000303-GPOS-00120

**Group ID:** `V-253026`

### Rule: TOSS must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd".

**Rule ID:** `SV-253026r825989_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable a new or disabled account. Auditing account modification actions provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/passwd /etc/audit/audit.rules -w /etc/passwd -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000303-GPOS-00120

**Group ID:** `V-253027`

### Rule: TOSS must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/security/opasswd".

**Rule ID:** `SV-253027r825992_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable a new or disabled account. Auditing account modification actions provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/security/opasswd". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/security/opasswd /etc/audit/audit.rules -w /etc/security/opasswd -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000303-GPOS-00120

**Group ID:** `V-253028`

### Rule: TOSS must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers".

**Rule ID:** `SV-253028r825995_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable a new or disabled account. Auditing account modification actions provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/sudoers /etc/audit/audit.rules -w /etc/sudoers -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000303-GPOS-00120

**Group ID:** `V-253029`

### Rule: TOSS must generate audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers.d/".

**Rule ID:** `SV-253029r825998_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable a new or disabled account. Auditing account modification actions provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers.d/". Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo grep /etc/sudoers.d/ /etc/audit/audit.rules -w /etc/sudoers.d/ -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-253030`

### Rule: The TOSS audit system must prevent all software from executing at higher privilege levels than users executing the software and the audit system must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-253030r824762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review. Satisfies: SRG-OS-000326-GPOS-00126, SRG-OS-000327-GPOS-00127</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS audits the execution of privileged functions. Check if TOSS is configured to audit the execution of the "execve" system call, by running the following command: $ sudo grep execve /etc/audit/audit.rules -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-253031`

### Rule: TOSS must allocate audit record storage capacity to store at least one week's worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-253031r877391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure TOSS systems have a sufficient storage capacity in which to write the audit logs, TOSS needs to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of TOSS. If an external logging system is used to aggregate and store logs for at least one week, this requirement is Not Applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS allocates audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility. If logs are immediately sent to a central audit record storage facility, this requirement is Not Applicable. Determine to which partition the audit records are being written with the following command: $ sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition to which audit records are written (with the example being /var/log/audit/) with the following command: $ sudo df -h /var/log/audit/audit.log /dev/sda2 24G 10.4G 13.6G 43% /var/log/audit If the audit records are not written to a partition made specifically for audit records (/var/log/audit is a separate partition), determine the amount of space being used by other files in the partition with the following command: $ sudo du -sh [audit_partition] 1.8G /var/log/audit If the audit record partition is not allocated for sufficient storage capacity, this is a finding. Note: The partition size needed to capture a week of audit records is based on the activity level of the system and the total storage capacity available. Typically, 10.0 GB of storage space for audit records should be sufficient.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-253032`

### Rule: The TOSS audit records must be offloaded onto a different system or storage media from the system being audited.

**Rule ID:** `SV-253032r944959_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. TOSS installation media provides "rsyslogd." "rsyslogd" is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Couple this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS, and DTLS protocols), and now there is a method to securely encrypt and offload auditing. Rsyslog provides three ways to forward message: the traditional UDP transport, which is extremely lossy but standard; the plain TCP based transport, which loses messages only during certain situations but is widely available; and the RELP transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above. Examples of each configuration: UDP *.* @remotesystemname TCP *.* @@remotesystemname RELP *.* :omrelp:remotesystemname:2514 Note that a port number was given as there is no standard port for RELP. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system offloads audit records onto a different system or media from the system being audited with the following command: $ sudo grep @@ /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:*.* @@[remoteloggingserver]:[port] If a remote server is not configured, or the line is commented out, ask the System Administrator to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the audit logs are being offloaded to another system or media, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-253033`

### Rule: TOSS must label all off-loaded audit logs before sending them to the central log server.

**Rule ID:** `SV-253033r877390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Enriched logging is needed to determine who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult. When audit logs are not labeled before they are sent to a central log server, the audit data will not be able to be analyzed and tied back to the correct system. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the TOSS audit Daemon is configured to label all off-loaded audit logs, with the following command: $ sudo grep "name_format" /etc/audit/auditd.conf name_format = hostname If the "name_format" option is not "hostname", "fqd", or "numeric", or the line is commented out, this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-253034`

### Rule: The TOSS audit system must be configured to audit any usage of the "fsetxattr" system call.

**Rule ID:** `SV-253034r824774_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). "Fsetxattr" is a system call used to set an extended attribute value. This is used to set extended attributes on a file. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The auid representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if TOSS is configured to audit the execution of the "fsetxattr" system call, by running the following command: $ sudo grep -w fsetxattr /etc/audit/audit.rules -a always,exit -F arch=b32 -S fsetxattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S fsetxattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b32 -S fsetxattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S fsetxattr -F auid=0 -k perm_mod If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-253035`

### Rule: The TOSS audit system must be configured to audit any usage of the "lsetxattr" system call.

**Rule ID:** `SV-253035r824777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). "Lsetxattr" is a system call used to set an extended attribute value. This is used to set extended attributes on a symbolic link. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way. Satisfies: SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if TOSS is configured to audit the execution of the "lsetxattr" system call, by running the following command: $ sudo grep -w lsetxattr /etc/audit/audit.rules -a always,exit -F arch=b32 -S lsetxattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S lsetxattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b32 -S lsetxattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S lsetxattr -F auid=0 -k perm_mod If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-253036`

### Rule: Successful/unsuccessful uses of the fremovexattr system call in TOSS must generate an audit record.

**Rule ID:** `SV-253036r824780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). "Fremovexattr" is a system call that removes extended attributes. This is used for removal of extended attributes from a file. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if TOSS is configured to audit the execution of the "fremovexattr" system call, by running the following command: $ sudo grep -w fremovexattr /etc/audit/audit.rules -a always,exit -F arch=b32 -S fremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S fremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b32 -S fremovexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S fremovexattr -F auid=0 -k perm_mod If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-253037`

### Rule: Successful/unsuccessful uses of the "lremovexattr" system call in TOSS must generate an audit record.

**Rule ID:** `SV-253037r824783_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). "Lremovexattr" is a system call that removes extended attributes. This is used for removal of extended attributes from symbolic links. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if TOSS is configured to audit the execution of the "lremovexattr" system call, by running the following command: $ sudo grep -w lremovexattr /etc/audit/audit.rules -a always,exit -F arch=b32 -S lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b32 -S lremovexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S lremovexattr -F auid=0 -k perm_mod If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-253038`

### Rule: Successful/unsuccessful uses of the "removexattr" system call in TOSS must generate an audit record.

**Rule ID:** `SV-253038r824786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). "Removexattr" is a system call that removes extended attributes. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1." The AUID representation is an unsigned 32-bit integer, which equals "4294967295." The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if TOSS is configured to audit the execution of the "removexattr" system call, by running the following command: $ sudo grep -w removexattr /etc/audit/audit.rules -a always,exit -F arch=b32 -S removexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S removexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b32 -S removexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S removexattr -F auid=0 -k perm_mod If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-253039`

### Rule: Successful/unsuccessful modifications to the "lastlog" file in TOSS must generate an audit record.

**Rule ID:** `SV-253039r824789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates an audit record when successful/unsuccessful modifications to the "lastlog" file by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253040`

### Rule: Successful/unsuccessful uses of "semanage" in TOSS must generate an audit record.

**Rule ID:** `SV-253040r824792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "semanage" command is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of "semanage" by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "semanage" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253041`

### Rule: Successful/unsuccessful uses of the "gpasswd" command in TOSS must generate an audit record.

**Rule ID:** `SV-253041r824795_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "gpasswd" command is used to administer /etc/group and /etc/gshadow. Every group can have administrators, members and a password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "gpasswd" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w gpasswd /etc/audit/audit.rules -a always,exit -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253042`

### Rule: Successful/unsuccessful uses of the "mount" command in TOSS must generate an audit record.

**Rule ID:** `SV-253042r824798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "mount" command is used to mount a filesystem.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "mount" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w /usr/bin/mount /etc/audit/audit.rules -a always,exit -F path=/usr/bin/mount -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253043`

### Rule: Successful/unsuccessful uses of the "mount" syscall in TOSS must generate an audit record.

**Rule ID:** `SV-253043r824801_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "mount" syscall is used to mount a filesystem.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "mount" syscall by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "\-S mount" /etc/audit/audit.rules -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=unset -k privileged -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253044`

### Rule: Successful/unsuccessful uses of the "su" command in TOSS must generate an audit record.

**Rule ID:** `SV-253044r824804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "su" command allows a user to run commands with a substitute user and group ID.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS generates audit records when successful/unsuccessful attempts to use the "su" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w /usr/bin/su /etc/audit/audit.rules -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253045`

### Rule: Successful/unsuccessful uses of the "umount" command in TOSS must generate an audit record.

**Rule ID:** `SV-253045r824807_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "umount" command is used to unmount a filesystem.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "umount" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w /usr/bin/umount /etc/audit/audit.rules -a always,exit -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253046`

### Rule: Successful/unsuccessful uses of the "unix_update" in TOSS must generate an audit record.

**Rule ID:** `SV-253046r824810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). "unix_update" is a helper program for the "pam_unix" module that updates the password for a given user. It is not intended to be run directly from the command line and logs a security violation if done so.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "unix_update" by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "unix_update" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253047`

### Rule: Successful/unsuccessful uses of the "usermod" command in TOSS must generate an audit record.

**Rule ID:** `SV-253047r824813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "usermod" command modifies the system account files to reflect the changes that are specified on the command line.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "usermod" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w usermod /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253048`

### Rule: Successful/unsuccessful uses of "unix_chkpwd" in TOSS must generate an audit record.

**Rule ID:** `SV-253048r824816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "unix_chkpwd" command is a helper program for the pam_unix module that verifies the password of the current user. It also checks password and account expiration dates in shadow. It is not intended to be run directly from the command line and logs a security violation if done so.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of "unix_chkpwd" by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "unix_chkpwd" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253049`

### Rule: Successful/unsuccessful uses of "userhelper" in TOSS must generate an audit record.

**Rule ID:** `SV-253049r824819_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "userhelper" command is not intended to be run interactively. "Userhelper" provides a basic interface to change a user's password, gecos information, and shell. The main difference between this program and its traditional equivalents (passwd, chfn, chsh) is that prompts are written to standard out to make it easy for a graphical user interface wrapper to interface to it as a child process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of "userhelper" by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w "userhelper" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=unset -k privileged If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000471-GPOS-00216

**Group ID:** `V-253050`

### Rule: Successful/unsuccessful uses of the "kmod" command in TOSS must generate an audit record.

**Rule ID:** `SV-253050r824822_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "kmod" command is used to control Linux Kernel modules. Satisfies: SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that TOSS is configured to audit the execution of the module management program "kmod", by running the following command: $ sudo grep "/usr/bin/kmod" /etc/audit/audit.rules -a always,exit -F path=/usr/bin/kmod -F perm=x -F auid>=1000 -F auid!=unset -k modules If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253051`

### Rule: The auditd service must be running in TOSS.

**Rule ID:** `SV-253051r824825_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring TOSS to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across the DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit service is enabled and active with the following commands: $ sudo systemctl is-enabled auditd enabled $ sudo systemctl is-active auditd active If the service is not "enabled" and "active" this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253052`

### Rule: The TOSS audit system must audit local events.

**Rule ID:** `SV-253052r824828_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the TOSS audit Daemon is configured to include local events, with the following command: $ sudo grep local_events /etc/audit/auditd.conf local_events = yes If the value of the "local_events" option is not set to "yes", or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253053`

### Rule: TOSS must resolve audit information before writing to disk.

**Rule ID:** `SV-253053r824831_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Enriched logging aids in making sense of who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the TOSS audit daemon is configured to resolve audit information before writing to disk, with the following command: $ sudo grep "log_format" /etc/audit/auditd.conf log_format = ENRICHED If the "log_format" option is not "ENRICHED", or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253054`

### Rule: TOSS must have the packages required for offloading audit logs installed.

**Rule ID:** `SV-253054r826062_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. TOSS installation media provides "rsyslogd." "rsyslogd" is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Couple this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS, and DTLS protocols), and now there is a method to securely encrypt and offload auditing. Rsyslog provides three ways to forward message: the traditional UDP transport, which is extremely lossy but standard; the plain TCP based transport, which loses messages only during certain situations but is widely available; and the RELP transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above. Examples of each configuration: UDP *.* @remotesystemname TCP *.* @@remotesystemname RELP *.* :omrelp:remotesystemname:2514 Note that a port number was given as there is no standard port for RELP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system has the packages required for offloading audit logs installed with the following commands: $ sudo yum list installed rsyslog rsyslog.x86_64 8.2102.0-5.el8 @AppStream If the "rsyslog" package is not installed, ask the administrator to indicate how audit logs are being offloaded and what packages are installed to support it. If there is no evidence of audit logs being offloaded, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253055`

### Rule: TOSS must have the packages required for encrypting offloaded audit logs installed.

**Rule ID:** `SV-253055r826063_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. TOSS installation media provides "rsyslogd." "rsyslogd" is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Couple this utility with "rsyslog-gnutls" (which is a secure communications library implementing the SSL, TLS, and DTLS protocols), and now there is a method to securely encrypt and offload auditing. Rsyslog provides three ways to forward message: the traditional UDP transport, which is extremely lossy but standard; the plain TCP based transport, which loses messages only during certain situations but is widely available; and the RELP transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above. Examples of each configuration: UDP *.* @remotesystemname TCP *.* @@remotesystemname RELP *.* :omrelp:remotesystemname:2514 Note that a port number was given as there is no standard port for RELP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system has the packages required for encrypting offloaded audit logs installed with the following commands: $ sudo yum list installed rsyslog-gnutls rsyslog-gnutls.x86_64 8.2102.0-5.el8 @AppStream If the "rsyslog-gnutls" package is not installed, ask the administrator to indicate how audit logs are being encrypted during offloading and what packages are installed to support it. If there is no evidence of audit logs being encrypted during offloading, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-253056`

### Rule: TOSS must monitor remote access methods.

**Rule ID:** `SV-253056r824840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that TOSS monitors all remote access methods. Check that remote access methods are being logged by running the following command: $ sudo grep -E '(auth.*|authpriv.*|daemon.*)' /etc/rsyslog.conf auth.*;authpriv.*;daemon.* /var/log/secure If any of "auth.*", "authpriv.*" or "daemon.*" are not configured to be logged, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-253057`

### Rule: TOSS must force a frequent session key renegotiation for SSH connections by the client.

**Rule ID:** `SV-253057r877398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Session key regeneration limits the chances of a session key becoming compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH client is configured to force frequent session key renegotiation with the following command: $ sudo grep -i RekeyLimit /etc/ssh/ssh_config RekeyLimit 1G 1h If "RekeyLimit" does not have a maximum data amount and maximum time defined, is missing or commented out, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-253058`

### Rule: TOSS must force a frequent session key renegotiation for SSH connections to the server.

**Rule ID:** `SV-253058r877398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Session key regeneration limits the chances of a session key becoming compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to force frequent session key renegotiation with the following command: $ sudo grep -i RekeyLimit /etc/ssh/sshd_config RekeyLimit 1G 1h If "RekeyLimit" does not have a maximum data amount and maximum time defined, is missing or commented out, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-253059`

### Rule: TOSS must implement NIST FIPS-validated cryptography for the following: to provision digital signatures; to generate cryptographic hashes; and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-253059r877398_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. TOSS utilizes GRUB 2 as the default bootloader. Note that GRUB 2 command-line parameters are defined in the "kernelopts" variable of the /boot/grub2/grubenv file for all kernel boot entries. The command "fips-mode-setup" modifies the "kernelopts" variable, which in turn updates all kernel boot entries. The fips=1 kernel option needs to be added to the kernel command line during system installation so that key generation is done with FIPS-approved algorithms and continuous monitoring tests in place. Users must also ensure the system has plenty of entropy during the installation process by moving the mouse around, or if no mouse is available, ensuring that many keystrokes are typed. The recommended amount of keystrokes is 256 and more. Less than 256 keystrokes may generate a non-unique key. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000396-GPOS-00176, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS implements DoD-approved encryption to protect the confidentiality of remote access sessions. Check to see if FIPS mode is enabled with the following command: $ fips-mode-setup --check FIPS mode is enabled If FIPS mode is "enabled", check to see if the kernel boot parameter is configured for FIPS mode with the following command: $ sudo grub2-editenv list | grep fips kernelopts=root=/dev/mapper/rhel-root ro crashkernel=auto resume=/dev/mapper/rhel-swap rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet fips=1 boot=UUID=8d171156-cd61-421c-ba41-1c021ac29e82 If the kernel boot parameter is configured to use FIPS mode, check to see if the system is in FIPS mode with the following command: $ sudo cat /proc/sys/crypto/fips_enabled 1 If FIPS mode is not "on", the kernel boot parameter is not configured for FIPS mode, or the system does not have a value of "1" for "fips_enabled" in "/proc/sys/crypto", this is a finding. If the hardware configuration of the operating system does not allow for enabling FIPS mode, and has been documented with the Information System Security Officer (ISSO), this requirement is Not Applicable.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-253060`

### Rule: TOSS must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-253060r824852_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. TOSS utilizes "pwquality" as a mechanism to enforce password complexity. Note that in order to require uppercase characters, without degrading the "minlen" value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value for "ucredit" in "/etc/security/pwquality.conf" with the following command: $ sudo grep ucredit /etc/security/pwquality.conf ucredit = -1 If the value of "ucredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-253061`

### Rule: TOSS must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-253061r824855_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. TOSS utilizes "pwquality" as a mechanism to enforce password complexity. Note that in order to require lower-case characters, without degrading the "minlen" value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value for "lcredit" in "/etc/security/pwquality.conf" with the following command: $ sudo grep lcredit /etc/security/pwquality.conf lcredit = -1 If the value of "lcredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-253062`

### Rule: TOSS must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-253062r824858_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. TOSS utilizes "pwquality" as a mechanism to enforce password complexity. Note that in order to require numeric characters, without degrading the minlen value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value for "dcredit" in "/etc/security/pwquality.conf" with the following command: $ sudo grep dcredit /etc/security/pwquality.conf dcredit = -1 If the value of "dcredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-253063`

### Rule: TOSS must require the change of at least eight characters when passwords are changed.

**Rule ID:** `SV-253063r824861_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least 8 characters. TOSS utilizes "pwquality" as a mechanism to enforce password complexity. The "difok" option sets the number of characters in a password that must not be present in the old password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value of the "difok" option in "/etc/security/pwquality.conf" with the following command: $ sudo grep difok /etc/security/pwquality.conf difok = 8 If the value of "difok" is set to less than "8" or is commented out, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-253064`

### Rule: TOSS must store only encrypted representations of passwords.

**Rule ID:** `SV-253064r877397_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the TOSS shadow password suite configuration is set to encrypt password with a FIPS 140-2-approved cryptographic hashing algorithm. Check the hashing algorithm that is being used to hash passwords with the following command: $ sudo grep -i crypt /etc/login.defs ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" does not equal SHA512 or greater, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-253065`

### Rule: TOSS must not have the rsh-server package installed.

**Rule ID:** `SV-253065r877396_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. The rsh-server service provides an unencrypted remote access service that does not provide for the confidentiality and integrity of user passwords or the remote session and has very weak authentication. Satisfies: SRG-OS-000074-GPOS-00042, SRG-OS-000095-GPOS-00049</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if the rsh-server package is installed with the following command: $ sudo yum list installed rsh-server If the rsh-server package is installed, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-253066`

### Rule: TOSS must enforce 24 hours/1 day as the minimum password lifetime.

**Rule ID:** `SV-253066r824870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that TOSS enforces 24 hours/1 day as the minimum password lifetime for new user accounts. Check for the value of "PASS_MIN_DAYS" in "/etc/login.defs" with the following command: $ sudo grep -i pass_min_days /etc/login.defs PASS_MIN_DAYS 1 If the "PASS_MIN_DAYS" parameter value is not "1" or greater, or is commented out, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-253067`

### Rule: TOSS must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-253067r824873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that TOSS enforces a 60-day maximum password lifetime for new user accounts by running the following command: $ sudo grep -i pass_max_days /etc/login.defs PASS_MAX_DAYS 60 If the "PASS_MAX_DAYS" parameter value is greater than "60", or commented out, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-253068`

### Rule: TOSS must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-253068r824876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS prohibits password reuse for a minimum of five generations. Check for the value of the "remember" argument in "/etc/pam.d/system-auth" and "/etc/pam.d/password-auth" with the following command: $ sudo grep -i remember /etc/pam.d/system-auth /etc/pam.d/password-auth /etc/pam.d/system-auth:password required pam_pwhistory.so use_authtok remember=5 retry=3 /etc/pam.d/password-auth:password required pam_pwhistory.so use_authtok remember=5 retry=3 If either file is missing "pam_pwhistory.so" and does not have the "remember" module argument set, is commented out, or the value of the "remember" module argument is set to less than "5", this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-253069`

### Rule: TOSS must enforce a minimum 15-character password length.

**Rule ID:** `SV-253069r824879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS enforces a minimum 15-character password length. The "minlen" option sets the minimum number of characters in a new password. Check for the value of the "minlen" option in "/etc/security/pwquality.conf" with the following command: $ sudo grep minlen /etc/security/pwquality.conf minlen = 15 If the command does not return a "minlen" value of 15 or greater, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253070`

### Rule: TOSS must cover or disable the built-in or attached camera when not in use.

**Rule ID:** `SV-253070r824882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect from collaborative computing devices (i.e., cameras) can result in subsequent compromises of organizational information. Providing easy methods to physically disconnect from such devices after a collaborative computing session helps to ensure participants actually carry out the disconnect activity without having to go through complex and tedious procedures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device or operating system does not have a camera installed, this requirement is Not Applicable. This requirement is not applicable to mobile devices (smartphones and tablets), where the use of the camera is a local AO decision. This requirement is not applicable to dedicated VTC suites located in approved VTC locations that are centrally managed. For an external camera, if there is not a method for the operator to manually disconnect the camera at the end of collaborative computing sessions, this is a finding. For a built-in camera, the camera must be protected by a camera cover (e.g., laptop camera cover slide) when not in use. If the built-in camera is not protected with a camera cover, or is not physically disabled, this is a finding. If the camera is not disconnected, covered, or physically disabled, determine if it is being disabled via software with the following commands: Determine if the camera is disabled via blacklist with the following command: $ sudo grep blacklist /etc/modprobe.d/* /etc/modprobe.d/blacklist.conf:blacklist uvcvideo Determine if a camera driver is in use with the following command: $ sudo dmesg | grep -i video [ 44.630131] ACPI: Video Device [VGA] [ 46.655714] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/LNXVIDEO:00/input/input7 [ 46.670133] videodev: Linux video capture interface: v2.00 [ 47.226424] uvcvideo: Found UVC 1.00 device WebCam (0402:7675) [ 47.235752] usbcore: registered new interface driver uvcvideo [ 47.235756] USB Video Class driver (1.1.1) If the camera driver blacklist is missing, a camera driver is determined to be in use, and the collaborative computing device has not been authorized for use, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253071`

### Rule: TOSS must disable IEEE 1394 (FireWire) Support.

**Rule ID:** `SV-253071r824885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The IEEE 1394 (FireWire) is a serial bus standard for high-speed real-time communication. Disabling FireWire protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the firewire-core kernel module. $ sudo grep -r firewire-core /etc/modprobe.d/* | grep install install firewire-core /bin/false If the command does not return any output, or the line is commented out, and use of the firewire-core protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the firewire-core kernel module. Check to see if the firewire-core kernel module is disabled with the following command: $ sudo grep -r firewire-core /etc/modprobe.d/* | grep "blacklist" blacklist firewire-core If the command does not return any output or the output is not "blacklist firewire-core", and use of the firewire-core kernel module is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253072`

### Rule: TOSS must disable mounting of cramfs.

**Rule ID:** `SV-253072r824888_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Removing support for unneeded filesystem types reduces the local attack surface of the server. Compressed ROM/RAM file system (or cramfs) is a read-only file system designed for simplicity and space efficiency. It is mainly used in embedded and small footprint systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the cramfs kernel module. $ sudo grep -r cramfs /etc/modprobe.d/* | grep install install cramfs /bin/false If the command does not return any output, or the line is commented out, and use of the cramfs protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the cramfs kernel module. Check to see if the cramfs kernel module is disabled with the following command: $ sudo grep -r cramfs /etc/modprobe.d/* | grep "blacklist" blacklist cramfs If the command does not return any output or the output is not "blacklist cramfs", and use of the cramfs kernel module is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253073`

### Rule: TOSS must disable network management of the chrony daemon.

**Rule ID:** `SV-253073r824891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time when a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Not exposing the management interface of the chrony daemon on the network diminishes the attack space. TOSS utilizes the "timedatectl" command to view the status of the "systemd-timesyncd.service." The "timedatectl" status will display the local time, UTC, and the offset from UTC. Note that USNO offers authenticated NTP service to DoD and U.S. Government agencies operating on the NIPR and SIPR networks. Visit https://www.usno.navy.mil/USNO/time/ntp/dod-customers for more information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS disables network management of the chrony daemon with the following command: $ sudo grep -w 'cmdport' /etc/chrony.conf cmdport 0 If the "cmdport" option is not set to "0", is commented out or missing, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253074`

### Rule: TOSS must disable the asynchronous transfer mode (ATM) protocol.

**Rule ID:** `SV-253074r824894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect unused protocols can result in a system compromise. The Asynchronous Transfer Mode (ATM) is a protocol operating on network, data link, and physical layers, based on virtual circuits and virtual paths. Disabling ATM protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the ATM protocol kernel module. $ sudo grep -r atm /etc/modprobe.d/* | grep install install atm /bin/false If the command does not return any output, or the line is commented out, and use of the ATM protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the ATM protocol. Check to see if the ATM protocol is disabled with the following command: $ sudo grep -r atm /etc/modprobe.d/* | grep "blacklist" blacklist atm If the command does not return any output or the output is not "blacklist atm", and use of the ATM protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253075`

### Rule: TOSS must disable the controller area network (CAN) protocol.

**Rule ID:** `SV-253075r824897_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect unused protocols can result in a system compromise. The Controller Area Network (CAN) is a serial communications protocol, which was initially developed for automotive and is now also used in marine, industrial, and medical applications. Disabling CAN protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the CAN protocol kernel module. $ sudo grep -r can /etc/modprobe.d/* | grep install install can /bin/false If the command does not return any output, or the line is commented out, and use of the CAN protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the CAN protocol. Check to see if the CAN protocol is disabled with the following command: $ sudo grep -r can /etc/modprobe.d/* | grep "blacklist" blacklist can If the command does not return any output or the output is not "blacklist can", and use of the CAN protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253076`

### Rule: TOSS must disable the stream control transmission (SCTP) protocol.

**Rule ID:** `SV-253076r824900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect unused protocols can result in a system compromise. The Stream Control Transmission Protocol (SCTP) is a transport layer protocol, designed to support the idea of message-oriented communication, with several streams of messages within one connection. Disabling SCTP protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the SCTP protocol kernel module. $ sudo grep -r sctp /etc/modprobe.d/* | grep install install sctp /bin/false If the command does not return any output, or the line is commented out, and use of the SCTP protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the SCTP protocol. Check to see if the SCTP protocol is disabled with the following command: $ sudo grep -r sctp /etc/modprobe.d/* | grep "blacklist" blacklist sctp If the command does not return any output or the output is not "blacklist sctp", and use of the SCTP protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253077`

### Rule: TOSS must disable the transparent inter-process communication (TIPC) protocol.

**Rule ID:** `SV-253077r824903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect unused protocols can result in a system compromise. The Transparent Inter-Process Communication (TIPC) protocol is designed to provide communications between nodes in a cluster. Disabling TIPC protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the TIPC protocol kernel module. $ sudo grep -r tipc /etc/modprobe.d/* | grep install install tipc /bin/false If the command does not return any output, or the line is commented out, and use of the TIPC protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the TIPC protocol. Check to see if the TIPC protocol is disabled with the following command: $ sudo grep -r tipc /etc/modprobe.d/* | grep "blacklist" blacklist tipc If the command does not return any output or the output is not "blacklist tipc", and use of the TIPC protocol is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253078`

### Rule: TOSS must not have any automated bug reporting tools installed.

**Rule ID:** `SV-253078r824906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Verify the operating system is configured to disable non-essential capabilities. The most secure way of ensuring a non-essential capability is disabled is to not have the capability installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if any automated bug reporting packages are installed with the following command: $ sudo yum list installed abrt* If any automated bug reporting package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253079`

### Rule: TOSS must not have the sendmail package installed.

**Rule ID:** `SV-253079r824909_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Verify the operating system is configured to disable non-essential capabilities. The most secure way of ensuring a non-essential capability is disabled is to not have the capability installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if the sendmail package is installed with the following command: $ sudo yum list installed sendmail If the sendmail package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253080`

### Rule: TOSS must not have the telnet-server package installed.

**Rule ID:** `SV-253080r824912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Verify the operating system is configured to disable non-essential capabilities. The most secure way of ensuring a non-essential capability is disabled is to not have the capability installed. The telnet service provides an unencrypted remote access service that does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to log on using this service, the privileged user password could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if the telnet-server package is installed with the following command: $ sudo yum list installed telnet-server If the telnet-server package is installed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-253081`

### Rule: TOSS must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-253081r824915_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the firewall configuration and running services to verify it is configured to prohibit or restrict the use of functions, ports, protocols, and/or services that are unnecessary or prohibited. Check which services are currently active with the following command: $ sudo firewall-cmd --list-all-zones custom (active) target: DROP icmp-block-inversion: no interfaces: ens33 sources: services: dhcpv6-client dns http https ldaps rpc-bind ssh ports: masquerade: no forward-ports: icmp-blocks: rich rules: Ask the System Administrator for the site or program Ports, Protocols, and Services Management Component Local Service Assessment (PPSM CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM Category Assurance List (CAL), this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-253082`

### Rule: TOSS must be configured to disable USB mass storage.

**Rule ID:** `SV-253082r942859_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB mass storage permits easy introduction of unknown devices, thereby facilitating malicious activity. Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the USB Storage kernel module. $ sudo grep -r usb-storage /etc/modprobe.d/* | grep "install" install usb-storage /bin/false If the command does not return any output, or the line is commented out, and use of USB Storage is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use USB mass storage devices. Check to see if USB mass storage is disabled with the following command: $ sudo grep -r usb-storage /etc/modprobe.d/* | grep "blacklist" blacklist usb-storage If the command does not return any output or the output is not "blacklist usb-storage", and use of USB storage devices is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-253083`

### Rule: TOSS must be configured so that all network connections associated with SSH traffic are terminated at the end of the session or after 10 minutes of inactivity, except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-253083r824921_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. TOSS utilizes /etc/ssh/sshd_config for configurations of OpenSSH. Within the sshd_config the product of the values of "ClientAliveInterval" and "ClientAliveCountMax" are used to establish the inactivity threshold. The "ClientAliveInterval" is a timeout interval in seconds after which if no data has been received from the client, sshd will send a message through the encrypted channel to request a response from the client. The "ClientAliveCountMax" is the number of client alive messages that may be sent without sshd receiving any messages back from the client. If this threshold is met, sshd will disconnect the client. The default setting for "ClientAliveCountMax" is "3." If "ClientAliveInterval is set to "15" and "ClientAliveCountMax" is left at the default, unresponsive SSH clients will be disconnected after approximately 45 seconds. Satisfies: SRG-OS-000126-GPOS-00066, SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all network connections associated with SSH traffic are automatically terminated at the end of the session or after 10 minutes of inactivity, or as long as documented with the Information System Security Officer (ISSO) as an operational requirement. Check that the "ClientAliveInterval" variable is set to a value of "600" or less and that the "ClientAliveCountMax" is set to "1" by performing the following command: $ sudo grep -i clientalive /etc/ssh/sshd_config ClientAliveInterval 600 ClientAliveCountMax 1 If "ClientAliveInterval" and "ClientAliveCountMax" do not exist, does not have a product value of "600" or less in "/etc/ssh/sshd_config", or is commented out, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-253084`

### Rule: TOSS must have policycoreutils package installed.

**Rule ID:** `SV-253084r824924_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Policycoreutils contains the policy core utilities that are required for basic operation of an SELinux-enabled system. These utilities include load_policy to load SELinux policies, setfile to label filesystems, newrole to switch roles, and run_init to run /etc/init.d scripts in the proper context.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system has the policycoreutils package installed with the following command: $ sudo yum list installed policycoreutils policycoreutils.x86_64 2.9-16.el8 @anaconda If the policycoreutils package is not installed, this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-253085`

### Rule: All TOSS local disk partitions must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection.

**Rule ID:** `SV-253085r824927_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>TOSS systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption. If there is a documented and approved reason for not having data-at-rest encryption, this requirement is Not Applicable. Verify all local system partitions are encrypted with the following command: $ sudo blkid /dev/mapper/rhel-root: UUID="67b7d7fe-de60-6fd0-befb-e6748cf97743" TYPE="crypto_LUKS" Every persistent disk partition present must be of TYPE "crypto_LUKS." If any partitions other than pseudo file systems (such as /proc or /sys) are not type "crypto_LUKS", ask the administrator to indicate how the partitions are encrypted. If there is no evidence that all local disk partitions are encrypted, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-253086`

### Rule: TOSS must limit privileges to change software resident within software libraries.

**Rule ID:** `SV-253086r824930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to TOSS with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are owned by "root" or an appropriate system account with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -exec ls -l {} \; If any system commands are returned which are not owned by an appropriate system account, this is a finding. Verify the system-wide shared library files are owned by "root" or an appropriate system account with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -user root -exec ls -l {} \; If any system wide shared library file is returned which is not owned by an appropriate system account, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-253087`

### Rule: TOSS must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-253087r824933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. TOSS utilizes "pwquality" as a mechanism to enforce password complexity. Note that to require special characters without degrading the "minlen" value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value for "ocredit" in "/etc/security/pwquality.conf" with the following command: $ sudo grep ocredit /etc/security/pwquality.conf ocredit = -1 If the value of "ocredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-253088`

### Rule: A firewall must be installed on TOSS.

**Rule ID:** `SV-253088r824936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"Firewalld" provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols. Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. TOSS functionality (e.g., SSH) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "firewalld" is installed and active with the following commands: $ sudo yum list installed firewalld firewalld.noarch 0.9.3-7.el8 $ sudo systemctl is-active firewalld active If the "firewalld" package is not installed and "active", ask the System Administrator if another firewall is installed. If no firewall is installed and active this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-253089`

### Rule: TOSS must take appropriate action when the internal event queue is full.

**Rule ID:** `SV-253089r877390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. TOSS installation media provides "rsyslogd." "rsyslogd" is a system utility providing support for message logging. Support for both internet and UNIX domain sockets enables this utility to support both local and remote logging. Couple this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS, and DTLS protocols), and now there is a method to securely encrypt and offload auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system is configured to take an appropriate action when the internal event queue is full: $ sudo grep -i overflow_action /etc/audit/auditd.conf overflow_action = syslog If the value of the "overflow_action" option is not set to "syslog", "single", "halt", or the line is commented out, ask the System Administrator to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the transfer of the audit logs being offloaded to another system or media takes appropriate action if the internal event queue becomes full, this is a finding.

## Group: SRG-OS-000376-GPOS-00161

**Group ID:** `V-253090`

### Rule: TOSS must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-253090r824942_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. The DoD has mandated the use of the Common Access Card (CAC) to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS accepts PIV credentials. Check that the "opensc" package is installed on the system with the following command: $ sudo yum list installed opensc opensc.x86_64 0.20.0-4.el8 @anaconda Check that "opensc" accepts PIV cards with the following command: $ sudo opensc-tool --list-drivers | grep -i piv PIV-II Personal Identity Verification Card If the "opensc" package is not installed and the "opensc-tool" driver list does not include "PIV-II", this is a finding.

## Group: SRG-OS-000393-GPOS-00173

**Group ID:** `V-253091`

### Rule: TOSS must implement DoD-approved encryption in the OpenSSL package.

**Rule ID:** `SV-253091r877382_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. TOSS incorporates system-wide crypto policies by default. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/openssl.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OpenSSL library is configured to use only ciphers employing FIPS 140-2-approved algorithms: Verify that system-wide crypto policies are in effect: $ sudo grep -i opensslcnf.config /etc/pki/tls/openssl.cnf .include /etc/crypto-policies/back-ends/opensslcnf.config If the "opensslcnf.config" is not defined in the "/etc/pki/tls/openssl.cnf" file, this is a finding. Verify which system-wide crypto policy is in use: $ sudo update-crypto-policies --show FIPS:OSPP If the system-wide crypto policy is set to anything other than "FIPS" or "FIPS:OSPP", this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-253092`

### Rule: A firewall must be able to protect against or limit the effects of Denial of Service (DoS) attacks by ensuring TOSS can implement rate-limiting measures on impacted network interfaces.

**Rule ID:** `SV-253092r824948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of TOSS to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exists to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. Since version 0.6.0, "firewalld" has incorporated "nftables" as its backend support. Utilizing the limit statement in "nftables" can help to mitigate DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "firewalld" has "nftables" set as the default backend: $ sudo grep -i firewallbackend /etc/firewalld/firewalld.conf # FirewallBackend FirewallBackend=nftables If the "nftables" is not set as the "firewallbackend" default, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-253093`

### Rule: TOSS must implement non-executable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-253093r824951_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NX (no-execution) bit flag is set on the system. Check that the no-execution bit flag is set with the following commands: $ sudo dmesg | grep NX [ 0.000000] NX (Execute Disable) protection: active If "dmesg" does not show "NX (Execute Disable) protection" active, check the cpuinfo settings with the following command: $ sudo less /proc/cpuinfo | grep -i flags flags : fpu vme de pse tsc ms nx rdtscp lm constant_tsc If "flags" does not contain the "nx" flag, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-253094`

### Rule: YUM must remove all software components after updated versions have been installed on TOSS.

**Rule ID:** `SV-253094r824954_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system removes all software components after updated versions have been installed. Check if YUM is configured to remove unneeded packages with the following command: $ sudo grep -i clean_requirements_on_remove /etc/dnf/dnf.conf clean_requirements_on_remove=True If "clean_requirements_on_remove" is not set to either "1", "True", or "yes", commented out, or is missing from "/etc/dnf/dnf.conf", this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-253095`

### Rule: TOSS must enable the "SELinux" targeted policy.

**Rule ID:** `SV-253095r824957_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure TOSS verifies correct operation of all security functions. Check if "SELinux" is active and is enforcing the targeted policy with the following command: $ sudo sestatus SELinux status: enabled SELinuxfs mount: /sys/fs/selinux SELinux root directory: /etc/selinux Loaded policy name: targeted Current mode: enforcing Mode from config file: enforcing Policy MLS status: enabled Policy deny_unknown status: allowed Memory protection checking: actual (secure) Max kernel policy version: 33 If the "Loaded policy name" is not set to "targeted", this is a finding. Verify that the /etc/selinux/config file is configured to the "SELINUXTYPE" to "targeted": $ sudo grep -i "selinuxtype" /etc/selinux/config | grep -v '^#' SELINUXTYPE = targeted If no results are returned or "SELINUXTYPE" is not set to "targeted", this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-253096`

### Rule: TOSS must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-253096r824960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If TOSS allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS prevents the use of dictionary words for passwords. Determine if the field "dictcheck" is set in the "/etc/security/pwquality.conf" or "/etc/security/pwquality.conf.d/*.conf" files with the following command: $ sudo grep -r dictcheck /etc/security/pwquality.conf /etc/security/pwquality.conf.d /etc/security/pwquality.conf:dictcheck=1 If the "dictcheck" parameter is not set to "1", or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-253097`

### Rule: TOSS must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-253097r824963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system enforces a delay of at least four seconds between console logon prompts following a failed logon attempt with the following command: $ sudo grep -i fail_delay /etc/login.defs FAIL_DELAY 4 If the value of "FAIL_DELAY" is not set to "4" or greater, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253098`

### Rule: A File Transfer Protocol (FTP) server package must not be installed unless mission essential on TOSS.

**Rule ID:** `SV-253098r824966_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The FTP service provides an unencrypted remote access that does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to log on using this service, the privileged user password could be compromised. SSH or other encrypted file transfer methods must be used in place of this service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an FTP server has not been installed on the system with the following commands: $ sudo yum list installed *ftpd* vsftpd.x86_64 3.0.3-28.el8 appstream If an FTP server is installed and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253099`

### Rule: All TOSS local files and directories must have a valid group owner.

**Rule ID:** `SV-253099r824969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files without a valid group owner may be unintentionally inherited if a group is assigned the same Group Identifier (GID) as the GID of the files without a valid group owner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all local files and directories on TOSS have a valid group with the following command: Note: The value after -fstype must be replaced with the filesystem type. XFS is used as an example. $ sudo find / -fstype xfs -nogroup If any files on the system do not have an assigned group, this is a finding. Note: Command may produce error messages from the /proc and /sys directories.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253100`

### Rule: All TOSS local files and directories must have a valid owner.

**Rule ID:** `SV-253100r824972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unowned files and directories may be unintentionally inherited if a user is assigned the same User Identifier "UID" as the UID of the un-owned files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all local files and directories on TOSS have a valid owner with the following command: Note: The value after -fstype must be replaced with the filesystem type. XFS is used as an example. $ sudo find / -fstype xfs -nouser If any files on the system do not have an assigned owner, this is a finding. Note: Command may produce error messages from the /proc and /sys directories.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253101`

### Rule: Cron logging must be implemented in TOSS.

**Rule ID:** `SV-253101r824975_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron logging can be used to trace the successful or unsuccessful execution of cron jobs. It can also be used to spot intrusions into the use of the cron facility by unauthorized and malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "rsyslog" is configured to log cron events with the following command: Note: If another logging package is used, substitute the utility configuration file for "/etc/rsyslog.conf" or "/etc/rsyslog.d/*.conf" files. $ sudo grep -r cron /etc/rsyslog.conf /etc/rsyslog.d /etc/rsyslog.conf:*.info;mail.none;authpriv.none;cron.none /var/log/messages /etc/rsyslog.conf:# Log cron stuff /etc/rsyslog.conf:cron.* /var/log/cron If the command does not return a response, check for cron logging all facilities with the following command. $ sudo grep -r /var/log/messages /etc/rsyslog.conf /etc/rsyslog.d /etc/rsyslog.conf:*.info;mail.none;authpriv.none;cron.none /var/log/messages If "rsyslog" is not logging messages for the cron facility or all facilities, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253102`

### Rule: If the Trivial File Transfer Protocol (TFTP) server is required, the TOSS TFTP daemon must be configured to operate in secure mode.

**Rule ID:** `SV-253102r824978_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting TFTP to a specific directory prevents remote users from copying, transferring, or overwriting system files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the TFTP daemon is configured to operate in secure mode with the following commands: $ sudo yum list installed tftp-server tftp-server.x86_64 x.x-x.el8 If a TFTP server is not installed, this is Not Applicable. If a TFTP server is installed, check for the server arguments with the following command: $ sudo grep server_args /etc/xinetd.d/tftp server_args = -s /var/lib/tftpboot If the "server_args" line does not have a "-s" option, and a subdirectory is not assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253103`

### Rule: The graphical display manager must not be installed on TOSS unless approved.

**Rule ID:** `SV-253103r824981_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet services that are not required for system or application processes must not be active to decrease the attack surface of the system. Graphical display managers have a long history of security vulnerabilities and must not be used, unless approved and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system is configured to boot to the command line: $ systemctl get-default multi-user.target If the system default target is not set to "multi-user.target" and the Information System Security Officer (ISSO) lacks a documented requirement for a graphical user interface, this is a finding. Verify that a graphical user interface is not installed: $ rpm -qa | grep xorg | grep server Ask the System Administrator if use of a graphical user interface is an operational requirement. If the use of a graphical user interface on the system is not documented with the ISSO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253104`

### Rule: The TOSS file integrity tool must be configured to verify Access Control Lists (ACLs).

**Rule ID:** `SV-253104r824984_rule`
**Severity:** low

**Description:**
<VulnDiscussion>ACLs can provide permissions beyond those permitted through the file mode and must be verified by file integrity tools. TOSS installation media come with a file integrity tool, Advanced Intrusion Detection Environment (AIDE).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the file integrity tool is configured to verify ACLs. Note: AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory. If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. Use the following command to determine if the file is in a location other than "/etc/aide/aide.conf": $ sudo find / -name aide.conf Check the "aide.conf" file to determine if the "acl" rule has been added to the rule list being applied to the files and directories selection lists with the following command: $ sudo egrep "[+]?acl" /etc/aide.conf VarFile = OwnerMode+n+l+X+acl If the "acl" rule is not being used on all selection lines in the "/etc/aide.conf" file, is commented out, or ACLs are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253105`

### Rule: The TOSS file integrity tool must be configured to verify extended attributes.

**Rule ID:** `SV-253105r824987_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Extended attributes in file systems are used to contain arbitrary data and file metadata with security implications. TOSS installation media come with a file integrity tool, Advanced Intrusion Detection Environment (AIDE).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the file integrity tool is configured to verify extended attributes. If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. Note: AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory. Use the following command to determine if the file is in another location: $ sudo find / -name aide.conf Check the "aide.conf" file to determine if the "xattrs" rule has been added to the rule list being applied to the files and directories selection lists. An example rule that includes the "xattrs" rule follows: All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux /bin All # apply the custom rule to the files in bin /sbin All # apply the same custom rule to the files in sbin If the "xattrs" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or extended attributes are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253106`

### Rule: The TOSS SSH daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-253106r824990_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log on to the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon performs strict mode checking of home directory configuration files with the following command: $ sudo grep -i strictmodes /etc/ssh/sshd_config StrictModes yes If "StrictModes" is set to "no", is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253107`

### Rule: The TOSS SSH private host key files must have mode 0600 or less permissive.

**Rule ID:** `SV-253107r824993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH private host key files have mode "0600" or less permissive with the following command: $ sudo ls -l /etc/ssh/ssh_host*key -rw------- 1 root ssh_keys 668 Nov 28 06:43 ssh_host_dsa_key -rw------- 1 root ssh_keys 582 Nov 28 06:43 ssh_host_key -rw------- 1 root ssh_keys 887 Nov 28 06:43 ssh_host_rsa_key If any private host key file has a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253108`

### Rule: The TOSS SSH public host key files must have mode 0644 or less permissive.

**Rule ID:** `SV-253108r824996_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH public host key files have mode "0644" or less permissive with the following command: $ sudo ls -l /etc/ssh/*.pub -rw-r--r-- 1 root root 618 Nov 28 06:43 ssh_host_dsa_key.pub -rw-r--r-- 1 root root 347 Nov 28 06:43 ssh_host_key.pub -rw-r--r-- 1 root root 238 Nov 28 06:43 ssh_host_rsa_key.pub If any key.pub file has a mode more permissive than "0644", this is a finding. Note: SSH public key files may be found in other directories on the system depending on the installation.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253109`

### Rule: The x86 Ctrl-Alt-Delete key sequence must be disabled on TOSS.

**Rule ID:** `SV-253109r824999_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user, who presses Ctrl-Alt-Delete when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS is not configured to reboot the system when Ctrl-Alt-Delete is pressed with the following command: $ sudo systemctl status ctrl-alt-del.target ctrl-alt-del.target Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) Active: inactive (dead) If the "ctrl-alt-del.target" is loaded and not masked, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253110`

### Rule: TOSS must be a vendor-supported release.

**Rule ID:** `SV-253110r825002_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An operating system release is considered "supported" if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the version of the operating system is vendor supported. Check the version of the operating system with the following command: $ sudo cat /etc/toss-release toss-release-4.3-3 Current End of support for TOSS 4.3 is 30 April 2022. Current End of support for TOSS 4.4 is 30 November 2023. Current End of support for TOSS 4.5 is 30 April 2023. Current End of support for TOSS 4.6 is 30 November 2023. Current End of support for TOSS 4.7 is 30 April 2024. Current End of support for TOSS 4.8 is 31 May 2029. If the release is not supported by the vendor, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253111`

### Rule: TOSS must be configured to prevent unrestricted mail relaying.

**Rule ID:** `SV-253111r825005_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unrestricted mail relaying is permitted, unauthorized senders could use this host as a mail relay for the purpose of sending spam or other unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is configured to prevent unrestricted mail relaying. Determine if "postfix" is installed with the following commands: $ sudo yum list installed postfix postfix.x86_64 2:3.5.8-2.el8 If postfix is not installed, this is Not Applicable. If postfix is installed, determine if it is configured to reject connections from unknown or untrusted networks with the following command: $ sudo postconf -n smtpd_client_restrictions smtpd_client_restrictions = permit_mynetworks, reject If the "smtpd_client_restrictions" parameter contains any entries other than "permit_mynetworks" and "reject", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253112`

### Rule: TOSS must define default permissions for logon and non-logon shells.

**Rule ID:** `SV-253112r825008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 600 or less permissive. Although umask can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0." This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the umask default for installed shells is "077." Check for the value of the "UMASK" parameter in the "/etc/bashrc" and "/etc/csh.cshrc" files with the following command: Note: If the value of the "UMASK" parameter is set to "000" in either the "/etc/bashrc" or the "/etc/csh.cshrc" files, the severity is raised to a CAT I. $ sudo grep -i umask /etc/bashrc /etc/csh.cshrc /etc/bashrc: umask 077 /etc/bashrc: umask 077 /etc/csh.cshrc: umask 077 /etc/csh.cshrc: umask 077 If the value for the "UMASK" parameter is not "077", or the "UMASK" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253113`

### Rule: TOSS must disable access to network bpf syscall from unprivileged processes.

**Rule ID:** `SV-253113r825011_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS prevents privilege escalation thru the kernel by disabling access to the bpf syscall with the following commands: $ sudo sysctl kernel.unprivileged_bpf_disabled kernel.unprivileged_bpf_disabled = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253114`

### Rule: TOSS must enable hardening for the Berkeley Packet Filter Just-in-time compiler.

**Rule ID:** `SV-253114r825014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Enabling hardening for the Berkeley Packet Filter (BPF) Just-in-time (JIT) compiler aids in mitigating JIT spraying attacks. Setting the value to "2" enables JIT hardening for all users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS enables hardening for the BPF JIT with the following commands: $ sudo sysctl net.core.bpf_jit_harden net.core.bpf_jit_harden = 2 If the returned line does not have a value of "2", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253115`

### Rule: TOSS must enable the hardware random number generator entropy gatherer service.

**Rule ID:** `SV-253115r825017_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The most important characteristic of a random number generator is its randomness, namely its ability to deliver random numbers that are impossible to predict. Entropy in computer security is associated with the unpredictability of a source of randomness. The random source with high entropy tends to achieve a uniform distribution of random values. Random number generators are one of the most important building blocks of cryptosystems. The rngd service feeds random data from hardware device to kernel random device. Quality (non-predictable) random number generation is important for several security functions (i.e., ciphers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TOSS has enabled the hardware random number generator entropy gatherer service. Verify the rngd service is enabled and active with the following commands: $ sudo systemctl is-enabled rngd enabled $ sudo systemctl is-active rngd active If the service is not "enable and "active", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253116`

### Rule: TOSS must ensure the SSH server uses strong entropy.

**Rule ID:** `SV-253116r825020_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The most important characteristic of a random number generator is its randomness, namely its ability to deliver random numbers that are impossible to predict. Entropy in computer security is associated with the unpredictability of a source of randomness. The random source with high entropy tends to achieve a uniform distribution of random values. Random number generators are one of the most important building blocks of cryptosystems. The SSH implementation in TOSS uses the OPENSSL library, which does not use high-entropy sources by default. By using the SSH_USE_STRONG_RNG environment variable the OPENSSL random generator is reseeded from /dev/random. This setting is not recommended on computers without the hardware random generator because insufficient entropy causes the connection to be blocked until enough entropy is available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system SSH server uses strong entropy with the following command: $ sudo grep -i ssh_use_strong_rng /etc/sysconfig/sshd SSH_USE_STRONG_RNG=32 If the "SSH_USE_STRONG_RNG" line does not equal "32", is commented out or missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253117`

### Rule: TOSS must have the packages required to use the hardware random number generator entropy gatherer service.

**Rule ID:** `SV-253117r825023_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The most important characteristic of a random number generator is its randomness, namely its ability to deliver random numbers that are impossible to predict. Entropy in computer security is associated with the unpredictability of a source of randomness. The random source with high entropy tends to achieve a uniform distribution of random values. Random number generators are one of the most important building blocks of cryptosystems. The rngd service feeds random data from hardware device to kernel random device. Quality (non-predictable) random number generation is important for several security functions (i.e., ciphers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TOSS has the packages required to enable the hardware random number generator entropy gatherer service with the following command: $ sudo yum list installed rng-tools rng-tools.x86_64 6.13-1.git.d207e0b6.el8 @anaconda If the "rng-tools" package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253118`

### Rule: TOSS must ignore IPv4 Internet Control Message Protocol (ICMP) redirect messages.

**Rule ID:** `SV-253118r825026_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS ignores IPv4 ICMP redirect messages. Note: If IPv4 is disabled on the system, this requirement is Not Applicable. Check the value of the "accept_redirects" variables with the following command: $ sudo sysctl net.ipv4.conf.all.accept_redirects net.ipv4.conf.all.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253119`

### Rule: TOSS must ignore IPv6 Internet Control Message Protocol (ICMP) redirect messages.

**Rule ID:** `SV-253119r825029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS ignores IPv6 ICMP redirect messages. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check the value of the "accept_redirects" variables with the following command: $ sudo sysctl net.ipv6.conf.all.accept_redirects net.ipv6.conf.all.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253120`

### Rule: TOSS must not accept router advertisements on all IPv6 interfaces by default.

**Rule ID:** `SV-253120r825032_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network. An illicit router advertisement message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not accept router advertisements on all IPv6 interfaces by default, unless the system is a router. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check to see if router advertisements are not accepted by default by using the following command: $ sudo sysctl net.ipv6.conf.default.accept_ra net.ipv6.conf.default.accept_ra = 0 If the "accept_ra" value is not "0" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253121`

### Rule: TOSS must not accept router advertisements on all IPv6 interfaces.

**Rule ID:** `SV-253121r825035_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network. An illicit router advertisement message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not accept router advertisements on all IPv6 interfaces, unless the system is a router. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check to see if router advertisements are not accepted by using the following command: $ sudo sysctl net.ipv6.conf.all.accept_ra net.ipv6.conf.all.accept_ra = 0 If the "accept_ra" value is not "0" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253122`

### Rule: TOSS must not allow blank or null passwords in the password-auth file.

**Rule ID:** `SV-253122r825038_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that null passwords cannot be used, run the following command: $ sudo grep -i nullok /etc/pam.d/password-auth If output is produced, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253123`

### Rule: TOSS must not allow interfaces to perform Internet Control Message Protocol (ICMP) redirects by default.

**Rule ID:** `SV-253123r825041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology. There are notable differences between Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). There is only a directive to disable sending of IPv4 redirected packets. Refer to RFC4294 for an explanation of "IPv6 Node Requirements", which resulted in this difference between IPv4 and IPv6.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not allow interfaces to perform Internet Protocol version 4 (IPv4) ICMP redirects by default. Note: If IPv4 is disabled on the system, this requirement is Not Applicable. Check the value of the "default send_redirects" variables with the following command: $ sudo sysctl net.ipv4.conf.default.send_redirects net.ipv4.conf.default.send_redirects=0 If the returned line does not have a value of "0", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253124`

### Rule: TOSS must not forward IPv4 source-routed packets by default.

**Rule ID:** `SV-253124r825044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not accept IPv4 source-routed packets by default. Note: If IPv4 is disabled on the system, this requirement is Not Applicable. Check the value of the accept source route variable with the following command: $ sudo sysctl net.ipv4.conf.default.accept_source_route net.ipv4.conf.default.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253125`

### Rule: TOSS must not forward IPv4 source-routed packets.

**Rule ID:** `SV-253125r825047_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not accept IPv4 source-routed packets. Note: If IPv4 is disabled on the system, this requirement is Not Applicable. Check the value of the accept source route variable with the following command: $ sudo sysctl net.ipv4.conf.all.accept_source_route net.ipv4.conf.all.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253126`

### Rule: TOSS must not forward IPv6 source-routed packets by default.

**Rule ID:** `SV-253126r825050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not accept IPv6 source-routed packets by default. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check the value of the accept source route variable with the following command: $ sudo sysctl net.ipv6.conf.default.accept_source_route net.ipv6.conf.default.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253127`

### Rule: TOSS must not forward IPv6 source-routed packets.

**Rule ID:** `SV-253127r825053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not accept IPv6 source-routed packets. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check the value of the accept source route variable with the following command: $ sudo sysctl net.ipv6.conf.all.accept_source_route net.ipv6.conf.all.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253128`

### Rule: TOSS must not respond to Internet Control Message Protocol (ICMP) echoes sent to a broadcast address.

**Rule ID:** `SV-253128r825056_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast ICMP echoes facilitates network mapping and provides a vector for amplification attacks. There are notable differences between Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). IPv6 does not implement the same method of broadcast as IPv4. Instead, IPv6 uses multicast addressing to the all-hosts multicast group. Refer to RFC4294 for an explanation of "IPv6 Node Requirements", which resulted in this difference between IPv4 and IPv6.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not respond to ICMP echoes sent to a broadcast address. Note: If IPv4 is disabled on the system, this requirement is Not Applicable. Check the value of the "icmp_echo_ignore_broadcasts" variable with the following command: $ sudo sysctl net.ipv4.icmp_echo_ignore_broadcasts net.ipv4.icmp_echo_ignore_broadcasts = 1 If the returned line does not have a value of "1", a line is not returned, or the retuned line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253129`

### Rule: TOSS must not send Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-253129r825059_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology. There are notable differences between Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). There is only a directive to disable sending of IPv4 redirected packets. Refer to RFC4294 for an explanation of "IPv6 Node Requirements", which resulted in this difference between IPv4 and IPv6.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS does not IPv4 ICMP redirect messages. Note: If IPv4 is disabled on the system, this requirement is Not Applicable. Check the value of the "all send_redirects" variables with the following command: $ sudo sysctl net.ipv4.conf.all.send_redirects net.ipv4.conf.all.send_redirects = 0 If the returned line does not have a value of "0", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253130`

### Rule: TOSS must prevent IPv4 Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-253130r825062_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS will not accept IPv4 ICMP redirect messages. Note: If IPv4 is disabled on the system, this requirement is Not Applicable. Check the value of the default "accept_redirects" variables with the following command: $ sudo sysctl net.ipv4.conf.default.accept_redirects net.ipv4.conf.default.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253131`

### Rule: TOSS must prevent IPv6 Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-253131r825065_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS will not accept IPv6 ICMP redirect messages. Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Check the value of the default "accept_redirects" variables with the following command: $ sudo sysctl net.ipv6.conf.default.accept_redirects net.ipv6.conf.default.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253132`

### Rule: TOSS must restrict exposed kernel pointer addresses access.

**Rule ID:** `SV-253132r825068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS restricts exposed kernel pointer addresses access with the following commands: $ sudo sysctl kernel.kptr_restrict kernel.kptr_restrict = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253133`

### Rule: TOSS must restrict privilege elevation to authorized personnel.

**Rule ID:** `SV-253133r826066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sudo command allows a user to execute programs with elevated (administrator) privileges. It prompts the user for their password and confirms the request to execute a command by checking a file, called sudoers. If the "sudoers" file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "sudoers" file restricts sudo access to authorized personnel. $ sudo grep -iwr 'ALL[[:blank:]]\+ALL' /etc/sudoers /etc/sudoers.d If the either of the following entries are returned, this is a finding: ALL ALL=(ALL) ALL ALL ALL=(ALL:ALL) ALL

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253134`

### Rule: TOSS must use reverse path filtering on all IPv4 interfaces.

**Rule ID:** `SV-253134r825074_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Enabling reverse path filtering drops packets with source addresses that are not routable. There is not an equivalent filter for IPv6 traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TOSS uses reverse path filtering on all IPv4 interfaces with the following commands: $ sudo sysctl net.ipv4.conf.all.rp_filter net.ipv4.conf.all.rp_filter = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253135`

### Rule: TOSS network interfaces must not be in promiscuous mode.

**Rule ID:** `SV-253135r825077_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network interfaces in promiscuous mode allow for the capture of all network traffic visible to the system. If unauthorized individuals can access these applications, it may allow them to collect information such as logon IDs, passwords, and key exchanges between systems. If the system is being used to perform a network troubleshooting function, the use of these tools must be documented with the Information System Security Officer (ISSO) and restricted to only authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify network interfaces are not in promiscuous mode unless approved by the ISSO and documented. Check for the status with the following command: $ sudo ip link | grep -i promisc If network interfaces are found on the system in promiscuous mode and their use has not been approved by the ISSO and documented, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-253136`

### Rule: TOSS must enable kernel parameters to enforce discretionary access control on symlinks.

**Rule ID:** `SV-253136r825080_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control. By enabling the fs.protected_symlinks kernel parameter, symbolic links are permitted to be followed only when outside a sticky world-writable directory, or when the UID of the link and follower match, or when the directory owner matches the symlink's owner. Disallowing such symlinks helps mitigate vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat(). Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to enable DAC on symlinks with the following commands: Check the status of the fs.protected_symlinks kernel parameter. $ sudo sysctl fs.protected_symlinks fs.protected_symlinks = 1 If "fs.protected_symlinks" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter. $ sudo grep -r fs.protected_symlinks /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:fs.protected_symlinks = 1 If "fs.protected_symlinks" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-253137`

### Rule: TOSS must enable kernel parameters to enforce discretionary access control on hardlinks.

**Rule ID:** `SV-253137r825083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control. By enabling the fs.protected_hardlinks kernel parameter, users can no longer create soft or hard links to files they do not own. Disallowing such hardlinks mitigate vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat(). Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to enable DAC on hardlinks with the following commands: Check the status of the fs.protected_hardlinks kernel parameter. $ sudo sysctl fs.protected_hardlinks fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter. $ sudo grep -r fs.protected_hardlinks /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf /etc/sysctl.d/99-sysctl.conf:fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

