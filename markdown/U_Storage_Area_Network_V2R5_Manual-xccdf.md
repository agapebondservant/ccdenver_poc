# STIG Benchmark: Storage Area Network Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: The default zone visibility is not set to "none"

**Group ID:** `V-6605`

### Rule: The default zone visibility setting is not set to “none”.

**Rule ID:** `SV-6724r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the default zone visibility setting is set to "none", new clients brought into the SAN will not be allowed access to any SAN zone they are not explicitly placed into. The IAO/NSO will ensure that the default zone visibility setting, if available, is set to “none”.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>If there are client systems that have not explicitly been placed in a zone they may be denied access to data they need.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Reviewer with the assistance of the IAO/NSO, verify that the default zone visibility setting is set to “none”.. If this setting is not available mark this check as N/A.

## Group: Hard zoning is not used to protect the SAN.

**Group ID:** `V-6608`

### Rule: Hard zoning is not used to protect the SAN.

**Rule ID:** `SV-6727r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Risk: In a SAN environment, we potentially have data with differing levels or need-to-know stored on the same "system". A high level of assurance that a valid entity (user/system/process) of one set of data is not inadvertently given access to data that is unauthorized. Depending on the data and implementation, lack of hard zoning could provide access to classifed, administrative configuration, or other privileged information. A zone is considered to be "hard" if it is hardware enforced. In other words, it is considered “hard” in that they are always enforced by the destination ASIC. "Soft" zoning is more flexible but is also more vulnerable. In "soft" or WWN-enforced zoning, however, the HBA on the initiating devices store a copy of the name server entries, which were discovered in the last IO scan/discovery. It is possible for the HBA to include old addresses, which are no longer allowed in the newly established zoning rules. So your goal is to mitigate this risk in some way. If hardware enforced zoning is used this is not an issue as the destination port will not allow any access regardless of what the OS/HBA “thinks” it has access to. Supplementary Note: Registry State Change Notifications ( RSCN ) storms in large SAN deployments are another factor of which the system administrator must be aware. RSCNs are a broadcast function that allows notification to registered devices when a state change occurs within a SAN topology. These changes could be as simple as a cable being unplugged or a new HBA being connected. When such changes take place, all members would have to be notified of the change and conflicts would have to be resolved, before the name servers are updated. In large configurations it could take a long time for the entire system to stabilize, impairing performance. Effective zoning on the switch would help in minimizing RSCN storms, as only devices within a zone would get notified of state changes. It would also be ideal to make note of business critical servers and make changes to zones and fabrics that affect these servers at non business critical times. Tape fabrics could also be separated from disk fabric (although this comes at a cost). Statistics of RSCN's are available from a few switch vendors. Monitoring these consistently and considering these before expansion of SAN's would help you with effective storage deployments. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance>Although soft zoning is not recommended for DoD SAN implementations, this form of zoning does partially mitigate the risk and is preferred to no zoning. If soft zoning is used AND the system is does not process classified information, then this finding may be downgraded to a CAT 2 with a POA&M documenting a migration plan for implementation of hard zoning.</SeverityOverrideGuidance><PotentialImpacts>If the zoning ACLs are not properly migrated from the soft zoning format to the hard zoning format a denial of service can be created where a client is not allowed to access required data. Also a compromise of sensitive data can occur if a client is allowed access to data not required. This can also happen if you are moving from no zoning to hard zoning and incorrectly configure the ACLs.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer, with the assistance of the IAO/NSO, will verify that hard zoning is used to protect the SAN. If soft zoning is used, this is a finding. If soft zoning must be used (with DAA approval), this is still a CAT II finding and a migration plan must be in place. However, note that the HBA’s memory is non-persistent, thus when zoning changes are made, a policy must be in place (show via the log that it is enforced) to force a state change update in the affected HBAs immediately after making zoning changes.

## Group: Compliance with Network Infrastructure and Enclave

**Group ID:** `V-6610`

### Rule: The SANs are not compliant with overall network security architecture, appropriate enclave, and data center security requirements in the Network Infrastructure STIG and the Enclave STIG

**Rule ID:** `SV-6730r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inconsistencies with the Network Infrastructure STIG, the Enclave STIG, and the SAN implementation can lead to the creation of vulnerabilities in the network or the enclave.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will interview the IAO/NSO to validate that SANs are compliant with overall network security architecture, appropriate enclave, and data center security requirements in the Network Infrastructure STIG and the Enclave STIG. NOTE: The intent of this check is to ensure that the other checklists were applied. If they are applied then, regardless of what the findings are, this is not a finding. The objective of this policy is met if the other checklists were applied and documented.

## Group: All security related patches are not installed.

**Group ID:** `V-6613`

### Rule: All security related patches are not installed.

**Rule ID:** `SV-6733r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to install security related patches leaves the SAN open to attack by exploiting known vulnerabilities. The IAO/NSO will ensure that all security-related patches are installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>Untested patches can lead to the SAN degradation or failure.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>VIVM-1</IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that all security related patches are installed.

