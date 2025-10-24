# STIG Benchmark: Network Infrastructure Policy Security Technical Implementation Guide

---

**Version:** 10

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: NET0160

**Group ID:** `V-251333`

### Rule: Written mission justification approval must be obtained from the Office of the DoD CIO prior to establishing a direct connection to the Internet via commercial service provider outside DoD CIO approved Internet access points (e.g. DISA IAP, Cloud Access Point, NIPRnet Federated Gateway, DREN IAP, etc.).

**Rule ID:** `SV-251333r877971_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Analysis of DoD reported incidents reveal current protective measures at the NIPRNet boundary points are insufficient. Documented ISPs and validated architectures for DMZs are necessary to protect internal network resources from cyber attacks originating from external Internet sources by protective environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Any connection to an internet service provider (ISP) must be approved by the Office of the DoD CIO before a connection is made to the ISP. Specifically, DoD Instruction 8010.01, DEPARTMENT OF DEFENSE INFORMATION NETWORK (DODIN) TRANSPORT, Sept 10, 2018 states: Para 4.4 “a. Commercial transport services procured as an alternative to the DISN-provided transport requires compliance with this issuance or DoD CIO review and approval.” Based on the use cases below, verify written approval has been obtained from the Office of the DoD CIO or verify a renewal request has been appropriately submitted. There are three basic use cases for an ISP connection. Use case (1): An ISP connection that originates from an approved DISN infrastructure source (includes IAP connections at the DECCs). A DoDIN Waiver is required for a CC/S/A to connect the unclassified DISN to an ISP. These connection requests must come to the Waiver Panel with a Component CIO endorsement of the requirement. These connections should not be provisioned and put into use until waived. Expired waivers pending renewal from the OSD DoDIN Waiver Panel may be downgraded to a Severity 3 category, if proof of a requested renewal can be verified. A DISN enclave that cannot prove DoDIN Waiver approval for the ISP connection is a Severity 1 category. Note: If discovered during a CCRI assessment, the review team lead will immediately report the unapproved ISP connection to the USCYBERCOM (301-688-3585) and the Connection Approval Office (301-225-2900/2901). USCYBERCOM will direct the connection be immediately disconnected. Use Case (2): An ISP connection to a Stand Alone Enclave (physically and logically separated from any DISN connection) requires DoDIN Waiver approval prior to connection. The Stand Alone Enclave must have an AO issued ATO and the connection must be logically and physically separated from the DISN. An unapproved ISP connection in this use case will be assigned a Severity 3 category. Use Case (3): An ISP connection to a non-DoD network (such as a contractor-owned infrastructure) co-located on the same premises as the DoD network. The non-DoD network is physically and logically separated from any DoD IP network. Furthermore, it is not connected to any DoD IP network. The non-DoD network infrastructure is not DoD funded nor is it operated or administered by DoD military or civilian personnel. In addition, the non-DoD network with the ISP connection is not storing, processing, or transmitting any DoD data. For such a network as defined herein, a DoDIN Waiver approval is not required for deploying a connection to an ISP. However, the AO must perform and have on file a risk assessment endorsed by the facility or installation command. If any of the above use cases are applicable, and written approval has been not been obtained from the Office of the DoD CIO or a renewal request has not been submitted, this is a finding.

## Group: NET0140

**Group ID:** `V-251334`

### Rule: The connection between the Channel Service Unit/Data Service Unit (CSU/DSU) and the Local Exchange Carriers (LEC) data service jack (i.e., demarc) as well as any service provider premise equipment must be located in a secure environment.

**Rule ID:** `SV-251334r805957_rule`
**Severity:** low

**Description:**
<VulnDiscussion>DOD leased lines carry an aggregate of sensitive and non-sensitive data; therefore unauthorized access must be restricted. Inadequate cable protection can lead to damage and denial of service attacks against the site and the LAN infrastructure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology to determine external connections and inspect location where CSU/DSUs and data service jacks reside. If these components are not in a secured environment, this is a finding.

## Group: NET-IDPS-016

**Group ID:** `V-251335`

### Rule: An Intrusion Detection and Prevention System (IDPS) sensor must be deployed to monitor all Demilitarized Zone (DMZ) segments housing public servers.

**Rule ID:** `SV-251335r853642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The initial step in IDPS deployment is determining where sensors should be placed. Because attacks originate at the enclave perimeter and within the enclave boundary an IDPS implementation at the enclave perimeter only will not suffice. By placing IDPS technology throughout the Enterprise Regional enclaves and stand-alone enclaves, system administrators can track the spread of attacks and take corrective actions to prevent attacks reaching critical resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DMZ topology and verify public servers are being monitored by an IDPS. If an IDPS sensor is not deployed to monitor all DMZ segments housing public servers, this is a finding.

## Group: NET-IDPS-018

**Group ID:** `V-251336`

### Rule: An Intrusion Detection and Prevention System (IDPS) sensor must be deployed to monitor the network segment hosting web, application, and database servers.

**Rule ID:** `SV-251336r853643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attacks can originate within the enclave boundary. Hence, deploying an IDPS on the network segment hosting web, application, and database servers is imperative. The servers are critical resource and the network segment hosting them will receive the most traffic within the enclave. Deploying IDPS on this network is promotes defense-in-depth principles that will enable operations to detect attacks quickly and take corrective actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review topology of the network segment hosting the web, application, and database servers. If this segment is not being monitored by an IDPS sensor, this is a finding.

## Group: NET-IDPS-019

**Group ID:** `V-251337`

### Rule: An Intrusion Detection and Prevention System (IDPS) sensor must be deployed to monitor network segments that house network security management servers.

**Rule ID:** `SV-251337r853644_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The initial step in IDPS deployment is determining where sensors should be placed. Because attacks originate at the enclave perimeter and within the enclave boundary an IDPS implementation at the enclave perimeter only will not suffice. By placing IDPS technology throughout the Enterprise Regional enclaves and stand-alone enclaves, system administrators can track the spread of attacks and take corrective actions to prevent attacks reaching critical resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the management network topology and verify network security management servers are being monitored by an IDPS. If an IDPS sensor is not deployed to monitor all segments housing network security management servers, this is a finding.

## Group: NET-IDPS-021

**Group ID:** `V-251338`

### Rule: An Intrusion Detection and Prevention System (IDPS) must be deployed to monitor all unencrypted traffic entering and leaving the enclave.

**Rule ID:** `SV-251338r1007842_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Per CJCSI 6510.01F, Enclosure A-5, Paragraph 8, "DOD ISs (e.g., enclaves, applications, outsourced IT-based process, and platform IT interconnections) shall be monitored to detect and react to incidents, intrusions, disruption of services, or other unauthorized activities (including insider threat) that threaten the security of DOD operations or IT resources, including internal misuse." An Intrusion Prevention System (IPS) allows the sensor to monitor, alert, and actively attempt to drop/block malicious traffic. An Intrusion Detection System (IDS) uses a passive method; receiving a copy of the packets to analyze and alert authorized persons about any malicious activity. While an IDS or an IPS in a passive role cannot stop the attack itself, it can typically notify and dynamically assign ACLs or other rules to a firewall or router for filtering. The preferred method of installation is to have the IDPS configured for inline mode. Only when there is a valid technical reason, should the IDPS be placed into a passive or IDS mode. For a full uninhibited view of the traffic, the IDPS must sit behind the enclave's firewall. This will allow the IDPS to monitor all traffic unencrypted, entering or leaving the enclave.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology to ensure the enclave has the IDPS positioned to monitor all traffic to and from the enclave. Review any type of report that was recently produced from information provided by the sensor showing any recent alerts, an escalation activity and any type of log or configuration changes. This will show the sensor is being actively monitored and alerts are being acted upon. If the enclave's CNDSP requires continuous monitoring of the IDPS, the CNDSPs management team (e.g. sensor grid management team at DISA) will verify the operational status by providing information about the enclave's IDPS such as a network diagram, MOA, current alert information, or other information to validate its operational status. Note: If the authorized Cybersecurity Service Provider (CSSP) can utilize security tools and services that ensures the network (can include perimeter connection and enclave) is monitored in a manner that would satisfy CJCSI 6510.01F, Enclosure A-5, Paragraph 8, an IDSP is not required to be part of the security solution. If there is no IDPS positioned and enabled to monitor all ingress and egress traffic, this is a finding. Exception: If the perimeter security for the enclave or B/C/P/S is provisioned via the JRSS, then this requirement is not applicable.

## Group: NET-IDPS-024

**Group ID:** `V-251339`

### Rule: Sensor traffic in transit must be protected at all times via an Out-of-Band (OOB) network or an encrypted tunnel between site locations.

**Rule ID:** `SV-251339r805972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User interface services must be physically or logically separated from data storage and management services. Data from IDS sensors must be protected by confidentiality controls; from being lost and altered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram and interview the ISSO to determine how the IDS sensor data is transported between sites. If it is not transported across an OOB network or an encrypted tunnel, this is a finding.

## Group: NET-IDPS-025

**Group ID:** `V-251340`

### Rule: Intrusion Detection and Prevention System (IDPS) traffic between the sensor and the security management or sensor data collection servers must traverse a dedicated Virtual Local Area Network (VLAN) logically separating IDPS traffic from all other enclave traffic.

