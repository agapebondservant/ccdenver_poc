# STIG Benchmark: Active Directory Domain Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480

**Group ID:** `V-243466`

### Rule: Membership to the Enterprise Admins group must be restricted to accounts used only to manage the Active Directory Forest.

**Rule ID:** `SV-243466r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Enterprise Admins group is a highly privileged group. Personnel who are system administrators must log on to Active Directory systems only using accounts with the level of authority necessary. Only system administrator accounts used exclusively to manage the Active Directory Forest may be members of the Enterprise Admins group. A separation of administrator responsibilities helps mitigate the risk of privilege escalation resulting from credential theft attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Enterprise Admins group in Active Directory Users and Computers. Any accounts that are members of the Enterprise Admins group must be documented with the IAO. Each Enterprise Administrator must have a separate unique account specifically for managing the Active Directory forest. If any account listed in the Enterprise Admins group is a member of other administrator groups including the Domain Admins group, domain member server administrators groups, or domain workstation administrators groups, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243467`

### Rule: Membership to the Domain Admins group must be restricted to accounts used only to manage the Active Directory domain and domain controllers.

**Rule ID:** `SV-243467r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Domain Admins group is a highly privileged group. Personnel who are system administrators must log on to Active Directory systems only using accounts with the level of authority necessary. Only system administrator accounts used exclusively to manage an Active Directory domain and domain controllers may be members of the Domain Admins group. A separation of administrator responsibilities helps mitigate the risk of privilege escalation resulting from credential theft attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Domain Admins group in Active Directory Users and Computers. Any accounts that are members of the Domain Admins group must be documented with the IAO. Each Domain Administrator must have a separate unique account specifically for managing the Active Directory domain and domain controllers. If any account listed in the Domain Admins group is a member of other administrator groups including the Enterprise Admins group, domain member server administrators groups, or domain workstation administrators groups, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243468`

### Rule: Administrators must have separate accounts specifically for managing domain member servers.

**Rule ID:** `SV-243468r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Personnel who are system administrators must log on to domain systems only using accounts with the minimum level of authority necessary. Only system administrator accounts used exclusively to manage domain member servers may be members of an administrator group for domain member servers. A separation of administrator responsibilities helps mitigate the risk of privilege escalation resulting from credential theft attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the membership groups in Active Directory Users and Computers. Membership groups must be designated at the domain level specifically for domain member server administrators. Domain member server administrator groups and any accounts that are members of the groups must be documented with the IAO. Each member server administrator must have a separate unique account specifically for managing member servers. If any account listed in a domain member server administrator group is a member of other administrator groups including the Enterprise Admins group, the Domain Admins group, or domain workstation administrator groups, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243469`

### Rule: Administrators must have separate accounts specifically for managing domain workstations.

**Rule ID:** `SV-243469r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Personnel who are system administrators must log on to domain systems only using accounts with the minimum level of authority necessary. Only system administrator accounts used exclusively to manage domain workstations may be members of an administrators group for domain workstations. A separation of administrator responsibilities helps mitigate the risk of privilege escalation resulting from credential theft attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the membership groups in Active Directory Users and Computers. Membership groups must be designated at the domain level specifically for domain workstation administrators. Domain workstation administrator groups and any accounts that are members of the groups must be documented with the IAO. Each domain workstation administrator must have a separate unique account specifically for managing domain workstations. If any account listed in a domain workstation administrator group is a member of other administrator groups including the Enterprise Admins group, the Domain Admins group, or domain member server administrator groups, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243470`

### Rule: Delegation of privileged accounts must be prohibited.

**Rule ID:** `SV-243470r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Privileged accounts such as those belonging to any of the administrator groups must not be trusted for delegation. Allowing privileged accounts to be trusted for delegation provides a means for privilege escalation from a compromised system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the properties of all privileged accounts in Active Directory Users and Computers. Under the Account tab, verify "Account is sensitive and cannot be delegated" is selected in the Account Options section. If delegation is not prohibited for any privileged account, this is a finding.

## Group: SRG-OS-000112

**Group ID:** `V-243471`

### Rule: Local administrator accounts on domain systems must not share the same password.

**Rule ID:** `SV-243471r958494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local administrator accounts on domain systems must use unique passwords. In the event a domain system is compromised, sharing the same password for local administrator accounts on domain systems will allow an attacker to move laterally and compromise multiple domain systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify local administrator accounts on domain systems are using unique passwords. If local administrator accounts on domain systems are sharing a password, this is a finding. It is highly recommended to use Microsoft's Local Administrator Password Solution (LAPS), which provides an automated solution for maintaining and regularly changing a local administrator password for domain-joined systems. LAPS can manage a single local administrator account. The default is the built-in administrator account; however, it can be configured to manage an administrator account of a different name. If additional local administrator accounts exist across systems, the organization must have a process to require unique passwords on each system for the additional accounts. The AO may approve other automated solutions that provide this capability. If LAPS has been installed and enabled in the domain, the following PowerShell query will return a list of systems that do not have a local administrator password managed by LAPS. (The LAPS PowerShell module requires PowerShell 2.0 or higher and .NET Framework 4.0.) Open "Windows PowerShell". If the LAPS PowerShell module has not been previously imported, execute the following first: "Import-Module AdmPwd.ps". Execute "Get-AdmPwdPassword -ComputerName * | Where-object {$_.password -eq $null}" Review the returned list for validity. Exclude computers with "OU=Domain Controllers" in the DistinguishedName field. Other possible exceptions include but are not limited to non-Windows computers in Active Directory. If any active/deployed Windows systems that are not managed by another process to ensure unique passwords for local administrator accounts are listed, this is a finding. If the query fails, the organization must demonstrate that passwords for local administrator accounts are properly managed to ensure unique passwords for each. If not, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243472`

