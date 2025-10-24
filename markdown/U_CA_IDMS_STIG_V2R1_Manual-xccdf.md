# STIG Benchmark: CA IDMS Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-251582`

### Rule: For interactive sessions, IDMS must limit the number of concurrent sessions for the same user to one or allow unlimited sessions.

**Rule ID:** `SV-251582r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multiple interactive sessions can provide a way to cause a DoS attack against IDMS if a user ID and password were compromised. Not allowing multiple sign-ons can mitigate the risk of malicious attacks using multiple sessions for a user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use task SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "MULTIPLE SIGNON" is found. If the associated value is "YES", this is a finding.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-251583`

### Rule: IDMS must support the implementation of an external security manager (ESM) to handle account management and user accesses, etc.

**Rule ID:** `SV-251583r960768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internal security in a DBMS can be complex to implement and maintain with the increased possibility of no access or the wrong access to a needed resource. IDMS can be configured to use an ESM as the security repository allowing access rules to be added to already-known users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When securing IDMS user IDs with an ESM, some preparation must be done in IDMS itself. Identify CA IDMS security domains (a set of DC systems and local mode applications sharing a single user catalog and SRTT). For a given security domain, logon to one DC system. Issue DCPROFIL. If there is nothing specified for "Security System" and therefore no external security system being used, this is a finding. Examine load module RHDCSRTT by executing CA IDMS utility "IDMSSRTD", or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If no TYPE=ENTRY with RESTYPE=SGON is found, this is a finding. If RESTYPE=SGON is secured internally, this is a finding. Interrogate the security office and verify the ESM has the appropriate entries to secure the RESTYPE of SGON. If not, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251584`

### Rule: IDMS must allow only authorized users to sign on to an IDMS CV.

**Rule ID:** `SV-251584r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unauthorized users signing on to IDMS can pose varying amounts of risk depending upon the security of the IDMS resources in an IDMS CV. Until the IDMS sign-on resource type (SGON) is secured anyone can sign on to IDMS. This risk can be mitigated by securing the SGON resource.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note that this requires PTFs SO07995 and SO09476. Look for a #SECRTT statement with the string "RESTYPE=SGON" and SECBY=EXTERNAL. If no "RESTYPE=SGON" is found or "SECBY=OFF" or "SECBY=INTERNAL" is specified, this is a finding. Execute an external security manager (ESM) resource access list for resource "SGON" for each CV on the system. If the resource access is not restricted to only users authorized in the site security plan, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251585`

### Rule: IDMS must enforce applicable access control policies, even after a user successfully signs on to CV.

**Rule ID:** `SV-251585r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unless the DBMS is secured properly, there are innumerable ways that a system and its data can be compromised. The IDMS SRTT is the basis for mitigating these problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. In the SRTT, resources are protected by #SECRTT TYPE=ENTRY and TYPE=OCCURRENCE statements. Examine the SRTT to ensure that there are #SECRTT statements for the desired recourses that have "SECBY=EXTERNAL". If there are none, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251586`

### Rule: All installation-delivered IDMS USER-level tasks must be properly secured.

**Rule ID:** `SV-251586r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User-level tasks that are not secured may allow anyone who signs on to IDMS to use them to access and manipulate various resources within the DBMS. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000211-DB-000122</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module "RHDCSRTT" by executing CA IDMS utility "IDMSSRTD", or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Validate the following suggested user-level tasks are secured in the SRTT (included, for example, in the roles of DCADMIN-, DBADMIN-, and DEVELOPER-level security). Note: USER, DEVELOPER, DBADMIN, and DCADMIN are suggested categories only. ADS OCF OCFT OCFX OLP OLQ OLQNT OLQT OLQTNOTE If "TASK" is not found as the resource type in any of the entries, this is a finding. If "TASK" is secured internally, this is a finding. If "TASK" is secured externally in the SRTT, review the SRTT entries to ensure that the above tasks are secured and review ESM for external class and external name format to verify the appropriate authorizations have been defined. If they have not, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251587`

### Rule: All installation-delivered IDMS DEVELOPER-level tasks must be properly secured.

**Rule ID:** `SV-251587r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developer-level tasks that are not secured may allow anyone who signs on to IDMS to use them to access and manipulate various resources within the DBMS. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000211-DB-000122</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Validate the following suggested developer-level tasks are secured in the SRTT (included, for example, in the roles of DCADMIN, DBADMIN level security). Note: USER, DEVELOPER, DBADMIN, and DCADMIN are suggested categories only. ADSA ADSAT ADSC ADSCT ADSK ADSL DEBUG IDDML IDDM IDDT LOOK MAPB MAPBT MAPC MAPCT PMAM PMIM QUED SCHEMA SCHEMAT SHOWMAP If "TASK" is not found as the resource type in any of the entries, this is a finding. If "TASK" is secured internally, this is a finding. If "TASK" is secured externally in the SRTT, review the SRTT entries to ensure that the above tasks are secured and review ESM for external class and external name format to make sure the appropriate authorizations have been defined. If they have not, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251588`

### Rule: All installation-delivered IDMS DBADMIN-level tasks must be properly secured.

**Rule ID:** `SV-251588r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBA-level tasks that are not secured may allow anyone who signs on to IDMS to use them to access and manipulate various resources within the DBMS. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000211-DB-000122</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing the command "DCMT DISPLAY SRTT" while signed on to the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Validate the following suggested DBA-level tasks are secured in the SRTT (included, for example, in the role of DCADMIN-level security): Note: USER, DEVELOPER, DBADMIN, and DCADMIN are suggested categories only. ADSM ADSOTATU IDD IDDM SSC SSCT If "TASK" is not found as the resource type in any of the entries, this is a finding. If "TASK" is secured internally this is a finding. If "TASK" is secured externally in the SRTT, review the SRTT entries to ensure that the above tasks are secured and review external security manager (ESM) for external class and external name format to make sure the appropriate authorizations have been defined. If they have not, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251589`

### Rule: All installation-delivered IDMS DCADMIN-level tasks must be properly secured.

**Rule ID:** `SV-251589r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If DC Administrator-level tasks are not secured, any user logged on to IDMS may use them to access and manipulate various resources within the DBMS. This can be mitigated using the proper entries in the SRTT. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000211-DB-000122</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Validate the following suggested DC-Administrator-level tasks are secured in the SRTT. If they are not secured, this is a finding. (Note that USER, DEVELOPER, DBADMIN, and DCADMIN are suggested categories only). ASF CLOD DCMT OPER PMBILL PMRM SDEL SEND SYSGEN SYSGENT WEBC If "TASK" is not found as the resource type in any of the entries, this is a finding. IF "TASK" is secured internally, this is a finding. If "TASK" is secured externally in the SRTT, review the SRTT entries to ensure that the above tasks are secured, and review the external security manager (ESM) for external class and external name format to make sure the appropriate authorizations have been defined. If they have not, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251590`

### Rule: All installation-delivered IDMS User-level programs must be properly secured.

**Rule ID:** `SV-251590r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If user-level programs are not secured, then unauthorized users may use them to access and manipulate various resources within the DBMS. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000211-DB-000122</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following are user-level batch programs that are executed using JCL rather than by the CV. As batch programs, they need to be secured by the external security manager (ESM) rather than through the SRTT. Validate the following suggested user-level programs are secured by the ESM: ADSBATCH ADSOBPLG CULPRIT IDMSBCF OLQBATCH OLQBNOTE Contact the security office to confirm that the programs in this list are secured. If the programs listed are not secured, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251591`

### Rule: All installation-delivered IDMS Developer-level Programs must be properly secured.

**Rule ID:** `SV-251591r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developer-level programs that are not secured may allow unauthorized users to access and manipulate various resources within the DBMS. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000211-DB-000122</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following are developer-level batch programs and are executed using JCL rather than the CV. As batch programs, they need to be secured in the external security manager (ESM) rather than through the SRTT. Validate the following suggested developer-level programs are secured by the ESM. ADSOBCOM ADSORPTS IDMSDMLA IDMSDMLC IDMSDMLP IDMSLOOK IDMSRPTS RHDCMAP1 RHDCMPUT Contact the security office to confirm that the programs in this list are secured. If they are not, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251592`

### Rule: All installation-delivered IDMS Database-Administrator-level programs must be properly secured.