**Rule ID:** `SV-251340r805975_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All IDPS data collected by agents in the enclave at required locations must also be protected by logical separation when in transit from the agent to the management or database servers located on the Network Management subnet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram and interview the ISSO to determine how the IDPS traffic between the sensor and the security management or sensor data collection servers is transported. If the IDPS traffic does not traverse a dedicated VLAN logically separating IDPS traffic from all other enclave traffic, this is a finding.

## Group: NET-IDPS-027

**Group ID:** `V-251341`

### Rule: Products collecting baselines for anomaly-based detection must have their baselines rebuilt based on changes to mission requirements such as Information Operations Conditions (INFOCON) levels and when the traffic patterns are expected to change significantly.

**Rule ID:** `SV-251341r805978_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Administrators should ensure that any products collecting baselines for anomaly-based detection have their baselines rebuilt periodically as needed to support accurate detection. The ISSM is required to have the enclave prepared for readiness by raising INFOCON levels prior to an activity to ensure the network is as ready as possible when the operation or exercise begins. Because system and network administrators implement many of the INFOCON measures over a period of time in a pre-determined operational rhythm, commanders should raise INFOCON levels early enough to ensure completion of at least one cycle before the operational activity begins. Recommendations for possible INFOCON changes should be written into Operation Plans (OPLAN) and Concept Plans (CONPLAN). Guidelines can be found in Strategic Command Directive (SD) 527-1.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the IDPS administrator and determine if anomaly-based detection is deployed in the network. If implemented, ensure that any products collecting baselines for anomaly-based detection have their baselines rebuilt periodically to support accurate detection. If the collection products do not have their baselines rebuilt periodically, this is a finding.

## Group: NET-IDPS-029

**Group ID:** `V-251342`

### Rule: If a Secure File Transfer Protocol (SFTP) server is used to provide updates to the sensors, the server must be configured to allow read-only access to the files within the directory on which the signature packs are placed.

**Rule ID:** `SV-251342r805981_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In a large scale IDPS deployment, it is common to have an automated update process implemented. This is accomplished by having the updates downloaded on a dedicated SFTP server within the management network. The SFTP server should be configured to allow read-only access to the files within the directory on which the signature packs are placed, and then only from the account that the sensors will use. The sensors can then be configured to automatically check the SFTP server periodically to look for the new signature packs and to update themselves once they have been tested.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the signatures are located on a server, verify that the directories on which the signature packs are placed are protected by read-only access. If the directories are not set for read-only access, this is a finding.

## Group: NET-IDPS-030

**Group ID:** `V-251343`

### Rule: If an automated scheduler is used to provide updates to the sensors, an account on the file server must be defined that will provide access to the signatures only to the sensors.

**Rule ID:** `SV-251343r805984_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In a large scale IDPS deployment, it is common to have an automated update process implemented. This is accomplished by having the updates downloaded on a dedicated secure file server within the management network. The file server should be configured to allow read-only access to the files within the directory on which the signature packs are placed, and then only from the account that the sensors will use. The sensors can then be configured to automatically check the secure file server periodically to look for the new signature packs and to update themselves.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the file server accounts and determine if the accounts with read access to the IDPS signatures are provided only to the IDPS sensors. If there are accounts other than those allocated for the IDPS sensors providing access to the signatures, this is a finding.

## Group: NET-IDPS-031

**Group ID:** `V-251344`

### Rule: The Intrusion Detection and Prevention System (IDPS) configuration must be backed up before applying software or signature updates, or when making changes to the configuration.

**Rule ID:** `SV-251344r805987_rule`
**Severity:** low

**Description:**
<VulnDiscussion>There are two types of IDPS updates: software updates and signature updates. Software updates fix bugs in the IDPS software or add new functionality, while signature updates add new detection capabilities or refine existing detection capabilities (e.g., reducing false positives). For many IDPSs, signature updates cause program code to be altered or replaced, so they are really a specialized form of software update. For other IDPSs, signatures are not written in code, so a signature update is a change to the configuration data for the IDPS. Software updates can include any or all IDPS components, including sensors, agents, management servers, and consoles. Software updates for sensors and management servers, particularly appliance-based devices, are often applied by replacing an existing IDPS CD with a new one and rebooting the device. Many IDPSs run the software directly from the CD, so that no software installation is required. Other components, such as agents, require an administrator to install software or apply patches, either manually on each host or automatically through IDPS management software. Some vendors make software and signature updates available for download from their Web sites or other servers; often, the administrator interfaces for IDPSs have features for downloading and installing such updates. Administrators should verify the integrity of updates before applying them, because updates could have been inadvertently or intentionally altered or replaced. The recommended verification method depends on the update's format, as follows: Files downloaded from a Web site or FTP site. Administrators should compare file checksums provided by the vendor with checksums that they compute for the downloaded files. Update downloaded automatically through the IDPS user interface. If an update is downloaded as a single file or a set of files, either checksums provided by the vendor should be compared to checksums generated by the administrator, or the IDPS user interface itself should perform some sort of integrity check. In some cases, updates might be downloaded and installed as one action, precluding checksum verification; the IDPS user interface should check each update's integrity as part of this. Removable media (e.g., CD, DVD). Vendors may not provide a specific method for customers to verify the legitimacy of removable media apparently sent by the vendors. If media verification is a concern, administrators should contact their vendors to determine how the media can be verified, such as comparing vendor-provided checksums to checksums computed for files on the media, or verifying digital signatures on the media's contents to ensure they are valid. Administrators should also consider scanning the media for malware, with the caveat that false positives might be triggered by IDPS signatures for malware on the media.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to determine the IDPS maintenance procedures as well as have SA display the backup files saved on the file server. If the IDPS configuration is not backed up prior to applying software or signature updates, or when making changes to the configuration, this is a finding.

## Group: NET-IDPS-032

**Group ID:** `V-251345`

### Rule: The Intrusion Detection and Prevention System (IDPS) file checksums provided by the vendor must be compared and verified with checksums computed from CD or downloaded files.

**Rule ID:** `SV-251345r805990_rule`
**Severity:** low

**Description:**
<VulnDiscussion>There are two types of IDPS updates: software updates and signature updates. Software updates fix bugs in the IDPS software or add new functionality, while signature updates add new detection capabilities or refine existing detection capabilities (e.g., reducing false positives). For many IDPSs, signature updates cause program code to be altered or replaced, so they are really a specialized form of software update. For other IDPSs, signatures are not written in code, so a signature update is a change to the configuration data for the IDPS. Software updates can include any or all IDPS components, including sensors, agents, management servers, and consoles. Software updates for sensors and management servers, particularly appliance-based devices, are often applied by replacing an existing IDPS CD with a new one and rebooting the device. Many IDPSs run the software directly from the CD, so that no software installation is required. Other components, such as agents, require an administrator to install software or apply patches, either manually on each host or automatically through IDPS management software. Some vendors make software and signature updates available for download from their Web sites or other servers; often, the administrator interfaces for IDPSs have features for downloading and installing such updates. Administrators should verify the integrity of updates before applying them, because updates could have been inadvertently or intentionally altered or replaced. The recommended verification method depends on the update's format, as follows: Files downloaded from a Web site or FTP site. Administrators should compare file checksums provided by the vendor with checksums that they compute for the downloaded files. Update downloaded automatically through the IDPS user interface. If an update is downloaded as a single file or a set of files, either checksums provided by the vendor should be compared to checksums generated by the administrator, or the IDPS user interface itself should perform some sort of integrity check. In some cases, updates might be downloaded and installed as one action, precluding checksum verification; the IDPS user interface should check each update's integrity as part of this. Removable media (e.g., CD, DVD). Vendors may not provide a specific method for customers to verify the legitimacy of removable media apparently sent by the vendors. If media verification is a concern, administrators should contact their vendors to determine how the media can be verified, such as comparing vendor-provided checksums to checksums computed for files on the media, or verifying digital signatures on the media's contents to ensure they are valid. Administrators should also consider scanning the media for malware, with the caveat that false positives might be triggered by IDPS signatures for malware on the media.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA and determine the process of software and signature validation. If file checksums provided by the vendor are not compared and verified with checksums computed from CD or downloaded files, this is a finding.

## Group: NET-IDPS-033

**Group ID:** `V-251346`

### Rule: The organization must establish weekly data backup procedures for the network Intrusion Detection and Prevention System (IDPS) data.

**Rule ID:** `SV-251346r805993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IDPS data needs to be backed up to ensure preservation in the case a loss of data due to hardware failure or malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to determine the IDPS backup procedures as well as have SA display the backup files saved on the file server. If the IDPS data is not backed up on a weekly basis, this is a finding.

## Group: NET-IDPS-035

**Group ID:** `V-251347`

### Rule: The Intrusion Detection and Prevention System (IDPS) software and signatures must be updated when updates are provided by the vendor.

**Rule ID:** `SV-251347r805996_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Keeping the IDPS software updated with the latest engine and attack signatures will allow for the IDPS to detect all forms of known attacks. Not maintaining the IDPS properly could allow for attacks to go unnoticed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and the IDPS administrator. Have the IDPS administrator display update notifications that have been received, the build number or patch level, then search the vendor's vulnerability database for current release and patch level. If software and signatures are not updated when updates are provided by the vendor, this is a finding.

## Group: NET-TUNL-026

**Group ID:** `V-251348`

### Rule: Encapsulated and/or encrypted traffic received from another enclave must not bypass the network perimeter defense without being terminated and inspected before entering the enclaves private network.

