# STIG Benchmark: Network WLAN AP-IG Platform Security Technical Implementation Guide

---

**Version:** 7

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000512

**Group ID:** `V-243207`

### Rule: WLAN SSIDs must be changed from the manufacturer's default to a pseudo random word that does not identify the unit, base, organization, etc.

**Rule ID:** `SV-243207r720076_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An SSID identifying the unit, site, or purpose of the WLAN or that is set to the manufacturer default may cause an OPSEC vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration. 1. Obtain the SSID using a wireless scanner or the AP or WLAN controller management software. 2. Verify the name is not meaningful (e.g., site name, product name, room number, etc.) and is not set to the manufacturer's default value. If the SSID does not meet the requirement listed above, this is a finding.

## Group: SRG-NET-000514

**Group ID:** `V-243208`

### Rule: The WLAN inactive/idle session timeout must be set for 30 minutes or less.

**Rule ID:** `SV-243208r817084_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A WLAN session that never terminates due to inactivity may allow an opening for an adversary to highjack the session to obtain access to the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Review the relevant configuration screen of the WLAN controller or access point. 2. Verify the inactive/idle session timeout setting is set for 30 minutes or less. If the inactive/idle session timeout is not set to 30 minutes or less for the entire WLAN, or the WLAN does not have the capability to enable the session timeout feature, this is a finding.

## Group: SRG-NET-000063

**Group ID:** `V-243209`

### Rule: WLAN components must be Wi-Fi Alliance certified with WPA2 or WPA3.

**Rule ID:** `SV-243209r720082_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Wi-Fi Alliance certification ensures compliance with DoD interoperability requirements between various WLAN products.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the WLAN equipment specification and verify it is Wi-Fi Alliance certified with either the older WPA2 certification or the newer WPA3 certification. WPA3 is preferred but not required at this time. If the WLAN equipment is not Wi-Fi Alliance certified with WPA2 or WPA3, this is a finding.

## Group: SRG-NET-000151

**Group ID:** `V-243210`

### Rule: WLAN components must be FIPS 140-2 or FIPS 140-3 certified and configured to operate in FIPS mode.

**Rule ID:** `SV-243210r891317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DoD WLAN components (WLAN AP, controller, or client) are not NIST FIPS 140-2/FIPS 140-3 (Cryptographic Module Validation Program, CMVP) certified, the WLAN system may not adequately protect sensitive unclassified DoD data from compromise during transmission.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the WLAN equipment specification and verify it is FIPS 140-2/3 (CMVP) certified for data in transit, including authentication credentials. Verify the component is configured to operate in FIPS mode. If the WLAN equipment is not is FIPS 140-2/3 (CMVP) certified or is not configured to operate in FIPS mode, this is a finding.

## Group: SRG-NET-000384

**Group ID:** `V-243211`

### Rule: WLAN signals must not be intercepted outside areas authorized for WLAN access.