### Rule: Separate smart cards must be used for Enterprise Admin (EA) and Domain Admin (DA) accounts from smart cards used for other accounts.

**Rule ID:** `SV-243472r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A separate smart card for Enterprise Admin and Domain Admin accounts eliminates the automatic exposure of the private keys for the EA/DA accounts to less secure user platforms when the other accounts are used. Having different certificates on one card does not provide the necessary separation. The same smart card may be used by an administrator for both EA and DA accounts. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify separate smart cards are used for EA and DA accounts from smart cards used for other accounts. EA and DA accounts may be on the same smart card but must be separate from any other accounts. If separate smart cards for EA and DA accounts from other accounts are not used, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243473`

### Rule: Separate domain accounts must be used to manage public facing servers from any domain accounts used to manage internal servers.

**Rule ID:** `SV-243473r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Public facing servers should be in DMZs with separate Active Directory forests. If, because of operational necessity, this is not possible, lateral movement from these servers must be mitigated within the forest. Having different domain accounts for administering domain joined public facing servers, from domain accounts used on internal servers, protects against an attacker's lateral movement from a compromised public facing server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the domain does not have any public facing servers, this is NA. Review the local Administrators group on public facing servers. Only the appropriate administrator groups or accounts responsible for administration of the system may be members of the group. For public facing servers, the Domain Admins group must be replaced by a domain member server administrator group whose members are different from any used to manage internal servers. If any domain accounts or groups used to manage internal servers are members of the local administrators group, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243475`

### Rule: Domain controllers must be blocked from Internet access.

**Rule ID:** `SV-243475r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Domain controllers provide access to highly privileged areas of a domain. Such systems with Internet access may be exposed to numerous attacks and compromise the domain. Restricting Internet access for domain controllers will aid in protecting these privileged areas from being compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify domain controllers are blocked from Internet access. Various methods may be employed to accomplish this, such as restrictions at boundary firewalls, through proxy services, host based firewalls or IPsec. Review the Internet access restrictions with the administrator. If Internet access is not prevented, this is a finding. If a critical function requires Internet access, this must be documented and approved by the organization.

## Group: SRG-OS-000076

**Group ID:** `V-243476`

### Rule: All accounts, privileged and unprivileged, that require smart cards must have the underlying NT hash rotated at least every 60 days.

**Rule ID:** `SV-243476r1026173_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a smart card is required for a domain account, a long password, unknown to the user, is generated. This password and associated NT hash are not changed as are accounts with passwords controlled by the maximum password age. Disabling and reenabling the "Smart card is required for interactive logon" (SCRIL) replaces the NT hash of the account with a newly randomized hash. Otherwise, the existing NT hash could be reused for Pass-the-Hash in the future. Windows Server 2016 includes a built-in feature for SCRIL hash rolling that will automatically reset NT hashes in accordance with the existing maximum password age policy. This requires the domain functional level to be Windows Server 2016. In Active Directory with a domain functional level below Windows Server 2016, scripts can be used to reset the NT hashes of all domain accounts. Associated documentation should be reviewed for potential issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Windows Server 2016 with a domain functional level of Windows Server 2016: Open "Active Directory Administrative Center". Right-click on the domain name and select "Properties". If the "Domain functional level:" is not "Windows Server 2016", another method must be used to reset the NT hashes. See below for other options. If the "Domain functional level:" is "Windows Server 2016" and "Enable rolling of expiring NTLM secrets during sign on, for users who are required to use Microsoft Passport or smart card for interactive sign on" is not checked, this is a finding. Active Directory domains with a domain functional level below Windows Server 2016: Verify the organization rotates the NT hash for smart card-enforced accounts every 60 days. This can be accomplished with the use of scripts. DOD PKI-PKE has provided a script under PKI and PKE Tools at https://cyber.mil/pki-pke/tools-configuration-files/. Refer to the User Guide for additional information. NSA has also provided a PowerShell script with Pass-the-Hash guidance at https://github.com/nsacyber/Pass-the-Hash-Guidance. Running the "Invoke-SmartcardHashRefresh" cmdlet in the "PtHTools" module will trigger a change of the underlying NT hash. Refer to the site for additional information. Manually rolling the NT hash requires disabling and reenabling the "Smart Card required for interactive logon" option for each smart card-enforced account, which is not practical for large groups of users. If NT hashes for smart card-enforced accounts are not rotated every 60 days, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243477`