**Rule ID:** `SV-251348r819076_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing encapsulated traffic to bypass the enclave's network perimeter without being filtered and inspected leaves the enclave vulnerable to malicious traffic that could result in compromise and denial of service. The destination of these packets could be servers that provide mission critical services and data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review network device configurations and topology diagrams to validate encapsulated traffic received from other enclaves terminate at the perimeter for filtering and content inspection. If the tunnel is terminated on a VPN gateway, validate the traffic is inspected by a firewall and IDPS before gaining access to the private network. If the tunnel is being provided by the perimeter router with a direct connection to the tenant's perimeter router, then the perimeter router (of the enclave providing the transient service) must be configured (examples: policy based routing or VRF bound to this interface with only a default route pointing out) to insure all traffic received by this connecting interface is forwarded directly to the NIPR/SIPR interface regardless of destination. If this isn't being done then the connecting interface will have to be treated as an external interface with all the applicable checks. Secured connections such as SSL or TLS which are used for remote access, secure web access, etc. is also applicable to this rule. These types of connections like the other types above must terminate at the enclave perimeter, enclave DMZ, or an enclave service network for filtering and content inspection before passing into the enclave's private network. If the tunnels do not meet any of the criteria above and bypass the enclave's perimeter without filtering and inspection, this is a finding. Note: This vulnerability is not applicable for any VPN connectivity between multiple sites of the same enclave, nor is it applicable for VPN remote access to the enclave. For theses deployments, the implementation must be compliant with all requirements specified within the VPN SRG.

## Group: NET-TUNL-028

**Group ID:** `V-251349`

### Rule: Tunneling of classified traffic across an unclassified IP transport network or service provider backbone must be documented in the enclaves security authorization package and an Approval to Connect (ATC), or an Interim ATC must be issued by DISA prior to implementation.

**Rule ID:** `SV-251349r916231_rule`
**Severity:** high

**Description:**
<VulnDiscussion>CJCSI 6211.02D instruction establishes policy and responsibilities for the connection of any information systems to the Defense Information Systems Network (DISN) provided transport. Enclosure E mandates that the CC/S/A document all IP tunnels transporting classified communication traffic in the enclave's security authorization package prior to implementation. An ATC or IATC amending the current connection approval must be in place prior to implementation. Enclosure D of the CJCSI 6211.02D also provides guidance on the requirements of tunneling classified data (section 15.a), which helps a CC/S/A determine applicability to their mission. Items include but are not limited to: - minimize tunneling of classified data over transport other than DISN provided transport (i.e., SIPRNET); - ensure the Authorizing Official (DAA) validates all requirements to tunnel classified information across unclassified IP infrastructure; - obtain DSAWG approval before tunneling classified data across unclassified IP infrastructure; - ensure transmission of classified information is secured through use of authorized cryptographic equipment and algorithms and/or PDSs; - document IP tunnels transporting classified communication traffic in the enclave’s security authorization package prior to implementation; - an ATC or IATC amending the current connection approval must be in place prior to implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the enclave's security authorization package and the ATC or Interim ATC amending the connection approval received. If the tunneling of classified traffic is not documented in the security authorization package and an ATC or Interim ATC, this is a finding.

## Group: NET-TUNL-030

**Group ID:** `V-251350`

### Rule: DSAWG approval must be obtained before tunneling classified traffic outside the components local area network boundaries across a non-DISN or OCONUS DISN unclassified IP wide area network transport infrastructure.

**Rule ID:** `SV-251350r877972_rule`
**Severity:** high

**Description:**
<VulnDiscussion>CJCSI 6211.02D instruction establishes policy and responsibilities for the connection of any information systems to the Defense Information Systems Network (DISN) provided transport. Enclosure E mandates that the CC/S/A obtain DSAWG approval before tunneling classified data outside component's local area network boundaries across a non-DISN or OCONUS DISN unclassified IP-wide area transport infrastructure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram. If there is a connection between the classified network and the unclassified network for the purpose of tunneling classified traffic across a non-DISN or OCONUS DISN unclassified IP network, verify there is approval by the DSAWG. If there is no document stating DSAWG approval, this is a finding.

## Group: NET-TUNL-031

**Group ID:** `V-251351`

### Rule: Tunneling of classified traffic across an unclassified IP transport network must employ cryptographic algorithms in accordance with CNSS Policy No. 15.

**Rule ID:** `SV-251351r916232_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When transporting classified data over an unclassified IP network, it is imperative that traffic from the classified enclave or community of interest is encrypted prior reaching the point of presence or service delivery node of the unclassified network. Confidentiality and integrity of the classified traffic must be preserved by employing cryptographic algorithms in accordance with CNSS Policy No. 15 which requires the appropriate Suite B cryptographic algorithms listed in ANNEX B or a commensurate suite of NSA-approved cryptographic algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the IPsec VPN gateway and verify that the tunnel provisioned for transporting classified traffic across an unclassified IP transport network is using cryptographic algorithms in accordance with CNSS Policy No. 15. If cryptographic algorithms used for tunneling classified traffic across an unclassified network are not in accordance with CNSS Policy No. 15, this is a finding.

## Group: NET-VLAN-001

**Group ID:** `V-251352`

### Rule: The organization must ensure all switches and associated cross-connect hardware are kept in a secure Intermediate Distribution Frame (IDF) or an enclosed cabinet that is kept locked.

**Rule ID:** `SV-251352r806011_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the IDF includes all hardware required to connect horizontal wiring to the backbone, it is imperative that all switches and associated cross-connect hardware are kept in a secured IDF or an enclosed cabinet that is kept locked. This will also prevent an attacker from gaining privilege mode access to the switch. Several switch products only require a reboot of the switch in order to reset or recover the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect switches and associated cross-connect hardware are kept in a secured IDF. If the hardware is located in an open area, verify all hardware is located in a secured and locked cabinet. If switches and associated cross-connect hardware are not kept in secured IDFs or locked cabinet, this is a finding.

## Group: NET0090

**Group ID:** `V-251353`

### Rule: Network topology diagrams for the enclave must be maintained and up to date at all times.

**Rule ID:** `SV-251353r806014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assist in the management, auditing, and security of the network infrastructure facility drawings and topology maps are a necessity. Topology maps are important because they show the overall layout of the network infrastructure and where devices are physically located. They also show the relationship and interconnectivity between devices and where possible intrusive attacks could take place. Having up to date network topology diagrams will also help show what the security, traffic, and physical impact of adding a new user(s) will be on the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validate the network diagram by correlating the information with all routers, multi-layer switches, and firewall configurations. Validate all subnets have been documented accordingly. Validate any connectivity documented on the diagram by physically examining the cable connections for the downstream and upstream links, as well as connections for major network components (Routers, Switches, Firewalls, IDS/IPS, etc.). If the site has not maintained network topology diagrams for the enclave, this is a finding.

## Group: NET0130

**Group ID:** `V-251354`

### Rule: All external connections must be validated and approved by the Authorizing Official (AO) and the Connection Approval Office (CAO) and meeting Connection Approval Process (CAP) requirements.

**Rule ID:** `SV-251354r806017_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Every site must have a security policy to address filtering of the traffic to and from those connections. This documentation along with diagrams of the network topology is required to be submitted to the Connection Approval Process (CAP) for approval to connect to the NIPRNet or SIPRNet. SIPRNet connections must also comply with the documentation required by the Classified Connection Approval Office (CCAO) to receive the SIPRNet Interim Approval to Connect (IATC) or final Approval to Connect (ATC). Also any additional requirements must be met as outlined in the Interim Authority to Operate (IATO) or Authority to Operate (ATO) forms signed by the Authorizing Official (AO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology and interview the ISSO to verify that each external connection to the site's network has been validated and approved by the AO and CAO and that CAP requirements have been met. If there are any external connections that have not been validated and approved, this is a finding.

## Group: NET0131

**Group ID:** `V-251355`

### Rule: Prior to having external connection provisioned between enclaves, a Memorandum of Agreement (MOA) or Memorandum of Understanding (MOU) must be established.

**Rule ID:** `SV-251355r806020_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prior to establishing a connection with another activity, a Memorandum of Understanding (MOU) or Memorandum of Agreement (MOA) must be established between the two sites prior to connecting with each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology and interview the ISSO to verify that each external connection to the site's network has been validated and approved by the AO and CAO and that CAP requirements have been met. If there are any external connections that have not been validated and approved, this is a finding.

## Group: NET0135

**Group ID:** `V-251356`

### Rule: External connections to the network must be reviewed and the documentation updated semi-annually.

**Rule ID:** `SV-251356r806023_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A network is only as secure as its weakest link. It is imperative that all external connections be reviewed and kept to a minimum needed for operations. All external connections should be treated as untrusted networks. Reviewing who or what the network is connected to empowers the security manager to make sound judgements and security recommendations. Minimizing backdoor circuits and connections reduces the risk for unauthorized access to network resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology and interview the ISSO to verify that external connections to the network are reviewed and documented on a semi-annual basis. If there are any external connections that have not been documented, or if the connections are not reviewed on a semi-annual basis, this is a finding.

## Group: NET0168

**Group ID:** `V-251357`

### Rule: If the site has a non-DoD external connection (i.e. Approved Gateway), an Intrusion Detection and Prevention System (IDPS) must be located between the sites Approved Gateway and the perimeter router.

**Rule ID:** `SV-251357r806026_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The incorrect placement of the external IDPS may allow unauthorized access to go undetected and limit the ability of security personnel to stop malicious or unauthorized use of the network. In order to ensure that an attempted or existing attack goes unnoticed, the data from the sensors must be monitored continuously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the network topology and physical connectivity to verify compliance. If the site has a non-DoD external connection and does not have an IDPS located between the site's Approved Gateway and the perimeter router, this is a finding. Note: An Approved Gateway (AG) is any external connection from a DoD NIPRNet enclave to an Internet Service Provider, or network owned by a contractor, or non-DoD federal agency that has been approved by either the DoD CIO or the DoD Component CIO. This AG requirement does not apply to commercial cloud connections when the Cloud Service Provider (CSP) network is connected via the NIPRNet Boundary Cloud Access Point (BCAP).

