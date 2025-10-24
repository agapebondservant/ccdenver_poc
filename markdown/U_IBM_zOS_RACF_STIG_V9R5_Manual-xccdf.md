# STIG Benchmark: IBM z/OS RACF Security Technical Implementation Guide

---

**Version:** 9

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223646`

### Rule: Certificate Name Filtering must be implemented with appropriate authorization and documentation.

**Rule ID:** `SV-223646r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Currently the RACDCERT command does not support a generic userid value of ID(*) LISTMAP to list all the certificate name filters defined to RACF. However, the following commands can be issued to determine if certificate name filtering may be implemented. If certificate name filtering is in use, collect documentation describing each active filter rule and written approval from the ISSM to use the rule. Issue the SETROPTS LIST command. If the DIGTNMAP resource class is active, RACF is ready to process any certificate name filters with a Status of TRUST. The DIGTNMAP resource class should not be active unless certificate name filtering is desired. If the DIGTNMAP resource class is not active, this is not a finding. Certificate name filters are stored as profiles in the DIGTNMAP resource class. The RLIST command is not intended for use with profiles in the DIGTNMAP resource class. However it can be used to determine if any profiles are defined. (NOTE: The information will not be displayed in a suitable format to easily interpret the filter.) RLIST DIGTNMAP * If there is nothing to list in the DIGTNMAP resource class, this is not a finding. If profile information is displayed, one or more certificate name filters are defined to RACF. Under the NAME heading of each profile listing is the userid the filter is being mapped to. Issue the following command the list the certificate name filter associated with each userid: RACDCERT ID(profile name userid) LISTMAP NOTE: Certificate name filters are only valid when their Status is TRUST. Therefore, you may ignore filters with the NOTRUST status. If the DIGTNMAP resource class is active and certificate name filters have a Status of TRUST, certificate name filtering is in use. If certificate name filtering is in use and filtering rules have been documented and approved by the ISSM, this is not a finding. If certificate name filtering is in use and filtering rules have not been documented and approved by the ISSM, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-223647`

### Rule: Expired digital certificates must not be used.

**Rule ID:** `SV-223647r958448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The longer and more often a key is used, the more susceptible it is to loss or discovery. This weakens the assurance provided to a relying Party that the unique binding between a key and its named subscriber is valid. Therefore, it is important that certificates are periodically refreshed. This is in accordance with DoD requirement. Expired Certificate must not be in use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RACDCERT CERTAUTH LIST If no certificate information is found, this is not a finding. NOTE: Certificates are only valid when their Status is TRUST. Therefore, you may ignore certificates with the NOTRUST status during the following check. Check the expiration (End Date) for each certificate with a status of TRUST. If the expiration date has passed, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-223648`

### Rule: All digital certificates in use must have a valid path to a trusted certification authority (CA).

**Rule ID:** `SV-223648r998341_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The origin of a certificate, or the CA, is crucial in determining if the certificate should be trusted. An approved CA establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000403-GPOS-00182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RACDCERT CERT AUTH If no certificate information is found, this is not a finding. NOTE: Certificates are only valid when their Status is TRUST. Therefore, you may ignore certificates with the NOTRUST status during the following check. If the digital certificate information indicates that the issuer's distinguished name leads to one of the following, this is not a finding: a) A DOD PKI Root Certification Authority b) An External Root Certification Authority (ECA) c) An approved External Partner PKI's Root Certification Authority The DOD Cyber Exchange website contains information as to which certificates maybe acceptable (https://public.cyber.mil/pki-pke/interoperability/ or https://cyber.mil/pki-pke/interoperability/). Examples of an acceptable DOD CA are: DOD PKI Class 3 Root CA DOD PKI Med Root CA

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223649`

### Rule: IBM RACF must limit Write or greater access to SYS1.NUCLEUS to system programmers only.

**Rule ID:** `SV-223649r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This data set contains a large portion of the system initialization (IPL) programs and pointers to the master and alternate master catalog. Unauthorized access could result in the compromise of the operating system environment, ACP, and customer data. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset access list for SYS1.NUCLEUS. If all of the Following are untrue, this is not a finding. If any of the following is true, this is a finding. -The ACP data set rules for SYS1.NUCLEUS do not restrict WRITE or greater access to only z/OS systems programming personnel. -The ACP data set rules for SYS1.NUCLEUS do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223650`

### Rule: IBM RACF must limit Write or greater access to libraries that contain PPT modules to system programmers only.

**Rule ID:** `SV-223650r958472_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Specific PPT designated program modules possess significant security bypass capabilities. Unauthorized access could result in the compromise of the operating system environment, ACP, and customer data. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review program entries in the IBM Program Properties Table (PPT). You may use a third-party product to examine these entries however, to determine program entries issue the following command from an ISPF command line: TSO ISRDDN LOAD IEFSDPPT Press Enter. For each module identified in the "eyecatcher" if all of the following are untrue, this is not a finding. If any of the following is true, this is a finding. -The ACP data set rules for libraries that contain PPT modules do not restrict WRITE or greater access to only z/OS systems programming personnel. -The ACP data set rules for libraries that contain PPT modules do not specify that all WRITE or greater access will be logged.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-223652`

### Rule: IBM RACF emergency USERIDs must be properly defined.

**Rule ID:** `SV-223652r958508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by the organization's system administrators when network or normal logon/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for a list of all emergency userids available to the site along with the associated function of each userid. If there are no emergency logonids defined ask the system administrator for an alternate documented procedure to handle emergencies. If there are no emergency logonids and no documented emergency procedure this is a finding. Execute an access list for each emergency userid. If emergency userids exist at a minimum an emergency logonid will exist with the security administration attributes specified in accordance with the following requirements. If the following guidance is not true, this is a finding. At least one userid exists to perform RACF security administration. These userids are defined to RACF with the system-SPECIAL attribute. They must not have the OPERATIONS attribute. If any userids exist to perform operating system functions, they are defined without any RACF security administration privileges. These userids are defined to RACF with the system-OPERATIONS attribute, and FULL access to all DASD volumes. They must not have the SPECIAL attribute. NOTE: A user who has the system-OPERATIONS attribute has FULL access authorization to all RACF-protected resources in the DASDVOL/GDASDVOL resource classes. However, if their userid or any associated group (i.e., default or connect) is in the access list of a resource profile, they will only have the access specified in the access list. All emergency userids are defined to RACF and SYS1.UADS. All emergency logonid/logonid(s) are to be implemented with logging to provide an audit trail of their activities. This is accomplished with the UAUDIT attribute. All emergency logonid/logonid(s) will have distinct, different passwords in SYS1.UADS and in RACF, and the site is to establish procedures to ensure that the passwords differ. The password for any ID in SYS1.UADS is never to match the password for the same ID in RACF. All emergency logonid/logonid(s) will have documented procedures to provide a mechanism for the use of the IDs. Their release for use is to be logged, and the log is to be maintained by the ISSO. When an emergency logonid is released for use, its password is to be reset by the ISSO within 12 hours.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-223653`

### Rule: IBM RACF SETROPTS LOGOPTIONS must be properly configured.

**Rule ID:** `SV-223653r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000392-GPOS-00172, SRG-OS-000458-GPOS-00203, SRG-OS-000461-GPOS-00205, SRG-OS-000462-GPOS-00206, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209, SRG-OS-000466-GPOS-00210, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218, SRG-OS-000474-GPOS-00219, SRG-OS-000475-GPOS-00220, SRG-OS-000476-GPOS-00221, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Evaluate the impact associated with implementation of the control option. Develop a plan of action to implement the control option as specified in the example below: Verify that the following LOGOPTIONS are specified: LOGOPTIONS "FAILURES" CLASSES = <all the classes listed in the "ACTIVE" class as a minimum> LOGOPTIONS "NEVER" CLASSES = NONE The other LOGOPTIONS may be site determined. If the LOGOPTIONS are not set as described above, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223654`

### Rule: IBM RACF must protect memory and privileged program dumps in accordance with proper security requirements.

**Rule ID:** `SV-223654r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a resource access list for the IEAABD. resources. If the IEAABD. resource and/or generic equivalent is defined with no access and all access logged, this is not a finding. If the IEAABD.DMPAUTH. resource and/or generic equivalent is defined with READ access limited to authorized users, this is not a finding. If the IEAABD.DMPAUTH. resource and/or generic equivalent WRITE or greater access is restricted to only systems personnel and all access is logged, this is not a finding. If the IEAABD.DMPAKEY resource and/or generic equivalent is defined and all access is restricted to systems personnel and that all access is logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223655`

### Rule: IBM z/OS system commands must be properly protected.

**Rule ID:** `SV-223655r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>z/OS system commands provide a method of controlling the operating environment. Failure to properly control access to z/OS system commands could result in unauthorized personnel issuing sensitive system commands. This exposure may threaten the integrity and availability of the operating system environment, and compromise the confidentiality of customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RList OPERCMDS * If the MVS.** resource is defined to the OPERCMDS class with an access of NONE and all (i.e., failures and successes) access logged, this is not a finding. If the access to z/OS system commands defined in the table entitled MVS commands, RACF access authorities, and resource names, in the IBM z/OS MVS System Commands manual, is restricted to the appropriate personnel (e.g., operations staff, systems programming personnel, general users) as determined in the Documented site Security Plan, this is not a finding. Note: Display commands and others as deemed by the site IAW site security plan may be allowed for all users with no logging. The (MVS.SEND) Command will not be a finding if used by all. If all access (i.e., failures and successes) to specific z/OS system commands is logged as indicated in the table entitled MVS commands, RACF access authorities, and resource names, in the z/OS MVS System Commands, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223656`

### Rule: IBM RACF must properly define users that have access to the CONSOLE resource in the TSOAUTH resource class.

**Rule ID:** `SV-223656r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MCS consoles can be used to issue operator commands. Failure to properly control access to MCS consoles could result in unauthorized personnel issuing sensitive operator commands. This exposure may threaten the integrity and availability of the operating system environment, and compromise the confidentiality of customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the CONSOLE privilege is not defined to the TSOAUTH resource class, this is not a finding. At the discretion of the site, users may be allowed to issue z/OS system commands from a TSO session. With this in mind, review the following items for users granted the CONSOLE resource in the TSOAUTH resource class: If Userids are restricted to the INFO level on the AUTH parameter specified in the OPERPARM segment of their userid, this is not a finding. If Userids are restricted to READ access to the MVS.MCSOPER.userid resource defined in the OPERCMDS resource class, this is not a finding. If Userids and/or group IDs are restricted to READ access to the CONSOLE resource defined in the TSOAUTH resource class, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223657`

### Rule: The IBM RACF FACILITY resource class must be active.

**Rule ID:** `SV-223657r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Provides the FACILITY Class for use in protecting a variety of features/functions/products both IBM and third-party. The FACILITY Class is not dedicated to any one specific use and is intended as a multi-purpose RACF Class. Failure to activate this class will result in unprotected resources. This exposure may threaten the integrity of the operating system environment, and compromise the confidentiality of customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The RACF Command SETR LIST will show the status of RACF Controls including a list of ACTIVE classes. From the ISPF Command Shell enter: SETRopts List If the FACILITY resource class is active, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223658`

### Rule: The IBM RACF OPERCMDS resource class must be active.

**Rule ID:** `SV-223658r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The RACF Command SETR LIST will show the status of RACF Controls including a list of ACTIVE classes. From the ISPF Command Shell enter: SETRopts List If the OPERCMDS resource class is active, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223659`

### Rule: The IBM RACF MCS consoles resource class must be active.

**Rule ID:** `SV-223659r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The RACF Command SETR LIST will show the status of RACF Controls including a list of ACTIVE classes. From the ISPF Command Shell enter: SETRopts List If the CONSOLE resource class is active, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223660`

### Rule: IBM RACF CLASSACT SETROPTS must be specified for the TEMPDSN class.

**Rule ID:** `SV-223660r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The RACF Command SETR LIST will show the status of RACF Controls including a list of ACTIVE classes. From the ISPF Command Shell enter: SETRopts List If the TEMPDSN resource class is ACTIVE, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223661`

### Rule: IBM RACF started tasks defined with the trusted attribute must be justified.

**Rule ID:** `SV-223661r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trusted Started tasks bypass RACF checking. It is vital that this attribute is NOT granted to unauthorized Started Tasks which could then obtain unauthorized access to the system. This could result in the compromise of the confidentiality, integrity, and availability of the operating system, ACP, or customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the list of z/OS started tasks and address spaces in the IBM z/OS MVS Initialization and Tuning Reference. If the only approved Started Tasks that have the TRUSTED flag enabled are in this list, this is not a finding. If there are no Started Tasks that have been granted the PRIVILEGED attribute, this is not a finding. Guidelines for reference: Assign the TRUSTED attribute when one of the following conditions applies: - The started procedure or address space creates or accesses a wide variety of unpredictably named data sets within your installation. - Insufficient authority to an accessed resource might risk an unsuccessful IPL or other system problem. Avoid assigning TRUSTED to a z/OS started procedure or address space unless it is listed here or you are instructed to do so by the product documentation. Additionally external security managers are candidates for trusted attribute. Any other started tasks not listed or not covered by the guidelines are a finding unless approval by the Authorizing Official.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223662`

### Rule: IBM RACF USERIDs possessing the Tape Bypass Label Processing (BLP) privilege must be justified.

**Rule ID:** `SV-223662r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RLIST FACILITY ICHBLP AUTHUSER If access authorization to the ICHBLP resource is restricted at the userid level to data center personnel (e.g., tape librarian, operations staff, etc.), this is not a finding. If no tape management system (e.g., CA-1) is installed the following: From the ISPF Command Shell enter: SETROPTS LIST If the TAPEVOL class is active, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223663`

### Rule: IBM RACF DASD volume-level protection must be properly defined.

**Rule ID:** `SV-223663r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RLIST DASDVOL AUTHUSER If a profile of "**" is defined for the "DASDVOL" resource class, this is not finding. If access authorization to "DASDVOL" profiles is restricted to Storage Management Personnel, Storage Management Batch Userids, and Systems Programmers, this is not a finding. If all (i.e., failures and successes) access is logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223664`

### Rule: IBM Sensitive Utility Controls must be properly defined and protected.

**Rule ID:** `SV-223664r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the RACF resource access authorizations for the following sensitive utilities restrict access to the appropriate personnel according to the site security plan, this is not a finding. If all access for these sensitive utilities is audited, this is not a finding. Sensitive Utility Controls Program Product Function AHLGTF z/OS System Activity Tracing HHLGTF IHLGTF ICPIOCP z/OS System Configuration IOPIOCP IXPIOCP IYPIOCP IZPIOCP BLSROPTR z/OS Data Management DEBE OS/DEBE Data Management DITTO OS/DITTO Data Management FDRZAPOP FDR Product Internal Modification GIMSMP SMP/E Change Management Product ICKDSF z/OS DASD Management IDCSC01 z/OS IDCAMS Set Cache Module IEHINITT z/OS Tape Management IFASMFDP z/OS SMF Data Dump Utility IND$FILE z/OS PC to Mainframe File Transfer (Applicable only for classified systems) CSQJU003 IBM WebSphereMQ CSQJU004 CSQUCVX CSQ1LOGP CSQUTIL WHOIS z/OS Share MOD to identify user name from USERID. Restricted to data center personnel only.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223665`

### Rule: IBM RACF Global Access Checking must be restricted to appropriate classes and resources.

**Rule ID:** `SV-223665r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a command input screen enter: RL Global * If Global * is specified in SETROPTS, this is a finding. The following entries may be allowed with the approval of the ISSM: Dataset Class - ALTER access level to &RACUID.** (Allows users all access to their own datasets) OPERCMDS Class - READ access to MVS.MCSOPER.&RACUID (Allows users access to console for their jobs) JESJOBS Class - ALTER access to CANCEL.*.*.&RACUID (Allows users to cancel their own jobs) JESJOBS Class - ALTER access to SUBMIT.*.*.&RACUID (Allows users to submit their own jobs) The ISSM may allow other classes to be included after evaluation with the system programmer. If any other members are included for Global Access Checking, this is a finding. If written approval by the ISSM is not provided, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223666`

### Rule: IBM RACF access to the System Master Catalog must be properly protected.

**Rule ID:** `SV-223666r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to SYSCATxx member of SYS1.NUCLEUS. Multiple SYSCATxx members may be defined. If so, refer to Master Catalog message for IPL. If the member is not found, refer to the appropriate LOADxx member of SYS1.PARMLIB. If data set rules for the Master Catalog do not restrict greater than "READ" access to only z/OS systems programming personnel, this is a finding. If Products or procedures requiring system programmer access for system-level maintenance meet the following specific case, this is not a finding: - The batch job or procedure must be documented in the SITE Security Plan. - Reside in a data set that is restricted to systems programmers' access only. If dataset rules for the Master Catalog do not specify that all (i.e., failures and successes) greater than "READ" access will be logged, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223667`

### Rule: IBM RACF must limit Write or greater access to SYS1.UADS to system programmers only, and WRITE or greater access must be limited to system programmer personnel and/or security personnel.

**Rule ID:** `SV-223667r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The ESM data set rules for SYS1.UADS restrict WRITE or Greater access to only z/OS systems programming personnel. The ESM data set rules for SYS1.UADS restrict READ and/or UPDATE access to z/OS systems programming personnel and/or security personnel. The ESM data set rules for SYS1.UADS restrict READ access to auditors as documented in Security Plan. The ESM data set rules for SYS1.UADS specify that all (i.e., failures and successes) data set access authorities (i.e., READ, UPDATE, ALTER, and CONTROL) will be logged. If all of the above are untrue, this is not a finding. If any of the above is true, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223668`

### Rule: IBM z/OS must protect dynamic lists in accordance with proper security requirements.

**Rule ID:** `SV-223668r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute RACF command: RLIST FACILITY * If the RACF resources and/or generic equivalent identified below are defined with AUDIT(ALL(READ)) and WRITE or greater access restricted to system programming personnel, this is not a finding. CSVAPF. CSVAPF.MVS.SETPROG.FORMAT.DYNAMIC CSVAPF.MVS.SETPROG.FORMAT.STATIC CSVDYLPA. CSVDYNEX. CSVDYNEX.LIST CSVDYNL. CSVDYNL.UPDATE.LNKLST CSVLLA. If the RACF CSVDYNEX.LIST resource and/or generic equivalent is defined with AUDIT(FAILURE(READ)SUCCESS(UPDATE)) and WRITE or greater access restricted to system programming personnel, this is not a finding. If the RACF CSVDYNEX.LIST resource and/or generic equivalent is defined with READ access restricted to auditors, this is not a finding. If the products CICS and/or CONTROL-O are on the system, the RACF access to the CSVLLA resource and/or generic equivalent will be defined with AUDIT(ALL) and UPDATE access restricted to the CICS and CONTROL-O STC userids. If any software product requires access to dynamic LPA updates on the system, the RACF access to the CSVDYLPA resource and/or generic equivalent will be defined with LOG and SERVICE(UPDATE) only after the product has been validated with the appropriate STIG or SRG for compliance AND receives documented and filed authorization that details the need and any accepted risks from the site ISSM or equivalent security authority. Note: In the above, UPDATE access can be substituted with ALTER or CONTROL. Review the permissions in the IBM documentation when specifying UPDATE.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223669`

### Rule: IBM RACF allocate access to system user catalogs must be properly protected.

**Rule ID:** `SV-223669r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: LISTCat USERCATALOG ALL NOPREFIX Review the ESM data set rules for each usercatalog defined. If the data set rules for User Catalogs do not restrict ALTER access to only z/OS systems programming personnel, this is a finding. If Products or procedures requiring system programmer access for system-level maintenance meets the following specific case, this is not a finding: - The batch job or procedure must be documented in the SITE Security Plan. - Reside in a data set that is restricted to systems programmers' access only. If the data set rules for User Catalogs do not specify that all (i.e., failures and successes) ALTER access will be logged, this a finding. Note: If the USER CATALOGS contain SMS managed data sets READ access is sufficient to allow user operations. If the USER CATALOGS do not contain SMS managed data sets UPDATE access is required for user operation.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223670`

### Rule: IBM RACF must limit WRITE or greater access to System backup files to system programmers and/or batch jobs that perform DASD backups.

**Rule ID:** `SV-223670r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Collect from the storage management group the identification of the DASD backup files and all associated storage management userids. If ESM data set rules for system DASD backup files do not restrict WRITE or greater access to z/OS systems programming and/or batch jobs that perform DASD backups, this is a finding. If READ Access to system backup data sets is not limited to auditors and others approved by the ISSM, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223671`

### Rule: IBM RACF must limit access to SYS(x).TRACE to system programmers only.

**Rule ID:** `SV-223671r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access for SYS(x).TRACE files. If the ESM data set rule for SYS1.TRACE restricts access to systems programming personnel and started tasks that perform GTF processing, this is not a finding. If the ESM data set rule for SYS1.TRACE restricts access to others as documented and approved by ISSM, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223672`

### Rule: IBM RACF batch jobs must be properly secured.

**Rule ID:** `SV-223672r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Batch jobs that are submitted to the operating system should inherit the USERID of the submitter. This will identify the batch job with a userid for the purpose of accessing resources. BATCHALLRACF ensures that a valid USERID is associated with batch jobs. Jobs that are submitted to the operating system via a scheduling facility must also be identified to the system. Without a batch job having an associated USERID, access to system resources will be limited. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000326-GPOS-00126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the documentation of the processes used for submission of batch jobs via an automated process (i.e., scheduler or other sources) and each of the associated userids. Determine any other scheduled batch jobs on the system. From an ISPF Command Shell enter: RLIST SURROGAT * If each batch job userid used for batch submission by a Job Scheduler (e.g., CONTROL-M, CA-7, CA-Scheduler, etc.) is defined as an execution-userid in a SURROGAT resource class profile, this is not a finding. From an ISPF Command Shell enter: RLIST SURROGAT <surrogat-userid> ALL If the Job Scheduler userids (i.e., surrogate-userid) are permitted surrogate authority to the appropriate SURROGAT profiles, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223673`

### Rule: IBM RACF batch jobs must be protected with propagation control.

**Rule ID:** `SV-223673r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000326-GPOS-00126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to a list all Multiple User Access Systems in use on this system. These are systems that run in a single address space, but allow multiple users to sign on to them (e.g., CICS regions, Session Managers, etc.). For each region, also include corresponding userids, profiles, data management files, and a brief description (of each region). Refer to the documentation of the processes used for submission of batch jobs via an automated process (i.e., scheduler or other sources) and each of the associated userids. If the submission of batch jobs via an automated process (e.g., job scheduler, job submission started task, etc.) is being utilized, and/or Multiple User Single Address Space Systems (MUSASS) capable of submitting batch jobs are active on this system and the following items are in effect, this is not a finding. The PROPCNTL resource class is active. A PROPCNTL resource class profile is defined for each userid associated with a job scheduler (e.g., CONTROL-M, CA-7, etc.) and a MUSASS able to submit batch jobs (e.g., CA-ROSCOE, etc.).

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223674`

### Rule: IBM RACF must limit Write or greater access to SYS1.IMAGELIB to system programmers only.

**Rule ID:** `SV-223674r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access for SYS1.IMAGELIB. If the following guidance is true, this is not a finding. -The ACP data set rules for SYS1.IMAGELIB do not restrict WRITER or greater access to only systems programming personnel. -The ACP data set rules for SYS1.IMAGELIB do not specify that all (i.e., failures and successes) WRITER or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223675`

### Rule: IBM RACF must limit Write or greater access to SYS1.SVCLIB to appropriate authorized users.

**Rule ID:** `SV-223675r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access for SYS1.SVCLIB. If all of the following are true, this is not a finding. If any of the following are untrue, this is a finding. -ESM data set rules for SYS1.SVCLIB restrict WRITE or greater access to only z/OS systems programming personnel. -ESM data set rules for SYS1.SVCLIB specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223676`

### Rule: IBM RACF must limit Write or greater access to SYS1.LPALIB to system programmers only.

**Rule ID:** `SV-223676r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access for SYS1.LPALIB. If any of the following is true, this is a finding. -The ESM data set rules for SYS1.LPALIB do not restrict WRITE or greater access to only z/OS systems programming personnel. -The ESM data set rules for SYS1.LPALIB do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223677`

### Rule: IBM z/OS libraries included in the system REXXLIB concatenation must be properly protected.

**Rule ID:** `SV-223677r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to AXRxx member of PARMLIB, for each REXXLIB ADD statement: If the ESM data set rules for libraries in the REXXLIB concatenation restrict WRITE or greater access to only z/OS systems programming personnel, this is not a finding. If ESM dataset rules for libraries in the REXXLIB concatenation restrict GLOBAL read access, this is not a finding. If ESM data set rules for libraries in the REXXLIB concatenating restrict WRITE or Greater access to z/OS system Programmers, this is not a finding. If the ESM data set rules for libraries in the REXXLIB concatenation restrict READ access to the following, this is not a finding. -Appropriate Started Tasks -Auditors -User-id defined in PARMLIB member AXR00 AXRUSER(user-id) If the ESM data set rules for libraries in the REXXLIB concatenation specify that all (i.e., failures and successes) WRITE or greater access will be logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223678`

### Rule: IBM RACF must limit write or greater access to all LPA libraries to system programmers only.

**Rule ID:** `SV-223678r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From Any ISPF input line, enter: TSO ISRDDN LPA. If any of the following is true, this is a finding. -The ACP data set rules for LPA libraries do not restrict WRITE or greater access to only z/OS systems programming personnel. -The ACP data set rules for LPA libraries do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223679`

### Rule: IBM RACF must limit Write or greater access to libraries containing EXIT modules to system programmers only.

**Rule ID:** `SV-223679r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the system for active exit modules. The system administrator may have to help for this. Third-party software products can determine standard and dynamic exits loaded in the system. If all the exits are found within APF, LPA, and LINKLIST, this is Not Applicable. If ESM data set rules for libraries that contain system exit modules restrict WRITE or greater access to only z/OS systems programming personnel, this is not a finding. If the ESM data set rules for libraries that contain exit modules specify that all WRITE or greater access will be logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223680`

### Rule: IBM RACF must limit WRITE or greater access to all system-level product installation libraries to system programmers.

**Rule ID:** `SV-223680r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the systems programmer for z/OS supply the following information: The data set name and associated SREL for each SMP/E CSI utilized to maintain this system. The data set name of all SMP/E TLIBs and DLIBs used for installation and production support. A comprehensive list of the SMP/E DDDEFs for all CSIs may be used if valid. If the ESM data set rules for system-level product installation libraries (e.g., SMP/E CSIs) do not restrict WRITE or greater access to only z/OS systems programming personnel this is a finding. If any of these data sets cannot be identified due to a lack of requested information, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223681`

### Rule: IBM RACF must limit access to SYSTEM DUMP data sets to system programmers only.

**Rule ID:** `SV-223681r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator and/or DASD administrator to determine the System Dump data sets. Refer to data sets SYS1.DUMPxx, additionally, Dump data sets can be identified by reviewing the logical parmlib concatenation data sets for the current COMMNDxx member. Find the COM= which specifies the DUMPDS NAME (DD NAME=name-pattern) entry. The name-pattern is used to identify additional Dump data sets. If ESM data set rules for System Dump data sets do not restrict READ, UPDATE, and/or ALTER access to only systems programming personnel, this is a finding. If ESM data set rules for all System Dump data sets do not restrict READ access to personnel having justification to review these dump data, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223682`

### Rule: IBM RACF must limit WRITE or greater access to all APF-authorized libraries to system programmers only.

**Rule ID:** `SV-223682r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From Any ISPF input line, enter TSO ISRDDN APF. If all of the following are untrue, this is not a finding. If any of the following are true, this is a finding. -The ACP data set rules for APF libraries do not restrict WRITE or greater access to only z/OS systems programming personnel. -The ACP data set rules for APF libraries do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223683`

### Rule: IBM RACF access to SYS1.LINKLIB must be properly protected.

**Rule ID:** `SV-223683r998342_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125, SRG-OS-000362-GPOS-00149</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access to SYS1.LINKLIB. If the ESM data set rules for SYS1.LINKLIB allow inappropriate (e.g., global READ) access, this is a finding. If data set rules for SYS1.LINKLIB do not restrict READ, UPDATE, and ALTER access to only systems programming personnel, this is a finding. If data set rules for SYS1.LINKLIB do not restrict READ and UPDATE access to only domain level security administrators, this is a finding. If data set rules for SYS1.LINKLIB do not restrict READ access to only system Level Started Tasks, authorized Data Center personnel, and auditors, this is a finding. If data set rules for SYS1.LINKLIB do not specify that all (i.e., failures and successes) UPDATE and/or ALTER access will be logged, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223684`

### Rule: The IBM RACF System REXX IRRPWREX security data set must be properly protected.

**Rule ID:** `SV-223684r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Operating systems restrict access to security functions through the use of access control mechanisms and by implementing least privilege capabilities. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000134-GPOS-00068, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the zOS system REXXLIB concatenation found in SYS1. PARMLIB (AXR) for the data set that contains the REXX for Password exit named IRRPWREX and the defined AXRUSER. If the following guidance is true, this is not a finding. -RACF data set access authorizations restrict READ to AXRUSER, z/OS systems programming personnel, security personnel, and auditors. -RACF data set access authorizations restrict UPDATE to security personnel using a documented change management procedure to provide a mechanism for access and revoking of access after use. -All (i.e., failures and successes) data set access authorities (i.e., READ, UPDATE, and CONTROL) is logged. -RACF data set access authorizations specify UACC(NONE) and NOWARNING.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223685`

### Rule: IBM RACF security data sets and/or databases must be properly protected.

**Rule ID:** `SV-223685r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The External Security Manager (ESM) database files contain all access control information for the operating system environment and system resources. Unauthorized access could result in the compromise of the operating system environment, ACP, and customer data. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000134-GPOS-00068, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following accesses to the ESM security data sets and/or databases are properly restricted as detailed below, this is not a finding. -The ESM data set rules for ESM security data sets and/or databases restrict READ access to auditors and DASD batch. -The ESM data set rules for ESM security data sets and/or databases restrict READ and/or greater access to z/OS systems programming personnel, security personnel, and/or batch jobs that perform ESM maintenance. All (i.e., failures and successes) data set access authorities (i.e., READ, UPDATE, ALTER, and CONTROL) for ESM security data sets and/or databases are logged.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223686`

### Rule: IBM RACF must limit access to data sets used to back up and/or dump SMF collection files to appropriate users and/or batch jobs that perform SMF dump processing.

**Rule ID:** `SV-223686r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000206-GPOS-00084, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the procedures and collection specifics for SMF datasets and backup. If the ESM data set rules for the SMF dump/backup files do not restrict WRITE or greater to authorized DISA and site personnel (e.g., systems programmers and batch jobs that perform SMF processing), this is a finding. If the ESM dataset rules for the SMF dump/backup files do not restrict update access as documented in the site security plan, this is a finding. If the ESM data set rules for the SMF dump/backup files do not restrict READ access to auditors and others approved by the ISSM, this is a finding. If the ESM data set rules for SMF dump/backup files do not specify that all (i.e., failures and successes) WRITE or greater will be logged, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223687`

### Rule: IBM RACF must limit all system PROCLIB data sets to system programmers only.

**Rule ID:** `SV-223687r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the following for the PROCLIB data sets that contain the STCs and TSO logons from the following sources: - MSTJCLxx member used during an IPL. The PROCLIB data sets are obtained from the IEFPDSI and IEFJOBS DD statements. - PROCxx DD statements and JES2 Dynamic PROCLIBs where 'xx' is the PROCLIB entries for the STC and TSU JOBCLASS configuration definitions. Verify the accesses to the above PROCLIB data sets are properly restricted. If the following guidance is true, this is not a finding. If the ESM data set access authorizations restrict READ access to all authorized users, this is not a finding. If the ESM data set access authorizations restrict WRITE and/or greater access to systems programming personnel, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223688`

### Rule: IBM RACF must limit access to System page data sets (i.e., PLPA, COMMON, and LOCALx) to system programmers.

**Rule ID:** `SV-223688r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access for System page data sets (i.e., PLPA, COMMON, and LOCALx). If ESM data set rules for system page data sets (PLPA, COMMON, and LOCAL) restrict access to only systems programming personnel, this is not a finding. If ESM data set rules for system page data sets (PLPA, COMMON, and LOCAL) restrict auditors to READ only, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223689`

### Rule: IBM z/OS MCS consoles access authorization(s) for CONSOLE resource(s) must be properly protected.

**Rule ID:** `SV-223689r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MCS consoles can be used to issue operator commands. Failure to properly control access to MCS consoles could result in unauthorized personnel issuing sensitive operator commands. This exposure may threaten the integrity and availability of the operating system environment, and compromise the confidentiality of customer data. Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the CONSOLxx member of SYS1.PARMLIB.console is defined to RACF with a corresponding profile in the CONSOLE resource class. If each console is defined to RACF with a corresponding profile in the CONSOLE resource class, this is not a finding. If the userid associated with each console has READ access to the corresponding resource defined in the CONSOLE resource class, this is not a finding. If access authorization for CONSOLE resources restricts READ access to operations and system programming personnel or authorized personnel, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223690`

### Rule: IBM RACF must limit WRITE or greater access to the JES2 System data sets (e.g., Spool, Checkpoint, and Initialization parameters) to system programmers only.

**Rule ID:** `SV-223690r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The ESM data set rules for the JES2 System data sets (e.g., Spool, Checkpoint, and Initialization parameters) do not restrict WRITE or greater access to only z/OS systems programming personnel. The ESM data set rules for the JES2 System data sets (e.g., Spool, Checkpoint, and Initialization parameters) allow inappropriate access not documented and approved by ISSO. If both of the above are untrue, this is not a finding. If either of the above is true, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223691`

### Rule: The IBM z/OS IEASYMUP resource must be protected in accordance with proper security requirements.

**Rule ID:** `SV-223691r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: Search all Class(Facility) MASK(ieasymup) For each entity found enter: RL facility <entity> If RACF resources are defined with a default access of NONE, this is not a finding. If RACF resource access authorizations restrict UPDATE and/or greater access to appropriate personnel (i.e., DASD administrators, Tape Library personnel, and system programming personnel), this is not a finding. If RACF resource logging requirements are specified for UPDATE and/or greater access, this is not a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-223692`

### Rule: The IBM RACF JES(BATCHALLRACF) SETROPTS value must be set to JES(BATCHALLRACF).

**Rule ID:** `SV-223692r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From ISPF Command Shell enter: SETRopts List If the JES(BATCHALLRACF) is enabled then the message "JES-BATCHALLRACF OPTION IS ACTIVE" will be displayed, this is not a finding. If the message "JES-BATCHALLRACF OPTION IS INACTIVE" is displayed, this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-223693`

### Rule: The IBM z/OS JES(XBMALLRACF) SETROPTS value must be set to JES(XBMALLRACF).

**Rule ID:** `SV-223693r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts List If the JES(XBMALLRACF) is enabled then the message "JES-XBMALLRACF OPTION IS ACTIVE" will be displayed, this is not a finding. If the message "JES-XBMALLRACF OPTION IS INACTIVE" is displayed, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-223694`

### Rule: IBM RACF OPERAUDIT SETROPTS value must set to OPERAUDIT.

**Rule ID:** `SV-223694r958732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts List If the OPERAUDIT value is listed as one of the ATTRIBUTES, this is not a finding. If the OPERAUDIT value is not listed as one of the ATTRIBUTES, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-223695`

### Rule: The IBM RACF PASSWORD(REVOKE) SETROPTS value must be specified to revoke the userid after three invalid logon attempts.

**Rule ID:** `SV-223695r1050760_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts List If the PASSWORD(REVOKE) value shows "AFTER <n> CONSECUTIVE UNSUCCESSFUL PASSWORD ATTEMPTS, A USERID WILL BE REVOKED." where <n> is either "1" or "2", this is not a finding. If the PASSWORD(REVOKE) value is not enabled and is not set to either "1" or "2", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-223697`

### Rule: IBM z/OS SYS1.PARMLIB must be properly protected.

**Rule ID:** `SV-223697r998344_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. SYS1.PARMLIB contains the parameters that control audit configuration. Unauthorized access could result in the compromise of the operating system environment, ACP, and customer data. Satisfies: SRG-OS-000063-GPOS-00032, SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125, SRG-OS-000337-GPOS-00129, SRG-OS-000362-GPOS-00149</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset list of access to SYS1.PARMLIB. If the ESM data set rules for SYS1.PARMLIB allow inappropriate (e.g., global READ) access, this is a finding. If data set rules for SYS1.PARMLIB do not restrict READ, WRITE or greater access to only systems programming personnel, this is a finding. If data set rules for SYS1.PARMLIB do not restrict READ and UPDATE access to only domain level security administrators, this is a finding. If data set rules for SYS1.PARMLIB do not restrict READ access to only system Level Started Tasks, authorized Data Center personnel, and auditors, this is a finding. If data set rules for SYS1.PARMLIB do not specify that all (i.e., failures and successes) UPDATE and/or ALTER access will be logged, this is a finding.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-223699`

### Rule: The IBM RACF SETROPTS SAUDIT value must be specified.

**Rule ID:** `SV-223699r991577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETROPTS LIST If the SAUDIT value is listed as one of the ATTRIBUTES, this is not a finding. If the NOSAUDIT value is listed as one of the ATTRIBUTES, this is a finding.

## Group: SRG-OS-000255-GPOS-00096

**Group ID:** `V-223700`

### Rule: The IBM RACF REALDSN SETROPTS value must be specified.

**Rule ID:** `SV-223700r991556_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts list If the REALDSN is enabled then the message "REAL DATA SET NAMES OPTION IS ACTIVE" will be displayed, this is not a finding. If the message "REAL DATA SET NAMES OPTION IS INACTIVE" is displayed, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-223701`

### Rule: IBM z/OS must limit access for SMF collection files (i.e., SYS1.MANx) to appropriate users and/or batch jobs that perform SMF dump processing.

**Rule ID:** `SV-223701r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMF data collection is the system activity journaling facility of the z/OS system. Unauthorized access could result in the compromise of logging and recording of the operating system environment, ESM, and customer data. Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000256-GPOS-00097, CCI-001494, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099, SRG-OS-000080-GPOS-00048, SRG-OS-000206-GPOS-00084, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the SMFPRMxx member in SYS1.PARMLIB. Determine the SMF and/or Logstream dataset name. If the following statements are true, this is not a finding. The ESM data set rules for the SMF data collection files (e.g., SYS1.MAN* or IFASMF.SYS1.*) restrict ALTER or greater access to only z/OS systems programming personnel. The ESM data set rules for the SMF data collection files (e.g., SYS1.MAN* or IFASMF.SYS1.*) restrict UPDATE or greater access to z/OS systems programming staff and/or batch jobs that perform SMF dump processing and others approved by the ISSM. The ESM data set rules for the SMF data collection files (e.g., SYS1.MAN* or IFASMF.SYS1.*) restrict READ access to auditors and others approved by the ISSM. The ESM data set rules for SMF data collection files (e.g., SYS1.MAN* or IFASMF.SYS1.*) specify that all (i.e., failures and successes) UPDATE and/or ALTER accesses are logged.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-223702`

### Rule: IBM RACF SETROPTS RVARYPW values must be properly set.

**Rule ID:** `SV-223702r958796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to system configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the operating system can have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to operating system components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETROPTS LIST If the "INSTALLATION DEFINED RVARY PASSWORD IS IN EFFECT" message for both the SWITCH and STATUS functions, this is not a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-223703`

### Rule: IBM RACF must define WARN = NO on all profiles.

**Rule ID:** `SV-223703r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all Dataset and resource profiles in the RACF database. If any are not defined with WARN = NO, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223704`

### Rule: The IBM RACF PROTECTALL SETROPTS value specified must be properly set.

**Rule ID:** `SV-223704r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETROPTS LIST If the SETROPTS values for PROTECTALL is ACTIVE and set to FAIL, this is not a finding. If the SETROPTS PROTECTALL parameter is set to NOPROTECTALL or PROTECTALL(WARNING), this is a finding. Additional analysis may be required to determine whether this finding should be downgraded to a Category II or remain a Category I. Example of a Category I finding where not a further analysis is required: Control Options: SETROPTS NOPROTECTALL Example of a possible Category I finding requiring additional analysis: Control Options: SETROPTS PROTECTALL(WARNING) PROTECTALL(WARNING) allows access to a data set only if it is not at protected by a profile in the DATASET resource class. Therefore if all sensitive data sets are properly protected by profiles in the DATASET resource class, PROTECTALL(WARNING) will not at allow unauthorized access. This situation allows for a downgrade to a Category II.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223705`

### Rule: The IBM RACF GRPLIST SETROPTS value must be set to ACTIVE.

**Rule ID:** `SV-223705r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETROPTS LIST If the GRPLIST is enabled then the message "LIST OF GROUPS ACCESS CHECKING IS ACTIVE." will be displayed, this is not a finding. If the message indicates that LIST OF GROUPS is NOT ACTIVE, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223706`

### Rule: The IBM RACF RETPD SETROPTS value specified must be properly set.

**Rule ID:** `SV-223706r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETROPTS LIST If the RETPD is enabled then the message "SECURITY RETENTION PERIOD IN EFFECT IS NEVER-EXPIRES DAYS" will be displayed, this is not a finding. If the RETPD value is not set to "NEVER-EXPIRES", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223707`

### Rule: The IBM RACF TAPEDSN SETROPTS value specified must be properly set.

**Rule ID:** `SV-223707r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETROPTS LIST If the TAPEDSN is enabled then the message "TAPE DATA SET PROTECTION IS ACTIVE" will be displayed, this is not a finding. NOTE 1: TAPEDSN should be active for domains without a tape management product. NOTE 2: For domains running CA 1, Computer Associates recommends that TAPEDSN be active and CA 1 parameter OCEOV be set to OFF. If the TAPEDSN value is set to INACTIVE, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223708`

### Rule: The IBM RACF WHEN(PROGRAM) SETROPTS value specified must be active.

**Rule ID:** `SV-223708r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETROPTS LIST If the WHEN(PROGRAM) value is listed as one of the ATTRIBUTES, this is not a finding. If the NOWHEN(PROGRAM) value is listed as one of the ATTRIBUTES, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223709`

### Rule: IBM RACF use of the AUDITOR privilege must be justified.

**Rule ID:** `SV-223709r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ListUser * If authorization to the SYSTEM AUDITOR attribute is restricted to auditing and/or security personnel, this is not a finding. If at minimum, any users connected to sensitive system dataset HLQ (e.g., SYS1, SYS2, etc.) groups or general resource owning groups with the Group-AUDITOR attribute are Auditor and/or Security personnel, this is not a finding. Otherwise, Group-AUDITOR is allowed.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223710`

### Rule: The IBM RACF database must be on a separate physical volume from its backup and recovery datasets.

**Rule ID:** `SV-223710r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the RACDST report from DSMON Utility using 'RACF PRIMARY' and 'RACF BACKUP' as selection criteria. If the security database and its backup exist on the same volume, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223711`

### Rule: The IBM RACF database must be backed up on a scheduled basis.

**Rule ID:** `SV-223711r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator to determine that procedures exist to back up the security data base and files. Have the system administrator identify the dataset names and frequency of the backups. If, based on the information provided, it can be determined that the ESM database is being backed up on a regularly scheduled basis, this is not a finding. If it cannot be determined that the ESM database is being backed up on a regularly scheduled basis, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223712`

### Rule: IBM z/OS Batch job user IDs must be properly defined.

**Rule ID:** `SV-223712r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the documentation of the processes used for submission of batch jobs via an automated process (i.e., scheduler or other sources) and each of the associated user IDs. From the ISPF COMMAND INPUT screen enter: LISTUSER(each identified batch job) The following USERID record fields/attributes must be specified: NAME PROTECTED No USERID has the LAST-ACCESS field set to UNKNOWN. If both of the above are true, this is not a finding. If either of the USERID record fields/attributes (NAME and/or PROTECTED) are blank and/or the LAST ACCESS field is set to unknown, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223713`

### Rule: IBM RACF use of the RACF SPECIAL Attribute must be justified.

**Rule ID:** `SV-223713r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must perform a periodic scan/review of the application (as required by CCI-000384) and disable functions, ports, protocols, and services deemed to be unneeded or non-secure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ListUser * If authorization to the SYSTEM SPECIAL attribute is restricted to key systems personnel such as individuals responsible for continuing operations, Storage Management, and emergency recovery, this is not a finding. If any users connected to sensitive system dataset HLQ (e.g., SYS1, SYS2, ETC) groups with the Group-SPECIAL are key systems personnel, such as individuals responsible for continuing operations, Storage Management, and emergency recovery, this is a finding. Otherwise, Group-SPECIAL is allowed.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223714`

### Rule: IBM RACF assignment of the RACF OPERATIONS attribute to individual userids must be fully justified.

**Rule ID:** `SV-223714r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is intended to cover both traditional interactive logons to information systems and general accesses to information systems that occur in other types of architectural configurations (e.g., service-oriented architectures).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ListUser * If authorization to the SYSTEM OPERATIONS attribute is restricted to key systems personnel such as individuals responsible for continuing operations, Storage Management, and emergency recovery, this is not a finding. If any users connected to sensitive system dataset HLQ (e.g., SYS1, SYS2, ETC) groups with the Group-OPERATIONS are key systems personnel, such as individuals responsible for continuing operations, Storage Management, and emergency recovery, this is a finding. Otherwise, Group-OPERATIONS is allowed.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-223715`

### Rule: IBM z/OS must properly configure CONSOLxx members.

**Rule ID:** `SV-223715r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. MCS consoles can be used to issue operator commands. Failure to properly control access to MCS consoles could result in unauthorized personnel issuing sensitive operator commands. This exposure may threaten the integrity and availability of the operating system environment, and compromise the confidentiality of customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review each CONSOLxx parmlib member. If the following guidance is true, this is not a finding. The "DEFAULT" statement for each CONSOLxx member specifies "LOGON(REQUIRED)" or "LOGON(AUTO)". The "CONSOLE" statement for each console assigns a unique name using the "NAME" parameter. The "CONSOLE" statement for each console specifies "AUTH(INFO)". Exceptions are the "AUTH" parameter is not valid for consoles defined with "UNIT(PRT)" and specifying "AUTH(MASTER)" is permissible for the system console. Note: The site should be able to determine the system consoles. However, it is imperative that the site adhere to the "DEFAULT" statement requirement.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-223716`

### Rule: IBM z/OS must properly protect MCS console userid(s).

**Rule ID:** `SV-223716r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. MCS consoles can be used to issue operator commands. Failure to properly control access to MCS consoles could result in unauthorized personnel issuing sensitive operator commands. This exposure may threaten the integrity and availability of the operating system environment, and compromise the confidentiality of customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 to determine correct CONSOLxx member. Examine the CONSOLxx member. Verify that the MCS console userids are properly restricted. If the following guidance is true, this is not a finding. Each console defined in the currently active CONSOLxx parmlib member in EXAM.RPT(PARMLIB) is associated with a valid RACF userid. Each console userid has no special privileges and/or attributes (e.g., SPECIAL, OPERATIONS, etc.). Each console userid has no accesses to interactive on-line facilities (e.g., TSO, CICS, etc.; excluding VTAM SMCS consoles). Each console userid will be restricted from accessing all data sets and resources except MVS.MCSOPER.consolename in the OPERCMDS resource class and console name in the CONSOLE resource class. Each console userid has the RACF default group that is an appropriate console group profile. NOTE: If LOGON(AUTO) is specified in the currently active CONSOLxx parmlib member, additional access may be required. Permissions for the console userids and/or console group may be given with access READ to MVS.CONTROL, MVS.DISPLAY, MVS.MONITOR, and MVS.STOPMN OPERCMDS resource. NOTE: Execute the JCL in CNTL(IRRUT100) using the RACF console userids as SYSIN input. This report lists all occurrences of these userids within the RACF database, including data set and resource access lists.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223717`

### Rule: IBM RACF users must have the required default fields.

**Rule ID:** `SV-223717r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensure that Every USERID is uniquely identified to the system. Within the USERID record, the user's name, default group, the owner, and the user's passdate or phrasedate fields are completed. This will uniquely identify each user. If these fields are not completed for each user, user accountability will become lost. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a z/OS command screen enter: ListUser * Examine each user entry verify every user is fully identified with all of the following conditions: -A completed NAME field that can either be traced back to a current DD2875 or a Vendor Requirement (example: A Started Task). -The presence of the DEFAULT-GROUP and OWNER fields. -The PASSDATE field or the PHRASEDATE field accordingly is not set to N/A excluding users with the PROTECTED attribute. If all of the above are true, this is not a finding. If any of above is untrue, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223718`

### Rule: IBM interactive USERIDs defined to RACF must have the required fields completed.

**Rule ID:** `SV-223718r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Interactive users are considered to be users of CICS, IMS, TSO/E, NetView, or other products that support logging on at a terminal. Improper assignments of attributes in the LOGONID record for interactive users may allow users excessive privileges resulting in unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a z/OS command screen enter: ListUser * Examine each user entry that has either TSO, CICS, ROSCOE, IMS, or any other products that support logging on at a terminal. If every user is fully identified with all of the following condition, this is not a finding. -Each interactive userid has a valid LAST-ACCESS date that does not contain the value UNKNOWN. -Each interactive userid has PASS-INTERVAL define and set to a value of 60 days. Note: FTP only process and server to server userids may have PASSWORD(NOINTERVAL) specified. These users must be identified in the FTPUSERS group in the Dialog Process or FTP in the name field. Additionally these users must change their passwords on an annual basis.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223719`

### Rule: IBM z/OS Started Tasks must be properly identified and defined to RACF.

**Rule ID:** `SV-223719r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Started procedures have system generated job statements that do not contain the user, group, or password statements. To enable the started procedure to access the same protected resources that users and groups access, started procedures must have an associated USERID. If a USERID is not associated with the started procedure, the started procedure will not have access to the resources. To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the site security plan, the system administrator, and system libraries to determine list of stated tasks available on the system. If each Started task procedure identified has a unique associated userid or STC userid that is unique per product and function, this is not a finding. If any of the following are untrue, this is a finding. -All started task userids are connected to a valid STC group ID. -Only userids associated with STCs are connected to STC group IDs. -All STC userids are defined with the PROTECTED attribute. From the ISPF Command Shell enter: RL STARTED (Alternately execute RACF DSMON utility for the RACSPT report) If all of the following is true, this is not a finding, If any of the following is untrue, this is a finding. -A generic catch all profile of ** is defined to the STARTED resource class. -The STC group associated with the ** profile is not granted any explicit data set or resource access authorizations. -The STC userid associated with the ** profile is not granted any explicit dataset or resource access authorizations and is defined with the RESTRICTED attribute. Note: Execute the JCL in CNTL(IRRUT100) using the STC group associated with the ** profile as SYSIN input. This report lists all occurrences of this group within the RACF database, including data set and resource access lists. Execute RACF utility DSMON RACSPT report. If the ICHRIN03 started procedures table is not maintained to support recovery efforts in the event the STARTED resource class is deactivated or critical STC profiles are deleted, this is a finding. If STCs critical to support this recovery effort (e.g., JES2, VTAM, TSO, etc.) are not maintained in ICHRIN03 to reflect the current STARTED resource class profiles, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223721`

### Rule: The IBM RACF Automatic Data Set Protection (ADSP) SETROPTS value must be set to NOADSP.

**Rule ID:** `SV-223721r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETROPTS LIST If the ADSP value is NOT IN EFFECT, this is not a finding. Note: NOADSP is the required setting. In the SETROPTS LIST output this will display as AUTOMATIC DATASET PROTECTION IS NOT IN EFFECT. If the ADSP value is IN EFFECT, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223722`

### Rule: IBM RACF user accounts must uniquely identify system users.

**Rule ID:** `SV-223722r998345_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the UNIX OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the UNIX and Windows operating systems offer a "switch user" capability allowing users to authenticate with their individual credentials and, when needed, switch to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000109-GPOS-00056, SRG-OS-000125-GPOS-00065, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of all userids that are shared among multiple users (i.e., not uniquely identified system users). If there are no shared userids on this domain, this is not a finding. If there are shared userids on this domain, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-223723`

### Rule: The IBM RACF INACTIVE SETROPTS value must be set to 35 days.

**Rule ID:** `SV-223723r998346_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a z/OS command input screen enter: List SETRopts If the INACTIVE value is set properly In the message "INACTIVE USERIDS ARE BEING AUTOMATICALLY REVOKED AFTER xxx DAYS.", where xxx is a value "35" or less, this is not a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-223724`

### Rule: IBM RACF PASSWORD(RULEn) SETROPTS value(s) must be properly set.

**Rule ID:** `SV-223724r998347_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000078-GPOS-00046</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts If the following options are specified, this is not a finding. Every PASSWORD(RULE) under "INSTALLATION PASSWORD SYNTAX RULES" is defined with the values shown below: RULE n LENGTH(8) xxxxxxxx The following options are in effect under "PASSWORD PROCESSING OPTIONS": "MIXED CASE PASSWORD SUPPORT IS IN EFFECT" "SPECIAL CHARACTERS ARE ALLOWED."

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-223725`

### Rule: IBM RACF exit ICHPWX01 must be installed and properly configured.

**Rule ID:** `SV-223725r998349_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Satisfies: SRG-OS-000070-GPOS-00038, SRG-OS-000071-GPOS-00039, SRG-OS-000072-GPOS-00040, SRG-OS-000266-GPOS-00101, SRG-OS-000480-GPOS-00225</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a system console screen, issue the following modify command: F AXR,IRRPWREX LIST Review the results of the modify command. If the following options are listed, this is not a finding. -The number of required character types is 4 (ensures that at least one uppercase, one lowercase, one number, and one special character is used in password) -The user's name cannot be contained in the password. (Only three consecutive characters of the user's name are allowed) -The minimum word length checked is eight. -The user ID cannot be contained in the password. (Only three consecutive characters of the user ID are allowed) -Only three unchanged positions of the current password are allowed. (These positions need to be consecutive to cause a failure and this check is not case sensitive) -No more than zero pairs of repeating characters are allowed. (This check is not case sensitive) -A minimum list of 33 restricted prefix strings is being checked: APPL APR AUG ASDF BASIC CADAM DEC DEMO FEB FOCUS GAME IBM JAN JUL JUN LOG MAR MAY NET NEW NOV OCT PASS ROS SEP SIGN SYS TEST TSO VALID VTAM XXX 1234 If the modify command fails or returns the following message in the system log, this is a finding. IRX0406E REXX exec load file REXXLIB does not contain exec member IRRPWREX.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-223726`

### Rule: The IBM RACF SETROPTS PASSWORD(MINCHANGE) value must be set to 1.

**Rule ID:** `SV-223726r998350_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts List If the PASSWORD(MINCHANGE) value shows PASSWORD MINIMUM CHANGE INTERVAL IS <1> DAYS, this is not a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-223727`

### Rule: IBM RACF SETROPTS PASSWORD(INTERVAL) must be set to 60 days.

**Rule ID:** `SV-223727r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised. INTERVAL specifies the maximum number of days that each user's password is valid. When a user logs on to the system, RACF compares the system password interval value specified in the user profile. RACF uses the lower of the two values to determine if the users password has expired.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts List If the PASSWORD(INTERVAL) value is set properly and the message is PASSWORD CHANGE INTERVAL IS 060 DAYS, this is not a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-223728`

