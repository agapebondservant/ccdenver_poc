# STIG Benchmark: Cisco ISE NAC Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000062-NAC-000340

**Group ID:** `V-242575`

### Rule: The Cisco ISE must use TLS 1.2, at a minimum, to protect the confidentiality of information passed between the endpoint agent and the Cisco ISE. This is This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242575r812732_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The agent may pass information about the endpoint to the Cisco ISE, which may be sensitive. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify that only TLS 1.2 is enabled. From the Web Admin portal: 1. Navigate to Administration >> System >> Settings >> Security Settings. 2. Ensure "Allow TLS1.0", "Allow TLS1.1", and "Allow legacy unsafe TLS renegotiation for ISE as a client" are unchecked. If TLS 1.0 or 1.1 is enabled, this is a finding.

## Group: SRG-NET-000015-NAC-000020

**Group ID:** `V-242576`

### Rule: The Cisco ISE must enforce approved access by employing authorization policies with specific attributes; such as resource groups, device type, certificate attributes, or any other attributes that are specific to a group of endpoints, and/or mission conditions as defined in the site's Cisco ISE System Security Plan (SSP). This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242576r812734_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the unauthorized network access. Configuration policy sets with specific authorization policies. Policies consist of rules, where each rule consists of conditions to be met that allow differential access based on grouping of device types by common attributes. ISE requires each authorization policy to have at a minimum one condition. The default authorization policy is the only policy in which there is not a requirement for a condition, nor is it possible to assign a condition to the default authorization policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Verify that the authorization policies have either "deny-access" or restricted access on their default authorization policy set. 1. Work Centers >> Network Access >> Policy Sets. 2. Choose ">" on the desired policy set. 3. Expand Authorization Policy. If the default authorization policy within each policy set has "deny-access" or restricted access, this is not a finding.

## Group: SRG-NET-000015-NAC-000020

**Group ID:** `V-242577`

### Rule: The Cisco ISE must be configured to profile endpoints connecting to the network. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242577r812736_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is possible for endpoints to be manually added to an incorrect endpoint identity group. The endpoint policy can be dynamically set through profiling. If the endpoint group is statically set but the endpoint policy is set to dynamic, then it is possible to identify endpoints that may receive unintended access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Verify the profiling service is configured and enabled. 1. Choose Administration >> System >> Deployment. 2. View the Deployment Nodes. Verify the following services are enabled via the check box: Policy Service Enable Session Services Enable Profiling Services If the Cisco ISE profiling service is not configured and enabled, this is a finding.

## Group: SRG-NET-000015-NAC-000020

**Group ID:** `V-242578`

### Rule: The Cisco ISE must verify host-based firewall software is running on posture required clients defined in the NAC System Security Plan (SSP) prior to granting trusted network access. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242578r812738_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Automated policy assessments must reflect the organization's current security policy so entry control decisions will happen only where remote endpoints meet the organization's security requirements. If the remote endpoints are allowed to connect to the organization's network without passing minimum-security controls, they become a threat to the entire network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. If host-based firewall is not required by the NAC SSP, this is not a finding. Verify that the posture policy will verify that a host-based firewall is running. 1. Navigate to Work Center >> Posture >> Posture Policy. 2. Review the enabled posture policies analyzing all the conditions. 3. Review the requirements listed on polices that the posture required clients will use. 4. Navigate to Work Center >> Posture >> Policy Elements. 5. Review the requirements applied in the posture policy to ensure there is one with a firewall condition applied. 6. Review the firewall condition ensuring it is configured to verify that the client firewall is enabled. If there is not a firewall condition tied to a requirement that is applied to an applicable posture policy, this is a finding.

## Group: SRG-NET-000015-NAC-000020

**Group ID:** `V-242579`

### Rule: The Cisco ISE must verify anti-malware software is installed and up to date on posture required clients defined in the NAC System Security Plan (SSP) prior to granting trusted network access. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242579r1025166_rule`
**Severity:** high