## Group: NET0170

**Group ID:** `V-251358`

### Rule: External network connections must not bypass the enclaves perimeter security.

**Rule ID:** `SV-251358r806029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without taking the proper safeguards, external networks connected to the organization will impose security risks unless properly routed through the perimeter security devices. Since external networks to the organization are considered to be untrusted, this could prove detrimental since there is no way to verify traffic inbound or outbound on this backdoor connection. An attacker could carry out attacks or steal data from the organization without any notification. An external connection is considered to be any link from the organization's perimeter to the NIPRNet, SIPRNet, Commercial ISP, or other untrusted network outside the organization's defined security policy. The DREN and SREN are DoD's Research & Engineering Network. A DoD Network that is the official DoD long-haul network for computational scientific research, engineering, and testing in support of DoD's S&T and T&E communities. It has also been designated as a DoD IPv6 pilot network by the Assistant Secretary of Defense (Networks & Information Integration)/DoD Chief Information Officer ASD (NII)/DoD CIO. A DISN enclave should not have connectivity to the DREN unless approved by the AO and the requirements have been met for all external connections described in NET0130.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram and verify that ingress and egress traffic via external connections to the enclave do not bypass the enclave's perimeter security. If there are external connections to the enclave that bypass the enclaves' perimeter security, this is a finding.

## Group: NET0180

**Group ID:** `V-251359`

### Rule: All global address ranges used on unclassified and classified networks must be properly registered with the DoD Network Information Center (NIC).

**Rule ID:** `SV-251359r877974_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If network address space is not properly configured, managed, and controlled, the network could be accessed by unauthorized personnel resulting in security compromise of site information and resources. Allowing subscribers onto the network whose IP addresses are not registered with the .Mil NIC may allow unauthorized users access into the network. These unauthorized users could then monitor the network, steal passwords, and access classified information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validate global IP addresses in use on unclassified or classified networks registered through the DoD Network Information Center. For NIPRNet, go to the website https://www.nic.mil. For SIPRNet, go to the web portal at http://www.ssc.smil.mil. If the site is using an address space that has not been registered and allocated to the site, this is a finding.

## Group: NET0185

**Group ID:** `V-251360`

### Rule: Network Address Translation (NAT) and private IP address space must not be deployed within the SIPRNet enclave.

**Rule ID:** `SV-251360r808530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD has an enterprise level security-focused configuration management (SecCM) requirement to support end-to-end monitoring of SIPRNet, as a National Security System (NSS). The use of NAT and private IP address space inhibits the view of specialized DISN enterprise tools in tracking client level enclave to enclave traffic, monitoring client use of enterprise level application services, and detecting anomalies and potential malicious attacks in SIPRNet client application traffic flows. Enclave nodes that communicate outside the organization's enclave to other SIPRNet enclaves or enterprise services cannot use NATd private addresses via an enclave proxy without the permission of the SIPRNet DISN Authorizing Official, the DISA AO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review network diagrams, enterprise sensor reports, and network scans submitted to the Connection Approval Office. Determine that only global IP addresses assigned by the NIC are in use within the organization's SIPRNet enclave. NOTE: This requirement also applies to IPv6 ULA addresses. The IPv6 ULA is unauthorized on SIPR without approval. Determine whether NAT and unauthorized IP address space is in use in the organization's SIPRNet enclave. Exceptions to this requirement are listed below: 1. Closed classified networks logically transiting SIPRNet for enclave-to-enclave VPN transport only. 2. Out-of-Band management networks, where the NATd nodes do not access SIPRNet base enterprise services. 3. Thin client deployments where the hosting thin client server serves as the SIPRNet access point for its thin clients and that the organization maintains detailed thin client service usage audit logs. 4. Valid operational mission need or implementation constraints. All exceptions must have approval by the SIPRNet DISN accreditation official, DISA AO. If NAT and unauthorized IP address space is in use on the organization's SIPRNet infrastructure, this is a finding.

## Group: NET0198

**Group ID:** `V-251361`

### Rule: Dynamic Host Configuration Protocol (DHCP) audit and event logs must record sufficient forensic data to be stored online for thirty days and offline for one year.

**Rule ID:** `SV-251361r853649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to identify and combat IP address spoofing, it is highly recommended that the DHCP server logs MAC addresses and hostnames on the DHCP server, in addition to standard data such as IP address and date/time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DHCP audit and event logs include hostnames and MAC addresses of all clients, in addition to IP address and date/time. Also, validate logs are kept online for thirty days and offline for one year. If the logs do not include hostnames and MAC addresses along with the IP address and date/time, or if the logs are not kept online for thirty days and offline for one year, this is a finding.

## Group: NET0199

**Group ID:** `V-251362`

### Rule: Dynamic Host Configuration Protocol (DHCP) servers used within SIPRNet infrastructure must be configured with a minimum lease duration time of 30 days.

**Rule ID:** `SV-251362r853650_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to trace, audit, and investigate suspicious activity, DHCP servers within the SIPRNet infrastructure must have the minimum lease duration time configured to 30 or more days.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of SIPRNet DHCP servers to verify that the lease duration is set to a minimum of thirty days. If the lease duration is less than thirty days, this is a finding.

## Group: NET0210

**Group ID:** `V-251363`

### Rule: All network infrastructure devices must be located in a secure room with limited access.

**Rule ID:** `SV-251363r806044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If all communications devices are not installed within controlled access areas, risk of unauthorized access and equipment failure exists, which could result in denial of service or security compromise. It is not sufficient to limit access to only the outside world or non-site personnel. Not everyone within the site has the need-to-know or the need-for-access to communication devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the site to validate physical network components are in a secure environment with limited access. If there are any network components not located in a secure environment, this is a finding.

## Group: NET0346

**Group ID:** `V-251364`

### Rule: All hosted NIPRNet-only applications must be located in a local enclave Demilitarized Zone (DMZ).

**Rule ID:** `SV-251364r853651_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the protection of a DMZ, production networks will be prone to outside attacks as they are allowing externally accessible services to be accessed on the internal LAN. This can cause many undesired consequences such as access to the entire network, Denial of Service attacks, or theft of sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram and interview the ISSO to verify that all NIPRNet-only applications are located in a local enclave DMZ. If there are any NIPRNet-only applications not hosted in the enclave's DMZ, this is a finding.

## Group: NET0348

**Group ID:** `V-251365`

### Rule: All Internet-facing applications must be hosted in a DoD Demilitarized Zone (DMZ) Extension.

**Rule ID:** `SV-251365r806050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the protection of a DMZ, production networks will be prone to outside attacks as they are allowing externally accessible services to be accessed on the internal LAN. This can cause many undesired consequences such as access to the entire network, Denial of Service attacks, or theft of sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram and interview the ISSO to verify that all Internet-facing applications are hosted in a DoD DMZ Extension. If there are any Internet-facing applications hosted in the enclave's DMZ or private network, this is a finding.

## Group: NET0351

**Group ID:** `V-251366`

### Rule: When protecting the boundaries of a network, the firewall must be placed between the private network and the perimeter router and the Demilitarized Zone (DMZ).

**Rule ID:** `SV-251366r853652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The only way to mediate the flow of traffic between the inside network, the outside connection, and the DMZ is to place the firewall into the architecture in a manner that allows the firewall the ability to screen content for all three destinations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagrams and visually inspect the firewall location to validate correct position on the network. If the firewall is not positioned between the perimeter router and the private network and between the perimeter router and the DMZ, this is a finding. Exception: If the perimeter security for the enclave or B/C/P/S is provisioned via the JRSS, then this requirement is not applicable.

## Group: NET0365

**Group ID:** `V-251367`

### Rule: The organization must implement a deep packet inspection solution when protecting perimeter boundaries.

**Rule ID:** `SV-251367r806056_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Deep packet inspection (DPI) examines the packet beyond the Layer 4 header by examining the payload to identify the application or service. DPI searches for illegal statements, predefined criteria, malformed packets, and malicious code, thereby enabling the IA appliances to make a more informed decision on whether to allow or not allow the packet through. DPI engines can delve into application centric information to allow different applications to be protected in different ways from different threats. Examples of DPI appliances include next-generation firewalls, application layer gateways as well as specific gateways for web, email and SSL traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine which type of solution is used for deep packet inspection at the enclave boundary. Acceptable solutions for meeting this requirement are a deep packet inspection firewall, or a stateful packet inspection firewall in conjunction with any combination of application firewalls or application layer gateways. If the organization does not have any implementation of deep packet inspection protecting their network perimeter boundaries, this is a finding. Exception: If the perimeter security for the enclave or B/C/P/S is provisioned via the JRSS, then this requirement is not applicable.