### Rule: The IBM RACF PASSWORD(HISTORY) SETROPTS value must be set to five or more.

**Rule ID:** `SV-223728r998354_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. HISTORY specifies the number of previous passwords that RACF saves for each USERID and compares with an intended new password. If there is a match with one of the previous passwords, or with the current password, RACF rejects the intended new password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts List If the PASSWORD(HISTORY) value is set properly then the message x GENERATIONS OF PREVIOUS PASSWORDS BEING MAINTAINED, where x is a minimum of "5", this is not a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-223729`

### Rule: NIST FIPS-validated cryptography must be used to protect passwords in the security database.

**Rule ID:** `SV-223729r998355_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000074-GPOS-00042, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts List If the following is specified under PASSWORD PROCESSING OPTIONS: THE ACTIVE PASSWORD ENCRYPTION ALGORITHM IS KDFAES, this is not a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-223731`

### Rule: The IBM RACF ERASE ALL SETROPTS value must be set to ERASE(ALL) on all systems.

**Rule ID:** `SV-223731r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts List For all systems, if the ERASE values are set as follows, this is not a finding. ERASE-ON-SCRATCH IS ACTIVE, CURRENT OPTIONS: ERASE-ON-SCRATCH FOR ALL DATA SETS IS IN EFFECT

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223732`