### Rule: User accounts with domain level administrative privileges must be members of the Protected Users group in domains with a domain functional level of Windows 2012 R2 or higher.

**Rule ID:** `SV-243477r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User accounts with domain level administrative privileges are highly prized in Pass-the-Hash/credential theft attacks. The Protected Users group provides extra protections to accounts such as preventing authentication using NTLM. These accounts include Enterprise and Domain Admins as well as other accounts that may have domain level privileges. The Protected Users group requires a domain functional level of at least Windows 2012 R2 to provide domain level protections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the domain functional level is not at least Windows 2012 R2, this is NA. Open "Windows PowerShell". Enter "Get-ADDomain | FL DomainMode" to determine the domain functional level. Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Compare membership of the Protected Users group to membership of the following groups. By default, the groups are under the node referenced; however, it is possible to move those under "Users" to another location. Enterprise Admins (Users node) Domain Admins (Users node) Schema Admins (Users node) Administrators (Builtin node) Account Operators (Builtin node) Backup Operators (Builtin node) It is recommended that one account be excluded to ensure availability if there are issues with Kerberos. Excluding the account left out for availability, if all user accounts from the local domain that are members of the domain level groups above are not also members of the Protected Users group, this is a finding. (User accounts is referring to accounts for personnel, not service accounts.)

## Group: SRG-OS-000480

**Group ID:** `V-243478`

### Rule: Domain-joined systems (excluding domain controllers) must not be configured for unconstrained delegation.

**Rule ID:** `SV-243478r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unconstrained delegation enabled on a computer can allow the computer account to be impersonated without limitation. If delegation is required, it must be limited/constrained to the specific services and accounts required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Windows PowerShell" on a domain controller. Enter "Get-ADComputer -Filter {(TrustedForDelegation -eq $True) -and (PrimaryGroupID -eq 515)} -Properties TrustedForDelegation, TrustedToAuthForDelegation, ServicePrincipalName, Description, PrimaryGroupID". If any computers are returned, this is a finding. (TrustedForDelegation equaling True indicates unconstrained delegation.) PrimaryGroupID 515 = Domain computers (excludes DCs) TrustedForDelegation = Unconstrained Delegation TrustedToAuthForDelegation = Constrained delegation ServicePrincipalName = Service Names Description = Computer Description

## Group: SRG-OS-000480

**Group ID:** `V-243479`

### Rule: The Directory Service Restore Mode (DSRM) password must be changed at least annually. 

**Rule ID:** `SV-243479r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Directory Service Restore Mode (DSRM) password, used to log on to a domain controller (DC) when rebooting into the server recovery mode, is very powerful. With a weak or known password, someone with local access to the DC can reboot the server and copy or modify the Active Directory database without leaving any trace of the activity. Failure to change the DSRM password periodically could allow compromised of the Active Directory. It could also allow an unknown (lost) password to go undetected. If not corrected during a periodic review, the problem might surface during an actual recovery operation and delay or prevent the recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the organization has a process that addresses DSRM password change frequency. If DSRM passwords are not changed at least annually, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243480`

### Rule: The domain functional level must be at a Windows Server version still supported by Microsoft.

**Rule ID:** `SV-243480r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Domains operating at functional levels below Windows Server versions no longer supported by Microsoft reduce the level of security in the domain and forest as advanced features of the directory are not available. This also prevents the addition of domain controllers to the domain using Windows Server versions prior to the current domain functional level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Active Directory Domains and Trusts" (run "domain.msc") or "Active Directory Users and Computers" (run "dsa.msc"). Right-click in the left pane on the name of the Domain being reviewed. Select "Raise domain functional level..." The current domain functional level will be displayed (as well as the option to raise the domain functional level). Select "Cancel" to exit. Alternately, using PowerShell (Windows Server 2016): Select "Active Directory Module for Windows PowerShell", available in Administrative Tools or the Start Screen. Run "Get-ADDomain". View the value for "DomainMode:" If the domain functional level is not Windows Server 2016, this is a finding. Using the highest domain functional level supported by the domain controllers is recommended.

## Group: SRG-OS-000480

**Group ID:** `V-243481`

### Rule: Access to need-to-know information must be restricted to an authorized community of interest.

**Rule ID:** `SV-243481r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Because trust relationships effectively eliminate a level of authentication in the trusting domain or forest, they represent less stringent access control at the domain or forest level in which the resource resides. To mitigate this risk, trust relationships must be documented so that they can be readily verified during periodic inspections designed to validate only approved trusts are configured in AD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Before performing this check, perform V-243494, which validates the trusts within the documentation are current within AD. 2. Obtain documentation of the site's approved trusts from the site representative. 3. For each of the identified trusts, verify the documentation includes a justification or explanation of the need-to-know basis of the trust. 4. If the need for the trust is not documented, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243482`