## Group: NET0369

**Group ID:** `V-251368`

### Rule: A deny-by-default security posture must be implemented for traffic entering and leaving the enclave.

**Rule ID:** `SV-251368r853653_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent malicious or accidental leakage of traffic, organizations must implement a deny-by-default security posture at the network perimeter. Such rulesets prevent many malicious exploits or accidental leakage by restricting the traffic to only known sources and only those ports, protocols, or services that are permitted and operationally necessary. Applications, protocols, TCP/UDP ports, and endpoints (specific hosts or networks) are identified and used to develop rulesets and access control lists to restrict traffic to and from an enclave.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if a deny-by-default security posture has been implemented for both inbound and outbound traffic on the perimeter router or firewall. If a deny-by-default security posture has not been implemented at the network perimeter, this is a finding.

## Group: NET0445

**Group ID:** `V-251369`

### Rule: Two-factor authentication must be implemented to restrict access to all network elements.

**Rule ID:** `SV-251369r806062_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without secure management implemented with authenticated access controls, strong two-factor authentication, encryption of the management session and audit logs, unauthorized users may gain access to network managed devices compromised, large parts of the network could be incapacitated with only a few commands.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all network element configurations to ensure that an authentication server is being used. Then verify that a two-factor authentication method has been implemented. The RADIUS or TACACS server referenced in the configurations will call a two-factor authentication server. If two-factor authentication is not being used to access all network elements, this is a finding.

## Group: NET0810

**Group ID:** `V-251370`

### Rule: Two Network Time Protocol (NTP) servers must be deployed in the management network.

**Rule ID:** `SV-251370r806065_rule`
**Severity:** low

**Description:**
<VulnDiscussion>NTP provides an efficient and scalable method for managed network elements to actively synchronize to an accurate time source. Insuring that there are always NTP servers available to provide time is critical. It is imperative that all single points of failure for the NTP infrastructure are eliminated. Knowing the correct time is not only crucial for proper network functioning but also for security. Compromising an NTP server opens the door to more sophisticated attacks that include NTP poisoning, replay attacks, and denial of service. Where possible, deploy multiple gateways with diverse paths to the NTP servers. An alternative design is to have one server connected to a reference clock and the other server reference an external stratum-1 server. With this scenario, the NTP clients should be configured to prefer the stratum-1 server over the stratum-2 server. The NTP servers should be configured to easily scale by creating a hierarchy of lower level (stratum-2 to stratum-15) servers to accommodate the workload. The width and depth of the hierarchy is dependent on the number of NTP clients as well as the amount of redundancy that is required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology to determine that there are two NTP servers and what network they are connected to. Verify that they are both online according to the documented IP address. Where possible, deploy multiple gateways with diverse paths to the NTP servers. An alternative design is to have one server connected to a reference clock and the other server reference an external stratum-1 server. With this scenario, the NTP clients should be configured to prefer the stratum-1 server over the stratum-2 server. The NTP servers should be configured to easily scale by creating a hierarchy of lower level (stratum-2 to stratum-15) servers to accommodate the workload. The width and depth of the hierarchy is dependent on the number of NTP clients as well as the amount of redundancy that is required. If two NTP servers have not been deployed in the management network, this is a finding.

## Group: NET0928

**Group ID:** `V-251371`

### Rule: A policy must be implemented to keep Bogon/Martian rulesets up to date.

**Rule ID:** `SV-251371r806068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A Bogon route or Martian address is a type of packet that should never be routed inbound through the perimeter device. Bogon routes and Martian addresses are commonly found as the source addresses of DDoS attacks. By not having a policy implemented to keep these addresses up to date, the enclave will run the risk of allowing illegitimate traffic into the enclave or even blocking legitimate traffic. Also, if there are rulesets with "any" as the source address then Bogons/Martians must be applied. Bogons and Martian addresses can be kept up to date routinely checking the IANA website or creating an account with Team Cymru to retrieve these lists in one of many ways. http://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xml http://www.team-cymru.org/Services/Bogons/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Bogon/Martian maintenance policy to validate plans and procedures are in place to protect the enclave from illegitimate network traffic with up to date Bogon/Martian rulesets. If the site does not have a policy to keep Bogon/Martian rulesets up to date, this is a finding.

## Group: NET0998

**Group ID:** `V-251372`

### Rule: A dedicated management network must be implemented.

**Rule ID:** `SV-251372r806071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To deploy a management network for the purpose of controlling, monitoring, and restricting management traffic, a separate management subnet must be implemented. Define a large enough address block that will enable the management network to scale in proportion to the managed network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram to determine if a management network has been implemented. Validate the IP address space documented for this network by verifying the IP addresses referenced for management access (SSH, NTP, AAA, SNMP manager, Syslog server, etc.) to the managed network elements. If a management network has not been implemented, this is a finding.

## Group: NET1025

**Group ID:** `V-251373`

### Rule: A minimum of two syslog servers must be deployed in the management network.

**Rule ID:** `SV-251373r916119_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, understand past intrusions, troubleshoot service disruptions, and react to probes and scans of the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology and verify that at least two syslog servers are located within the management network. Note the IP addresses as documented on the management network topology and verify that this is what is configured on the network elements as the host devices for sending syslog data. If a minimum of two syslog servers have not been deployed in the management network, this is a finding.

## Group: NET1026

**Group ID:** `V-251374`

### Rule: Syslog messages must be retained for a minimum of 30 days online and then stored offline for one year.

**Rule ID:** `SV-251374r806077_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Logging is a critical part of router security. Maintaining an audit trail of system activity logs (syslog) can help identify configuration errors, understand past intrusions, troubleshoot service disruptions, and react to probes and scans of the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the syslog server to verify that it is configured to store messages for at least 30 days. Have the administrator show you the syslog files stored offline for one year. If the syslog messages are not kept online for thirty days and offline for one year, this is a finding.

## Group: NET1040

**Group ID:** `V-251375`

### Rule: Current and previous network element configurations must be stored in a secured location.

**Rule ID:** `SV-251375r853654_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the network element's non-volatile memory is lost without a recent configuration stored in an offline location, it may take time to recover that segment of the network. Users connected directly to the switch or router will be without service for a longer than acceptable time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At a minimum, a copy of the current and previous network element configurations must be saved. Storage can take place on a classified network, OOB network, or offline. If the current and previous network element configurations are not stored in a secured location, this is a finding.

## Group: NET1050

**Group ID:** `V-251376`

### Rule: The organization must encrypt all network device configurations while stored offline.

**Rule ID:** `SV-251376r853655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a network device's non-volatile memory is lost without a recent configuration stored in an offline location, it may take time to recover that segment of the network. Users connected directly to the switch or router will be without service for a longer than acceptable time. Encrypting the configuration stored offline protects the data at rest and provides additional security to prevent tampering and potentially cause a network outage if the configuration were to be put into service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the network element configurations that have been stored offline. If the configurations are not encrypted, this is a finding.

## Group: NET1622

**Group ID:** `V-251377`

### Rule: An Out-of-Band (OOB) management network must be deployed or 24x7 personnel must have console access for device management.

**Rule ID:** `SV-251377r808534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>From an architectural point of view, providing Out-Of-Band (OOB) management of network systems is the best first step in any management strategy. No production traffic resides on an out-of-band network. The biggest advantage to implementation of an OOB network is providing support and maintenance to the network that has become degraded or compromised. During an outage or degradation period the in band management link may not be available. The consequences of loss of availability is unacceptable and could include the immediate and sustained loss of mission effectiveness. Maintenance support for key IT assets must be available to respond 24x7 immediately upon failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology and verify that an OOB network provides connectivity from the management network to all of the managed network elements. If an OOB network has not been deployed, verify that the network administrators have management access via the console to the managed network elements. If there is no OOB network or if network administrators do not have management access via the console to the managed network elements, this is a finding.

## Group: NET1815

**Group ID:** `V-251378`

### Rule: All Releasable Local Area Network (REL LAN) environments must be documented in the System Security Authorization Agreement (SSAA).

**Rule ID:** `SV-251378r806089_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ISSM will ensure Releasable Local Area Network (REL LAN) environments are documented in the SSAA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSM and review the SSAA. GRE tunnels found on a premise or edge SIPRNet router that have an endpoint within the REL IP address space must be documented in the SSAA. If the REL LAN has not been documented in the SSAA, this is a finding.

## Group: NET1816

**Group ID:** `V-251379`

### Rule: Annual reviews must be performed on all Releasable Local Area Network (REL LAN) environments.

**Rule ID:** `SV-251379r806092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ISSM will ensure Releasable Local Area Network (REL LAN) reviews are performed annually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the ISSM disclose documentation that a REL LAN review has been performed annually. If annual reviews are not being performed, this is a finding.

## Group: NET1826

**Group ID:** `V-251380`

### Rule: Enabling a connection that extends DISN IP network connectivity (e.g., NIPRNet and SIPRNet) to any DoD Vendor, Foreign, or Federal Mission Partner enclave or network without a signed DoD CIO approved sponsorship memo is prohibited. For classified connectivity it must be to a DSS approved contractor facility or DoD Component approved foreign government facility.

**Rule ID:** `SV-251380r806095_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Having a circuit provisioned that connects the SIPRNet enclave to a non-DoD, foreign, or contractor network puts the enclave and the entire SIPRNet at risk. If the termination point is not operated by the government, there is no control to ensure that the network element at the remote facility is not compromised or connected to another network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the topology diagram of the classified network. If there are any leased circuits connecting to DoD Vendor, Foreign, or Federal Mission Partner enclave or network without a signed DoD CIO-approved sponsorship memo, this is a finding. If classified connectivity is not to a DSS-approved contractor facility or DoD Component-approved foreign government facility, this is a finding.