**Rule ID:** `SV-251592r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBA-level programs that are not secured may allow unauthorized users to use them to access and manipulate various resources within the DBMS. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000211-DB-000122</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following are DBA-level batch programs and are executed using JCL rather than the CV. As batch programs, they need to be secured for DBAs in the external security manager (ESM) (included in DCADMIN, DBADMIN level security) rather than through the SRTT. Validate the following suggested DBA-level programs are secured by the ESM. ADSOBSYS ADSOBTAT IDMSCHEM IDMSDBN1 IDMSDBN2 IDMSDDDL IDMSPASS IDMSRSTC IDMSUBSC RHDCOMVS Contact the security office to confirm that the programs in this list are secured. If not, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251593`

### Rule: All installation-delivered IDMS DC-Administrator-level programs must be properly secured.

**Rule ID:** `SV-251593r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DC Administrator-level programs that are not secured may allow unauthorized users to use them to access and manipulate various resources within the DBMS. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000211-DB-000122</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following are DC-administrator level batch programs and are executed using JCL rather than the CV. As batch programs, they need to be secured in the external security manager (ESM) rather than through the SRTT. Validate the following suggested DBA-level programs are secured by the ESM: IDMSDIRL RHDCSGEN RHDCTTBL If the suggested DC-Administrator-level programs are not secured in the SRTT and have not been authorized for DCADMINs in the ESM, this is a finding. (Note that USER, DEVELOPER, DBADMIN and DCADMIN are suggested categories only). Contact the security office if the programs in this list are not secured, for this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-251594`

### Rule: IDMS must protect against the use of default userids.

**Rule ID:** `SV-251594r960864_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Default sign-ons can be used by individuals to perform adverse actions anonymously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module "RHDCSRTT" by executing CA IDMS utility "IDMSSRTD", or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If the TYPE=INITIAL #SECRTT has DFLTSGN=YES specified, this is a finding. If DFLTUID is defined, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-251595`

### Rule: IDMS must protect against the use of external request exits that change the userid to a shared id when actions are performed that may be audited.

**Rule ID:** `SV-251595r960864_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables and configuring the DBMS's audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to the DBMS, even where the application connects to the DBMS with a standard, shared account. User exits that change userids can be used to hide the true identities of those who may perform an action and should be carefully restricted or eliminated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the CV and enter command DCPROFIL. Press "Enter" until the page titled "Named User Exits" appears. Find the entry for USRIDXIT. If the DEFINED column says YES, then a user-written exit has been linked with IDMSUXIT. If a user-written exit USRIDXIT has been linked with IDMSUXIT (for batch or TSO-front end use), UCFCICS (UCF access from a CICS transaction) or IDMSINTC (DML or SQL access form a CICS transaction server front-end) and the USRIDXIT changes the userid to a shared userid, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-251596`

### Rule: IDMS must protect against the use of numbered exits that change the userid to a shared id.

**Rule ID:** `SV-251596r960864_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables and configuring the DBMS's audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to the DBMS, even where the application connects to the DBMS with a standard, shared account. User exits that change userids can be used to hide the true identities of those who may perform an action and should be carefully restricted or eliminated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Issue LOOK PROGRAM=RHDCUXIT. If there are non-zeros in the 12 bytes starting at X'200', exit 27 is being used. If there are non-zeros in the 12 bytes starting at X'20C', exit 28 is being used. Check exits for a change in userid and if there is a change to a shared user ID, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-251597`

### Rule: IDMS must protect against the use of web-based applications that use generic IDs.

**Rule ID:** `SV-251597r960864_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Web-based applications that allow a generic ID can be a door into IDMS allowing unauthorized changes whose authors may not be determined.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are web-based applications to which individual users sign on, and a generic ID associated with the application is used to access back-end IDMS databases, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-251598`

### Rule: IDMS must protect against the use web services that do not require a sign on when actions are performed that may be audited.

**Rule ID:** `SV-251598r960864_rule`
**Severity:** low

**Description:**
<VulnDiscussion>IDMS web services provide a way for web-based applications to access an IDMS database. If not secured, the Web services interface could be used to reveal or change sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the IDMS CV system where CA IDMS Web Services executes, enter "WEBC" to check Web Services configuration. If "REQUIRE SIGNON = NO", this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-251599`

### Rule: IDMS must use the ESM to generate auditable records for resources when DoD-defined auditable events occur.

**Rule ID:** `SV-251599r960879_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Audit records provide a tool to help research events within IDMS. IDMS does not produce audit records, but when using external security, records can be produced through the ESM. IDMS relies on the ESM to log organization-defined auditable events. To ensure that all secure actions are logged, those actions must be defined to the IDMS Security Resource Type Table (SRTT) with a type of external security. When IDMS has to perform a given security check, it will defer to the ESM to determine the user's authorization. The auditing functionality of the ESM can be used to track the IDMS security calls. Some organization-defined auditable events are expected to be handled solely by the ESM. This would include requirements such as "successful and unsuccessful attempts to modify or delete privileges, security objects, security levels, or categories of information" as well as "account creation, modification, disablement, or termination." For the audit logging of other organization-defined auditable events, IDMS requires RHDCSRTT security module set up to route requests for these events through the ESM. This will ensure that they are audited appropriately. The following resource types must be defined with SECBY type of EXTERNAL in the RHDCSRTT load module to achieve the appropriate level of audit logging. If there is not a resource type definition with a security type of EXTERNAL for the following resources, this is a finding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If the ESM specification does not match the RHDCSRTT entry, this is a finding. Validate each of the following listed entries: Access Actions such as login - Resource type SGON Privileged system access - Resource types SYST, DB, DMCL, DBTB Privileged object access - Resource types SLOD, SACC, QUEU Privileged program access - Resource type TASK, SPGM If any are not secured externally, this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-251600`

### Rule: IDMS must use the ESM to generate auditable records for commands and utilities when DoD-defined auditable events occur.

**Rule ID:** `SV-251600r960879_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Audit records provide a tool to help research events within IDMS. IDMS itself does not produce audit records but, when external security is in place, records can be produced through the ESM. IDMS relies on the ESM to log organization-defined auditable events. To ensure that all secure actions are logged, those actions must be defined to the IDMS Security Resource Type Table (SRTT) with a type of external security. When IDMS has to perform a given security check, it will defer to the ESM to determine the user's authorization. The auditing functionality of the ESM can be used to track the IDMS security calls. Some organization-defined auditable events are expected to be handled solely by the ESM. This would include requirements such as "successful and unsuccessful attempts to modify or delete privileges, security objects, security levels, or categories of information" as well as "account creation, modification, disablement, or termination." For the audit logging of other organization-defined auditable events, IDMS requires RHDCSRTT security module set up to route requests for these events through the ESM. This will ensure that they are audited appropriately. The following resource types must be defined with SECBY type of EXTERNAL in the RHDCSRTT load module to achieve the appropriate level of audit logging. If there is not a resource type definition with a security type of EXTERNAL for the following resources, this is a finding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module IDMSCTAB by executing CA IDMS utility IDMSCTAD, or by issuing command "DCMT DISPLAY CTAB" while signed onto the CV and reviewing the output. Note: This requires PTF SO08199. If there is execution of certain OCF/BCF commands that have not defined in the IDMSCTAB module using the #CTABGEN macro, this is a finding. If these task codes are defined to the IDMSCTAB module but have not been defined for the related activities to the RHDCSRTT module, this is a finding. If the execution of DCMT utility command codes is not defined in the IDMSUTAB module using the #UTABGEN macro, this is a finding. Examine load module IDMSUTAB using CA IDMS utility IDMSUTAD, or by issuing command 'DCMT DISPLAY UTAB' while signed onto the CV, and reviewing the output. Note: This requires PTF SO08527. If IDMSUTAB load module defined commands but has not defined the related activities to the RHDCSRTT module, this is a finding. If any of the above tasks are completed from local mode, utilize a custom EXIT 14 to trigger a security check that will go through the ESM. If an EXIT 14 is not configured for each situation, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-251601`

### Rule: Database objects in an IDMS environment must be secured to prevent privileged actions from being performed by unauthorized users.

