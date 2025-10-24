# STIG Benchmark: Forescout Network Access Control Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000015-NAC-000020

**Group ID:** `V-233309`

### Rule: Forescout must enforce approved access by employing admissions assessment filters that include, at a minimum, device attributes such as type, IP address, resource group, and/or mission conditions as defined in Forescout System Security Plan (SSP).  This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233309r811367_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Many NACs include the ability to create network access control policies that include identity-based policies, role-based policies, and attribute-based policies. It is recommended that Forescout have the capability to expose collected data on the assessed endpoints through an API that can be accessed externally, or the NAC solution must supply an SDK to allow customers to export data. Admissions assessment filters should include, at a minimum, device attributes such as type, IP address, resource group, and/or mission conditions as defined in the Forescout SSP. Forescout should also track the following to facilitate security investigations: when each device was last admitted/readmitted to the network; owning organization; owning organization's organizational unit; geographic location or the nearest network switch; motherboard serial number and BIOS; globally unique ID; and which unique network access compliance policies each device passed or failed during the latest network admission/readmission. The client may be denied admission based on a returned posture token. In most Forescout implementations, additional network access authorization policies can also be tied to the user's identity, but these features are out of scope for this STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Use the Forescout Administrator UI to ensure that the endpoint compliance assessment policies have been implemented per the SSP and are functioning correctly. If Forescout does not have compliance assessment policies configured this is a finding.

## Group: SRG-NET-000015-NAC-000030

**Group ID:** `V-233310`

### Rule: Endpoint policy assessment must proceed after the endpoint attempting access has been identified using an approved identification method such as IP address.  This is required for compliance with C2C Step 2.

**Rule ID:** `SV-233310r811369_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Automated policy assessments must reflect the organization's current security policy so entry control decisions will happen only where remote endpoints meet the organization's security requirements. If the remote endpoints are allowed to connect to the organization's network without passing minimum-security controls, they become a threat to the entire network. Organizational policy must be established for what Forescout will check on the host for the agent and agentless. The Forescout system security plan (SSP) will be used to assess compliance with the requirement since each SSP item must be configured. Examples include, but are not limited to: - Verification that anti-virus software is authorized, running, and virus signatures are up to date. - Host-based firewall installed and configured according to the organization's security policy. - Host IDS/IPS is installed, operational, and up to date. - Uses the result of malware, anti-virus, and IDS scans and status as part of the assessment decision process. - Required BIOS, operating system, browser, and office application patch levels. - Performs an assessment of the list of running services. - Test for the presence of DoD-required software. - Test for presence of peer-to-peer software (not allowed).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 2 or higher, this is not a finding. Use the Forescout Administrator UI to ensure that the endpoint compliance assessment policies have been implemented per the SSP and are functioning correctly. 1. Log on to the Forescout Administrator UI. 2. From the Home screen select the "Policy" tab. 3. Verify that policies exist that assess compliance in accordance with the SSP. If Forescout does not have compliance assessment policies configured this is a finding.

## Group: SRG-NET-000015-NAC-000040

**Group ID:** `V-233311`

### Rule: For endpoints that require automated remediation, Forescout must be configured to redirect endpoints to a logically separate network segment for remediation services. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233311r811371_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Automated and manual procedures for remediation for critical security updates will be managed differently. Continuing to assess and remediate endpoints with risks that could endanger the network could impact network usage for all users. This isolation prevents traffic from flowing with traffic from endpoints that have been fully assessed and authorized. Unauthenticated devices must not be allowed to connect to remediation services. Forescout accepts only endpoints with IP addresses that are in range. Configure Forescout to identify the endpoint. By default the IP address is used as the endpoint identifier. The system can be configured to capture the following other endpoint unique identifiers if approved for use by the SSP as the identification method: BIOS Serial number and other hardcoded attributes, OS host name, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. If automated remediation is not required by the SSP, this is not a finding. Use the Forescout Administrator UI to verify that Forescout is configured to redirect endpoints requiring automated remediation to a network segment that is isolated from trusted traffic. If Forescout does not have one or more policies that redirect endpoints that require automated remediation to a logically isolated, this is a finding.

## Group: SRG-NET-000015-NAC-000060

**Group ID:** `V-233312`

### Rule:  If a device requesting access fails Forescout policy assessment, Forescout must communicate with other components and the switch to either terminate the session or isolate the device from the trusted network for remediation. This is required for compliance with C2C Step 3.

**Rule ID:** `SV-233312r811373_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Endpoints with identified security flaws and weaknesses endanger the network and other devices on it. Isolation or termination prevents traffic from flowing with traffic from endpoints that have been fully assessed and authorized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 3 or higher, this is not a finding. Use the Forescout Administrator UI to verify that policies are configured to filter the policy assessment devices based on risk and are remediated or isolated according to the SSP. 1. In the Forescout UI, go to the Policy Tab >> Compliance Policies. 2. Verify the action within the Compliance Policies is configured with one of the following actions: - Terminate the connection and place the device on a blacklist to prevent future connection attempts until action is taken to remove the device from the blacklist. - Redirect traffic from the remote endpoint to the automated remediation subnet for connection to the remediation server. - Allow the device access to limited network services such as public web servers in the protected DMZ (must be approved by the AO). - Allow the device and user full entry into the protected networks but flag it for future remediation. With this option, an automated reminder should be used to inform the user of the remediation status. If Forescout does not communicate with the remote access gateway to implement a policy to either terminate the session or isolate the device from the trusted network this is a finding.

