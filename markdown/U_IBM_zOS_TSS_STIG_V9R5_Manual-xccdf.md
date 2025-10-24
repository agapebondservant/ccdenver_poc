# STIG Benchmark: IBM z/OS TSS Security Technical Implementation Guide

---

**Version:** 9

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-223871`

### Rule: All IBM z/OS digital certificates in use must have a valid path to a trusted Certification Authority (CA).

**Rule ID:** `SV-223871r998483_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a CA. A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000403-GPOS-00182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the CA-TSS SAFCRRPT using the following as SYSIN input: RECORDID(-) DETAIL TRUST FIELDS(ISSUER SUBJECT ACTIVE EXPIRE TRUST) If no certificate information is found, this is not a finding. NOTE: Certificates are only valid when their Status is TRUST. Therefore, you may ignore certificates with the NOTRUST status during the following check. If the digital certificate information indicates that the issuer's distinguished name leads to one of the following this is not a finding: a) A DOD PKI Root Certification Authority b) An External Root Certification Authority (ECA) c) An approved External Partner PKI's Root Certification Authority The DOD Cyber Exchange website contains information as to which certificates may be acceptable (https://public.cyber.mil/pki-pke/interoperability/ or https://cyber.mil/pki-pke/interoperability/). Examples of an acceptable DOD CA are: DOD PKI Class 3 Root CA DOD PKI Med Root CA

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-223872`

### Rule: Expired IBM z/OS digital certificates must not be used.

**Rule ID:** `SV-223872r958448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the CA-TSS SAFCRRPT using the following as SYSIN input: RECORDID(-) DETAIL FIELDS(ISSUER SUBJECT ACTIVE EXPIRE TRUST) If no certificate information is found, this is not a finding. NOTE: Certificates are only valid when their Status is TRUST. Therefore, you may ignore certificates with the NOTRUST status during the following checks. Check the expiration for each certificate with a status of TRUST. If the expiration date has passed, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223873`

### Rule: IBM z/OS must have Certificate Name Filtering implemented with appropriate authorization and documentation.

**Rule ID:** `SV-223873r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If certificate name filtering is in use, the ISSM should document each active filter rule and have written approval to use the rule. Issue the following TSS command to list any certificate name filters defined to TSS: TSS LIST(SDT) CERTMAP(ALL) If there is nothing to list, this is not a finding. NOTE: Certificate name filters are only valid when their Status is TRUST. Therefore, you may ignore filters with the NOTRUST status. If certificate name filters are defined and they have a Status of TRUST, certificate name filtering is in use. If certificate name filtering is in use and filtering rules have been documented and approved by the ISSM, this is not a finding. If certificate name filtering is in use and filtering rules have not been documented and approved by the ISSM, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223874`

### Rule: CA-TSS Security control ACIDs must be limited to the administrative authorities authorized and that require these privileges to perform their job duties.

**Rule ID:** `SV-223874r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The use of security policy filters provides protection for the confidentiality of data by restricting the flow of data. A crucial part of any flow control solution is the ability to configure policy filters. This allows the operating system to enforce multiple and different security policies. Policy filters serve to enact and enforce the organizational policy as it pertains to controlling data flow.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) DATA(ADMIN, BASIC) If any ACIDs other than TYPE=CENTRAL (SCA/MSCA) has the following administrative authority, this is a finding. FACILITIES(ALL) PROGRAM(ALL) PROGRAM(OWN) RESOURCE(ALL) ROSRES(ALL) VOLUME(ALL) VOLUME(OWN) MISC1(ALL) MISC1(LCF) MISC1(LTIME) MISC1(RDT) MISC1(USER) MISC2(ALL) MISC2(DLF) MISC2(NDT) MISC2(SMS) MISC4(ALL) MISC8(ALL) MISC8(LISTAPLU) MISC8(LISTRDT) MISC8(LISTSDT) MISC8(LISTSTC) MISC8(MCS) MISC9(ALL) MISC9(BYPASS) MISC9(CONSOLE) MISC9(GLOBAL) MISC9(MASTFAC) MISC9(MODE) MISC9(STC) MISC9(TRACE)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223875`

### Rule: The number of CA-TSS ACIDs possessing the tape Bypass Label Processing (BLP) privilege must be limited.

**Rule ID:** `SV-223875r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of security policy filters provides protection for the confidentiality of data by restricting the flow of data. A crucial part of any flow control solution is the ability to configure policy filters. This allows the operating system to enforce multiple and different security policies. Policy filters serve to enact and enforce the organizational policy as it pertains to controlling data flow.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) DATA(BASIC) If only authorized personnel have BLP access and documentation for access is on file with the ISSO, this is not a finding.

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-223876`

### Rule: CA-TSS MODE Control Option must be set to FAIL.

**Rule ID:** `SV-223876r958362_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other errors. A comprehensive account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service. The automated mechanisms may reside within the operating system itself or may be offered by other infrastructure providing automated account management capabilities. Automated mechanisms may be composed of differing technologies that, when placed together, contain an overall automated mechanism supporting an organization's automated account management requirements. Account management functions include: assigning group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to automatically notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephonic notification to report atypical system account usage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the global MODE Control Option value is set to "FAIL", this is not a finding. If the global MODE Control Option value is not set to "FAIL", this is a finding. Additional analysis may be required under the following conditions: Mode(IMPL) is allowed while a system is in implementation with a documented process that includes an implementation completion date.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-223877`

### Rule: The CA-TSS NPWRTHRESH Control Option must be properly set.

**Rule ID:** `SV-223877r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the NPWRTHRESH Control Option value is not set to NPWRTHRESH(02), this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-223878`

### Rule: The CA-TSS NPPTHRESH Control Option must be properly set.

**Rule ID:** `SV-223878r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the NPPTHRESH Control Option value is not set to NPWRTHRESH(02), this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-223879`

### Rule: The CA-TSS PTHRESH Control Option must be set to 2.

**Rule ID:** `SV-223879r1050764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the PTHRESH Control Option value is not set to PTHRESH(02), this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-223881`

### Rule: IBM z/OS must limit access for SMF collection files (i.e., SYS1.MANx) to appropriate users and/or batch jobs that perform SMF dump processing.

**Rule ID:** `SV-223881r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMF data collection is the system activity journaling facility of the z/OS system. Unauthorized access could result in the compromise of logging and recording of the operating system environment, ESM, and customer data. Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000256-GPOS-00097, CCI-001494, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099, SRG-OS-000080-GPOS-00048, SRG-OS-000206-GPOS-00084, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the SMFPRMxx member in SYS1.PARMLIB. Determine the SMF and/or Logstream data set name. If the following statements are true, this is not a finding. -The ESM data set rules for the SMF data collection files (e.g., SYS1.MAN* or IFASMF.SYS1.*) restrict ALTER access to only z/OS systems programming personnel. -The ESM data set rules for the SMF data collection files (e.g., SYS1.MAN* or IFASMF.SYS1.*) restrict UPDATE access to z/OS systems programming personnel, and/or batch jobs that perform SMF dump processing and others as approved by ISSM. -The ESM data set rules for the SMF data collection files (e.g., SYS1.MAN* or IFASMF.SYS1.*) restrict READ access to auditors and others approved by the ISSM. -The ESM data set rules for SMF data collection files (e.g., SYS1.MAN* or IFASMF.SYS1.*) specify that all (i.e., failures and successes) UPDATE and/or ALTER access are logged.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-223882`

### Rule: IBM z/OS SYS1.PARMLIB must be properly protected.

**Rule ID:** `SV-223882r998484_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Satisfies: SRG-OS-000063-GPOS-00032, SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000362-GPOS-00149, SRG-OS-000337-GPOS-00129, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a data set list of access to SYS1.PARMLIB. If the ESM data set rules for SYS1.PARMLIB allow inappropriate (e.g., global READ) access, this is a finding. If data set rules for SYS1.PARMLIB do not restrict READ, WRITE or greater access to only systems programming personnel, this is a finding. If data set rules for SYS1.PARMLIB do not restrict READ and UPDATE access to only domain level security administrators, this is a finding. If data set rules for SYS1.PARMLIB do not restrict READ access to only system Level Started Tasks, authorized Data Center personnel, and auditors, this is a finding. If data set rules for SYS1.PARMLIB do not specify that all (i.e., failures and successes) WRITE or greater access will be logged, this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-223883`

### Rule: IBM z/OS for PKI-based authentication must use ICSF or the ESM to store keys.

**Rule ID:** `SV-223883r998485_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Any keys or Certificates must be managed in ICSF or the external security manager and not in UNIX files. From the ISPF Command Shell enter: OMVS enter find / -name *.kdb and Find / -name *.jks If any files are present, this is a finding. OMVS enter find / -name *.kdb and Find / -name *.jks If any files are present, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-223885`

### Rule: The CA-TSS NEWPHRASE and PPSCHAR Control Options must be properly set.

**Rule ID:** `SV-223885r998486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000070-GPOS-00038</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the NEWPHRASE Control Option conforms to the following requirements, this is not a finding. MA=1-32 MN=1-32 ID MAX=100 MIN=15-100 MINDAYS=1 NR=0-1 SC=1-32 WARN=1-10 If the PPSCHAR Control Option conform to the allowable list defined in CA Top Secret for z/OS Control Options Guide, this is not a finding. Note: These characters will be specified at a minimum. "40" represents the blank character. Characters can be identified by their character or hex equivalent.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-223886`

### Rule: The CA-TSS NEWPW control options must be properly set.

**Rule ID:** `SV-223886r998487_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is stolen, this will lead to the compromise of the authentication and nonrepudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Satisfies: SRG-OS-000071-GPOS-00039, SRG-OS-000072-GPOS-00040, SRG-OS-000075-GPOS-00043, SRG-OS-000480-GPOS-00225, SRG-OS-000266-GPOS-00101, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the NEWPW Control Option values conform to the following requirements, this is not a finding. NEWPW(MIN=8,WARN=10, MINDAYS=1, NR=0, ID, TS, SC, RS, FA, FN, MC, UC, LC) NOTE: For the Option SC, the PASSCHAR control option should be set to the allowable list defined in CA Top Secret for z/OS Control Options Guide. NOTE: For the Option RS, at a minimum use the reserved word prefix list found in the site security plan.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-223887`

### Rule: IBM z/OS must use NIST FIPS-validated cryptography to protect passwords in the security database.

**Rule ID:** `SV-223887r998488_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000074-GPOS-00042</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF command shell line enter: TSS MODIFY(STATUS) If either of the following is included, this is not a finding. AES_ENCRYPTION(Active,128) AES_ENCRYPTION(Active,256)

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-223888`

### Rule: The CA-TSS PWEXP Control Option must be set to 60.

**Rule ID:** `SV-223888r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the PWEXP Control Option value is not set to PWEXP(60), this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-223889`

### Rule: The CA-TSS PPEXP Control Option must be properly set.

**Rule ID:** `SV-223889r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the PPEXP Control Option will conform to the following requirements, this is not a finding. PPEXP(60)

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-223890`

### Rule: The CA-TSS PWHIST Control Option must be set to 10 or greater.

**Rule ID:** `SV-223890r998491_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the PWHIST Control Option value is not set to PWHIST(10) or greater, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-223891`

### Rule: The CA-TSS PPHIST Control Option must be properly set.

**Rule ID:** `SV-223891r998492_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the PPHIST Control Option conforms to the following requirements, this is not a finding. PPHIST(10-64)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223893`

### Rule: CA-TSS access to SYS1.LINKLIB must be properly protected.

**Rule ID:** `SV-223893r998494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000362-GPOS-00149, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a data set list of access to SYS1.LINKLIB. If the ESM data set rules for SYS1.LINKLIB allow inappropriate (e.g., global READ) access, this is a finding. If data set rules for SYS1.LINKLIB do not restrict READ, WRITE or greater access to only systems programming personnel, this is a finding. If data set rules for SYS1.LINKLIB do not restrict READ and UPDATE access to only domain level security administrators, this is a finding. If data set rules for SYS1.LINKLIB do not restrict READ access to only system Level Started Tasks, authorized Data Center personnel, and auditors, this is a finding. If data set rules for SYS1.LINKLIB do not specify that all (i.e., failures and successes) WRITE or greater access will be logged, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223894`

### Rule: CA-TSS must limit Write or greater access to SYS1.SVCLIB to system programmers only.

**Rule ID:** `SV-223894r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a data set list of access for SYS1.SVCLIB. If all of the following are true, this is not a finding. If any of the following are untrue, this is a finding. ESM data set rules for SYS1.SVCLIB restrict WRITE or greater access to only z/OS systems programming personnel. ESM data set rules for SYS1.SVCLIB specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223895`

### Rule: CA-TSS must limit Write or greater access to SYS1.IMAGELIB to system programmers only.

**Rule ID:** `SV-223895r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a data set list of access for SYS1.IMAGELIB. If the following guidance is true, this is not a finding. The ACP data set rules for SYS1.IMAGELIB do not restrict WRITE or greater access to only systems programming personnel. The ACP data set rules for SYS1.IMAGELIB do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223896`

### Rule: CA-TSS must limit Write or greater access to SYS1.LPALIB to system programmers only.

**Rule ID:** `SV-223896r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a data set list of access for SYS1.LPALIB. If all of the following are untrue, this is a finding. If any of the following is true, this is a finding. The ESM data set rules for SYS1.LPALIB do not restrict WRITE or greater access to only z/OS systems programming personnel. The ESM data set rules for SYS1.LPALIB do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223897`

### Rule: CA-TSS must limit WRITE or greater access to all APF-authorized libraries to system programmers only.

**Rule ID:** `SV-223897r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From Any ISPF input line, enter TSO ISRDDN APF. If all of the following are untrue, this is not a finding. If any of the following are true, this is a finding. The ACP data set rules for APF libraries do not restrict WRITE or greater access to only z/OS systems programming personnel. The ACP data set rules for APF libraries do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223898`

### Rule: IBM z/OS libraries included in the system REXXLIB concatenation must be properly protected.

**Rule ID:** `SV-223898r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to AXRxx member of PARMLIB for each REXXLIB ADD statement. If the ESM data set rules for libraries in the REXXLIB concatenation restrict WRITE or greater access to only z/OS systems programming personnel, this is not a finding. If the ESM data set rules for libraries in the REXXLIB concatenation restrict READ access to the following, this is not a finding. Appropriate Started Tasks Auditors The user-id defined in PARMLIB member AXR00 AXRUSER(user-id) If the ESM data set rules for libraries in the REXXLIB concatenation specify that all (i.e., failures and successes) WRITE or greater access will be logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223899`

### Rule: CA-TSS must limit Write or greater access to all LPA libraries to system programmers only.

**Rule ID:** `SV-223899r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From any ISPF input line, enter TSO ISRDDN LPA. If all of the following are untrue, this is not a finding. If any of the following is true, this is a finding. The ACP data set rules for LPA libraries do not restrict WRITE or greater access to only z/OS systems programming personnel. The ACP data set rules for LPA libraries do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223900`

### Rule: CA-TSS must limit Write or greater access to SYS1.NUCLEUS to system programmers only.

**Rule ID:** `SV-223900r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access for SYS1.NUCLEUS. If all of the following are untrue, there is not a finding. If any of the following is true, this is a finding. The ACP data set rules for SYS1.NUCLEUS do not restrict WRITE or greater access to only z/OS systems programming personnel. The ACP data set rules for SYS1.NUCLEUS do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223901`

### Rule: CA-TSS must limit Write or greater access to libraries that contain PPT modules to system programmers only.

**Rule ID:** `SV-223901r958472_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review program entries in the IBM Program Properties Table (PPT). You may use a third-party product to examine these entries however, to determine program entries issue the following command from an ISPF command line: TSO ISRDDN LOAD IEFSDPPT Press Enter. For each module identified in the "eyecatcher" if all of the following are untrue, this is not a finding. If any of the following is true, this is a finding. The ACP data set rules for libraries that contain PPT modules do not restrict WRITE or greater access to only z/OS systems programming personnel. The ACP data set rules for libraries that contain PPT modules do not specify that all WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223902`

### Rule: CA-TSS must limit WRITE or greater access to LINKLIST libraries to system programmers only.

**Rule ID:** `SV-223902r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From any ISPF input line, enter TSO ISRDDN LINKLIST. If all of the following are untrue, this is not a finding. If any of the following is true, this is a finding. The ACP data set rules for LINKLIST libraries do not restrict WRITE or greater access to only z/OS systems programming personnel. The ACP data set rules for LINKLIST libraries do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223903`

### Rule: CA-TSS security data sets and/or databases must be properly protected.

**Rule ID:** `SV-223903r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000134-GPOS-00068, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine all associated ESM security data sets and/or databases. If the following accesses to the ESM security data sets and/or databases are properly restricted as detailed below, this is not a finding. The ESM data set rules for ESM security data sets and/or databases restrict READ access to auditors and DASD batch. The ESM data set rules for ESM security data sets and/or databases restrict READ and/or greater access to z/OS systems programming personnel, security personnel, and/or batch jobs that perform ESM maintenance. All (i.e., failures and successes) data set access authorities (i.e., READ, UPDATE, ALTER, and CONTROL) for ESM security data sets and/or databases are logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223904`

### Rule: CA-TSS must limit access to the System Master Catalog to appropriate authorized users.

**Rule ID:** `SV-223904r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to SYSCATxx member of SYS1.NUCLEUS. Multiple SYSCATxx members may be defined; if so, refer to Master Catalog message for IPL. If the member is not found, refer to the appropriate LOADxx member of SYS1.PARMLIB. If data set rules for the Master Catalog do not restrict greater than "READ" access to only z/OS systems programming personnel, this is a finding. If products or procedures requiring system programmer access for system-level maintenance meet the following specific case, this is not a finding: - The batch job or procedure must be documented in the SITE Security Plan. - Reside in a data set that is restricted to systems programmers' access only. If data set rules for the Master Catalog do not specify that all (i.e., failures and successes) greater than "READ" access will be logged, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223905`

### Rule: CA-TSS allocate access to system user catalogs must be limited to system programmers only.

**Rule ID:** `SV-223905r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: LISTCat USERCATALOG ALL NOPREFIX Review the ESM data set rules for each usercatalog defined. If the data set rules for User Catalogs do not restrict ALTER access to only z/OS systems programming personnel, this is a finding. If products or procedures requiring system programmer access for system-level maintenance meet the following specific case, this is not a finding: - The batch job or procedure must be documented in the SITE Security Plan. - Reside in a data set that is restricted to systems programmers' access only. If the data set rules for User Catalogs do not specify that all (i.e., failures and successes) ALTER access will be logged, this a finding. Note: If the USER CATALOGS contain SMS managed data sets, READ access is sufficient to allow user operations. If the USER CATALOGS do not contain SMS managed data sets, UPDATE access is required for user operation.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223906`

### Rule: CA-TSS must limit WRITE or greater access to all system-level product installation libraries to system programmers only.

**Rule ID:** `SV-223906r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the systems programmer for z/OS supply the following information: The data set name and associated SREL for each SMP/E CSI utilized to maintain this system. The data set name of all SMP/E TLIBs and DLIBs used for installation and production support. A comprehensive list of the SMP/E DDDEFs for all CSIs may be used if valid. The ACP data set rules for system-level product installation libraries (e.g., SMP/E CSIs) allow inappropriate access. The ACP data set rules for system-level product installation libraries (e.g., SMP/E CSIs) do not restrict WRITE or greater access to only z/OS systems programming personnel. If all of the above are untrue, this is not a finding. If any of the above is true, or if these data sets cannot be identified due to a lack of requested information, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223907`

