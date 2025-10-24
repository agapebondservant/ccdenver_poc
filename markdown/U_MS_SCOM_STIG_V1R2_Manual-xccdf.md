# STIG Benchmark: Microsoft SCOM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-237423`

### Rule: Members of the SCOM Administrators Group must be reviewed to ensure access is still required.

**Rule ID:** `SV-237423r984107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When people leave their roles, their group memberships are often times not updated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From Active Directory Users and Computers, search for the group containing SCOM administrators. Review the users who are listed in this group. If any user in this group is no longer with the organization, no longer requires SCOM administration rights, or is no longer in a SCOM administration role within the organization, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-237424`

### Rule: Manually configured SCOM Run As accounts must be set to More Secure distribution.

**Rule ID:** `SV-237424r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Microsoft SCOM privileged Run As accounts are used to execute work flow tasks on target endpoints. A SCOM Run As account creates an interactive log on session to perform its tasks. The interactive session could allow an attacker to harvest and reuse these credentials. The SCOM less-secure distribution option configures a Run As account to run on every SCOM agent within the environment, making it easier for an attacker to compromise a critical account. The use of the SCOM "More Secure" option restricts Run As accounts to specific systems. This restricts a compromised account to a specific set of systems limiting the ability of an attacker to move laterally within the network. A less secure distribution means that if any server running a SCOM agent is compromised, then the accounts credentials may be reused by an attacker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the account distribution settings on the SCOM Management server. Open the Operations Console and select the Administration workspace. Under Run As Configuration, select Accounts. Double-click on each account listed under the Windows type and select the distribution tab (note that the network system and local system accounts do not need to be checked). If any Run As account is set to the "less secure" distribution option, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-237425`

### Rule: SCOM Run As accounts used to manage Linux/UNIX endpoints must be configured for least privilege.

**Rule ID:** `SV-237425r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Microsoft SCOM privileged Run As accounts are used to execute work flow tasks on target endpoints. A SCOM Run As account must only have the level of privileges required to perform the defined SCOM actions. An account with full administrative (SUDO) privileges could be used to breach security boundaries and compromise the endpoint.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Microsoft SCOM environment is not used to monitor Linux/UNIX endpoints, this check is Not Applicable. Review the account permission settings on the SCOM Management server. Log on to a subset of Linux or UNIX servers being monitored by SCOM and look at the Sudoers file. Verify that the SCOM account does not have Sudo all permissions. Alternatively, the following command can be run from the machine "sudo -l -U <Run As account Name>". If any Run As account used for Linux\UNIX endpoint management has the SUDO ALL permissions, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-237426`

### Rule: The Microsoft SCOM Agent Action Account must be a local system account.

**Rule ID:** `SV-237426r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SCOM agent action account is the account agent used to perform tasks on an individual machine. By default, the action agent account is the local system account, but this can be configured to run as a service account. In that scenario, the account will be running locally in memory and could be used by an attacker to laterally move throughout an environment. Using the local system account limits the ability to laterally traverse within the environment if a specific endpoint is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the SCOM console, go to the administration workspace. Under Run As Configuration, select Profiles. Double-click on the Default Action Account in the center pane. From the box that appears, select the Run As accounts link. Under the Account Name column, verify that ONLY management servers are running with a specified user account. All other accounts should say Local System Action Account. If any non-management servers have a specific user account listed, this is a finding. Elevate to a CAT I if the specified account is a local administrator on other systems. This can be downgraded to CAT III if the agent action account has been restricted from logging on to all other systems except the monitored endpoint, as the risk of credential leakage has been sufficiently mitigated.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-237427`

### Rule: The Microsoft SCOM Run As accounts must only use least access permissions.

**Rule ID:** `SV-237427r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Microsoft SCOM privileged Run As accounts are used to execute work flow tasks on target endpoints. Run As Accounts are interactive logon sessions on a system. An attacker who has compromised one of those systems could potentially reuse the credentials of a Run As account on another system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the User ID(s) in SCOM: Open the Operations Console and select the Administration workspace. Under Run As Configuration, select Accounts. Double-click on each account listed under the Windows type and select the credentials tab (note that the network system and local system accounts do not need to be checked). Note the Username and domain name. Click on the Distribution tab and note the computer names that the account is distributed to. Validate Permissions in Active Directory: For each SCOM Run As account, open the Active Directory Users and Computers MMC and if necessary connect to the appropriate domain. Right-click on the domain and select "Find". In the "Name" field, type the User ID and click "Find Now". The account will appear in the results below. Double-click on the account and select the "Member Of" tab. Review the groups listed. If any group listed is an administrator on any system other than the systems the account is distributed to, this is a finding. If the account is part of Domain Administrators or Enterprise Administrators, elevate to CAT I.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-237428`