**Rule ID:** `SV-251601r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If database objects like areas, schemas, and run units are not secured, they may be changed or deleted by unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Examine the SRTT and verify that entries exist for all desired database resources. The database resources that may be secured are and their respective RESTYPEs are: Database - DB Area - AREA (1) Rununit - NRU (1) SQL Schema - QSCH (1) Non-SQL Schema - NSCH (1) Access Module - DACC (1) Table - TABL (1) DMCL - DMCL Database name table - DBTB Note: Securing RESTYPE=DB (Database) also secures for these resource types. SRTT TYPE=ENTRY statements with RESTYPEs of AREA, NRU, QSRCH, NSCH, DACC, and TABL do not turn security on or off for these RESTYPEs, but are used to build the EXTNAME and EXTCLAS to be passed to the external security manager (ESM). Interrogate the DBA(s) to determine which database objects may need secured. For SQL access, check that both the catalog and user database are secured in the SRTT. If not, this is a finding. If batch jobs are allowed to be run with access an IDMS database, check whether the access is covered by standard ESM dataset security and/or the user-written exit 14 (issues a security check when a BIND RUN-UNIT or READY AREA is being done). If not, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-251602`

### Rule: The programs that can be run through a CA IDMS CV must be defined to the CV to prevent installation of unauthorized programs; must have the ability to dynamically register new programs; and must have the ability to secure tasks.

**Rule ID:** `SV-251602r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IDMS SYSGEN must be protected against unauthorized changes. Satisfies: SRG-APP-000133-DB-000362, SRG-APP-000378-DB-000365</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SRTT for the externally secured resource SYST which allows the SYSGEN to be modified and application program definitions to be added. Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If "SYST" is not found as the resource type in any of the entries, this is a finding. IF "SYST' is not coded with SECBY=EXTERNAL, this is a finding. If "SYST" is found to be secured externally, ensure the external security manager (ESM) contains the correct definition using the external resource class name and the external name construction rules. If it is not defined or not defined correctly, this is a finding. If the ESM definition is correct but the role(s)/groups(s) are not defined correctly to give the appropriate permissions, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-251603`

### Rule: The commands that allow dynamic definitions of PROGRAM/TASK and the dynamic varying of memory must be secured.

**Rule ID:** `SV-251603r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IDMS provides commands that can change memory, the attributes of programs, or tasks and are meant for use by the appropriate administrators. These commands must be protected from use by the wrong personnel. Satisfies: SRG-APP-000133-DB-000362, SRG-APP-000380-DB-000360, SRG-APP-000378-DB-000365</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SRTT for externally secured ACTI resource which can be used to secure DCMT VARY DYNAMIC PROGRAM, DCMT VARY DYNAMIC TASK and DCMT VARY MEMORY. Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If "ACTI" is not found as the resource type in any of the entries, this is a finding. IF "ACTI" is found but has SECBY=INTERNAL, this is a finding. If no entry is securing VARY DYNAMIC and VARY MEMORY externally, this is a finding. If there is no IDMSCTAB load module into which the #CTABGEN has been generated that specifies the nodes names that correspond to the DCMT commands (DCMT VARY DYNAMIC - N046; DCMT VARY MEMORY - N033), this is a finding. Examine load module IDMSCTAB using CA IDMS utility IDMSCTAD, or by issuing command "DCMT DISPLAY CTAB" while signed onto the CV, and reviewing the output. Note that this requires PTF SO08199. If DCMT command codes N024, N025, and N033 are not defined, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-251604`

### Rule: Databases must be secured to protect from structural changes.

**Rule ID:** `SV-251604r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database objects, like areas and run units, can be changed or deleted if not protected. Steps must be taken to secure these objects via the external security manager (ESM). Satisfies: SRG-APP-000133-DB-000362, SRG-APP-000380-DB-000360</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All database objects to be secured must be specified to the CA IDMS centralized security in the security resource type table (SRTT) as being secured externally. Log on to a DC system in the security domain. Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Check each entry in the SRTT. If the resource type is DB, AREA, NRU, QSCH, NSCH, TABL, DACC, SACC, DMCL, or DBTB, the resource type is a database object. If it contains SECBY=INTERNAL, this is a finding. If any of the database types are not found in the SRTT, this is a finding. For SQL access, check that both the catalog and user database are secured in the SRTT. If not, this is a finding. If batch jobs are allowed to be run which access an IDMS database, check whether the access is covered by standard ESM dataset security and/or the user-written exit 14 (issues a security check at BIND/READY time). If not, this is a finding. If the ESM definition is correct but the role(s)/groups(s) are not defined correctly to give the appropriate permissions, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-251605`

### Rule: Database utilities must be secured in CA IDMS and permissions given to appropriate role(s)/groups(s) in the external security manager (ESM).

**Rule ID:** `SV-251605r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IDMS has tasks that are used to perform necessary maintenance, but in the wrong hands could damage the integrity of the DBMS. Tasks that can change database structure must be protected. Satisfies: SRG-APP-000133-DB-000362, SRG-APP-000380-DB-000360</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SRTT for externally secured ACTI which can be used to secure utility functions that can impact database structure, e.g., CONVERTCATALOG, CONVERTPAGE, EXPANDPAGE, MAINTAININDEX, REORG, RESTRUCTURE and TUNEINDEX. For a full list, see the UTABGEN UTILITY COMMAND CODES table in the Administrating Security for IDMS manual. Examine load module IDMSUTAB using CA IDMS utility IDMSUTAD, or by issuing command "DCMT DISPLAY UTAB" while signed onto the CV, and reviewing the output. Note: This requires PTF SO08527. If there is no IDMSUTAB load module into which the #UTABGEN has been generated that specifies the nodes names that correspond to the UTILITY statements, this is a finding. Examine load module RHDCSRTT by executing CA IDMS utility "IDMSSRTD", or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. If "ACTI" is not found as the resource type in any of the entries, this is a finding. IF "ACTI" is found to be secured internally, this is a finding. If "ACTI" is found to be secured externally, ensure that the ESM contains the correct definition using the external resource class name and the external name construction rules. If it is not defined or not defined correctly, this is a finding. If the ESM definition is correct but the role(s)/groups(s) are not defined correctly to give the appropriate permissions, this is a finding. Note: There are alternative ways to secure utilities by using RESTYPE=DB and corresponding ESM definitions can give authorization to appropriate role(s)/group(s).

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-251606`

### Rule: The online debugger which can change programs and storage in the CA IDMS address space must be secured.

**Rule ID:** `SV-251606r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations. Users of the online debugger may alter programs and storage in the IDMS CV. Satisfies: SRG-APP-000133-DB-000362, SRG-APP-000380-DB-000360</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the load module RHDCSRTT by executing CA IDMS utility "IDMSSRTD", or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Check the SRTT for externally secured ACTI where the task name is DBUG. If none is found, this is a finding. If the entry is secured internally, this is a finding. If an ACTI statement for DBUG that secures DBUG externally is found, verify the program IDMSGTAB resides in the CV's CMDSLIB concatenation. If not, this is a finding. If IDMSGTAB is found, perform a DUMPT of IDMSGTAB using AMASPZAP. The last 28 bytes are a table of 14 halfwords, one for each security category that can be secured by the #GTABGEN macro. Examine this table in the DUMPT. If all halfwords are zero, and no debugger functions are secure, and this is a finding. If any halfword is non-zero, then the first byte will be x'01' and the second byte will contain the activity number assigned to that function in hexadecimal. The order of the security-categories in the table is: UPGMR UPGMU USTGR USTGU SHSTGR SHSTGU AUPGMR AUPGMU ASYSTGR ASYSTGU ASYSPGR ASYSPGU ALLR ALLU If the debug activity is found to be secured externally, confer with the security office to ensure that the external security manager (ESM) contains the correct definition using the external resource class name the external name construction rules. If it is not defined correctly, this is a finding. If the ESM definition is correct but the role(s)/groups(s) are not defined correctly to give the appropriate permissions, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-251607`

### Rule: CA IDMS must secure the ability to create, alter, drop, grant, and revoke user and/or system profiles to users or groups.

**Rule ID:** `SV-251607r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Even when using an external security manager (ESM), IDMS system and user profiles which reside in an IDMS user catalog may be assigned to users or groups. The ability to administer user and system profiles must be secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Check the SRTT for externally secured RESTYPE=SYSA. If none is found, this is a finding. If the entry is secured internally, this is a finding.

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-251608`

### Rule: The EMPDEMO databases, database objects, and applications must be removed.