## Group: NET1827

**Group ID:** `V-251381`

### Rule: Command and Control (C2) and non-C2 exceptions of SIPRNet must be documented in the enclaves accreditation package and an Authority to Connect (ATC) or Interim ATC  amending the connection approval received prior to implementation.

**Rule ID:** `SV-251381r806098_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any exception to use SIPRNet must be documented in an update to the enclave's accreditation package and an Authority to Connect (ATC) or Interim ATC amending the connection approval received prior to implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review SIPRNet accreditation package and an Interim Authority to Connect/Authority to Connect (IATC/ATC) amending the connection approval received. If C2 and non-C2 exceptions are not documented, this is a finding.

## Group: NET1832

**Group ID:** `V-251382`

### Rule: VPN gateways used to create IP tunnels to transport classified traffic across an unclassified IP network must comply with appropriate physical security protection standards for processing classified information.

**Rule ID:** `SV-251382r806101_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When transporting classified data over an unclassified IP network, it is imperative that the network elements deployed to provision the encrypted tunnels are located in a facility authorized to process the data at the proper classification level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram. If there is a connection between the classified network and the unclassified network for the purpose of tunneling classified traffic across the unclassified IP network, verify that the IPsec VPN gateway used to provision the tunnel is compliant with appropriate physical security protection standards for processing classified information. If appropriate physical security protection has not been enforced, this is a finding.

## Group: NET2000

**Group ID:** `V-251383`

### Rule: Multi-Protocol Labeled Switching (MPLS) protocols deployed to build Label-Switch Path (LSP) tunnels must authenticate all messages with a hash function using the most secured cryptographic algorithm available.

**Rule ID:** `SV-251383r806104_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Spoofed TCP segments could be introduced into the connection streams for LDP sessions used to build LSPs. By configuring strict authentication between LSR peers, LDP TCP sessions can be restricted and the integrity of LSPs can be guarded using the TCP MD5 Signature Option. The LSR ignores LDP Hellos from any LSR for which a password has not been configured. This ensures that the LSR establishes LDP TCP connections only with LSRs for which the shared secret has been configured. RSVP messages are used to control resource reservations for MPLS TE tunnels inside the MPLS core. The RSVP message authentication permits neighbors to use a secure hash to digitally sign all RSVP signaling messages, thus allowing the receiver of an RSVP message to verify the sender. By protecting against corruption and spoofing of RSVP messages, the integrity of the LSPs for bandwidth provisioning, path setup, and path teardown is maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if LDP and RSVP messages are being authenticated as shown in the examples below. If authentication is not being used for these protocols using a secured hashing algorithm for message authentication, this is a finding. An LDP session is secured by configuring a password for each LDP peer as shown in the example below: mpls ip mpls label protocol ldp mpls ldp neighbor 10.1.1.1 password xzxxxxxxxxxxx mpls ldp neighbor 10.3.3.3 password xxxxxzzzzxxxz The IP address 10.1.1.1 and 10.3.3.3 in this example are the router IDs of the neighbors for which this router has an LDP session requiring MD5 authentication. To specify that the router ID 10.1.1.1 is to be found in VPN routing/forwarding instance (VRF) named VPN1 instead of the global route table, the "vrf" keyword is used in the command as shown in the following example: mpls ldp neighbor vrf VPN1 10.1.1.1 password xxxxxxxxxxxxxxxxx A group of peers using the same MD5 password can be configured as shown in the example below: mpls ldp password for 10 xxxxxxxxxxxxxxx mpls ldp password required for 10 ! access-list 10 permit 10.1.1.1 access-list 10 permit 10.3.3.3 access-list 10 permit 10.4.4.4 The access list specifies a password is mandatory for LDP sessions with neighbors whose LDP router IDs are permitted by the access list. To configure MD5 or SHA-1 authentication for RSVP, both ip rsvp authentication key and ip rsvp authentication commands must be configured as shown in the example below. The latter command simply enables authentication. interface Ethernet0/0 ip address 192.168.101.2 255.255.255.0 ip rsvp bandwidth 7500 7500 ip rsvp authentication type sha-1 ip rsvp authentication key xxxxxxxx ip rsvp authentication Note: If SHA-1 is not specified using the ip rsvp authentication type command, MD5 will be utilized.

## Group: NET2001

**Group ID:** `V-251384`

### Rule: Multi-Protocol Labeled Switching (MPLS) labels must not be exchanged between the enclaves edge routers and any external neighbor routers.

**Rule ID:** `SV-251384r806107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MPLS label exchange via Label Distribution Protocol (LDP) or Resource Reservation Protocol (RSVP) with any external neighbor creates the risk of label spoofing that could disrupt optimum routing, or even drop packets that are encapsulated with a label that is not in the MPLS forwarding table.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DISN-facing interfaces of the enclave perimeter routers to verify that LDP or RSVP is not enabled. If any of these interfaces are LDP or RSVP enabled, this is a finding.

## Group: NET2002

**Group ID:** `V-251385`

### Rule: Label Distribution Protocol (LDP) must be synchronized with the Interior Gateway Protocol (IGP) to minimize packet loss when an IGP adjacency is established prior to LDP peers completing label exchange.

**Rule ID:** `SV-251385r806110_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Packet loss can occur when an IGP adjacency is established and the router begins forwarding packets using the new adjacency before the LDP label exchange completes between the peers on that link. Packet loss can also occur if an LDP session closes and the router continues to forward traffic using the link associated with the LDP peer rather than an alternate pathway with a fully synchronized LDP session. The MPLS LDP-IGP Synchronization feature provides a means to synchronize LDP with OSPF or IS-IS to minimize MPLS packet loss. When an IGP adjacency is established on a link but LDP-IGP synchronization is not yet achieved or is lost, the IGP will advertise the max-metric on that link.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and verify that the "mpls ldp sync" command is configured on the IS-IS or OSPF configuration as shown in the following example: mpls ip mpls label protocol ldp ! interface POS0/3 ip router isis mpls ip ... ... ... router isis mpls ldp sync If not all MPLS routers synchronize IGP and LDP, this is a finding. Note: If the LDP peer is reachable, the IGP waits indefinitely (by default) for synchronization to be achieved. To limit the length of time the IGP session must wait, enter the "mpls ldp igp sync holddown" command. If the LDP peer is not reachable, the IGP establishes the adjacency to enable the LDP session to be established.

## Group: NET2004

**Group ID:** `V-251386`

### Rule: Rapid Spanning Tree Protocol (STP) must be implemented at the access and distribution layers where Virtual Local Area Networks (VLANs) span multiple switches.

**Rule ID:** `SV-251386r806113_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) is implemented on bridges and switches to prevent Layer 2 loops when a broadcast domain spans multiple bridges and switches and when redundant links are provisioned to provide high availability in case of link failures. Convergence time can be significantly reduced using Rapid STP (802.1w) instead of STP (802.1d), resulting in improved availability. Rapid STP should be deployed by implementing either Rapid Per-VLAN-Spanning-Tree (Rapid-PVST) or Multiple Spanning-Tree Protocol (MSTP), the later scales much better when there are many VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In cases where VLANs do not span multiple switches it is a best practice to not implement STP. Avoiding the use of STP will provide the most deterministic and highly available network topology. If STP is required, then review the switch configuration to verify that RSTP or MSTP has been implemented. Following are example configurations: RSTP spanning-tree mode rapid-pvst MST spanning-tree mode mst spanning-tree mst configuration name Region1 revision 1 instance 1 vlan 10, 11, 12 instance 2 vlan 13, 14 If RSTP or MSTP has not been implemented where STP is required, this is a finding. Note: Note: Cisco has implemented RSTP as part of MSTP and Rapid-PVST+.

## Group: NET2005

**Group ID:** `V-251387`

### Rule: A Quality of Service (QoS) policy must be implemented to provide preferred treatment for Command and Control (C2) real-time services and control plane traffic.

