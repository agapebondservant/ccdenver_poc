# STIG Benchmark: Arista Multilayer Switch DCS-7000 Series L2S Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000018

**Group ID:** `V-214662`

### Rule: The Arista Multilayer Switch must enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies.

**Rule ID:** `SV-214662r382732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. A few examples of flow control restrictions include: keeping export-controlled information from being transmitted in the clear to the Internet and blocking information marked as classified but which is being transported to an unapproved destination. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, devices) within information systems. Enforcement occurs, for example, in boundary protection devices (e.g., gateways, routers, guards, encrypted tunnels, and firewalls) that employ rule sets or establish configuration settings that restrict information system services, provide a packet filtering capability based on header information, or provide a message filtering capability based on message content (e.g., implementing key word searches or using document characteristics).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the use of Spanning-Tree Protocol for information flow control via the "show spanning-tree" command. Alternatively, from the output of the "show running-config" command, review the configuration for "spanning-tree mode" statement, and verify the line "spanning-tree disabled" is not present for production VLANs. If spanning-tree is not used for controlling the flow of information, this is a finding.

## Group: SRG-NET-000019

**Group ID:** `V-214663`

### Rule: The Arista Multilayer Switch must enforce approved authorizations for controlling the flow of information between interconnected systems based on organization-defined information flow control policies.

**Rule ID:** `SV-214663r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Examples of flow control restrictions include blocking outside traffic claiming to be from within the organization, and not passing any web requests to the Internet not from the internal web proxy. Additional examples of restrictions include: keeping export-controlled information from being transmitted in the clear to the Internet, and blocking information marked as classified, but which is being transported to an unapproved destination. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, and devices) within information systems. Enforcement occurs, for example, in boundary protection devices (e.g., gateways, routers, guards, encrypted tunnels, and firewalls) that employ rule sets or establish configuration settings that restrict information system services, provide a packet filtering capability based on header information, or provide a message filtering capability based on message content (e.g., implementing key word searches or using document characteristics).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the use of MAC Access Control Lists to prevent unintended information flow between network segments. For network boundary interfaces, verify the use of an access control list by entering "show mac access-list summary" to validate the use of an access control list on the interface. Verify the access control list restricts network traffic as intended by entering "show mac access-list [name]" and substituting the name of the access control list for the bracketed variable. If there is no access control list configured, or if the access control list does not prevent unintended flow of information between network segments, this is a finding.

## Group: SRG-NET-000148

**Group ID:** `V-214664`

### Rule: The Arista Multilayer Switch must uniquely identify all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-214664r385501_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of identification claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide the identification decisions (as opposed to the actual identifiers) to the services that need to act on those decisions. This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers (outside a datacenter), VoIP Phones, and VTC CODECs). Gateways and SOA applications are examples of where this requirement would apply.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the network device uniquely identifies network-connected endpoint devices. This requirement is not applicable to Arista switches when not used as an access switch. 802.1X must be configured on any interface where there is an applicable endpoint device connected. This is demonstrated by viewing the running-config via the "show dot1x all" command and validating the following lines are present in the configuration: Dot1X Information for Ethernet[X] -------------------------------------------- PortControl : auto HostMode : single-host QuietPeriod : [value] TxPeriod : [value] ReauthPeriod : 3600 seconds MaxReauthReq : 2 ! 802.1X must also be globally enabled on the switch using the "dot1x system-auth-control" command from the configuration mode interface. When this is configured, the following line will be visible in the running-config: dot1x-system-auth-control 802.1X is dependent on a properly configured RADIUS server for authentication. Refer to the RADIUS configuration example for validation of properly configured AAA services. Additionally, the user must specify to use the RADIUS server as an 802.1X authenticator with the "aaa authentication dot1x default group [radius]" command from the configuration mode interface, replacing the bracketed variable with either the group name of the RADIUS server group or leaving it as is to authenticate against all RADIUS servers. When properly configured, the following line is visible in the running-config: aaa authentication dot1x default group radius If 802.1X is not configured on necessary ports or is not globally enabled on the switch, or if it is not set to authenticate supplicants via RADIUS, this is a finding.

## Group: SRG-NET-000151

**Group ID:** `V-214665`