**Rule ID:** `SV-251608r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions, and are not developed to prevent vulnerabilities from being introduced to the DBMS and host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a CAISAG base installation completed with EMPDEMO=YES and/or SQLDEMO=YES, or if a base installation completed with CSM and CREATE_DB_DEMO and/or CREATE_SQL_DEMO selected, this is a finding. In OCF/BCF, DISPLAY DMCL <dmclname>. If segments EMPDEMO, SQLDEMO, and/or PROJDEMO exist, this is a finding. In OCF/BCF, DISPLAY DBTABLE <dbtbname>. If segments EMPDEMO, SQLDEMO, and/or PROJDEMO exist, this is a finding. In OCF/BCF, DISPLAY SCHEMA DEMOEMPL and DISPLAY SCHEMA DEMOPROJ. If either or both exist, this is a finding. If schema EMPSCHM exists, this is a finding. If any of the following load modules are in load libs used by the installation, this is a finding: EMPSS01, EMPDMCL, EMPLOAD, EMPRPT, EMPINQ If any of the following files are found to be used by the installation, this is a finding: <installation prefix>.EMPDEMO.EMPDEMO. <installation prefix>.EMPDEMO.INSDEMO, <installation prefix>.ORGDEMO.EMPDEMO, <installation prefix>.SQLDEMO.EMPLDEMO, <installation prefix>.SQLDEMO.INDXDEMO, <installation prefix>.SQLDEMO.INFODEMO, <installation prefix>.PROJSEG.PROJDEMO

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-251609`

### Rule: Default demonstration and sample databases, database objects, and applications must be removed.

**Rule ID:** `SV-251609r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a CAISAG base installation done with EMPDEMO=YES and/or SQLDEMO=YES, or if a base installation done with CSM and CREATE_DB_DEMO and/or CREATE_SQL_DEMO selected, this is a finding. In OCF/BCF, DISPLAY DMCL <dmclname>. If segments EMPDEMO, SQLDEMO and/or PROJDEMO exist, this is a finding. In OCF/BCF, DISPLAY DBTABLE <dbtbname>. If segments EMPDEMO, SQLDEMO and/or PROJDEMO exist, this is a finding. In OCF/BCF, DISPLAY SCHEMA DEMOEMPL and DISPLAY SCHEMA DEMOPROJ. If either or both exist, this is a finding. If schema EMPSCHM exists, this is a finding. If any of the following load modules are in load libs used by the installation, this is a finding. EMPSS01, EMPDMCL, EMPLOAD, EMPRPT, EMPINQ If any of the following files are found to be used by the installation, this is a finding. <installation prefix>.EMPDEMO.EMPDEMO. <installation prefix>.EMPDEMO.INSDEMO, <installation prefix>.ORGDEMO.EMPDEMO, <installation prefix>.SQLDEMO.EMPLDEMO, <installation prefix>.SQLDEMO.INDXDEMO, <installation prefix>.SQLDEMO.INFODEMO, <installation prefix>.PROJSEG.PROJDEMO

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-251610`

### Rule: IDMS components that cannot be uninstalled must be disabled.

**Rule ID:** `SV-251610r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>DBMSs must adhere to the principles of least functionality by providing only essential capabilities. At installation, all CA IDMS products are installed but can be disabled (i.e., forced to fail if invoked).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to IDMS DC system and issue DCPROFIL. Scroll to the Product Intent Status screen. If any unused product has a status of "YES", this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-251611`

### Rule: IDMS nodes, lines, and pterms must be protected from unauthorized use.

**Rule ID:** `SV-251611r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system. Unused nodes, lines, and ports must be secured to prevent unauthorized use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each load area, run a CREPORT 43 to check the nodes and access types for each node. For each node, issue DCMT D LINE. For each LINE type with a status of InSrv, inspect the access type for potential unauthorized connection types. For TCP/IP, any line with access type SOCKET, issue DCMT D LINE <tcp-line-id>. If any terminals are of type LIST and status InSrv, check port number for a valid port. If the port number is unacceptable as defined in the PPSM CAL, this is a finding. For each terminal with the type of LIST and InSrv, issue DCMT D PTE <pterm-id>. For each task and (possible PARM STRING which could pass a task) identified in the PTE display, issue DCMT D TASK <task-id>. If the task is IDMSJSRV and the associated program is not RHDCNP3J, this is a finding. If the task/program has not been authorized, this is a finding. If other access types (e.g., VTAM, SVC, CCI) have been deemed nonsecure in the PPSM CAL, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-251612`

### Rule: The IDMS environment must require sign-on for users and restrict them to only authorized functions.

**Rule ID:** `SV-251612r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals using shared accounts, for detailed accountability of individual activity. The SGON resource must be protected to prevent unauthorized users from signing on.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each CA IDMS system, verify the resource module RHDCSRTT for the security domain in which the CA IDMS system exists has an entry for sign-on. Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If no SGON entry exists (sign-on not secured), this is a finding. If found and the entry is not secured externally, this is a finding. Ensure the external security manager (ESM) entry for the externally secured "SGON" resource is correctly configured for the external resource class and the external name of the "SGON" resource. The external name must match the format of the external name construction tokens found in the SRTT entry. If not, this is a finding. For local batch jobs that access database files, if there is no ESM security defined for the users submitting the jobs or securing the database datasets, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-251613`

### Rule: DBMS authentication using passwords must be avoided.

**Rule ID:** `SV-251613r981946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords that are easy to guess open a vulnerability allowing an unauthorized user to potentially gain access to the DBMS. IDMS uses the External Security Manager (ESM) to enforce complexity and lifetime standards.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Find the entry for RESTYPE=SGON. If no SGON entry exists, this is a finding. If found, verify that the entry has SECBY=EXTERNAL. If it does not, this is a finding. Verify that the ESM entry for the externally secured "SGON" resource is correctly configured for the external resource class and the external name of the "SGON" SRTT entry. For local batch jobs that access database files, if there is no ESM security defined for the users submitting the jobs or securing the database datasets, this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-251614`

### Rule: Passwords sent through ODBC/JDBC must be encrypted.

**Rule ID:** `SV-251614r961029_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Unencrypted passwords transmitted from ODBC and JDBC may be intercepted to prevent their being intercepted in a plain-text format.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using ODBC (with the CCI communications protocol) or a JDBC type 2 driver, if SSL encryption is not being used with CAICCI r2.1 and above, this is a finding. When using ODBC (with the IDMS communications protocol), if SSL encryption is not being used as indicated on the "Server" tab of the Data Source definition, this is a finding. When using a JDBC type 4 driver, if SSL is not being used as indicated by the connection URL, this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-251615`

### Rule: The DBMS must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-251615r961053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the Nation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that sign-on has been secured. Examine load module RHDCSRTT by executing CA IDMS utility "IDMSSRTD", or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Find the entry for sign-on by examining the entries. If no SGON entry exists (sign-on not secured), this is a finding. If found, but the entry is not secured externally, this is a finding. Verify the ESM entry for the externally secured "SGON" resource is correctly configured for the external resource class and the external name of the "SGON" resource in the SRTT. If not, this is a finding. If users, groups, and roles have not been appropriately defined to the external security manager (ESM), this is a finding. Interrogate the security administrator and verify that only authorized users have permission through the ESM to access IDMS. For local batch jobs that access database files, if there is no ESM security defined for the users submitting the jobs or securing the database datasets, this is a finding.

## Group: SRG-APP-000225-DB-000153

**Group ID:** `V-251616`

### Rule: IDMS executing in a local mode batch environment must be able to manually recover or restore database areas affected by failed transactions.

**Rule ID:** `SV-251616r961122_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Local mode update jobs can either use local mode journaling or perform a backup of the database prior to executing the local mode updates. Local mode journaling could be completed if the database is too large to back up in a reasonable amount of time. To use local mode journals for manual recovery, the journals must be defined in the IDMS DMCL as a TAPE JOURNAL and a DD for the journal file must be coded in the update job step JCL. The local mode update job must include the IDMS DMCL name in the SYSIDMS parameter file as DMCL=dmcl-name. If the local mode update step fails, then a rollback step must be performed to recover the database. Without local mode journaling, the local mode batch job should include a backup of the database step, a local mode update step and another backup of the database step if the local updates step successfully complete. If the local mode update step fails, then a step to restore the database from the first backup step must be performed. Satisfies: SRG-APP-000225-DB-000153, SRG-APP-000226-DB-000147</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the job or prior job contains a step to vary the areas offline to the CV and takes a backup. If not there, it is a finding. Perform a second check to verify there is a restore step or JCL that can be used when the job fails.

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-251617`

