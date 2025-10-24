# STIG Benchmark: Microsoft Windows PAW Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243442`

### Rule: Administrators of high-value IT resources must complete required training.

**Rule ID:** `SV-243442r722897_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Required training helps to mitigate the risk of administrators not following required procedures. High-value IT resources are the most important and critical IT resources within an organization. They contain the most sensitive data in an organization, perform the most critical tasks of an organization, or have access to and can control all or nearly all IT resources within an organization. Requiring a PAW used exclusively for remote administrative management of designated high-value IT resources, including servers, workstations, directory services, applications, databases, and network components, will provide a separate "channel" for the performance of administrative tasks on high-value IT resources and isolate these functions from the majority of threats and attack vectors found on higher-risk standard client systems. A main security architectural construct of a PAW is to remove non-administrative applications and functions from the PAW. Technical controls for securing high-value IT resources will be ineffective if administrators are not aware of key security requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review site training records and verify the organization's system administrators of high-value IT resources have received the following initial and annual training: - Remotely manage high-value IT resources only via a PAW. - Administrative accounts will not be used for non-administrative functions (for example, read email, browse Internet). If required training has not been completed by the organization's system administrators of high-value IT resources, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243443`

### Rule: Site IT resources designated as high value by the Authorizing Official (AO) must be remotely managed only via a Windows privileged access workstation (PAW).

**Rule ID:** `SV-243443r722900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The AO must designate which IT resources are high value. The list must include the following IT resources: - Directory service (including Active Directory) - Cloud service - Identity management service - Privileged access management service - Credential management service - Security management service (anti-virus, network monitoring/scanning, IDS/IPS, etc.) - Any sensitive business/mission service - Any other IT resource designated as high value by the AO Note: A high-value IT resource is defined as any IT resource whose purpose is considered critical to the organization or whose loss or compromise would cause a significant impact on the organization. Note: Sensitive business/mission service is any business or mission service that needs additional protection from higher-risk IT services based on the nature of the function it provides; sensitivity of the data it consumes, processes, or stores; or criticality to the operation of the organization. High-value IT resources are the most important and critical IT resources within an organization. They contain the most sensitive data in an organization, perform the most critical tasks of an organization, or have access to and can control all or nearly all IT resources within an organization. Administrator accounts for high-value IT resources must be protected against various threats and attacks because threats to sensitive privileged accounts are high and risk of compromise is increasing. Requiring a PAW used exclusively for remote administrative management of designated high-value IT resources, including servers, workstations, directory services, applications, databases, and network components, will provide a separate "channel" for the performance of administrative tasks on high-value IT resources and isolate these functions from the majority of threats and attack vectors found on higher-risk standard client systems. Some IT resources, by the nature of the function they perform, should always be considered high value and should be remotely administered only via a PAW. The IT resources listed above are in this category. Note: The term "manage" in the Requirement statement includes any remote connection to a high-value IT resource (for example, to view resource status and current configuration or to make changes to any resource configuration).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review site documentation to confirm required high-value IT resources are remotely managed only via a PAW. Verify the site maintains a list of designated high-value IT resources and the list contains the following IT resources (if deployed at the site): - Active Directory - Cloud service - Identity management service - Privileged access management service - Credential management service - Security management service (anti-virus, network monitoring/scanning, IDS/IPS, etc.) - Any sensitive business/mission service - Any other IT resource designated as high value by the Authorizing Official (AO) Identify the PAWs set up to manage these high-value IT resources. If the organization does not maintain a list of designated high-value IT resources or has not set up PAWs to remotely manage its high-value IT resources, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243444`

### Rule: Administrative accounts of all high-value IT resources must be assigned to a specific administrative tier in Active Directory to separate highly privileged administrative accounts from less privileged administrative accounts.