### Rule: Interconnections between DoD directory services of different classification levels must use a cross-domain solution that is approved for use with inter-classification trusts.

**Rule ID:** `SV-243482r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If a robust cross-domain solution is not used, then it could permit unauthorized access to classified data. To support secure access between resources of different classification levels, the solution must meet discretionary access control requirements. There are currently, no DOD- approved solutions. Further Policy Details: Do not define trust relationships between domains, forests, or realms with resources at different classification levels. The configuration of a trust relationship is one of the steps used to allow users in one AD domain to access resources in another domain, forest, or Kerberos realm. (This check does not apply to trusts with non-DoD organizations since these trusts are examined in a previous check.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Refer to the list of identified trusts and the trust documentation provided by the site representative. (Obtained in V-8530) 2. For each of the identified trusts between DoD organizations, compare the classification level (unclassified, confidential, secret, and top secret) of the domain being reviewed with the classification level of the other trust party as noted in the documentation. 3. If the classification level of the domain being reviewed is different than the classification level of any of the entities for which a trust relationship is defined, then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243483`

### Rule: A controlled interface must have interconnections among DoD information systems operating between DoD and non-DoD systems or networks.

**Rule ID:** `SV-243483r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The configuration of an AD trust relationship is one of the steps used to allow users in one domain to access resources in another domain, forest, or Kerberos realm. When a trust is defined between a DoD organization and a non-DoD organization, the security posture of the two organizations might be significantly different. If the non-DoD organization maintained a less secure environment and that environment were compromised, the presence of the AD trust might allow the DoD environment to be compromised also.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Refer to the list of identified trusts obtained in a previous check (V8530). 2. For each of the identified trusts, determine if the other trust party is a non-DoD entity. For example, if the fully qualified domain name of the other party does not end in ".mil", the other party is probably not a DoD entity. 3. Review the local documentation approving the external network connection and documentation indicating explicit approval of the trust by the DAA. 4. The external network connection documentation is maintained by the IAO\NSO for compliance with the Network Infrastructure STIG. 5. If any trust is defined with a non-DoD system and there is no documentation indicating approval of the external network connection and explicit DAA approval of the trust, then this is a finding.

## Group: SRG-OS-000104

**Group ID:** `V-243484`

### Rule: Security identifiers (SIDs) must be configured to use only authentication data of directly trusted external or forest trust. 

**Rule ID:** `SV-243484r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances it is possible for attackers or rogue administrators that have compromised a domain controller in a trusted domain to use the SID history attribute (sIDHistory) to associate SIDs with new user accounts, granting themselves unauthorized rights. To help prevent this type of attack, SID filter quarantining is enabled by default on all external trusts. However, it is possible for an administrator to change this setting or the trust may have been created in an older version of AD. SID filtering causes SID references that do not refer to the directly trusted domain or forest to be removed from inbound access requests in the trusting domain. Without SID filtering, access requests could contain spoofed SIDs, permitting unauthorized access. In cases where access depends on SID history or Universal Groups, failure to enable SID filtering could result in operational problems, including denial of access to authorized users. When the quarantine switch is applied to external or forest trusts, only those SIDs from the single, directly trusted domain are valid. In effect, enabling /quarantine on a trust relationship will break the transitivity of that trust so that only the specific domains on either side of the trust are considered participants in the trust.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Active Directory Domains and Trusts". (Available from various menus or run "domain.msc".) Right-click the domain in the left pane and select "Properties". Select the "Trusts" tab. Note any existing trusts and the type. If no trusts exist, this is NA. Access a command line and run the following command on the trusting domain: "netdom trust <trusting domain> /d:<trusted domain> /quarantine" If the result does not specify the following, this is a finding. "SID filtering is enabled for this trust. Only SIDs from the trusted domain will be accepted for authorization data returned during authentication. SIDs from other domains will be removed." If the trust type is Forest, run the following command on the trusting domain: "netdom trust <trusting domain> /d:<trusted domain> /enablesidhistory" If the result does not specify "SID history is disabled for this trust", this is a finding.

## Group: SRG-OS-000080

**Group ID:** `V-243485`

### Rule: Selective Authentication must be enabled on outgoing forest trusts.