**Rule ID:** `SV-251387r806116_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Different applications have unique requirements and toleration levels for delay, jitter, packet loss, and availability. To manage the multitude of applications and services, a network requires a Quality of Service (QoS) framework to differentiate traffic and provide a method to manage network congestion. The Differentiated Services Model (DiffServ) is based on per-hop behavior by categorizing traffic into different classes and enabling each node to enforce a forwarding treatment to each packet as dictated by a service policy. Packet markings such as IP Precedence and its successor, Differentiated Services Code Points (DSCP), were defined along with specific per-hop behaviors for key traffic types to enable a scalable QoS solution. DiffServ QoS categorizes network traffic, prioritizes it according to its relative importance, and provides priority treatment based on the classification. It is imperative that end-to-end QoS is implemented to guarantee the required bandwidth for control plane traffic and C2 real-time services during periods of congestion within the JIE WAN IP network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review each router and verify that a QoS policy has been configured to provide preferred treatment for control plane traffic and C2 real-time services. Step 1: Verify that the class-maps are configured to match on DSCP values that have been set at the edges as shown in the configuration example below: class-map match-all CONTROL_PLANE match ip dscp 48 class-map match-all C2_VOICE match ip dscp 47 class-map match-all VOICE match ip dscp ef class-map match-all VIDEO match ip dscp af4 class-map match-all PREFERRED_DATA match ip dscp af3 Step 2: Verify that the policy map applied to the core-layer-facing interface reserves the bandwidth for each traffic type as shown in the following example: policy-map QOS_POLICY class CONTROL_PLANE priority percent 10 class C2_VOICE priority percent 10 class VOICE priority percent 15 class VIDEO bandwidth percent 25 class PREFERRED_DATA bandwidth percent 25 class class-default bandwidth percent 15 Step 3: Verify that an output service policy is bound to the core-layer-facing interface as shown in the configuration example below: interface GigabitEthernet1/1 ip address 10.2.0.2 255.255.255.252 service-policy output QOS_POLICY If a QoS policy has not been implemented within the JIE WAN infrastructure to provide assured services for control plane traffic and C2 real-time services, this is a finding.

## Group: NET2006

**Group ID:** `V-251388`

### Rule: Protocol Independent Multicast (PIM) must be disabled on all router interfaces that are not required to support multicast routing.

**Rule ID:** `SV-251388r806119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PIM is a routing protocol that is used by the IP core for forwarding multicast traffic. PIM operates independent of any particular IP routing protocol but makes use of the IP unicast routing table--PIM does not keep a separate multicast routing table. The multicast tree is built by first allowing a flood of traffic from the source to every dense mode router in the network. For a brief time, unnecessary traffic is allowed. As each router receives traffic for the group, it will decide whether it has active recipients wanting to receive the multicast data. If so, the router will let the flow continue. If no hosts have registered for the multicast group, the router sends a prune message to its neighbor toward the source. That branch of the tree is then pruned off so that the unnecessary traffic does not continue. Dense mode is viewed as a "flood and prune" implementation. With PIM Sparse Mode (PIM-SM), the multicast tree is not extended to a router unless a local host has already joined the group. The multicast tree is built by beginning with group members at the end leaf nodes and extending back toward a central root point--the tree is built from the bottom up. In either case, if an interface is not going to be supporting any of the multicast traffic--that is, join a multicast tree, PIM should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, multicast is disabled globally as well as on all interfaces. Multicast routing is enabled on a router with the global command ip multicast-routing. PIM is enabled on an interface with either of the following commands: ip pim sparse-mode, ip pim dense-mode, ip pim sparse-dense-mode. If the global command ip multicast-routing is defined, review all interface configurations and verify that only the required interfaces are enabled for PIM. The following is a sample configuration with multicast routing enabled and PIM enabled on an interface. ip multicast-routing ! interface FastEthernet0/0 ip pim sparse-mode If PIM is not disabled on interfaces that are not supporting multicast, this is a finding.

## Group: NET2007

**Group ID:** `V-251389`

### Rule: A Protocol Independent Multicast (PIM) neighbor filter must be implemented to restrict and control multicast traffic.

**Rule ID:** `SV-251389r806122_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Protocol Independent Multicast (PIM) is a routing protocol that is used by the IP core for forwarding multicast traffic. PIM traffic must be limited to only known PIM neighbors by configuring and binding a PIM neighbor filter to those interfaces that have PIM enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify that an ACL is configured that will specify the allowable PIM neighbors similar to the following example. ip access-list standard pim-neighbors permit 192.0.2.1 permit 192.0.2.3 Step 2: Verify that a pim neighbor-filter command is configured on all PIM enabled interfaces that is referencing the PIM neighbor ACL similar to the following example: interface GigabitEthernet0/3 ip address 192.0.2.2 255.255.255.0 pim neighbor-filter pim-neighbors If PIM neighbor filter is not bound to interfaces that have PIM enabled, this is a finding.

## Group: NET2008

**Group ID:** `V-251390`

### Rule: The multicast domain must block inbound and outbound administratively-scoped multicast traffic at the edge.

**Rule ID:** `SV-251390r806125_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A multicast boundary must be established to ensure that administratively-scoped multicast traffic does not flow into or out of the IP core. The multicast boundary can be created by ensuring that COI-facing interfaces on all PIM routers are configured to block inbound and outbound administratively-scoped multicast traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The administratively-scoped IPv4 multicast address space is 239.0.0.0 through 239.255.255.255. Packets addressed to administratively-scoped multicast addresses must not cross administrative boundaries. This can be accomplished by applying a multicast boundary statement to all COI-facing interfaces as shown in the following example: ip multicast-routing ! interface FastEthernet0/0 ip address 199.36.92.1 255.255.255.252 ip pim sparse-mode ip multicast boundary 1 ! access-list 1 deny 239.0.0.0 0.255.255.255 access-list 1 permit any If inbound and outbound administratively-scoped multicast traffic is not blocked, this is a finding.

## Group: NET2009

**Group ID:** `V-251391`

### Rule: The multicast domain must block inbound and outbound Auto-RP discovery and announcement messages at the edge.

**Rule ID:** `SV-251391r806128_rule`
**Severity:** low

**Description:**
<VulnDiscussion>With static RP, the RP address for any multicast group must be consistent across all routers in a multicast domain. A static configuration is simple and convenient. However, if the statically defined RP router becomes unreachable, there is no automatic failover to another RP router. Auto-RP distributes information to routers as to which RP address must be used for various multicast groups. Auto-RP eliminates inconsistencies and enables scalability and automatic failover. All PIM-enabled routers join the RP discovery group (224.0.1.40), which allows them to receive all group-to-RP mapping information. This information is distributed by an entity called RP mapping agent. Mapping agents themselves join the RP announce group (224.0.1.39). All candidate RPs advertise themselves periodically using the RP announce group address. The mapping agent listens to all RP candidate announcements and determines which routers will be used for each multicast group. It then advertises the RP and its associate multicast groups to all PIM routers in the network using an RP discovery message. Auto-RP announcement and discovery messages provide information (i.e., IP addresses of the RP candidates, multicast groups, etc.) vital to the multicast domain and should not be leaked out of the multicast domain. Using this information, a malicious user could disrupt multicast services by attacking the RP or flooding bogus traffic destined to the learned multicast groups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To prevent Auto-RP messages from entering or leaving the PIM domain, the ip multicast boundary command must be configured on a COI-facing PIM-enabled interface. Verify that the referenced ACL denies multicast addresses 224.0.1.39 and 224.0.1.40, as shown in the example below: ip multicast-routing ! interface FastEthernet0/0 ip address 199.36.92.1 255.255.255.252 ip pim sparse-mode ip multicast boundary 1 ! access-list 1 deny 224.0.1.39 access-list 1 deny 224.0.1.40 If COI-facing interfaces do not block inbound and outbound Auto-RP discovery and announcement messages, this is a finding.

## Group: NET2010

**Group ID:** `V-251392`

### Rule: Protocol Independent Multicast (PIM) register messages received from a downstream multicast Designated Routers (DR) must be filtered for any reserved or any other undesirable multicast groups.

**Rule ID:** `SV-251392r806131_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Customer networks that do not maintain a multicast domain and only require the IP multicast service will be required to stand up a PIM-SM router that will be incorporated into the JIE shared tree structure by establishing a peering session with an RP router. Both of these implementations expose several risks that must be mitigated to provide a secured IP core network. All RP routers that are peering with customer PIM-SM routers must implement a PIM import policy to block multicast registration requests for reserved or any other undesirable multicast groups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the RP router is configured to filter PIM register messages using the ip pim accept-register global command as shown in the example below. This command can reference either an ACL or a route-map to identify and prevent unauthorized sources or groups from registering with the RP. ip pim accept-register list PIM_REGISTER_FILTER ! ip access-list extended PIM_REGISTER_FILTER deny ip any 224.0.0.0 0.0.0.255 deny ip 0.0.0.0 0.255.255.255 any deny ip 1.0.0.0 0.255.255.255 any deny ip 2.0.0.0 0.255.255.255 any deny ip 5.0.0.0 0.255.255.255 any deny ip 7.0.0.0 0.255.255.255 any deny ip 10.0.0.0 0.255.255.255 any deny ip 23.0.0.0 0.255.255.255 any deny ip 27.0.0.0 0.255.255.255 any ... ... ... deny ip 172.16.0.0 0.15.255.255 any deny ip 192.168.0.0 0.0.255.255 any deny ip 197.0.0.0 0.255.255.255 any deny ip 223.0.0.0 0.255.255.255 any deny ip 224.0.0.0 224.255.255.255 any permit ip any any If the RP router peering with customer PIM-SM routers is not configured with a PIM import policy to block registration messages for reserved multicast groups, this is a finding.

## Group: NET2011

**Group ID:** `V-251393`

### Rule: Protocol Independent Multicast (PIM) join messages received from a downstream multicast Designated Routers (DR) must be filtered for any reserved or any other undesirable multicast groups.

**Rule ID:** `SV-251393r806134_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Customer networks that do not maintain a multicast domain and only require the IP multicast service will be required to stand up a PIM-SM router that will be incorporated into the JIE shared tree structure by establishing a peering session with an RP router. Both of these implementations expose several risks that must be mitigated to provide a secure IP core network. All RP routers that are peering with customer PIM-SM routers must implement a PIM import policy to block multicast join requests for reserved or any other undesirable multicast groups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the RP router is configured to filter PIM join messages for any reserved multicast groups using the ip pim accept-rp global command as shown in the example below. The ip pim accept-rp global command causes the router to accept only (*, G) join messages destined for the specified RP address as allowed by the referenced access-list. ip pim accept-rp 10.10.2.1 PIM_JOIN_FILTER ! ip access-list standard PIM_JOIN_FILTER deny 224.0.1.2 deny 224.0.1.3 deny 224.0.1.8 deny 224.0.1.22 deny 224.0.1.24 deny 224.0.1.25 ... ... ... deny 225.1.2.3 deny 229.55.150.208 deny 234.42.42.42 255.255.255.252 deny 239.0.0.0 0.255.255.255 permit any Note: IOS 12.4T extends the ip multicast-routing command with a group-range or access-list argument that can be used to filter multicast control (PIM, IGMP) and data packets for unauthorized groups. If the RP router peering with customer PIM-SM routers is not configured with a PIM import policy to block join messages for reserved and any undesirable multicast groups, this is a finding.

