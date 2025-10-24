# STIG Benchmark: Active Directory Forest Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480

**Group ID:** `V-243502`

### Rule: Membership to the Schema Admins group must be limited.

**Rule ID:** `SV-243502r1026198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Schema Admins group is a privileged group in a forest root domain. Members of the Schema Admins group can make changes to the schema, which is the framework for the Active Directory forest. Changes to the schema are not frequently required. This group only contains the Built-in Administrator account by default. Additional accounts must only be added when changes to the schema are necessary and then must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Active Directory Users and Computers" on a domain controller in the forest root domain. Navigate to the "Users" container. Right-click on "Schema Admins" and select "Properties", and then select the "Members" tab. If any accounts other than the built-in Administrators group are members, verify their necessity with the ISSO. If any accounts are members of the group when schema changes are not being made, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243503`

### Rule: Anonymous Access to AD forest data above the rootDSE level must be disabled. 

**Rule ID:** `SV-243503r1026201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For Windows Server 2003 or above, the dsHeuristics option can be configured to override the default restriction on anonymous access to AD data above the rootDSE level. Anonymous access to AD data could provide valuable account or configuration information to an intruder trying to determine the most effective attack strategies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. At the command line prompt enter (on a single line): dsquery * "cn=Directory Service, cn=Windows NT,cn=Services,cn=Configuration,dc=[forest-name]" -scope base -attr * (Where dc=[forest-name] is the fully qualified LDAP name of the root of the domain being reviewed.) Example: The following is an example of the dsquery command for the vcfn.ost.com forest. dsquery * "cn=Directory Service,cn=Windows NT,cn=Services,cn=Configuration, dc=vcfn,dc=ost,dc=com -scope base -attr * 2. If the dsHeuristics attribute is listed, note the assigned value. 3. If the dsHeuristics attribute is defined and has a "2" as the 7th character, then this is a finding. Examples of values that would be a finding as follows: "0000002", "0010002", "0000002000001". (The 7th character controls anonymous access.) Supplementary Notes: Domain controllers have this option disabled by default. However, this check verifies that the option has not been enabled. The dsHeuristics option can be configured with the Windows Support Tools Active Directory Service Interfaces Editor (ADSI Edit) console (adsiedit.msc).

## Group: SRG-OS-000355

**Group ID:** `V-243504`

### Rule: The Windows Time Service on the forest root PDC Emulator must be configured to acquire its time from an external time source.

**Rule ID:** `SV-243504r1026204_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the Windows Time service is used to synchronize time on client computers (workstations and servers) throughout an AD forest, the forest root domain PDC Emulator is the normal default to provide the authoritative time source for the entire forest. To obtain an accurate time for itself, the forest root domain PDC Emulator acts as a client to an external time source. If the Windows Time service on the forest root domain PDC Emulator is not configured to acquire the time from a proper source, it may cause time service clients throughout the forest to operate with the inaccurate time setting. When a Windows computer operates with an inaccurate time setting, access to resources on computers with the accurate time might be denied. This is notably true when Kerberos authentication is utilized. Operation with an inaccurate time setting can reduce the value of audit data and invalidate it as a source of forensic evidence in an incident investigation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to the domain controller with the PDC Emulator role in forest root domain; it is NA for other domain controllers in the forest. Determine the domain controller with the PDC Emulator role in the forest root domain: Windows 2016 or later: Open "Windows PowerShell". Enter "Get-ADDomain -Identity [Forest Root Domain] | FT PDCEmulator", where [Forest Root Domain] is the forest root domain name, such as "example.mil". (This can also be entered without the -Identity parameter if running within the forest root domain.) Windows 2016: Open "Active Directory Users and Computers" from a domain controller in or connected to the forest root (available from various menus or run "dsa.msc"). Select "Action" in the menu, then All Tasks >> Operations Masters. Select the "PDC" tab. On the system with the PDC Emulator role, open "Windows PowerShell" or an elevated "Command Prompt" (run as administrator). Enter "W32tm /query /configuration". Under the "NtpClient" section: If the value for "Type" is not "NTP", this is a finding. If the value for "NtpServer" is not an external DOD time source, this is a finding. If an alternate time synchronization tool is used and is not enabled or not configured to a synchronize with an external DOD time source, this is a finding. The US Naval Observatory operates stratum 1 time servers, identified at https://www.cnmoc.usff.navy.mil/Our-Commands/United-States-Naval-Observatory/Precise-Time-Department/Network-Time-Protocol-NTP/. Time synchronization will occur through a hierarchy of time servers down to the local level. Clients and lower-level servers will synchronize with an authorized time server in the hierarchy.

## Group: SRG-OS-000480

**Group ID:** `V-243505`

### Rule: Changes to the AD schema must be subject to a documented configuration management process. 