### Rule: CA-TSS must limit WRITE or greater access to the JES2 System data sets (e.g., Spool, Checkpoint, and Initialization parameters) to system programmers only.

**Rule ID:** `SV-223907r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The ESM data set rules for the JES2 System data sets (e.g., Spool, Checkpoint, and Initialization parameters) do not restrict WRITE or greater access to only z/OS systems programming personnel. The ESM data set rules for the JES2 System data sets (e.g., Spool, Checkpoint, and Initialization parameters) allow inappropriate access not documented and approved by ISSO. If both of the above are untrue, this is not a finding. If either of the above is true, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223908`

### Rule: CA-TSS must limit Write or greater access to SYS1.UADS to system programmers only, and Read and Update access must be limited to system programmer personnel and/or security personnel.

**Rule ID:** `SV-223908r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The ESM data set rules for SYS1.UADS restricts WRITE or Greater access to only z/OS systems programming personnel. The ESM data set rules for SYS1.UADS restricts READ and/or UPDATE access to z/OS systems programming personnel and/or security personnel. The ESM data set rules for SYS1.UADS specifies that all (i.e., failures and successes) data set access authorities (i.e., READ, UPDATE, ALTER, and CONTROL) will be logged. The ESM data set rules for SYS1.UADS restricts READ access to auditors as documented in Security Plan. If all of the above are untrue, this is not a finding. If any of the above is true, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223909`

### Rule: CA-TSS must limit access to data sets used to back up and/or dump SMF collection files to appropriate users and/or batch jobs that perform SMF dump processing.

**Rule ID:** `SV-223909r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000206-GPOS-00084, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the procedures and collection specifics for SMF data sets and backup. If the ESM data set rules for the SMF dump/backup files do not restrict WRITE or greater access to authorized DISA and site personnel (e.g., systems programmers and batch jobs that perform SMF processing), this is a finding. If the ESM data set rules for the SMF dump/backup files do restrict update access as documented in the site security plan, this is a finding. If the ESM data set rules for the SMF dump/backup files do not restrict READ access to auditors and others approved by the ISSM, this is a finding. If the ESM data set rules for SMF dump/backup files do not specify that all (i.e., failures and successes) WRITE or greater access will be logged, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223910`

### Rule: CA-TSS must limit access to SYSTEM DUMP data sets to system programmers only.

**Rule ID:** `SV-223910r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System DUMP data sets are used to record system data areas and virtual storage associated with system task failures. Unauthorized access could result in the compromise of the operating system environment, ACP, and customer data. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to data sets SYS1.DUMPxx, additionally, Dump data sets can be identified by reviewing the logical parmlib concatenation data sets for the current COMMNDxx member. Find the COM= which specifies the DUMPDS NAME (DD NAME=name-pattern) entry. The name-pattern is used to identify additional Dump data sets. If the ESM data set rules for System Dump data sets do not restrict READ, UPDATE, and/or ALTER access to only systems programming personnel, this is a finding. If the ESM data set rules for all System Dump data sets do not restrict READ access to personnel having justification to review these dump data sets, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223911`

### Rule: CA-TSS WRITE or Greater access to System backup files must be limited to system programmers and/or batch jobs that perform DASD backups.

**Rule ID:** `SV-223911r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Collect from the storage management group the identification of the DASD backup files and all associated storage management ACIDs. If ESM data set rules for system DASD backup files do not restrict WRITE or greater access to z/OS systems programming and/or batch jobs that perform DASD backups this is a finding. If READ Access to system backup data sets is not limited to auditors and others approved by the ISSM this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223912`

### Rule: CA-TSS must limit access to SYS(x).TRACE to system programmers only.

**Rule ID:** `SV-223912r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access for SYS(x).TRACE files. If the ESM data set rule for SYS1.TRACE restricts access to systems programming personnel and started tasks that perform GTF processing, this is not a finding. If the ESM data set rule for SYS1.TRACE restricts access to others as documented and approved by ISSM, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223913`

### Rule: CA-TSS must limit access to System page data sets (i.e., PLPA, COMMON, and LOCALx) to system programmers only.

**Rule ID:** `SV-223913r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access for System page data sets (i.e., PLPA, COMMON, and LOCALx). If ESM data set rules for system page data sets (PLPA, COMMON, and LOCAL) restrict access to only systems programming personnel, this is not a finding. If ESM data set rules for system page data sets (PLPA, COMMON, and LOCAL) restrict auditors to READ only, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223914`

### Rule: CA-TSS must limit WRITE or greater access to libraries containing EXIT modules to system programmers only.

**Rule ID:** `SV-223914r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the system for active exit modules. You may need the system administrator's help for this. There are third-party software products that can determine standard and dynamic exits loaded in the system. If all the exits are found within APF, LPA, and LINKLIST, this is not applicable. If ESM data set rules for libraries that contain system exit modules restrict WRITE or greater access to only z/OS systems programming personnel, this is not a finding. If the ESM data set rules for libraries that contain exit modules specify that all WRITE or greater access will be logged, this is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223915`

### Rule: CA-TSS must limit all system PROCLIB data sets to system programmers only and appropriate authorized users.

**Rule ID:** `SV-223915r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000324-GPOS-00125, SRG-OS-000080-GPOS-00048</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the following for the PROCLIB data sets that contain the STCs and TSO logons from the following sources: -MSTJCLxx member used during an IPL. The PROCLIB data sets are obtained from the IEFPDSI and IEFJOBS DD statements. -PROCxx DD statements and JES2 Dynamic PROCLIBs. Where 'xx' is the PROCLIB entries for the STC and TSU JOBCLASS configuration definitions. Verify that the accesses to the above PROCLIB data sets are properly restricted. If the following guidance is true, this is not a finding. If the ESM data set access authorizations restrict READ access to all authorized users, this is not a finding. If the ESM data set access authorizations restrict WRITE and/or greater access to systems programming personnel, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223916`

### Rule: CA-TSS must protect memory and privileged program dumps in accordance with proper security requirements.

**Rule ID:** `SV-223916r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IEAABD. resource and/or generic equivalent is defined with no access and all access logged, this is not a finding. If the IEAABD.DMPAUTH. resource and/or generic equivalent is defined with READ access limited to authorized users, this is not a finding. If the IEAABD.DMPAUTH. resource and/or generic equivalent UPDATE or greater access is restricted to only systems personnel and all access is logged, this is not a finding. If the IEAABD.DMPAKEY resource and/or generic equivalent is defined and all access is restricted to systems personnel and that all access is logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223917`

### Rule: IBM z/OS must protect dynamic lists in accordance with proper security requirements.

**Rule ID:** `SV-223917r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the CSV-prefixed resources defined below: CSVAPF. CSVAPF.MVS.SETPROG.FORMAT.DYNAMIC CSVAPF.MVS.SETPROG.FORMAT.STATIC CSVDYLPA. CSVDYNEX. CSVDYNEX.LIST CSVDYNL. CSVDYNL.UPDATE.LNKLST CSVLLA. If the TSS IBMFAC resource class in the RDT has the DEFPROT attribute specified and/or the CSV resources and/or generic equivalent are owned this is not a finding. If the TSS resources and/or generic equivalent identified above are defined with ACTION(AUDIT) and UPDATE access restricted to system programming personnel this is not a finding. If the TSS CSVDYNEX.LIST resource and/or generic equivalent is defined with ACTION(AUDIT) and UPDATE access restricted to system programming personnel this is a finding. If the TSS CSVDYNEX.LIST resource and/or generic equivalent are defined with READ access restricted to auditors this is not a finding. If the products CICS and/or CONTROL-O are on the system, and the TSS access to the CSVLLA resource access to the CSVLLA resource and/or generic equivalent are defined with ACTION(AUDIT) and UPDATE access restricted to the CICS and CONTROL-O STC ACIDs this is not a finding. If any software product requires access to dynamic LPA updates on the system, the TSS access to the CSVDYLPA resource and/or generic equivalent will be defined with ACTION(AUDIT) and UPDATE only after the product has been validated with the appropriate STIG or SRG for compliance AND receives documented and filed authorization that details the need and any accepted risks from the site ISSM or equivalent security authority. Note: In the above, UPDATE access can be substituted with ALL or CONTROL. Review the permissions in the TSS documentation when specifying UPDATE.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223918`

### Rule: IBM z/OS system commands must be properly protected.

**Rule ID:** `SV-223918r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a command screen enter: TSS WHOHAS OPERCMDS(MVS) If any of below is untrue for any z/OS system command resource, this is a finding. Access to MVS resource of the OPERCMDS class is restricted to a limited number of authorized users, and all access logged. Access to "MVS.**" is not allowed. Access to z/OS system commands as defined in the table entitled MVS commands, RACF access authorities, and resource names, in the IBM z/OS MVS System Commands manual, is restricted to the appropriate personnel (e.g., operations staff, systems programming personnel, general users). NOTE: Use the GROUP category specified in the table referenced above as a guideline to determine appropriate personnel access to system commands. NOTE: The (MVS.SEND) Command will not be a finding if used by all. Access to specific z/OS system commands is logged as indicated in the table entitled MVS commands, RACF access authorities, and resource names, in the IBM z/OS MVS System Commands manual.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223919`

### Rule: IBM z/OS MCS consoles access authorization(s) for CONSOLE resource(s) must be properly protected.

**Rule ID:** `SV-223919r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS SYSCONS(*) For each Console defined enter: TSS WHOHAS SYSCONS(<console>) If the ACID associated with each console has READ access to the corresponding resource defined in the SYSCONS resource class, this is not a finding. If access authorization for SYSCONS resources restricts access to operations, the Master SCA, system programming personnel, or authorized personnel, this is not a finding. If the console defined is not defined to the TSS SYSCONS resource class enter: TSS LIST (RDT) RESCLASS(SYSCONS) If the SYSCONS resource class does not have the DEPROT attribute, this is a finding. For each Console defined enter: TSS WHOHAS(<CONSOLE>) If the console defined is not defined to the TSS SYSCONS resource class enter: TSS LIST (RDT) RESCLASS(SYSCONS) If the SYSCONS resource class does not have the DEPROT attribute, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223920`

### Rule: CA-TSS must properly define users that have access to the CONSOLE resource in the TSOAUTH resource class.

**Rule ID:** `SV-223920r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
TSS WHOOWNS TSOAUTH(*) If the Console is not defined to TSOAuth RESOURCE CLASS this is Not Applicable. Refer to the CONSOLxx member of SYS1.PARMLIB. For each Console defined if the following is true, this is not a finding. -User ACIDs are restricted to the INFO level in the MCSAUTH attribute. -User ACIDs are restricted to READ access to the MVS.MCSOPER.acid resource defined in the OPERCMDS resource class. -User ACIDs and/or profile ACIDs are restricted to the CONSOLE resource defined in the TSOAUTH resource class. If any of the above are untrue, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223921`

### Rule: IBM z/OS Operating system commands (MVS.) of the OPERCMDS resource class must be properly owned.

**Rule ID:** `SV-223921r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS OPERCMDS(MVS) If the (MVS) resource is owned, this is not a finding. If the (MVS) resource is not owned, this is a finding. TSS LIST RDT RESCLASS(OPERCMDS) If the (MVS) resource is not OWNED and the OPERCMDS class does not have DEFPROT as an attribute, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223922`

### Rule: CA-TSS AUTH Control Option values specified must be set to (OVERRIDE,ALLOVER) or (MERGE,ALLOVER).

**Rule ID:** `SV-223922r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
TSS MODIFY STATUS If the AUTH Control Option values are not set to AUTH(OVERRIDE, ALLOVER) or AUTH(MERGE, ALLOVER), this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223923`

### Rule: Access to the CA-TSS MODE resource class must be appropriate.

**Rule ID:** `SV-223923r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOHAS MODE(*) If any ACIDs is permitted a mode of "DORM", "WARN", or "IMPL", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223924`

### Rule: Data set masking characters must be properly defined to the CA-TSS security database.

**Rule ID:** `SV-223924r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS data set(*) If data set masking characters. (*, %, and +, **) are owned by the MSCA, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223925`

### Rule: CA-TSS Emergency ACIDs must be properly limited and must audit all resource access.

**Rule ID:** `SV-223925r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the SYS1.UADS. Ask the System Administrator for list of all emergency ACIDs available to the site along with the associated function of each. If there are no emergency ACIDs defined ask the system administrator for an alternate documented procedure to handle emergencies. If there are no emergency ACIDs and no documented emergency procedure, this is a finding. If at a minimum, an emergency ACID exists with the security administration attributes specified in accordance with the following requirements, this is not a finding. For emergency IDs with security administration privileges, but which cannot access and update system data sets: ADMIN Authority: ACID(ALL) DATA(ALL) OTRAN(ALL) MISC1(INSTDATA,SUSPEND,TSSSIM,NOATS) MISC2(TSO,TARGET) MISC8(PWMAINT,REMASUSP) MISC9(GENERIC) FACILITY(BATCH, TSO, ROSCOE, CICS, xxxx) Where 'xxxx' is a facility the application security team grants access into for their application users. An additional class of userids can exist to perform all operating system functions except ESM administration. These emergency ACID(s) will have ability to access and update all system data sets but will not have security administration privileges. See the following requirements: Data set permissions for the emergency ACIDs will be permitted as follows: TSS PER(acid) DSN(*****) ACCESS(ALL) ACTION(AUDIT) Security Bypass Attributes NODSNCHK, NOVOLCHK, and NORESCHK will not be given to the Emergency ACIDs. All emergency ACID(s) are to be implemented with logging to provide an audit trail of their activities. All emergency ACID(s) are to be maintained in both the ESM and SYS1.UADS to ensure they are available in the event that the ESM is not functional. All emergency ACID(s) will have distinct, different passwords in SYS1.UADS and in the ACP, and the site is to establish procedures to ensure that the passwords differ. The password for any ID in SYS1.UADS is never to match the password for the same ID in the ACP. All emergency ACID(s) will have documented procedures to provide a mechanism for the use of the IDs. Their release for use is to be logged, and the log is to be maintained by the ISSO. When an emergency ACID is released for use, its password is to be reset by the ISSO within 12 hours. 1) Review the access authorizations for all emergency ACIDs to ensure that all access permitted to these ACIDs is reviewed and approved by the ISSO. 2) If emergency ACIDs are utilized, ensure they are restricted to performing only the operating system recovery functions or the ESM administration functions. If these emergency ACID(s) have ability to ACCESS and UPDATE all system data sets, but do not have security administration privileges, this is not a finding. Note: If running Quest NC-Pass, validate that the Emergency ACIDS are identified to have the FACILITY of NCPASS and SECURID resource in the ABSTRACT resource class.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223926`

### Rule: CA-TSS ACIDs must not have access to FAC(*ALL*).

**Rule ID:** `SV-223926r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) DATA(BASIC) If any ACID(s) is (are) assigned FACILITY(*ALL*), this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223927`

### Rule: The CA-TSS ALL record must have appropriate access to Facility Matrix Tables.

**Rule ID:** `SV-223927r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ALL record for the assignment of FACILITY. If CA-Top Secret facilities are granted via the ALL record, with the exception of DFHSM/HSM, this is a finding. The DFHSM/HSM FACILITY can be determined by reviewing FACLIST for the FACILITY that contains INITPGM=ARC.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223928`

### Rule: Data set masking characters allowing access to all data sets must be properly restricted in the CA-TSS security database.

**Rule ID:** `SV-223928r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer the accesses to the TSS masking character (*, *., and/or **) for data sets. If the following guidance is true, this is not a finding. If the TSS data set access authorizations restrict READ access to auditors, this is not a finding. If the TSS data set access authorizations restrict READ and/or greater access to DASD administrators, Trusted Started Tasks, emergency users, and DASD batch users, this is not a finding. If CA VTAPE is installed on the systems and the TSS data set access authorizations restrict READ access to CA VTAPE STCs and/or batch users, this is not a finding. If the TSS data set access authorizations specify that all (i.e., failures and successes) EXECUTE and/or greater accesses are logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223929`

### Rule: IBM z/OS DASD Volume access greater than CREATE found in the CA-TSS database must be limited to authorized information technology personnel requiring access to perform their job duties.

**Rule ID:** `SV-223929r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS VOLUME(*) For each volume identified issue WHOHAS (<volume id>) If access authorizations greater than CREATE (e.g., CONTROL or ALL) granted for DASD volumes are within the requirements in the site security plan, this is not a finding. If access authorization for volumes exceeds the requirements without justification, this is a finding. NOTE: Domain-level DASD Administrators who are responsible for the Domain level DASD/storage administration. Volume level access to those team members who are directly responsible and perform Domain level DASD/Storage administration may be granted access to all volumes via PRIVPGM controls.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223930`

### Rule: IBM z/OS Sensitive Utility Controls must be properly defined and protected.

**Rule ID:** `SV-223930r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the table of Sensitive Utilities resources and/or generic equivalent as detail in the table below. If the TSS resource access authorizations for the following sensitive utilities restrict access to the appropriate personnel, this is not a finding. Sensitive Utility Controls Program Product Function AHLGTF z/OS System Activity Tracing HHLGTF IHLGTF ICPIOCP z/OS System Configuration IOPIOCP IXPIOCP IYPIOCP IZPIOCP BLSROPTR z/OS Data Management DEBE OS/DEBE Data Management DITTO OS/DITTO Data Management FDRZAPOP FDR Product Internal Modification GIMSMP SMP/E Change Management Product ICKDSF z/OS DASD Management IDCSC01 z/OS IDCAMS Set Cache Module IEHINITT z/OS Tape Management IFASMFDP z/OS SMF Data Dump Utility IND$FILE z/OS PC to Mainframe File Transfer (Applicable only for classified systems) CSQJU003 IBM WebSphereMQ CSQJU004 CSQUCVX CSQ1LOGP CSQUTIL WHOIS z/OS Share MOD to identify user name from USERID. Restricted to data center personnel only. If the TSS resources are owned or DEFPROT is specified for the resource class, this is not a finding. If the TSS resource logging is correctly specified, this is not a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-223931`

### Rule: IBM z/OS Started tasks must be properly defined to CA-TSS.

**Rule ID:** `SV-223931r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Started procedures have system generated job statements that do not contain the user, group, or password statements. To enable the started procedure to access the same protected resources that users and groups access, started procedures must have an associated USERID. If a USERID is not associated with the started procedure, the started procedure will not have access to the resources. To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the site security plan, the system administrator, and system libraries to determine list of stated tasks available on the system. If the following guidance is true, this is not a finding. -All started tasks are assigned a unique user ACID or STC ACIDs that will be unique per product and function if supported by vendor documentation. -Every ACID with the STC Facility has a corresponding entry defined in the STC record. -Every ACID defined in the STC record has a corresponding user ACID defined to TSS with the STC Facility. -All STC ACIDs will have a password generated in accordance with STIG requirements. -All STC ACIDs will be sourced to the internal reader (e.g., ADD(stc-acid) SOURCE(INTRDR). -The STC ACIDs may have the NOSUSPEND attribute.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223932`