## Group: SRG-NET-000015-NAC-000070

**Group ID:** `V-233313`

### Rule: Forescout must be configured to notify the user before proceeding with remediation of the user's endpoint device when automated remediation is used. This is required for compliance with C2C Step 3.

**Rule ID:** `SV-233313r811375_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Connections that bypass established security controls should be allowed only in cases of administrative need. These procedures and use cases must be approved by the Information System Security Manager (ISSM). This setting may be sent from the assessment server, a central server, or from the remediation server. Verify the user is notified and accepts (e.g., using an accept button) that remediation is needed and is about to begin.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 3 or higher, this is not a finding. Check Forescout policy to ensure that exempt devices that are in need of remediation prompt the user to accept the remediation process, prior to conducting. 1. Log on to the Forescout UI. 2. Select the "Policy" tab. 3. Review the compliance policy identified by the site representation as the remediation policy, then click "Edit". 4. In the Sub-Rules section, select a policy and click "Edit". 5. From the Actions section, verify that the policy is configured to notify the user, prior to remediation, that user interaction is required. If Forescout is not configured to notify the user before proceeding with remediation of the user's endpoint device when automated remediation is used, this is a finding.

## Group: SRG-NET-000015-NAC-000080

**Group ID:** `V-233314`

### Rule: Forescout must be configured so that all client machines are assessed by Forescout with exceptions that are allowed to bypass Forescout based on account or account type, as approved by the information system security manager (ISSM) and documented in the System Security Plan (SSP). This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233314r919219_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The NAC gateway provides the policy enforcement allowing or denying the endpoint to the network. Unauthorized endpoints that bypass this control present a risk to the organization's data and network. The focus of this requirement is on identification, documentation, and approval of devices that will bypass the NAC. This is not a requirement that all traffic flow through the NAC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DOD is not at C2C Step 1 or higher, this is not a finding. If traffic is not allowed to bypass the NAC policy, this is not a finding. Use the Forescout Administrator UI to verify a policy exists that uses the exemption group configured so that all client machines are assessed by Forescout with exceptions that are allowed to bypass Forescout based on the account or account type, as approved by the ISSM and documented in the SSP. 1. In the filters pane under Groups, right-click the group editor. Pick the group indicated as compliance by the site representative. 2. Click "Scope" and review the Exemptions Group. If Forescout is not configured to approve all instances where traffic is allowed to bypass the NAC as approved by the ISSM, this is a finding.

## Group: SRG-NET-000015-NAC-000090

**Group ID:** `V-233315`

### Rule: Forescout appliance must not be configured to implement a DHCP layer 3 method for separation or device authorization. This is required for compliance with C2C Step 2.

**Rule ID:** `SV-233315r919222_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An internal rogue device can still bypass the authentication process, regardless of the policy flow. Configuring the NAC to process all device authentication will ensure that any rogue device, internal or external, will be authenticated prior to network access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DOD is not at C2C Step 1 or higher, this is not a finding. Check Forescout policy and verify it is configured to prohibit the use of DHCP to separate authenticated and nonauthenticated network access requests. If the NAC does not prohibit the use of DHCP to separate authenticated and nonauthenticated network access requests, this is a finding.