### Rule: CA IDMS must isolate the security manager to which users, groups, roles are assigned authorities/permissions to resources.

**Rule ID:** `SV-251617r961131_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database Management Systems typically separate security functionality from non-security functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and non-security functionality are commingled, users who have access to non-security functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify CA IDMS security domains (a set of DC systems and local mode applications sharing a single user catalog and SRTT). For a given security domain, log on to one DC system. Issue DCPROFIL. If there is nothing specified for "Security System" and therefore no external security system being used, this is a finding. Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If any entries have SECBY=INTERNAL, this is a finding. For local batch jobs (i.e., those jobs that access database files without going through the CA IDMS system), dataset-level security should be defined in the external security manager (ESM) with authorizations according the site security plan. If it is not, this is a finding. Check those resources that are secured externally to make sure the mapping to the ESM is correct. Check that the ESM entry for the externally secured resource is correctly configured for the external resource class and the external name of the resource being secured. The external name must match the format of the external name construction tokens found in the entry. If the ESM specification does not match the RHDCSRTT entry, this is a finding.

## Group: SRG-APP-000243-DB-000373

**Group ID:** `V-251618`

### Rule: IDMS must prevent unauthorized and unintended information transfer via database buffers.

**Rule ID:** `SV-251618r961149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The purpose of this control is to prevent information, including encrypted representations of information, produced by the actions of a prior user/role (or the actions of a process acting on behalf of a prior user/role) from being available to any current user/role (or current process) that obtains access to a shared system resource (e.g., registers, main memory, secondary storage) after the resource has been released back to the information system. Control of information in shared resources is also referred to as object reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to IDMS DC system and issue "DCPROFIL". If PRIMARY STORAGE PROTECT KEY is the same as the ALTERNATE STORAGE KEY, this is a finding. If SYSTEM STORAGE PROTECTED is "NO", this is a finding. Issue command "DCMT DISP PROG xxxxxxxx" and "DCMT DISP DYN PROG xxxxxxxx" replacing [xxxxxxxx] with the names of user programs and look for Storage Prot. If any are "NO", then this is a finding. Issue command "DCMT DISP BUFFER". If any of the buffers do not have OPSYS in the Getstg column, this is a finding.

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-251619`

### Rule: IDMS must check the validity of all data input unless the organization says otherwise.

**Rule ID:** `SV-251619r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. With respect to database management systems, one class of threat is known as SQL injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. Even when no such hijacking takes place, invalid input that gets recorded in the database, whether accidental or malicious, reduces the reliability and usability of the system. Available protections include data types, referential constraints, uniqueness constraints, range checking, and application-specific logic. Application-specific logic can be implemented within the database in stored procedures and triggers, where appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validate SQL-defined tables, DISPLAY TABLE <schema-name>.<table-name> . If there is not a CHECK for the columns and accompanying accepted values, this is a finding. Validate network-defined records, DISPLAY SCHEMA or DISPLAY RECORD. If there is no CALL to a procedure BEFORE STORE and BEFORE MODIFY, this is a finding. If the procedure does not validate the non-exempt columns, this is a finding. Other applications and front-ends using mapping can use the automatic editing feature and edit and code tables to verify that an input value is valid.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-251620`

### Rule: CA IDMS must permit the use of dynamic code execution only in circumstances determined by the organization and limit use of online and batch command facilities from which dynamic statements can be issued.

**Rule ID:** `SV-251620r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IDMS Common Facilities (BCF and OCF) can execute commands that can make updates to IDMS, and their use should be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SRTT for externally secured resource TASK for command facility task codes (e.g., OCF or organization-defined task codes that invokes program IDMSOCF or IDMSBCF). Examine load module RHDCSRTT by executing CA IDMS utility "IDMSSRTD", or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Review the output looking for those statements that secure RESTYPE=TASK and RESNAMEs OCF or any organization-defined task codes that invoke programs IDMSOCF or IDMSBCF. If none are found for OCF, this is a finding. BCF may not be defined as a task. If it is, this is a finding. The program invoked by installation-defined task codes can be determined by issuing command "DCMT DISP TASK" task-name. Issue command "DCMT DISP TASK" and look for organization-defined tasks, then issue the "DCMT DISP TASK" task-name to determine the program being invoked. Review the code to determine if any of these execute dynamic code. If any do, this is a finding. If command facility tasks are found to be secured externally, ensure the external security manager (ESM) contains the correct definition using the external resource class name and the external resource name construction rules in the #SECRTT. If it is not defined or not defined correctly, this is a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-251621`

### Rule: CA IDMS must limit the use of dynamic statements in applications, procedures, and exits to circumstances determined by the organization.

**Rule ID:** `SV-251621r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Dynamic SQL statements are compiled at runtime and, if manipulated by an unauthorized user, can produce an innumerable array of undesired results. These statements should not be used casually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If EXECUTE IMMEDIATE, PREPARE, and EXECUTE statements are found while reviewing source code in applications, procedures, and exits in code that does not require it, this is a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-251622`

### Rule: CA IDMS must limit  use of IDMS server used in issuing dynamic statements from client applications circumstances determined by the organization.

**Rule ID:** `SV-251622r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Server tasks can execute dynamic SQL code and should be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SRTT for externally secured resource TASK for IDMS Server task codes IDMSJSRV and CASERVER. Examine load module RHDCSRTT by executing CA IDMS utility "IDMSSRTD", or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If no TASK entry is found for either IDJSJSRV or CASERVER, this is a finding. If either is not secured external, this is a finding. If tasks IDMSJSRV and CASERVER are found to be secured externally, ensure that the external security manager (ESM) contains the correct definition using the external resource class name and the external name construction rules. If it is not defined or not defined correctly, this is a finding.

## Group: SRG-APP-000251-DB-000392

**Group ID:** `V-251623`

### Rule: CA IDMS and associated applications, when making use of dynamic code execution, must scan input data for invalid values that may indicate a code injection attack.

**Rule ID:** `SV-251623r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the use of dynamic SQL is necessary, the code should be written so that the invalid data can be found and the appropriate action taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If dynamic code execution is used and identified user input is not validity checked user input, this is a finding. If SQL-defined tables, DISPLAY TABLE <schema-name>.<table-name> . If there is not a CHECK for the columns and accompanying accepted values, this is a finding. If network-defined records, DISPLAY SCHEMA or DISPLAY RECORD. If there is no CALL to a procedure BEFORE STORE and BEFORE MODIFY, this is a finding. If the procedure does not validate the non-exempt columns, this is a finding. Other applications and front-ends using mapping can use the automatic editing feature and edit and code tables to verify that an input value is valid.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-251624`

### Rule: IDMS must suppress security-related messages so that no information is returned that can be exploited.

**Rule ID:** `SV-251624r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Error messages issued to non-privileged users may have contents that should be considered confidential. IDMS should be configured so that these messages are not issued to those users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to IDMS DC system and issue "DCPROFIL". Scroll to the OPTION FLAGS screen. If "OPT00051" is not listed, this is a finding. For IDMS LOG messages, if OPT00226 is not listed, this is a finding.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-251625`

### Rule: Custom database code and associated application code must not contain information beyond what is needed for troubleshooting.

**Rule ID:** `SV-251625r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Error codes issued by custom code could provide more information than needed for problem resolution and should be vetted to make sure this does not occur.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check custom database code to verify that error messages do not contain information beyond what is needed for troubleshooting the issue. If database errors contain PII data, sensitive business data, or information useful for identifying the host system or database structure, this is a finding.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-251626`

### Rule: IDMS must reveal security-related messages only to authorized users.

**Rule ID:** `SV-251626r961170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Error messages issued to non-privileged users may have contents that should be considered confidential. IDMS should be configured so that these messages are not issued to those users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that security messages from external security managers (ESMs) are sent only to the log which can be secured. Log on to IDMS DC system and issue "DCPROFIL". Scroll to the "OPTION FLAGS" screen. If OPT00051 is not listed, this is a finding. For IDMS LOG messages, if OPT00226 is not listed, this is a finding. Contact the security office and verify that the user, groups, and roles are defined to the ESM so that DC log can only be viewed by Information System Security Officer (ISSO), Information System Security manager (ISSM), Systems Administrator (SA), and Database Administrator (DBA).

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-251627`

### Rule: Custom database code and associated application code must reveal detailed error messages only to the Information System Security Officer (ISSO), Information System Security manager (ISSM), Systems Administrator (SA), and Database Administrator (DBA).

**Rule ID:** `SV-251627r961170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Detailed error messages issued by custom or user-written code can possibly give too much detail to the users. This code should be examined to ensure that this does not happen.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check custom database code to determine if detailed error messages are ever displayed to unauthorized individuals. If detailed error messages are displayed to individuals not authorized to view them, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-251628`

### Rule: CA IDMS must automatically terminate a terminal session after organization-defined conditions or trigger events of terminal inactivity time.

**Rule ID:** `SV-251628r961221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance. If a user does not sign off a terminal after use it can be used for illegitimate purposes. The IDMS RESOURCE TIMEOUT INTERVAL allows the organization to set a limit to the amount of time it can be left unattended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use task SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "RESOURCE TIMEOUT INTERVAL" is found. If the associated value is not the organization-defined timeout number of wall-clock seconds, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-251629`

### Rule: CA IDMS must automatically terminate a batch external request unit after organization-defined conditions or trigger events after the batch program abnormally terminates.

**Rule ID:** `SV-251629r961221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance. If a batch request terminates abnormally the external run unit process needs to be terminated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use task SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "CHKUSER TASK" is found. If the associated value is not the organization-defined number of subtasks that detect abnormally terminated batch external request units, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-251630`

### Rule: CA IDMS must automatically terminate an external run-unit after organization-defined conditions or trigger events of time waiting to issue a database request.

**Rule ID:** `SV-251630r961221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive sessions, such as a logged on user who leaves their terminal, may give a bad actor access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use task SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "EXTERNAL WAIT" is found. If the associated value is not the organization-defined timeout number of wall-clock seconds, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-251631`

### Rule: CA IDMS must automatically terminate a task or session after organization-defined conditions or trigger events of time waiting to get a resource and/or time of inactivity.

**Rule ID:** `SV-251631r961221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance. It may be desired to limit the amount of time a task can wait for a resource before terminating it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use task SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "INACTIVE INTERVAL" is found. If the associated value is not the organization-defined timeout number of wall-clock seconds, this is a finding. Scroll through the returned text until "RUNAWAY INTERVAL" is found. If the associated value is not the organization-defined timeout number of wall-clock seconds, this is a finding.