**Description:**
<VulnDiscussion>New viruses and malware are consistently being discovered. If the host-based security software is not current then it will not be able to defend against exploits that have been previously discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DOD is not at C2C Step 4 or higher, this is not a finding. Verify that the posture policy will verify that anti-malware software is installed and up to date. If not required by the NAC SSP, this is not a finding. 1. Navigate to Work Center >> Posture >> Posture Policy. 2. Check the enabled posture policies analyzing all the conditions. 3. Review the requirements listed on polices that the posture required clients will use. 4. Navigate to Work Center >> Posture >> Policy Elements. 5. Review the requirements applied in the posture policy to ensure there are with anti-malware conditions applied. 6. Review the anti-malware conditions ensuring one is configured to verify that the software is installed, and one is configured to make sure the software is up to date. If this requirement is met by another system or application, this is not applicable. If there is not a firewall condition tied to a requirement that is applied to an applicable posture policy, this is a finding.

## Group: SRG-NET-000015-NAC-000020

**Group ID:** `V-242580`

### Rule: The Cisco ISE must verify host-based IDS/IPS software is authorized and running on posture required clients defined in the NAC System Security Plan (SSP) prior to granting trusted network access. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242580r1025168_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Automated policy assessments must reflect the organization's current security policy so entry control decisions will happen only where remote endpoints meet the organization's security requirements. If the remote endpoints are allowed to connect to the organization's network without passing minimum-security controls, they become a threat to the entire network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that the posture policy will verify that a host-based IPS is running. 1. Navigate to Work Center >> Posture >> Posture Policy. 2. Look over the enabled posture policies analyzing all the conditions. 3. Review the requirements listed on polices that the posture required clients will use. 4. Navigate to Work Centers >> Posture >> Policy Elements. 5. Review the requirements applied in the posture policy to ensure there is one with a firewall condition applied. 6. Review the firewall condition ensuring it is configured to verify that the client firewall is enabled. If there is not a firewall condition tied to a requirement that is applied to an applicable posture policy, this is a finding.

## Group: SRG-NET-000015-NAC-000040

**Group ID:** `V-242581`

### Rule: For endpoints that require automated remediation, the Cisco ISE must be configured to redirect endpoints to a logically separate VLAN for remediation services. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242581r812744_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated and manual procedures for remediation for critical security updates will be managed differently. Continuing to assess and remediate endpoints with risks that could endanger the network could impact network usage for all users. This isolation prevents traffic from flowing with traffic from endpoints that have been fully assessed and authorized. Unauthenticated devices must not be allowed to connect to remediation services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that the authorization policies for "Posture NonCompliant" have a result that will assign the remediation VLAN. 1. Work Centers >> Network Access >> Policy Sets. 2. Choose ">" on the desired policy set. 3. Expand Authorization Policy. 4. Scan for Authorization policies with "Posture NonCompliant" condition. 5. Verify the result assigned to the authorization policy will assign the remediation VLAN. If the result is the remediation VLAN, this is not a finding. If posture is not mandated by the Information System Security Manager (ISSM), this is not a finding.

## Group: SRG-NET-000015-NAC-000070

**Group ID:** `V-242582`

### Rule: The Cisco ISE must be configured to notify the user before proceeding with remediation of the user's endpoint device when automated remediation is used. This is required for compliance with C2C Step 3.

**Rule ID:** `SV-242582r812746_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Notification will let the user know that installation is in progress and may take a while. This notice may deter the user from disconnecting and retrying the connection before the remediation is completed. Premature disconnections may increase network demand and frustrate the user. Note: This policy does not require remediation to be performed by the Cisco ISE, but will apply if remediation services are used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 3 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that each requirement used has a message to display. 1. Navigate to Work Centers >> Posture >> Posture Policy. 2. Make a note of each "Requirement" tied to an enabled Posture Policy. 3. Navigate to Work Centers >> Posture >> Policy Elements >> Requirements. 4. Verify that each requirement noted has a message in the "Message Shown to Agent User" box. If a requirement that is used does not have a message, this is a finding.

## Group: SRG-NET-000015-NAC-000080

**Group ID:** `V-242583`

### Rule: The Cisco ISE must be configured so that all endpoints that are allowed to bypass policy assessment are approved by the Information System Security Manager (ISSM) and documented in the System Security Plan (SSP). This is This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242583r812748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Connections that bypass established security controls should be only in cases of administrative need. These procedures and use cases must be approved by the Information System Security Manager (ISSM).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Review the posture policy to ensure mandated endpoints are being assed and if there are exceptions to the policy that they are documented and approved by the ISSM. 1. Navigate to Work Centers >> Posture >> Posture Policy. 2. Examine the enabled Posture Policies to determine if the endpoints that are mandated to be assessed will use the required policies. 3. If there is an endpoint type that should be assessed and there is a condition or conditions exempting a sub group of that endpoint type, verify that the sub group is documented and approved by the ISSM. If the policy will not be applied to required endpoints or if exempted endpoints are not approved and documented, this is a finding.

## Group: SRG-NET-000015-NAC-000100

**Group ID:** `V-242584`

### Rule: The Cisco ISE must send an alert to the Information System Security Manager (ISSM) and System Administrator (SA), at a minimum, when security issues are found that put the network at risk. This is required for compliance with C2C Step 2.

**Rule ID:** `SV-242584r812750_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trusted computing should require authentication and authorization of both the user's identity and the identity of the computing device. An authorized user may be accessing the network remotely from a computer that does not meet DoD standards. This may compromise user information, particularly before or after a VPN tunnel is established.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 2 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that an alarm will be generated and sent when an endpoint has a change in posture status. From the Web Admin portal: 1. Choose Administration >> System >> Logging >> Logging Categories. 2. Verify the "AAA Audit", "Failed Attempts", and "Posture and Client Provisioning Audit" have LogCollector set as a target at a minimum. If the Posture and Client Provisioning Audit logging category is not configured to send to the LogCollector and/or another logging target, this is a finding.