**Rule ID:** `SV-243505r1026206_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Poorly planned or implemented changes to the AD schema could cause the applications that rely on AD (such as web and database servers) to operate incorrectly or not all. Improper changes to the schema could result in changes to AD objects that are incompatible with correct operation of the Windows domain controller and the domain clients. This could cause outages that prevent users from logging on or accessing Windows server resources across multiple hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Interview the ISSO. 2. Obtain a copy of the site's configuration management procedures documentation. 3. Verify that there is a local policy that requires changes to the directory schema to be processed through a configuration management process. This applies to directory schema changes whether implemented in a database or other types of files. For AD, this refers to changes to the AD schema. 4. If there is no policy that requires changes to the directory schema to be processed through a configuration management process, then this is a finding.

## Group: SRG-OS-000324

**Group ID:** `V-243506`

### Rule: Update access to the directory schema must be restricted to appropriate accounts.

**Rule ID:** `SV-243506r1026208_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A failure to control update access to the AD Schema object could result in the creation of invalid directory objects and attributes. Applications that rely on AD could fail as a result of invalid formats and values. The presence of invalid directory objects and attributes could cause failures in Windows AD client functions and improper resource access decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Start a Schema management console. (See supplemental notes.) Select and then right-click on the Active Directory Schema entry in the left pane. Select Permissions. If any of the permissions for the Schema object are not at least as restrictive as those below, this is a finding. The permissions shown are at the summary level. More detailed permissions can be viewed by selecting the Advanced button, selecting the desired entry, and the Edit button. Authenticated Users: Read Special Permissions The Special permissions for Authenticated Users are List and Read type. If detailed permissions include any additional Permissions or Properties this is a finding. System: Full Control Enterprise Read-only Domain Controllers: Replicating Directory Changes Replicating Directory Changes All Replicating Directory Changes In Filtered Set Schema Admins: Read Write Create all child objects Change schema master Manage replication topology Monitor active directory replication Read only replication secret synchronization Reanimate tombstones Replicating Directory Changes Replicating Directory Changes All Replicating Directory Changes In Filtered Set Replication synchronization Update schema cache Special permissions (Special permissions = all except Full, Delete, and Delete subtree when detailed permissions viewed.) Administrators: Manage replication topology Replicating Directory Changes Replicating Directory Changes All Replicating Directory Changes In Filtered Set Replication Synchronization Enterprise Domain Controllers: Manage replication topology Replicating Directory Changes Replicating Directory Changes All Replicating Directory Changes In Filtered Set Replication Synchronization Supplemental Notes: If the Schema management console has not already been configured on the computer, create a console by using the following: The steps for adding the snap-in may vary depending on the Windows version. Register the required DLL module by typing the following at a command line "regsvr32 schmmgmt.dll". Run "mmc.exe" to start a Microsoft Management Console. Select Add/Remove Snap-in from the File menu. From the Available Standalone Snap-ins list, select Active Directory Schema Select the Add button. Select the OK button. When done using the console, select Exit from the File (or Console) menu. Select the No button to the Save console settings... prompt (unless the SA wishes to retain this console). If the console is retained, the recommended name is schmmgmt.msc and the recommended location is the [systemroot]\system32 directory.

## Group: SRG-OS-000324

**Group ID:** `V-269098`

### Rule: Windows Server hosting Active Directory Certificate Services (AD CS) must enforce Certificate Authority (CA) certificate management approval for certificate requests.

**Rule ID:** `SV-269098r1106505_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When users are requesting new certificates through AD CS, there must be management approval and awareness for these requests. Without this, a user or bad actor could request certificates they should not have or should not have access to.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Certificate templates with the following extended key usages AND that allow a requestor to supply the subject name in the request require manual approval. In the AD CS web server properties, select "VulnerableCertTemplate" properties. Verify that "Subject Name" and "Supply in the request" are selected. If "Subject Name" AND "Supply in the request" are selected and if manual approval is not required, this is a finding. If the "Supply in Request" is NOT selected, and the Enroll Permissions for the template have been limited to a select group of users/administrators, this is not a finding.

## Group: SRG-OS-000324

**Group ID:** `V-269099`

### Rule: Windows Server running Active Directory Certificate Services (AD CS) must be managed by a PAW tier 0.

**Rule ID:** `SV-269099r1026184_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that a site has set aside one or more PAWs for remote management of AD CS. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a site has set aside one or more PAWs for remote management of AD CS. A dedicated AD CS/CA Admin account that is only usable on tier 0 PAW or the ADCS server must be used to manage the certificate authority and approve requests. Review any available site documentation. Verify that any PAW used to manage high-value IT resources of a specific tier are used exclusively for managing high-value IT resources assigned to only one tier. If the site has not set aside one or more PAWs for remote management of AD CS, this is a finding.