## Group: SRG-NET-000015-NAC-000100

**Group ID:** `V-233316`

### Rule: Forescout must send an alert to the Information System Security Manager (ISSM) and System Administrator (SA), at a minimum, when critical security issues are found that put the network at risk. This is required for compliance with C2C Step 2.

**Rule ID:** `SV-233316r811381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring authentication and authorization of both the user's identity and the identity of the computing device is essential to ensuring a non-authorized person or device has entered the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 2 or higher, this is not a finding. Verify Forescout performs device authentication before policy assessment is performed. If device authentication is not completed prior to the NAC check, this is a finding.

## Group: SRG-NET-000015-NAC-000110

**Group ID:** `V-233317`

### Rule: When devices fail the policy assessment, Forescout must create a record with sufficient detail suitable for forwarding to a remediation server for automated remediation or sending to the user for manual remediation. This is required for compliance with C2C Step 3.

**Rule ID:** `SV-233317r811383_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Notifications sent to the user and/or network administrator informing them of remediation requirements will ensure that action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 3 or higher, this is not a finding. Verify Forescout sends user and/or admin notification of remediation requirements, whether manual or automated. If the NAC does not flag for future manual or automated remediation, devices failing policy assessment that are not automatically remediated either before or during the remote access session, this a finding.

## Group: SRG-NET-000015-NAC-000120

**Group ID:** `V-233318`

### Rule:  Forescout must place client machines on a blacklist or terminate network communications on devices when critical security issues are found that put the network at risk. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233318r811385_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Devices that are found to have critical security issues place the network at risk if they are allowed to continue communications. Policy actions should be in place to terminate or restrict network communication or place the suspicious machine on a blacklist.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Check Forescout policy to ensure that any device with a critical security issue is checked through a security policy and an action is taken to either blacklist it or terminate communication with other network devices. If the NAC does not immediately place the device on the blacklist and terminate the connection when critical security issues are found that put the network at immediate risk, this a finding.

## Group: SRG-NET-000015-NAC-000130

**Group ID:** `V-233319`

### Rule: Forescout must be configured so client machines do not communicate with other network devices in the DMZ or subnet except as needed to perform a client assessment or to identify itself. This is required for compliance with C2C Step 2.