## Group: SRG-NET-000015-NAC-000110

**Group ID:** `V-242585`

### Rule: When endpoints fail the policy assessment, the Cisco ISE must create a record with sufficient detail suitable for forwarding to a remediation server for automated remediation or sending to the user for manual remediation. This is required for compliance with C2C Step 3. 

**Rule ID:** `SV-242585r812752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing the NAC assessment means that an unauthorized machine has attempted to access the secure network. Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 3 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that each requirement used has a message to display. 1. Navigate to Work Centers >> Posture >> Posture Policy. 2. Make a note of each "Requirement" tied to an enabled Posture Policy. 3. Navigate to Work Centers >> Posture >> Policy Elements >> Requirements. 4. Verify that each requirement noted has a message in the "Message Shown to Agent User" box. If a requirement that is used does not have a message, this is a finding.

## Group: SRG-NET-000015-NAC-000120

**Group ID:** `V-242586`

### Rule: The Cisco ISE must place client machines on the blacklist and terminate the agent connection when critical security issues are found that put the network at risk. This is required for compliance with C2C Step 4.



**Rule ID:** `SV-242586r1018688_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the Cisco ISE devices and servers should have no legitimate reason for communicating with other devices outside of the assessment solution, any direct communication with unrelated hosts would be suspect traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that blacklisted devices will be denied access or quarantined. 1. Navigate to Work Centers >> Network Access >> Policy Sets. 2. Choose ">" on the applicable policy set. 3. Expand the "Authorization Policy – Global Exceptions". 4. Verify that a rule with the condition "Session-ANCPolicy EQUALS <Configured ANC Policy>", or "IdentityGroup-Name EQUALS Endpoint Identity Group:Blocklist" is present with a result that will deny access or quarantine the endpoint. If the enforcement is completed in the Authorization Policy versus the Global Exceptions, then each policy set must contain a policy for blacklisted endpoints. If there is not an authorization policy for Blacklist endpoints, this is a finding. If the authorization policy does not restrict or deny the access of blacklisted endpoints, this is a finding.

## Group: SRG-NET-000015-NAC-000130

**Group ID:** `V-242587`

### Rule: The Cisco ISE must be configured so client machines do not communicate with other network devices in the DMZ or subnet except as needed to perform an access client assessment or to identify themselves. This is required for compliance with C2C Step 2.