**Rule ID:** `SV-243444r852041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: The Microsoft Tier 0-2 AD administrative tier model (https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#ADATM_BM) is an example. A key security construct of a PAW is to separate administrative accounts into specific trust levels so that an administrator account used to manage an IT resource at one trust level cannot be used to manage IT resources at another trust level. This architecture protects IT resources in a tier from threats from higher-risk tiers. Isolating administrative accounts by forcing them to operate only within their assigned trust zone implements the concept of containment of security risks and adversaries within a specific zone. The Tier model prevents escalation of privilege by restricting what administrators can control and where they can log on.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In Active Directory, verify an Organizational Unit (OU) and Group hierarchy have been set up to segregate administrative accounts used to manage both high-value IT resources and PAWs into assigned tiers. Verify each administrative account and each PAW has been assigned to one and only one tier. If the site has not set up a tier structure on Active Directory for administrative accounts used to manage either high-value IT resources or PAWs, this is a finding. If any administrative account used to manage either high-value IT resources or PAWs is assigned to more than one tier, this is a finding. If each administrative account and each PAW has not been assigned to one and only one tier, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243445`

### Rule: A Windows PAW must only be used to manage high-value IT resources assigned to the same tier.

**Rule ID:** `SV-243445r722906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: Allowed exception - For sites that are constrained in the number of available workstations, an acceptable approach is to install lower-tier administrative accounts on a separate virtual machine (VM) on the PAW workstation where higher-tier administrative accounts are installed on the host OS and lower-tier administrative accounts are installed in a VM. The VM will provide acceptable isolation between administrative accounts of different tiers. Note: Relationship between the exception in WPAW-00-000500 and WPAW-00-001000 and requirement WPAW-00-001800: WPAW-00-000500 and WPAW-00-001000 allow an exception to the requirement for sites constrained in the number of available workstations. Lower-tier, high-value admin accounts can operate in a VM if the higher-tier, high-value admin accounts operate in the VM host-OS, but WPAW-00-001800 is more appropriate for a multiple PAW VM environment. If administrative accounts assigned to different tiers were installed on the same PAW, it would be impossible to isolate administrative accounts to specific trust zones and protect IT resources from one trust zone (tier) from threats from high-risk trust zones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a site has set aside one or more PAWs for remote management of high-value IT resources assigned to a specific tier. Review any available site documentation. Verify that any PAW used to manage high-value IT resources of a specific tier are used exclusively for managing high-value IT resources assigned to one and only one tier. If the site has not set aside one or more PAWs for remote management of high-value IT resources assigned to a specific tier, this is a finding. If PAWs used for managing high-value IT resources are used for additional functions, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243446`

### Rule: All high-value IT resources must be assigned to a specific administrative tier to separate highly sensitive resources from less sensitive resources.

**Rule ID:** `SV-243446r722909_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: The Microsoft Tier 0-2 AD administrative tier model (https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#ADATM_BM) is an example. A key security construct of a PAW is to separate high-value IT resources into specific trust levels so that if a device at one trust level is compromised the risk of compromise of more critical IT resources at a different tier is reduced. This architecture protects IT resources in a tier from threats from higher-risk tiers. Isolating administrative accounts by forcing them to operate only within their assigned trust zone implements the concept of containment of security risks and adversaries within a specific zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the site has assigned each high-value IT resource to an administrative tier level by reviewing the site's list of high-value IT resources. In Active Directory verify each high-value IT resource has been assigned to the Organizational Unit (OU) corresponding to the administrative tier the resource is assigned to. If the site has not assigned an administrative tier level to each high-value IT resource or any high-value IT resource is not assigned to the appropriate OU in Active Directory, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243447`

### Rule: The Windows PAW must be configured with a vendor-supported version of Windows 11 and applicable security patches that are DOD approved.

**Rule ID:** `SV-243447r921973_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Older versions of operating systems usually contain vulnerabilities that have been fixed in later released versions. In addition, most operating system patches contain fixes for recently discovered security vulnerabilities. Due to the highly privileged activities of a PAW, it must be maintained at the highest security posture possible and therefore must have one of the current vendor-supported operating system versions installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the current approved versions of Windows 11. Talk to the authorizing official (AO) staff, information system security manager (ISSM), or PAW system administrator to determine the approved versions of Windows 11. Review the configuration of the PAW and determine which version of Windows is installed on the PAW. Verify the installed Windows 11 version is an approved version. If the installed Windows 11 version on the PAW is not the same as an approved version, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243448`