### Rule: The CA-TSS CANCEL Control Option must not be specified.

**Rule ID:** `SV-223932r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections. The CANCEL Control Option allows security administrators to use the O/S CANCEL command to bring the TSS address space down.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command enter: TSS MODIFY STATUS If the CANCEL Control Option is not specified, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223933`

### Rule: The CA-TSS HPBPW Control Option must be set to three days maximum.

**Rule ID:** `SV-223933r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command enter: TSS MODIFY STATUS If the HPBPW Control Option value is set to (3) days maximum, this is not a finding. If the HPBPW Control Option value is set to greater than (3) days, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223934`

### Rule: The CA-TSS INSTDATA Control Option must be set to 0.

**Rule ID:** `SV-223934r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command enter: TSS MODIFY STATUS If the INSTDATA Control Option is set to NONE this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223935`

### Rule: The CA-TSS OPTIONS Control Option must include option 4 at a minimum.

**Rule ID:** `SV-223935r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the OPTIONS Control Option contains at a minimum option number (4), this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223936`

### Rule: CA-TSS TEMPDS Control Option must be set to YES.

**Rule ID:** `SV-223936r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the TEMPDS Control Option value is set to TEMPDS(YES), this not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223937`

### Rule: The number of CA-TSS control ACIDs must be justified and properly assigned.

**Rule ID:** `SV-223937r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) TYPE(SCA) DATA(BASIC) If the persons listed agree with the site security plan, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223938`

### Rule: The number of CA-TSS ACIDs with MISC9 authority must be justified.

**Rule ID:** `SV-223938r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) DATA(ADMIN) If the ACIDs having MISC9(ALL) or MISC9(CONSOLE) authority are designated SCAs who are responsible for the security for the domain this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223939`

### Rule: The CA-TSS LUUPDONCE Control Option value specified must be set to NO.

**Rule ID:** `SV-223939r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the LUUPDONCE Control Option value is set to "YES", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223940`

### Rule: The CA-TSS Automatic Data Set Protection (ADSP) Control Option must be set to NO.

**Rule ID:** `SV-223940r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the ADSP Control Option value is not set to "ADSP(NO)", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223941`

### Rule: CA-TSS RECOVER Control Option must be set to ON.

**Rule ID:** `SV-223941r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the RECOVER Control Option value is not set to "RECOVER(ON)", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-223942`

### Rule: IBM z/OS must properly configure CONSOLxx members.

**Rule ID:** `SV-223942r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review each CONSOLxx parmlib member. If the following guidance is true, this is not a finding. The "DEFAULT" statement for each CONSOLxx member specifies "LOGON(REQUIRED)" or "LOGON(AUTO)". The "CONSOLE" statement for each console assigns a unique name using the "NAME" parameter. The "CONSOLE" statement for each console specifies "AUTH(INFO)". Exceptions are the "AUTH" parameter is not valid for consoles defined with "UNIT(PRT)" and specifying "AUTH(MASTER)" is permissible for the system console. Note: The site should be able to determine the system consoles. However, it is imperative that the site adhere to the "DEFAULT" statement requirement.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-223943`

### Rule: IBM z/OS must properly protect MCS console userid(s).

**Rule ID:** `SV-223943r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 to determine correct CONSOLxx member. Examine the CONSOLxx member. If the following guidance is true, this is not a finding. Each console defined in the currently active CONSOLxx parmlib member in EXAM.RPT(PARMLIB) is associated with a valid TSS ACID. Each console ACID has no special privileges and/or attributes (e.g., BYPASSING, CONSOLE, etc.; excluding VTAM SMCS consoles). Each console ACID has no accesses to interactive on-line facilities (e.g., TSO, CICS, etc.; excluding VTAM SMCS consoles). Each console can have the Facility of CONSOLE. Each console ACID will be restricted from accessing all data sets and resources except MVS.MCSOPER.consolename in the OPERCMDS resource class and consolename in the CONSOLE resource class. NOTE: If LOGON(AUTO) is specified in the currently active CONSOLxx parmlib member, additional access may be required. Permissions for the console ACIDs and/or console profile may be given with access READ to MVS.CONTROL, MVS.DISPLAY, MVS.MONITOR, and MVS.STOPMN OPERCMDS resource.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223944`

### Rule: The CA-TSS CPFRCVUND Control Option value specified must be set to NO.

**Rule ID:** `SV-223944r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the "CPFRCVUND" Control Option value is set to "YES", this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223945`

### Rule: The CA-TSS CPFTARGET Control Option value specified must be set to LOCAL.

**Rule ID:** `SV-223945r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the CPFTARGET Control Option value specified is not set to "LOCAL", this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223946`

### Rule: CA-TSS User ACIDs and Control ACIDs must have the NAME field completed.

**Rule ID:** `SV-223946r958482_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST (ACIDs) DATA (BASIC) If any ACID does not have the "NAME" field completed, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223947`

### Rule: The CA-TSS PASSWORD(NOPW) option must not be specified for any ACID type.

**Rule ID:** `SV-223947r958482_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) DATA(PASSWORD) - NOTE: To evaluate the PASSWORD option NOPW, it must be run under the MSCA's authority, if not the information will not be generated. If PASSWORD(NOPW) is specified for any ACID types (USER, DCA, VCA, ZCA, LSCA, SCA, and MSCA), this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223948`

### Rule: Interactive ACIDs defined to CA-TSS must have the required fields completed.

**Rule ID:** `SV-223948r958482_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST (ACIDs) DATA (BASIC,TSO,CICS) If all the fields and information listed below, are not present for all interactive users this is a finding. FIELD DESCRIPTION VALUE FACILITY Validated facilities to use BATCH, TSO, NCPASS, or other interactive Facility PASSWORD logon password must have a value INSTDATA Installation data optional PROFILE Profile(s) optional TSOLPROC Default TSO logon PROC optional for TSO users TSOLACCT Default TSO logon account may be required for a fee for service.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223950`

### Rule: CA-TSS Batch ACID(s) submitted through RJE and NJE must be sourced.

**Rule ID:** `SV-223950r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to data obtained from the site installation identifying batch type ACIDs. If all static batch ACIDs (ACIDs whose passwords never change) originating from a physical reader, RJE, or NJE are sourced to those readers such as (INTRDR, N12.IR, etc.) with the appropriate source Syntax, this is not a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223951`

### Rule: IBM z/OS DASD management ACIDs must be properly defined to CA-TSS.

**Rule ID:** `SV-223951r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to data obtained from the site installation identifying DASD maintenance ACIDs. If each DASD Maintenance ACID has batch Facility, this is not a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-223952`

### Rule: CA-TSS user accounts must uniquely identify system users.

**Rule ID:** `SV-223952r998495_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the UNIX OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the UNIX and Windows operating systems offer a "switch user" capability allowing users to authenticate with their individual credentials and, when needed, "switch" to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge. Satisfies: SRG-OS-000109-GPOS-00056, SRG-OS-000121-GPOS-00062, SRG-OS-000125-GPOS-00065</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of all userids that are shared among multiple users (i.e., not uniquely identified system users). If there are no shared userids on this domain, this is not a finding. If there are shared userids on this domain, this is a finding. NOTE: Userid

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-223953`

### Rule: CA-TSS security administrator must develop a process to suspend userids found inactive for more than 35 days.

**Rule ID:** `SV-223953r998496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) If every user shows a LAST-USED=yy.ddd within the past "35" days, this is not a finding. NOTE: VALID FOR INTERACTIVE USERIDS, NOT VALID FOR STARTED TASK USERIDS AND BATCH USERIDS.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-223954`

### Rule: The CA-TSS INACTIVE Control Option must be properly set.

**Rule ID:** `SV-223954r998497_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the INACTIVE Control Option is set to a value of "0", this is not a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-223955`

### Rule: The CA-TSS AUTOERASE Control Option must be set to ALL for all systems.

**Rule ID:** `SV-223955r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the AUTOERASE Control Option value is set to (ALL), this is not a finding.

## Group: SRG-OS-000184-GPOS-00078

**Group ID:** `V-223956`

### Rule: CA-TSS DOWN Control Option values must be properly specified.

**Rule ID:** `SV-223956r958550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known safe state helps prevent systems from failing to a state that may cause loss of data or unauthorized access to system resources. Operating systems that fail suddenly and with no incorporated failure state planning may leave the system available but with a reduced security protection capability. Preserving operating system state information also facilitates system restart and return to the operational mode of the organization with less disruption to mission-essential processes. Abort refers to stopping a program or function before it has finished naturally. The term abort refers to both requested and unexpected terminations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If only systems personnel are defined in SYS1.UADS and the DOWN Control Option values are set to DOWN(BW,SB,TN,OW), this is not a finding. If non-systems personnel are defined in SYS1.UADS and the DOWN Control Option values are set to DOWN(BW,SB,TW,OW), this is not a finding.

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-223957`

### Rule: The CA-TSS Facility Control Option must specify the sub option of MODE=FAIL.

**Rule ID:** `SV-223957r958808_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Utilizing a whitelist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. Verification of white-listed software occurs prior to execution or at system startup. This requirement applies to operating system programs, functions, and services designed to manage system processes and configurations (e.g., group policies).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY(FACILITY(ALL)) If the Facility Control Option does not specifies the sub option of "MODE=FAIL" for all facilities, this is a finding.

## Group: SRG-OS-000380-GPOS-00165

**Group ID:** `V-223958`

### Rule: CA-TSS ACID creation must use the EXP option.

**Rule ID:** `SV-223958r998498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without providing this capability, an account may be created without a password. Nonrepudiation cannot be guaranteed once an account is created if a user is not forced to change the temporary password upon initial logon. Temporary passwords are typically used to allow access when new accounts are created or passwords are changed. It is common practice for administrators to create temporary passwords for user accounts which allow the users to log on, yet force them to change the password once they have successfully authenticated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator (SA) for the procedures for creating new ACIDs. If the procedure contains the "EXP" option, this is not a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-223959`

### Rule: The CA-TSS SUBACID Control Option must be set to U,8.

**Rule ID:** `SV-223959r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From this ISPF Command Shell enter: TSS MODIFY STATUS If the SUBACID Control Option values are NOT set to "SUBACID(U,8)", this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-223960`

### Rule: CA-TSS must use propagation control to eliminate ACID inheritance.

**Rule ID:** `SV-223960r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY FACILITY(ALL) enter TSS MODIFY FACILITY(<FACILITY>) If no Facility is defined with both the "MULTIUSER" and "ASUBM" attributes further analysis is not needed. For each Facility with "MULTIUSER" and "ASUBM" attribute, review the @ACIDS report to determine which ACID(s) has (have) the following: -A Master Facility of the Facility with "MULTIUSER" and "ASUBM" attribute, and, -The Facility of "BATCH" If each ACID that has the Master Facility of the Facility with "MULTIUSER" and "ASUBM" attribute and the Facility of "BATCH" is defined to the "PROPCNTL" resource class, this is not a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-223961`

### Rule: IBM z/OS scheduled production batch ACIDs must specify the CA-TSS BATCH Facility, and the Batch Job Scheduler must be authorized to the Scheduled production CA-TSS batch ACID.

**Rule ID:** `SV-223961r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the documentation of the processes used for submission of batch jobs via an automated process (i.e., scheduler or other sources) and each of the associated userids. Ensure that each identified batch ACID is sourced to a specific submission process used only for batch processing. If the following guidance is true, this is not a finding. -The job scheduler is cross-authorized to the batch ACIDs. -The Facility of BATCH is specified for each batch ACID. -Batch ACIDs with facilities other than BATCH should be questioned to ensure they are truly used for batch processing only, especially if a non-expiring password is used. -The batch ACIDS may have the NOSUSPEND attribute.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-223962`

### Rule: CA-TSS ADMINBY Control Option must be set to ADMINBY.

**Rule ID:** `SV-223962r958732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From ISPF Command Shell enter: TSS MODIFY STATUS If the ADMINBY Control Option value is not set or set to "NOADMBY", this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-223963`

### Rule: CA-TSS LOG Control Option must be set to (SMF,INIT, SEC9, MSG).

**Rule ID:** `SV-223963r958732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the LOG Control Option is NOT set to (SMF,INIT, SEC9, MSG), this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-223964`

### Rule: CA-TSS MSCA ACID password changes must be documented in the change log.

**Rule ID:** `SV-223964r958732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From ISPF Command Shell enter: Exec the CA-TSS TSSAUDIT Utility using CHANGES Control Statement. Note: If running Quest NC-Pass, validate that the MSCA ACID has the FACILITY of NCPASS and SECURID resource in the ABSTRACT resource class. If the MSCA password changes are documented in the change log, this is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223965`

### Rule: The IBM z/OS IEASYMUP resource must be protected in accordance with proper security requirements.

**Rule ID:** `SV-223965r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS IBMFAC(IEASYMUP) If the TSS resources are owned or DEFPROT is specified for the resource class, this is not a finding. Enter TSS WHOHAS IBMFAC(IEASYMUP) If TSS resource access authorizations restrict UPDATE and/or greater access to DASD administrators, Tape Library personnel, and system programming personnel, this is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223966`

### Rule: CA-TSS Default ACID must be properly defined.

**Rule ID:** `SV-223966r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST STC If *DEF* has action of *FAIL* this is not a finding. If the default ACID is defined enter: TSS List(<defined ACID>) If the ACID has no access to resources and no facility access and sourced to the internal reader, this is not a finding. If any of the above is untrue, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223967`

### Rule: The CA-TSS BYPASS attribute must be limited to trusted STCs only.

**Rule ID:** `SV-223967r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(STC) If only STCs listed as trusted in the IBM z/OS MVS Initialization and Tuning Reference are granted the BYPASS privilege, this is not a finding. Guidelines for reference: Assign the TRUSTED attribute when one of the following conditions applies: -The started procedure or address space creates or accesses a wide variety of unpredictably named data sets within your installation. -Insufficient authority to an accessed resource might risk an unsuccessful IPL or other system problem. -Avoid assigning TRUSTED to a z/OS started procedure or address space unless it is listed here or you are instructed to do so by the product documentation. Additionally external security managers are candidates for trusted attribute. Any other started tasks not listed or not covered by the guidelines are a finding unless approval by the Authorizing Official AO.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223968`

### Rule: CA-TSS MSCA ACID must perform security administration only.

**Rule ID:** `SV-223968r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) DATA(ALL,PA) TYPE(SCA) If the MSCA ACID has access limited to performing security administration functions only, this is not a finding. Below is an example of allowed setup for MSCA account and authorities. "MSCA" as the Accessorid is merely an example here, which is site determined. List is not all inclusive. The primary SCA for the domain will be listed within the "NAME" field since they are responsible for the MSCA ACID. ACCESSORID = MSCA NAME = "primary SCA" TYPE = MASTER FACILITY = BATCH PROFILES = SECURID ATTRIBUTES = AUDIT,CONSOLE,NOATS data set = %. *. data set = ***** +. VOLUMES = *(G) XA data set = SYS3.TSS.BACKUP ACCESS = UPDATE ACTION = AUDIT ----------- ADMINISTRATION AUTHORITIES RESOURCE = *ALL* ACCESS = ALL ACID = *ALL* FACILITIES = *ALL* LIST DATA = *ALL*,PROFILES,PASSWORD,SESSKEY MISC1 = *ALL* MISC2 = *ALL* MISC4 = *ALL* MISC8 = *ALL* MISC9 = *ALL* NOTE 1: Update access to the backup security database is required by the MSCA account anytime the ISSO needs to run/submit the TSS Utility called TSSFAR. MSCA account may from time to time be required to have additional access for the period of project such as Extending the Security Database. NOTE 2: MSCA account must be used for such items as: TSSFAR, EXTENDING Security Database, creating SCA/LSCA accounts, working with LSCA accounts (scoping, admin rights, etc.). Most often the ISSO staff will utilize their normal SCA account. The MSCA account will not be anyone's primary security administrative account.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223969`

### Rule: CA-TSS ACIDs granted the CONSOLE attribute must be justified.

**Rule ID:** `SV-223969r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute TSS Report TSS AUDIT with PRIVILEGES control statement PRIVILEGES [SHORT]. For more information TSSAUDIT reports refer to the CA-TSS Report and Tracking Guide. Refer to the resulting report. If ACIDs with CONSOLE authority are limited to authorized SCA security administrators and the system programmers that maintain the CA-TSS software product only, this is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223970`

### Rule: CA-TSS ACIDs defined as security administrators must have the NOATS attribute.

**Rule ID:** `SV-223970r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute TSS Report TSS AUDIT with PRIVILEGES control statement PRIVILEGES [SHORT]. For more information TSSAUDIT reports refer to the CA-TSS Report and Tracking Guide. Refer to the resulting report. If all security administrators have the "NOATS" attribute, this is not a finding.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-223972`

### Rule: CA-TSS VTHRESH Control Option values specified must be set to (10,NOT,CAN).

**Rule ID:** `SV-223972r958636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific operating system functionality where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Control Shell enter: TSS MODIFY STATUS If the VTHRESH Control Option values are not set to "VTHRRESH(10,NOT,CAN)", this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-223973`

### Rule: IBM z/OS FTP.DATA configuration statements must have a proper banner statement with the Standard Mandatory DOD Notice and Consent Banner.

**Rule ID:** `SV-223973r1050767_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000024-GPOS-00007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the FTP.DATA file specified on the SYSFTPD DD statement in the FTP started task JCL. The SYSFTPD DD statement is optional. The search order for FTP.DATA is: /etc/ftp.data SYSFTPD DD statement jobname.FTP.DATA SYS1.TCPPARMS(FTPDATA) tcpip.FTP.DATA Examine the BANNER statement. If the BANNER statement in the FTP Data configuration file specifies an HFS file or data set that contains a logon banner, this is not a finding. The below banner is mandatory and deviations are not permitted except as authorized in writing by the DOD chief information officer. The thrust of this new policy is to make it clear that there is no expectation of privacy when using DOD information systems and all use of DOD information systems is subject to searching, auditing, inspecting, seizing, and monitoring, even if some personal use of a system is permitted: STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-223974`

### Rule: IBM z/OS SMF recording options for the FTP server must be configured to write SMF records for all eligible events.

**Rule ID:** `SV-223974r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). Satisfies: SRG-OS-000032-GPOS-00013, SRG-OS-000392-GPOS-00172</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If FTPDATA is configured with the following SMF statements, this is not a finding. FTP.DATA Configuration Statements SMF TYPE119 SMFJES TYPE119 SMFSQL TYPE119 SMFAPPE [Not coded or commented out] SMFDEL [Not coded or commented out] SMFEXIT [Not coded or commented out] SMFLOGN [Not coded or commented out] SMFREN [Not coded or commented out] SMFRETR [Not coded or commented out] SMFSTOR [Not coded or commented out]

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223975`

### Rule: CA-TSS permission bits and user audit bits for HFS objects that are part of the FTP server component must be properly configured.