**Rule ID:** `SV-242587r812756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Devices not compliant with DoD secure configuration policies are vulnerable to attack. Allowing these systems to connect presents a danger to the enclave. This requirement gives the option to configure for automated remediation and/or manual remediation. Detailed record must be passed to the remediation server for action. Alternatively, the details can be passed in a notice to the user for action. The device status will be updated on the network access server/authentication server so that further access attempts are denied. The Cisco ISE should have policy assessment mechanisms with granular control to distinguish between access restrictions based on the criticality of the software or setting failure. Configure reminders to be sent to the user and the SA periodically or at a minimum, each time a policy assessment is performed. This can be done via the Cisco ISE or any notification system. The failure must also be used to update the HBSS agent.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 2 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify the authorization policy will prevent intra-remediation VLAN communication. 1. Navigate to Policy >> Policy Elements >> Results. 2. Choose ">" on the applicable policy set. 3. Expand the Authorization Policy. 4. Verify that a rule with the condition "Session-PostureStatus EQUALS NonCompliant" or an authorization policy for remediation is present making a note of the authorization profile. 5. Navigate to Policy >> Policy Elements >> Results >> Authorization >> Authorization Profiles >> Authorization profile noted above. 6. Ensure the result that is used will result in lateral traffic for that VLAN will be restricted by a private VLAN, dACL, ACL, SGT, or any combination. 7. If a private VLAN is used, review the switch configuration to confirm it is a private VLAN. If there is not an authorization policy for NonCompliant clients or remediation, this is a finding. If the authorization policy does not prevent intra-remediation VLAN communication, this is a finding.

## Group: SRG-NET-000322-NAC-001230

**Group ID:** `V-242588`

### Rule: The Cisco ISE must deny or restrict access for endpoints that fail required posture checks. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242588r1001248_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Devices, which do not meet minimum-security configuration requirements, pose a risk to the DOD network and information assets. Endpoint devices must be disconnected or given limited access as designated by the approval authority and system owner if the device fails the authentication or security assessment. The user will be presented with a limited portal, which does not include access options for sensitive resources. Required security checks must implement DOD policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DOD is not at C2C Step 4 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that the Policy Set will enforce the posture assessment. 1. Navigate to Work Centers >> Network Access >> Policy Sets. 2. Choose ">" on the applicable policy set. 3. Expand the Authorization Policy. 4. Verify that the Attribute of PostureStatus of NonCompliant is configured in the policy. 5. Make a note of the result/results on the NonCompliant Policy. 6. Navigate to Policy >> Policy >> Elements >> Results >> Authorization. 7. Expand Authorization. 8. Choose Authorization Profiles. 9. View the Standard Authorization Profile/Profiles noted above to ensure that a remediation VLAN, Access Control List, Scalable Group Tag, or any combination of these are used to restrict access. If there is not a "NonCompliant" authorization rule or the result is not restrictive, this is a finding.

## Group: SRG-NET-000492-NAC-002100

**Group ID:** `V-242589`

### Rule: The Cisco ISE must generate a log record when an endpoint fails authentication. This is This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242589r812760_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing the Cisco ISE assessment means that an unauthorized machine has attempted to access the secure network. Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that a log will be generated and sent when an Endpoint has a change in posture status. From the Web Admin portal: 1. Choose Administration >> System >> Logging >> Logging Categories. 2. Verify the Failed Attempts has LogCollector set as a target at a minimum. If the Failed Attempts logging category is not configured to send to the LogCollector and/or another logging target, this is a finding.

## Group: SRG-NET-000492-NAC-002101

**Group ID:** `V-242590`

### Rule: The Cisco ISE must generate a log record when the client machine fails posture assessment because required security software is missing or has been deleted. This is This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242590r812762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing the Cisco ISE assessment means an unauthorized machine has attempted to access the secure network. Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Log records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that a log will be generated and sent when an Endpoint has a change in posture status. From the Web Admin portal: 1. Choose Administration >> System >> Logging >> Logging Categories. 2. Verify the Posture and Client Provisioning Audit has LogCollector set as a target at a minimum. If the Posture and Client Provisioning Audit logging category is not configured to send to the LogCollector and/or another logging target, this is a finding.

## Group: SRG-NET-000492-NAC-002120

**Group ID:** `V-242591`

### Rule: The Cisco ISE must send an alert to the system administrator, at a minimum, when endpoints fail the policy assessment checks for organization-defined infractions. This is required for compliance with C2C Step 3.

**Rule ID:** `SV-242591r812764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing the Cisco ISE assessment, means that an unauthorized machine has attempted to access the secure network. Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Log records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 3 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that an alarm will be generated and sent when an endpoint has a change in posture status. From the Web Admin portal: 1. Choose Administration >> System >> Logging >> Logging Categories. 2. Verify the Posture and Client Provisioning Audit has LogCollector set as a target at a minimum. If the Posture and Client Provisioning Audit logging category is not configured to send to the LogCollector and/or another logging target, this is a finding.

## Group: SRG-NET-000335-NAC-001360

**Group ID:** `V-242594`