### Rule: IBM RACF DASD Management USERIDs must be properly controlled.

**Rule ID:** `SV-223732r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to non-SMS volumes. For SMS-Managed volumes this is Not Applicable. Ask the system administrator for all documents and procedures that apply to Storage Management, including identification of the DASD backup data sets and associated storage management userids. From the ISPF Command enter: RL User for each identified Userid. Review storage management userids, if the following guidance is true, this is not a finding. Storage management userids will not be given the "OPERATIONS" attribute. Storage management userids will be defined with the "PROTECTED" attribute. Storage management userids are permitted to the appropriate "STGADMIN" profiles in the "FACILITY" class for SMS-managed volumes. Storage management userids assigned to storage management tasks (e.g., volume backup, data set archive and restore, etc.) are given access to data sets using "DASDVOL" and/or "GDASDVOL" profiles for non-SMS-managed volumes. NOTE: "DASDVOL" profiles will not work with SMS-managed volume. "FACILITY" class profiles must be used instead. If "DFSMS/MVS" is used to perform DASD management operations, "FACILITY" class profiles may also be used to authorize storage management operations to non-SMS-managed volumes in lieu of using "DASDVOL" profiles. Therefore, not all volumes may be defined to the "DASDVOL/GDASDVOL" resource classes, and not all storage management userids may be represented in the profile access lists.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-223733`

### Rule: IBM z/OS SMF recording options for the FTP Server must be configured to write SMF records for all eligible events.

**Rule ID:** `SV-223733r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The FTP Server can provide audit data in the form of SMF records. The SMF data produced by the FTP Server provides transaction information for both successful and unsuccessful FTP commands. Failure to collect and retain audit data may contribute to the loss of accountability and hamper security audit activities. Satisfies: SRG-OS-000032-GPOS-00013, SRG-OS-000392-GPOS-00172</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If FTPDATA is configured with the following SMF statements, this is not a finding. FTP.DATA Configuration Statements SMF TYPE119 SMFJES TYPE119 SMFSQL TYPE119 SMFAPPE [Not coded or commented out] SMFDEL [Not coded or commented out] SMFEXIT [Not coded or commented out] SMFLOGN [Not coded or commented out] SMFREN [Not coded or commented out] SMFRETR [Not coded or commented out] SMFSTOR [Not coded or commented out]

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223734`

### Rule: IBM RACF permission bits and user audit bits for HFS objects that are part of the FTP server component must be properly configured.

**Rule ID:** `SV-223734r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MVS data sets of the FTP Server provide the configuration and operational characteristics of this product. Failure to properly secure these data sets may lead to unauthorized access resulting in the compromise of the integrity and availability of customer data and some system services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs At the input line enter: cd /usr/sbin/ enter ls -alW If the following File permission and user Audit Bits are true, this is not a finding. /usr/sbin/ftpd 1740 fff /usr/sbin/ftpdns 1755 fff /usr/sbin/tftpd 0644 faf cd ls -alW If the following file permission and user Audit Bits are true, this is not a finding. /etc/ftp.data 0744 faf /etc/ftp.banner 0744 faf NOTES: Some of the files listed above are not used in every configuration. The absence of a file is not considered a finding. The /usr/sbin/ftpd and /usr/sbin/ftpdns objects are symbolic links to /usr/lpp/tcpip/sbin/ftpd and /usr/lpp/tcpip/sbin/ftpdns respectively. The permission and user audit bits on the targets of the symbolic links must have the required settings. The /etc/ftp.data file may not be the configuration file the server uses. It is necessary to check the SYSFTPD DD statement in the FTP started task JCL to determine the actual file. The TFTP Server does not perform any user identification or authentication, allowing any client to connect to the TFTP Server. Due to this lack of security, the TFTP Server will not be used. The TFTP Client is not secured from use. The permission bits for /usr/sbin/tftpd should be set to 644. The /etc/ftp.banner file may not be the banner file the server uses. It is necessary to check the BANNER statement in the FTP Data configuration file to determine the actual file. Also, the permission bit setting for this file must be set as indicated in the table above. A more restrictive set of permissions is not permitted. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223735`

### Rule: IBM z/OS data sets for the FTP server must be properly protected.

**Rule ID:** `SV-223735r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MVS data sets of the FTP Server provide the configuration and operational characteristics of this product. Failure to properly secure these data sets may lead to unauthorized access resulting in the compromise of the integrity and availability of customer data and some system services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the FTP server Started task (usually FTPD). Refer to the dataset defined on the SYSFTPD DD statement. If WRITE and ALLOCATE access to the data set containing the FTP Data configuration file is restricted to systems programming personnel, this is not a finding. Note: READ access to all authenticated users is permitted. If WRITE and ALLOCATE access to the data set containing the FTP Data configuration file is logged, this is not a finding. If WRITE and ALLOCATE access to the data set containing the FTP banner file is restricted to systems programming personnel, this is not a finding. Note: READ access to the data set containing the FTP banner file is permitted to all authenticated users. Notes: The MVS data sets mentioned above are not used in every configuration. Absence of a data set will not be considered a finding. The data set containing the FTP Data configuration file is determined by checking the SYSFTPD DD statement in the FTP started task JCL. The data set containing the FTP banner file is determined by checking the BANNER statement in the FTP Data configuration file.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-223736`

### Rule: IBM z/OS FTP.DATA configuration statements must indicate a BANNER statement with the proper content.