### Rule: A Windows update service must be available to provide software updates for the PAW platform.

**Rule ID:** `SV-243448r722915_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Older versions of operating systems usually contain vulnerabilities that have been fixed in later versions. In addition, most operating system patches contain fixes for recently discovered security vulnerabilities. Due to the highly privileged activities of a PAW, it must be maintained at the highest security posture possible and therefore must have the latest operating system updates installed. Because a PAW is isolated from online operating system update services, a software update service must be available on the intranet to manage operating system and other software updates for site PAWs. A separate software update service is not required at each tier.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an automated software update service is being used at the site to update the operating system of site PAWs. If an automated software update service is not set up and configured to provide updates to site PAWs, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243449`

### Rule: The Windows PAW must be configured so that all non-administrative-related applications and functions are blocked or removed from the PAW platform, including but not limited to email, Internet browsing, and line-of-business applications.

**Rule ID:** `SV-243449r722918_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: The intent of this requirement is that a PAW must not be used for any function not related to the management of high-value IT resources. Note: Authorized exception - It is noted that administrators will need access to non-administrative functions, such as email and the Internet, but a PAW must not be used for these activities. For sites that are constrained in the number of available workstations, an acceptable approach is to install the non-administrative services on a separate virtual machine (VM) on the workstation where the PAW service is installed. The VM will provide acceptable isolation between high-value administrative management accounts and non-administrative services. Note: Relationship between the exception in WPAW-00-000500 and WPAW-00-001000 and requirement WPAW-00-001800: WPAW-00-000500 and WPAW-00-001000 allow an exception to the requirement for sites constrained in the number of available workstations. Lower-tier, high-value admin accounts can operate in a VM if the higher-tier, high-value admin accounts operate in the VM host-OS, but WPAW-00-001800 is more appropriate for a multiple PAW VM environment. A main security architectural construct of a PAW is to remove non-administrative applications and functions from the PAW workstation. Many standard user applications and functions, including email processing, Internet browsing, and using business applications, can increase the security risk to the workstation. These apps and functions are susceptible to many security vulnerabilities, including phishing attacks and embedded malware. This increased risk is not acceptable for the highly privileged activities of a PAW.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: Internet browsing is blocked using the PAW host-based firewall or by configuring a proxy address with a loopback address on the PAW. (See STIG check WPAW-00-002200.) Blocking Internet browsing does not need to be verified in this procedure. Review the services and applications installed on the PAW. Verify there are no email applications/clients and line-of-business applications installed on the PAW. If email applications/clients or line-of-business applications are installed on the PAW, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243450`

### Rule: Device Guard Code Integrity Policy must be used on the Windows PAW to restrict applications that can run on the system (Device Guard Code Integrity Policy).

**Rule ID:** `SV-243450r804960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A main security architectural construct of a PAW is to restrict non-administrative applications and functions from the PAW workstation. Many standard user applications and functions, including email processing, Internet browsing, and using business applications, can increase the security risk to the workstation. These apps and functions are susceptible to many security vulnerabilities, including phishing attacks and embedded malware. This increased risk is not acceptable for the highly privileged activities of a PAW.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is Not Applicable (NA) if the Endpoint Security Solution (ESS) managed system is used on the PAW and application white listing is enforced. Verify Device Guard is enforcing a code integrity policy to restrict authorized applications. Run "PowerShell" with elevated privileges (run as administrator). Enter the following: "Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard | FL *codeintegrity*" If "CodeIntegrityPolicyEnforcementStatus" does not have a value of "2" indicating "Enforced", this is a finding. (For reference: 0 - Not Configured; 1 - Audit; 2 - Enforced) Alternately: - Run "System Information". - Under "System Summary", verify the following: If "Device Guard Code Integrity Policy" does not display "Enforced", this is finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243451`

### Rule: Device Guard Code Integrity Policy must be used on the Windows PAW to restrict applications that can run on the system (Device Guard User Mode Code Integrity).