### Rule: The Arista Multilayer Switch must authenticate all endpoint devices before establishing a network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-214665r971529_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity on the network. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk (e.g., remote connections). Bidirectional authentication solutions include, but are not limited to, IEEE 802.1x and Extensible Authentication Protocol (EAP) and Radius server with EAP-Transport Layer Security (TLS) authentication. A network connection is any connection with a device that communicates through a network (e.g., local area network, wide area network, or the Internet). Authentication must use a form of cryptography to ensure a high level of trust and authenticity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the network device uniquely identifies network-connected endpoint devices. This requirement is not applicable to Arista switches when not used as an access switch. 802.1X must be configured on any interface where there is an applicable endpoint device connected. This is demonstrated by viewing the running-config via the "show dot1x all" command and validating the following lines are present in the configuration: Dot1X Information for Ethernet[X] -------------------------------------------- PortControl : auto HostMode : single-host QuietPeriod : [value] TxPeriod : [value] ReauthPeriod : 3600 seconds MaxReauthReq : 2 ! 802.1X must also be globally enabled on the switch using the "dot1x system-auth-control" command from the configuration mode interface. When this is configured, the following line will be visible in the running-config: dot1x-system-auth-control 802.1X is dependent on a properly configured RADIUS server for authentication. Refer to the RADIUS configuration example for validation of properly configured AAA services. Additionally, the user must specify to use the RADIUS server as an 802.1X authenticator with the "aaa authentication dot1x default group [radius]" command from the configuration mode interface, replacing the bracketed variable with either the group name of the RADIUS server group, or leaving it as is to authenticate against all RADIUS servers. When properly configured, the following line is visible in the running-config: aaa authentication dot1x default group radius If 802.1X is not configured on necessary ports, or is not globally enabled on the switch, or if it is not set to authenticate supplicants via RADIUS, this is a finding.

## Group: SRG-NET-000343

**Group ID:** `V-214666`

### Rule: The Arista Multilayer Switch must authenticate 802.1X connected devices before establishing any connection.

**Rule ID:** `SV-214666r856148_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers (outside a datacenter), VoIP Phones, and VTC CODECs). Gateways and SOA applications are examples of where this requirement would apply. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific pre-authorized devices can access the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement only applies to devices required to employ 802.1X. Verify that the network device uniquely identifies network-connected endpoint devices. This requirement is not applicable to Arista switches when not used as an access switch. 802.1X must be configured on any interface where there is an applicable endpoint device connected. This is demonstrated by viewing the running-config via the "show dot1x all" command and validating the following lines are present in the configuration: Dot1X Information for Ethernet[X] -------------------------------------------- PortControl : auto HostMode : single-host QuietPeriod : [value] TxPeriod : [value] ReauthPeriod : 3600 seconds MaxReauthReq : 2 ! 802.1X must also be globally enabled on the switch using the "dot1x system-auth-control" command from the configuration mode interface. When this is configured, the following line will be visible in the running-config: dot1x-system-auth-control 802.1X is dependent on a properly configured RADIUS server for authentication. Refer to the RADIUS configuration example for validation of properly configured AAA services. Additionally, the user must specify to use the RADIUS server as an 802.1X authenticator with the "aaa authentication dot1x default group [radius]" command from the configuration mode interface, replacing the bracketed variable with either the group name of the RADIUS server group or leaving it as is to authenticate against all RADIUS servers. When properly configured, the following line is visible in the running-config: aaa authentication dot1x default group radius If 802.1X is not configured on necessary ports or is not globally enabled on the switch, or if it is not set to authenticate supplicants via RADIUS, this is a finding.

## Group: SRG-NET-000151

**Group ID:** `V-230143`

### Rule:  The Arista Multilayer Switch must re-authenticate all endpoint devices every 60 minutes or less.

**Rule ID:** `SV-230143r971529_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity on the network. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk (e.g., remote connections). Bidirectional authentication solutions include, but are not limited to, IEEE 802.1x and Extensible Authentication Protocol (EAP) and Radius server with EAP-Transport Layer Security (TLS) authentication. A network connection is any connection with a device that communicates through a network (e.g., local area network, wide area network, or the Internet). Authentication must use a form of cryptography to ensure a high level of trust and authenticity. Re-authentication must occur to ensure session security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement only applies to devices required to employ 802.1X authentication. Verify that the network device uniquely identifies network-connected endpoint devices and re-authenticates devices every 60 minutes or less. This can be viewed via the "show dot1x all" command. Under the interface configuration for the .1X connected port, the following statements must be present: ReauthPeriod : 3600 seconds If the device does not require re-authentication, or if the re-authentication period is longer than 60 minutes, this is a finding.

## Group: SRG-NET-000338

**Group ID:** `V-230144`

### Rule: The Arista Multilayer Switch must re-authenticate 802.1X connected devices every hour.

**Rule ID:** `SV-230144r953984_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. In addition to the re-authentication requirements associated with session locks, organizations may require re-authentication of individuals and/or devices in other situations, including (but not limited to) the following circumstances: (i) When authenticators change; (ii) When roles change; (iii) When security categories of information systems change; (iv) When the execution of privileged functions occurs; (v) After a fixed period of time; or (vi) Periodically. Within the DoD, the minimum circumstances requiring re-authentication are privilege escalation and role changes. This requirement only applies to components where this is specific to the function of the device or has the concept of user authentication (e.g., VPN or ALG capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement only applies to devices required to employ 802.1X. Verify the Arista Multilayer Switch re-authenticates 802.1X connected devices every hour. If the Arista Multilayer Switch does not re-authenticate 802.1X connected devices, this is a finding. This can be viewed via the "show dot1x all" command. Under the interface configuration for the .1X connected port, the following statements must be present: ReauthPeriod : 3600 seconds If the device does not require re-authentication, or if the re-authentication period is longer than 60 minutes, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-264427`

### Rule: The Arista MLS L2S must be using a version supported by the vendor.

**Rule ID:** `SV-264427r992078_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

