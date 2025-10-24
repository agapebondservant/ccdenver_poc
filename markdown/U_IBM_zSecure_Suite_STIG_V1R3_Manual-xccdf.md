# STIG Benchmark: IBM zSecure Suite Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000133-MFP-000192

**Group ID:** `V-259728`

### Rule: Access to IBM Security zSecure installation data sets must be properly restricted and logged.

**Rule ID:** `SV-259728r1050748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the zSecure application were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to applications with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components to initiate changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the accesses to zSecure installation data sets are properly restricted. - The RACF profile(s) protecting zSecure installation data sets must not allow general access by means of UACC, ID(*), WARNING, or global access. - The RACF profile(s) protecting zSecure installation data sets must restrict READ access to auditors, security administrators , decentralized security administrators, batch jobs that perform External Security Manager (ESM) maintenance, and trusted STC users. - The RACF profile(s) protecting zSecure installation data sets must restrict UPDATE and higher access to systems programmers. - All failures and successful UPDATE and higher access must be logged. If all of the above restrictions are true, this is not a finding.

## Group: SRG-APP-000133-MFP-000193

**Group ID:** `V-259729`

### Rule: Access to IBM Security zSecure STC data sets must be properly restricted and logged.

**Rule ID:** `SV-259729r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IBM Security zSecure STC have the ability to use privileged functions and/or have access to sensitive data. Failure to properly restrict access to these zSecure STC data sets could result in violating the integrity of the base product, which could compromise the operating system or sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that access to the zSecure STC data sets is properly restricted. If the following guidance is true, this is not a finding. - The RACF profiles protecting zSecure STC data sets do not allow general access by means of UACC, ID(*), WARNING, or global access. - READ and higher access to zAlert CKFREEZE data sets is restricted to trusted STC users and systems programmers. - READ access to Access Monitor output data sets is restricted to auditors, decentralized security administrators, security administrators, automated operation STCs/batch jobs, batch jobs performing ESM maintenance, trusted STC users, and systems programmers. - UPDATE access to Access Monitor output data sets is restricted to automated operation STCs/batch jobs, batch jobs performing ESM maintenance, trusted STC users, and systems programmers. - CONTROL and higher access to Access Monitor output data sets is restricted to trusted STC users and systems programmers. - All failures and successful UPDATE and higher access to zSecure STC data sets is logged. DASD-only CKXLOG log stream resources in the LOGSTRM class: - READ is restricted to security administrators, auditors, batch jobs performing ESM maintenance - ALTER restricted to CKXLOG task, system programmers, and batch jobs performing ESM maintenance * For Coupling-Facility CKXLOG log streams, the above applies in addition to checking the IXLSTR.model_structure_name profiles in the FACILITY class: - UPDATE and higher trusted STC users, and systems programmers.

## Group: SRG-APP-000133-MFP-000194

**Group ID:** `V-259730`

### Rule: Access to IBM Security zSecure user data sets must be properly restricted and logged.