## Group: SRG-APP-000296-DB-000306

**Group ID:** `V-251632`

### Rule: CA IDMS CV must supply logout functionality to allow the user to implicitly terminate a session initiated by the terminal user.

**Rule ID:** `SV-251632r961224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user does not sign off a terminal after use, it can be used for illegitimate purposes. The IDMS RESOURCE TIMEOUT INTERVAL allows the organization to set a limit to the amount of time it can be left unattended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use TASK SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "RESOURCE TIMEOUT INTERVAL" is found. If the associated value is not the organization-defined timeout number of wall-clock seconds, this is a finding.

## Group: SRG-APP-000296-DB-000306

**Group ID:** `V-251633`

### Rule: CA IDMS CV must supply logout functionality to allow the user to implicitly terminate a session by disconnecting or ending before an explicit logout.

**Rule ID:** `SV-251633r961224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user cannot explicitly end a DBMS session, the session may remain open and be exploited by an attacker; this is referred to as a zombie session. Such logouts may be explicit or implicit. Examples of explicit logouts are: clicking on a "Log Out" link or button in the application window; clicking the Windows Start button and selecting "Log Out" or "Shut Down." Examples of implicit logouts are: closing the application's (main) window; powering off the workstation without invoking the OS shutdown. Both the explicit and implicit logouts must be detected by the DBMS. In all cases, the DBMS must ensure that the user's DBMS session and all processes owned by the session are terminated. This should not, however, interfere with batch processes/jobs initiated by the user during their online session: these should be permitted to run to completion. IDMS must provide a facility by which an inactive user session may be terminated after a predetermined period of time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use TASK SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "INACTIVE INTERVAL" is found. If the associated value is not the organization-defined timeout number of wall-clock seconds, this is a finding. Scroll through the returned text until "RUNAWAY INTERVAL" is found. If the associated value is not the organization-defined timeout number of wall-clock seconds, this is a finding.

## Group: SRG-APP-000296-DB-000306

**Group ID:** `V-251634`

### Rule: CA IDMS CV must supply logout functionality to allow the user to implicitly terminate an external run-unit when a database request has not been made in an organizationally prescribed time frame.

**Rule ID:** `SV-251634r961224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user cannot explicitly end a DBMS session, the session may remain open and be exploited by an attacker; this is referred to as a zombie session. Such logout may be explicit or implicit. Examples of explicit logouts are: clicking on a "Log Out" link or button in the application window; clicking the Windows Start button and selecting "Log Out" or "Shut Down." Examples of implicit logouts are: closing the application's (main) window; powering off the workstation without invoking the OS shutdown. Both the explicit and implicit logouts must be detected by the DBMS. In all cases, the DBMS must ensure that the user's DBMS session and all processes owned by the session are terminated. This should not, however, interfere with batch processes/jobs initiated by the user during his/her online session: these should be permitted to run to completion. IDMS must provide a facility by which an inactive user session may be terminated after a predetermined period of time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use TASK SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "EXTERNAL WAIT" is found. If the associated value is not the organization-defined timeout number of wall-clock seconds, this is a finding.

## Group: SRG-APP-000296-DB-000306

**Group ID:** `V-251635`

### Rule: CA IDMS CV must supply logout functionality to allow the user to implicitly terminate a batch external request unit when the batch job abnormally terminates.

**Rule ID:** `SV-251635r961224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IDMS must provide a facility by which an inactive user session may be terminated after a predetermined period of time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use TASK SYSGEN if online, or program RHDCSGEN if batch. Sign on to the dictionary where the System definition is maintained: "SIGNON DICTIONARY SYSTEM.", for example. Enter: "DISPLAY SYSTEM 123." where 123 is the number of the system being checked. Scroll through the returned text until "CHKUSER TASK" is found. If the associated value is not the organization-defined number of subtasks that detect abnormally terminated batch external request units, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-251636`

### Rule: IDMS must prevent users without the appropriate access from executing privileged functions or tasks within the IDMS environment.

**Rule ID:** `SV-251636r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In general, all functions within IDMS can be controlled, therefore it is up to the IDMS system administrator to determine which functions or tasks are secured or require proper authorization. Any function within the IDMS environment can be considered privileged if the administrator deems it appropriate. Access to different functions is protected through a number of load modules that are generated from assembler macros. The load modules are RHDCSRTT, IDMSCTAB, and IDMSUTAB. The related assembler macros are #SECRTT, #CTABGEN, and #UTABGEN. The #SECRTT macro is used to define different functions to the ESM so that they can be secured. The #UTABGEN macro is used to secure specific OCF/BCF commands. The #CTABGEN macro is used to secure DCMT commands. IDMS provides several tasks, programs and data sets that, in the wrong hands, could allow access to sensitive data or give access to make detrimental changes. These tasks, programs and data sets should be deemed privileged and protected from unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following steps apply to "Online" and "Batch to CV" access to IDMS. If CAGJMAC and AAGJMAC libraries with external security manager (ESM) dataset level security are not secured, this is a finding. If the functions to be protected within the RHDCSRTT, IDMSCTAB, or IDMSUTAB modules are not defined, this is a finding. Note: The recommended method of securing the IDMS environment is through the ESM. The RHDCSRTT module allows users to define the different functions and applications as type EXTERNAL to make them visible to the ESM so that they can be secured. These load modules are used by the IDMS Central Version to understand how access to the IDMS environment is to be controlled. Again, it is not sufficient to merely define what should be secured via the RHDCSRTT module, these functions must be secured through the ESM. The security of the assembler macros and the security load modules must be upheld to protect the environment. Use the ESM to enact Dataset Level Security on the CAGJMAC macro library where the IDMS assembler macros reside. This is to protect unauthorized users from creating their own versions of the security load modules. Also, protect the CUSTLOAD load library or wherever the generated security load modules used by the IDMS environment are stored. By defining the functions to be protected in the RHDCSRTT module and then protecting those functions via the ESM, users are able to protect the DBMS environment. By taking these steps, unauthorized users are prevented from performing privileged functions when executing jobs in either a "Batch to Central Version" or "Online Central Version" environment. If accessing CA IDMS in "Batch Local" mode, access control is performed at the dataset level using the ESM. It is necessary to restrict users from accessing the CA IDMS Database files in Local Mode. If the CA IDMS Database files are not secured using the ESM, this is a finding. If limited access is allowed to database files in a batch to local scenario, consider utilizing a custom EXIT 14. If a user wishes to granularly protect specific DBMS verbs and have not implemented an EXIT 14, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-251637`