**Rule ID:** `SV-243485r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling Selective Authentication on outbound Active Directory (AD) forest trusts significantly strengthens access control by requiring explicit authorization (through the Allowed to Authenticate permission) on resources in the trusting forest. When Selective Authentication is not enabled, less secure resource access permissions (such as those that specify Authenticated Users) might permit unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Active Directory Domains and Trusts". (Available from various menus or run "domain.msc".) Right click the domain name in the left pane and select "Properties". Select the "Trusts" tab. For each outgoing forest trust, right-click the trust item and select "Properties". Select the "Authentication" tab. If the "Selective Authentication" option is not selected on every outgoing forest trust, this is a finding.

## Group: SRG-OS-000121

**Group ID:** `V-243486`

### Rule: The Anonymous Logon and Everyone groups must not be members of the Pre-Windows 2000 Compatible Access group.

**Rule ID:** `SV-243486r958504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Pre-Windows 2000 Compatible Access group was created to allow Windows NT domains to interoperate with AD domains by allowing unauthenticated access to certain AD data. The default permissions on many AD objects are set to allow access to the Pre-Windows 2000 Compatible Access group. When the Anonymous Logon or Everyone groups are members of the Pre-Windows 2000 Compatible Access group, anonymous access to many AD objects is enabled. Anonymous access to AD data could provide valuable account or configuration information to an intruder trying to determine the most effective attack strategies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Expand the domain being reviewed in the left pane and select the "Builtin" container. Double-click on the "Pre-Windows 2000 Compatible Access" group in the right pane. Select the "Members" tab. If the "Anonymous Logon" or "Everyone" groups are members, this is a finding. (By default, these groups are not included in current Windows versions.)

## Group: SRG-OS-000480

**Group ID:** `V-243487`

### Rule: Membership in the Group Policy Creator Owners and Incoming Forest Trust Builders groups must be limited.

**Rule ID:** `SV-243487r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Membership in the Group Policy Creator Owners and Incoming Forest Trust Builders groups assigns a high privilege level for AD functions. Unnecessary membership increases the risk from compromise or unintended updates. Members of these groups must specifically require those privileges and be documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Start "Active Directory Users and Computers" (Available from various menus or run "dsa.msc"). Review the membership of the "Incoming Forest Trust Builders" group. Navigate to the "Built-in" container. Right-click on the "Incoming Forest Trust Builders", select "Properties" and then the "Members" tab. If any accounts are not documented as necessary with the ISSO, this is a finding. Review the membership of the "Group Policy Creator Owner" group. Navigate to the "Users" container. Right-click on the "Group Policy Creator Owner", select "Properties" and then the "Members" tab. If any accounts are not documented as necessary with the ISSO, this is a finding. It is possible to move some system-defined groups from their default locations. If a group is not in the location noted, review other containers to locate.

## Group: SRG-OS-000480

**Group ID:** `V-243488`

### Rule: User accounts with delegated authority must be removed from Windows built-in administrative groups or remove the delegated authority from the accounts.

**Rule ID:** `SV-243488r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In AD it is possible to delegate account and other AD object ownership and administration tasks. (This is commonly done for help desk or other user support staff.) This is done to avoid the need to assign users to Windows groups with more widely ranging privileges. If a user with delegated authority to user accounts in a specific OU is also a member of the Administrators group, that user has the ability to reconfigure a wide range of domain security settings and change user accounts outside of the OU to which s/he is a delegated authority. A lack of specific baseline documentation of accounts with delegated privileges makes it impossible to determine if the configured privileges are consistent with the intended security policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Interview the IAM or site representative and obtain the list of accounts that have been delegated AD object ownership or update permissions and that are not members of Windows built-in administrative groups. (This includes accounts for help desk or support personnel who are not Administrators, but have authority in AD to maintain user accounts or printers.) 2. If accounts with delegated authority are defined and there is no list, then this is a finding. 3. Count the number of accounts on the list. 4. If the number of accounts with delegated authority is greater than 10, review the site documentation that justifies this number. Validate that the IAM explicitly acknowledges the need to have a high number of privileged users. 5. If the number of accounts with delegated authority is greater than 10 and there is no statement in the documentation that justifies the number, then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243489`

### Rule: Read-only Domain Controller (RODC) architecture and configuration must comply with directory services requirements.

**Rule ID:** `SV-243489r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The RODC role provides a unidirectional replication method for selected information from your internal network to the DMZ. If not properly configured so that the risk footprint is minimized, the interal domain controller or forest can be compromised. RODC is considered part of the site's Forest or Domain installation since it is not a standalone product, but rather a role of the the Windows AD DS full installation or Server Core installation. It is possible to have Windows 2003 clients authenticated using RODC, however, compatibility packs are needed. Note that RODC is not authorized for use across the site's perimeter firewall.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify that the site has applied the Network Infrastucture STIG to configure the VPN and IPSec. 2. Verify that IPSec and other communications and security configurations for the management and replication of the RODC will be managed by use of the minimum required Group Policy Objects (GPOs). 3. Include an inspection of the RODC server in the DMZ when inspection for least privilege. 4. Verify that required patches and compatibility packs are installed if RODC is used with Windows 2003 (or earlier) clients. 5. If RODC server and configuration does not comply with requirements, then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243490`

### Rule: Usage of administrative accounts must be monitored for suspicious and anomalous activity.

**Rule ID:** `SV-243490r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Monitoring the usage of administrative accounts can alert on suspicious behavior and anomalous account usage that would be indicative of potential malicious credential reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify account usage events for administrative accounts are being monitored. This includes events related to approved administrative accounts as well as accounts being added to privileged groups such as Administrators, Domain and Enterprise Admins and other organization defined administrative groups. Event monitoring may be implemented through various methods including log aggregation and the use of monitoring tools. Monitor for the events listed below, at minimum. If these events are not monitored, this is a finding. Account Lockouts (Subcategory: User Account Management) 4740 - A user account is locked out. User Added to Privileged Group (Subcategory: Security Group Management) 4728 - A member was added to a security-enabled global group. 4732 - A member was added to a security-enabled local group. 4756 - A member was added to a security-enabled universal group. Successful User Account Login (Subcategory: Logon) 4624 - An account was successfully logged on. Failed User Account Login (Subcategory: Logon) 4625 - An account failed to log on. Account Login with Explicit Credentials (Subcategory: Logon) 4648 - A logon was attempted using explicit credentials.