## Group: Component Compliance with applicable STIG

**Group ID:** `V-6619`

### Rule: Prior to installing SAN components (servers, switches, and management stations) onto the DOD network infrastructure, components are not configured to meet the applicable STIG requirements.

**Rule ID:** `SV-6739r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many SAN components (servers, switches, management stations) have security requirements from other STIGs. It will be verified that all requirement are complied with. The IAO/NSO will ensure that prior to installing SAN components (servers, switches, and management stations) onto the DOD network infrastructure, components are configured to meet the applicable STIG requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will interview the IAO/NSO and view VMS to verify that prior to installing SAN components (servers, switches, and management stations) onto the DOD network infrastructure, components are configured to meet the applicable STIG requirements.

## Group: Servers and hosts OS STIG Requirements

**Group ID:** `V-6622`

### Rule: Servers and other hosts are not compliant with applicable Operating System (OS) STIG requirements.

**Rule ID:** `SV-6742r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SAN servers and other hosts are hardware software combinations that actually run under the control of a native OS found on the component. This OS may be UNIX, LNIX, Windows, etc. The underlying OS must be configured to be compliant with the applicable STIG to ensure that they do not insert known vulnerabilities into the DOD network infrastructure. The IAO/NSO will ensure that servers and other hosts are compliant with applicable Operating System (OS) STIG requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>Some SAN software may not function correctly on a STIG compliant server or host. </PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>DCCS-1, DCCS-2</IAControls>

**Check Text:**
The reviewer will interview the IAO/NSO and view the VMS to verify that servers and other hosts are compliant with applicable Operating System (OS) STIG requirements.

## Group: Anti-virus on servers and host.

**Group ID:** `V-6623`

### Rule: Vendor supported, DOD approved, anti-virus software is not installed and configured on all SAN servers in accordance with the applicable operating system STIG on SAN servers and management devices and kept up-to-date with the most recent virus definition tables.

**Rule ID:** `SV-6743r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The SAN servers and other hosts are subject to virus and worm attacks as are any systems running an OS. If the anti-virus software is not installed or the virus definitions are not maintained on these systems, this could expose the entire enclave network to exploits of known vulnerabilities. The IAO/NSO will ensure that vendor supported, DOD approved, anti-virus software is installed and configured on all SAN servers in accordance with the applicable operating system STIG on SAN servers and management devices and kept up-to-date with the most recent virus definition tables.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will verify that vendor supported, DOD approved, anti-virus software is installed and configured on all SAN servers in accordance with the applicable operating system STIG on SAN servers and management devices and kept up-to-date with the most recent virus definition tables. If an OS review has reciently been completed verify that the anti-virus check was not a finding. Otherwise perform a manual check as described in the applicable OS checklist.

## Group: SAN Topology Drawing

**Group ID:** `V-6628`

### Rule: A current drawing of the site’s SAN topology that includes all external and internal links, zones, and all interconnected equipment is not being maintained.

**Rule ID:** `SV-6748r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A drawing of the SAN topology gives the IAO and other interested individuals a pictorial representation of the SAN. This can be helpful in diagnosing potential security problems. The IAO/NSO will maintain a current drawing of the site’s SAN topology that includes all external and internal links, zones, and all interconnected equipment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>DCHW-1</IAControls>

**Check Text:**
The reviewer will interview the IAO/NSO and view the drawings supplied to verify that a current drawing of the site’s SAN topology that includes all external and internal links, zones, and all interconnected equipment.

## Group: Physical Access to SAN Network Devices

**Group ID:** `V-6631`

### Rule: All the network level devices interconnected to the SAN are not located in a secure room with limited access.