### Rule: The Microsoft SCOM administration console must only be installed on Management Servers and hardened Privileged Access Workstations.

**Rule ID:** `SV-237428r960792_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Microsoft SCOM management servers are considered high value IT resources where compromise would cause a significant impact to the organization. The Operations Manager console contains APIs that an attacker can use to decrypt Run As accounts or install malicious management packs. If a SCOM console sits on a Tier 2 device, an attacker could use the administrator's alternate credentials to exploit SCOM. A Privileged Admin Workstation (PAW) device provides configuration and installation requirements for dedicated Windows workstations used exclusively for remote administrative management of designated high-value IT resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SCOM console is installed on a Terminal Server within a dedicated hardened management forest, this check is Not Applicable. If the console is installed on a general purpose device and the user is NOT a SCOM administrator, this is not a finding. Examples would be individuals in the Network Operations Center (NOC) who only respond to alerts. From the SCOM Administrator(s) productivity workstation (i.e. it has internet, or office applications), check for the presence of the operations console. This can be done by clicking the windows button and typing "Operations" in the search bar. If the console is installed on a general purpose device and the user is NOT a SCOM administrator, this is not a finding. Examples would be individuals in the Network Operations Center (NOC) who only respond to alerts. If the Operations console appears, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-237429`

### Rule: The Microsoft SCOM Service Accounts and Run As accounts must not be granted enterprise or domain level administrative privileges.

**Rule ID:** `SV-237429r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Microsoft SCOM privileged Run As accounts are used to execute work flow tasks on target endpoints. A SCOM Run As account must only have the level of privileges required to perform the defined SCOM actions. An account with full administrative at the domain or enterprise level could be used to breach security boundaries and compromise the endpoint.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the User ID(s) for the appropriate accounts in SCOM: Open the Operations Console and select the Administration workspace. Under Run As Configuration, select Accounts. Double-click on each account listed under the Windows type and select the credentials tab (note that the network system and local system accounts do not need to be checked). Note the Username and domain name. Open Active Directory Users and Computers. Determine rights in Active Directory: Review the Domain Admins, Administrators (in AD), Enterprise Admins, Schema Admins groups, and any group that is a member of these groups. If a SCOM Run-As account or Service account is a member of any of these groups, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-237430`

### Rule: SCOM SQL Management must be configured to use least privileges.

**Rule ID:** `SV-237430r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Microsoft SCOM's SQL management requires a Run as solution because the local system account will not have the required permissions to monitor SQL. If the Run As account is created with elevated database privileges on the SQL endpoint, this can be used to modify SQL databases, breach security boundaries, or otherwise compromise the endpoint.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Microsoft SQL management packs for SCOM are not imported, this check is Not Applicable. Determine which SQL Servers are managed by SCOM: From the Operations Console, click on the Monitoring workspace. In the left pane, expand the "Microsoft SQL Servers folder" and click on the Computers icon (note older versions of this management pack may be version specific). Make note of the servers listed. Log on to SQL Server Management Studio and connect to servers being managed in SCOM. Expand the Security Tab and select Logins. Verify that NT System\Authority, NT Service\HealthService, or the SQL Run As account has not been granted System Admin privileges (SA rights). If the any of these accounts have been granted SA privileges, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-237431`

### Rule: The Microsoft SCOM server must back up audit records at least every seven days onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-237431r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Regularly backing up audit records to a different system or onto separate media than the system being audited helps to assure, in the event of a catastrophic system failure, the audit records will be retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the security logs as well as the Operations Manager logs on the SCOM management server are being ingested by a tool such as Splunk, ArcSite, or Azure Log Analytics. If no effort is being made to retain log data on the SCOM server, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-237432`

### Rule: The Microsoft SCOM server must be running Windows operating system that supports modern security features such as virtualization based security.

**Rule ID:** `SV-237432r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running older but supported operating systems lack modern security features that mitigate attack surfaces. Attackers face a higher level of complexity to overcome during a compromise attempt.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the operating system version. From the SCOM management servers, type winver and press enter. If the operating system is not Windows Server 2016 or later, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-237433`

### Rule: SCOM unsealed management packs must be backed up regularly.

**Rule ID:** `SV-237433r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SCOM's configuration information is stored within unsealed management packs. Even without SQL backups, a catastrophic failure to SCOM can be recovered from quickly if the unsealed management packs have been backed up. Satisfies: SRG-APP-000516-NDM-000340, SRG-APP-000516-NDM-000341</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
There is more than one way to configure this, and it will be at an administrator's discretion. Open task scheduler and check for the presence of a scheduled task to back up unsealed management packs. If present, review the script to determine where backups are being stored. Verify that the unsealed management packs are being saved to the location specified in the task and that the location is being backed up regularly. Alternatively, several free management packs do exist to automate this process within SCOM, or an administrator could automate this with their own custom management pack or using an orchestration tool such as System Center Orchestrator. This is not a finding if an administrator can show that one of these is installed/configured and that unsealed management packs are being written to the configured location. If unsealed management packs are not being exported to disk and backed up, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-237434`