**Rule ID:** `SV-223975r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs At the input line enter: cd /usr/sbin/ enter ls -alW If the following File permission and user Audit Bits are true, this is not a finding. /usr/sbin/ftpd 1740 fff /usr/sbin/ftpdns 1755 fff /usr/sbin/tftpd 0644 faf cd ls -alW If the following file permission and user Audit Bits are true, this is not a finding. /etc/ftp.data 0744 faf /etc/ftp.banner 0744 faf NOTES: Some of the files listed above are not used in every configuration. The absence of a file is not considered a finding. The /usr/sbin/ftpd and /usr/sbin/ftpdns objects are symbolic links to /usr/lpp/tcpip/sbin/ftpd and /usr/lpp/tcpip/sbin/ftpdns respectively. The permission and user audit bits on the targets of the symbolic links must have the required settings. The /etc/ftp.data file may not be the configuration file the server uses. It is necessary to check the SYSFTPD DD statement in the FTP started task JCL to determine the actual file. The TFTP Server does not perform any user identification or authentication, allowing any client to connect to the TFTP Server. Due to this lack of security, the TFTP Server will not be used. The TFTP Client is not secured from use. The permission bits for /usr/sbin/tftpd should be set to 644. The /etc/ftp.banner file may not be the banner file the server uses. It is necessary to check the BANNER statement in the FTP Data configuration file to determine the actual file. Also, the permission bit setting for this file must be set as indicated in the table above. A more restrictive set of permissions is not permitted. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223976`

### Rule: IBM z/OS data sets for the FTP server must be properly protected.

**Rule ID:** `SV-223976r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If WRITE and ALLOCATE access to the data set containing the FTP Data configuration file is restricted to systems programming personnel this is not a finding. Note: READ access to all authenticated users is permitted. If WRITE and ALLOCATE access to the data set containing the FTP Data configuration file is logged this is not a finding. If WRITE and ALLOCATE access to the data set containing the FTP banner file is restricted to systems programming personnel this is not a finding. Note: READ access to the data set containing the FTP banner file is permitted to all authenticated users. Notes: The MVS data sets mentioned above are not used in every configuration. Absence of a data set will not be considered a finding. The data set containing the FTP Data configuration file is determined by checking the SYSFTPD DD statement in the FTP started task JCL. The data set containing the FTP banner file is determined by checking the BANNER statement in the FTP Data configuration file.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223977`

### Rule: IBM z/OS FTP Control cards must be properly stored in a secure PDS file.

**Rule ID:** `SV-223977r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the System administrator fora list(s) of the locations for all FTP Control cards within a given application/AIS, ensuring no FTP control cards are within in-stream JCL, JCL libraries or any open access data sets. If access to PDS files where FTP Control cards are stored are not restricted to appropriate personnel this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-223978`

### Rule: IBM z/OS user exits for the FTP server must not be used without proper approval and documentation.

**Rule ID:** `SV-223978r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Data configuration file specified on the SYSFTPD DD statement in the FTP started task JCL. Refer to the file(s) allocated by the STEPLIB DD statement in the FTP started task JCL. Refer to the libraries specified in the system Linklist and LPA. If any FTP Server exits are in use, identify them and validate that they were reviewed for integrity and approved by the site AO. Refer to the following items are in effect for FTP Server user exits: The FTCHKCMD, FTCHKIP, FTCHKJES, FTCHKPWD, FTPSMFEX and FTPOSTPR modules are not located in the FTP daemon's STEPLIB, Linklist, or LPA. NOTE: The ISPF ISRFIND utility can be used to search the system Linklist and LPA for specific modules. If both of the above are true, this is not a finding. If any FTP Server user exits are implemented and the site has not had the site systems programmer verify the exit was securely written and installed, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223979`

### Rule: The IBM z/OS FTP server daemon must be defined with proper security parameters.

**Rule ID:** `SV-223979r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPD Command Shell enter: TSS LIST(FTPD) SEGMENT(OMVS) NOTE: The JCL member is typically named FTPD If the FTPD ACID has the STC facility, this is not a finding. If the FTPD ACID has the following z/OS UNIX attributes, this is not a finding. UID(0), HOME directory '/', shell program /bin/sh.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-223980`

### Rule: IBM z/OS FTP.DATA configuration for the FTP server must have the INACTIVE statement properly set.

**Rule ID:** `SV-223980r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the file specified on the SYSFTPD DD statement in the FTP started task JCL. If the INACTIVE statement is coded with a value greater than "600", this is a finding. If the INACTIVE statement is coded with a value of "0", this is a finding. If there is no INACTIVE statement coded or the INACTIVE statement is commented out, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-223981`

### Rule: IBM z/OS startup parameters for the FTP server must have the INACTIVE statement properly set.

**Rule ID:** `SV-223981r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TCPIP started task JCL. If all the items below are true, this is not a finding. If any of the items below are untrue, this is a finding. The following items are in effect for the FTP daemon's started task JCL: -The SYSTCPD and SYSFTPD DD statements specify the TCP/IP Data and FTP Data configuration files respectively. -The ANONYMOUS keyword is not coded on the PARM parameter on the EXEC statement. -The ANONYMOUS=logonid combination is not coded on the PARM parameter on the EXEC statement. -The INACTIVE keyword is not coded on the PARM parameter on the EXEC statement. The AUTOLOG statement block can be configured to have TCP/IP start the FTP Server. The FTP entry (e.g., FTPD) can include the PARMSTRING parameter to pass parameters to the FTP procedure when started. NOTE: Parameters passed on the PARMSTRING parameter override parameters specified in the FTP procedure. If an FTP entry is configured in the AUTOLOG statement block in the TCP/IP Profile configuration file, ensure the following items are in effect: -The ANONYMOUS keyword is not coded on the PARMSTRING parameter. -The ANONYMOUS=logonid combination is not coded on the PARMSTRING parameter. -The INACTIVE keyword is not coded on PARMSTRING parameter.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-223982`

### Rule: IBM z/OS FTP.DATA configuration statements for the FTP server must specify the Standard Mandatory DoD Notice and Consent Banner statement.

**Rule ID:** `SV-223982r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the file specified on the SYSFTPD DD statement in the FTP started task JCL. If the BANNER statement is not coded or is commented out, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-223984`

### Rule: The IBM z/OS TFTP server program must be properly protected.

**Rule ID:** `SV-223984r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS PROGRAM(*) If the Program resources TFTPD and EZATD are owned appropriately in the PROGRAM resource class, this is not a finding. Enter TSS WHOHAS(TFTPD) TSS WHOHAS(EZATD) If no access to the program resources TFTPD and EZATD is permitted, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223985`

### Rule: IBM z/OS JES2.** resource must be properly protected in the CA-TSS database.

**Rule ID:** `SV-223985r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: WHOOWNS OPERCMDS(JES2) NOTE: JES2 is typically the name of the JES2 subsystem. Refer to the SUBSYS report and locate the entry with the description of PRIMARY JOB ENTRY SUBSYSTEM. The SUBSYSTEM NAME of this entry is the name of the JES2 subsystem. If the JES2. resource is not owned, or is owned inappropriately, in the OPERCMDS class, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223986`

### Rule: IBM z/OS RJE workstations and NJE nodes must be controlled in accordance with STIG requirements.

**Rule ID:** `SV-223986r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to SYS1.PARMLIB (JES2PARM) For each node entry If all JES2 defined NJE nodes and RJE workstations have a profile defined in the IBMFAC resource class, this is not a finding. Notes: Nodename is the NAME parameter value specified on the NODE statement. Review the JES2 parameters for NJE node definitions by searching for "NODE(" in the report. Workstation is RMTnnnn, where nnnn is the number on the RMT statement. Review the JES2 parameters for RJE workstation definitions by searching for "RMT(" in the report. NJE. and RJE. definitions will force logonid and password protection of all NJE and RJE connections respectively. This method is acceptable in lieu of using discrete profiles. If any JES2 defined NJE node or RJE workstation is not owned in the IBMFAC class, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223987`

### Rule: IBM z/OS JES2 input sources must be controlled in accordance with the proper security requirements.

**Rule ID:** `SV-223987r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer the JES2PARM member of SYS1.PARMLIB Review the following resources in the JESINPUT resource class: NOTE: If any of the following are not defined within the JES2 parameters, the resource in the JESINPUT resource class does not have to be owned. INTRDR (internal reader for batch jobs) nodename (NJE node) OFFn.* (spool offload receiver) Rnnnn (RJE workstation) RDRnn (local card reader) STCINRDR (internal reader for started tasks) TSUINRDR (internal reader for TSO logons) Note 1: Nodename is the NAME parameter in the NODE statement. Review the NJE node definitions by searching for "NODE(" in the report. Note 2: OFFn, where n is the number of the offload receiver. Review the spool offload receiver definitions by searching for "OFF(" in the report. Note 3: Rnnnn, where nnnn is the number of the remote workstation. Review the RJE node definitions by searching for "RMT(" in the report. Note 4: RDRnn, where nn is the number of the reader. Review the reader definitions by searching for "RDR(" in the report. From the ISPF Command Shell enter: TSS WHOOWNS JESINPUT(*) If all of the resources above are owned by generic and/or fully qualified entries in the JESINPUT resource class, this is not a finding. If any of the above resources are not owned, or are owned inappropriately, in the JESINPUT resource class, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223988`

### Rule: IBM z/OS JES2 input sources must be properly controlled.

**Rule ID:** `SV-223988r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS JESINPUT(*) For each resource owned If all of the TSS resources and/or generic equivalent identified above are defined with access restricted to the appropriate personnel, this is not a finding. If any of the TSS resources and/or generic equivalent identified above are not defined with access restricted to the appropriate personnel, this is a finding. From the ISPF Command Shell enter: TSS LIST RDT(*) If the JESINPT RESOURCE does not have DEFPROT as an attribute, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223989`

### Rule: IBM z/OS JES2 output devices must be controlled in accordance with the proper security requirements.

**Rule ID:** `SV-223989r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer the JES2PARM member of SYS1.PARMLIB Review the WRITER resource in the JESINPUT resource class: NOTE: If the WRITER resource is not defined within the JES2 parameters, the resource in the JESINPUT resource class does not have to be owned. From the ISPF Command Shell enter: TSS WHOOWNS JESINPUT(WRITER) If the WRITER resource is owned by generic and/or fully qualified entries in the JESINPUT resource class, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223990`

### Rule: IBM z/OS JES2 output devices must be properly controlled for classified systems.

**Rule ID:** `SV-223990r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Classification of the system is unclassified, this is not applicable. From the ISPF Command Shell enter: TSS WHOHAS WRITER(JES2.) If the TSS WRITER resource or generic equivalent identified above is defined with access restricted to the appropriate personnel, this is not a finding. If the TSS WRITER resource or generic equivalent identified above is not defined with access restricted to the appropriate personnel, this is a finding. From the ISPF Command Shell enter: TSS LIST RDT(*) If the JESINPUT RESOURCE does not have DEFPROT as an attribute, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223991`

### Rule: IBM z/OS JESSPOOL resources must be protected in accordance with security requirements.

**Rule ID:** `SV-223991r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer the JES2PARM member of SYS1.PARMLIB. Review the JESSPOOL resource in the JESINPUT resource class: NOTE: If the JESSPOOL resource is not defined within the JES2 parameters, the resource in the JESINPUT resource class does not have to be owned. From the ISPF Command Shell enter: TSS WHOOWNS JESINPUT(JESSPOOL) If the JESSPOOL resource is owned by generic and/or fully qualified entries in the JESINPUT resource class, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223992`

### Rule: IBM z/OS JESNEWS resources must be protected in accordance with security requirements.

**Rule ID:** `SV-223992r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOHAS OPERCMDS(JES2.) NOTE: JES2 is typically the name of the JES2 subsystem. Refer to the SUBSYS report and locate the entry with the description of PRIMARY JOB ENTRY SUBSYSTEM. The SUBSYSTEM NAME of this entry is the name of the JES2 subsystem. If access authorization to the JES2.UPDATE.JESNEWS resource in the OPERCMDS class restricts CONTROL access to the appropriate personnel (i.e., users responsible for maintaining the JES News data set) and all access is logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223993`

### Rule: IBM z/OS JESTRACE and/or SYSLOG resources must be protected in accordance with security requirements.

**Rule ID:** `SV-223993r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS JESSPOOL(*) If JESSPOOL localnodeid resource is not defined, this is a finding. Enter TSS WHOHAS JESSPOOL(localnodeid.) Review the following resources defined to the JESSPOOL resource class: localnodeid.JES2.$TRCLOG.taskid.*.JESTRACE localnodeid.+MASTER+.SYSLOG.jobid.*.SYSLOG or localnodeid.+BYPASS+.SYSLOG.jobid.-.SYSLOG NOTE: These resource profiles may be more generic as long as they pertain directly to the JESTRACE and SYSLOG data sets. For example: localnodeid.JES2.*.*.*.JESTRACE localnodeid.+MASTER+.*.*.*.SYSLOG or localnodeid.+BYPASS+.*.*.*.SYSLOG NOTE: Review the JES2 parameters to determine the localnodeid by searching for OWNNODE in the NJEDEF statement, and then searching for NODE(nnnn) (where nnnn is the value specified by OWNNODE). The NAME parameter value specified on this NODE statement is the localnodeid. Another method is to issue the JES2 command $D NODE,NAME,OWNNODE=YES to obtain the NAME of the OWNNODE. If the access authorization for the resources mentioned above is restricted to the following, this is not a finding. -ACID(s) associated with external writer(s) can have complete access. NOTE: An external writer is an STC that removes data sets from the JES spool. In this case, it is responsible for archiving the JESTRACE and SYSLOG data sets. The STC default name is XWTR and the external writer program is called IASXWR00. -Systems personnel and security administrators responsible for diagnosing JES2 and z/OS problems can have complete access. -Application Development and Application Support personnel responsible for diagnosing application problems can have READ access to the SYSLOG resource.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223994`

### Rule: IBM z/OS JES2 spool resources must be controlled in accordance with security requirements.

**Rule ID:** `SV-223994r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOHAS JESSPOOL(localnodeid.) If the following guidance is true, this is not a finding. Review the JESSPOOL report for resource permissions with the following naming convention. These permissions may be fully qualified, be specified as generic, or be specified with masking as indicated below: localnodeid.useracid.jobname.jobid.dsnumber.name localnodeid - The name of the node on which the SYSIN or SYSOUT data set currently resides. useracid - The user ACID associated with the job. This is the user ACID TSS uses for validation purposes when the job runs. jobname - The name that appears in the name field of the JOB statement. jobid - The job number JES2 assigned to the job. dsnumber - The unique data set number JES2 assigned to the spool data set. A D is the first character of this qualifier. name - The name of the data set specified in the DSN= parameter of the DD statement. If the JCL did not specify DSN= on the DD statement that creates the spool data set, JES2 uses a question mark (?). All users must have access to their own JESSPOOL resources. Permission can be granted by resource permission JESSPOOL(localnodeid.%.) ACCESS(ALL). This permission can be given to profiles, individual user, and/or the ALL record. Access to this resource does not require logging. Ensure the following items are in effect: The localnodeid. resource will be restricted to only system programmers, operators, and automated operations personnel, with access of ALL. All access will be logged. (localnodeid. resource includes all generic and/or masked permissions, example: localnodeid.**, localnodeid.*, etc.) The JESSPOOL localnodeid.userid.jobname.jobid.dsnumber.name, whether generic and/or masked, can be made available to users, when approved by the ISSO. Access will be identified at the minimum access for the user to accomplish the users function. All access will be logged. An example is team members within a team, providing the capability to view, help, and/or debug other team member jobs/processes. CSSMTP will be restricted to localnodeid.userid.jobname.jobid.dsnumber.name, whether generic and/or masked when approved by the ISSO. All access will be logged. Spooling products users (CA-SPOOL, CA View, etc.) will be restricted to localnodeid.userid.jobname.jobid.dsnumber.name, whether generic and/or masked when approved by the ISSO. Logging of access is not required.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223995`

### Rule: IBM z/OS JES2 system commands must be protected in accordance with security requirements.

**Rule ID:** `SV-223995r1115950_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell, enter: TSS WHOHAS OPERCMDS(JES2.) If the JES2.** resource is defined to the OPERCMDS class with an access of NONE and all access is logged, this is not a finding. If access to JES2 system commands defined in the IBM z/OS JES2 commands is restricted to the appropriate personnel (e.g., operations staff, systems programming personnel, general users), this is not a finding. NOTE: Use the GROUP category specified in the table referenced above as a guideline to determine appropriate personnel access to system commands.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223996`

### Rule: IBM z/OS Surrogate users must be controlled in accordance with proper security requirements.

**Rule ID:** `SV-223996r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000326-GPOS-00126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) DATA(XA) If no XA ACID entries exist in the above reports, this is not applicable. For each ACID identified in the XA ACID entries, if the following items are true regarding ACID permissions, this is not a finding. -ACID permission (XA ACID) is logged (ACTION = AUDIT), only for Privileged USERIDS (MASTER, SCA, DCA, VCA, ZCA) if they are XAUTH; at the discretion of the ISSM/ISSO scheduling tasks may be exempted from logging. -Access authorization is restricted to scheduling tools, started tasks or other system applications required for running production jobs. -Other users may have minimal access required for running production jobs with documentation properly approved and filed with the site security official (ISSM or equivalent).

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-223997`

### Rule: Duplicated IBM z/OS sensitive utilities and/or programs must not exist in APF libraries.

**Rule ID:** `SV-223997r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removal of unneeded or non-secure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ISPF Command line enter: TSO ISRDDN APF An APF List results. On the Command line enter: DUPlicates (Make sure there is appropriate access. If there is not, you may receive insufficient access errors.) If any of the list of Sensitive Utilities exist in the duplicate APF modules returned, this is a finding. The following list contains Sensitive Utilities that will be checked. AHLGTF AMASPZAP AMAZAP AMDIOCP AMZIOCP BLSROPTR CSQJU003 CSQJU004 CSQUCVX CSQUTIL CSQ1LOGP DEBE DITTO FDRZAPOP GIMSMP HHLGTF ICKDSF ICPIOCP IDCSC01 IEHINITT IFASMFDP IGWSPZAP IHLGTF IMASPZAP IND$FILE IOPIOCP IXPIOCP IYPIOCP IZPIOCP WHOIS L052INIT TMSCOPY TMSFORMT TMSLBLPR TMSMULV TMSREMOV TMSTPNIT TMSUDSNB

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-223998`

### Rule: IBM z/OS required SMF data record types must be collected.