### Rule: The Cisco ISE must generate a critical alert to be sent to the ISSO and SA (at a minimum) in the event of an audit processing failure. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242594r855855_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without an alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Cisco ISE provides system alarms which notify the administrator when critical system condition occurs. Alarms are displayed in the Alarm dashlet. Administrators can configured the dashlet to receive notification of alarms through e-mail and/or syslog messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify the Cisco ISE will notify one or more individuals when there is a Log Collection Error. From the Web Admin portal: 1. Choose Administration >> System >> Settings >> Alarm Settings. 2. Select "Log Collector Error" from the list of default alarms and click "Edit". 3. Verify that "Enable" is selected. 4. Select "Enter Multiple Emails Separated with Comma". 5. Verify one or more email addresses are configured. If "Log Collector Error" alarm type is not enabled or email addresses are not configured to receive the alert, this is a finding.

## Group: SRG-NET-000335-NAC-001370

**Group ID:** `V-242595`

### Rule: The Cisco ISE must provide an alert to, at a minimum, the SA and ISSO of all audit failure events where the detection and/or prevention function is unable to write events to either local storage or the centralized server. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242595r855856_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less). This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify the Cisco ISE will notify one or more individuals when there is a Log Collection Error. From the Web Admin portal: 1. Choose Administration >> System >> Settings >> Alarm Settings. 2. Select "Log Collector Error" from the list of default alarms and click "Edit". 3. Verify that "Enable" is selected. 4. Select "Enter Multiple Emails Separated with Comma". 5. Verify one or more email addresses are configured. If "Log Collector Error" alarm type is not enabled or email addresses are not configured to receive the alert, this is a finding.

## Group: SRG-NET-000336-NAC-001390

**Group ID:** `V-242596`

### Rule: The Cisco ISE must be configured with a secondary log server in case the primary log is unreachable. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242596r1001250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Review the configured Remote Logging Targets to ensure there are, at a minimum, two configured. From the Web Admin portal: 1. Choose Administration >> System >> Logging >> Logging Targets. 2. Verify that "LogCollector" and "LogCollector2" or an additional target is defined along with being enabled. If there are not two separate logging targets defined, this is a finding. Note: "ProfilerRadiusProbe" or any other target with a "127.0.0.1" address does not count as being a "Remote" Logging Target.

## Group: SRG-NET-000088-NAC-000440

**Group ID:** `V-242597`

### Rule: The Cisco ISE must generate a critical alert to be sent to the ISSO and SA (at a minimum) if it is unable to communicate with the central event log. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242597r812776_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where log records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify that a log will be generated and sent when a Logging Target becomes unavailable. From the Web Admin portal: 1. Choose Administration >> System >> Logging >> Logging Categories. 2. Verify that Internal Operations Diagnostics has "LogCollector" and "LogCollector2" set. If there are a minimum of two logging targets selected for Internal Operations Diagnostics, this is not a finding.

## Group: SRG-NET-000089-NAC-000450

**Group ID:** `V-242598`

### Rule: The Cisco ISE must continue to queue traffic log records locally when communication with the central log server is lost and there is an audit archival failure. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242598r812778_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the network element is at risk of failing to process traffic logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend on the nature of the failure mode. In accordance with DoD policy, the traffic log must be sent to a central audit server. When logging functions are lost, system processing cannot be shut down because NAC availability is an overriding concern given the role of the firewall in the enterprise. The system should either be configured to log events to an alternative server or queue log records locally. Upon restoration of the connection to the central log server, action should be taken to synchronize the local log data with the central audit server. If the central audit server uses User Datagram Protocol (UDP) communications instead of a connection-oriented protocol such as TCP, a method for detecting a lost connection must be implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify that logging targets are configured to buffer syslog messages when the server is down. From the Web Admin portal: 1. Choose Administration >> System >> Logging >> Remote Logging Targets. 2. Select remote targets and verify that "Buffer Messages When Server Down" box is checked. Note: If "LogCollector" and "LogCollector2" are configured for UDP and ISE Messaging service is configured, this is not a finding. Verify that ISE Messaging Service is enabled. From the Web Admin portal: 1. Choose Administration >> System >> Logging >> Log Settings. 2. Verify that "Use ISE Messaging Service for UDP Syslogs delivery to MnT" box is checked. If messages are not buffered for remote syslog servers, this is a finding.

## Group: SRG-NET-000512-NAC-002310

**Group ID:** `V-242599`