**Rule ID:** `SV-6751r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network level devices are not located in a secure area they can be tampered with which could lead to a denial of service if the device is powered off or sensitive data can be compromised by a tap connected to the device. The IAO/NSO will ensure that all the network level devices interconnected to the SAN are located in a secure room with limited access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>Moving devices can disrupt the SAN environment while the move is taking place.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>PECF-1, PECF-2</IAControls>

**Check Text:**
The reviewer will interview the IAO/NSO and view the network level devices to verify whether they are located in a secure room with limited access.

## Group: SAN Fabric Switch User Accounts with Passwords

**Group ID:** `V-6632`

### Rule: Individual user accounts with passwords are not set up and maintained for the SAN fabric switch.

**Rule ID:** `SV-6752r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identification and authentication unauthorized users could reconfigure the SAN or disrupt its operation by logging in to the fabric switch and executing unauthorized commands. The IAO/NSO will ensure individual user accounts with passwords are set up and maintained for the SAN fabric switch in accordance with the guidance contained in Appendix B, CJCSM and the Network Infrastructure STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>The IAO/NSO will ensure that individual user accounts with passwords are set up and maintained in accordance with the guidance contained in Appendix B, Chairman Of The Joint Chiefs of Staff Manual CJCSM 6510.1 and the DODI 8500.2.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>IAIA-1, IAIA-2</IAControls>

**Check Text:**
The reviewer, with the assistance of the IAO/NSO, will verify that individual user accounts with passwords are set up and maintained for the SAN fabric switch.

## Group: Fabric Switches do not have bidirectional authentication

**Group ID:** `V-6633`

### Rule: The SAN must be configured to use bidirectional authentication.

**Rule ID:** `SV-6753r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Switch-to-switch management traffic does not have to be encrypted. Bidirectional authentication ensures that a rogue switch cannot be inserted and be auto configured to join the fabric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>Failure to configure all components to use encryption could cause the SAN to degrade or fail.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Switch Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all fabric switches are configured to bidirectional authentication.

## Group: SAN Switch encryption and DOD PKI

**Group ID:** `V-6634`

### Rule: The fabric switches must use DoD-approved PKI rather than proprietary or self-signed device certificates.

**Rule ID:** `SV-6768r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>DOD PKI supplies better protection from malicious attacks than userid/password authentication and should be used anytime it is feasible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>Failure to develop a plan for the coordinated correction of these vulnerabilities across the SAN could lead to a denial of service caused by a disruption or failure of the SAN.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify fabric switches are protected by DOD PKI. View the installed device certificates. Verify a DoD -approved certificate is loaded. If any of the certificates have the name or identifier of a non-DoD- approved source in the Issuer field, this is a finding.

## Group: SAN Network Management Ports Fabric Switch

**Group ID:** `V-6635`

### Rule: Network management ports on the SAN fabric switches except those needed to support the operational commitments of the sites are not disabled.

**Rule ID:** `SV-6769r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabled network management ports that are not required expose the SAN fabric switch and the entire network to unnecessary vulnerabilities. By disabling these unneeded ports the exposure profile of the device and network is diminished. The IAO/NSO will disable all network management ports on the SAN fabric switches except those needed to support the operational commitments of the sites.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Switch Administrator</Responsibility><IAControls>DCBP-1</IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that all network management ports on the SAN fabric switches are disabled except those needed to support the operational commitments of the sites.

## Group: SAN management out-of-band or direct connect

**Group ID:** `V-6636`

### Rule: SAN management is not accomplished using the out-of-band or direct connection method.

**Rule ID:** `SV-6773r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing the management traffic from the production network diminishes the security profile of the SAN servers by allowing all the management ports to be closed on the production network. The IAO/NSO will ensure that SAN management is accomplished using the out-of-band or direct connection method.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will interview the IAO and view the SAN network drawings provided.

## Group: Management Console to SAN Fabric Authentication

**Group ID:** `V-6637`

### Rule: Communications from the management console to the SAN fabric are not protected strong two-factor authentication.

**Rule ID:** `SV-6778r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using two-factor authentication between the SAN management console and the fabric enhances the security of the communications carrying privileged functions. It is harder for an unauthorized management console to take control of the SAN. The preferred solution for two-factor authentication is DoD PKI implemented on the CAC or Alternative (Alt) token.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that communications from the management console to the SAN fabric are protected using DOD PKI. If another method of two-factor authentication is used, then inspect approval documentation. If two-factor authentication is not used, this is a finding. If two-factor authentication method is not DoD PKI and no approval documentation exists, this is a finding.

## Group: Default PKI keys

**Group ID:** `V-6638`

### Rule: The manufacturer’s default PKI keys have not been changed prior to attaching the switch to the SAN Fabric.

**Rule ID:** `SV-6780r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the manufacturer's default PKI keys are allowed to remain active on the device, it can be accessed by a malicious individual with access to the default key. The IAO/NSO will ensure that the manufacturer’s default PKI keys are changed prior to attaching the switch to the SAN Fabric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>The manufacturer may need to access the device for maintenance. If the PKI keys cannot be reestablished this will fail.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>IAIA-1, IAIA-2</IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that the manufacturer’s default PKI keys have been changed prior to attaching the switch to the SAN Fabric.