**Rule ID:** `SV-223998r998499_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000064-GPOS-00033, SRG-OS-000458-GPOS-00203, SRG-OS-000461-GPOS-00205, SRG-OS-000462-GPOS-00206, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209, SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000468-GPOS-00212, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218, SRG-OS-000474-GPOS-00219, SRG-OS-000475-GPOS-00220, SRG-OS-000476-GPOS-00221, SRG-OS-000477-GPOS-00222, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000255-GPOS-00096, SRG-OS-000365-GPOS-00152, SRG-OS-000348-GPOS-00136, SRG-OS-000303-GPOS-00120, SRG-OS-000327-GPOS-00127, SRG-OS-000392-GPOS-00172</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member. If all of the required SMF record types identified below are collected, this is not a finding. IBM SMF Records to be collected at a minimum: 0 (00) - IPL 6 (06) - External Writer/ JES Output Writer/ Print Services Facility (PSF) 7 (07) - [SMF] Data Lost 14 (0E) - INPUT or RDBACK Data Set Activity 15 (0F) - OUTPUT, UPDAT, INOUT, or OUTIN Data Set Activity 17 (11) - Scratch Data Set Status 18 (12) - Rename Non-VSAM Data Set Status 24 (18) - JES2 Spool Offload 25 (19) - JES3 Device Allocation 26 (1A) - JES Job Purge 30 (1E) - Common Address Space Work 32 (20) - TSO/E User Work Accounting 41 (29) - DIV Objects and VLF Statistics 42 (2A) - DFSMS statistics and configuration 43 (2B) - JES Start 45 (2D) - JES Withdrawal/Stop 47 (2F) - JES SIGNON/Start Line (BSC)/LOGON 48 (30) - JES SIGNOFF/Stop Line (BSC)/LOGOFF 49 (31) - JES Integrity 52 (34) - JES2 LOGON/Start Line (SNA) 53 (35) - JES2 LOGOFF/Stop Line (SNA) 54 (36) - JES2 Integrity (SNA) 55 (37) - JES2 Network SIGNON 56 (38) - JES2 Network Integrity 57 (39) - JES2 Network SYSOUT Transmission 58 (3A) - JES2 Network SIGNOFF 60 (3C) - VSAM Volume Data Set Updated 61 (3D) - Integrated Catalog Facility Define Activity 62 (3E) - VSAM Component or Cluster Opened 64 (40) - VSAM Component or Cluster Status 65 (41) - Integrated Catalog Facility Delete Activity 66 (42) - Integrated Catalog Facility Alter Activity 80 (50) - RACF/TOP SECRET Processing 81 (51) - RACF Initialization 82 (52) - ICSF Statistics 83 (53) - RACF Audit Record For Data Sets 90 (5A) - System Status 92 (5C) except subtypes 10, 11 - OpenMVS File System Activity 102 (66) - DATABASE 2 Performance 103 (67) - IBM HTTP Server 110 (6E) - CICS/ESA Statistics 118 (76) - TCP/IP Statistics 119 (77) - TCP/IP Statistics 199 (C7) - TSOMON 230 (E6) - ACF2 or as specified in ACFFDR (vendor-supplied default is 230) 231 (E7) - TSS logs security events under this record type

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-223999`

### Rule: IBM z/OS Session manager must properly configure wait time limits.

**Rule ID:** `SV-223999r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the session manager in use initiates a session lock after a 15-minute period of inactivity for all connection types, this is not a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-224000`

### Rule: The IBM z/OS BPX.SMF resource must be properly configured.

**Rule ID:** `SV-224000r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the FACILITY resource class for BPX.SMF. If the RACF rules are as follows, this is not a finding. BPX.SMF.119.94 - READ allowed for users running the ssh, sftp, or scp client commands. BPX.SMF.119.96 - READ allowed for users running the scp or sftp-server server commands. BPX.SMF.119.97 - READ allowed for users running the scp or sftp client commands. The following profile grants the permitted users the authority to write or test for any SMF record being recorded. Access should be permitted as follows: BPX.SMF - READ access only when documented and justified in Site Security Plan. Documentation should include a reason why a more specific profile is not acceptable.

## Group: SRG-OS-000038-GPOS-00016

**Group ID:** `V-224001`

### Rule: IBM z/OS must specify SMF data options to ensure appropriate activation.

**Rule ID:** `SV-224001r958414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know when events occurred (date and time). Associating event types with detected events in the operating system audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system. Satisfies: SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000254-GPOS-00095, SRG-OS-000269-GPOS-00103, SRG-OS-000368-GPOS-00154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member. SUBSYS(STC,EXITS(IEFU29,IEFU83,IEFU84,IEFUJP,IEFUSO), INTERVAL(SMF,SYNC),NODETAIL) If the SMF collection options are specified as stated below with exception of those specified in the above NOTEs, this is not a finding. The settings for several parameters are critical to the collection process: ACTIVE Activates the collection of SMF data. MAXDORM(0500) Specifies the amount of real time that SMF allows data to remain in an SMF buffer before it is written to a recording data set. Value is site defined. SID Specifies the system ID to be recorded in all SMF records. SYS(DETAIL) Controls the level of detail recorded. SYS(INTERVAL) Ensures the periodic recording of data for long running jobs. SYS Specifies the types and sub types of SMF records that are to be collected. SYS(TYPE) indicates that the supplied list is inclusive (i.e., specifies the record types to be collected). Record types not listed are not collected. SYS(NOTYPE) indicates that the supplied list is exclusive (i.e., specifies those record types not to be collected). Record types listed are not collected. The site may use either form of this parameter to specify SMF record type collection. However, at a minimum, all record types are listed.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-224002`

### Rule: IBM z/OS BUFUSEWARN in the SMFPRMxx must be properly set.

**Rule ID:** `SV-224002r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member in SYS1.PARMLIB. If BUFUSEWARN is set for "75" (75%) or less, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224003`

### Rule: IBM z/OS PASSWORD data set and OS passwords must not be used.

**Rule ID:** `SV-224003r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator to determine if the system PASSWORD data set and OS passwords are being used. If, based on the information provided, it can be determined that the system PASSWORD data set and OS passwords are not used, this is not a finding. If it is evident that OS passwords are utilized, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224004`

### Rule: The CA-TSS database must be on a separate physical volume from its backup and recovery data sets.

**Rule ID:** `SV-224004r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the System proclibs for the TSS STC. If the Security database is located on the same volume as either the backup, Alternate or Recovery file, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224005`

### Rule: The CA-TSS database must be backed up on a scheduled basis.

**Rule ID:** `SV-224005r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the TSS Proclib PARMFILE DD to determine the PARM member. If the BACKUP is missing or coded with blank or OFF this is a finding. Note: If the security data base is shared only one of the systems is required to configure the BACKUP option in the PARMFILE. Determine that the option is properly coded on one of the systems that share the security database. From the ISPF Command Shell enter: TSS MODIFY(Status) If the backup parameter is active with a valid time this is not a finding.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-224006`

### Rule: The IBM z/OS Policy Agent must be configured to deny-all, allow-by-exception firewall policy for allowing connections to other systems.

**Rule ID:** `SV-224006r991593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the policy agent policy statements. If it can be determined that the policy agent employs a deny-all, allow-by exception firewall policy for allowing connections to other systems this is not a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-224007`

### Rule: IBM z/OS must not have Inaccessible APF libraries defined.

**Rule ID:** `SV-224007r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper APF and/or PROG member. Examine each entry and verify that it exists on the specified volume. If inaccessible APF libraries exist, this is a finding. ISRDDN APF

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-224008`

### Rule: IBM z/OS inapplicable PPT entries must be invalidated.

**Rule ID:** `SV-224008r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review program entries in the IBM Program Properties Table (PPT). You may use a third-party product to examine these entries; however, to determine program entries, issue the following command from an ISPF command line: TSO ISRDDN LOAD IEFSDPPT Press Enter. Interpret the display as follows: Examine contents at offset 8 Hex 'x2' - Bypass Password Protection Hex 'x3' - Bypass Password Protection Hex 'x4' - No data set Integrity Hex 'x5' - No data set Integrity Hex 'x6' - Both Hex 'x7' - Both Determine Privilege Key at offset 9. A value of hex '70' or less indicates an elevated privilege. For each module identified in the "eyecatcher" that has BYPASS Password Protection, No data set Integrity, an elevated Privilege Key, or any combination thereof, determine if there is a valid loaded module. Again, you may use a third-party product; otherwise, execute the following steps: From an ISPF command line TSO ISRDDN LOAD <privileged module> Press Enter. If the return message is "Load Failed", make sure there is an entry in PARMLIB member SCHEDxx that revokes the excessive privilege. If this is not true, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-224009`

### Rule: IBM z/OS LNKAUTH=APFTAB must be specified in the IEASYSxx member(s) in the currently active parmlib data set(s).

**Rule ID:** `SV-224009r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. If "LNKAUTH=APFTAB" is not specified, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-224010`

### Rule: IBM z/OS sensitive and critical system data sets must not exist on shared DASD.

**Rule ID:** `SV-224010r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check HMC, VM, and z/OS on how to validate and determine a DASD volume(s) is shared. Note: In VM issue the command "QUEUE DASD SYSTEM" this display will show shared volume(s) and indicates the number of systems sharing the volume. Validate all machines that require access to these shared volume(s) have the volume(s) mounted. Obtain a map or list VTOC of the shared volume(s). Check if shared volume(s) contain any critical or sensitive data sets. Identify shared and critical or sensitive data sets on the system being audited. These data sets can be APF, LINKLIST, LPA, Catalogs, etc, as well as product data sets. If all of the critical or sensitive data sets identified on shared volume(s) are protected and justified to be on shared volume(s), this is not a finding. List critical or sensitive data sets are possible security breaches, if not justified and not protected on systems having access to the data set(s) and on shared volume(s).

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-224011`

### Rule: The IBM z/OS Policy Agent must contain a policy that manages excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-224011r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the Policy Agent policy statements. If it can be determined that there are policy statements that manages excess capacity, this is not a finding.

## Group: SRG-OS-000274-GPOS-00104

**Group ID:** `V-224013`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify appropriate personnel when accounts are created.

**Rule ID:** `SV-224013r998500_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of operating system user accounts and notifies administrators and information system security officers (ISSOs) that it exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented process to notify appropriate personnel when accounts are created. If there is no documented process, this is a finding.

## Group: SRG-OS-000275-GPOS-00105

**Group ID:** `V-224014`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify appropriate personnel when accounts are modified.

**Rule ID:** `SV-224014r998501_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of operating system user accounts and notifies administrators and information system security officers (ISSOs) that it exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented process to notify appropriate personnel when accounts are modified. If there is no documented process, this is a finding.

## Group: SRG-OS-000276-GPOS-00106

**Group ID:** `V-224015`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify appropriate personnel when accounts are deleted.

**Rule ID:** `SV-224015r998502_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When operating system accounts are disabled, user accessibility is affected. Accounts are utilized for identifying individual operating system users or for identifying the operating system processes themselves. Sending notification of account disabling events to the system administrator and information system security officers (ISSOs) is one method for mitigating this risk. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented process to notify appropriate personnel when accounts are deleted. If there is no documented process, this is a finding.

## Group: SRG-OS-000277-GPOS-00107

**Group ID:** `V-224016`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify appropriate personnel when accounts are removed.

**Rule ID:** `SV-224016r998503_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When operating system accounts are disabled, user accessibility is affected. Accounts are utilized for identifying individual operating system users or for identifying the operating system processes themselves. Sending notification of account disabling events to the system administrator and information system security officers (ISSOs) is one method for mitigating this risk. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented process to notify appropriate personnel when accounts are removed. If there is no documented process, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-224017`

### Rule: Unsupported IBM z/OS system software must not be installed and/or active on the system.

**Rule ID:** `SV-224017r958804_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to all products that meet the following criteria: - Uses authorized and restricted z/OS interfaces by utilizing Authorized Program Facility (APF) authorized modules or libraries. - Requires access to system data sets or sensitive information or requires special or privileged authority to run. For the products in the above category, refer to the vendor's support lifecycle information for current versions and releases. If the software products currently running on the reviewed system are at a version greater than or equal to the products listed in the vendor's Support Lifecycle information, this is not a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-224018`

### Rule: IBM z/OS must not allow nonexistent or inaccessible Link Pack Area (LPA) libraries.

**Rule ID:** `SV-224018r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ISPF Command line enter: TSO ISRDDN LPA Review the list. If there are any DUMMY entries, i.e., inaccessible LPA libraries, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-224019`

### Rule: IBM z/OS must not allow nonexistent or inaccessible LINKLIST libraries.

**Rule ID:** `SV-224019r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From and ISPF Command line enter: TSO ISRDDN LINKLIST Review the list, if there are any DUMMY entries i.e., inaccessible LINKLIST libraries, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-224020`

### Rule: CA-TSS must be installed and properly configured.

**Rule ID:** `SV-224020r958796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to system configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the operating system can have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to operating system components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the active tasks on the system. Use IBM SDSF or the system Log. If CA-TSS is active this is not a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-224021`

### Rule: IBM z/OS SMF collection files (system MANx data sets or LOGSTREAM DASD) must have storage capacity to store at least one weeks worth of audit data.

**Rule ID:** `SV-224021r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SMF dump procedure in there system. If the output data sets in the procedure have storage capacity to store at least one weeks' worth of audit data, this is not a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-224022`

### Rule: IBM z/OS System Administrators must develop an automated process to collect and retain SMF data.

**Rule ID:** `SV-224022r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator if there is an automated process is in place to collect and retain all SMF data produced on the system. If, based on the information provided, it can be determined that an automated process is in place to collect and retain all SMF data produced on the system, this is not a finding. If it cannot be determined this process exists and is being adhered to, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-224023`

### Rule: The IBM z/OS SNTP daemon (SNTPD) must be active.

**Rule ID:** `SV-224023r1038944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From UNIX System Services ISPF Shell, navigate to ribbon select tools. Select option 1 - Work with Processes. If SNTP Daemon (SNTPD) is not active, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-224024`

### Rule: IBM z/OS SNTP daemon (SNTPD) permission bits must be properly configured.

**Rule ID:** `SV-224024r1038944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: cd /usr/sbin ls -al If the following File permission and user Audit Bits are true, this is not a finding. /usr/sbin/sntpd 1740 faf The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-224025`

### Rule: IBM z/OS PARMLIB CLOCKxx must have the Accuracy PARM coded properly.

**Rule ID:** `SV-224025r998506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done in order to determine the time difference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the CLOCKxx member of PARMLIB. If the ACCURACY parm is not coded, this is a finding. If the ACCURACY parm is coded to "1000", this is not a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-224026`

### Rule: The IBM z/OS Policy Agent must contain a policy that protects against or limits the effects of denial-of-service (DoS) attacks by ensuring IBM z/OS is implementing rate-limiting measures on impacted network interfaces.

**Rule ID:** `SV-224026r958902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of the operating system to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the "Policy Agent" policy statements. If it can be determined that the policy that protects against or limits the effects of denial-of-service (DoS) attacks by ensuring the operating system is implementing rate-limiting measures on impacted network interfaces, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224031`

### Rule: IBM z/OS must configure system wait times to protect resource availability based on site priorities.

**Rule ID:** `SV-224031r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member. Examine the JWT, SWT, and TWT values. If the JWT parameter is greater than "15" minutes, and the system is processing unclassified information, review the following items. If any of these items is true, this is not a finding. -If a session is not terminated, but instead is locked out after 15 minutes of inactivity, a process must be in place that requires user identification and authentication before the session is unlocked. Session lock-out will be implemented through system controls or terminal screen protections. -A system's default time for terminal lock-out or session termination may be lengthened to 30 minutes at the discretion of the ISSM or ISSO. The ISSM and/or ISSO will maintain the documentation for each system with a time-out adjusted beyond the 15-minute recommendation to explain the basis for this decision. -The ISSM and/or ISSO may set selected userids to have a time-out of up to 60 minutes in order to complete critical reports or transactions without timing out. Each exception must meet the following criteria: -The time-out exception cannot exceed 60 minutes. -A letter of justification fully documenting the user requirement(s) must be submitted and approved by the site ISSM or ISSO. In addition, this letter must identify an alternate means of access control for the terminal(s) involved (e.g., a room that is locked at all times, a room with a cipher lock to limit access, a password protected screen saver set to 30 minutes or less, etc.). -The requirement must be revalidated on an annual basis. If the TWT and SWT values are equal or less than the JWT value, this is not a finding.

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-224032`

### Rule: IBM z/OS must employ a session manager to conceal, via the session lock, information previously visible on the display with a publicly viewable image.

**Rule ID:** `SV-224032r958404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. The operating system session lock event must include an obfuscation of the display screen so as to prevent other users from reading what was previously displayed. Publicly viewable images can include static or dynamic images, for example, patterns used with screen savers, photographic images, solid colors, a clock, a battery life indicator, or a blank screen, with the additional caveat that none of the images convey sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the configuration parameters for the session manager in use. If there is no session manager in use, this is a finding. If the session manager is not configured to conceal, via the session lock, information previously visible on the display with a publicly viewable image, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-224034`

### Rule: IBM z/OS must employ a session manager to manage retaining a users session lock until that user reestablishes access using established identification and authentication procedures.

**Rule ID:** `SV-224034r958400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock must remain in place until the user re-authenticates. No other activity aside from re-authentication will unlock the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the configuration parameters for the session manager in use. If there is no session manager in use, this is a finding. If the session manager is not configured to retain a user's session lock until that user reestablishes access using established identification and authentication procedures, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-224035`

### Rule: IBM z/OS system administrator (SA) must develop a procedure to remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-224035r998507_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, the operating system must be configured to automatically terminate these types of accounts after a DOD-defined time period of 72 hours. To address access requirements, many operating systems may be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the procedure to automatically remove or disable temporary user accounts after 72 hours. If there is no procedure, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-224036`

### Rule: IBM z/OS system administrator (SA) must develop a procedure to remove or disable emergency accounts after the crisis is resolved or 72 hours.

**Rule ID:** `SV-224036r998508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by the organization's system administrators when network or normal logon/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the procedure to automatically remove or disable emergency accounts after the crisis is resolved or 72 hours. If there is no procedure, this is a finding.

## Group: SRG-OS-000304-GPOS-00121

**Group ID:** `V-224037`

### Rule: IBM z/OS system administrator (SA) must develop a procedure to notify SAs and information system security officers (ISSOs) of account enabling actions.

**Rule ID:** `SV-224037r998509_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable an existing disabled account. Sending notification of account enabling actions to the System Administrator and ISSO is one method for mitigating this risk. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. In order to detect and respond to events that affect user accessibility and application processing, operating systems must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the procedure to notify system administrators and ISSOs of account enabling actions. If there is no procedure, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-224038`

### Rule: IBM z/OS system administrator must develop a procedure to notify designated personnel if baseline configurations are changed in an unauthorized manner.

**Rule ID:** `SV-224038r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to notify designated personnel if baseline configurations are changed in an unauthorized manner. If there is no procedure, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-224040`

### Rule: IBM z/OS system administrator must develop a procedure to remove all software components after updated versions have been installed.

**Rule ID:** `SV-224040r958936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to remove all software components after updated versions have been installed. If there is no procedure, this is a finding.

## Group: SRG-OS-000447-GPOS-00201

**Group ID:** `V-224041`

### Rule: IBM z/OS system administrator must develop a procedure to shut down the information system, restart the information system, and/or notify the system administrator when anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-224041r958948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If anomalies are not acted upon, security functions may fail to secure the system. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to shut down the information system, restart the information system, and/or notify the system administrator when anomalies occur. If a procedure does not exist, this is a finding. If the procedure does not properly shut down the information system, restart the information system, and/or notify the system administrator when anomalies occur, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-224042`

### Rule: IBM z/OS system administrator must develop a procedure to offload SMF files to a different system or media than the system being audited.