**Rule ID:** `SV-243451r804962_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A main security architectural construct of a PAW is to restrict non-administrative applications and functions from the PAW workstation. Many standard user applications and functions, including email processing, Internet browsing, and using business applications, can increase the security risk to the workstation. These apps and functions are susceptible to many security vulnerabilities, including phishing attacks and embedded malware. This increased risk is not acceptable for the highly privileged activities of a PAW.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is Not Applicable (NA) if the Endpoint Security Solution (ESS) managed system is used on the PAW and application white listing is enforced. Verify Device Guard is enforcing a code integrity policy to restrict authorized applications. Run "PowerShell" with elevated privileges (run as administrator). Enter the following: "Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard | FL *codeintegrity*" If "UserModeCodeIntegrityPolicyEnforcementStatus" does not have a value of "2" indicating "Enforced", this is a finding. (For reference: 0 - Not Configured; 1 - Audit; 2 - Enforced) Alternately: - Run "System Information". - Under "System Summary", verify the following: If "Device Guard user mode Code Integrity" does not display "Enforced", this is finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243452`

### Rule: Windows PAWs must be restricted to only allow groups used to manage high-value IT resources and members of the local Administrators group to log on locally.

**Rule ID:** `SV-243452r722927_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A main security architectural construct of a PAW is to limit users of the PAW to only administrators of high-value IT resources. This will mitigate some of the risk of attack on administrators of high-value IT resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Allow log on locally" user right, this is a finding: - Administrators - Groups specifically designated to manage high-value IT resources

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243453`

### Rule: The domain must be configured to restrict privileged administrator accounts from logging on to lower-tier hosts.

**Rule ID:** `SV-243453r722930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the domain is not configured to restrict privileged administrator accounts from logging on to lower-tier hosts, it would be impossible to isolate administrative accounts to specific trust zones and protect IT resources from threats from high-risk trust zones. Blocking logon to lower-tier assets helps protect IT resources in a tier from being attacked from a lower tier.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify domain systems are configured to prevent higher-tier administrative accounts from logging on to lower-tier hosts. This can be accomplished by adding the higher-tier administrative groups to the Deny log on user rights of the lower-tier system. These include the following user rights: Deny log on as a batch job Deny log on as a service Deny log on locally If domain systems are not configured to prevent higher-tier administrative accounts from logging on to lower-tier hosts, this is a finding. Domain and Enterprise Admins are currently required to be included in the appropriate deny user rights in the Windows STIGs for member servers and workstations. Note: Severity category exception - Upgrade to a CAT I finding if any Tier 0 administrative account used to manage high-value IT resources is able to log on to a lower-tier host.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-243454`

### Rule: A Windows PAW used to manage domain controllers and directory services must not be used to manage any other type of high-value IT resource.

**Rule ID:** `SV-243454r722933_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Domain controllers (DC) are usually the most sensitive, high-value IT resources in a domain. Dedicating a PAW to be used solely for managing domain controllers will aid in protecting privileged domain accounts from being compromised. For Windows, this includes the management of Active Directory itself and the DCs that run Active Directory, including such activities as domain-level user and computer management, administering trusts, replication, schema changes, site topology, domain-wide group policy, the addition of new DCs, DC software installation, and DC backup and restore operations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If domain controllers and directory services are only managed with local logons to domain controllers, not remotely, this requirement is not applicable. Discuss with the Information System Security Manager (ISSM) or PAW system administrators and review any available site documentation. Verify that a site has designated specific PAWs for the sole purpose of remote management of domain controllers and directory service servers. Review any available site documentation. Verify that any PAW used to manage domain controllers and directory services remotely are used exclusively for managing domain controllers and directory services. If the site has not designated specific PAWs for the sole purpose of remote management of domain controllers and directory service servers, this is a finding. If PAWs used for managing domain controllers and directory services are used for additional functions, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243455`

### Rule: PAWs used to manage Active Directory must only allow groups specifically designated to manage Active Directory, such as Enterprise and Domain Admins and members of the local Administrators group, to log on locally.