## Group: FIPS 140-1/2 for management to fabric.

**Group ID:** `V-6639`

### Rule: The SAN is not configured to use FIPS 140-1/2 validated encryption algorithm to protect management-to-fabric communications.

**Rule ID:** `SV-6783r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The communication between the SAN management consol and the SAN fabric carries sensitive privileged configuration data. This data's confidentiality will be protected with FIPS 140-1/2 validate algorithm for encryption. Configuration data could be used to create a denial of service by disrupting the SAN fabric. The storage administrator will configure the SAN to use FIPS 140-1/2 validated encryption algorithm to protect management-to-fabric communications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Other</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will, with the assistance of the storage administrator, verify that the SAN is configured to use FIPS 140-1/2 validated encryption algorithm to protect management-to-fabric communications.

## Group: Password SAN Management Console and Ports

**Group ID:** `V-6645`

### Rule: All SAN management consoles and ports are not password protected.

**Rule ID:** `SV-6791r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without password protection malicious users can create a denial of service by disrupting the SAN or allow the compromise of sensitive date by reconfiguring the SAN topography. The IAO/NSO will ensure that all SAN management consoles and ports are password protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that all SAN management consoles and ports are password protected.

## Group: Default SAN Management Software Password

**Group ID:** `V-6646`

### Rule: The manufacturer’s default passwords have not been changed for all SAN management software.

**Rule ID:** `SV-6792r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The changing of passwords from the default value blocks malicious users with knowledge of the default passwords for the manufacturer's SAN Management software from creating a denial of service by disrupting the SAN or reconfigure the SAN topology leading to a compromise of sensitive data. The IAO/NSO will ensure that the manufacturer’s default passwords are changed for all SAN management software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that the manufacturer’s default passwords have been changed for all SAN management software.

## Group: SAN Fabric Zoning List Deny-By-Default

**Group ID:** `V-6647`

### Rule: The SAN fabric zoning lists are not based on a policy of Deny-by-Default with blocks on all services and protocols not required on the given port or by the site.

**Rule ID:** `SV-6793r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By using the Deny-by-Default based policy, any service or protocol not required by a port and overlooked in the zoning list will be denied access. If Deny-by-Default based policy was not used any overlooked service or protocol not required by a port could have access to sensitive data compromising that data. The IAO/NSO will ensure that SAN fabric zoning lists are based on a policy of Deny-by-Default with blocks on all services and protocols not required on the given port or by the site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>Changing to a policy based on Deny-by-Default can cause overlooked services or protocols required by a port to be denied access to data they need.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>DCBP-1</IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that SAN fabric zoning lists are based on a policy of Deny-by-Default with blocks on all services and protocols not required on the given port or by the site.

## Group: Logging Failed Access to Port, Protocols, Services

**Group ID:** `V-6648`

### Rule: Attempts to access ports, protocols, or services that are denied are not logged..

**Rule ID:** `SV-6794r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Logging or auditing of failed access attempts is a necessary component for the forensic investigation of security incidents. Without logging there is no way to demonstrate that the access attempt was made or when it was made. Additionally a pattern of access failures cannot be demonstrated to assert that an intended attack was being made as apposed to an accidental intrusion. The IAO/NSO will ensure that all attempts to any port, protocol, or service that is denied are logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>If sufficient space is not allowed for logging or auditing, a denial of service or loss of data could be caused by overflowing the space allocated.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that all attempts to any port, protocol, or service that is denied are logged.

## Group: SNMP usage and configuration.

**Group ID:** `V-6652`

### Rule: Simple Network Management Protocol (SNMP) is used and it is not configured in accordance with the guidance contained in the Network Infrastructure STIG.

**Rule ID:** `SV-6798r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>There are vulnerabilities in some implementations and some configurations of SNMP. Therefore if SNMP is used the guidelines found in the Network Infrastructure STIG in selecting a version of SNMP to use and how to configure it will be followed. If Simple Network Management Protocol (SNMP) is used, the IAO/NSO will ensure it is configured in accordance with the guidance contained in the Network Infrastructure STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>Network monitoring tools that are not modified to match the configuration used for SNMP in the SAN will fail.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the IAO/NSO, verify that if Simple Network Management Protocol (SNMP) is used, it is configured in accordance with the guidance contained in the Network Infrastructure STIG. NOTE: The intent of this check is to ensure that the other checklists were applied. If they are applied then, regardless of what the findings are, this is not a finding. The objective of this policy is met if the other checklist was applied and documented.