**Rule ID:** `SV-224042r959008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to offload SMF files to a different system or media than the system being audited. If the procedure does not exist, this is a finding.

## Group: SRG-OS-000030-GPOS-00011

**Group ID:** `V-224043`

### Rule: IBM z/OS must employ a session manager for users to directly initiate a session lock for all connection types.

**Rule ID:** `SV-224043r998511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, operating systems need to provide users with the ability to manually invoke a session lock so users may secure their session should the need arise for them to temporarily vacate the immediate physical vicinity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the configuration parameters for the session manager in use. If there is no session manager in use this is a finding. If the session manager in use does not allow users to directly initiate a session lock for all connection types, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-224044`

### Rule: The SSH daemon must be configured to use a FIPS 140-2 compliant cryptographic algorithm.

**Rule ID:** `SV-224044r1083018_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000120-GPOS-00061, SRG-OS-000250-GPOS-00093</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the SSH daemon configuration file found in /etc/ssh/ directory. Alternately: From the Unix System Services ISPF Shell, navigate to ribbon select tools. Select option 1 - Work with Processes. If SSH Daemon is not active, this is not a finding. Examine SSH daemon configuration file. sshd_config If there are no Ciphers lines, or the ciphers list contains any cipher not starting with "aes", this is a finding. If the MACs line is not configured to "hmac-sha1" or greater, this is a finding. Examine the z/OS-specific sshd server systemwide configuration: zos_sshd_config If any of the following is untrue, this is a finding. FIPSMODE=YES CiphersSource=ICSF MACsSource=ICSF

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-224045`

### Rule: IBM z/OS SSH daemon must be configured to only use the SSHv2 protocol.

**Rule ID:** `SV-224045r958480_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the SSH daemon configuration file. May be found in /etc/ssh/ directory. Alternately: From UNIX System Services ISPF Shell navigate to ribbon select tools. Select option 1 - Work with Processes. If SSH Daemon is not active, this is not a finding. Examine SSH daemon configuration file. If the variables "Protocol 2,1" or "Protocol 1" are defined on a line without a leading comment, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224046`

### Rule: IBM z/OS permission bits and user audit bits for HFS objects that are part of the Syslog daemon component must be configured properly.

**Rule ID:** `SV-224046r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ISPF Enter cd /usr/sbin Enter ls -alW If File Permission Bits and User Audit Bits for SYSLOG Daemon HFS directories and files are as below this is not a finding. /usr/sbin/syslogd 1740 fff Enter cd /etc/ Enter ls -alW If File Permission Bits and User Audit Bits for Output log file defined in the configuration file are as below this is not a finding. /etc/syslog.conf 0744 faf 0744 fff Notes: The /usr/sbin/syslogd object is a symbolic link to /usr/lpp/tcpip/sbin/syslogd. The permission and user audit bits on the target of the symbolic link must have the required settings. The /etc/syslog.conf file may not be the configuration file the daemon uses. It is necessary to check the script or JCL used to start the daemon to determine the actual configuration file. For example, in /etc/rc: _BPX_JOBNAME='SYSLOGD' /usr/sbin/syslogd -f /etc/syslog.conf For example, in the SYSLOGD started task JCL: //SYSLOGD EXEC PGM=SYSLOGD,REGION=30M,TIME=NOLIMIT // PARM='POSIX(ON) ALL31(ON)/ -f /etc/syslogd.conf' //SYSLOGD EXEC PGM=SYSLOGD,REGION=30M,TIME=NOLIMIT // PARM='POSIX(ON) ALL31(ON) /-f //''SYS1.TCPPARMS(SYSLOG)''' The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224047`

### Rule: The IBM z/OS Syslog daemon must not be started at z/OS initialization.

**Rule ID:** `SV-224047r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
SYSLOGD may be started from the shell, a cataloged procedure (STC), or the BPXBATCH program. Additionally, other mechanisms (e.g., a job scheduler) may be used to automatically start the Syslog daemon. To thoroughly analyze this requirement you may need to view the OS SYSLOG using SDSF, find the last IPL, and look for the initialization of SYSLOGD. If the Syslog daemon SYSLOGD is started automatically during the initialization of the z/S/ system, this is not a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224048`

### Rule: The IBM z/OS Syslog daemon must be properly defined and secured.

**Rule ID:** `SV-224048r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(SYSLOGD) SEGMENT(OMVS) If the following guidance is true, this is not a finding. -The Syslog daemon userid is SYSLOGD. -The SYSLOGD userid has the STC facility. -The SYSLOGD userid has UID(0), HOME('/'), and PROGRAM('/bin/sh') specified in the OMVS segment. -The SYSLOGD started proc is assigned the SYSLOGD userid is in the Started Task Table. If Syslog daemon is started from /etc/rc then from the ISPF Command Shell enter: OMVS cd /etc cat rc If Syslog daemon is started from /etc/rc then ensure that the "_BPX_JOBNAME" and "_BPX_USERID" environment variables are assigned a value of SYSLOGD. If the Syslog daemon is started from /etc/rc and the "_BPX_JOBNAME" and "_BPX_USERID" environment variables are not assigned a value of SYSLOGD, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224049`

### Rule: IBM z/OS DFSMS resources must be protected in accordance with the proper security requirements.

**Rule ID:** `SV-224049r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all SMS resources and/or generic equivalent are properly protected according to the requirements specified and the following guidance is true, this is not a finding. The TSS resources are owned or DEFPROT is specified for the resource class. To avoid authorization failures once a base cluster is accessed via a PATH or AIX by a user or application that has authority to the PATH and AIX, but not the base cluster, APAR OA50118 must be applied. The resource STGADMIN.IGG.CATALOG.SECURITY.CHANGE is defined with access of NONE. The resource STGADMIN.IGG.CATALOG.SECURITY.BOTH is defined with access of READ. Note: The resource STGADMIN.IGG.CATALOG.SECURITY.CHANGE can be defined with read access for migration purposes. If it is, a detailed migration plan must be documented and filed by the ISSM that determines a definite migration period. All access must be logged. At the completion of migration, this resource must be configured with access of NONE. If the resource STGADMIN.IGG.CATALOG.SECURITY.CHANGE and STGADMIN.IGG.CATALOG.SECURITY.BOTH are both defined, ADMIN.IGG.CATALOG.SECURITY.BOTH takes precedence. STGADMIN.DPDSRN.olddsname is restricted to system programmers and all access is logged. The STGADMIN.IGD.ACTIVATE.CONFIGURATION is restricted to system programmers and all access is logged. The STGADMIN.IGG.DEFDEL.UALIAS is restricted to centralized and decentralized security personnel and system programmers and all access is logged. The following resources and prefixes may be available to the end user. STGADMIN.ADR.COPY.CNCURRNT STGADMIN.ADR.COPY.FLASHCPY STGADMIN.ADR.COPY.TOLERATE.ENQF STGADMIN.ADR.DUMP.CNCURRNT STGADMIN.ADR.DUMP.TOLERATE.ENQF STGADMIN.ADR.RESTORE.TOLERATE.ENQF STGADMIN.ARC.ENDUSER. STGADMIN.IGG.ALTER.SMS The following resource is restricted to Application Production Support Team members, Automated Operations, DASD managers, and system programmers. STGADMIN.IDC.DCOLLECT The following resources are restricted to Application Production Support Team members, DASD managers, and system programmers. STGADMIN.ARC.CANCEL STGADMIN.ARC.LIST STGADMIN.ARC.QUERY STGADMIN.ARC.REPORT STGADMIN.DMO.CONFIG STGADMIN.IFG.READVTOC STGADMIN.IGG.DELGDG.FORCE The following resource prefixes, at a minimum, are restricted to DASD managers and system programmers. STGADMIN.ADR STGADMIN.ANT STGADMIN.ARC STGADMIN.DMO STGADMIN.ICK STGADMIN.IDC STGADMIN.IFG STGADMIN.IGG STGADMIN.IGWSHCDS The following Storage Administrator functions prefix is restricted to DASD managers and system programmers and all access is logged. STGADMIN.ADR.STGADMIN.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224050`

### Rule: IBM z/OS DFSMS Program Resources must be properly defined and protected.

**Rule ID:** `SV-224050r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the load modules residing in the following Load libraries to determine program resource definitions: v SYS1.DGTLLIB for DFSMSdfp/ISMF v SYS1.DGTLLIB for DFSMSdss/ISMF v SYS1.DFQLLIB for DFSMShsm If the installation moves these modules to another load library the installation-defined load library must be used in the program protection. If the TSS resources are owned or DEFPROT is specified for the resource class, this is not a finding. If the TSS resource access authorizations restrict access to the appropriate personnel, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224051`

### Rule: IBM z/OS DFSMS control data sets must be protected in accordance with security requirements.

**Rule ID:** `SV-224051r1050768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the logical parmlib data sets, example: SYS1.PARMLIB(IGDSMSxx), to identify the fully qualified file names for the following SMS data sets: Source Control Data Set (SCDS) Active Control Data Set (ACDS) Communications Data Set (COMMDS) Automatic Class Selection Routine Source Data Sets (ACS) ACDS Backup COMMDS Backup If the TSS data set rules for the SCDS, ACDS, COMMDS, and ACS data sets restrict UPDATE and ALL access to only systems programming personnel, this is not a finding. If the TSS data set rules for the SCDS, ACDS, COMMDS, and ACS data sets do not restrict UPDATE and ALL access to only systems programming personnel, this is a finding. Note: At the discretion of the ISSM, DASD administrators are allowed UPDATE access to the control data sets.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224052`

### Rule: IBM z/OS using DFSMS must properly specify SYS(x).PARMLIB(IGDSMSxx), SMS parameter settings.

**Rule ID:** `SV-224052r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the logical parmlib data sets, example: SYS1.PARMLIB(IGDSMSxx), for the following SMS parameter settings: Parameter Key SMS ACDS(ACDS data set name) COMMDS(COMMDS data set name) If the required parameters are defined, this is not a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-224054`

### Rule: IBM z/OS SMF recording options for the SSH daemon must be configured to write SMF records for all eligible events.

**Rule ID:** `SV-224054r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMF data collection is the basic unit of tracking of all system functions and actions. Included in this tracking data are the audit trails from each of the ACPs. If the control options for the recording of this tracking are not properly maintained, then accountability cannot be monitored, and its use in the execution of a contingency plan could be compromised. Satisfies: SRG-OS-000032-GPOS-00013, SRG-OS-000392-GPOS-00172</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the SSH daemon configuration file, which may be found in /etc/ssh/ directory. Alternately: From UNIX System Services ISPF Shell, navigate to ribbon select tools. Select option 1 - Work with Processes. If SSH Daemon is not active, this is not a finding. Examine SSH daemon configuration file. If ServerSMF is not coded with ServerSMF TYPE119_U83 or is commented out, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-224055`

### Rule: The IBM z/OS SSH daemon must be configured with the Standard Mandatory DoD Notice and Consent Banner.

**Rule ID:** `SV-224055r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the SSH daemon configuration file. May be found in /etc/ssh/ directory. Alternately: From UNIX System Services ISPF Shell navigate to ribbon select tools. Select option 1 - Work with Processes. If SSH Daemon is not active, this is not a finding. Examine SSH daemon configuration file. If Banner statement is missing or configured to none, this is a finding. Ensure that the contents of the file specified on the banner statement contain a logon banner. The below banner is mandatory and deviations are not permitted except as authorized in writing by the DoD Chief Information Officer. If there is any deviation this is a finding. STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-224056`

### Rule: IBM z/OS PROFILE.TCPIP configuration statements for the TCP/IP stack must be properly coded.

**Rule ID:** `SV-224056r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TCPIP started task JCL. If the following items are in effect for the configuration statements specified in the TCP/IP Profile configuration file, this is not a finding. NOTE: If the INCLUDE statement is coded in the TCP/IP Profile configuration file, the data set specified on this statement must be checked for the following items as well. -The SMFPARMS statement is not coded or commented out. -The DELETE statement is not coded or commented out for production systems. -The SMFCONFIG statement is coded with (at least) the FTPCLIENT and TN3270CLIENT operands. -The TCPCONFIG and UDPCONFIG statements are coded with (at least) the RESTRICTLOWPORTS operand. If the TCPCONFIG does not have the TTLS statement coded, this is a finding. NOTE: If the INCLUDE statement is coded, the data set specified will be checked for access authorization compliance.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224057`

### Rule: IBM z/OS permission bits and user audit bits for HFS objects that are part of the Base TCP/IP component must be configured properly.

**Rule ID:** `SV-224057r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs At the input line enter: cd /etc enter ls -alW If the following File permission and user Audit Bits are true this is not a finding. /etc/hosts 0744 faf /etc/protocol 0744 faf /etc/resolv.conf 0744 faf /etc/services 0740 faf cd /usr ls -alW If the following file permission and user Audit Bits are true this is not a finding. /usr/lpp/tcpip/sbin 0755 faf /usr/lpp/tcpip/bin 0755 faf Notes: Some of the files listed above are not used in every configuration. The absence of a file is not considered a finding. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224058`

### Rule: IBM z/OS TCP/IP resources must be properly protected.

**Rule ID:** `SV-224058r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following guidance is true, this is not a finding. -The EZA, EZB, and IST resources of the SERVAUTH resource class are properly owned and/or DEFPROT is specified in the SERVAUTH resource class. -No access is given to the EZA, EZB, and IST high level resources of the SERVAUTH resource class. -If the product CSSMTP is on the system, no access is given to EZB.CSSMTP of the SERVAUTH resource class. -If the product CSSMTP is on the system, EZB.CSSMTP.sysname.writername.JESnode will be specified and made available to the CSSMTP started task and authenticated users that require access to use CSSMTP for e-mail services. -Authenticated users that require access will be permitted access to the second level of the resources in the SERVAUTH resource class. Examples are the network (NETACCESS), port (PORTACCESS), stack (STACKACCESS), and FTP resources in the SERVAUTH resource class. -The EZB.STACKACCESS. resource access authorizations restrict access to those started tasks with valid requirements and users with valid FTP access requirements. -The EZB.FTP.*.*.ACCESS.HFS) resource access authorizations restrict access to FTP users with specific written documentation showing a valid requirement exists to access OMVS files and directories. -The EZB.INITSTACK.sysname.tcpname resource access authorizations restrict access before policies have been installed, to users authorized by the system security plan requiring access to the TCP/IP stack.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224059`

### Rule: IBM z/OS data sets for the Base TCP/IP component must be properly protected.

**Rule ID:** `SV-224059r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MVS data sets of the Base TCP/IP component provide the configuration, operational, and executable properties of IBMs TCP/IP system product. Failure to properly secure these data sets may lead to unauthorized access resulting in the compromise of the integrity and availability of the operating system environment, ACP, and customer data. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a data set access list for all TCP/IP base components. If all of the following items are true, this is not a finding. WRITE and ALLOCATE access to product data sets is restricted to systems programming personnel (i.e., SMP/E distribution data sets with the prefix SYS1.TCPIP.AEZA and target data sets with the prefix SYS1.TCPIP.SEZA). WRITE and ALLOCATE access to the data set(s) containing the Data and Profile configuration files is restricted to systems programming personnel. Note: If any INCLUDE statements are specified in the Profile configuration file, the named MVS data sets have the same access authorization requirements. WRITE and ALLOCATE access to the data set(s) containing the Data and Profile configuration files is logged. Note: If any INCLUDE statements are specified in the Profile configuration file, the named MVS data sets have the same logging requirements. WRITE and ALLOCATE access to the data set(s) containing the configuration files shared by TCP/IP applications is restricted to systems programming personnel. Note: For systems running the TSS ACP replace the WRITE and ALLOCATE with WRITE, UPDATE, CREATE, CONTROL, SCRATCH, and ALL.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224060`

### Rule: IBM z/OS Configuration files for the TCP/IP stack must be properly specified.

**Rule ID:** `SV-224060r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the procedure libraries defined to JES2 and locate the TCPIP JCL member. Note: If GLOBALTCPIPDATA is specified, any TCPIP.DATA statements contained in the specified file or data set take precedence over any TCPIP.DATA statements found using the appropriate environment's (native MVS or z/OS UNIX) search order. If GLOBALTCPIPDATA is not specified, the appropriate environment's (Native MVS or z/OS UNIX) search order is used to locate TCPIP.DATA. If the PROFILE and SYSTCPD DD statements specify the TCP/IP Profile and Data configuration files respectively, this not a finding. If the RESOLVER_CONFIG variable on the EXEC statement is set to the same file name specified on the SYSTCPD DD statement, this is not a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224061`

### Rule: IBM z/OS started tasks for the Base TCP/IP component must be defined in accordance with security requirements.

**Rule ID:** `SV-224061r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to system Proclibs to determine the TCPIP address space(s). From the ISPF Command Shell enter: TSS list(<TCPIP STCs>) SEGMENT(OMVS) For each TCPIP: If all of the following items are true, this is not a finding. If any item is untrue, this is a finding. From the ISPF Command Shell enter TSS LIST(EZAZSSI) SEGMENT(OMVS) If EZAZSSI STC has the STC facility, this is not finding. -Named TCPIP or, in the case of multiple instances, prefixed with TCPIP. -Has the STC facility. -z/OS UNIX attributes: UID(0), HOME directory '/', shell program /bin/sh Ensure the following items are in effect for the ACID assigned to the EZAZSSI started task: -Named EZAZSSI -Has the STC facility.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-224062`

### Rule: IBM z//OS must be configured to restrict all TCP/IP ports to ports, protocols, and/or services as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-224062r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer the TCPIP PROFILE DD statement to determine the TCP/IP Ports. If the PROFILE DD statement is not supplied use the default search order to find thee PROFILE data set. See the IP Configuration Guide for a description of the search order for PROFILE.TCPIP. If the all the Ports included into the configuration are restricted to the ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and vulnerability assessments, this is not a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-224065`

### Rule: IBM z/OS TN3270 Telnet server configuration statement MSG10 text must have the Standard Mandatory DoD Notice and Consent Banner.

**Rule ID:** `SV-224065r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000024-GPOS-00007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TN3270 started task JCL. If all USS tables referenced in BEGINVTAM USSTCP statements include MSG10 text that specifies the Standard logon banner this is not a finding. The below banner is mandatory and deviations are not permitted except as authorized in writing by the DoD Chief Information Officer. The thrust of this new policy is to make it clear that there is no expectation of privacy when using DoD information systems and all use of DoD information systems is subject to searching, auditing, inspecting, seizing, and monitoring, even if some personal use of a system is permitted: STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. DOD requires that a logon warning banner be displayed. Within the TN3270 Telnet Server, the banner can be implemented through the USS table that is specified on a BEGINVTAM USSTCP statement. The text associated with message ID 10 (i.e., MSG10) in the USS table is sent to clients that are subject to USSTCP processing.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-224066`

### Rule: IBM z/OS SMF recording options for the TN3270 Telnet server must be properly specified.

**Rule ID:** `SV-224066r958846_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000032-GPOS-00013</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TCPIP started task JCL. If the following configuration statement settings are in effect in the TCP/IP Profile configuration data set, this is not a finding. NOTE: If the INCLUDE statement is coded in the TCP/IP Profile configuration data set, the data set specified on this statement must be checked for the following items as well. -The TELNETPARMS SMFINIT statement is coded with the TYPE119 operand within each TELNETPARMS statement block. -The TELNETPARMS SMFTERM statement is coded with the TYPE119 operand within each TELNETPARMS statement block. Note: The SMFINIT and SMFTERM statement can appear in both TELNETGLOBAL and TELNETPARM statement blocks. If duplicate statements appear in the TELNETGLOBALS, TELNETPARMS, Telnet uses the last valid statement that was specified.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-224067`