**Rule ID:** `SV-223736r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000024-GPOS-00007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the FTP.DATA file specified on the SYSFTPD DD statement in the FTP started task JCL. The SYSFTPD DD statement is optional. The search order for FTP.DATA is: /etc/ftp.data SYSFTPD DD statement jobname.FTP.DATA SYS1.TCPPARMS(FTPDATA) tcpip.FTP.DATA Examine the BANNER statement. Ensure the BANNER statement in the FTP Data configuration file specifies an HFS file or data set that contains a logon banner with the Standard Mandatory DoD Notice and Consent Banner. The below banner is mandatory and deviations are not permitted except as authorized in writing by the DoD Chief Information Officer. The thrust of this new policy is to make it clear that there is no expectation of privacy when using DoD information systems and all use of DoD information systems is subject to searching, auditing, inspecting, seizing, and monitoring, even if some personal use of a system is permitted: STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. If the BANNER statement in the FTP Data configuration file does not specify an HFS file or z/OS data set that contains the Standard Mandatory DoD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-223737`

### Rule: IBM z/OS FTP.DATA configuration statements for the FTP server must specify the BANNER statement.

**Rule ID:** `SV-223737r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Data configuration file specified on the SYSFTPD DD statement in the FTP started task JCL. If the BANNER statement is coded, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223739`

### Rule: IBM z/OS FTP.DATA configuration statements for the FTP Server must be specified in accordance with requirements.

**Rule ID:** `SV-223739r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is intended to cover both traditional interactive logons to information systems and general accesses to information systems that occur in other types of architectural configurations (e.g., service-oriented architectures).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Data configuration file specified on the SYSFTPD DD statement in the FTP started task JCL. If the UMASK statement is coded with a value of 077, this is not a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-223740`

### Rule: The IBM z/OS TFTP server program must be properly protected.

**Rule ID:** `SV-223740r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RL Program * If Program resources TFTPD and EZATD are defined to the PROGRAM resource class with a UACC(NONE), this is not a finding. The library name where these programs are located is SYS1.TCPIP.SEZALOAD. If no access to the program resources TFTPD and EZATD is permitted, this is not a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-223741`

### Rule: IBM z/OS user exits for the FTP server must not be used without proper approval and documentation.

**Rule ID:** `SV-223741r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Several user exit points in the FTP Server component are available to permit customization of its operating behavior. These exits can be used to modify functions such as FTP command usage, client connection controls, post processing tasks, and SMF record modifications. Without proper review and adequate documentation of these exit programs, undesirable operations and degraded security may result. This exposure could lead to unauthorized access impacting data integrity or the availability of some system services, or contribute to the loss of accountability and hamper security audit activities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Data configuration file specified on the SYSFTPD DD statement in the FTP started task JCL. Refer to the file(s) allocated by the STEPLIB DD statement in the FTP started task JCL. Refer to the libraries specified in the system Linklist and LPA. If any FTP Server exits are in use, identify them and validate that they were reviewed for integrity and approved by the site AO. If the following items are in effect for FTP Server user exits, this is not a finding: The FTCHKCMD, FTCHKIP, FTCHKJES, FTCHKPWD, FTPSMFEX, and FTPOSTPR modules are not located in the FTP daemon's STEPLIB, Linklist, or LPA. NOTE: The ISPF ISRFIND utility can be used to search the system Linklist and LPA for specific modules.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223742`

### Rule: The IBM z/OS FTP server daemon must be defined with proper security parameters.

**Rule ID:** `SV-223742r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The FTP Server daemon requires special privileges and access to sensitive resources to provide its system services. Failure to properly define and control the FTP Server daemon could lead to unauthorized access. This exposure may result in the compromise of the integrity and availability of the operating system environment, ACP, and customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From z/OS command screen enter: ListUser FTPD OMVS (FTPD is usual name of the FTP daemon) If all of the following are true, this is not a finding. If either of the following is untrue, this is a finding. -The FTPD userid is defined as a PROTECTED userid. -The FTPD userid has the following z/OS UNIX attributes: UID(0), HOME directory '/', shell program /bin/sh. From z/OS command screen enter: RList STARTED FTPD If a matching entry in the STARTED resource class exists enabling the use of the standard userid and appropriate group, this is not a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-223743`

### Rule: IBM FTP.DATA configuration for the FTP server must have the INACTIVE statement properly set.

**Rule ID:** `SV-223743r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Data configuration file specified on the SYSFTPD DD statement in the FTP started task JCL. If the INACTIVE statement is coded with a value between 1 and 900 (seconds), this is not a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-223744`

### Rule: IBM z/OS startup parameters for the FTP server must have the INACTIVE statement properly set.

**Rule ID:** `SV-223744r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the FTPD started task procedure. If the SYSTCPD and SYSFTPD DD statements specify the TCP/IP Data and FTP Data configuration files respectively, this is not a finding. If the ANONYMOUS keyword is not coded on the PARM parameter on the EXEC statement, this is not a finding. If the ANONYMOUS=logonid combination is not coded on the PARM parameter on the EXEC statement, this is not a finding. If the INACTIVE keyword is not coded on the PARM parameter on the EXEC statement, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223745`

### Rule: IBM z/OS RJE workstations and NJE nodes must be defined to the FACILITY resource class.

**Rule ID:** `SV-223745r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to SYS1.PARMLIB (JES2PARM) For each node entry If all JES2 defined NJE nodes and RJE workstations have a profile defined in the FACILITY resource class, this is not a finding. Notes: Nodename is the NAME parameter value specified on the NODE statement. Review the JES2 parameters for NJE node definitions by searching for NODE( in the report. Workstation is RMTnnnn, where nnnn is the number on the RMT statement. Review the JES2 parameters for RJE workstation definitions by searching for RMT( in the report. NJE.* and RJE.* profiles will force userid and password protection of all NJE and RJE connections respectively. This method is acceptable in lieu of using discrete profiles.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223746`

### Rule: IBM z/OS JES2 input sources must be controlled in accordance with the proper security requirements.

**Rule ID:** `SV-223746r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer the JES2PARM member of SYS1.PARMLIB. Review the following resources in the RACF JESINPUT resource class: INTRDR (internal reader for batch jobs) nodename (NJE node) OFFn.* (spool offload receiver) Rnnnn (RJE workstation) RDRnn (local card reader) STCINRDR (internal reader for started tasks) TSUINRDR (internal reader for TSO logons) Note: If any of the following are not defined within the JES2 parameters, the resource in the JESINPUT resource class does not have to be defined. -Nodename is the NAME parameter in the NODE statement. Review the NJE node definitions by searching for NODE( in the report. -OFFn, where n is the number of the offload receiver. Review the spool offload receiver definitions by searching for OFF( in the report. -Rnnnn, where nnnn is the number of the remote workstation. Review the RJE node definitions by searching for RMT( in the report. -RDRnn, where nn is the number of the reader. Review the reader definitions by searching for RDR( in the report. If the JESINPUT resource class is active, this is not a finding. If the resources detailed above are protected by generic and/or fully qualified profiles defined to the JESINPUT resource class, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223747`

### Rule: IBM z/OS JES2 input sources must be properly controlled.

**Rule ID:** `SV-223747r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RL JESINPUT * If the RACF resources and/or generic equivalent identified below are defined with access restricted to the appropriate personnel, this is not a finding. INTRDR nodename OFFn.* OFFn.JR OFFn.SR Rnnnn.RDm RDRnn STCINRDR TSUINRDR and/or TSOINRDR Note: Examples of appropriate might be access to the offload input sources is limited to systems personnel (e.g., operations staff) as directed by site operations and the site security plan.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223748`

### Rule: IBM z/OS JES2 output devices must be controlled in accordance with the proper security requirements.

**Rule ID:** `SV-223748r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer the JES2PARM member of SYS1.PARMLIB. Review the following resources in the RACF WRITER resource class: JES2.** (backstop profile) JES2.LOCAL.OFFn.* (spool offload transmitter) JES2.LOCAL.OFFn.ST (spool offload SYSOUT transmitter) JES2.LOCAL.OFFn.JT (spool offload job transmitter) JES2.LOCAL.PRTn (local printer) JES2.LOCAL.PUNn (local punch) JES2.NJE.nodename (NJE node) JES2.RJE.Rnnnn.PRm (remote printer) JES2.RJE.Rnnnn.PUm (remote punch) -JES2 is typically the name of the JES2 subsystem. Refer to the SUBSYS report and locate the entry with the description of PRIMARY JOB ENTRY SUBSYSTEM. The SUBSYSTEM NAME of this entry is the name of the JES2 subsystem. -OFFn, where n is the number of the offload transmitter. Determine the numbers by searching for OFF( in the JES2 parameters. -PRTn, where n is the number of the local printer. Determine the numbers by searching for PRT( in the JES2 parameters. -PUNn, where n is the number of the local card punch. Determine the numbers by searching for PUN( in the JES2 parameters. -Nodename is the NAME parameter value specified on the NODE statement. Review the JES2 parameters for NJE node definitions by searching for NODE( in the report. -Rnnnn.PRm, where nnnn is the number of the remote workstation and m is the number of the printer. Determine the numbers by searching for .PR in the JES2 parameters. -Rnnnn.PUm, where nnnn is the number of the remote workstation and m is the number of the punch. Determine the numbers by searching for .PU in the JES2 parameters. If the WRITER resource class is active, this is not a finding. If the other resources detailed above are protected by generic and/or fully qualified profiles defined to the WRITER resource class with UACC(NONE), this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223749`

### Rule: IBM z/OS JES2 output devices must be properly controlled for classified systems.

**Rule ID:** `SV-223749r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RL WRITER * If the RACF resources and/or generic equivalent identified below are defined with access restricted to the appropriate personnel, this is not a finding. JES2.LOCAL.devicename JES2.LOCAL.OFFn.* JES2.LOCAL.OFFn.JT JES2.LOCAL.OFFn.ST JES2.LOCAL.PRTn JES2.LOCAL.PUNn JES2.NJE.nodename JES2.RJE.devicename Note: Examples of appropriate restriction might be access to the offload input sources is limited to systems personnel (e.g., operations staff) as directed by site operations and the site security plan.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223750`

### Rule: IBM z/OS JESSPOOL resources must be protected in accordance with security requirements.

**Rule ID:** `SV-223750r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopt list If the JESSPOOL resource class is active, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223751`

### Rule: IBM z/OS JESNEWS resources must be protected in accordance with security requirements.

**Rule ID:** `SV-223751r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RL OPERCMS * JES2 is typically the name of the JES2 subsystem. Refer to the SUBSYS report and locate the entry with the description of PRIMARY JOB ENTRY SUBSYSTEM. The SUBSYSTEM NAME of this entry is the name of the JES2 subsystem. If the JES2.UPDATE.JESNEWS resource is defined to the OPERCMDS resource class, this is not a finding. If access authorization to the JES2.UPDATE.JESNEWS resource in the OPERCMDS class restricts CONTROL access to the appropriate personnel (i.e., users responsible for maintaining the JES News data set), this is not a finding. If all access to the JES2.UPDATE.JESNEWS resource is logged, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223752`

### Rule: IBM z/OS JESTRACE and/or SYSLOG resources must be protected in accordance with security requirements.

**Rule ID:** `SV-223752r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the JESPARM member of SYS1.PARMLIB. Review the JES2 parameters to determine the localnodeid by searching for OWNNODE in the NJEDEF statement, and then searching for NODE(nnnn) (where nnnn is the value specified by OWNNODE). The NAME parameter value specified on this NODE statement is the localnodeid. Another method is to issue the JES2 command $D NODE,NAME,OWNNODE=YES to obtain the NAME of the OWNNODE. From the ISPF Command Shell enter: RL JESSPOOL * Review the following resources defined to the JESSPOOL resource class: localnodeid.JES2.$TRCLOG.taskid.*.JESTRACE localnodeid.+MASTER+.SYSLOG.jobid.*.SYSLOG or localnodeid.+BYPASS+.SYSLOG.jobid.-.SYSLOG NOTE: These resource profiles may be more generic as long as they pertain directly to the JESTRACE and SYSLOG data sets. For example: localnodeid.JES2.*.*.*.JESTRACE localnodeid.+MASTER+.*.*.*.SYSLOG or localnodeid.+BYPASS+.*.*.*.SYSLOG If Userid(s) associated with external writer(s) have complete access, this is not a finding. Note: An external writer is an STC that removes data sets from the JES spool. In this case, it is responsible for archiving the JESTRACE and SYSLOG data sets. The STC default name is XWTR and the external writer program is called IASXWR00. If Systems personnel and security administrators responsible for diagnosing JES2 and z/OS problems have complete access, this is not a finding. If Application Development and Application Support personnel responsible for diagnosing application problems have READ access to the SYSLOG resource, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223753`

### Rule: IBM z/OS JES2 spool resources must be controlled in accordance with security requirements.

**Rule ID:** `SV-223753r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RL JESSPOOL * Review the accesses to the JESSPOOL resources. If the following guidance is true, this is not a finding. Review the JESSPOOL report for resource permissions with the following naming convention. These profiles may be fully qualified, be specified as generic, or be specified with masking as indicated below: localnodeid.userid.jobname.jobid.dsnumber.name localnodeid The name of the node on which the SYSIN or SYSOUT data set currently resides. userid The userid associated with the job. This is the userid RACF uses for validation purposes when the job runs. jobname The name that appears in the name field of the JOB statement. jobid The job number JES2 assigned to the job. dsnumber The unique data set number JES2 assigned to the spool data set. A D is the first character of this qualifier. name The name of the data set specified in the DSN= parameter of the DD statement. If the JCL did not specify DSN= on the DD statement that creates the spool data set, JES2 uses a question mark (?). All users have access to their own JESSPOOL resources. The localnodeid. resources are restricted to only system programmers, operators, and automated operations personnel with access of ALTER. All access will be logged. (localnodeid. resource includes all generic and/or masked permissions, example: localnodeid.**, localnodeid.*, etc.) The JESSPOOL localnodeid.userid.jobname.jobid.dsnumber.name, whether generic and/or masked, can be made available to users when approved by the ISSO. Access will be identified at the minimum access for the user to accomplish the users function. UPDATE, CONTROL, and ALTER access will be logged. An example is team members within a team, providing the capability to view, help, and/or debug other team member jobs/processes. CSSMTP will be restricted to localnodeid.userid.jobname.jobid.dsnumber.name, whether generic and/or masked, when approved by the ISSO. All access will be logged. Spooling products users (CA-SPOOL, CA View, etc.) will be restricted to localnodeid.userid.jobname.jobid.dsnumber.name, whether generic and/or masked, when approved by the ISSO. Logging of access is not required.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223754`

### Rule: IBM z/OS JES2 system commands must be protected in accordance with security requirements.

**Rule ID:** `SV-223754r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RList OPERCMDS * If the JES2.** resource is defined to the OPERCMDS class with an access of NONE and all access is logged, this is not a finding. If access to JES2 system commands defined in the IBM z/OS JES2 Commands is restricted to the appropriate personnel (e.g., operations staff, systems programming personnel, general users), as determined in the documented site Security Plan, this is not a finding. If access to specific JES2 system commands is logged as indicated in the documented site Security Plan, this is not a finding. Note: Display commands and others as deemed by the site IAW site security plan may be allowed for all users with no logging.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223755`

### Rule: IBM z/OS surrogate users must be controlled in accordance with proper security requirements.

**Rule ID:** `SV-223755r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000326-GPOS-00126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RList SURROGAT * If no executionuserid.SUBMIT resources are defined to the SURROGAT resource class, this is Not Applicable. For each executionuserid.SUBMIT resource defined to the SURROGAT resource class, if the following items are in true regarding surrogate controls, this is not a finding. -All executionuserid.SUBMIT resources defined to the SURROGAT resource class specify a default access of NONE. -All resource access is logged; at the discretion of the ISSM/ISSO scheduling tasks may be exempted. Access authorization is restricted to scheduling tools, started tasks, or other system applications required for running production jobs. Other users may have minimal access required for running production jobs with documentation properly approved and filed with the site security official (ISSM or equivalent).

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223756`

### Rule: IBM z/OS RJE workstations and NJE nodes must be controlled in accordance with security requirements.

**Rule ID:** `SV-223756r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note that this guidance addresses RJE Workstations that are "Dedicated". If an RJE workstation is dedicated, the assumption is that the RJE to host connection is hard-wired between the RJE and host. In this case the RMT definition statement will contain the keyword LINE= which specifies that this RJE is only connected via that one LINE statement. Refer to the JES2PARM member of PARMLIB. If all of the statements below are true, this is not a finding. If any of the statements below are untrue, this is a finding. Review the JES2 parameters for RJE workstation definitions by searching for RMT( in the report. A userid of RMTnnnn is defined to RACF for each RJE workstation, where nnnn is the number on the RMT statement. No userid segments (e.g., TSO, CICS, etc.) are defined. Restricted from accessing all data sets and resources with exception of the corresponding JESINPUT class profile for that remote. NOTE: Execute the JCL in CNTL(IRRUT100) using the RACF RMTnnnn userids as SYSIN input. This report lists all occurrences of these userids within the RACF database, including data set and resource access lists. A FACILITY-Class profile exists in the format RJE.RMTnnnn where nnn identifies the remote number.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-223757`

### Rule: IBM z/OS must configure system wait times to protect resource availability based on site priorities.

**Rule ID:** `SV-223757r958636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific operating system functionality where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member. Examine the JWT, SWT, and TWT values. If the JWT parameter is greater than "15" minutes, and the system is processing unclassified information, review the following items. If any of these items is true, this is not a finding. -If a session is not terminated, but instead is locked out after "15" minutes of inactivity, a process must be in place that requires user identification and authentication before the session is unlocked. Session lock-out will be implemented through system controls or terminal screen protections. -A system's default time for terminal lock-out or session termination may be lengthened to "30" minutes at the discretion of the ISSM or ISSO. The ISSA and/or ISSO will maintain the documentation for each system with a time-out adjusted beyond the 15-minute recommendation to explain the basis for this decision. -The ISSM and/or ISSO may set selected userids to have a time-out of up to "60" minutes to complete critical reports or transactions without timing out. Each exception must meet the following criteria: -The time-out exception cannot exceed "60" minutes. -A letter of justification fully documenting the user requirement(s) must be submitted and approved by the site ISSM or ISSO. In addition, this letter must identify an alternate means of access control for the terminal(s) involved (e.g., a room that is locked at all times, a room with a cipher lock to limit access, a password protected screen saver set to "30" minutes or less, etc.). -The requirement must be revalidated on an annual basis. If the TWT and SWT values are equal or less than the JWT value, this is not a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-223758`

### Rule: The IBM z/OS BPX.SMF resource must be properly configured.

**Rule ID:** `SV-223758r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the FACILITY resource class for BPX.SMF. If the RACF rules are as follows this is not a finding. BPX.SMF.119.94 - READ allowed for users running the ssh, sftp, or scp client commands. BPX.SMF.119.96 - READ allowed for users running the scp or sftp-server server commands. BPX.SMF.119.97 - READ allowed for users running the scp or sftp client commands. The following profile grants the permitted users the authority to write or test for any SMF record being recorded. Access should be permitted as follows: BPX.SMF - READ access only when documented and justified in Site Security Plan. Documentation should include a reason why a more specific profile is not acceptable.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-223759`

### Rule: IBM z/OS SMF recording options for the TN3270 Telnet Server must be properly specified.

**Rule ID:** `SV-223759r958846_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The TN3270 Telnet Server can provide audit data in the form of SMF records. The SMF data produced provides information about individual sessions. This data includes the VTAM application, the remote and local IP addresses, and the remote and local IP port numbers. Failure to collect and retain audit data may contribute to the loss of accountability and hamper security audit activities. Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000032-GPOS-00013</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TCPIP started task JCL. If the following configuration statement settings are in effect in the TCP/IP Profile configuration data set, this is not a finding. NOTE: If the INCLUDE statement is coded in the TCP/IP Profile configuration data set, the data set specified on this statement must be checked for the following items as well. The TELNETPARMS SMFINIT statement is coded with the TYPE119 operand within each TELNETPARMS statement block. The TELNETPARMS SMFTERM statement is coded with the TYPE119 operand within each TELNETPARMS statement block. Note: The SMFINIT and SMFTERM statement can appear in both TELNETGLOBAL and TELNETPARM statement blocks. If duplicate statements appear in the TELNETGLOBALS, TELNETPARMS, Telnet uses the last valid statement that was specified.

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-223760`

### Rule: IBM RACF must be installed and active on the system.

**Rule ID:** `SV-223760r958362_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management for operating systems challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other errors. IBM z/OS requires an external security manager to assure proper account management.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper IEFSSnxx member. If RACF is defined in the SubSystem member, this is not a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-223761`

### Rule: The IBM z/OS system administrator (SA) must develop a process to disable emergency accounts after the crisis is resolved or 72 hours.

**Rule ID:** `SV-223761r998357_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by the organization's SAs when network or normal logon/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented process to disable emergency accounts. If there is no documented process, this is a finding. Examine the process, if it does not include procedures to disable emergency accounts after the crisis is resolved or 72 hours, this is a finding.

## Group: SRG-OS-000274-GPOS-00104

**Group ID:** `V-223762`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify appropriate personnel when accounts are created.

**Rule ID:** `SV-223762r998358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of operating system user accounts and notifies SAs and information system security officers (ISSOs) that it exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system Administrator for the documented process to notify appropriate personnel when accounts are created. If there is no documented process, this is a finding.