### Rule: If a certificate is used for the SCOM web console, this certificate must be generated by a DoD CA or CA approved by the organization.

**Rule ID:** `SV-237434r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Web certificates should always be signed by a trusted signer and never self-signed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the web console server, open IIS. Right-click on the Default Website and choose Edit Bindings. Select the https binding and click edit. Click View to view the certificate being used to protect the website. If the certificate is not issued by a DoD CA or a trusted internal CA, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-237435`

### Rule: The Microsoft SCOM SNMP Monitoring in SCOM must use SNMP V3.

**Rule ID:** `SV-237435r961506_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SNMP Versions 1 and 2 do not use a FIPS-validated Keyed-Hash message Authentication Code (HMAC). SCOM has the capability of monitoring all versions of SNMP. As such, SNMP 1 and 2 monitoring should only be done if the device being monitored does not support SNMP V3.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the SCOM Console, select the Administration workspace. Navigate to Run As Configuration and select Accounts. Review all of the listed Accounts. If any account is listed under the "Community String" type, this is a finding.

## Group: SRG-APP-000080-NDM-000345

**Group ID:** `V-237436`

### Rule: The Microsoft SCOM server must use an active directory group that contains authorized members of the SCOM Administrators Role Group.

**Rule ID:** `SV-237436r984088_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial installation, SCOM grants the Builtin\Administrators group administrator rights to the application. This configuration will allow any local administrator to the SCOM server to have full administrative rights into SCOM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Operations Console and select the Administrative workspace. In the left pane, expand Security and select User Roles. In the center pane, double-click on Operations Manager Administrators. If Builtin\Administrators is listed, this is a finding.

## Group: SRG-APP-000080-NDM-000345

**Group ID:** `V-237437`

### Rule: The default Builtin\Administrators group must be removed from the SCOM Administrators Role Group.

**Rule ID:** `SV-237437r984088_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SCOM servers with default well-known operating system groups defined the SCOM Administrators Global Group may allow a local administrator access to privileged SCOM access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SCOM Administrators Global Group and verify that the Built-in\Administrators Group is not a member. If the Built-in\Administrators group is a member, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-237438`

### Rule: The SCOM Web Console must be configured for HTTPS.

**Rule ID:** `SV-237438r961557_rule`
**Severity:** high

**Description:**
<VulnDiscussion>HTTP sessions are sent in clear text and can allow a man in the middle to recon the environment. The web console itself does not allow for administrative actions, so most of the risk associated with http authentication is inherently mitigated. However, this would allow an attacker to intercept SCOM web-console traffic for reconnaissance purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is Not Applicable if the SCOM web console is not installed. From the SCOM web console server, open IIS. Right-click on the Default Website and choose edit bindings. Examine the bindings for the web console and verify that only https is an option. If http is present or if there is no https binding, this is a finding.

## Group: SRG-APP-000224-NDM-000270

**Group ID:** `V-237439`

### Rule: All SCOM servers must be configured for FIPS 140-2 compliance.

**Rule ID:** `SV-237439r1043181_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not validated and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms. SCOM is FIPS-compliant out of the box with the exception of the Web Console.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From a SCOM Management server, open the registry editor. Navigate to the following key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\FipsAlgorithmPolicy Verify that the "Enabled" key is set to 1. If the "Enabled" key is not set to 1 or is not present, this is a finding. From a command prompt, open the following file with notepad: C:\Windows\Micosoft.NET\Framework]v2.0.50727\CONFIG\machine.config. Immediately following the <ConfigSection>, look for <cryptographySettings>. If the <cryptographySettings> section does not exist under <ConfigSection> of the machine.config file, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-237440`

### Rule: A host-based firewall must be configured on the SCOM management servers.

**Rule ID:** `SV-237440r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent a DDoS, a firewall that inspects and drops packets must be configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The steps in this check will vary based on the host-based firewall being used in the environment. For Windows Firewall, type wf.msc. Verify that the firewall is set to On. Click on Inbound rules and verify that there are no any-any allow rules in any profile. If McAfee is installed, it will be visible in the system tray. Verify with a McAfee administrator that there are no any-any rules allowing full access. If no host-based firewall is installed, or a host-based firewall is configured to allow all traffic inbound, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-272361`

### Rule: The version of SCOM running on the system must be a supported version.

**Rule ID:** `SV-272361r1067605_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
SCOM is no longer supported by the vendor. If the system is running SCOM, this is a finding.