## Group: Authorized IP Addresses allowed for SNMP

**Group ID:** `V-6656`

### Rule: Unauthorized IP addresses are allowed Simple Network Management Protocol (SNMP) access to the SAN devices.

**Rule ID:** `SV-6802r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SNMP, by virtue of what it is designed to do, can be a large security risk. Because SNMP can obtain device information and set device parameters, unauthorized users can cause damage. Restricting IP address that can access SNMP on the SAN devices will further limit the possibility of malicious access being made. The IAO/NSO will ensure that only authorized IP addresses are allowed Simple Network Management Protocol (SNMP) access to the SAN devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>DCBP-1</IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that only authorized IP addresses are allowed Simple Network Management Protocol (SNMP) access to the SAN devices. This can be done with by checking the ACLs for the SAN device ports.

## Group: Only Internal Network SNMP Access to SAN

**Group ID:** `V-6657`

### Rule: The IP addresses of the hosts permitted SNMP access to the SAN management devices do not belong to the internal network.

**Rule ID:** `SV-6803r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SNMP, by virtue of what it is designed to do, can be a large security risk. Because SNMP can obtain device information and set device parameters, unauthorized users can cause damage. Therefore access to a SAN device from an IP address outside of the internal network will not be allowed. The IAO/NSO will ensure IP addresses of the hosts that are permitted SNMP access to the SAN management devices belong to the internal network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that the IP addresses of the hosts permitted SNMP access to the SAN management devices belong to the internal network. The ACLs for the SAN ports should be checked.

## Group: Fibre Channel network End-User Platform Restricted

**Group ID:** `V-6660`

### Rule: End-user platforms are directly attached to the Fibre Channel network or access storage devices directly.

**Rule ID:** `SV-6807r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>End-user platforms should only be connected to servers that run applications that access the data found on the SAN devices. SANs do not supply a robust user identification and authentication platform. They depend on the servers and applications to authenticate the users and restrict access to users as required. The IAO/NSO will ensure that end-user platforms are not directly attached to the Fibre Channel network and may not access storage devices directly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>End-user platforms attached to the SAN may be dependent upon the SAN for storage. An alternate type of storage will need to be found for these platforms.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>DCBP-1</IAControls>

**Check Text:**
The reviewer will, with the assistance of the IAO/NSO, verify that end-user platforms are not directly attached to the Fibre Channel network and may not access storage devices directly. If the SAN is small with all of its components collocated, this can be done by a visual inspection but in most cases the reviewer will have to check the SAN network drawing.

## Group: Backup of critical SAN Software and configurations

**Group ID:** `V-6661`

### Rule: Fabric switch configurations and management station configuration are not archived and/or copies of the operating system and other critical software for all SAN components are not stored in a fire rated container or are not collocated with the operational software.

**Rule ID:** `SV-6809r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.Backup and recovery procedures are critical to the security and availability of the SAN system. If a system is compromised, shut down, or otherwise not available for service, this could hinder the availability of resources to the warfighter. The IAO/NSO will ensure that all fabric switch configurations and management station configuration are archived and copies of the operating system and other critical software for all SAN components are stored in a fire rated container or otherwise not collocated with the operational software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>COSW-1</IAControls>

**Check Text:**
The reviewer will interview the IAO/NSO and view the stored information to verify that all fabric switch configurations and management station configuration are archived and copies of the operating system and other critical software for all SAN components are stored in a fire rated container or otherwise not collocated with the operational software.

## Group: SAN Fixed IP Required.

**Group ID:** `V-7081`

### Rule: SAN components are not configured with fixed IP addresses.

**Rule ID:** `SV-7465r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without fixed IP address filtering or restricting of access based on IP addressing will not function correctly allowing unauthorized access to SAN components or creating a denial of service by blocking legitimate traffic from authorized components. The storage administrator will ensure that all SAN components are configured to use static IP addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts>If this is not done in a coordinated manner with all access lists a denial of service could be created.</PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls>DCBP-1</IAControls>

**Check Text:**
The reviewer with the assistance of the SA will verify that all SAN components are configured with fixed IP addresses.

## Group: Sunset Requirement

**Group ID:** `V-6662`

### Rule: The device must be supported by the vendor.

**Rule ID:** `SV-6802r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The use of unsupported devices can lead to the compromise of sensitive data or the compromise of the network the SAN is attached to.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Network Security Officer</Responsibility><IAControls>DCBP-1</IAControls>

**Check Text:**
This STIG is sunset and will no longer be maintained. If the site is using a device not supported by the vendor, this is a finding.