### Rule: The Cisco ISE must perform continuous detection and tracking of endpoint devices attached to the network. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242599r812780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Continuous scanning capabilities on the Cisco ISE provide visibility of devices that are connected to the switch ports. The Cisco ISE continuously scans networks and monitors the activity of managed and unmanaged devices, which can be personally owned or rogue endpoints. Because many of today's small devices do not include agents, an agentless discovery is often combined to cover more types of equipment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Review the posture settings to ensure Continuous Monitoring Interval is enabled and a value configured. From the Web Admin portal: 1. Choose Work Centers >> Posture >> Settings >> Posture General Settings. 2. Verify that "Continuous Monitoring Interval" is enabled and an interval configured. If "Continuous Monitoring Interval" is not enabled with an interval defined, this is a finding.

## Group: SRG-NET-000148-NAC-000620

**Group ID:** `V-242600`

### Rule: The Cisco ISE must deny network connection for endpoints that cannot be authenticated using an approved method. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242600r812782_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Identification failure does not need to result in connection termination or preclude compliance assessment. This is particularly true for unmanaged systems or when the Cisco ISE is performing network discovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Verify that the authorization policies have either "deny-access" or restricted access on their default authorization policy set. 1. Work Centers >> Network Access >> Policy Sets. 2. Choose ">" on the desired policy set. 3. Expand Authorization Policy. If the default authorization policy within each policy set has "deny-access" or restricted access, this is not a finding.

## Group: SRG-NET-000343-NAC-001460

**Group ID:** `V-242601`

### Rule: The Cisco ISE must authenticate all endpoint devices before establishing a connection and proceeding with posture assessment. This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242601r855858_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. However, failure to authenticate an endpoint does not need to result in connection termination or preclude compliance assessment. This is particularly true for unmanaged systems or when the Cisco ISE is performing network discovery. Authentication methods for NAC on access switches are MAC Authentication Bypass (MAB), or 802.1x.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify that the authorization policies have either "deny-access" or restricted access on their default authorization policy set. 1. Work Centers >> Network Access >> Policy Sets. 2. Choose ">" on the desired policy set. 3. Expand Authorization Policy. If the default authorization policy within each policy set has "deny-access" or restricted access, this is not a finding.

## Group: SRG-NET-000343-NAC-001470

**Group ID:** `V-242602`

### Rule: The Cisco ISE must be configured to dynamically apply restricted access of endpoints that are granted access using MAC Authentication Bypass (MAB). This is required for compliance with C2C Step 4.

**Rule ID:** `SV-242602r855859_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MAB can be defeated by spoofing the MAC address of a valid device. MAB enables port-based access control using the MAC address of the endpoint. A MAB-enabled port can be dynamically enabled or disabled based on the MAC address of the device that connects to it. NPE devices that can support PKI or an allowed authentication type must use PKI. MAB may be used for NPE that cannot support an approved device authentication. Non-entity endpoints include IoT devices, VOIP phone, and printer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 4 or higher, this is not a finding. Verify that the authorization policies for devices granted access via MAB will have restricted access. 1. Navigate to Work Centers >> Network Access >> Policy Sets. 2. Choose ">" on the applicable policy set. 3. Expand the Authorization Policy. 4. Make a note of the result/results on each authorization policy for MAB. 5. Navigate to Policy >> Policy Elements >> Results >> Authorization. 6. Expand "Authorization". 7. Choose "Authorization Profiles". 8. View the Standard Authorization Profile/Profiles noted above to ensure that a restricted VLAN, Access Control List, Scalable Group Tag, or any combination of these is used to restrict access. If a VLAN is the only thing being applied to the session and the VLAN has an ACL on the layer 3 interface, this is not a finding. If there is not a restriction on an MAB authorization policy, this is a finding.

## Group: SRG-NET-000550-NAC-002470

**Group ID:** `V-242603`

### Rule: Before establishing a connection with a Network Time Protocol (NTP) server, the Cisco ISE must authenticate using a bidirectional, cryptographically based authentication method that uses a FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to authenticate with the NTP server. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242603r878130_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the NTP server is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source. Currently, AES block cipher algorithm is approved for use in DoD for both applying cryptographic protection (e.g., encryption) and removing or verifying the protection that was previously applied (e.g., decryption). NTP devices use MD5 authentication keys. The MD5 algorithm is not specified in either the FIPS or NIST recommendation. However, MD5 is preferred to no authentication at all. The trusted-key statement permits authenticating NTP servers. The product must be configured to support separate keys for each NTP server. Severs should have a PKI device certificate involved for use in the device authentication process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. Verify NTP setting to ensure NTP will be authenticated. From the CLI: 1. Type "show running-config | in ntp". 2. Verify that each defined NTP server has a key on the same line defining the server and make a note of the key number. 3. Verify that each NTP Key number used is created. If there is an NTP source without an NTP key defined and it is a domain controller, this is not a finding as Windows server does not support NTP keys. If there are any other NTP sources that do not use a defined key, this is a finding. Note: Each ISE node must be individually checked as NTP settings are local to each appliance. Note: There are NTP settings in the GUI; however, it is recommended to use the NTP setting solely in CLI to prevent issues.

## Group: SRG-NET-000151-NAC-000630

**Group ID:** `V-242604`

### Rule: Before establishing a local, remote, and/or network connection with any endpoint device, the Cisco ISE must use a bidirectional authentication mechanism configured with a FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to authenticate with the endpoint device. This is required for compliance with C2C Step 1.

**Rule ID:** `SV-242604r971529_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Currently, DoD requires the use of AES for bidirectional authentication since it is the only FIPS-validated AES cipher block algorithm. Because of the challenges of applying this requirement on a large scale, organizations are encouraged to apply the requirement only to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DoD is not at C2C Step 1 or higher, this is not a finding. From the Web Admin portal: 1. Navigate to Administration >> System >> Settings >> Security Settings. 2. Ensure "Allow TLS1.0", "Allow TLS1.1", and "Allow legacy unsafe TLS renegotiation for ISE as a client" are unchecked. If TLS 1.0 or 1.1 is enabled, this is a finding.

