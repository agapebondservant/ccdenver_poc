# STIG Benchmark: Network WLAN Controller Platform Security Technical Implementation Guide

---

**Version:** 7

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000514

**Group ID:** `V-243233`

### Rule: The WLAN inactive/idle session timeout must be set for 30 minutes or less.

**Rule ID:** `SV-243233r817090_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A WLAN session that never terminates due to inactivity may allow an opening for an adversary to highjack the session to obtain access to the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Review the relevant configuration screen of the WLAN controller or access point. 2. Verify the inactive/idle session timeout setting is set for 30 minutes or less. If the inactive/idle session timeout is not set to 30 minutes or less for the entire WLAN, or the WLAN does not have the capability to enable the session timeout feature, this is a finding.

## Group: SRG-NET-000070

**Group ID:** `V-243234`

### Rule: WLAN must use EAP-TLS.

**Rule ID:** `SV-243234r720157_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>EAP-TLS provides strong cryptographic mutual authentication and key distribution services not found in other EAP methods, and thus provides significantly more protection against attacks than other methods. Additionally, EAP-TLS supports two-factor user authentication on the WLAN client, which provides significantly more protection than methods that rely on a password or certificate alone. EAP-TLS also can leverage the DoD Common Access Card (CAC) in its authentication services, providing additional security and convenience.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the equipment is WPA2/WPA3 certified by the Wi-Fi Alliance, it is capable of supporting this requirement. Review the WLAN equipment configuration to verify that EAP-TLS is actively used and no other methods are enabled. If EAP-TLS is not used or if the WLAN system allows users to connect with other methods, this is a finding.

## Group: SRG-NET-000151

**Group ID:** `V-243235`

### Rule: WLAN components must be FIPS 140-2 or FIPS 140-3 certified and configured to operate in FIPS mode.

**Rule ID:** `SV-243235r891326_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DoD WLAN components (WLAN AP, controller, or client) are not NIST FIPS 140-2/FIPS 140-3 (Cryptographic Module Validation Program, CMVP) certified, the WLAN system may not adequately protect sensitive unclassified DoD data from compromise during transmission.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the WLAN equipment specification and verify it is FIPS 140-2/3 (CMVP) certified for data in transit, including authentication credentials. Verify the component is configured to operate in FIPS mode. If the WLAN equipment is not is FIPS 140-2/3 (CMVP) certified or is not configured to operate in FIPS mode, this is a finding.

## Group: SRG-NET-000070

**Group ID:** `V-243236`

### Rule: WLAN EAP-TLS implementation must use certificate-based PKI authentication to connect to DoD networks.

**Rule ID:** `SV-243236r720163_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD certificate-based PKI authentication is strong, two-factor authentication that relies on carefully evaluated cryptographic modules. Implementations of EAP-TLS that are not integrated with certificate-based PKI could have security vulnerabilities. For example, an implementation that uses a client certificate on laptop without a second factor could enable an adversary with access to the laptop to connect to the WLAN without a PIN or password. Systems that do not use the certificate-based PKI are also much more likely to be vulnerable to weaknesses in the underlying public key infrastructure (PKI) that supports EAP-TLS. Certificate-based PKI authentication must be used to connect WLAN client devices to DoD networks. The certificate-based PKI authentication should directly support the WLAN EAP-TLS implementation. At least one layer of user authentication must enforce network authentication requirements (e.g., CAC authentication) before the user is able to access DoD information resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the site ISSO and SA. Determine if the site's network is configured to require certificate-based PKI authentication before a WLAN user is connected to the network. If certificate-based PKI authentication is not required prior to a DoD WLAN user accessing the DoD network, this is a finding. Note: This check does not apply to medical devices. Medical devices are permitted to connect to the WLAN using pre-shared keys.

## Group: SRG-NET-000205

**Group ID:** `V-243237`

### Rule: The network device must be configured to only permit management traffic that ingresses and egresses the out-of-band management (OOBM) interface.

**Rule ID:** `SV-243237r720166_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM access switch will connect to the management interface of the managed network elements. The management interface can be a true OOBM interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will be directly connected to the OOBM network. (See SRG-NET-000205-RTR-000012.) Network boundaries, also known as managed interfaces, include, for example, gateways, routers, firewalls, guards, network-based malicious code analysis, and virtualization systems, or encrypted tunnels implemented within a security architecture (e.g., routers protecting firewalls or application gateways residing on protected subnetworks). Subnetworks that are physically or logically separated from internal networks are referred to as demilitarized zones (DMZs). Methods used for prohibiting interfaces within organizational information systems include, for example, restricting external web traffic to designated web servers within managed interfaces and prohibiting external traffic that appears to be spoofing internal addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if the OOB management interface is assigned an appropriate IP address from the authorized OOB management network. If an IP address assigned to the interface is not from an authorized OOB management network, this is a finding.

## Group: SRG-NET-000131

**Group ID:** `V-243238`

### Rule: The network device must not be configured to have any feature enabled that calls home to the vendor.

**Rule ID:** `SV-243238r856613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Call-home services will routinely send data such as configuration and diagnostic information to the vendor for routine or emergency analysis and troubleshooting. There is a risk that transmission of sensitive data sent to unauthorized persons could result in data loss or downtime due to an attack. (See SRG-NET-000131-RTR-000083.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if the call home service or feature is disabled on the device. If the call home service is enabled on the device, this is a finding. Note: This feature can be enabled if the communication is only to a server residing in the local area network or enclave.