## Group: SRG-OS-000275-GPOS-00105

**Group ID:** `V-223763`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify appropriate personnel when accounts are modified.

**Rule ID:** `SV-223763r998360_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented process to notify appropriate personnel when accounts are modified. If there is no documented process, this is a finding.

## Group: SRG-OS-000276-GPOS-00106

**Group ID:** `V-223764`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify appropriate personnel when accounts are deleted.

**Rule ID:** `SV-223764r998362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented process to notify appropriate personnel when accounts are deleted. If there is no documented process, this is a finding.

## Group: SRG-OS-000277-GPOS-00107

**Group ID:** `V-223765`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify appropriate personnel when accounts are removed.

**Rule ID:** `SV-223765r998364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When operating system accounts are removed, user accessibility is affected. Accounts are utilized for identifying individual operating system users or for identifying the operating system processes themselves. Sending notification of account removal events to the SAs and information system security officers (ISSOs) is one method for mitigating this risk. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented process to notify appropriate personnel when accounts are removed. If there is no documented process, this is a finding.

## Group: SRG-OS-000304-GPOS-00121

**Group ID:** `V-223766`

### Rule: The IBM z/OS system administrator (SA) must develop a process to notify information system security officers (ISSOs) of account enabling actions.

**Rule ID:** `SV-223766r998367_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable an existing disabled account. Sending notification of account enabling actions to the SAs and ISSOs is one method for mitigating this risk. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. In order to detect and respond to events that affect user accessibility and application processing, operating systems must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA for the documented processes to notify the ISSOs of account enabling actions. If there is no documented process, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-223767`

### Rule: IBM z/OS required SMF data record types must be collected.

**Rule ID:** `SV-223767r998368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00020, SRG-OS-000042-GPOS-00021, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000327-GPOS-00127, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000458-GPOS-00203, SRG-OS-000461-GPOS-00205, SRG-OS-000462-GPOS-00206, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209, SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218, SRG-OS-000474-GPOS-00219, SRG-OS-000475-GPOS-00220, SRG-OS-000476-GPOS-00221, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member. If all of the required SMF record types identified below are collected, this is not a finding. IBM SMF Records to be collect at a minimum: 0 (00) - IPL 6 (06) - External Writer/ JES Output Writer/ Print Services Facility (PSF) 7 (07) - [SMF] Data Lost 14 (0E) - INPUT or RDBACK Data Set Activity 15 (0F) - OUTPUT, UPDAT, INOUT, or OUTIN Data Set Activity 17 (11) - Scratch Data Set Status 18 (12) - Rename Non-VSAM Data Set Status 24 (18) - JES2 Spool Offload 25 (19) - JES3 Device Allocation 26 (1A) - JES Job Purge 30 (1E) - Common Address Space Work 32 (20) - TSO/E User Work Accounting 41 (29) - DIV Objects and VLF Statistics 42 (2A) - DFSMS statistics and configuration 43 (2B) - JES Start 45 (2D) - JES Withdrawal/Stop 47 (2F) - JES SIGNON/Start Line (BSC)/LOGON 48 (30) - JES SIGNOFF/Stop Line (BSC)/LOGOFF 49 (31) - JES Integrity 52 (34) - JES2 LOGON/Start Line (SNA) 53 (35) - JES2 LOGOFF/Stop Line (SNA) 54 (36) - JES2 Integrity (SNA) 55 (37) - JES2 Network SIGNON 56 (38) - JES2 Network Integrity 57 (39) - JES2 Network SYSOUT Transmission 58 (3A) - JES2 Network SIGNOFF 60 (3C) - VSAM Volume Data Set Updated 61 (3D) - Integrated Catalog Facility Define Activity 62 (3E) - VSAM Component or Cluster Opened 64 (40) - VSAM Component or Cluster Status 65 (41) - Integrated Catalog Facility Delete Activity 66 (42) - Integrated Catalog Facility Alter Activity 80 (50) - RACF/TOP SECRET Processing 81 (51) - RACF Initialization 82 (52) - ICSF Statistics 83 (53) - RACF Audit Record For Data Sets 90 (5A) - System Status 92 (5C) except subtypes 10, 11 - OpenMVS File System Activity 102 (66) - DATABASE 2 Performance 103 (67) - IBM HTTP Server 110 (6E) - CICS/ESA Statistics 118 (76) - TCP/IP Statistics 119 (77) - TCP/IP Statistics 199 (C7) - TSOMON 230 (E6) - ACF2 or as specified in ACFFDR (vendor-supplied default is 230) 231 (E7) - TSS logs security events under this record type

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-223768`

### Rule: IBM z/OS must employ a session manager to manage display of the Standard Mandatory DoD Notice and Consent Banner.

**Rule ID:** `SV-223768r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. All methods of gaining access to the system must comply with this requirement to assure that regulations are upheld.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that any session manger in use displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the system. If the session manager does not display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system, this is a finding.

## Group: SRG-OS-000038-GPOS-00016

**Group ID:** `V-223769`

### Rule: IBM z/OS must specify SMF data options to assure appropriate activation.

**Rule ID:** `SV-223769r958414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMF data collection is the basic unit of tracking of all system functions and actions. Included in this tracking data are the audit trails from each of the ACPs. If the control options for the recording of this tracking are not properly maintained, then accountability cannot be monitored, and its use in the execution of a contingency plan could be compromised. Satisfies: SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000254-GPOS-00095, SRG-OS-000269-GPOS-00103</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member. If the following SMF collection options are specified as stated below, this is not a finding. The settings for several parameters are critical to the collection process: ACTIVE - Activates the collection of SMF data. MAXDORM - Specifies the amount of real time that SMF allows data to remain in an SMF buffer before it is written to a recording data set. Value is site defined. SID - Specifies the system ID to be recorded in all SMF records. SYS(DETAIL) - Controls the level of detail recorded. SYS(INTERVAL) - Ensures the periodic recording of data for long running jobs. SYS - Specifies the types and sub types of SMF records that are to be collected. SYS(TYPE) indicates that the supplied list is inclusive (i.e., specifies the record types to be collected). Record types not listed are not collected. SYS(NOTYPE) indicates that the supplied list is exclusive (i.e., specifies those record types not to be collected). Record types listed are not collected. The site may use either form of this parameter to specify SMF record type collection. However, at a minimum all record types listed.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-223770`

### Rule: IBM z/OS SMF collection files (system MANx datasets or LOGSTREAM DASD) must have storage capacity to store at least one weeks worth of audit data.

**Rule ID:** `SV-223770r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SMF dump procedure in there system. If the output datasets in the procedure have storage capacity to store at least one week's worth of audit data, this is not a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-223771`

### Rule: IBM z/OS system administrators must develop an automated process to collect and retain SMF data.

**Rule ID:** `SV-223771r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator if there is an automated process is in place to collect and retain all SMF data produced on the system. If, based on the information provided, it can be determined that an automated process is in place to collect and retain all SMF data produced on the system, this is not a finding. If it cannot be determined this process exists and is being adhered to, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-223772`

### Rule: IBM z/OS BUFUSEWARN in the SMFPRMxx must be properly set.

**Rule ID:** `SV-223772r971542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both. Satisfies: SRG-OS-000343-GPOS-00134, SRG-OS-000344-GPOS-00135, SRG-OS-000046-GPOS-00022</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member in SYS1.PARMLIB. If BUFUSEWARN is set for "75" (75%) or less, this is not a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-223773`

### Rule: IBM z/OS NOBUFFS in SMFPRMxx must be properly set (default is MSG).

**Rule ID:** `SV-223773r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper SMFPRMxx member in SYS1.PARMLIB. If NOBUFFS is set to "HALT", this is not a finding. Note: If availability is an overriding concern NOBUFFS can be set to MSG.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-223774`

### Rule: The IBM z/OS SNTP daemon (SNTPD) must be active.

**Rule ID:** `SV-223774r1038944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From UNIX System Services ISPF Shell navigate to ribbon select tools. Select option 1 - Work with Processes. If SNTP Daemon (SNTPD) is not active, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-223775`

### Rule: IBM z/OS SNTP daemon (SNTPD) permission bits must be properly configured.

**Rule ID:** `SV-223775r1038944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time, a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: cd /usr/sbin ls -al If the following File permission and user Audit Bits are true, this is not a finding. /usr/sbin/sntpd 1740 faf The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-223776`

### Rule: IBM z/OS PARMLIB CLOCKxx must have the Accuracy PARM properly coded.

**Rule ID:** `SV-223776r998371_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done in order to determine the time difference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the CLOCKxx member of PARMLIB. If the ACCURACY parm is not coded, this is a finding. If the ACCURACY parm is coded to "1000", this is not a finding.

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-223777`

### Rule: IBM RACF must define UACC of NONE on all profiles.

**Rule ID:** `SV-223777r1050763_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The operating system must employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all Dataset and resource profiles in the RACF database. If any are not defined with UACC NONE, this is a finding. There is an exception when evaluating the UACC for DIGTCERT and NODES resource classes. The universal access (UACC) for DIGTCERT profiles: For profiles in classes other than DIGTCERT, the valid values are NONE, READ, EXECUTE, UPDATE, CONTROL, and ALTER. For DIGTCERT profiles, the valid values are TRUST, NOTRUST, and HIGHTRST. If DIGTCERT Profiles are defined with other than UACC NONE, this is not a finding. The universal access (UACC) for NODES: A UACC of NONE fails the inbound job. If NODES profiles are defined with other than UACC NONE, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223778`

### Rule: IBM z/OS PASSWORD data set and OS passwords must not be used.

**Rule ID:** `SV-223778r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator to determine if the system PASSWORD data set and OS passwords are being used. If, based on the information provided, it can be determined that the system PASSWORD data set and OS passwords are not used, this is not a finding. If it is evident that OS passwords are utilized, this is a finding.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-223780`

### Rule: The IBM z/OS Policy Agent must employ a deny-all, allow-by-exception firewall policy for allowing connections to other systems.

**Rule ID:** `SV-223780r991593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to restrict network connectivity only to authorized systems permits inbound connections from malicious systems. It also permits outbound connections that may facilitate exfiltration of DoD data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the policy agent policy statements. If it can be determined that the policy agent employs a deny-all, allow-by exception firewall policy for allowing connections to other systems this is not a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-223781`

### Rule: Unsupported system software must not be installed and/ or active on the system.

**Rule ID:** `SV-223781r958804_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to all products that meet the following criteria: - Uses authorized and restricted z/OS interfaces by utilizing Authorized Program Facility (APF) authorized modules or libraries. - Requires access to system datasets or sensitive information or requires special or privileged authority to run. For the products in the above category, refer to the Vendor's support lifecycle information for current versions and releases. If the software products currently running on the reviewed system are at a version greater than or equal to the products listed in the vendor's Support Lifecycle information, this is not a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-223782`

### Rule: IBM z/OS must not allow nonexistent or inaccessible LINKLIST libraries.

**Rule ID:** `SV-223782r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From and ISPF Command line enter: TSO ISRDDN LINKLIST Review the list, if there are any DUMMY entries i.e., inaccessible LINKLIST libraries, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-223783`

### Rule: IBM z/OS must not allow nonexistent or inaccessible Link Pack Area (LPA) libraries.

**Rule ID:** `SV-223783r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From and ISPF Command line enter: TSO ISRDDN LPA Review the list, if there are any DUMMY entries i.e., inaccessible LPA libraries, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-223784`

### Rule: IBM z/OS must not have inaccessible APF libraries defined.

**Rule ID:** `SV-223784r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. Determine proper APF and/or PROG member. Examine each entry and verify that it exists on the specified volume. If inaccessible APF libraries exist, this is a finding. ISRDDN APF

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-223785`

### Rule: IBM zOS inapplicable PPT entries must be invalidated.

**Rule ID:** `SV-223785r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Invalid or inapplicable PPT entries exist, a venue is provided for the introduction of trojan horse modules with security bypass capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review program entries in the IBM Program Properties Table (PPT). You may use a third-party product to examine these entries; however, to determine program entries, issue the following command from an ISPF command line: TSO ISRDDN LOAD IEFSDPPT Interpret the display as follows: Examine contents at offset 8 Hex 'x2' - Bypass Password Protection Hex 'x3' - Bypass Password Protection Hex 'x4' - No Dataset Integrity Hex 'x5' - No Dataset Integrity Hex 'x6' - Both Hex 'x7' - Both Determine Privilege Key at offset 9. A value of hex '70' or less indicates an elevated privilege. For each module identified in the "eyecatcher" that has BYPASS Password Protection, No Dataset Integrity, an elevated Privilege Key or any combination thereof, determine if there is a valid loaded module. Again, you may use a third-party product; otherwise, execute the following steps from an ISPF command line: TSO ISRDDN LOAD <privileged module> If the return message is "Load Failed", make sure there is an entry in PARMLIB member SCHEDxx that revokes the excessive privilege. If this is not true, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-223786`

### Rule: IBM z/OS LNKAUTH=APFTAB must be specified in the IEASYSxx member(s) in the currently active parmlib data set(s).

**Rule ID:** `SV-223786r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to specify LINKAUTH=APFTAB allows libraries other than those designated as APF to contain authorized modules which could bypass security and violate the integrity of the operating system environment. This expanded authorization list inhibits the ability to control inclusion of these modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to IEASYS00 member in SYS1.PARMLIB Concatenation. If LNKAUTH=APFTAB is not specified, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-223787`

### Rule: IBM z/OS must not have duplicated sensitive utilities and/or programs existing in APF libraries.

**Rule ID:** `SV-223787r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Removal of unneeded or non-secure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ISPF Command line enter: TSO ISRDDN APF An APF List results On the command line enter: DUPlicates (make sure there is appropriate access; if there is not you may receive insufficient access errors) If any of the list of Sensitive Utilities exist in the duplicate APF modules return, this is a finding. The following list contains Sensitive Utilities that will be checked. AHLGTF AMASPZAP AMAZAP AMDIOCP AMZIOCP BLSROPTR CSQJU003 CSQJU004 CSQUCVX CSQUTIL CSQ1LOGP DEBE DITTO FDRZAPOP GIMSMP HHLGTF ICKDSF ICPIOCP IDCSC01 IEHINITT IFASMFDP IGWSPZAP IHLGTF IMASPZAP IND$FILE IOPIOCP IXPIOCP IYPIOCP IZPIOCP WHOIS L052INIT TMSCOPY TMSFORMT TMSLBLPR TMSMULV TMSREMOV TMSTPNIT TMSUDSNB

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-223788`

### Rule: The IBM z/OS systems requiring data-at-rest protection must properly employ IBM DS8880 or equivalent hardware solutions for full disk encryption.

**Rule ID:** `SV-223788r1028297_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control addresses the confidentiality and integrity of information at rest and covers user information and system information. Information at rest refers to the state of information when it is located on storage devices as specific components of information systems. Operating systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000405-GPOS-00184, SRG-OS-000404-GPOS-00183, SRG-OS-000396-GPOS-00176</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if IBM's DS8880 Disks or equivalent hardware solutions are in use. If they are not in use for systems that require data at rest, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-223792`

### Rule: The IBM z/OS Policy Agent must contain a policy that protects against or limits the effects of denial-of-service (DoS) attacks by ensuring the operating system is implementing rate-limiting measures on impacted network interfaces.

**Rule ID:** `SV-223792r958902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the Policy Agent policy statements. If it can be determined that policy that protects against or limits the effects of denial-of-service (DoS) attacks by ensuring the operating system is implementing rate-limiting measures on impacted network interfaces, this is not a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-223793`

### Rule: The IBM z/OS Policy Agent must contain a policy that manages excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-223793r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the Policy Agent policy statements. If it can be determined that there are policy statements that manages excess capacity, this is not a finding.

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-223794`

### Rule: The IBM z/OS must employ a session manager that conceals, via the session lock, information previously visible on the display with a publicly viewable image.

**Rule ID:** `SV-223794r958404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. The operating system session lock event must include an obfuscation of the display screen so as to prevent other users from reading what was previously displayed. Publicly viewable images can include static or dynamic images, for example, patterns used with screen savers, photographic images, solid colors, a clock, a battery life indicator, or a blank screen, with the additional caveat that none of the images convey sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the configuration parameters for the session manager in use. If there is no session manager in use, this is a finding. If the session manager is not configure to conceal, via the session lock, information previously visible on the display with a publicly viewable image, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-223795`

### Rule: IBM z/OS must employ a session manager to manage session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-223795r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the configuration parameters for the session manager in use. If there is no session manager in use, this is a finding. If the session manager is not configured to initiate session lock after a 15-minute period of inactivity, this is a finding.

## Group: SRG-OS-000030-GPOS-00011

**Group ID:** `V-223796`

### Rule: IBM z/OS must employ a session for users to directly initiate a session lock for all connection types.

**Rule ID:** `SV-223796r998372_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, operating systems need to provide users with the ability to manually invoke a session lock so users may secure their session should the need arise for them to temporarily vacate the immediate physical vicinity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the configuration parameters for the session manager in use. If there is no session manager in use, this is a finding. If the session manager in use does not allow users to directly initiate a session lock for all connection types, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-223797`

### Rule: IBM z/OS must employ a session manager to manage retaining a users session lock until that user reestablishes access using established identification and authentication procedures.

**Rule ID:** `SV-223797r958400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock must remain in place until the user reauthenticates. No other activity aside from reauthentication must unlock the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the configuration parameters for the session manager in use. If there is no session manager in use this is a finding. If the session manager is not configured to retain a user's session lock until that user reestablishes access using established identification and authentication procedures, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-223798`

### Rule: IBM z/OS system administrator must develop a procedure to remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-223798r998374_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by the organization's system administrators when network or normal logon/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator (SA) for the procedure to automatically remove or disable temporary user accounts after 72 hours. If there is no procedure, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-223800`

### Rule: IBM z/OS system administrator must develop a procedure to notify designated personnel if baseline configurations are changed in an unauthorized manner.

**Rule ID:** `SV-223800r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to notify designated personnel if baseline configurations are changed in an unauthorized manner. If there is no procedure, this is a finding.

## Group: SRG-OS-000122-GPOS-00063

**Group ID:** `V-223801`

### Rule: IBM z/OS system administrator must develop a procedure to provide an audit reduction capability that supports on-demand reporting requirements.

**Rule ID:** `SV-223801r958506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to generate on-demand reports, including after the audit data has been subjected to audit reduction, greatly facilitates the organization's ability to generate incident reports as needed to better handle larger-scale or more complex security incidents. Audit reduction is a process that manipulates collected audit information and organizes such information in a summary format that is more meaningful to analysts. The report generation capability provided by the application must support on-demand (i.e., customizable, ad hoc, and as-needed) reports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to provide an audit reduction capability that supports on-demand reporting requirements. If there is no procedure, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-223803`

### Rule: IBM z/OS system administrator must develop a procedure to remove all software components after updated versions have been installed.

**Rule ID:** `SV-223803r958936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to remove all software components after updated versions have been installed. If there is no procedure, this is a finding.

## Group: SRG-OS-000447-GPOS-00201

**Group ID:** `V-223804`

### Rule: IBM z/OS must shut down the information system, restart the information system, and/or notify the system administrator when anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-223804r958948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If anomalies are not acted upon, security functions may fail to secure the system. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to shut down the information system, restart the information system, and/or notify the system administrator when anomalies occur. If a procedure does not exist, this is a finding. If the procedure does not properly shut down the information system, restart the information system, and/or notify the system administrator when anomalies occur, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-223805`

### Rule: IBM z/OS system administrator must develop a procedure to offload SMF files to a different system or media than the system being audited.

**Rule ID:** `SV-223805r959008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to offload SMF files to a different system or media than the system being audited. If the procedure does not exist, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-223806`

### Rule: IBM z/OS SMF recording options for the SSH daemon must be configured to write SMF records for all eligible events.

**Rule ID:** `SV-223806r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMF data collection is the basic unit of tracking of all system functions and actions. Included in this tracking data are the audit trails from each of the ACPs. If the control options for the recording of this tracking are not properly maintained, then accountability cannot be monitored, and its use in the execution of a contingency plan could be compromised. Satisfies: SRG-OS-000032-GPOS-00013, SRG-OS-000392-GPOS-00172</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the SSH daemon configuration file, which may be found in /etc/ssh/ directory. Alternately: From UNIX System Services ISPF Shell navigate to ribbon select tools. Select option 1 - Work with Processes. If SSH Daemon is not active, this is not a finding. Examine SSH daemon configuration file. If ServerSMF is not coded with ServerSMF TYPE119_U83 or is commented out, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-223807`

### Rule:  The IBM RACF SSH daemon must be configured to use a FIPS 140-2 compliant cryptographic algorithm to protect confidential information and remote access sessions.

