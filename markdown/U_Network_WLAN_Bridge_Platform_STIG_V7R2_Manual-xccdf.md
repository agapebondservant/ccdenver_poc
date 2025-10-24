# STIG Benchmark: Network WLAN Bridge Platform Security Technical Implementation Guide

---

**Version:** 7

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000512

**Group ID:** `V-243227`

### Rule: WLAN SSIDs must be changed from the manufacturer's default to a pseudo random word that does not identify the unit, base, organization, etc.

**Rule ID:** `SV-243227r720136_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An SSID identifying the unit, site, or purpose of the WLAN or that is set to the manufacturer default may cause an OPSEC vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration. 1. Obtain the SSID using a wireless scanner or the AP or WLAN controller management software. 2. Verify the name is not meaningful (e.g., site name, product name, room number, etc.) and is not set to the manufacturer's default value. If the SSID does not meet the requirement listed above, this is a finding.

## Group: SRG-NET-000063

**Group ID:** `V-243228`

### Rule: WLAN components must be Wi-Fi Alliance certified with WPA2 or WPA3.

**Rule ID:** `SV-243228r720139_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Wi-Fi Alliance certification ensures compliance with DoD interoperability requirements between various WLAN products.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the WLAN equipment specification and verify it is Wi-Fi Alliance certified with either the older WPA2 certification or the newer WPA3 certification. WPA3 is preferred but not required at this time. If the WLAN equipment is not Wi-Fi Alliance certified with WPA2 or WPA3, this is a finding.

## Group: SRG-NET-000151

**Group ID:** `V-243229`

### Rule: WLAN components must be FIPS 140-2 or FIPS 140-3 certified and configured to operate in FIPS mode.

**Rule ID:** `SV-243229r891323_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DoD WLAN components (WLAN AP, controller, or client) are not NIST FIPS 140-2/FIPS 140-3 (Cryptographic Module Validation Program, CMVP) certified, the WLAN system may not adequately protect sensitive unclassified DoD data from compromise during transmission.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the WLAN equipment specification and verify it is FIPS 140-2/3 (CMVP) certified for data in transit, including authentication credentials. Verify the component is configured to operate in FIPS mode. If the WLAN equipment is not is FIPS 140-2/3 (CMVP) certified or is not configured to operate in FIPS mode, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-243230`

### Rule: Wireless access points and bridges must be placed in dedicated subnets outside the enclave's perimeter.

**Rule ID:** `SV-243230r720145_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an adversary is able to compromise an access point or controller that is directly connected to an enclave network, the adversary can easily surveil and attack other devices from that beachhead. A defense-in-depth approach requires an additional layer of protection between the WLAN and the enclave network. This is particularly important for wireless networks, which may be vulnerable to attack from outside the physical perimeter of the facility or base given the inherent nature of radio communications to penetrate walls, fences, and other physical boundaries. Wireless access points and bridges must not be directly connected to the enclave network. A network device must separate wireless access from other elements of the enclave network. Sites must also comply with the Network Infrastructure STIG configuration requirements for DMZ, VLAN, and VPN configurations, as applicable. Examples of acceptable architectures include placing access points or controllers in a screened subnet (e.g., DMZ separating intranet and wireless network) or dedicated virtual LAN (VLAN) with ACLs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review network architecture with the network administrator. 1. Verify compliance by inspecting the site network topology diagrams. 2. Since many network diagrams are not kept up to date, walk through the connections with the network administrator using network management tools or diagnostic commands to verify the diagrams are current. If the site's wireless infrastructure, such as access points and bridges, is not isolated from the enclave network, this is a finding.

## Group: SRG-NET-000205

**Group ID:** `V-243231`

### Rule: The network device must be configured to only permit management traffic that ingresses and egresses the out-of-band management (OOBM) interface.

**Rule ID:** `SV-243231r720148_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM access switch will connect to the management interface of the managed network elements. The management interface can be a true OOBM interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will be directly connected to the OOBM network. (See SRG-NET-000205-RTR-000012.) Network boundaries, also known as managed interfaces, include, for example, gateways, routers, firewalls, guards, network-based malicious code analysis, and virtualization systems, or encrypted tunnels implemented within a security architecture (e.g., routers protecting firewalls or application gateways residing on protected subnetworks). Subnetworks that are physically or logically separated from internal networks are referred to as demilitarized zones (DMZs). Methods used for prohibiting interfaces within organizational information systems include, for example, restricting external web traffic to designated web servers within managed interfaces and prohibiting external traffic that appears to be spoofing internal addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if the OOB management interface is assigned an appropriate IP address from the authorized OOB management network. If an IP address assigned to the interface is not from an authorized OOB management network, this is a finding.

## Group: SRG-NET-000131

**Group ID:** `V-243232`

### Rule: The network device must not be configured to have any feature enabled that calls home to the vendor.

**Rule ID:** `SV-243232r856611_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Call-home services will routinely send data such as configuration and diagnostic information to the vendor for routine or emergency analysis and troubleshooting. There is a risk that transmission of sensitive data sent to unauthorized persons could result in data loss or downtime due to an attack. (See SRG-NET-000131-RTR-000083.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if the call home service or feature is disabled on the device. If the call home service is enabled on the device, this is a finding. Note: This feature can be enabled if the communication is only to a server residing in the local area network or enclave.