**Rule ID:** `SV-259730r1050750_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If zSecure were to allow inappropriate reading or updating of user data sets, sensitive information could be disclosed, or changes might result in incorrect results reported by the product. Only qualified and authorized individuals must be allowed to create, read, update, and delete zSecure user data sets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the accesses to the zSecure user data sets are properly restricted. If the following guidance is true, this is not a finding. - The RACF profiles protecting zSecure user data sets do not allow general access by means of UACC, ID(*), WARNING, or global access. - READ access to ASSERTION, CKFREEZE, and UNLOAD data sets is restricted to auditors, automated operation STCs/batch jobs, decentralized security administrators, security administrators, batch jobs performing ESM maintenance, system programmers and trusted STC users. - UPDATE and higher access to ASSERTION, CKFREEZE, and UNLOAD data sets is restricted to decentralized security administrators, security administrators, batch jobs performing ESM maintenance, and system programmers. - All failures and successful UPDATE and higher access to ASSERTION, CKFREEZE, and UNLOAD data sets is logged. - READ access to Access Monitor output data sets is restricted to auditors, decentralized security administrators, security administrators, batch jobs performing ESM maintenance, automated operation STCs/batch jobs, and trusted STC users, and system programmers. - UPDATE and higher access to the Access Monitor output data sets is restricted to automated operation STCs/batch jobs, batch jobs performing ESM maintenance, trusted STC users, and system programmers. - All failed and all successful UPDATE and higher access to Access Monitor output data sets is logged. - READ access to CKACUST and CKACUSV data sets is restricted to auditors, batch jobs that perform ESM maintenance, decentralized security administrators, security administrators, automated operation STCs/batch jobs, trusted STC users, and systems programmers. - UPDATE access to CKACUST and CKACUSV data sets is restricted to decentralized security administrators, security administrators, automated operation STCs/batch jobs, batch jobs performing ESM maintenance, trusted STC users, and systems programmers. - CONTROL and higher access to CKACUST and CKACUSV data sets is restricted to systems programmers. - All failed and all successful UPDATE and higher access to CKACUST and CKACUSV data sets is logged. - READ access to CKXLOG log stream is restricted to auditors, decentralized security administrators, security administrators, automated operation STCs/batch jobs, trusted STC users, and system programmers. - UPDATE and higher access to CKXLOG log stream is restricted to automated operation STCs/batch jobs, trusted STC users, and system programmers. - All failed access to CKXLOG log stream is logged.

## Group: SRG-APP-000148-MFP-000206

**Group ID:** `V-259731`

### Rule: Started tasks for IBM Security zSecure products must be properly defined.

**Rule ID:** `SV-259731r1051324_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Started tasks and batch job IDs can be automatically revoked accidentally if not properly protected. When properly protected STCs prevent any attempts to log on with a password, it eliminates the possibility of revocation due to excessive invalid password attempts (denial of service).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If user IDs assigned to zSecure started tasks and scheduled batch jobs are not assigned the PROTECTED attribute and/or defined as an STC, this is a finding. The default zSecure STC names (that may be changed by installation) are as follows: - STC C2PACMON runs program C2PACMON. - STC C2POLICE runs program C2POLICE. - STC C2PCOLL runs program CKFCOLL. (CKFCOLL is also run as a step in batch jobs.) - STC C2RSERVE runs program BPXBATCH. - STC CKCS1154 runs program CKCS1154. - STC CKNSERVE runs program CKNSERVE. - STC CKCCEF runs program CKRCARLX. - STC CKQCLEEF runs program CKRCARLX. - STC CKQEXSMF runs program CKQEXSMF. - STC CKQRADAR runs program CKRCARLA. - STC CKXLOG runs program CKXLOG. Verify the naming conventions for the zSecure STCs and batch jobs with the responsible systems programmers. Check which user IDs are assigned in the STDATA segment of the zSecure STCs. For these user IDs, verify they are assigned the PROTECTED attribute.

## Group: SRG-APP-000211-MFP-000283

**Group ID:** `V-259732`

### Rule: Access to IBM Security zSecure program resources must be limited to authorized users.

**Rule ID:** `SV-259732r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Functional access (which is controlled with access to XFACILIT profiles) must not commingle multiple functions under a single resource profile.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the profiles protecting zSecure program resources do not allow general access by means of UACC, ID(*),WARNING, or global access, this is not a finding. Review profile(s) protecting CKF.** resources in XFACILIT class. If READ and higher access to any other CKF.<focus> profiles is not restricted to security administrators, decentralized security administrators, security batch jobs performing External Security Manager (ESM) maintenance, and trusted STC users, this is a finding. Review profile(s) protecting CKN*.** resources in XFACILIT class. If READ and higher access to any other CKNADMIN.**, and CKNDSN.**, profiles is not restricted to security administrators, decentralized security administrators, security batch jobs performing ESM maintenance, and trusted STC users, this is a finding. Review profile(s) protecting CKG.** resources in XFACILIT class. If READ and higher access to any other CKG.CMD.**, CKG.RAC.**, CKG.SCHEDULE.**, CKG.SCP.**, CKG.SCPASK.**,CKG.UCAT.**, or CKG.USRDATA.** profiles is not restricted to security administrators, decentralized security administrators, security batch jobs performing ESM maintenance, and trusted STC users, this is a finding. Review profile(s) protecting CKR.** resources in XFACILIT class. If READ and higher access to any other CKR.ACTION.**, CKR.CKRCARLA.APF, CKR.CKXLOG.**, CKR.OPTION.**, or CKR.READALL profiles is not restricted to security administrators, decentralized security administrators, security batch jobs performing ESM maintenance, and trusted STC users, this is a finding. If zSecure is used, review profile(s) protecting C2R.** resources in XFACILIT class. If READ and higher access to any other C2R.CLIENT.** or C2R.SERVER.ADMIN profiles is not restricted to security administrators, decentralized security administrators, security batch jobs performing ESM maintenance, and trusted STC users, this is a finding. Review profile(s) protecting C2X.** resources in XFACILIT class. If UPDATE access to any other C2X.ICH* profile is not restricted to automated operation STCs/batch jobs or trusted STC users, this is a finding. If all failures and successful UPDATE and higher access attempts are logged, this is not a finding.

## Group: SRG-APP-000340-MFP-000088

**Group ID:** `V-259733`

### Rule: IBM Security zSecure must prevent nonprivileged users from executing privileged zSecure functions.

**Rule ID:** `SV-259733r1050755_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged zSecure functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, running COLLECT jobs, generating audit reports, and adjusting RACF security settings. Nonprivileged users are individuals who do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from nonprivileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If READ access to zSecure functional resources is not restricted to privileged users, this is a finding. If the following high-level qualifier profiles are defined in the configured zSecure class, by default XFACILIT, with UACC (NONE) and not in WARNING mode, this is not a finding. CKF.** CKN*.** CKG.** CKR.** C2R.** (if you use zSecure Visual) C2X.** If a minimum of all failed access is logged, this is not a finding.