**Rule ID:** `SV-223807r1083014_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. Cryptographic modules must adhere to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the SSH daemon configuration file, which may be found in /etc/ssh/ directory. Alternately: From the Unix System Services ISPF Shell, navigate to ribbon select tools. Select option 1 - Work with Processes. If SSH Daemon is not active, this is not a finding. Examine SSH daemon configuration file. sshd_config If there are no "Ciphers" lines, or the ciphers list contains any cipher not starting with "aes", this is a finding. If the MACs line is not configured to "hmac-sha1" or greater this is a finding. Examine the z/OS-specific sshd server systemwide configuration: zos_sshd_config If any of the following is untrue, this is a finding. FIPSMODE=YES CiphersSource=ICSF MACsSource=ICSF

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-223809`

### Rule: The SSH daemon must be configured with the Standard Mandatory DoD Notice and Consent Banner.

**Rule ID:** `SV-223809r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the SSH daemon configuration file, which may be found in /etc/ssh/ directory. Alternately: From UNIX System Services ISPF Shell navigate to ribbon select tools. Select option 1 - Work with Processes. If SSH Daemon is not active, this is not a finding. Examine SSH daemon configuration file. If Banner statement is missing or configured to none, this is a finding. Ensure that the contents of the file specified on the banner statement contain a logon banner. The banner below is mandatory and deviations are not permitted except as authorized in writing by the DoD Chief Information Officer. If there is any deviation this is a finding. STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-223810`

### Rule: IBM z/OS SSH daemon must be configured to only use the SSHv2 protocol.

**Rule ID:** `SV-223810r958480_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the SSH daemon configuration file, which may be found in /etc/ssh/ directory. Alternately: From UNIX System Services ISPF Shell navigate to ribbon select tools. Select option 1 - Work with Processes. If SSH Daemon is not active, this is not a finding. Examine SSH daemon configuration file. If the variables "Protocol 2,1" or "Protocol 1" are defined on a line without a leading comment, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-223811`

### Rule: IBM z/OS, for PKI-based authentication, must use the ICSF or ESM for key management.

**Rule ID:** `SV-223811r998380_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Any keys or Certificates must be managed in ICSF or the external security manager and not in UNIX files. From the ISPF Command Shell enter: OMVS enter find / -name *.kdb and find / -name *.jks If any files are present, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223812`

### Rule: IBM z/OS permission bits and user audit bits for HFS objects that are part of the Syslog daemon component must be properly configured.

**Rule ID:** `SV-223812r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>HFS directories and files of the Syslog daemon provide the configuration and executable properties of this product. Failure to properly secure these objects could lead to unauthorized access. This exposure may result in the compromise of the integrity and availability of the operating system environment, ACP, and customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ISPF Enter cd /usr/sbin Enter ls -alW If File Permission Bits and User Audit Bits for SYSLOG Daemon HFS directories and files is as below, this is not a finding. /usr/sbin/syslogd 1740 fff Enter cd /etc/ Enter ls -alW If the file Permission Bits and User Audit Bits for Output log file defined in the configuration file are as below, this is not a finding. /etc/syslog.conf 0744 faf 0744 fff Notes: The /usr/sbin/syslogd object is a symbolic link to /usr/lpp/tcpip/sbin/syslogd. The permission and user audit bits on the target of the symbolic link must have the required settings. The /etc/syslog.conf file may not be the configuration file the daemon uses. It is necessary to check the script or JCL used to start the daemon to determine the actual configuration file. For example, in /etc/rc: _BPX_JOBNAME='SYSLOGD' /usr/sbin/syslogd -f /etc/syslog.conf For example, in the SYSLOGD started task JCL: //SYSLOGD EXEC PGM=SYSLOGD,REGION=30M,TIME=NOLIMIT // PARM='POSIX(ON) ALL31(ON)/ -f /etc/syslogd.conf' //SYSLOGD EXEC PGM=SYSLOGD,REGION=30M,TIME=NOLIMIT // PARM='POSIX(ON) ALL31(ON) /-f //''SYS1.TCPPARMS(SYSLOG)''' The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223813`

### Rule: The IBM z/OS Syslog daemon must be started at z/OS initialization.

**Rule ID:** `SV-223813r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
SYSLOGD may be started from the shell, a cataloged procedure (STC), or the BPXBATCH program. Additionally, other mechanisms (e.g., a job scheduler) may be used to automatically start the Syslog daemon. To thoroughly analyze this requirement you may need to view the OS SYSLOG using SDSF, find the last IPL, and look for the initialization of SYSLOGD. If the Syslog daemon SYSLOGD is started automatically during the initialization of the z/S/ system, this is not a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223814`

### Rule: The IBM z/OS Syslog daemon must be properly defined and secured.

**Rule ID:** `SV-223814r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Syslog daemon, known as syslogd, is a zOS UNIX daemon that provides a central processing point for log messages issued by other zOS UNIX processes. It is also possible to receive log messages from other network-connected hosts. Some of the IBM Communications Server components that may send messages to syslog are the FTP, TFTP, zOS UNIX Telnet, DNS, and DHCP servers. The messages may be of varying importance levels including general process information, diagnostic information, critical error notification, and audit-class information. Primarily because of the potential to use this information in an audit process, there is a security interest in protecting the syslogd process and its associated data. The Syslog daemon requires special privileges and access to sensitive resources to provide its system services. Failure to properly define and control the Syslog daemon could lead to unauthorized access. This exposure may result in the compromise of the integrity and availability of the operating system environment, ACP, and customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From z/OS command screen enter: ListUser SYSLOGD OMVS (SYSLOGD is usual name of the SYSLOG daemon) If all of the following are true, this is not a finding. If either of the following is untrue, this is a finding. -The SYSLOGD userid is defined as a PROTECTED userid. -The SYSLOGD userid has the following z/OS UNIX attributes: UID(0), HOME directory '/', shell program /bin/sh. From z/OS command screen enter: RList STARTED SYSLOGD If a matching entry in the STARTED resource class exists enabling the use of the standard userid and appropriate group, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223815`

### Rule: IBM z/OS DFSMS Program Resources must be properly defined and protected.

**Rule ID:** `SV-223815r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the load modules residing in the following Load libraries to determine program resource definitions: SYS1.DGTLLIB for DFSMSdfp/ISMF SYS1.DGTLLIB for DFSMSdss/ISMF SYS1.DFQLLIB for DFSMShsm If the installation moves these modules to another load library, the installation-defined load library must be used in the program protection. If the RACF resources are defined with a default access of NONE, this is not a finding. If the RACF resource access authorizations restrict access to the appropriate personnel, this is not a finding. (Refer to the chapter titled "Protecting the Storage Management Subsystem" in the IBM z/OS DFSMSdfp Storage Administration Guide to assist with guidance on appropriate access.)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223816`

### Rule: IBM z/OS DFSMS control data sets must be protected in accordance with security requirements.

**Rule ID:** `SV-223816r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the logical parmlib data sets, example: SYS1.PARMLIB(IGDSMSxx), to identify the fully qualified file names for the following SMS data sets: Source Control Data Set (SCDS) Active Control Data Set (ACDS) Communications Data Set (COMMDS) Automatic Class Selection Routine Source Data Sets (ACS) ACDS Backup COMMDS Backup If the RACF data set rules for the SCDS, ACDS, COMMDS, and ACS data sets restrict WRITE or greater access to only systems programming personnel, this is not a finding. If the RACF data set rules for the SCDS, ACDS, COMMDS, and ACS data sets do not restrict WRITE or greater access to only systems programming personnel, this is a finding. Note: At the discretion of the ISSM, DASD administrators are allowed UPDATE access to the control datasets.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223817`

### Rule: IBM z/OS DFSMS-related RACF classes must be active.

**Rule ID:** `SV-223817r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ISPF Command Shell enter: SETRopts list If ACTIVE CLASSES lists the MGMTCLAS, STORCLAS, PROGRAM, and FACILITY resources classes, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223818`

### Rule: IBM z/OS DFSMS resources must be protected in accordance with the proper security requirements.

**Rule ID:** `SV-223818r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all SMS resources and/or generic equivalent are properly protected according to the requirements specified and the following guidance is true, this is not a finding. The STGADMIN.** profile in the FACILITY resource class has a default access of NONE and no access is granted at this level. STGADMIN.DPDSRN.olddsname is restricted to system programmers and all access is logged. The STGADMIN.IGD.ACTIVATE.CONFIGURATION is restricted to system programmers and all access is logged. The STGADMIN.IGG.DEFDEL.UALIAS is restricted to Centralized and Decentralized Security personnel and system programmers and all access is logged. The resource STGADMIN.IGG.CATALOG.SECURITY.CHANGE is defined with access of NONE. Note: The resource STGADMIN.IGG.CATALOG.SECURITY.CHANGE can be defined with read access for migration purposes. If it is a detailed migration plan must be documented and filed by the ISSM that determines a definite migration period. All access must be logged. At the completion of migration this resource must be configured with access = NONE. The following resources and prefixes may be available to the end user. STGADMIN.ADR.COPY.CNCURRNT STGADMIN.ADR.COPY.FLASHCPY STGADMIN.ADR.COPY.TOLERATE.ENQF STGADMIN.ADR.DUMP.CNCURRNT STGADMIN.ADR.DUMP.TOLERATE.ENQF STGADMIN.ADR.RESTORE.TOLERATE.ENQF STGADMIN.ARC.ENDUSER.* STGADMIN.IGG.ALTER.SMS The following resource is restricted to Application Production Support Team members, Automated Operations, DASD managers, and system programmers. STGADMIN.IDC.DCOLLECT The following resources are restricted to Application Production Support Team members, DASD managers, and system programmers. STGADMIN.ARC.CANCEL STGADMIN.ARC.LIST STGADMIN.ARC.QUERY STGADMIN.ARC.REPORT STGADMIN.DMO.CONFIG STGADMIN.IFG.READVTOC STGADMIN.IGG.DELGDG.FORCE The following resource prefixes, at a minimum, are restricted to DASD managers and system programmers. STGADMIN.ADR STGADMIN.ANT STGADMIN.ARC STGADMIN.DMO STGADMIN.ICK STGADMIN.IDC STGADMIN.IFG STGADMIN.IGG STGADMIN.IGWSHCDS The following Storage Administrator functions prefix is restricted to DASD managers and system programmers and all access is logged. STGADMIN.ADR.STGADMIN.*

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223819`

### Rule: IBM z/OS using DFSMS must properly specify SYS(x).PARMLIB(IGDSMSxx), SMS parameter settings.

**Rule ID:** `SV-223819r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the logical parmlib data sets, example: SYS1.PARMLIB(IGDSMSxx), for the following SMS parameter settings: Parameter Key SMS ACDS(ACDS data set name) COMMDS(COMMDS data set name) If the required parameters are defined, this is not a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-223820`

### Rule: IBM z/OS PROFILE.TCPIP configuration statements for the TCP/IP stack must be coded properly.

**Rule ID:** `SV-223820r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TCPIP started task JCL. If the following items are in effect for the configuration statements specified in the TCP/IP Profile configuration file, this is not a finding. NOTE: If the INCLUDE statement is coded in the TCP/IP Profile configuration file, the data set specified on this statement must be checked for the following items as well. The SMFPARMS statement is not coded or commented out. The DELETE statement is not coded or commented out for production systems. The SMFCONFIG statement is coded with (at least) the FTPCLIENT and TN3270CLIENT operands. The TCPCONFIG and UDPCONFIG statements are coded with (at least) the RESTRICTLOWPORTS operand. If the TCPCONFIG does not have the TTLS statement coded, this is a finding. NOTE: If the INCLUDE statement is coded, the data set specified will be checked for access authorization compliance.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-223821`

### Rule: IBM z/OS must be configured to restrict all TCP/IP ports to ports, protocols, and/or services as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-223821r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer the TCP/IP PROFILE DD statement to determine the TCP/IP Ports. If the PROFILE DD statement is not supplied, use the default search order to find the PROFILE data set. See the IP Configuration Guide for a description of the search order for PROFILE.TCPIP. If the all the Ports included in the configuration are restricted to the ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and vulnerability assessments, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223822`

### Rule: IBM z/OS permission bits and user audit bits for HFS objects that are part of the Base TCP/IP component must be properly configured.

**Rule ID:** `SV-223822r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>HFS directories and files of the Base TCP/IP component provide the configuration, operational, and executable properties of IBMs TCP/IP system product. Failure to properly secure these objects may lead to unauthorized access resulting in the compromise of the integrity and availability of the operating system environment, ACP, and customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs At the input line enter: cd /etc enter ls -alW If the following file permission and user Audit Bits are true, this is not a finding. /etc/hosts 0744 faf /etc/protocol 0744 faf /etc/resolv.conf 0744 faf /etc/services 0740 faf cd /usr ls -alW If the following file permission and user Audit Bits are true, this is not a finding. /usr/lpp/tcpip/sbin 0755 faf /usr/lpp/tcpip/bin 0755 faf Notes: Some of the files listed above are not used in every configuration. The absence of a file is not considered a finding. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223823`

### Rule: IBM z/OS TCP/IP resources must be properly protected.

**Rule ID:** `SV-223823r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RLIST SERVAUTH * ALL If the following guidance is true, this is not a finding. The EZA, EZB, and IST resources and/or generic equivalent are defined to the SERVAUTH resource class with a UACC(NONE). No access is given to the EZA, EZB, and IST high level resources of the SERVAUTH resource class. If the product CSSMTP is on the system, no access is given to EZB.CSSMTP of the SERVAUTH resource class. If the product CSSMTP is on the system, EZB.CSSMTP.sysname.writername.JESnode will be specified and made available to the CSSMTP started task and authenticated users that require access to use CSSMTP for email services. Authenticated users that require access will be permitted access to the second level of the resources in the SERVAUTH resource class. Examples are the network (NETACCESS), port (PORTACCESS), stack (STACKACCESS), and FTP resources in the SERVAUTH resource class. The EZB.STACKACCESS. resource access authorizations restrict access to those started tasks with valid requirements and users with valid FTP access requirements. The EZB.FTP.*.*.ACCESS.HFS) resource access authorizations restrict access to FTP users with specific written documentation showing a valid requirement exists to access OMVS files and Directories. The EZB.INITSTACK.sysname.tcpname resource access authorizations restrict access before policies have been installed, to users authorized by the system security plan requiring access to the TCP/IP stack.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223824`

### Rule: The IBM RACF SERVAUTH resource class must be active for TCP/IP resources.

**Rule ID:** `SV-223824r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Provides the SERVAUTH Class for use in protecting a variety of TCP/IP features/functions/products both IBM and third-party. Failure to activate this class will result in unprotected resources. This exposure may threaten the integrity of the operating system environment, and compromise the confidentiality of customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a command input screen enter: SETROPTS LIST If there are TCP/IP resources defined and the SERVAUTH resource class is not active, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223826`

### Rule: IBM z/OS data sets for the Base TCP/IP component must be properly protected.

**Rule ID:** `SV-223826r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MVS data sets of the Base TCP/IP component provide the configuration, operational, and executable properties of IBMs TCP/IP system product. Failure to properly secure these data sets may lead to unauthorized access resulting in the compromise of the integrity and availability of the operating system environment, ACP, and customer data. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a dataset access list for Base TCP/IP component datasets. If the following items are true, this is not a finding. WRITE and ALLOCATE access to product data sets is restricted to systems programming personnel (i.e., SMP/E distribution data sets with the prefix SYS1.TCPIP.AEZA and target data sets with the prefix SYS1.TCPIP.SEZA). WRITE and ALLOCATE access to the data set(s) containing the Data and Profile configuration files is restricted to systems programming personnel. Note: If any INCLUDE statements are specified in the Profile configuration file, the named MVS data sets have the same access authorization requirements. WRITE and ALLOCATE access to the data set(s) containing the Data and Profile configuration files is logged. Note: If any INCLUDE statements are specified in the Profile configuration file, the named MVS data sets have the same logging requirements. WRITE and ALLOCATE access to the data set(s) containing the configuration files shared by TCP/IP applications is restricted to systems programming personnel.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223827`

### Rule: IBM z/OS Configuration files for the TCP/IP stack must be properly specified.

**Rule ID:** `SV-223827r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the procedure libraries defined to JES2 and locate the TCPIP JCL member. Note: If GLOBALTCPIPDATA is specified, any TCPIP.DATA statements contained in the specified file or data set take precedence over any TCPIP.DATA statements found using the appropriate environment's (native MVS or z/OS UNIX) search order. If GLOBALTCPIPDATA is not specified, the appropriate environment's (Native MVS or z/OS UNIX) search order is used to locate TCPIP.DATA. If the PROFILE and SYSTCPD DD statements specify the TCP/IP Profile and Data configuration files respectively, this not a finding. If the RESOLVER_CONFIG variable on the EXEC statement is set to the same file name specified on the SYSTCPD DD statement, this is not a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-223831`

### Rule: IBM z/OS SSL encryption options for the TN3270 Telnet Server must be specified properly for each statement that defines a SECUREPORT or within the TELNETGLOBALS.

**Rule ID:** `SV-223831r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the SSL connection process a mutually acceptable encryption algorithm is selected by the server and client. This algorithm is used to encrypt the data that subsequently flows between the two. However, the level or strength of encryption can vary greatly. Certain configuration options can allow no encryption to be used and others can allow a relatively weak 40-bit algorithm to be used. Failure to properly enforce adequate encryption strength could result in the loss of data privacy. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000120-GPOS-00061, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000396-GPOS-00176, SRG-OS-000478-GPOS-00223, SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TCPIP started task JCL. If the following items are in effect for the configuration specified in the TCP/IP Profile configuration file, this is not a finding. NOTE: If an INCLUDE statement is coded in the TCP/IP Profile configuration file, the data set specified on this statement must be checked for the following items as well. NOTE: FIPS 140-2 minimum encryption is the accepted level of encryption and will override this requirement if greater. The TELNETGLOBALS block that specifies an ENCRYPTION statement states one or more of the below cipher specifications. Each TELNETPARMS block that specifies the SECUREPORT statement, specifies an ENCRYPTION statement states one or more of the below cipher specifications. And the TELNETGLOBALS block does or does not specify an ENCRYPTION statement. Cipher Specifications SSL_3DES_SHA SSL_AES_256_SHA SSL_AES_128_SHA

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-223833`

### Rule: The IBM z/OS warning banner for the TN3270 Telnet server must contain the proper content of the Standard Mandatory DoD Notice and Consent Banner.

**Rule ID:** `SV-223833r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TN3270 started task JCL. If all USS tables referenced in BEGINVTAM USSTCP statements include MSG10 text that specifies the Standard logon banner, this is not a finding. The below banner is mandatory and deviations are not permitted except as authorized in writing by the DoD Chief Information Officer. The thrust of this new policy is to make it clear that there is no expectation of privacy when using DoD information systems and all use of DoD information systems is subject to searching, auditing, inspecting, seizing, and monitoring, even if some personal use of a system is permitted: STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. DOD requires that a logon warning banner be displayed. Within the TN3270 Telnet Server, the banner can be implemented through the USS table that is specified on a BEGINVTAM USSTCP statement. The text associated with message ID 10 (i.e., MSG10) in the USS table is sent to clients that are subject to USSTCP processing.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223834`

### Rule: IBM z/OS VTAM session setup controls for the TN3270 Telnet server must be properly specified.

**Rule ID:** `SV-223834r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the TN3270 Profile configuration file identified by the PROFILE DD in the TN3270 procedure. NOTE: If the INCLUDE statement is coded in the TCP/IP Profile configuration file, the data set specified on this statement must be checked for the following items as well. If all of the following are true, this is not a finding. If any of the following is untrue, this is a finding. -Within each BEGINVTAM statement block, one BEGINVTAM USSTCP statement is coded that specifies only the table name operand. No client identifier, such as host name or IP address, is specified so the statement applies to all connections not otherwise controlled. -The USS table specified on each "back stop" USSTCP statement mentioned in Item (1) above is coded to allow access only to session manager applications and NC PASS applications. -Within each BEGINVTAM statement block, additional BEGINVTAM USSTCP statements that specify a USS table that allows access to other applications may be coded only if the statements include a client identifier operand that references only secure terminals. -Any BEGINVTAM DEFAULTAPPL statement that does not specify a client identifier, or specifies any type of client identifier that would apply to unsecured terminals, specifies a session manager application or an NC PASS application as the application name. -Any BEGINVTAM LUMAP statement, if used with the DEFAPPL operand and applied to unsecured terminals, specifies only a session manager application or an NC PASS application. NOTE: The BEGINVTAM LINEMODEAPPL requirements will not be reviewed at this time. Further testing must be performed to determine how the CL/Supersession and NC-PASS applications work with line mode.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-223835`

### Rule: The IBM z/OS PROFILE.TCPIP configuration for the TN3270 Telnet server must have the INACTIVE statement properly specified.