### Rule: IDMS must prevent unauthorized users from executing certain privileged commands that can be used to change the runtime IDMS environment.

**Rule ID:** `SV-251637r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensure that a subset DCMT commands are secured so that only those with the appropriate authority are able to execute them. Access to these DCMT commands can allow a user to circumvent defined security policies and procedures, and to make other detrimental changes to the CV environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the following DCMT commands are protected for use by the appropriate users: DCMT DISPLAY MEMORY DCMT VARY DYNAMIC PROGRAM DCMT VARY DYNAMIC TASK DCMT VARY LOADLIB DCMT VARY MEMORY DCMT VARY NUCLEUS DCMT VARY PROGRAM DCMT VARY RUN UNIT DCMT VARY SYSGEN Examine load module IDMSCTAB using CA IDMS utility IDMSCTAD, or by issuing command "DCMT DISPLAY CTAB" while signed onto the CV and reviewing the output. Note: This requires PTF SO08199. If the command codes for the commands listed above are not present in the output, this is a finding. Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Review the output to determine if there are ACTI entries to secure the above commands. Activity numbers are assigned in IDMSCTAB and used in the SRTT formats for the external resource name. Contact the security office if the resource access is not restricted to only users authorized in the site security plan. If the resource access is not restricted to only users authorized in the site security plan, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-251638`

### Rule: IDMS must protect its user catalogs and system dictionaries to prevent unauthorized users from bypassing or updating security settings.

**Rule ID:** `SV-251638r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized access to user profiles, dictionaries, and user catalogs provides the ability to damage the IDMS system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Confirm that the #SECRTT macro contains entries for the following resource names: UPRF for User Profile, SYSTEM for System Dictionary, SYSMSG for System Messages, and CATSYS for the User Catalog. If all of these resource names are not defined to external security, this is a finding.

## Group: SRG-APP-000342-DB-000302

**Group ID:** `V-251639`

### Rule: IDMS must restrict the use of code that provides elevated privileges to specific instances.

**Rule ID:** `SV-251639r961359_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a user has elevated privileges, they may be able to deliberately or inadvertently make alterations to the DBMS structure or data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation, database, and DBMS security configuration (in SRTT and ESM), source code for DBMS internal logic, source code of external modules invoked by the DBMS, and source code of the application(s) using the database. If elevation of DBMS privileges is utilized but not documented, this is a finding. If elevation of DBMS privileges is documented, but not implemented as described in the documentation, this is a finding. If the privilege-elevation logic can be invoked in ways other than intended, or in contexts other than intended, or by subjects/principals other than intended, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-251640`

### Rule: CA IDMS programs that can be run through a CA IDMS CV must be defined to the CV.

**Rule ID:** `SV-251640r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to add programs to be executed under IDMS can be a problem if malicious programs are added. CA IDMS must prevent installation of unauthorized programs and the ability to dynamically register new programs and tasks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine load module RHDCSRTT by executing CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV, and reviewing the output. Note: This requires PTFs SO07995 and SO09476. Check the SRTT for externally secured resource SYST which allows the SYSGEN to be modified and application program definitions added. If "SYST" is not found as the resource type in any of the entries, this is a finding. If "SYST" is secured internally, this is a finding. If "SYST" is found to be secured externally, ensure that the ESM contains the correct definition using the external resource class name and the external name construction rules. If it is not defined or not defined correctly, this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-251641`

### Rule: IDMS terminal and lines that are not secure must be disabled.

**Rule ID:** `SV-251641r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure network functions, ports, protocols, and services exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each load area, run a CREPORT 43 to check the nodes and access types for each node. For each node, issue DCMT D LINE. For each LINE type with a status of InSrv, inspect the access type for potential unauthorized connection types. For TCP/IP, any line with access type SOCKET, issue DCMT D LINE <tcp-line-id>. If any terminals are of type LIST and status InSrv, check port number for a valid port. If the port number is unacceptable as defined in the PPSM CAL, this is a finding. For each terminal with the type of LIST and InSrv, issue DCMT D PTE <pterm-id>. For each task and (possible PARM STRING which could pass a task) identified in the PTE display, issue DCMT D TASK <task-id>. If the task is IDMSJSRV and the associated program is RHDCNP3J, this is not a finding. If the task/program has not been authorized, this is a finding. If other access types (e.g., VTAM, SVC, CCI) have been deemed nonsecure in the PPSM CAL, this is a finding.

## Group: SRG-APP-000431-DB-000388

**Group ID:** `V-251642`

### Rule: CA IDMS must protect the system code and storage from corruption by user programs.

**Rule ID:** `SV-251642r961608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management systems can maintain separate execution domains for each executing process by assigning each process a separate address space. Each process has a distinct address space so that communication between processes is controlled through the security functions, and one process cannot modify the executing code of another process. Maintaining separate execution domains for executing processes can be achieved, for example, by implementing separate address spaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to IDMS DC system and issue DCPROFIL. If HPSPO ENABLED: display is "NO", this is a finding.

## Group: SRG-APP-000431-DB-000388

**Group ID:** `V-251643`

### Rule: CA IDMS must protect system and user code and storage from corruption by user programs.

**Rule ID:** `SV-251643r961608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management systems can maintain separate execution domains for each executing process by assigning each process a separate address space. Each process has a distinct address space so that communication between processes is controlled through the security functions, and one process cannot modify the executing code of another process. Maintaining separate execution domains for executing processes can be achieved, for example, by implementing separate address spaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to IDMS DC system and issue "DCPROFIL". If SYSTEM STORAGE PROTECTED: display is "NO", this is a finding. Issue DCMT D PROGRAM pgmname where pgmname is ADSOMAIN, ADSORUN1, and user programs. If "Storage Prot" is "NO", this is a finding.

## Group: SRG-APP-000431-DB-000388

**Group ID:** `V-251644`

### Rule: CA IDMS must prevent user code from issuing selected SVC privileged functions.

**Rule ID:** `SV-251644r961608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an SVC is used to facilitate interpartition communication for online applications executing under other DC systems, batch application programs, and programs executed under TP monitors other than DC when running on the same LPAR, privileged functions of the SVC can be protected from these entities that do not run within the IDMS DC partition with a combination of the key specification and the disabling of selected SVC functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to IDMS DC system. Issue DCMT D MEM SVC+6D0 to get address of SVC options (svcopt-addr). Issue DCMT D MEM svcopt-addr. With all lengths of 1, at offset 1 is the SVC number, offset 3 contains CVKEY number, offset x' D' contains a flag byte where a setting of X'20' indicates AUTHREQ=YES. If there is no valid number for CVKEY and the flag byte of X'20' is not set, this is a finding. Note: Offsets are subject to change.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-251645`

### Rule: The system storage used for data collection by the CA IDMS server must be protected.

**Rule ID:** `SV-251645r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, the DBMS, associated applications, and infrastructure must leverage transmission protection mechanisms. Satisfies: SRG-APP-000441-DB-000378, SRG-APP-000442-DB-000379</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to IDMS DC system and issue DCPROFIL. If HPSPO ENABLED: display is "NO", this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-251646`

### Rule: The cache table procedures and views used for performance enhancements for dynamic SQL must be protected.

**Rule ID:** `SV-251646r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, the DBMS, associated applications, and infrastructure must leverage transmission protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For CA IDMS CV, issue "SELECT * FROM SYSCA.DSCCACHEOPT". If rows are returned, caching is on. For local, if no statement, SQL_CACHE_ENTRIES=0 exists in the SYSIDMS specification, caching is on. Examine RHDCSRTT in security domain for security on table procedures and views of DSCCACHE table; those supplied at installation (SYSCA.DSCCACHE, SYSCA.DSCCACHEOPT,SYSCA.DSCCACHECTRL, SYSCA.DSCCACHEV) or those created by organization. If no security is found for these table procedures and views, this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-251647`

### Rule: The storage used for data collection by CA IDMS web services must be protected.