## Group: SRG-OS-000480

**Group ID:** `V-243491`

### Rule: Systems must be monitored for attempts to use local accounts to log on remotely from other systems.

**Rule ID:** `SV-243491r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Monitoring for the use of local accounts to log on remotely from other systems may indicate attempted lateral movement in a Pass-the-Hash attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify attempts to use local accounts to log on remotely from other systems are being monitored. Event monitoring may be implemented through various methods including log aggregation and the use of monitoring tools. Monitor for the events listed below. If these events are not monitored, this is a finding. More advanced filtering is necessary to obtain the pertinent information than just looking for event IDs. Search for the event IDs listed with the following additional attributes: Logon Type = 3 (Network) Authentication Package Name = NTLM Not a domain logon and not the ANONYMOUS LOGON account Successful User Account Login (Subcategory: Logon) 4624 - An account was successfully logged on. Failed User Account Login (Subcategory: Logon) 4625 - An account failed to log on.

## Group: SRG-OS-000480

**Group ID:** `V-243492`

### Rule: Systems must be monitored for remote desktop logons.

**Rule ID:** `SV-243492r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote Desktop activity for administration should be limited to specific administrators, and from limited management workstations. Monitoring for any Remote Desktop logins outside of expected activity can alert on suspicious behavior and anomalous account usage that could be indicative of potential malicious credential reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Remote Desktop logins are being monitored. Event monitoring may be implemented through various methods including log aggregation and the use of monitoring tools. Monitor for the events listed below. If these events are not monitored, this is a finding. More advanced filtering is necessary to obtain the pertinent information than just looking for event IDs. Search for the event IDs listed with the following additional attributes: Logon Type = 10 (RemoteInteractive) Authentication Package Name = Negotiate Successful User Account Login (Subcategory: Logon) 4624 - An account was successfully logged on.

## Group: SRG-OS-000480

**Group ID:** `V-243493`

### Rule: Active Directory data must be backed up daily for systems with a Risk Management Framework categorization for Availability of moderate or high.  Systems with a categorization of low must be backed up weekly.

**Rule ID:** `SV-243493r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to maintain a current backup of directory data could make it difficult or impossible to recover from incidents including hardware failure or malicious corruption. A failure to recover from the loss of directory data used in identification and authentication services (i.e., Active Directory) could result in an extended loss of availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the organization's procedures for the backing up active directory data. Verify the frequency at which active directory data is backed up. If the Availability categorization of the domain is low, this must be at least weekly. If the Availability categorization of the domain is moderate or high, this must be at least daily. Verify the type of backup is appropriate to capturing the directory data. For AD domain controllers, this must include a System State data backup. If any of these conditions are not met, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243494`

### Rule: Each cross-directory authentication configuration must be documented.

**Rule ID:** `SV-243494r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Active Directory (AD) external, forest, and realm trust configurations are designed to extend resource access to a wider range of users (those in other directories). If specific baseline documentation of authorized AD external, forest, and realm trust configurations is not maintained, it is impossible to determine if the configurations are consistent with the intended security policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Start "Active Directory Domains and Trusts" (Available from various menus or run "domain.msc"). Select the left pane item that matches the name of the domain being reviewed. Right-click the domain name and select "Properties". Select the "Trusts" tab. For each outbound and inbound external, forest, and realm trust, record the name of the other party (domain name), the trust type, transitivity, and the trust direction. (Keep this trust information for use in subsequent checks.) Compare the list of trusts identified with documentation maintained by the ISSO. For each trust, the documentation must contain the following: Type (external, forest, or realm) Name of the other party Confidentiality, Availability, and Integrity categorization Classification level of the other party Trust direction (inbound and/or outbound) Transitivity Status of the Selective Authentication option Status of the SID filtering option If an identified trust is not listed in the documentation or if any of the required items are not documented, this is a finding.

## Group: SRG-OS-000423

**Group ID:** `V-243495`

### Rule: A VPN must be used to protect directory network traffic for directory service implementation spanning enclave boundaries.

**Rule ID:** `SV-243495r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The normal operation of AD requires the use of IP network ports and protocols to support queries, replication, user authentication, and resource authorization services. At a minimum, LDAP or LDAPS is usually required for communication with every domain controller. DoD Ports, Protocols, and Services Management (PPSM) policy restricts the use of LDAP, LDAPS, and many of the AD-related protocols across enclave boundaries because vulnerabilities exist in the protocols or service implementations. To comply with the restrictions and address the vulnerabilities, a VPN implementation may be used. If AD data traverses enclave network boundaries using a vulnerable protocol or service without the protection provided by a VPN, that data might be subject to tampering or interception. Further Policy Details: Implement a VPN or other network protection solution in accordance with the Network Infrastructure STIG that protects AD data in transit across DoD enclave boundaries. VPN requirements will include registering the VPN and connection points with the PPSM. Current guidance is available in the Network Infrastructure STIG and from the PPSM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Review the site's network diagram(s) to determine if domain controllers for the domain are located in multiple enclaves. The object is to determine if network traffic is traversing enclave network boundaries. 2. Request information about RODC or ADAM instances are installed. In particular, request details of Active Diretory functionality installed or extended into the DMZ or configured/allowed to cross the sites outbound firewall boundary. Ensure communications and replication traffic is encrypted. 3. If domain controllers are not located in multiple enclaves, then this check is not applicable. 4. If domain controllers are located in multiple enclaves, verify that a VPN is used to transport the network traffic (replication, user logon, queries, etc.). 5. If a VPN solution is not used to transport directory network traffic across enclave boundaries, then this is a finding. 6. If the ADAM mode is in use and a migration plan for converting to RODC is not in place, then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243496`