### Rule: IBM z/OS SSL encryption options for the TN3270 Telnet server must be specified properly for each statement that defines a SECUREPORT or within the TELNETGLOBALS.

**Rule ID:** `SV-224067r1050770_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000120-GPOS-00061, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000396-GPOS-00176, SRG-OS-000478-GPOS-00223, SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TCPIP started task JCL. If the following items are in effect for the configuration specified in the TCP/IP Profile configuration file, this is not a finding. NOTE: If an INCLUDE statement is coded in the TCP/IP Profile configuration file, the data set specified on this statement must be checked for the following items as well. NOTE: FIPS 140-2 minimum encryption is the accepted level of encryption and will override this requirement if greater. -The TELNETGLOBALS block that specifies an ENCRYPTION statement states one or more of the below cipher specifications. -Each TELNETPARMS block that specifies the SECUREPORT statement, specifies an ENCRYPTION statement states one or more of the below cipher specifications. And the TELNETGLOBALS block does or does not specify an ENCRYPTION statement. Cipher Specifications SSL_3DES_SHA SSL_AES_256_SHA SSL_AES_128_SHA

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224068`

### Rule: IBM z/OS VTAM session setup controls for the TN3270 Telnet server must be properly specified.

**Rule ID:** `SV-224068r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the TN3270 Profile configuration file identified by the PROFILE DD in the TN3270 procedure. NOTE: If the INCLUDE statement is coded in the TCP/IP Profile configuration file, the data set specified on this statement must be checked for the following items as well. If all of the following are true, this is not a finding. If any of the above is untrue, this is a finding. -Within each BEGINVTAM statement block, one BEGINVTAM USSTCP statement is coded that specifies only the table name operand. No client identifier, such as host name or IP address, is specified so the statement applies to all connections not otherwise controlled. -The USS table specified on each "back stop" USSTCP statement mentioned in Item (1) above is coded to allow access only to session manager applications and NC PASS applications. -Within each BEGINVTAM statement block, additional BEGINVTAM USSTCP statements that specify a USS table that allows access to other applications may be coded only if the statements include a client identifier operand that references only secure terminals. -Any BEGINVTAM DEFAULTAPPL statement that does not specify a client identifier, or specifies any type of client identifier that would apply to unsecured terminals, specifies a session manager application or an NC PASS application as the application name. -Any BEGINVTAM LUMAP statement, if used with the DEFAPPL operand and applied to unsecured terminals, specifies only a session manager application or an NC PASS application. NOTE: The BEGINVTAM LINEMODEAPPL requirements will not be reviewed at this time. Further testing must be performed to determine how the CL/Supersession and NC-PASS applications work with line mode.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-224069`

### Rule: IBM z/OS PROFILE.TCPIP configuration for the TN3270 Telnet server must have the INACTIVE statement properly specified.

**Rule ID:** `SV-224069r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TCPIP started task JCL. NOTE: If the INCLUDE statement is coded in the TCP/IP Profile configuration file, the data set specified on this statement must be checked for the following items as well. TELNETPARMS Block (one defined for each port the server is listening to, typically ports 23 and 992) If the TELNETPARMS INACTIVE statement is coded within each TELNETPARMS statement block and specifies a value between "1" and "900", this is not a finding. NOTE: Effective in z/OS release 1.2, the INACTIVE statement can appear in both TELNETGLOBAL and TELNETPARM statement blocks.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224072`

### Rule: IBM Z/OS TSOAUTH resources must be restricted to authorized users.

**Rule ID:** `SV-224072r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS TSOAUTH(*) For each resource defined enter: TSS WHOHAS(<tsoauth resource>) If the following guidance is true, this is not a finding. -The ACCT authorization is restricted to security personnel. -The CONSOLE authorization is restricted to authorized systems personnel (e.g., systems programming personnel, operations staff, etc.) and READ access may be given to all user when SDSF in install at the ISSOs discretion. -The MOUNT authorization is restricted to DASD batch users only. -The OPER authorization is restricted to authorized systems personnel (e.g., systems programming personnel, operations staff, etc.). -The PARMLIB authorization is restricted to only z/OS systems programming personnel and READ access may be given to auditors. -The TESTAUTH authorization is restricted to only z/OS systems programming personnel.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-224073`

### Rule: CA-TSS LOGONIDs must not be defined to SYS1.UADS for non-emergency use.

**Rule ID:** `SV-224073r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator to provide a list of all emergency userids available to the site along with the associated function of each. If any SYS1.UADS userids are assigned for other than emergency purposes, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224074`

### Rule: IBM z/OS UNIX HFS MapName file security parameters must be properly specified.

**Rule ID:** `SV-224074r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removal of unneeded or non-secure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the logical parmlib data sets, example: SYS1.PARMLIB(BPXPRMxx), for the following FILESYSTYPE entry: FILESYSTYPE TYPE(AUTOMNT) ENTRYPOINT(BPXTAMD) If the above entry is not found or is commented out in the BPXPRMxx member(s), this is not applicable. From the ISPF Command Shell enter: OMVS cd /etc cat auto.master perform a contents list for the file identified Example: cat u.map Note: The /etc/auto.master HFS file (and the use of Automount) is optional. If the file does not exist, this is not applicable. Note: The setuid parameter and the security parameter have a significant security impact. For this reason these parameters must be explicitly specified and not allowed to default. If each MapName file specifies the "setuid No" and "security Yes" statements for each automounted directory, this is not a finding. If there is any deviation from the required values, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-224075`

### Rule: IBM z/OS NOBUFFS in SMFPRMxx must be properly set (default is MSG).

**Rule ID:** `SV-224075r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member in SYS1.PARMLIB. If NOBUFFS is set to "HALT", this is not a finding. Note: If availability is an overriding concern NOBUFFS can be set to MSG.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224076`

### Rule: IBM z/OS BPX resource(s) must be protected in accordance with security requirements.

**Rule ID:** `SV-224076r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS IBMFAC(BPX.) If the BPX. resource is properly owned, this is not a finding. From the ISPF Command Shell enter: TSS WHOHAS (<each BPX resource>) If any item below are untrue, this is a finding. -There are no TSS rules that allow access to the BPX resource. -There are no TSS rules for BPX.SAFFASTPATH defined. -The TSS rules for each of the BPX resources listed in the z/OS UNIX System Services Planning, Establishing UNIX security, restrict access to appropriate system tasks or systems programming personnel.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224077`

### Rule: IBM z/OS UNIX resources must be protected in accordance with security requirements.

**Rule ID:** `SV-224077r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000326-GPOS-00126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS SURROGAT(*) If the TSS resources and/or generic equivalent for BPX. is not owned enter: TSS LIST RDT If the TSS resources and/or generic equivalent for BPX. is not owned or DEFPROT is specified for the resource class, this is a finding. From the ISPF Command Shell enter: TSS WHOHAS SURROGAT(BPX.) If the TSS resource access authorizations restrict BPX.SRV.user to system software processes (e.g., web servers) that act as servers under z/OS UNIX, this is not a finding. If the RACF rules for all BPX.SRV.user SURROGAT resources restrict access to authorized users identified in the Site Security Plan, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224078`

### Rule: IBM z/OS UNIX SUPERUSER resources must be protected in accordance with guidelines.

**Rule ID:** `SV-224078r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS WHOOWNS UNIXPRIV(*) If the TSS resources and/or generic equivalent for SUPERUSER. is not owned enter: TSS LIST RDT If the TSS resources and/or generic equivalent for SUPERUSER. is not owned or DEFPROT is specified for the resource class, this is a finding. From the ISPF Command Shell enter: TSS WHOHAS SURROGAT(SUPERUSER.) If the TSS resource access authorizations restrict BPX.SRV.user to system software processes (e.g., web servers) that act as servers under z/OS UNIX, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224079`

### Rule: IBM z/OS UNIX MVS data sets or HFS objects must be properly protected.

**Rule ID:** `SV-224079r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the proper BPXPRMxx member in SYS1.PARMLIB If the ESM data set rules for the data sets referenced in the ROOT and the MOUNT statements in BPXPRMxx restrict update access to the z/OS UNIX kernel (i.e., OMVS or OMVSKERN), this is not a finding. If the ESM data set rules for the data set referenced in the ROOT and the MOUNT statements in BPXPRMxx restrict WRITE or greater access to systems programming personnel, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224080`

### Rule: IBM z/OS UNIX MVS data sets with z/OS UNIX components must be properly protected.

**Rule ID:** `SV-224080r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESM data set rules for each of the data sets listed in the table below restrict WRITE or greater access to systems programming personnel, this is not a finding. MVS DATA SETS WITH z/OS UNIX COMPONENTS DATA SET NAME/MASK MAINTENANCE TYPE FUNCTION SYS1.ABPX* Distribution IBM z/OS UNIX ISPF panels, messages, tables, clists SYS1.AFOM* Distribution IBM z/OS UNIX Application Services SYS1.BPA.ABPA* Distribution IBM z/OS UNIX Connection Scaling Process Mgr. SYS1.CMX.ACMX* Distribution IBM z/OS UNIX Connection Scaling Connection Mgr. SYS1.SBPX* Target IBM z/OS UNIX ISPF panels, messages, tables, clists SYS1.SFOM* Target IBM z/OS UNIX Application Services SYS1.CMX.SCMX* Target IBM z/OS UNIX Connection Scaling Connection Mgr.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224081`

### Rule: IBM z/OS UNIX MVS data sets used as step libraries in /etc/steplib must be properly protected.

**Rule ID:** `SV-224081r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the pathname from the STEPLIBLIST line in BPXPRMxx member of PARMLIB. From the ISPF Command shell enter: ISHELL on the command line: on the path name line enter: /etc/ From the resulting display scroll down to the <stepliblist name> from BPXPRMxx parm. Enter B for browse on that line. If ESM data set rules for libraries specified restrict WRITE or greater access to only systems programming personnel, this is not a finding. If the ESM data set rules for libraries specify that all (i.e., failures and successes) WRITE or greater access will be logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224082`

### Rule: IBM z/OS UNIX HFS permission bits and audit bits for each directory must be properly protected.

**Rule ID:** `SV-224082r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs enter CD / enter ls -alW If the HFS permission bits and user audit bits for each directory and file match or are more restrictive than the specified settings listed in the SYSTEM DIRECTORY SECURITY SETTINGS table below, this is not a finding. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing SYSTEM DIRECTORY SECURITY SETTINGS DIRECTORY PERMISSION BITS USER AUDIT BITS FUNCTION / [root] 755 faf Root level of all file systems. Holds critical mount points. /bin 1755 fff Shell scripts and executables for basic functions /dev 1755 fff Character-special files used when logging into the OMVS shell and during C language program compilation. Files are created during system IPL and on a per-demand basis. /etc 1755 faf Configuration programs and files (usually with locally customized data) used by z/OS UNIX and other product initialization processes /lib 1755 fff System libraries including dynamic link libraries and files for static linking /samples 1755 fff Sample configuration and other files /tmp 1777 fff Temporary data used by daemons, servers, and users. Note: /tmp must have the sticky bit on to restrict file renames and deletions. /u 1755 fff Mount point for user home directories and optionally for third-party software and other local site files /usr 1755 fff Shell scripts, executables, help (man) files and other data. Contains sub-directories (e.g., lpp) and mount points used by program products that may be in separate file systems. /var 1775 fff Dynamic data used internally by products and by elements and features of z/OS UNIX.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224083`

### Rule: IBM z/OS UNIX system file security settings must be properly protected or specified.

**Rule ID:** `SV-224083r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: OMVS For each file listed in the table below enter: ls -alW /<directory name>/<file name> If the HFS permission bits and user audit bits for each directory and file match or are more restrictive than the specified settings listed in the table, this is not a finding. NOTE: Some of the files listed are not used in every configuration. Absence of any of the files is not considered a finding. SYSTEM FILE SECURITY SETTINGS FILE PERMISSION BITS USER AUDIT BITS FUNCTION /bin/sh 1755 faf z/OS UNIX shell Note: /bin/sh has the sticky bit on to improve performance. /dev/console 740 fff The system console file receives messages that may require System Administrator (SA) attention. /dev/null 666 fff A null file; data written to it is discarded. /etc/auto.master any mapname files 740 faf Configuration files for automount facility /etc/inetd.conf 740 faf Configuration file for network services /etc/init.options 740 faf Kernel initialization options file for z/OS UNIX environment /etc/log 744 fff Kernel initialization output file /etc/profile 755 faf Environment setup script executed for each user /etc/rc 744 faf Kernel initialization script for z/OS UNIX environment /etc/steplib 740 faf List of MVS data sets valid for set user ID and set group ID executables /etc/table name 740 faf List of z/OS userids and group names with corresponding alias names /usr/lib/cron/at.allow /usr/lib/cron/at.deny 700 faf Configuration files for the at and batch commands /usr/lib/cron/cron.allow /usr/lib/cron/cron.deny 700 faf Configuration files for the crontab command NOTE: Some of the files listed are not used in every configuration. Absence of any of the files is not considered a finding. NOTE: The names of the MapName files are site-defined. Refer to the listing in the EAUTOM report. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224084`

### Rule: IBM z/OS UNIX MVS HFS directory(s) with OTHER write permission bit set must be properly defined.

**Rule ID:** `SV-224084r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the OMVS Command line enter the following command string: find / -type d -perm -0002 ! -perm -1000 -exec ls -aldWE {} \; If there are no directories that have the other write permission bit set on without the sticky bit set on, there is no finding. NOTE: In the symbolic permission bit display, the sticky bit is indicated as a "t" or "T" in the execute portion of the other permissions. For example, a display of the permissions of a directory with the sticky bit on could be "drwxrwxrwt". If all directories that have the other write permission bit set on do not contain any files with the setuid bit set on, this is not a finding. NOTE: In the symbolic permission bit display, the setuid bit is indicated as an "s" or "S" in the execute portion of the owner permissions. For example, a display of the permissions of a file with the setuid bit on could be "-rwsrwxrwx". If all directories that have the other write permission bit set on do not contain any files with the setgid bit set on, this is not a finding. NOTE: In the symbolic permission bit display, the setgid bit is indicated as an "s" or "S" in the execute portion of the group permissions. For example, a display of the permissions of a file with the setgid bit on could be "-rwxrwsrwx".

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224085`

### Rule: The CA-TSS HFSSEC resource class must be defined with DEFPROT.

**Rule ID:** `SV-224085r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS MODIFY STATUS If the Control Option is HFSSEC(OFF), this is Not Applicable. Enter: TSS LIST RDT If the DEFPROT attribute is specified for the HFSSEC resource class in the RDT, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224086`

### Rule: IBM z/OS UNIX OMVS parameters in PARMLIB must be properly specified.

**Rule ID:** `SV-224086r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the IEASYS00 member of SYS1.PARMLIB. If the parameter is specified as OMVS=xx or OMVS=(xx,xx,...) in the IEASYSxx member, this is not a finding. If the OMVS statement is not specified, OMVS=DEFAULT is used. In minimum mode there is no access to permanent file systems or to the shell, and IBM's Communication Server TCP/IP will not run.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224087`

### Rule: IBM z/OS UNIX BPXPRMxx security parameters in PARMLIB must be properly specified.

**Rule ID:** `SV-224087r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the BPXPRM00 member of SYS1.PARMLIB. If the required parameter keywords and values are defined as detailed below, this is not a finding. Parameter Keyword Value SUPERUSER BPXROOT TTYGROUP TTY STEPLIBLIST /etc/steplib USERIDALIASTABLE Will not be specified. ROOT SETUID will be specified MOUNT NOSETUID SETUID (for Vendor-provided files)SECURITY STARTUP_PROC OMVS

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224088`

### Rule: IBM z/OS UNIX security parameters in etc/profile must be properly specified.

**Rule ID:** `SV-224088r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ISHELL /etc/profile If the final or only instance of the UMASK command in /etc/profile is specified as "umask 077", this is not a finding. If the LOGNAME variable is marked read-only (i.e., "readonly LOGNAME") in /etc/profile, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224089`

### Rule: IBM z/OS UNIX security parameters in /etc/rc must be properly specified.

**Rule ID:** `SV-224089r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ISHELL /etc/rc If all of the CHMOD commands in /etc/rc do not result in less restrictive access than what is specified in the tables below, this is not a finding. NOTE: The use of CHMOD commands in /etc/rc is required in most environments to comply with the required settings, especially for dynamic objects such as the /dev directory. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) If all of the CHAUDIT commands in /etc/rc do not result in less auditing than what is specified in the tables below, this is not a finding. NOTE: The use of CHAUDIT commands in /etc/rc may not be necessary. If none are found, there is not a finding. The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing If the _BPX_JOBNAME variable is appropriately set (i.e., to match daemon name) as each daemon (e.g., syslogd, inetd) is started in /etc/rc, this is not a finding. NOTE: If _BPX_JOBNAME is not specified, the started address space will be named using an inherited value. This could result in reduced security in terms of operator command access. SYSTEM DIRECTORY SECURITY SETTINGS DIRECTORY PERMISSION BITS USER AUDIT BITS FUNCTION / [root] 755 faf Root level of all file systems. Holds critical mount points. /bin 1755 fff Shell scripts and executables for basic functions /dev 1755 fff Character-special files used when logging into the OMVS shell and during C language program compilation. Files are created during system IPL and on a per-demand basis. /etc 1755 faf Configuration programs and files (usually with locally customized data) used by z/OS UNIX and other product initialization processes /lib 1755 fff System libraries including dynamic link libraries and files for static linking /samples 1755 fff Sample configuration and other files /tmp 1777 fff Temporary data used by daemons, servers, and users. Note: /tmp must have the sticky bit on to restrict file renames and deletions. /u 1755 fff Mount point for user home directories and optionally for third-party software and other local site files /usr 1755 fff Shell scripts, executables, help (man) files and other data. Contains sub-directories (e.g., lpp) and mount points used by program products that may be in separate file systems. /var 1775 fff Dynamic data used internally by products and by elements and features of z/OS UNIX. SYSTEM FILE SECURITY SETTINGS FILE PERMISSION BITS USER AUDIT BITS FUNCTION /bin/sh 1755 faf z/OS UNIX shell Note: /bin/sh has the sticky bit on to improve performance. /dev/console 740 fff The system console file receives messages that may require System Administrator (SA) attention. /dev/null 666 fff A null file; data written to it is discarded. /etc/auto.master and any mapname files 740 faf Configuration files for automount facility /etc/inetd.conf 740 faf Configuration file for network services /etc/init.options 740 faf Kernel initialization options file for z/OS UNIX environment /etc/log 744 fff Kernel initialization output file /etc/profile 755 faf Environment setup script executed for each user /etc/rc 744 faf Kernel initialization script for z/OS UNIX environment /etc/steplib 740 faf List of MVS data sets valid for set user ID and set group ID executables /etc/table name 740 faf List of z/OS userids and group names with corresponding alias names /usr/lib/cron/at.allow /usr/lib/cron/at.deny 700 faf Configuration files for the at and batch commands /usr/lib/cron/cron.allow /usr/lib/cron/cron.deny 700 faf Configuration files for the crontab command

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-224090`

### Rule: IBM z/OS Default profiles must not be defined in TSS OMVS UNIX security parameters for classified systems.