**Rule ID:** `SV-251647r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, the DBMS, associated applications, and infrastructure must leverage transmission protection mechanisms. Satisfies: SRG-APP-000441-DB-000378, SRG-APP-000442-DB-000379</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to IDMS DC system and issue "DCPROFIL". If SYSTEM STORAGE PROTECTED: display is "NO", this is a finding. Issue DCMT D PROGRAM RHDCWSSP. If Storage Prot is "NO", this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-251648`

### Rule: The storage used for data collection by CA IDMS Server and CA IDMS Web Services must be protected from online display and update.

**Rule ID:** `SV-251648r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, the DBMS, associated applications, and infrastructure must leverage transmission protection mechanisms. Satisfies: SRG-APP-000441-DB-000378, SRG-APP-000442-DB-000379</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SRTT for externally secured ACTI which can be used to secure DCMT DISPLAY MEMORY and DCMT VARY MEMORY. Examine load module RHDCSRTT using CA IDMS utility IDMSSRTD, or by issuing command "DCMT DISPLAY SRTT" while signed onto the CV and reviewing the output. Note: This requires PTFs SO07995 and SO09476. If RESTYPE=ACTI is not found as the resource type in any of the entries, this is a finding. If RESTYPE=ACTI is found but the entry is secured internally, this is a finding. Examine load module IDMSCTAB using CA IDMS utility IDMSCTAD, or by issuing command "DCMT DISPLAY CTAB" while signed onto the CV and reviewing the output. Note: This requires PTF SO08199. Verify that these DCMT command codes are present: N022 - DISPLAY MEMORY N033 - VARY MEMORY If they are not present, this is a finding.

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-251649`

### Rule: IDMS must check for invalid data and behave in a predictable manner when encountered.

**Rule ID:** `SV-251649r961656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If data inputs are specifically identified by the organization as exempt from validity checks, this is not applicable. If SQL-defined tables, DISPLAY TABLE <schema-name>.<table-name> . If there is not a CHECK for the columns and accompanying accepted values, this is a finding. If network-defined records, DISPLAY SCHEMA or DISPLAY RECORD. If there is no CALL to a procedure BEFORE STORE and BEFORE MODIFY, this is a finding. If the procedure does not validate the non-exempt columns, this is a finding. Other applications and front-ends using mapping can use the automatic editing feature and edit and code tables to verify that an input value is valid. Review the source code for checks, procedures, and edits to identify how the system responds to invalid input. If it does not implement the documented behavior, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-251650`

### Rule: Maintenance for security-related software updates for CA IDMS modules must be provided.

**Rule ID:** `SV-251650r1001008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a problem is found in IDMS, corrective maintenance is published to correct the problem (including security related problems). Published fixes should be applied to the IDMS system to correct any problems found.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determining which PTFs have been applied, a query can be done to an SMP/E CSI using the IBM SMP/E utility. New and existing PTFs must be reviewed using CA CARS or CSO in a timeframe determined by an authoritative source. If not, this is a finding.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-251652`

### Rule: The DBMS must develop a procedure to limit the number of concurrent sessions to an organization-defined number per user for all accounts and/or account types.

**Rule ID:** `SV-251652r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions utilizing a DBMS. Unlimited concurrent connections to the DBMS could allow a successful Denial of Service (DoS) attack by exhausting connection resources; and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. This requirement addresses concurrent session control for a single account. It does not address concurrent sessions by a single user via multiple system accounts; and it does not deal with the total number of sessions across all accounts. The capability to limit the number of concurrent sessions per user must be configured in or added to the DBMS (for example, by use of a logon trigger), when this is technically feasible. Note that it is not sufficient to limit sessions via a web server or application server alone, because legitimate users and adversaries can potentially connect to the DBMS by other means. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to consider the work requirements of the various types of users. For example, two might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session. (Sessions may also be referred to as connections or logons, which for the purposes of this requirement are synonyms.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult the system DBA and review system procedures for measures that establish a dataset to be used as a lock file. If there is no such procedure, this is a finding.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-251653`

### Rule: The DBMS must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-251653r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any DBMS or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, usernames, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, Social Security numbers, and credit card numbers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult the system DBA and review system procedures for WTO exits that modify IDMS messages that go to non-privileged users. If there is no procedure, this is a finding.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-251654`

### Rule: CA IDMS must use pervasive encryption to cryptographically protect the confidentiality and integrity of all information at rest in accordance with data owner requirements.

**Rule ID:** `SV-251654r1028319_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification. Satisfies: SRG-APP-000428-DB-000386, SRG-APP-000429-DB-000387, SRG-APP-000231-DB-000154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this CA IDMS has no requirement for confidentiality and integrity of all information at rest in accordance with the data owners requirements, this not applicable. If required files are not defined as a VSAM dataset this is a finding. Perform the following for the VSAM dataset 1. LISTC ENT('dsn') ALL" Where "dsn" is the DSNAME of the cluster; review the ATTRIBUTES section of the output to ensure that the database is defined as NONINEXED (the cluster is an ESDS). If not, this is a finding. 2. In the IDCAMS LISTC output, look for the SMSDATA section. If none is found this is a finding. Otherwise, find the "DATACLASS" name and query the systems programmer to ensure that the SMS data class specifies "Extended Format" but does not specify "Extended Addressing". If not, this is a finding. 3. In the IDCAMS LISTC output: Find the "STORAGECLASS" and query the systems programmer to ensure it supports extended format VSAM dataset. If not, this is a finding. 4. Confirm that the database(s) have a data set key label. Places to check for a data set key label: a. In the SMS data class definition by reviewing the entry for the appropriate data class in ISMF b. In the output of an IDCAMS LISTC in the ENCRYPTIONDATA section. If "DATA SET ENCRYPTION" is "YES", then the label will be displayed after "DATA SET KEY LABEL". c. The key label may be assigned through the ESM. Query the security team to determine if this is the case. 5. The database(s) must be defined in the DMCL as "VSAM". Run "IDMSLOOK" to print the contents of the DMCL and look for the desired database(s). If the TYPE column is not "VSAM", this is a finding.

## Group: SRG-APP-000313-DB-000309

**Group ID:** `V-251655`

### Rule: The DBMS must associate organization-defined types of security labels having organization-defined security label values with information in process.

**Rule ID:** `SV-251655r961272_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the DBMS to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of the DBMS product, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the site system plan does not require security labels, this requirement is Not Applicable. Consult the system DBA and review system procedures for an application that maintains security label processing. If there is no label application procedure, this is a finding.

## Group: SRG-APP-000514-DB-000383

**Group ID:** `V-251656`

### Rule: CA IDMS must implement NIST FIPS 140-2 validated cryptographic modules to protect data-in-transit.

**Rule ID:** `SV-251656r961857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. For detailed information, refer to NIST FIPS Publication 140-2, Security Requirements for Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that connection to IDMS is FIPS-compliant. 1. For ODBC and JDBC Type 2 connections: a. Configure the Data Source to enable the DTS-JCLI logging option. b. Perform a connection test using the "Test" function on the administrator. c. View the generated log entries to determine the TLS version, cipher algorithm, and certificate employed. 2020/04/27 09:51:41.946 P:0000502C T:00005DC8 JCLI Trace: SSL_connect(832) successful! 2020/04/27 09:51:41.946 P:0000502C T:00005DC8 JCLI Trace: SSL_connect(832) connection attempts: 1 2020/04/27 09:51:41.947 P:0000502C T:00005DC8 JCLI Trace: SSL_connect(832) TLS version TLSv1.2 2020/04/27 09:51:41.947 P:0000502C T:00005DC8 JCLI Trace: SSL_connect(832) cipher TLS_RSA_WITH_AES_256_CBC_SHA256 (this should be one or more of the accepted ciphers) Cipher Specifications 3DES_SHA AES_256_SHA AES_128_SHA If connection is not verified this is a finding. 2. For all connection types: IBM provides configuration options for multiple SSL components, to force FIPS-140 compliance. a. System SSL: The environment variable GSK_FIPS_STATE specifies GSK_FIPS_STATE_ON in the envar file in the GSKSRVR home directory or message "GSK01057I SSL server starting in FIPS mode" is in the JES log. b. ICFS: Review the JES log for the ICSF region for the following message is issued on startup CSFM015I FIPS 140 SELF CHECKS FOR PKCS11 SERVICES SUCCESSFUL. If either of the above is true this is not a finding. If none of the above is true this is a finding.