## Group: SRG-APP-000342-MFP-000090

**Group ID:** `V-259734`

### Rule: The IBM Security zSecure programs CKFCOLL and CKGRACF, and the APF-authorized version of program CKRCARLA, must be restricted to security administrators, security batch jobs performing External Security Manager (ESM) maintenance, auditors, and systems programmers, and must be audited.

**Rule ID:** `SV-259734r1050758_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users authorized to use the zSecure program CKFCOLL can collect z/OS system information that is not accessible to regular users. Users authorized to use the zSecure program CKGRACF can change certain permitted RACF profile definitions that otherwise would not be allowed. Users authorized to use the zSecure program CKRCARLX can fake SMF records. Allowing inappropriate users to use the CKFCOLL, CKGRACF, and CKRCARLX programs could result in disclosure of z/OS installation and configuration information or inappropriate RACF profile or SMF record changes. Satisfies: SRG-APP-000342-MFP-000090,SRG-APP-000343-MFP-000091</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is not a RACF system, the presence of CKGRACF is not applicable. Verify the access and log settings of the profiles that protect the use of the CKFCOLL and CKGRACF programs and the APF-authorized version of the CKRCARLA program. If the CKF.** and CKG.** profiles that protect the use of the CKFCOLL, CKGRACF, and CKRCARLA programs allow general access (UACC, ID(*), WARNING, or global access) or do not log successful READ access, this is a finding. If READ or higher access to profile(s) protecting CKF.** resources in XFACILIT class is not restricted to security administrators (domain or decentralized), batch jobs performing ESM maintenance, auditors, or systems programmers, this is a finding. If READ or higher access to profile(s) protecting CKG.** resources in XFACILIT class is not restricted to security administrators (domain or decentralized) or batch jobs performing ESM maintenance, this is a finding. Review auditing of the profile protecting the CKR.CKRCARLA.APF resource in XFACILIT class. If successful READs are not audited, this is a finding.

## Group: SRG-APP-000379-MFP-000186

**Group ID:** `V-259735`

### Rule: IBM Security zSecure must implement organization-defined automated security responses if baseline zSecure configurations are changed in an unauthorized manner.

**Rule ID:** `SV-259735r961458_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the zSecure baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the system. Changes to information system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the application. Examples of security responses include but are not limited to the following: halting application processing, halting selected application functions, or issuing alerts/notifications to organizational personnel when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a (daily) scheduled batch job is defined and used or a custom alert is configured and activated to inform appropriate personnel, such as auditors and compliance officers, about successful changes to the zSecure configuration data sets on their z/OS systems. If SMF records regarding successful UPDATE(s) to zSecure configuration data sets are not reported to the information system security manager (ISSM), this is a finding.

## Group: SRG-APP-000454-MFP-000343

**Group ID:** `V-259736`

### Rule: IBM Security zSecure must remove all upgraded/replaced zSecure software components that are no longer required for operation after updated versions have been installed.

**Rule ID:** `SV-259736r961677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of zSecure products and components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the inventory of installed software components for zSecure. If software components that are no longer required for operation exist, this is a finding.

## Group: SRG-APP-000456-MFP-000345

**Group ID:** `V-259737`

### Rule: IBM Security zSecure system administrators must install security-relevant zSecure software updates within the time period directed by an authoritative source (e.g., IAVMs, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-259737r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the system administrator for the procedure to install security-relevant software updates within the time period directed by an authoritative source (e.g., IAVMs, CTOs, DTMs, and STIGs. If there is no procedure, this a finding.

## Group: SRG-APP-000516-MFP-000195

**Group ID:** `V-259738`

### Rule: XFACILIT class, or alternate class if specified in module CKRSITE, must be active.

**Rule ID:** `SV-259738r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The zSecure resource class that is configured for the zSecure access checks must be active to receive valid Allow/Deny responses from external security manager (ESM) resource checks. Activation is outside of zSecure, in the ESM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the CARLa command SHOW CKRSITE. The output of this command reveals which resource class is configured for handling the zSecure security checks. The default resource class is XFACILIT. Verify in the class descriptor table that the configured zSecure resource class is active. If the configured zSecure resource class is not active, this is a finding.