**Rule ID:** `SV-224090r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system in not classified this is not applicable. From a command line issue the following command: TSS MODIFY STATUS Note: One must have appropriate access to perform this command (have the site security officer to issue command). If system is classified and UNIQUSER is off i.e., (UNIQUSER(OFF) this is not a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-224091`

### Rule: IBM z/OS UNIX security parameters for restricted network service(s) in /etc/inetd.conf must be properly specified.

**Rule ID:** `SV-224091r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the UNIX System Services ISPF Shell enter /etc/inetd.conf If any Restricted Network Services that are listed below are specified or not commented out this is a finding. RESTRICTED NETWORK SERVICES/PORTS Service Port Chargen 19 Daytime 13 Discard 9 Echo 7 Exec 512 finger 79 shell 514 time 37 login 513 smtp 25 timed 525 nameserver 42 systat 11 uucp 540 netstat 15 talk 517 qotd 17 tftp 69

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224092`

### Rule: IBM z/OS attributes of z/OS UNIX user accounts must have a unique GID in the range of 1-99.

**Rule ID:** `SV-224092r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A site can choose to have both an OMVSGRP group and an STCOMVS group or combine the groups under one of these names. If OMVSGRP and/or STCOMVS groups are defined and have a unique GID in the range of 1-99, this is not a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224093`

### Rule: The IBM z/OS user account for the UNIX kernel (OMVS) must be properly defined to the security database.

**Rule ID:** `SV-224093r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If OMVS userid is defined to the ESM as follows, this is not a finding. -No access to interactive on-line facilities (e.g., TSO, CICS, etc.) -Default group specified as OMVSGRP or STCOMVS -UID(0) -HOME directory specified as "/" -Shell program specified as "/bin/sh"

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224094`

### Rule: The IBM z/OS user account for the z/OS UNIX SUPERUSER userid must be properly defined.

**Rule ID:** `SV-224094r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to system PARMLIB member BPXPRMxx (xx is determined by OMVS entry in IEASYS00.) Determine the user ID identified by the SUPERUSER parameter. (BPXROOT is the default). From a command input screen enter: LISTUSER (superuser userid) TSO CICS OMVS If the SUPERUSER userid is defined as follows, this is not a finding: - No access to interactive on-line facilities (e.g., TSO, CICS, etc.) - Default group specified as OMVSGRP or STCOMVS - UID(0) - HOME directory specified as "/" - Shell program specified as "/bin/sh"

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224095`

### Rule: The IBM z/OS user account for the UNIX (RMFGAT) must be properly defined.

**Rule ID:** `SV-224095r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
RMFGAT is the userid for the Resource Measurement Facility (RMF) Monitor III Gatherer. If RMFGAT is not define this is not applicable. From a command input screen enter: TSS LIST (RMFGAT) DATA ALL If RMFGAT is defined as follows, this is not a finding: -Default group specified as OMVSGRP or STCOMVS -A unique, non-zero UID -HOME directory specified as "/" -Shell program specified as "/bin/sh"

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224096`

### Rule: IBM z/OS UID(0) must be properly assigned.

**Rule ID:** `SV-224096r958482_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) SEGMENT(OMVS) If UID(0) is assigned only to system tasks such as the z/OS/ UNIX kernel (i.e., OMVS), z/OS UNIX daemons (e.g., inetd, syslogd, ftpd), and other system software daemons, this is not a finding. If UID(0) is assigned to security administrators who create or maintain user account definitions; and to systems programming accounts dedicated to maintenance (e.g., SMP/E) of HFS-based components, this is not a finding. NOTE: The assignment of UID(0) confers full time superuser privileges. This is not appropriate for personal user accounts. Access to the BPX.SUPERUSER resource is used to allow personal user accounts to gain short-term access to superuser privileges. If UID(0) is assigned to non-systems or non-maintenance accounts, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224097`

### Rule: IBM z/OS UNIX user accounts must be properly defined.

**Rule ID:** `SV-224097r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: This only applies to users of z/OS UNIX (i.e., users with an OMVS profile defined). From the ISPF Command Shell enter: TSS LIST(ACIDS) SEGMENT(OMVS) If any user account is not defined as follows, this is a finding. -A unique UID number (except for UID(0) users). -A unique HOME directory (UID(0), other system task accounts, and tasks approved by the ISSM are excluded from this rule). -Shell program specified as "/bin/sh", "/bin/tcsh", "/bin/echo", or "/bin/false". NOTE: The shell program must have one of the specified values. The HOME directory must have a value (i.e., not be allowed to default; this does not include tasks that are excluded from above).

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-224098`

### Rule: IBM z/OS attributes of UNIX user accounts used for account modeling must be defined in accordance with security requirements.

**Rule ID:** `SV-224098r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: TSS LIST(ACIDS) DATA(NAME) SEGMENT(OMVS) This check applies to any user identifier (ACID) used to model OMVS access on the mainframe. This includes OMVSUSR; MODLUSER, and BPX.UNIQUE.USER. ENTER TSS MODIFY STATUS If ANY MODLUSER is specified then UNIQUSER must be specified as "ON" in the STATUS. If user identifier (ACID) used to model OMVS user account is defined as follows, this is not finding. A non-writable HOME directory Shell program specified as "/bin/echo", or "/bin/false" Note: The shell program must have one of the specified values. The HOME directory must have a value (i.e., not be allowed to default).

## Group: SRG-OS-000024-GPOS-00007

**Group ID:** `V-224099`

### Rule: The IBM z/OS UNIX Telnet server etc/banner file must have the Standard Mandatory DoD Notice and Consent Banner.

**Rule ID:** `SV-224099r958392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-OS-000024-GPOS-00007, SRG-OS-000023-GPOS-00006</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From UNIX System Services ISPF Shell, enter path "/etc/otelnet/banner/". If this file does not contain the banner below, check the UNIX System Services ISPF Shell path /etc/banner. If neither file contains the banner below, this is a finding. If the banner below is contained in either, this is not a finding. This banner is mandatory and deviations are not permitted except as authorized in writing by the DoD Chief Information Officer. The thrust of this new policy is to make it clear that there is no expectation of privacy when using DoD information systems and all use of DoD information systems is subject to searching, auditing, inspecting, seizing, and monitoring, even if some personal use of a system is permitted: STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224100`

### Rule: The IBM z/OS startup user account for the z/OS UNIX Telnet server must be properly defined.

**Rule ID:** `SV-224100r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs cd /etc cat inetd.conf If the "otelnetd" command specifies any user other than "OMVS" or "OMVSKERN", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224101`

### Rule: IBM z/OS HFS objects for the z/OS UNIX Telnet server must be properly protected.

**Rule ID:** `SV-224101r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs At the input line enter: cd /usr enter ls -alW If the following File permission and user Audit Bits are true, this is not a finding. /usr/sbin/otelnetd 1740 fff cd /etc ls -alW If the following file permission and user Audit Bits are true this is not a finding. /etc/banner 0744 faf The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-224102`

### Rule: The IBM z/OS UNIX Telnet server Startup parameters must be properly specified.

**Rule ID:** `SV-224102r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ISHELL Enter /etc/ for a pathname - you may need to issue a CD /etc/ select FILE NAME inetd.conf If Option -D login is included on the otelnetd command, this is not a finding. If Option -c 900 is included on the otelnetd command, this is not a finding. NOTE: "900" indicates a session timeout value of "15" minutes and is currently the maximum value allowed.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-224103`

### Rule: The IBM z/OS UNIX Telnet server warning banner must be properly specified.

**Rule ID:** `SV-224103r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: OMVS cat inetd.conf If the otelnet startup command includes option "-h" this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-224104`

### Rule: IBM z/OS System data sets used to support the VTAM network must be properly secured.

**Rule ID:** `SV-224104r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Create a list of data set names containing all VTAM start options, configuration lists, network resource definitions, commands, procedures, exit routines, all SMP/E TLIBs, and all SMP/E DLIBs used for installation and in development/production VTAM environments. If the ESM data set rules for all VTAM system data sets restrict access to only network systems programming staff, this is not a finding. If RACF data set rules for all VTAM system data sets all READ access to auditors only, this is not a finding. These data sets include libraries containing VTAM load modules and exit routines, and VTAM start options and definition statements.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-224105`

### Rule: IBM z/OS VTAM USSTAB definitions must not be used for unsecured terminals.

**Rule ID:** `SV-224105r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals will be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator to supply the following information: - Documentation regarding terminal naming standards. - Documentation of all procedures controlling terminal logons to the system. - A complete list of all USS commands used by terminal users to log on to the system. - Members and data set names containing USSTAB and LOGAPPL definitions of all terminals that can log on to the system (e.g., SYS1.VTAMLST). - Members and data set names containing logon mode parameters. If USSTAB definitions are only used for secure terminals (e.g., terminals that are locally attached to the host or connected to the host via secure leased lines), this is not a finding. If USSTAB definitions are used for any unsecured terminals (e.g., dial up terminals or terminals attached to the Internet such as TN3270 or KNET 3270 emulation), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245537`

### Rule: The IBM z/OS TCPIP.DATA configuration statement must contain the DOMAINORIGIN or DOMAIN specified for each TCP/IP defined.

**Rule ID:** `SV-245537r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed which would result in query failure or denial of service. Data origin authentication verification must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching Domain Name System (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. This is not applicable if DNSSEC is not implemented on the local network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Data configuration file specified on the SYSTCPD DD statement in the TCPIP started task JCL. Note: If GLOBALTCPIPDATA is specified, any TCPIP.DATA statements contained in the specified file or data set take precedence over any TCPIP.DATA statements found using the appropriate environment's (native MVS or z/OS UNIX) search order. If GLOBALTCPIPDATA is not specified, the appropriate environment's (Native MVS or z/OS UNIX) search order is used to locate TCPIP.DATA. If the DOMAINORIGIN/DOMAIN (The DOMAIN statement is functionally equivalent to the DOMAINORIGIN Statement) is specified in the TCP/IP Data configuration file, this is not a finding.

## Group: SRG-OS-000404-GPOS-00183

**Group ID:** `V-251108`

### Rule: The IBM z/OS systems requiring data at rest protection must properly employ IBM DS8880 or equivalent hardware solutions for full disk encryption.

**Rule ID:** `SV-251108r1028298_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control addresses the confidentiality and integrity of information at rest and covers user information and system information. Information at rest refers to the state of information when it is located on storage devices as specific components of information systems. Operating systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000405-GPOS-00184, SRG-OS-000404-GPOS-00183, SRG-OS-000396-GPOS-00176 </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if IBM's DS880 Disks or equivalent hardware solutions are in use. If IBMs DS880 Disks or equivalent hardware solutions are not in use for systems that require "data at rest", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-252554`

### Rule:  IBM z/OS TCP/IP AT-TLS policy must be properly configured in Policy Agent.

**Rule ID:** `SV-252554r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If events associated with nonlocal administrative access or diagnostic sessions are not logged, a major tool for assessing and investigating attacks would not be available. This requirement addresses auditing-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational information systems. Nonlocal maintenance and diagnostic activities are conducted by individuals communicating through an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are carried out by individuals physically present at the information system or information system component and not communicating across a network connection. This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system; for example, the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the z/OS UNIX pasearch -t command to query information from the z/OS UNIX Policy Agent. The command is issued from the UNIX System Services shell. Examine the results for AT-TLS initiation and control statements. If there are no AT-TLS initiation and controls statements, this is a finding. Verify the statements specify a FIPS 140-2 compliant value. If none of the following values are present, this is a finding ECDHE_ECDSA_AES_128_CBC_SHA256 ECDHE_ECDSA_AES_256_CBC_SHA384 ECDHE_RSA_AES_128_CBC_SHA256 ECDHE_RSA_AES_256_CBC_SHA384 TLS_RSA_WITH_3DES_EDE_CBC_SHA TLS_RSA_WITH_AES_128_CBC_SHA TLS_RSA_WITH_AES_128_CBC_SHA256 TLS_RSA_WITH_AES_256_CBC_SHA TLS_RSA_WITH_AES_256_CBC_SHA256

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-255896`

### Rule: IBM z/OS FTP.DATA configuration statements for the FTP Server must be specified in accordance with requirements.

**Rule ID:** `SV-255896r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is intended to cover both traditional interactive logons to information systems and general accesses to information systems that occur in other types of architectural configurations (e.g., service-oriented architectures).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Data configuration file specified on the SYSFTPD DD statement in the FTP started task JCL. If the UMASK statement is coded with a value of "077", this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-255940`

### Rule: IBM Integrated Crypto Service Facility (ICSF) Configuration parameters must be correctly specified.

**Rule ID:** `SV-255940r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Integrated Crypto Service Facility (ICSF) product has the ability to use privileged functions and/or have access to sensitive data. Failure to properly configure parameter values could potentially the integrity of the base product which could result in compromising the operating system or sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the CSFPRMxx member in the logical PARMLIB concatenation. If the configuration parameters are specified as follows this is not a finding. REASONCODES(ICSF) COMPAT(NO) SSM(NO) SSM can be dynamically set by defining the CSF.SSM.ENABLE SAF profile within the XFACILIT resource Class. If this profile is not limited to authorized personnel this is a finding. CHECKAUTH(YES) FIPSMODE(YES,FAIL(YES)) AUDITKEYLIFECKDS (TOKEN(YES),LABEL(YES)). AUDITKEYLIFEPKDS (TOKEN(YES),LABEL(YES)). AUDITKEYLIFETKDS (TOKENOBJ(YES),SESSIONOBJ(YES)). AUDITKEYUSGCKDS (TOKEN(YES),LABEL(YES),INTERVAL(n)). AUDITKEYUSGPKDS (TOKEN(YES),LABEL(YES),INTERVAL(n)). AUDITPKCS11USG (TOKENOBJ(YES),SESSIONOBJ(YES),NOKEY(YES),INTERVAL(n)). DEFAULTWRAP -This parameter can be determined by the site. ENHANCED wrapping specifies the new X9.24 compliant CBC wrapping is used. If DEFAULTWRAP is not specified, the default wrapping method will be ORIGINAL for both internal and external tokens. Starting with ICSF FMID HCR77C0, the value for this option can be updated without restarting ICSF by using either the SETICSF command or the ICSF Multi-Purpose service. If this access is not restricted to appropriate personnel, this is a finding. (Note: Other options may be site defined.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-255941`

### Rule: IBM Integrated Crypto Service Facility (ICSF) install data sets are not properly protected.

**Rule ID:** `SV-255941r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Integrated Crypto Service Facility (ICSF) product has the ability to use privileged functions and/or have access to sensitive data. Failure to properly restrict access to their data sets could result in violating the integrity of the base product which could result in compromising the operating system or sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that access to the IBM IntegrTated Crypto Service Facility (ICSF) install data sets are properly restricted. Execute a data set list of access to the IBM Integrated Crypto Service Facility (ICSF) install data sets If the TSS data set rules for the data sets does not restrict UPDATE and/or ALL access to systems programming personnel this is a finding. If the TSS data set rules for the data sets does not specify that all (i.e., failures and successes) UPDATE and/or ALL access will be logged this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-255942`

### Rule: IBM Integrated Crypto Service Facility (ICSF) Started Task name is not properly identified / defined to the system ACP.

**Rule ID:** `SV-255942r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Integrated Crypto Service Facility (ICSF) requires a started task that will be restricted to certain resources, datasets and other system functions. By defining the started task as a userid to the system ACP, It allows the ACP to control the access and authorized users that require these capabilities. Failure to properly control these capabilities, could compromise of the operating system environment, ACP, and customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the IBM Integrated Crypto Service Facility (ICSF) STC/Batch ACID(s) for the following: ___ Is defined with Facility of STC and/or BATCH. ___ Is sourced to the INTRDR. c) If all of the above are true this is not a finding d) If any of the above is untrue this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-255943`

### Rule: IBM Integrated Crypto Service Facility (ICSF) Started task(s) must be properly defined to the Started Task Table ACID for Top Secret.

**Rule ID:** `SV-255943r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access to product resources should be restricted to only those individuals responsible for the application connectivity and who have a requirement to access these resources. Improper control of product resources could potentially compromise the operating system, ACP, and customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
from the ISPF Command Shell enter TSS LIST(STC) If the IBM Integrated Crypto Service Facility (ICSF) started task(s) is (are) not defined in the TSS STC record this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-255944`

### Rule: IBM Integrated Crypto Service Facility (ICSF) STC data sets must be properly protected.

**Rule ID:** `SV-255944r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Integrated Crypto Service Facility (ICSF) STC data sets have the ability to use privileged functions and/or have access to sensitive data. Failure to properly restrict access to their data sets could result in violating the integrity of the base product which could result in compromising the operating system or sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that access to the IBM Integrated Crypto Service Facility (ICSF) STC data sets are properly restricted. The data sets to be protected are identified in the data set referenced in the CSFPARM DD statement of the ICSF started task(s) and/or batch job(s); the entries for CKDSN and PKDSN specify the data sets. If the following guidance is true, this is not a finding. If the TSS data set access authorizations do not restrict READ access to auditors, this is a finding. If the TSS data set access authorizations do not restrict WRITE and/or greater access to systems programming personnel, this is a finding. If the TSS data set access authorizations do not restrict WRITE and/or greater access to the product STC(s) and/or batch job(s), this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-272878`

### Rule: IBM z/OS DFSMS control data sets must reside on separate storage volumes.

**Rule ID:** `SV-272878r1082860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the logical parmlib data sets, for example SYS1.PARMLIB(IGDSMSxx), to identify the fully qualified file names for the following SMS data sets: Active Control Data Set (ACDS) Communications Data Set (COMMDS) If the COMMDS and ACDS SMS data sets identified above reside on different volumes, this is not a finding. If the COMMDS and ACDS SMS data sets identified above are collocated on the same volume, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-275959`

### Rule: zOSMF resource class(es) must be properly owned in accordance with security requirements.

**Rule ID:** `SV-275959r1115946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
OSMF resource class(es) must be properly owned in accordance with security requirements. From the ISPF command shell, enter: TSS WHOOWNS <CLASS> If each of the following classes are properly owned, this is not a finding. EJBROLE LOGSTRM SERVER TSOPROC ZMFAPLA ZMFCLOUD

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-275960`

### Rule: zOSMF resources must be protected in accordance with security requirements.

**Rule ID:** `SV-275960r1115947_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF command shell, enter WHOOWNS for the following resources: CRYPTOZ CSFKEYS CSFSERV GCSFKEYS XCSFKEY For each resource defined, enter: TSS <resource name> (*) If TSS access rules for each resource is restricted to appropriate users, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-275961`

### Rule: ICSF resource class(es) must be properly owned in accordance with security requirements.

**Rule ID:** `SV-275961r1115951_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF command shell, enter: TSS WHOOWNS <CLASS> If each of the following classes are properly owned, this is not a finding: CRYPTOZ CSFKEYS CSFSERV GCSFKEYS XCSFKEY

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-275962`

### Rule: ICSF resources must be protected in accordance with security requirements.

**Rule ID:** `SV-275962r1115949_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF command shell, enter WHOOWNS for the following resources: CRYPTOZ CSFKEYS CSFSERV GCSFKEYS XCSFKEY For each resource defined, enter: TSS <resource name> (*) If TSS access rules for each resource is restricted to appropriate users, this is not a finding.