**Rule ID:** `SV-243211r856608_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Most commercially available WLAN equipment is preconfigured for signal power appropriate to most applications of the WLAN equipment. In some cases, this may permit the signals to be received outside the physical areas for which they are intended. This can occur when the intended area is relatively small, such as a conference room, or when the access point is placed near or window or wall, thereby allowing signals to be received in neighboring areas. In such cases, an adversary may be able to compromise the site's posture by measuring the presence of the signal and the quantity of data transmitted to obtain information about when personnel are active and what they are doing. If the signal is not appropriately protected through defense-in-depth mechanisms, the adversary could possibly use the connection to access DoD networks and sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation and inspect access point locations. 1. Review documentation showing signal strength analysis from site survey activities, if available. 2. Use testing equipment or WLAN clients to determine if the signal strength is, in the reviewer's judgment, excessively outside the required area (e.g., strong signal in the parking area, public areas, or uncontrolled spaces). 3. Lower-end access points will not have this setting available. In this case, verify the access points are located away from exterior walls to achieve compliance with this requirement. If any of the following is found, this is a finding: - Visual inspection of equipment shows obvious improper placement of access points where they will emanate into uncontrolled spaces (e.g., next to external walls, windows, or doors; uncontrolled areas; or public areas). - Building walk-through testing shows signals of sufficient quality and strength to allow wireless access to exist in areas not authorized for WLAN access.

## Group: SRG-NET-000063

**Group ID:** `V-243212`

### Rule: The WLAN access point must be configured for Wi-Fi Alliance WPA2 or WPA3 security.

**Rule ID:** `SV-243212r720091_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Wi-Fi Alliance's WPA2/WPA3 certification provides assurance that the device has adequate security functionality and can implement the IEEE 802.11i standard for robust security networks. The previous version of the Wi-Fi Alliance certification, WPA, did not require AES encryption, which must be supported for DoD WLAN implementations. Devices without any WPA certification likely do not support required security functionality and could be vulnerable to a wide range of attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the access point is configured for either WPA2/WPA3 (Enterprise) or WPA2/WPA3 (Personal) authentication. The procedure for performing this review will vary depending on the AP model. Have the SA show the configuration setting. If the access point is not configured with either WPA2 or WPA3 security, this is finding.

## Group: SRG-NET-000512

**Group ID:** `V-243213`

### Rule: DoD Components providing guest WLAN access (internet access only) must use separate WLAN or logical segmentation of the enterprise WLAN (e.g., separate service set identifier [SSID] and virtual LAN) or DoD network.

**Rule ID:** `SV-243213r720094_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The purpose of the Guest WLAN network is to provide WLAN services to authorized site guests. Guests, by definition, are not authorized access to the enterprise network. If the guest WLAN is not installed correctly, unauthorized access to the enterprise wireless and/or wired network could be obtained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the SA show how the guest WLAN is physically connected to the firewall or supporting switch and how it is logically connected through firewall or switch configuration settings. Verify the equipment is connected via a separate WLAN or logical segmentation of the host WLAN (e.g., separate service set identifier [SSID] and virtual LAN). Verify the guest WLAN only provides internet access. If a guest WLAN is not set up as a separate WLAN from the DoD network or is not set up as a logical segmentation from the DoD network or DoD WLAN, this is a finding. If the guest WLAN does not provide only internet access, this is a finding.

## Group: SRG-NET-000205

**Group ID:** `V-243214`

### Rule: The network device must be configured to only permit management traffic that ingresses and egresses the out-of-band management (OOBM) interface.

**Rule ID:** `SV-243214r720097_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM access switch will connect to the management interface of the managed network elements. The management interface can be a true OOBM interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will be directly connected to the OOBM network. (See SRG-NET-000205-RTR-000012.) Network boundaries, also known as managed interfaces, include, for example, gateways, routers, firewalls, guards, network-based malicious code analysis, and virtualization systems, or encrypted tunnels implemented within a security architecture (e.g., routers protecting firewalls or application gateways residing on protected subnetworks). Subnetworks that are physically or logically separated from internal networks are referred to as demilitarized zones (DMZs). Methods used for prohibiting interfaces within organizational information systems include, for example, restricting external web traffic to designated web servers within managed interfaces and prohibiting external traffic that appears to be spoofing internal addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if the OOB management interface is assigned an appropriate IP address from the authorized OOB management network. If an IP address assigned to the interface is not from an authorized OOB management network, this is a finding.

## Group: SRG-NET-000131

**Group ID:** `V-243215`

### Rule: The network device must not be configured to have any feature enabled that calls home to the vendor.

**Rule ID:** `SV-243215r856609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Call-home services will routinely send data such as configuration and diagnostic information to the vendor for routine or emergency analysis and troubleshooting. There is a risk that transmission of sensitive data sent to unauthorized persons could result in data loss or downtime due to an attack. (See SRG-NET-000131-RTR-000083.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if the call home service or feature is disabled on the device. If the call home service is enabled on the device, this is a finding. Note: This feature can be enabled if the communication is only to a server residing in the local area network or enclave.