**Rule ID:** `SV-223835r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Profile configuration file specified on the PROFILE DD statement in the TN3270 started task JCL. Note: If the INCLUDE statement is coded in the TCP/IP Profile configuration file, the data set specified on this statement must be checked for the following items as well. TELNETGLOBAL Block (only one defined) TELNETPARMS Block (one defined for each port the server is listening to, typically ports 23 and 992) If the TELNETPARMS INACTIVE statement is coded either in the TELNETGLOBALS or within each TELNETPARMS statement block and specifies a value between "1" and "900", this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223836`

### Rule: IBM Z/OS TSOAUTH resources must be restricted to authorized users.

**Rule ID:** `SV-223836r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RLIST SURROGAT * Ensure that all TSOAUTH resources and/or generic equivalent are properly protected according to the requirements specified. If the following guidance is true, this is not a finding. The ACCT authorization is restricted to security personnel. The CONSOLE authorization is restricted to authorized systems personnel (e.g., systems programming personnel, operations staff, etc.) and READ access may be given to all user when SDSF in install at the ISSOs discretion. The MOUNT authorization is restricted to DASD batch users only. The OPER authorization is restricted to authorized systems personnel (e.g., systems programming personnel, operations staff, etc.). The PARMLIB authorization is restricted to only z/OS systems programming personnel and READ access may be given to auditors. The TESTAUTH authorization is restricted to only z/OS systems programming personnel.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-223837`

### Rule: IBM RACF LOGONIDs must not be defined to SYS1.UADS for non-emergency use.

**Rule ID:** `SV-223837r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator to provide a list of all emergency userids available to the site along with the associated function of each. If SYS1.UADS userids are limited and reserved for emergency purposes only, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223838`

### Rule: The IBM z/OS UNIX SUPERUSER resources must be protected in accordance with guidelines.

**Rule ID:** `SV-223838r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RL UNIXPRIV * AUTHUSER If the RACF rules for the SUPERUSER resource specify a default access of NONE, this is not a finding. If there are no RACF rules that allow access to the SUPERUSER resource, this is not a finding. If there is no RACF rule for CHOWN.UNRESTRICTED defined, this is not a finding. If the RACF rules for each of the SUPERUSER resources listed in the z/OS UNIX System Services Planning, Establishing UNIX security, specify a default access of NONE, this is not a finding. If the RACF rules for each of the SUPERUSER resources listed in the z/OS UNIX System Services Planning, Establishing UNIX security, restrict access to appropriate system tasks or systems programming personnel, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223839`

### Rule: IBM z/OS BPX resource(s) must be protected in accordance with security requirements.

**Rule ID:** `SV-223839r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RL FACILITY * AUTHUSER If the RACF rules for the BPX.** resource specify a default access of NONE, this is not a finding. If there are no RACF user access to the BPX.** resource, this is not a finding. If there is no RACF rule for BPX.SAFFASTPATH defined, this is not a finding. If the RACF rules for each of the BPX resources listed in the z/OS UNIX System Services Planning, Establishing UNIX security, restrict access to appropriate system tasks or systems programming personnel, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223840`

### Rule: IBM z/OS UNIX MVS HFS directories with other write permission bit set must be properly defined.

**Rule ID:** `SV-223840r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the OMVS Command line enter the following command string: find / -type d -perm -0002 ! -perm -1000 -exec ls -aldWE {} \; If there are no directories that have the other write permission bit set on without the sticky bit set on, this is not a finding. NOTE: In the symbolic permission bit display, the sticky bit is indicated as a "t" or "T" in the execute portion of the other permissions. For example, a display of the permissions of a directory with the sticky bit on could be "drwxrwxrwt". If all directories that have the other write permission bit set on do not contain any files with the setuid bit set on, this is not a finding. NOTE: In the symbolic permission bit display, the setuid bit is indicated as an "s" or "S" in the execute portion of the owner permissions. For example, a display of the permissions of a file with the setuid bit on could be "-rwsrwxrwx". If all directories that have the other write permission bit set on do not contain any files with the setgid bit set on, this is not a finding. NOTE: In the symbolic permission bit display, the setgid bit is indicated as an "s" or "S" in the execute portion of the group permissions. For example, a display of the permissions of a file with the setgid bit on could be "-rwxrwsrwx".

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223842`

### Rule: IBM z/OS UNIX security parameters in etc/profile must be properly specified.

**Rule ID:** `SV-223842r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ISHELL /etc/profile If the final or only instance of the UMASK command in /etc/profile is specified as "umask 077", this is not a finding. If the LOGNAME variable is marked read-only (i.e., "readonly LOGNAME") in /etc/profile, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223843`

### Rule: IBM z/OS UNIX security parameters in /etc/rc must be properly specified.

**Rule ID:** `SV-223843r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ISHELL /etc/rc If all of the CHMOD commands in /etc/rc do not result in less restrictive access than what is specified in the tables below, this is not a finding. NOTE: The use of CHMOD commands in /etc/rc is required in most environments to comply with the required settings, especially for dynamic objects such as the /dev directory. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) If all of the CHAUDIT commands in /etc/rc do not result in less auditing than what is specified in the tables below, this is not a finding. NOTE: The use of CHAUDIT commands in /etc/rc may not be necessary. If none are found, there is not a finding. The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing If the _BPX_JOBNAME variable is appropriately set (i.e., to match daemon name) as each daemon (e.g., syslogd, inetd) is started in /etc/rc, this is not a finding. NOTE: If _BPX_JOBNAME is not specified, the started address space will be named using an inherited value. This could result in reduced security in terms of operator command access. SYSTEM DIRECTORY SECURITY SETTINGS DIRECTORY PERMISSION BITS USER AUDIT BITS FUNCTION / [root] 755 faf Root level of all file systems. Holds critical mount points. /bin 1755 fff Shell scripts and executables for basic functions /dev 1755 fff Character-special files used when logging into the OMVS shell and during C language program compilation. Files are created during system IPL and on a per-demand basis. /etc 1755 faf Configuration programs and files (usually with locally customized data) used by z/OS UNIX and other product initialization processes /lib 1755 fff System libraries including dynamic link libraries and files for static linking /samples 1755 fff Sample configuration and other files /tmp 1777 fff Temporary data used by daemons, servers, and users. Note: /tmp must have the sticky bit on to restrict file renames and deletions. /u 1755 fff Mount point for user home directories and optionally for third-party software and other local site files /usr 1755 fff Shell scripts, executables, help (man) files and other data. Contains sub-directories (e.g., lpp) and mount points used by program products that may be in separate file systems. /var 1775 fff Dynamic data used internally by products and by elements and features of z/OS UNIX. SYSTEM FILE SECURITY SETTINGS FILE PERMISSION BITS USER AUDIT BITS FUNCTION /bin/sh 1755 faf z/OS UNIX shell Note: /bin/sh has the sticky bit on to improve performance. /dev/console 740 fff The system console file receives messages that may require System Administrator (SA) attention. /dev/null 666 fff A null file; data written to it is discarded. /etc/auto.master and any mapname files 740 faf Configuration files for automount facility /etc/inetd.conf 740 faf Configuration file for network services /etc/init.options 740 faf Kernel initialization options file for z/OS UNIX environment /etc/log 744 fff Kernel initialization output file /etc/profile 755 faf Environment setup script executed for each user /etc/rc 744 faf Kernel initialization script for z/OS UNIX environment /etc/steplib 740 faf List of MVS data sets valid for set user ID and set group ID executables /etc/tablename 740 faf List of z/OS userids and group names with corresponding alias names /usr/lib/cron/at.allow /usr/lib/cron/at.deny 700 faf Configuration files for the at and batch commands /usr/lib/cron/cron.allow /usr/lib/cron/cron.deny 700 faf Configuration files for the crontab command

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223844`

### Rule: IBM z/OS UNIX resources must be protected in accordance with security requirements.

**Rule ID:** `SV-223844r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000326-GPOS-00126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RL SURROGAT BPX.SRV AUTHUSER If the RACF rules for all BPX.SRV.user SURROGAT resources specify a default access of NONE, this is not a finding. If the RACF rules for all BPX.SRV.user SURROGAT resources restrict access to system software processes (e.g., web servers) that act as servers under z/OS UNIX, this is not a finding. If the RACF rules for all BPX.SRV.user SURROGAT resources restrict access to authorized users identified in the Site Security Plan, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223845`

### Rule: IBM z/OS UNIX MVS data sets or HFS objects must be properly protected.

**Rule ID:** `SV-223845r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the proper BPXPRMxx member in SYS1.PARMLIB If the ESM data set rules for the data sets referenced in the ROOT and the MOUNT statements in BPXPRMxx restrict update access to the z/OS UNIX kernel (i.e., OMVS or OMVSKERN), this is not a finding. If the ESM data set rules for the data set referenced in the ROOT and the MOUNT statements in BPXPRMxx restrict update and/or allocate access to systems programming personnel, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223846`

### Rule: IBM z/OS UNIX MVS data sets WITH z/OS UNIX COMPONENTS must be properly protected.

**Rule ID:** `SV-223846r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute an access list for MVS DATA SETS WITH z/OS UNIX COMPONENTS. If the ESM data set rules for each of the data sets listed in the table below restrict UPDATE and ALLOCATE access to systems programming personnel, this is not a finding. MVS DATA SETS WITH z/OS UNIX COMPONENTS DATA SET NAME/MASK MAINTENANCE TYPE FUNCTION SYS1.ABPX* Distribution IBM z/OS UNIX ISPF panels, messages, tables, clists SYS1.AFOM* Distribution IBM z/OS UNIX Application Services SYS1.BPA.ABPA* Distribution IBM z/OS UNIX Connection Scaling Process Mgr. SYS1.CMX.ACMX* Distribution IBM z/OS UNIX Connection Scaling Connection Mgr. SYS1.SBPX* Target IBM z/OS UNIX ISPF panels, messages, tables, clists SYS1.SFOM* Target IBM z/OS UNIX Application Services SYS1.CMX.SCMX* Target IBM z/OS UNIX Connection Scaling Connection Mgr.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223847`

### Rule: IBM z/OS UNIX HFS permission bits and audit bits for each directory must be properly protected.

**Rule ID:** `SV-223847r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs enter CD / enter ls -alW If the HFS permission bits and user audit bits for each directory and file match or are more restrictive than the specified settings listed in the SYSTEM DIRECTORY SECURITY SETTINGS table below, this is not a finding. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing SYSTEM DIRECTORY SECURITY SETTINGS DIRECTORY PERMISSION BITS USER AUDIT BITS FUNCTION / [root] 755 faf Root level of all file systems. Holds critical mount points. /bin 1755 fff Shell scripts and executables for basic functions /dev 1755 fff Character-special files used when logging into the OMVS shell and during C language program compilation. Files are created during system IPL and on a per-demand basis. /etc 1755 faf Configuration programs and files (usually with locally customized data) used by z/OS UNIX and other product initialization processes /lib 1755 fff System libraries including dynamic link libraries and files for static linking /samples 1755 fff Sample configuration and other files /tmp 1777 fff Temporary data used by daemons, servers, and users. Note: /tmp must have the sticky bit on to restrict file renames and deletions. /u 1755 fff Mount point for user home directories and optionally for third-party software and other local site files /usr 1755 fff Shell scripts, executables, help (man) files and other data. Contains sub-directories (e.g., lpp) and mount points used by program products that may be in separate file systems. /var 1775 fff Dynamic data used internally by products and by elements and features of z/OS UNIX.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223848`

### Rule: IBM z/OS UNIX SYSTEM FILE SECURITY SETTINGS must be properly protected or specified.

**Rule ID:** `SV-223848r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: OMVS For each file listed in the table below enter: ls -alW /<directory name>/<file name> If the HFS permission bits and user audit bits for each directory and file match or are more restrictive than the specified settings listed in the table, this is not a finding. NOTE: Some of the files listed are not used in every configuration. Absence of any of the files is not considered a finding. SYSTEM FILE SECURITY SETTINGS FILE PERMISSION BITS USER AUDIT BITS FUNCTION /bin/sh 1755 faf z/OS UNIX shell Note: /bin/sh has the sticky bit on to improve performance. /dev/console 740 fff The system console file receives messages that may require System Administrator (SA) attention. /dev/null 666 fff A null file; data written to it is discarded. /etc/auto.master any mapname files 740 faf Configuration files for automount facility /etc/inetd.conf 740 faf Configuration file for network services /etc/init.options 740 faf Kernel initialization options file for z/OS UNIX environment /etc/log 744 fff Kernel initialization output file /etc/profile 755 faf Environment setup script executed for each user /etc/rc 744 faf Kernel initialization script for z/OS UNIX environment /etc/steplib 740 faf List of MVS data sets valid for set user ID and set group ID executables /etc/tablename 740 faf List of z/OS userids and group names with corresponding alias names /usr/lib/cron/at.allow /usr/lib/cron/at.deny 700 faf Configuration files for the at and batch commands /usr/lib/cron/cron.allow /usr/lib/cron/cron.deny 700 faf Configuration files for the crontab command NOTE: Some of the files listed are not used in every configuration. Absence of any of the files is not considered a finding. NOTE: The names of the MapName files are site-defined. Refer to the listing in the EAUTOM report. The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223849`

### Rule: IBM z/OS UNIX MVS data sets used as step libraries in /etc/steplib must be properly protected.

**Rule ID:** `SV-223849r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the pathname from the STEPLIBLIST line in BPXPRMxx member of PARMLIB. From the ISPF Command Shell enter: ISHELL On the command line: on the path name line enter: /etc/ From the resulting display scroll down to the <stepliblist name> from BPXPRMxx parm. Enter B for browse on that line. If ESM data set rules for libraries specified restrict WRITE or greater access to only systems programming personnel, this is not a finding. If the ESM data set rules for libraries specify that all (i.e., failures and successes) WRITE or greater access will be logged, this is not a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-223850`

### Rule: The IBM RACF classes required to properly secure the z/OS UNIX environment must be ACTIVE.

**Rule ID:** `SV-223850r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: SETRopts list If the ACTIVE CLASSES list includes entries for the FACILITY, SURROGAT, and UNIXPRIV resource classes, this is not a finding. If either of the above resource classes is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223851`

### Rule: IBM z/OS UNIX OMVS parameters in PARMLIB must be properly specified.

**Rule ID:** `SV-223851r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the IEASYS00 member of SYS1.PARMLIB. If the parameter is specified as OMVS=xx or OMVS=(xx,xx,...) in the IEASYSxx member, this is not a finding. If the OMVS statement is not specified, OMVS=DEFAULT is used. In minimum mode there is no access to permanent file systems or to the shell, and IBM's Communication Server TCP/IP will not run.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223852`

### Rule: IBM z/OS UNIX BPXPRMxx security parameters in PARMLIB must be properly specified.

**Rule ID:** `SV-223852r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the BPXPRM00 member of SYS1.PARMLIB. If the required parameter keywords and values are defined as detailed below, this is not a finding. Parameter Keyword Value SUPERUSER BPXROOT TTYGROUP TTY STEPLIBLIST /etc/steplib USERIDALIASTABLE Will not be specified. ROOT SETUID will be specified MOUNT NOSETUID SETUID (for Vendor-provided files)SECURITY STARTUP_PROC OMVS

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223853`

### Rule: IBM z/OS default profiles must be defined in the corresponding FACILITY Class Profile for classified systems.

**Rule ID:** `SV-223853r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not classified, this is Not Applicable. From a command input screen enter: RLIST FACILITY (BPX.UNIQUE.USER) ALL Examine APPLICATION DATA for userid If system is classified and a userid is are not defined in the Application Data field in the BPX.UNIQUE.USER resource in the FACILITY report, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-223854`

### Rule: IBM z/OS UNIX HFS MapName files security parameters must be properly specified.

**Rule ID:** `SV-223854r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removal of unneeded or non-secure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources. The organization must perform a periodic scan/review of the application (as required by CCI-000384) and disable functions, ports, protocols, and services deemed to be unneeded or non-secure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the logical parmlib data sets, example: SYS1.PARMLIB(BPXPRMxx), for the following FILESYSTYPE entry: FILESYSTYPE TYPE(AUTOMNT) ENTRYPOINT(BPXTAMD) If the above entry is not found or is commented out in the BPXPRMxx member(s), this is Not Applicable. From the ISPF Command Shell enter: OMVS cd /etc cat auto.master perform a contents list for the file identified Example: cat u.map Note: The /etc/auto.master HFS file (and the use of Automount) is optional. If the file does not exist, this is not applicable. Note: The setuid parameter and the security parameter have a significant security impact. For this reason these parameters must be explicitly specified and not allowed to default. If each MapName file specifies the "setuid No" and "security Yes" statements for each automounted directory, this is not a finding. If there is any deviation from the required values, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-223855`

### Rule: IBM z/OS UNIX security parameters for restricted network service(s) in /etc/inetd.conf must be properly specified.

**Rule ID:** `SV-223855r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the UNIX System Services ISPF Shell enter: /etc/inetd.conf If any Restricted Network Services that are listed below are specified or specified but not commented out, this is a finding. RESTRICTED NETWORK SERVICES/PORTS Service Port Chargen 19 Daytime 13 Discard 9 Echo 7 Exec 512 finger 79 shell 514 time 37 login 513 smtp 25 timed 525 nameserver 42 systat 11 uucp 540 netstat 15 talk 517 qotd 17 tftp 69

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223856`

### Rule: IBM z/OS UID(0) must be properly assigned.

**Rule ID:** `SV-223856r958482_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a z/OS command screen enter: SR CLASS(USER) UID(0) If UID(0) is assigned only to system tasks such as the z/OS/ UNIX kernel (i.e., OMVS), z/OS UNIX daemons (e.g., inetd, syslogd, ftpd), and other system software daemons, this is not a finding. If UID(0) is assigned to security administrators who create or maintain user account definitions; and to systems programming accounts dedicated to maintenance (e.g., SMP/E) of HFS-based components, this not a finding. NOTE: The assignment of UID(0) confers full time superuser privileges. This is not appropriate for personal user accounts. Access to the BPX.SUPERUSER resource is used to allow personal user accounts to gain short-term access to superuser privileges. If UID(0) is assigned to non-systems or non-maintenance accounts, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223857`

### Rule: IBM z/OS UNIX groups must be defined with a unique GID.

**Rule ID:** `SV-223857r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. RACF userid groups, and started tasks that use z/OS UNIX facilities are defined to an ACP with attributes including UID and GID. If these attributes are not correctly defined, data access or command privilege controls could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From ISPF Command Shell enter: Listgrp * OMVS If each group is defined with a unique GID, this is not a finding. Note: A site can choose to have both an OMVSGRP group and an STCOMVS group or combine the groups under one of these names. If OMVSGRP and/or STCOMVS groups are defined and have a unique GID in the range of 1-99, this is not a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223859`

### Rule: The IBM z/OS user account for the UNIX kernel (OMVS) must be properly defined to the security database.

**Rule ID:** `SV-223859r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If OMVS userid is defined to the ESM as follows, this is not a finding. No access to interactive on-line facilities (e.g., TSO, CICS, etc.) Default group specified as OMVSGRP or STCOMVS UID(0) HOME directory specified as "/" Shell program specified as "/bin/sh"

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223860`

### Rule: The IBM z/OS user account for the z/OS UNIX SUPERUSER userid must be properly defined.

**Rule ID:** `SV-223860r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to system PARMLIB member BPXPRMxx (xx is determined by OMVS entry in IEASYS00.) Determine the user ID identified by the SUPERUSER parameter. (BPXROOT is the default). From a command input screen enter: LISTUSER (superuser userid) TSO CICS OMVS If the SUPERUSER userid is defined as follows, this is not a finding: -No access to interactive on-line facilities (e.g., TSO, CICS, etc.) -Default group specified as OMVSGRP or STCOMVS -UID(0) -HOME directory specified as "/" -Shell program specified as "/bin/sh"

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223861`

### Rule: The IBM z/OS user account for the UNIX (RMFGAT) must be properly defined.

**Rule ID:** `SV-223861r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
RMFGAT is the userid for the Resource Measurement Facility (RMF) Monitor III Gatherer. If RMFGAT is not defined, this is Not Applicable. From a command input screen enter: LISTUSER (RMFGAT) OMVS If RMFGAT is defined as follows, this is not a finding. Default group specified as OMVSGRP or STCOMVS A unique, non-zero UID HOME directory specified as "/" Shell program specified as "/bin/sh"

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223862`

### Rule: IBM z/OS UNIX user accounts must be properly defined.

**Rule ID:** `SV-223862r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a z/OS command screen enter: LISTUSER * OMVS NORACF NOTE: This check only applies to users of z/OS UNIX (i.e., users with an OMVS profile defined). If each user account with an OMVS segment is defined as follows, this is not a finding. -A unique UID number (except for UID(0) users). -A unique HOME directory (UID(0), other system task accounts, and tasks approved by the ISSM are excluded from this rule). -Shell program specified as "/bin/sh", "/bin/tcsh", "/bin/echo", or "/bin/false". NOTE: The shell program must have one of the specified values. The HOME directory must have a value (i.e., not be allowed to default; this does not include tasks that are excluded from above).

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-223863`