### Rule: Accounts from outside directories that are not part of the same organization or are not subject to the same security policies must be removed from all highly privileged groups. 

**Rule ID:** `SV-243496r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Membership in certain default directory groups assigns a high privilege level for access to the directory. In AD, membership in the following groups enables high privileges relative to AD and the Windows OS: Domain Admins, Enterprise Admins, Schema Admins, Group Policy Creator Owners, and Incoming Forest Trust Builders. When accounts from an outside directory are members of highly privileged groups in the directory being reviewed, less rigorous security policies or compromises of accounts in the outside directory could increase the risk to the directory where the privileged groups are defined. A compromise to the outside directory would allow unauthorized, privileged access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Start the Active Directory Users and Computers console (Start, Run, "dsa.msc"). 2. Select and expand the left pane item that matches the name of the domain being reviewed. 3. Select the Built-in container. a. If the Incoming Forest Trust Builders group is defined, double-click on the group, and select the Members tab b. Examine the defined accounts to see if they are from a domain that is not in the forest being reviewed. 4. Select the Users container a. For each group (Domain Admins, Enterprise Admins, Schema Admins, and Group Policy Creator Owners), double-click on the group, and select the Members tab. b. Examine the defined accounts to see if they are from a domain that is not in the forest being reviewed. 5. If any account in a privileged group is from a domain outside the forest being reviewed and that outside forest is not maintained by the same organization (e.g., enclave) or subject to the same security policies, then this is a finding. Supplementary Notes: Note: An account that is from an outside domain appears in the format "outside-domain-NetBIOSname\account" or "account@outside-domain-fully-qualified-name". Examples are "AOFN21\jsmit" or "jsmith@AOFN21.OST.COM". It may be necessary to use the AD Domains and Trusts (domain.msc) console to determine if the domain is from another AD forest. Note: It is possible to move the highly privileged AD security groups out of the AD Users container. If the Domain Admins, Enterprise Admins, Schema Admins, or Group Policy Creator Owners groups are not in the AD Users container, ask the SA for the new location and use that location for this check.

## Group: SRG-OS-000480

**Group ID:** `V-243497`

### Rule: Inter-site replication must be enabled and configured to occur at least daily.

**Rule ID:** `SV-243497r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Timely replication makes certain that directory service data is consistent across all servers that support the same scope of data for their clients. In AD implementation using AD Sites, domain controllers defined to be in different AD Sites require Site links to specify properties for replication scheduling. If AD Site link schedule and replication interval properties are configured improperly, AD data replication may not occur frequently enough and updates to identification, authentication, or authorization data may not be current on all domain controllers. If this data is not current, access to resources may be incorrectly granted or denied. The default for inter-site replication is to occur every 180 minutes, 24 hours a day.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Active Directory Sites and Services". (Available from various menus or run "dssite.msc".) Expand "Sites" in the left pane. If only a single site exists, this is NA. By default the first site in a domain is named "Default-First-Site-Name" but may have been changed. If more than one site exists, expand "Inter-Site Transports" and select "IP". For each site link that is defined in the right pane perform the following: Right click the site link item and select "Properties". If the interval on the "General" tab for the "Replicate every" field is greater than "1440", this is a finding. Click the "Change Schedule" button. If the time frames selected for "Replication Available" do not allow for replication to occur at least daily, this is a finding. Click the Cancel buttons to exit.

## Group: SRG-OS-000032

**Group ID:** `V-243498`

### Rule: If a VPN is used in the AD implementation, the traffic must be inspected by the network Intrusion detection system (IDS).