## Group: SRG-NET-000512-NAC-002310

**Group ID:** `V-242605`

### Rule: The Cisco ISE must enforce posture status assessment for posture required clients defined in the NAC System Security Plan (SSP). This is required for compliance with C2C Step 3.

**Rule ID:** `SV-242605r944370_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Posture assessments can reduce the risk that clients impose on networks by restricting or preventing access of noncompliant clients. If the posture assessment is not enforced, then access of clients not complying is not restricted allowing the risk of vulnerabilities being exposed. Though the configuration is out of scope, one of the ways to allow posturing with Cisco AnyConnect Secure Mobility Client is to enable http redirect on the network switch so that AnyConnect can connect to ISE's Client Provisioning Portal (call home). Every effort must be taken to configure this function without the need to require the command 'ip http server' on the switch (see V-220534 in the Network Infrastructure STIG). If deemed operationally necessary, the site must obtain AO approval and document the variation from V-220534, risk mitigations, and the mission need that makes the service necessary. If the service is operationally necessary to meet C2C compliance for posture assessment and a vendor-provided alternative is not available, then it is, by definition, a necessary service. Thus, V-220534 is not a finding as it states that "If a particular capability is used, then it must be documented and approved."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DOD is not at C2C Step 3 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify the authorization policy will enforce posture assessment status for posture required clients. 1. Navigate to Work Centers >> Network Access >> Policy Sets. 2. Choose ">" on the applicable policy set. 3. Expand the Authorization Policy. 4. Verify that a rule with the condition "Session-PostureStatus EQUALS NonCompliant" is present and will apply to posture required devices by analyzing other conditions used on the same policy. 5. Ensure the result that is used for remediation access is a restricted VLAN, ACL, SGT, or any combination used to restrict the access. If there is not an authorization policy for NonCompliant clients that are posture required, this is a finding. If the authorization policy does not restrict the access of NonCompliant clients that are posture required, this is a finding.

## Group: SRG-NET-000512-NAC-002310

**Group ID:** `V-242606`

### Rule: The Cisco ISE must have a posture policy for posture required clients defined in the NAC System Security Plan (SSP). This is required for compliance with C2C Step 2.

**Rule ID:** `SV-242606r944368_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Posture assessments can reduce the risk that clients impose on networks. The posture policy is the function that can link requirements to applicable clients. Multiple requirements can be associated with a single policy. However, multiple polices can also be applicable to the same client. The posture policy operates in such a way that all applicable policies are applied, versus the top-down first match approach.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DOD is not at C2C Step 2 or higher, this is not a finding. If not required by the NAC SSP, this is not a finding. Verify the posture policy for posture required clients. 1. Navigate to Work Centers >> Posture >> Posture Policy. 2. Review the enabled posture policies to ensure posture required endpoints will process requirements. If there is not an enabled policy that will be applied to posture required endpoints, this is a finding.