### Rule: IBM z/OS attributes of UNIX user accounts used for account modeling must be defined in accordance with security requirements.

**Rule ID:** `SV-223863r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is a Classified system, and there is an account used for modeling, this is a finding. From a command input screen enter: RLIST FACILITY (BPX.UNIQUE.USER) ALL Examine APPLICATION DATA for userid Enter: List User (<userid>) Note: This check applies to any user id used to model OMVS access on the mainframe. This includes the OMVS default user and BPX.UNIQUE.USER. If the OMVS default user or BPX.UNIQUE.USER is not defined in the FACILITY report, this is Not Applicable. If user account used for OMVS account modeling is defined as follows, this is not a finding: A non-writable HOME directory: Shell program specified as "/bin/echo" or "/bin/false" Note: The shell program must have one of the specified values. The HOME directory must have a value (i.e., not be allowed to default).

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223864`

### Rule: The IBM z/OS startup user account for the z/OS UNIX Telnet Server must be properly defined.

**Rule ID:** `SV-223864r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The PROFILE.TCPIP configuration file provides system operation and configuration parameters for the TN3270 Telnet Server. Several of these parameters have potential impact to system security. Failure to code the appropriate values could result in unexpected operations and degraded security. This exposure may result in unauthorized access impacting data integrity or the availability of some system services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs cd /etc cat inetd.conf If the otelnetd command specifies any user other than OMVS or OMVSKERN, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223865`

### Rule: IBM z/OS HFS objects for the z/OS UNIX Telnet Server must be properly protected.

**Rule ID:** `SV-223865r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>HFS directories and files of the z/OS UNIX Telnet Server provide the configuration and executable properties of this product. Failure to properly secure these objects may lead to unauthorized access resulting in the compromise of the integrity and availability of the operating system environment, ACP, and customer data. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: omvs At the input line enter cd /usr enter ls -alW If the following File permission and user Audit Bits are true, this is not a finding. /usr/sbin/otelnetd 1740 fff cd /etc ls -alW If the following file permission and user Audit Bits are true, this is not a finding. /etc/banner 0744 faf The following represents a hierarchy for permission bits from least restrictive to most restrictive: 7 rwx (least restrictive) 6 rw- 3 -wx 2 -w- 5 r-x 4 r-- 1 --x 0 --- (most restrictive) The possible audit bits settings are as follows: f log for failed access attempts a log for failed and successful access - no auditing

## Group: SRG-OS-000024-GPOS-00007

**Group ID:** `V-223866`

### Rule: The IBM z/OS UNIX Telnet Server etc/banner file must have the Standard Mandatory DoD Notice and Consent Banner.

**Rule ID:** `SV-223866r958392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A logon banner can be used to inform users about the environment during the initial logon. Logon banners are used to warn users against unauthorized entry and the possibility of legal action for unauthorized users, and advise all users that system use constitutes consent to monitoring. Failure to display a logon warning banner without this type of information could adversely impact the ability to prosecute unauthorized users and users who abuse the system. Satisfies: SRG-OS-000024-GPOS-00007, SRG-OS-000023-GPOS-00006</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From UNIX System Services ISPF Shell, enter path "/etc/otelnet/banner/". If this file does not contain the banner below, check the UNIX System Services ISPF Shell path /etc/banner If neither file contains the banner below this is a finding. This banner is mandatory and deviations are not permitted except as authorized in writing by the DoD Chief Information Officer. The thrust of this new policy is to make it clear that there is no expectation of privacy when using DoD information systems and all use of DoD information systems is subject to searching, auditing, inspecting, seizing, and monitoring, even if some personal use of a system is permitted: STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-223867`

### Rule: IBM z/OS UNIX Telnet server Startup parameters must be properly specified.

**Rule ID:** `SV-223867r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The z/OS UNIX Telnet Server (i.e., otelnetd) provides interactive access to the z/OS UNIX shell. During the initialization process, startup parameters are read to define the characteristics of each otelnetd instance. Some of these parameters have an impact on system security. Failure to specify the appropriate command options could result in degraded security. This exposure may result in unauthorized access impacting data integrity or the availability of some system services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ISHELL Enter /etc/ for a pathname - you may need to issue a CD /etc/ select FILE NAME inetd.conf If Option -D login is included on the otelnetd command, this is not a finding. If Option -c 900 is included on the otelnetd command, this is not a finding. NOTE: "900" indicates a session timeout value of "15" minutes and is currently the maximum value allowed.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-223868`

### Rule: The IBM z/OS UNIX Telnet server warning banner must be properly specified.

**Rule ID:** `SV-223868r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: ISHELL Enter /etc/ for a pathname - you may need to issue a CD /etc/ select FILE NAME inetd.conf If Option -h is included on the otelnetd command, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-223869`

### Rule: IBM z/OS System datasets used to support the VTAM network must be properly secured.

**Rule ID:** `SV-223869r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine data set names containing all VTAM start options, configuration lists, network resource definitions, commands, procedures, exit routines, all SMP/E TLIBs, and all SMP/E DLIBs used for installation and in development/production VTAM environments. If RACF data set rules for all VTAM system data sets restrict access to only network systems programming staff, this is not a finding. If RACF data set rules for all VTAM system data sets all READ access to auditors only, this is not a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-223870`

### Rule: IBM z/OS VTAM USSTAB definitions must not be used for unsecured terminals.

**Rule ID:** `SV-223870r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator to supply the following information: - Documentation regarding terminal naming standards. - Documentation of all procedures controlling terminal logons to the system. - A complete list of all USS commands used by terminal users to log on to the system. - Members and data set names containing USSTAB and LOGAPPL definitions of all terminals that can log on to the system (e.g., SYS1.VTAMLST). - Members and data set names containing logon mode parameters. If USSTAB definitions are only used for secure terminals (e.g., terminals that are locally attached to the host or connected to the host via secure leased lines), this is not a finding. If USSTAB definitions are used for any unsecured terminals (e.g., dial up terminals or terminals attached to the Internet such as TN3270 or KNET 3270 emulation), this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-230209`

### Rule: The IBM RACF System REXX IRRPHREX security data set must be properly protected.

**Rule ID:** `SV-230209r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the zOS system REXXLIB concatenation found in SYS1. PARMLIB (AXR) for the data set that contains the REXX for Password exit named IRRPHREX and the defined AXRUSER. If the following guidance is true, this is not a finding. -RACF data set access authorizations restrict READ to AXRUSER, z/OS systems programming personnel, security personnel, and auditors. -RACF data set access authorizations restrict UPDATE to security personnel using a documented change management procedure to provide a mechanism for access and revoking of access after use. -All (i.e., failures and successes) data set access authorities (i.e., READ, UPDATE, and CONTROL) is logged. -RACF data set access authorizations specify UACC(NONE) and NOWARNING.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-230210`

### Rule: IBM RACF exit ICHPWX11 for password phrases must be installed and properly configured.

**Rule ID:** `SV-230210r998382_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password phrase helps to increase the time and resources required to compromise the password. Password phrase complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password phrase complexity is one factor of several that determines how long it takes to crack a password. The more complex the password phrase, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a system console screen issue the following modify command: F AXR,IRRPHREX LIST Review the results of the modify command. If all of the following options are listed, this is not a finding. -The number of required character types is four. (ensures that at least one uppercase, one lowercase, one number, and one special character is used in password phrase) -The user's name is not contained in the password phrase. (Only three consecutive characters of the user's name are allowed) -The minimum password phrase length checked is 15. -The user ID is not contained in the password phrase. (Only three consecutive characters of the user ID are allowed) -The new password phrase is at least 50 percent changed positions of the old password phrase. (These positions need to be consecutive to cause a failure and this check is not case sensitive) -A minimum list of eight restricted words are being checked: 'IBM' , 'RACF', 'PASSWORD', 'PHRASE', 'PASSPHRASE', 'SECRET', 'IBMUSER', 'SYS1' If the modify command fails or returns the following message in the system log, this is a finding. IRX0406E REXX exec load file REXXLIB does not contain exec member IRRPHREX.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-235033`

### Rule: IBM RACF must limit WRITE or greater access to LINKLIST libraries to system programmers only.

**Rule ID:** `SV-235033r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The primary function of the LINKLIST is to serve as a single repository for commonly used system modules. Failure to ensure that the proper set of libraries is designated for LINKLIST can impact system integrity, performance, and functionality. For this reason, controls must be employed to ensure that the correct set of LINKLIST libraries is used. Unauthorized access could result in the compromise of the operating system environment, ACP, and customer data. Satisfies: SRG-OS-000080-GPOS-00048, SRG-OS-000259-GPOS-00100, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From Any ISPF input line, enter: TSO ISRDDN LINKLIST If all of the following are untrue, this is not a finding. If any of the following is true, this is a finding. -The ACP data set rules for LINKLIST libraries do not restrict WRITE or greater access to only z/OS systems programming personnel. -The ACP data set rules for LINKLIST libraries do not specify that all (i.e., failures and successes) WRITE or greater access will be logged.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-245536`

### Rule: The IBM z/OS TCPIP.DATA configuration statement must contain the DOMAINORIGIN or DOMAIN specified for each TCP/IP defined.

**Rule ID:** `SV-245536r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed which would result in query failure or denial of service. Data origin authentication verification must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching Domain Name System (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. This is not applicable if DNSSEC is not implemented on the local network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the Data configuration file specified on the SYSTCPD DD statement in the TCPIP started task JCL. Note: If GLOBALTCPIPDATA is specified, any TCPIP.DATA statements contained in the specified file or data set take precedence over any TCPIP.DATA statements found using the appropriate environment's (native MVS or z/OS UNIX) search order. If GLOBALTCPIPDATA is not specified, the appropriate environment's (Native MVS or z/OS UNIX) search order is used to locate TCPIP.DATA. If the DOMAINORIGIN/DOMAIN (the DOMAIN statement is functionally equivalent to the DOMAINORIGIN statement) is specified in the TCP/IP Data configuration file, this is not a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-251107`

### Rule: IBM z/OS sensitive and critical system data sets must not exist on shared DASDs.

**Rule ID:** `SV-251107r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check HMC, VM, and z/OS on how to validate and determine a DASD volume(s) is shared. Note: In VM issue the command "QUEUE DASD SYSTEM" this display will show shared volume(s) and indicates the number of systems sharing the volume. Validate all machines that require access to these shared volume(s) have the volume(s) mounted. Obtain a map or list VTOC of the shared volume(s). Check if shared volume(s) contain any critical or sensitive data sets. Identify shared and critical or sensitive data sets on the system being audited. These data sets can be APF, LINKLIST, LPA, Catalogs, etc, as well as product data sets. If all of the critical or sensitive data sets identified on shared volume(s) are protected and justified to be on shared volume(s), this is not a finding. List critical or sensitive data sets are possible security breaches, if not justified and not protected on systems having access to the data set(s) and on shared volume(s).

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-252553`

### Rule:  IBM z/OS TCP/IP AT-TLS policy must be properly configured in Policy Agent.

**Rule ID:** `SV-252553r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If events associated with nonlocal administrative access or diagnostic sessions are not logged, a major tool for assessing and investigating attacks would not be available. This requirement addresses auditing-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational information systems. Nonlocal maintenance and diagnostic activities are conducted by individuals communicating through an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are carried out by individuals physically present at the information system or information system component and not communicating across a network connection. This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system; for example, the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the z/OS UNIX pasearch -t command to query information from the z/OS UNIX Policy Agent. The command is issued from the UNIX System Services shell. Examine the results for AT-TLS initiation and control statements. If there are no AT-TLS initiation and controls statements this is a finding. Verify the statements specify a FIPS 140-2 compliant value. If none of the following values are present, this is a finding ECDHE_ECDSA_AES_128_CBC_SHA256 ECDHE_ECDSA_AES_256_CBC_SHA384 ECDHE_RSA_AES_128_CBC_SHA256 ECDHE_RSA_AES_256_CBC_SHA384 TLS_RSA_WITH_3DES_EDE_CBC_SHA TLS_RSA_WITH_AES_128_CBC_SHA TLS_RSA_WITH_AES_128_CBC_SHA256 TLS_RSA_WITH_AES_256_CBC_SHA TLS_RSA_WITH_AES_256_CBC_SHA256

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-255935`

### Rule: IBM Integrated Crypto Service Facility (ICSF) Configuration parameters must be correctly specified.

**Rule ID:** `SV-255935r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Integrated Crypto Service Facility (ICSF) product has the ability to use privileged functions and/or have access to sensitive data. Failure to properly configure parameter values could potentially the integrity of the base product which could result in compromising the operating system or sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the CSFPRMxx member in the logical PARMLIB concatenation. If the configuration parameters are specified as follows this is not a finding. REASONCODES(ICSF) COMPAT(NO) SSM(NO) SSM can be dynamically set by defining the CSF.SSM.ENABLE SAF profile within the XFACILIT resource Class. If this profile is not limited to authorized personnel this is a finding. CHECKAUTH(YES) FIPSMODE(YES,FAIL(YES)) AUDITKEYLIFECKDS (TOKEN(YES),LABEL(YES)). AUDITKEYLIFEPKDS (TOKEN(YES),LABEL(YES)). AUDITKEYLIFETKDS (TOKENOBJ(YES),SESSIONOBJ(YES)). AUDITKEYUSGCKDS (TOKEN(YES),LABEL(YES),INTERVAL(n)). AUDITKEYUSGPKDS (TOKEN(YES),LABEL(YES),INTERVAL(n)). AUDITPKCS11USG (TOKENOBJ(YES),SESSIONOBJ(YES),NOKEY(YES),INTERVAL(n)). DEFAULTWRAP -This parameter can be determined by the site. ENHANCED wrapping specifies the new X9.24 compliant CBC wrapping is used. If DEFAULTWRAP is not specified, the default wrapping method will be ORIGINAL for both internal and external tokens. Starting with ICSF FMID HCR77C0, the value for this option can be updated without restarting ICSF by using either the SETICSF command or the ICSF Multi-Purpose service. If this access is not restricted to appropriate personnel, this is a finding. ( Note: Other options may be site defined.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-255936`

### Rule: IBM Integrated Crypto Service Facility (ICSF) install data sets are not properly protected.

**Rule ID:** `SV-255936r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Integrated Crypto Service Facility (ICSF) product has the ability to use privileged functions and/or have access to sensitive data. Failure to properly restrict access to their data sets could result in violating the integrity of the base product which could result in compromising the operating system or sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESM dataset rules for the IBM Integrated Crypto Service Facility (ICSF) install data sets does not restrict UPDATE and/or ALTER access to systems programming personnel this is a finding. If the ESM data set rules for IBM Integrated Crypto Service Facility (ICSF) install data set does not specify that all (i.e., failures and successes) UPDATE and/or ALTER access will be logged this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-255937`

### Rule: IBM Integrated Crypto Service Facility (ICSF) Started Task name is not properly identified / defined to the system ACP.

**Rule ID:** `SV-255937r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Integrated Crypto Service Facility (ICSF) requires a started task that will be restricted to certain resources, datasets and other system functions. By defining the started task as a userid to the system ACP, It allows the ACP to control the access and authorized users that require these capabilities. Failure to properly control these capabilities, could compromise of the operating system environment, ACP, and customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell- enter ListUser If the userid(s) for the IBM Integrated Crypto Service Facility (ICSF) started task is not defined to the security database, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-255938`

### Rule: IBM Integrated Crypto Service Facility (ICSF) Started task(s) must be properly defined to the STARTED resource class for RACF.

**Rule ID:** `SV-255938r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access to product resources should be restricted to only those individuals responsible for the application connectivity and who have a requirement to access these resources. Improper control of product resources could potentially compromise the operating system, ACP, and customer data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the RACF DSMON report for RACSPT if the IBM Integrated Crypto Service Facility (ICSF) started task(s) is (are) not defined to the STARTED resource class profile and/or ICHRIN03 table entry this is a finding

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-255939`

### Rule: IBM Integrated Crypto Service Facility (ICSF) STC data sets must be properly protected.

**Rule ID:** `SV-255939r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Integrated Crypto Service Facility (ICSF) STC data sets have the ability to use privileged functions and/or have access to sensitive data. Failure to properly restrict access to their data sets could result in violating the integrity of the base product which could result in compromising the operating system or sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that access to the IBM Integrated Crypto Service Facility (ICSF) STC data sets are properly restricted. The data sets to be protected are identified in the data set referenced in the CSFPARM DD statement of the ICSF started task(s) and/or batch job(s); the entries for CKDSN and PKDSN specify the data sets. If the RACF data set access authorizations do not restrict READ access to auditors, this is a finding If the RACF data set access authorizations do not restrict WRITE and/or greater access to systems programming personnel, this is a finding. If the RACF data set access authorizations do not restrict WRITE and/or greater access to the product STC(s) and/or batch job(s), this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-257135`

### Rule: IBM Passtickets must be configured to be KeyEncrypted.

**Rule ID:** `SV-257135r998383_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords such as IBM Passtickets need to be protected at all times, and encryption is the standard method for protecting such passwords. If passwords are not encrypted, they may be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF Command Shell enter: RList PTKTDATA * SSIGNON NORACF If any profile is not defined as KEYENCRYPTED, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-272875`

### Rule: IBM z/OS FTP Control cards must be properly stored in a secure PDS file.

**Rule ID:** `SV-272875r1082845_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organizationwide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DOD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Provide a list(s) of the locations for all FTP Control cards within a given application/AIS, ensuring no FTP control cards are within in-stream JCL, JCL libraries, or any open access data sets. The list(s) must indicate which application uses the PDS and access requirements for those PDSs (who and what level of access). Lists/spreadsheets used for documenting the meeting of this requirement must be maintained by the responsible Application/AIS Team, available upon request and not maintained by the Mainframe ISSO. Obtain the list/spreadsheet from the Application/AIS Team. Access to FTP scripts and/or data files located on host system(s) that contain FTP userid and or password will be restricted to those individuals responsible for the application connectivity and who have a legitimate requirement to know the userid and password on a remote system. FTP Control Cards within in-stream JCL, within JCL libraries, or open access libraries/data sets is a finding. If there is anyone not listed within the spreadsheet by userid that has access of Read or greater to the FTP control cards, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-272877`

### Rule: IBM z/OS started tasks for the Base TCP/IP component must be defined in accordance with security requirements.

**Rule ID:** `SV-272877r1083016_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to system Proclibs to determine the TCPIP address space(s). From the ISPF Command Shell, enter: LISTUSER<TCPIP STCs> OMVS For each TCPIP: -Named TCPIP or, in the case of multiple instances, prefixed with TCPIP. -Has the STC facility. -z/OS Unix attributes: UID(0), HOME directory '/', shell program /bin/sh If all of the following items are true, this is not a finding. If any item is untrue, this is a finding. From the ISPF Command Shell, enter: LISTUSER EZAZSSI OMVS If EZAZSSI STC has the STC facility, this is not finding. Ensure the following items are in effect for the ACID assigned to the EZAZSSI started task: -Named EZAZSSI. -Has the STC facility.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-272879`

### Rule: IBM z/OS DFSMS control data sets must reside on separate storage volumes

**Rule ID:** `SV-272879r1082934_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the logical parmlib data sets, for example SYS1.PARMLIB(IGDSMSxx), to identify the fully qualified file names for the following SMS data sets: Active Control Data Set (ACDS) Communications Data Set (COMMDS) If the COMMDS and ACDS SMS data sets identified above reside on different volumes, this is not a finding. If the COMMDS and ACDS SMS data sets identified above are collocated on the same volume, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-275952`

### Rule: zOSMF resource class(es) must be active in accordance with security requirements.

**Rule ID:** `SV-275952r1115942_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF command shell enter: SETRopts list If the ACTIVE CLASSES list the EJBROLE, LOGSTRM, SERVER, TSOPROC, ZMFAPLA, and ZMFCLOUD, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-275953`

### Rule: The ICSF resource class(es) must be active in accordance with security requirements.

**Rule ID:** `SV-275953r1115944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF command shell, enter: SETRopts list If the ACTIVE CLASSES list the CRYPTOZ, CSFKEYS, CSFSERV, GCSFKEYS , GXCSFKEY, and XCSFKEY resource classes, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-275954`

### Rule:  ICSF resources must be protected in accordance with security requirements.

**Rule ID:** `SV-275954r1115945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF command shell, for each appropriate resource class, enter: RL <Class> * AUTHUSER If ACF2 access rules for each resource is restricted to appropriate users, this is not a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-275956`

### Rule: zOSMF resources must be protected in accordance with security requirements.

**Rule ID:** `SV-275956r1115943_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ISPF command shell, for each appropriate resource class, enter: RL <Class> * AUTHUSER If RACF access rules for each resource in the zOSMF Configuration Guide, and the security setup requirements for the Security Configuration Assistant service is restricted to appropriate users, this is not a finding.