**Rule ID:** `SV-243498r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To provide data confidentiality, a VPN is configured to encrypt the data being transported. While this protects the data, some implementations do not allow that data to be processed through an intrusion detection system (IDS) that could detect data from a compromised system or malicious client. Further policy details:Replace the VPN solution or reconfigure it so that directory data is processed by a network or host-based intrusion detection system (IDS). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Interview the site representative. Ask about the location of the domain controllers. 2. If domain controllers are not located in multiple enclaves, then this check is not applicable. 3. If domain controllers are located in multiple enclaves and a VPN is not used, then this check is not applicable. 4. If domain controllers are located in multiple enclaves and a VPN is used, review the site network diagram(s) with the SA, NSO, or network reviewer as required to determine if the AD network traffic is visible to a network or host IDS. 5. If the AD network traffic is not visible to a network or host IDS, then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243499`

### Rule: Active Directory implementation information must be added to the organization contingency plan where the Risk Management Framework categorization for Availability is moderate or high.

**Rule ID:** `SV-243499r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When an incident occurs that requires multiple Active Directory (AD) domain controllers to be rebuilt, it is critical to understand the AD hierarchy and replication flow so that the correct recovery sequence and configuration values can be selected. Without appropriate AD forest, tree and domain structural documentation, it may be impossible or very time consuming to reconstruct the original configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the Availability categorization information for the domain. If the Availability categorization of the domain is low, this is NA. If the Availability categorization of the domain is moderate or high, verify the organization's disaster recovery plans includes documentation on the AD hierarchy (forest, tree and domain structure). (A chart showing forest hierarchy and domain names is the minimum suggested.) If the disaster recovery plans do not include directory hierarchy information, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243500`

### Rule: Active Directory must be supported by multiple domain controllers where the Risk Management Framework categorization for Availability is moderate or high.

**Rule ID:** `SV-243500r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In Active Directory (AD) architecture, multiple domain controllers provide availability through redundancy. If an AD domain or servers within it have an Availability categorization of medium or high and the domain is supported by only a single domain controller, an outage of that machine can prevent users from accessing resources on servers in that domain and in other AD domains.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the Availability categorization information for the domain. If the Availability categorization of the domain is low, this is NA. If the Availability categorization of the domain is moderate or high, verify the domain is supported by more than one domain controller. Start "Active Directory Users and Computers" (Available from various menus or run "dsa.msc"). Expand the left pane item that matches the domain being reviewed. Select the Domain Controllers Organizational Unit (OU) in the left pane. If there is only one domain controller in the OU, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-243501`

### Rule: The impact of CPCON changes on the cross-directory authentication configuration must be considered and procedures documented.

**Rule ID:** `SV-243501r1016334_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When incidents occur that require a change in the Cyber Protection Conditions (CPCON) with the release of USSCI 5200-13 status, it may be necessary to take action to restrict or disable certain types of access based on a directory outside the Component's control. Cross-directory configurations (such as trusts and pass-through authentication) are specifically designed to enable resource access across directories. If conditions indicate an outside directory is at increased risk of compromise in the immediate or near future, actions to avoid a spread of the effects of the compromise must be taken. A trusted outside directory that is compromised could allow an unauthorized user to access resources in the trusting directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Refer to the list of actual manual AD trusts (cross-directory configurations) collected from the site representative. 2. If there are no manual AD trusts (cross-directory configurations) defined, this check is not applicable. For AD, this includes external, forest, or realm trust relationship types. 3. Obtain a copy of the site's supplemental CPCON procedures as required by Strategic Command Directive (SD) 527-1. 4. Verify that it has been determined by the IAM whether CPCON response actions need to include procedures to disable manual AD trusts (cross-directory configurations). The objective is to determine if the need has been explicitly evaluated. 5. If it has been determined that actions to disable manual AD trusts (cross-directory configurations) are not necessary, then this check is not applicable. 6. If it has been determined that actions to disable manual AD trusts (cross-directory configurations) are necessary, verify that the policy to implement these actions has been documented. 7. If actions to disable manual AD trusts (cross-directory configurations) are needed and no policy has been documented, then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-269097`

### Rule: Windows Server domain controllers must have Kerberos logging enabled with servers hosting Active Directory Certificate Services (AD CS).

**Rule ID:** `SV-269097r1026170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Although Kerberos logging can be used for troubleshooting, it can also provide security information for successful and failed login attempts. If a malicious actor uses a forged or unauthorized certificate to complete Kerberos PKINIT authentication, the Kerberos Authentication Service success audit in event 4768 can be used to detect the specific fraudulent certificate that was used to authenticate to then revoke the certificate. Kerberos Service Ticket operation events can be used in an investigation to discover which services were accessed by a malicious actor or to detect if an SCHANNEL-based authentication was abused by a malicious actor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers only. It is not applicable for other systems. Verify the following is configured on the domain controller. Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Advanced Audit Policy Configuration >> System Audit Policies >> Account Logon. If "Audit Kerberos Authentication Service" and "Audit Kerberos Ticket Operations" are not set to "Success and Failure", this is a finding.