**Rule ID:** `SV-243455r722936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PAW platforms are used for highly privileged activities. The accounts that have administrative privileges on domain-level PAW platforms must not be used on or used to manage any non-domain-level PAW platforms. Otherwise, there would be a clear path for privilege escalation to Enterprise Admin (EA)/Domain Admin (DA) privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify on the PAW the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Allow log on locally" user right, this is a finding: - Administrators - Groups specifically designated to manage domain controllers and Active Directory

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-243456`

### Rule: In a Windows PAW, administrator accounts used for maintaining the PAW must be separate from administrative accounts used to manage high-value IT resources.

**Rule ID:** `SV-243456r722939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: PAW accounts used to manage high-value IT resources have privileged rights on managed systems but no administrative or maintenance rights on the PAW. They only have user rights on the PAW. PAW administrative/maintenance accounts only have administrative rights on a PAW and are used only to perform administrative functions on the PAW. PAW administrative/maintenance accounts are the only admin accounts that have admin rights on a PAW. It is not required that PAW administrative/maintenance accounts be organized by tier. The PAW platform should be protected from high-value IT resource administrators accidently or deliberately modifying the security settings of the PAW. Therefore, high-value IT resource administrators must not have the ability to perform maintenance functions on the PAW platform. Separate PAW admin accounts must be set up that only have rights to manage PAW platforms. PAW administrators have the capability to compromise Domain Admin accounts; therefore, personnel assigned as PAW administrators must be the most trusted and experienced administrators within an organization, at least equal to personnel assigned as domain administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify at least one group has been set up in Active Directory (usually Tier 0) for administrators responsible for maintaining PAW workstations (for example, PAW Maintenance group). Verify no administrator account or administrator account group has been assigned to both the group of PAW workstation administrators and any group for administrators of high-value IT resources. If separate PAW administrator groups and administrators of high-value IT resources have not been set up, this is a finding. If a member of any group of PAW maintenance administrators is also a member of any group of administrators of high-value IT resources, this is a finding.

## Group: SRG-OS-000107-GPOS-00054

**Group ID:** `V-243457`

### Rule: The Windows PAW must be configured to enforce two-factor authentication and use Active Directory for authentication management.

**Rule ID:** `SV-243457r819679_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Due to the highly privileged functions of a PAW, a high level of trust must be implemented for access to the PAW, including non-repudiation of the user session. One-factor authentication, including username and password and shared administrator accounts, does not provide adequate assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration on the PAW. Verify group policy is configured to enable either smart card or another DoD-approved two-factor authentication method for site PAWs. - In Active Directory, go to Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options. - Verify "Interactive logon: Require Windows Hello for Business or smart card" is set to "Enabled". If group policy is not configured to enable either smart card or another DoD-approved two-factor authentication method, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243458`

### Rule: The Windows PAW must use a trusted channel for all connections between a PAW and IT resources managed from the PAW.

**Rule ID:** `SV-243458r852043_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Note: The Common Criteria Security Functional Requirement (SFR) FTP_ITC.1.1(1) defines "trusted channel" as "a channel that uses IPsec, SSH, TLS, or TLS/HTTPS to provide a trusted communications channel between itself and authorized IT entity that is logically distinct from other communication channels and provides assured identification of its end points and protection of the channel data from modification or disclosure." The trusted channel uses IPsec, TLS, DTLS, or HTTPS as the protocol that preserves the confidentiality and integrity of PAW communications. The confidentiality and integrity of the communications between the PAW and high-value IT resources being managed from the PAW must be protected due to the highly sensitive nature of the administrative functions being performed. A trusted channel provides the requisite assured identification of its end points and protection of the channel data from modification or disclosure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the PAW workstation, verify IPsec, SSH, TLS, or TLS/HTTPS is configured for all connections between the PAW and managed IT resources on the intranet. Verify the following registry setting: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\FIPSAlgorithmPolicy\ Value Name: Enabled Value Type: REG_DWORD Value: 1 Warning: Clients with this setting enabled will not be able to communicate via digitally encrypted or signed protocols with servers that do not support these algorithms. Both the browser and web server must be configured to use TLS; otherwise, the browser will not be able to connect to a secure site. If on the PAW workstation the registry value for HKEY_LOCAL_MACHINE does not exist or is not configured as specified, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243459`

### Rule: If several Windows PAWs are set up in virtual machines (VMs) on a host server, the host server must only contain PAW VMs.

**Rule ID:** `SV-243459r722948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A main security architectural construct of a PAW is to remove non-administrative functions from the PAW. Many standard user functions, including email processing, Internet browsing, and using business applications, can increase the security risk of the workstation. These apps and functions are susceptible to many security vulnerabilities, including phishing attacks and embedded malware. This increased risk is not acceptable for the highly privileged activities of a PAW. This requirement enforces this security concept in an environment where multiple PAW VMs are installed on a host server. Note: Relationship between the exception in WPAW-00-000500 and WPAW-00-001000 and requirement WPAW-00-001800: WPAW-00-000500 and WPAW-00-001000 allow an exception to the requirement for sites constrained in the number of available workstations. Lower-tier, high-value admin accounts can operate in a VM if the higher-tier, high-value admin accounts operate in the VM host-OS, but WPAW-00-001800 is more appropriate for a multiple PAW VM environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of all host servers where PAW VMs are installed. Verify the only VMs installed on the host server are PAW VMs. If a host server where PAW VMs are installed contains non-PAW VMs, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243460`

### Rule: The Windows PAW must be configured so that all inbound ports and services to a PAW are blocked except as needed for monitoring, scanning, and management tools or when the inbound communication is a response to an outbound connection request.

**Rule ID:** `SV-243460r852046_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A main security architectural construct of a PAW is that the workstation is isolated from most Internet threats, including phishing, impersonation, and credential theft attacks. This isolation is partially implemented by blocking unsolicited inbound traffic to the PAW.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of all ports and services required for site monitoring, scanning, and management tools. Review the configuration setting of the PAW host-based firewall. Verify the firewall is configured to block all inbound ports and services from a PAW except as needed for monitoring, scanning, and management tools or when the inbound communication is a response to an outbound connection request. Note: The exact procedure for verifying the configuration will depend on which host-based firewall (for example, Endpoint Security Solution [ESS]) is used on the PAW. DoD sites should refer to DoD policies and firewall STIGs to determine acceptable firewalls products. If the PAW host-based firewall is not configured to block all inbound ports and services from a PAW except as needed for monitoring, scanning, and management tools or when the inbound communication is a response to an outbound connection request, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243461`

### Rule: The Windows PAW must be configured so that all outbound connections to the Internet from a PAW are blocked.

**Rule ID:** `SV-243461r852049_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: Internal domain connections from a PAW to communicate with IT resources being managed via the PAW with domain controllers or with a digital credential verification service (for example, Online Certificate Status Protocol [OCSP]) are allowed. A main security architectural construct of a PAW is that the workstation is isolated from most internet threats, including phishing, impersonation, and credential theft attacks. This isolation is partially implemented by blocking all outbound connections to the internet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PAW configuration to verify all outbound connections to the internet from the PAW are blocked except to communicate with IT resources being managed via the PAW, including the management console of authorized public cloud services, with domain controllers, or with a digital credential verification service (for example, OCSP). Ask site personnel how outbound connections from the PAW to the internet have been blocked. Two common methods are to either configure the host-based firewall to block all outbound connection requests to the internet gateway or to configure the PAW with an internet proxy address with a loopback address. Based on the method used at the site, review either the configuration of the host-based firewall or the PAW configuration and verify the configuration blocks all outbound internet connections except to communicate with IT resources being managed via the PAW, with domain controllers, or with a digital credential verification service (for example, OCSP). If the site has configured the PAW with a loopback address, verify a proxy server group policy has been set up with a loopback address (127.0.0.1) and assigned to the PAW Users group. If the PAW system has not been configured to block all outbound connections to the internet from a PAW except to communicate with IT resources being managed via the PAW, with domain controllers, or with a digital credential verification service, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243462`

### Rule: The local Administrators group on the Windows PAW must only include groups with accounts specifically designated to administer the PAW.

**Rule ID:** `SV-243462r722957_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A main security architectural construct of a PAW is to restrict access to the PAW from only specific privileged accounts designated for managing the high-value IT resources the PAW has been designated to manage. If unauthorized standard user accounts or unauthorized high-value administrative accounts are able to access a specific PAW, high-value IT resources and critical DoD information could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the PAW is configured to restrict access to privileged accounts specifically designated to administer the PAW: - On the Windows PAW, verify the membership of the local Administrators group. - Verify the only members in the local Administrators group are the group specifically designated for managing the PAW and local administrator(s). If the local Administrators group includes any members not members of the specifically designated group for managing the PAW and local administrator(s), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243463`

### Rule: Local privileged groups (excluding Administrators) on the Windows PAW must be restricted to include no members.

**Rule ID:** `SV-243463r722960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A main security architectural construct of a PAW is to restrict access to the PAW from only specific privileged accounts designated for managing the high-value IT resources the PAW has been designated to manage. If unauthorized standard user accounts or unauthorized high-value administrative accounts are able to access a specific PAW, high-value IT resources and critical DoD information could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify membership of local admin groups on the PAW are empty: On the Windows PAW, verify there are no members in the following local privileged groups (excluding Administrators)*: - Backup Operators (built-in) - Cryptographic Operators - Hyper-V Administrators - Network Configuration Operators - Power Users - Remote Desktop Users - Replicator If the membership of the following admin groups is not empty, this is a finding: Backup Operators (built-in), Cryptographic Operators, Hyper-V Administrators, Network Configuration Operators, Power Users, Remote Desktop Users, and Replicator. *Allowed exception: If a Hyper-V environment is used, the Hyper-V Administrators group may include members.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243464`

### Rule: Restricted remote administration must be enabled for high-value systems.

**Rule ID:** `SV-243464r921975_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricted remote administration features, RestrictedAdmin mode, and Remote Credential Guard for Remote Desktop Protocol (RDP), are an additional safeguard against "pass the hash" attacks, where hackers attempt to gain higher administrative privileges from a single compromised machine. Restricted remote administration protects administrator accounts by ensuring that reusable credentials are not stored in memory on remote devices that could potentially be compromised. When restricted remote administration is implemented, the local RDP service tries to log on to the remote device using a network logon, so the user's credentials are not sent across the network. Therefore, if the high-value IT resource is compromised, the credentials of the administrator connecting to the IT resource from the PAW are not compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the Registry Editor of the remote target system (high-value assets), verify the following registry key has a value of "0": - HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa - Name: DisableRestrictedAdmin - Type: REG_DWORD - Value: 0 If restricted remote administration has not been enabled on the target system, this is a finding. In the Registry Editor of the PAW system, verify the following registry key has a value of "1": HKLM\Software\Policies\Microsoft\Windows\CredentialsDelegation Name: RestrictedRemoteAdministration Type: REG_DWORD Value: 1 If restricted remote administration has not been enabled on the PAW and is not enforced by policy, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-243465`

### Rule: If several PAWs are set up in virtual machines (VMs) on a host server, domain administrative accounts used to manage high-value IT resources must not have access to the VM host operating system (OS) (only domain administrative accounts designated to manage PAWs should be able to access the VM host OS).

**Rule ID:** `SV-243465r722970_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The VM host OS should be protected from high-value IT resource administrators accidently or deliberately modifying the security settings of the host OS. Therefore, high-value IT resource administrators must not have the ability to perform maintenance functions on the VM host OS platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify at least one group has been set up in Active Directory (usually Tier 0) for administrators responsible for maintaining VM host OSs (usually the same as the PAW workstation administrator's group). Verify no administrator account or administrator account group has been assigned to both the group of VM host OS administrators and any group for administrators of high-value IT resources. If separate VM host OS administrator groups and administrators of high-value IT resources have not been set up, this is a finding.