## Group: NET2012

**Group ID:** `V-251394`

### Rule: Multicast register messages must be rate limited per each source-group (S, G) entry.

**Rule ID:** `SV-251394r853656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a new source starts transmitting in a PIM Sparse Mode network, the DR will encapsulate the multicast packets into register messages and forward them to the Rendezvous Point (RP) using unicast. This process can be taxing on the CPU for both the DR and the RP if the source is running at a high data rate and there are many new sources starting at the same time. This scenario can potentially occur immediately after a network failover. The rate limit for the number of register messages should be set to a relatively low value based on the known number of multicast sources within the multicast domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the DR to verify that it is rate limiting the number of multicast register messages. If the DR is not limiting multicast register messages, this is a finding. The following is a PIM sparse mode configuration example that limits the number of register messages for each (S, G) multicast entry to 10 per second. ip multicast-routing ! interface FastEthernet 0/0 description link to core ip address 192.168.123.2 255.255.255.0 ip pim sparse-mode ! interface FastEthernet 0/1 description User LAN ip address 192.168.122.1 255.255.255.0 ip pim sparse-mode ! ip pim rp-address 1.1.1.1 ip pim register-rate 10

## Group: NET2013

**Group ID:** `V-251395`

### Rule: Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) report messages must be filtered to allow hosts to join only those multicast groups that have been approved by the organization.

**Rule ID:** `SV-251395r806140_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (e.g., someone doing a file download here or there), whereas multicast can have broader impact on bandwidth consumption resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups that hosts are allowed to join via IGMP (IPv4) or MLD (IPv6).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the DR to verify that it is filtering IGMP or MLD report messages allowing hosts to only join those groups that have been approved by the organization. If the DR is not filtering IGMP or MLD report messages, this is a finding. The following is a PIM sparse mode configuration example filtering specific multicast groups as defined in access-list 11 on the LAN-facing interface. ip multicast-routing ! interface FastEthernet 0/0 description link to core ip address 192.168.123.2 255.255.255.0 ip pim sparse-mode ! interface FastEthernet 0/1 description User LAN ip address 192.168.122.1 255.255.255.0 ip pim sparse-mode ip igmp access-group 11 ! access-list 11 permit 224.10.10.0 0.0.0.255 access-list 11 permit 224.11.11.0 0.0.0.255 access-list 11 permit 224.20.20.0 0.0.0.255

## Group: NET2014

**Group ID:** `V-251396`

### Rule: The number of mroute states resulting from Internet Group Management Protocol (IGMP) or Multicast Listener Discovery (MLD) membership reports must be limited.

**Rule ID:** `SV-251396r853657_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The current multicast paradigm can let any host join any multicast group at any time by sending an Internet Group Management Protocol (IGMP) or Multicast Listener Discovery (MLD) membership report to the Designated Router (DR). In a PIM Sparse Mode network, the DR will send a PIM Join message for the group to the Rendezvous Point (RP). Without any form of admission control, this can pose a security risk to the entire multicast domain, specifically the multicast routers along the shared tree from the DR to the RP that must maintain the mroute state information for each group join request. Hence, it is imperative that the DR is configured to limit the number of mroute state information that must be maintained to mitigate the risk of IGMP (IPv4) or MLD (IPv6) flooding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DR configuration to verify that it is limiting the number of mroute states via IGMP or MLD. If the DR is not limiting multicast join requests via IGMP or MLD, this is a finding. The following is a PIM sparse mode DR configuration example that limits the number of IGMP join requests on both a global and a per-interface basis ip multicast-routing ip igmp limit 80 ! interface FastEthernet 0/1 description User LAN121 ip address 192.168.122.1 255.255.255.0 ip pim sparse-mode ip igmp limit 50 ! interface FastEthernet 0/2 description User LAN122 ip address 192.168.122.1 255.255.255.0 ip pim sparse-mode ip igmp limit 50 Note: If both global and per interface state limiters are configured, the limits configured for per interface state limiters are still enforced but are constrained by the global limit.

## Group: NET2015

**Group ID:** `V-251397`

### Rule: The number of source-group (SG) states must be limited within the multicast topology where Any Source Multicast (ASM) is deployed.

**Rule ID:** `SV-251397r853658_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any Source Multicast (ASM) can have many sources for the same groups (many-to-many). For many receivers, the path via the Rendezvous Point (RP) may not be ideal compared with the shortest path from the source to the receiver. By default, the last-hop router will initiate a switch from the shared tree to a source-specific shortest-path tree (SPT) to obtain lower latencies. This is accomplished by the last-hop router sending an (S, G) PIM Join towards S (the source). When the last-hop router begins to receive traffic for the group from the source via the SPT, it will send a PIM Prune message to the RP for the (S, G). The RP will then send a Prune message towards the source. The SPT switchover becomes a scaling issue for large multicast topologies that have many receivers and many sources for many groups because (S, G) entries require more memory than (*, G). Hence, it is imperative to minimize the amount of (S, G) state to be maintained by increasing the threshold that determines when the SPT switchover occurs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the multicast last-hop router configuration to verify that the SPT switchover threshold is increased (default is 0) or set to infinity (never switch over). The following is a PIM sparse mode last-hop router configuration example that will disable the SPT switchover for all multicast groups: ip multicast-routing ip pim spt-threshold infinity If any multicast router is not configured to increase the SPT threshold or set it to infinity to minimalize (S,G) state, this is a finding.

## Group: NET2016

**Group ID:** `V-251398`

### Rule: Internet Group Management Protocol (IGMP) or Multicast Listener Discovery (MLD) snooping must be implemented within the network access layer.

**Rule ID:** `SV-251398r853659_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The last-hop router sends the multicast packet out the interface towards the LAN containing interested receivers. The default behavior for a Layer 2 switch is to forward all multicast traffic out every access switch port that belongs to the VLAN. IGMP snooping is a mechanism used by "Layer 3 aware" switches to maintain a Layer 2 multicast table by examining all IGMP join and leave messages (destined to the all router's multicast address 224.0.0.2) sent between hosts and the multicast routers on the LAN. This will enable the switch to only forward multicast packets out the access switch ports that have connected hosts that have subscribed to the multicast group, thereby reducing the load on the switching backplane as well as eliminating unwanted traffic to uninterested hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the access switches connected to multicast last-hop routers to determine if IGMP snooping is enabled. The following are switch configuration examples with IGMP snooping enabled globally and on a per-VLAN basis: Enable IGMP Snooping globally: ip igmp snooping Enable IGMP Snooping for VLAN: ip igmp snooping vlan 7 If any switches within the ICAN access layer do not have IGMP or MLD snooping enabled, this is a finding.

## Group: NET2017

**Group ID:** `V-251399`

### Rule: First-hop redundancy services must be configured to delay any preempt to provide enough time for the Internet Gateway Protocol (IGP) to stabilize.

**Rule ID:** `SV-251399r806152_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Layer 2 connection between the nodes providing first-hop redundancy comes up quickly. If the preemption takes effect prior to the routing protocol converging, traffic is black holed. Traffic will go to the active router that does not have full routing information. It may take several seconds for the IGP to exchange all the routes, longer than the Hot Standby Router Protocol (HSRP), Virtual Router Redundancy Protocol (VRRP), or Gateway Load Balancing Protocol (GLPB) transition. The recommended practice is to delay the preemption action until after the IGP has a chance to stabilize.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All routers or multilayer switches providing first-hop redundancy services must be configured to delay preemption to provide enough time for the IGP to stabilize. Review the router or multilayer switch providing first-hop redundancy services and verify that the preemption delay is configured. If preemption delay is not configured, this is a finding. Following is an HSRP configuration example that delays the preemption by 30 seconds. interface GigabitEthernet 0/0/0 ip address 10.11.0.2 255.255.255.0 standby 1 priority 110 standby 1 ip 10.21.0.1 standby 1 preempt standby 1 preempt delay minimum 30 Following is a VRRP configuration example that delays the preemption by 30 seconds. interface GigabitEthernet 0/0/0 ip address 10.11.0.2 255.255.255.0 vrrp 1 priority 110 vrrp 1 ip 10.21.0.1 vrrp 1 preempt delay minimum 30 For VRRP implementations, a preemptive scheme is enabled by default. If preemption is disabled using the no vrrp preempt command, the virtual router backup that is elected to become virtual router master remains the master until the original virtual router master recovers and becomes master again.