**Rule ID:** `SV-233319r811387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Devices not compliant with DoD secure configuration policies are vulnerable to attack. Allowing these systems to connect presents a danger to the enclave. Verify that Forescout is not allowed to communicate with other hosts in the DMZ that do not perform security policy assessment or remediation services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 2 or higher, this is not a finding. 1. Select Tools >> Options >> Appliance >> IP Assignment. 2. Select Segment >> IP Addresses. 3. Verify the IP address for the DMZ subnet is not present. If Forescout is not configured so the devices and servers in the Forescout solution (e.g., NAC, assessment server, policy decision point) do not communicate with other network devices in the DMZ or subnet except as needed to perform a remote access client assessment or to identify itself, this is a finding.

## Group: SRG-NET-000321-NAC-001210

**Group ID:** `V-233320`

### Rule: Forescout must enforce the revocation of endpoint access authorizations when devices are removed from an authorization group. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233320r856506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring the conditions that are configured in policy have proper time limits set to reflect changes will allow for proper access. This will help to validate that authorized individuals have proper access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Verify Forescout admission policy has been configured to revoke access to endpoints that have not met or are removed from the authorized group. If Forescout is not configured with an admissions policy that enforces the revocation of endpoint access authorizations based on when devices are removed from an authorization group, this is a finding.

## Group: SRG-NET-000322-NAC-001220

**Group ID:** `V-233321`

### Rule: Forescout must enforce the revocation of endpoint access authorizations at the next compliance assessment interval based on changes to the compliance assessment security policy. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233321r856507_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement gives the option to configure for automated remediation and/or manual remediation. A detailed record must be passed to the remediation server for action. Alternatively, the details can be passed in a notice to the user for action. The device status will be updated on the network access server/authentication server so that further access attempts are denied. The NAC must have policy assessment mechanisms with granular control to distinguish between access restrictions based on the criticality of the software or setting failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Verify Forescout admission policy has been configured to revoke access to endpoints that have not met or are removed from the authorized group. If Forescout is not configured with an admissions policy that enforces the revocation of endpoint access authorizations based on when devices are removed from an authorization group, this is a finding.

## Group: SRG-NET-000322-NAC-001230

**Group ID:** `V-233322`

### Rule: Forescout must deny or restrict access for endpoints that fail critical endpoint security checks. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233322r856508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Devices that do not meet minimum-security configuration requirements pose a risk to the DoD network and information assets. Endpoint devices must be disconnected or given limited access as designated by the approval authority and system owner if the device fails the authentication or security assessment. The user will be presented with a limited portal, which does not include access options for sensitive resources. Required security checks must implement DoD policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Verify Forescout has been configured to redirect filtered devices to a limited access network to include a remediation network or limited access network. If a policy does not exist that redirects the failed device to an authorized network for remediation or limited access, this is not a finding. If the NAC does not deny or restrict access for endpoints that fail critical endpoint security checks, this is a finding.

## Group: SRG-NET-000333-NAC-001340

**Group ID:** `V-233323`

### Rule: Forescout must be configured to log records onto a centralized events server. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233323r856509_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Keeping an established, connection-oriented audit record is essential to keeping audit logs in accordance with DoD requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. 1. Go to Tools >> Options >> Syslog. 2. Verify a central log server's IP address is configured. If Forescout does not configured to log records onto a centralized events server, this is a finding.

## Group: SRG-NET-000334-NAC-001350

**Group ID:** `V-233324`

### Rule: Forescout must off-load log records onto a different system. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233324r856510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having a separate, secure location for log records is essential to the preservation of logs as required by policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. 1. Go to Tools >> Options >> Syslog. 2. Verify a syslog server's IP address is configured. If each Forescout device does not offload log records to a separate device, this is a finding.

## Group: SRG-NET-000335-NAC-001360

**Group ID:** `V-233325`

### Rule: Forescout must generate a critical alert to be sent to the Information System Security Officer (ISSO) and Systems Administrator (SA) (at a minimum) in the event of an audit processing failure. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233325r856511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring that a security solution alerts in the event of misconfiguration or error is imperative to ensuring that proper auditing is being conducted. Having the ability to immediately notify an administrator when this auditing fails allows for a quick response and real-time remediation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify Forescout sends an alert to the proper security personnel when an audit process failure occurs. 1. Log on to the Forescout UI. 2. Locate the audit process policies as identified by the site representative. 3. Verify a policy for "audit failure" exists. 4. Verify this policy includes notification of security personnel. If Forescout does not send an alert when an audit processing failure occurs, this is a finding.

## Group: SRG-NET-000343-NAC-001460

**Group ID:** `V-233326`

### Rule: Forescout must authenticate all endpoint devices before establishing a connection and proceeding with posture assessment. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233326r856512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authenticating all devices as they connect to the network is the baseline of a good security solution. This is especially important prior to posture assessment to ensure authorized devices are online and have the proper posture prior to accessing the production network. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring that only specific preauthorized devices can access the system. Authentication methods for NAC include, but are not limited to, Kerberos, MAC, or other protocols. The IP Assignment Forescout configuration ensures any IP addresses that should be managed by the configured network will go through the policies within Forescout. Forescout policy structure is applied in a "waterfall" like way that assures all IP addresses start with the top most policy and flow down the policy tree. This policy flow ensures that all endpoints are properly identified, classified, and authenticated prior to the posture assessment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Use the Forescout Administrator UI to verify all IP addresses identified in the SSP are configured within the Appliance IP Assignments list. 1. Log on to the Forescout UI. 2. Select Tools >> Option >> Appliance >> IP Assignment. 3. Verify all IP addresses associated with the SSP are labeled within the IP Assignments list. If Forescout does not authenticate all endpoints prior to establishing a connection and proceeding with posture assessment, this is a finding.

## Group: SRG-NET-000343-NAC-001470

**Group ID:** `V-233327`

### Rule: Forescout must be configured to apply dynamic ACLs that restrict the use of ports when non-entity endpoints are connected using MAC Authentication Bypass (MAB). This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233327r856513_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MAB is only one way of connecting non-entity endpoints, and can be defeated by spoofing the MAC address of an assumed authorized device. By adding the device to the MAR, the device can then gain access to the network. NPE devices that can support PKI or an allowed authentication type must use PKI. MAB may be used for NPE that cannot support an approved device authentication. Non-entity endpoints include Internet of Things (IoT) devices, VoIP phone, and printer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Verify Forescout applies dynamic ACLs that restrict the use of ports when non-entity endpoints are connected using MAC Address Repository (MAR). If the NAC does not apply dynamic ACLs that restrict the use of ports when non-entity endpoints are connected using MAR, this is a finding.

## Group: SRG-NET-000273-NAC-000970

**Group ID:** `V-233328`

### Rule: Forescout must reveal error messages only to the Information System Security Officer (ISSO), Information System Security Manager (ISSM), and System Administrator (SA). This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233328r811406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring the proper amount of information is provided to the Security Management staff is imperative to ensure role based access control. Only those individuals that need to know about a security error of an application need to be notified of the error.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Use the Forescout Administrator UI to verify only individuals authorized by the SSP are configured to receive error messages. 1. Log on to the Forescout UI. 2. Within the highlighted policy, under the Actions section, select a configured action to view. 3. Find the Notify section and verify that only authorized individuals (IAW the SSP) are configured for the following: - HTTP Notification - Send Email - Send Notification If Forescout error messages can be viewed by unauthorized users other than the security personnel that have a need to know, this is a finding.

## Group: SRG-NET-000088-NAC-000440

**Group ID:** `V-233329`

### Rule: Forescout must configure TCP for the syslog protocol to allow for detection by the central event server if communications is lost. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233329r811408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Note that this configuration allows for the central log server to be configured with a critical alert to be sent to the System Security Officer (ISSO) and Systems Administrator (SA) (at a minimum) if it is unable to communicate the Forescout or stops receiving log updates. The alert requirement is in the Syslog STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. 1. Go to Tools >> Options >> Syslog. 2. Verify the Server Protocol is set to TCP. 3. Verify "Use TLS" setting is set. 4. Verify the "Identity, Facility, and Severity" setting is configured. If Forescout does not use TCP for the syslog protocol, this is a finding.

## Group: SRG-NET-000343-NAC-001480

**Group ID:** `V-233330`

### Rule: Forescout switch module must only allow a maximum of one registered MAC address per access port. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233330r856514_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of registered MAC addresses on a switch access port can help prevent a CAM table overflow attack. This type of attack lets an attacker exploit the hardware and memory limitations of a switch. If there are enough entries stored in a CAM table before the expiration of other entries, no new entries can be accepted into the CAM table. An attacker will be able to flood the switch with mostly invalid MAC addresses until the CAM table's resources have been depleted. When there are no more resources, the switch has no choice but to flood all ports within the VLAN with all incoming traffic. This happens because the switch cannot find the switch port number for a corresponding MAC address within the CAM table, allowing the switch to become a hub and traffic to be monitored. Some technologies are exempt from requiring a single MAC address per access port; however, restrictions still apply. VoIP or VTC endpoints may provide a PC port so a PC can be connected. Each of the devices will need to be statically assigned to each access port. Hot-desking is where several people are assigned to work at the same desk at different times, each user with their own PC. In this case, a different MAC address needs to be permitted for each PC that is connecting to the LAN drop in the workspace. Additionally, this workspace could contain a single phone (and possibly desktop VTC endpoint) used by all assignees, and the PC port on it might be the connection for their laptop. In this case, it is best not to use sticky port security but to use a static mapping of authorized devices. If this is not a teleworking remote location, this exemption does not apply.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Review the switch configuration to verify each access port is configured for a single registered MAC address. 1. Log on to the Forescout UI. 2. Go to Tools >> Options >> Switch >> Permissions >> Advanced. 3. Verify the "Maximum connected endpoints per port" is set to "1". If Forescout switch is not configured to permit a maximum of one registered MAC address per access port, this is a finding.

## Group: SRG-NET-000517-NAC-002370

**Group ID:** `V-233331`

### Rule: For TLS connections, Forescout must automatically terminate the session when a client certificate is requested and the client does not have a suitable certificate. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233331r856515_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In accordance with NIST SP 800-52, the TLS server must terminate the connection with a fatal “handshake failure” alert when a client certificate is requested and the client does not have a suitable certificate. During the TLS handshake negotiation, a "client certificate request" that includes a list of the types of certificates supported and the Distinguished Names of acceptable Certification Authorities (CAs) is sent to the client. TLS handshake enables the SSL or TLS client and server to establish the secret keys with which they communicate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify Forescout is configured to a list of DoD-approved certificate types and CAs. Verify the TLS session is configured to automatically terminate any session if the client does not have a suitable certificate. For TLS connections, if Forescout is not configured to automatically terminate the session when the client does not have a suitable certificate, this is a finding.

## Group: SRG-NET-000062-NAC-000340

**Group ID:** `V-233332`

### Rule: Forescout must use TLS 1.2, at a minimum, to protect the confidentiality of information passed between the endpoint agent and Forescout for the purposes of client posture assessment. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233332r811414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify Forescout is configured to a list of DoD-approved certificate types and CAs. Verify the TLS session is configured to automatically terminate any session if the client does not have a suitable certificate. For TLS connections, if Forescout is not configured to use TLS 1.2 at a minimum, this is a finding.

## Group: SRG-NET-000525-NAC-002430

**Group ID:** `V-233333`

### Rule: Forescout that stores device keys must have a key management process that is FIPS-approved and protected by Advanced Encryption Standard (AES) block cipher algorithms. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233333r814346_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The NAC that stores secret or private keys must use FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys. Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the authorized device and gain access to the network. Private key data associated with software certificates, including those issued to a NAC, are required to be generated and protected in at least a FIPS 140-2 Level 1-validated cryptographic module.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. If the NAC does not store device keys, this is not applicable. Verify the NAC is configured to use FIPS-mode or a key management process that is protected by Advanced Encryption Standard (AES) block cipher algorithms. If the NAC does not use FIPS-mode or key management process that is FIPS-approved and protected by Advanced Encryption Standard (AES) block cipher algorithms, this is a finding.

## Group: SRG-NET-000320-NAC-001200

**Group ID:** `V-233334`

### Rule: Communications between Forescout endpoint agent and the switch must transmit access authorization information via a protected path using a cryptographic mechanism. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233334r856516_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Forescout solution assesses the compliance posture of each client and returns an access decision based on configured security policy. The communications associated with this traffic must be protected from alteration and spoofing attacks so unauthorized devices do not gain access to the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify both ends are configured for secure communications between the NAC and NAC agent. If communication between the NAC and NAC agent does not use an encrypted method for protecting posture information transmitted between the devices, this is a finding.

## Group: SRG-NET-000492-NAC-002110

**Group ID:** `V-233335`

### Rule: Forescout must generate a log record when the client machine fails policy assessment because required security software is missing or has been deleted. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233335r811420_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Generating log records with regard to modules and policies is an important part of maintaining proper cyber hygiene. Keeping and maintaining the logs helps to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Use the Forescout Administrator UI to verify a central log server's IP address is configured withing the Syslog configuration settings. 1. Log on to the Forescout UI. 2. Select Tools >> Option >> HPS Inspection Engine >> SecureConnector. 3. In the Client-Server Connection, check the Minimum Supported TLS Version is set to TLS version 1.2. If the NAC does not use TLS 1.2, at a minimum, to protect the confidentiality of information passed between the endpoint agent and the NAC for the purposes of client posture assessment, this is a finding.

## Group: SRG-NET-000336-NAC-001390

**Group ID:** `V-233336`

### Rule: Forescout must be configured with a secondary log server, in case the primary log is unreachable. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233336r856517_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement pertains to NAC types and threat protection events of events as opposed to device management events vs. operating system and system log types of events in the NDM check.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify the NAC is configured with a secondary log server in case the primary log is unreachable. 1. Log on to the Forescout UI. 2. Select Tools >> Options >>Syslog >>Syslog Triggers. 3. Verify all boxes in the NAC Events section are checked. This includes the "Include NAC policy logs" and the "Include NAC policy match/unmatch events". If the NAC is not configured with a secondary log server in case the primary log is unreachable, this is a finding.

## Group: SRG-NET-000512-NAC-002310

**Group ID:** `V-233337`

### Rule: Forescout must perform continuous detection and tracking of endpoint devices attached to the network. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233337r811425_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Continuous scanning capabilities on the NAC provide visibility of devices that are connected to the switch ports. The NAC continuously scans networks and monitors the activity of managed and unmanaged devices, which can be personally owned or rogue endpoints. Because many of today's small devices do not include agents, an agentless discovery is often combined to cover more types of equipment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify the NAC performs continuous detection and tracking of endpoint devices attached to the network. 1. Log on to the Forescout UI. 2. Go to Tools >> Options >> Appliance >> IP Assignment. 3. Check that all IP addresses that should be managed are within the IP Assignments as required by the SSP. If the NAC does not perform continuous detection and tracking of endpoint devices attached to the network, this is a finding.

## Group: SRG-NET-000148-NAC-000620

**Group ID:** `V-233338`

### Rule: Forescout must deny network connection for endpoints that cannot be authenticated using an approved method. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-233338r811427_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Identification failure does not need to result in connection termination or preclude compliance assessment. This is particularly true for unmanaged systems or when the NAC is performing network discovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Use the Forescout Administrator UI to verify that a policy exists to deny network connections for endpoints that cannot be authenticated using an approved method and that the authentication failure is logged. 1. Log on to Forescout UI. 2. From the Policy tab, select the Authentication and Authorization policy. 3. Find the 802.1x Authorization policy. If NAC does not have an authorization policy that denies network connection for endpoints that cannot be authenticated using an approved method and log authentication failures, this is a finding.

## Group: SRG-NET-000151-NAC-000630

**Group ID:** `V-233339`

### Rule: Forescout must use a bidirectional authentication mechanism configured with a FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to authenticate with the endpoint device. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233339r856518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Currently, DoD requires the use of AES for bidirectional authentication since it is the only FIPS-validated AES cipher block algorithm. Because of the challenges of applying this requirement on a large scale, organizations are encouraged to apply the requirement only to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Use the Forescout CLI credentials to verify FIPS mode is set by running the "fstool version" command and look for the "FIPS enabled" setting. Log on using the CLIAdmin credentials established upon initial configuration. Verify FIPS mode by typing the command "fstool version". If Forescout does not use AES, this is a finding.

## Group: SRG-NET-000580-NAC-002530

**Group ID:** `V-233340`

### Rule: When connecting with endpoints, Forescout must validate certificates used for Transport Layer Security (TLS) functions by performing RFC 5280-compliant certification path validation. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-233340r811431_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. NAC must be configured for only Certificate Signing. The NAC must interact with TLS-compliant lookups and verification in exchange with endpoints in Extensible Authentication Protocol (EAP) transactions where TLS is supported within the EAP type. Certification path validation includes checks such as certificate issuer trust, time validity, and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Use the Forescout CLI credentials to verify FIPS mode is set by running the "fstool version" command and look for the "FIPS enabled" setting. Use the Forescout Administrator UI to verify SecureConnector is set to use TLS version 1.2 or higher for Client-Server Connections. 1. Log on using the CLIAdmin credentials established upon initial configuration. 2. Verify FIPS mode by typing the command "fstool version". To configure TLS: 1. Log on to the Forescout UI. 2. Select Tools >> Option >> HPS Inspection Engine >> SecureConnector. 3. In the Client-Server Connection, check the Minimum Supported TLS Version is set to TLS version 1.2. If the NAC does not perform RFC 5280-compliant certification path validation for validating certificates used for TLS functions when connecting with endpoints, this is a finding.

