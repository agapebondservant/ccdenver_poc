# STIG Benchmark: Ivanti MobileIron Sentry 9.x ALG Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-251008`

### Rule: The Sentry must enforce approved authorizations for logical access to information and system resources by enabling identity-based, role-based, and/or attribute-based security policies. These controls are enabled in MobileIron UEM (MobileIron Core) and applied by the Sentry for conditional access enforcement.

**Rule ID:** `SV-251008r802246_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication through Sentry must not automatically give an entity access to resources behind Sentry. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the MobileIron Sentry is configured to enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and attribute-based security policies. The Sentry system configured for ActiveSync, AppTunnel, and/or as a Kerberos Proxy ensures only authenticated and authorized apps and managed devices have access to backend resources. Refer to the MobileIron Sentry 9.8.0 Guide for Core pages 20-21 for more information. 1. Log in to the Core Admin Portal. 2. Go to Service >> Sentry. 3. Verify the Sentry is configured with one or all the of the applicable services (ActiveSync, AppTunnel, or Kerberos Proxy). If no services are applied, this is a finding. 4. If Sentry is being used as an ActiveSync Proxy or AppTunnel, verify an Identity Certificate is configured for the Device Authentication Configuration in the Sentry Configuration and that CRL is enabled. If not, this is a finding. Refer to the MobileIron Sentry 9.8.0 Guide on how to configure the specific Sentry Services. ActiveSync: Standalone Sentry for ActiveSync Email Section, AppTunnel: Standalone Sentry for AppTunnel Section Kerberos Proxy: Standalone Sentry for KKDCP Section. MobileIron UEM applies security, privacy, lockdown, and sync policies to registered devices. These policies ensure that devices can connect only if they comply to an organization’s security requirements. Standalone Sentry gets device posture and compliance information from MobileIron UEM, and allows access to Email via ActiveSync or backend systems based on the device posture. 1. Log in to the Core Admin Portal. 2. Go to Policies and Configurations >> Policies. 3. Verify the appropriate Lockdown and Security Policies are applied to the devices accessing systems behind the Sentry. If no policies are applied, this is a finding. By default, Sentry allows unregistered devices to access the ActiveSync server. Use this setting to change Sentry’s behavior to block unregistered devices from access if configuring Sentry for ActiveSync. 1. Log in to the Core Admin Portal. 2. Go to Services >> Sentry >> Preferences. 3. Verify "Yes" for Auto Block Unregistered Devices is applied. If not applied, this is a finding.

## Group: SRG-NET-000018-ALG-000017

**Group ID:** `V-251009`

### Rule: The Sentry must enforce approved authorizations for controlling the flow of information within the network based on attribute-based inspection of the source, destination, and headers, of the communications traffic.

**Rule ID:** `SV-251009r802249_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Sentry enforces approved authorizations by employing security policy and/or rules configured in MobileIron UEM that restrict information system services capability based on header or protocol information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry and MobileIron UEM is configured to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. MobileIron UEM applies Configurations to devices/users based on manual or dynamic labels. Verify that Configurations that leverage Sentry such as Email, VPN, Docs@Work, or any backend service which leverage Sentry as a gateway are applied to the appropriate user groups via the configurable labels. If not, this is a finding. 1. Log in to the Core Admin Portal. 2. Go to Policies and Configurations >> Configurations. 3. Verify the Sentry related Configurations are applied to the devices accessing systems behind the Sentry. If Configurations are misassigned to the wrong label/user groups, this is a finding.

## Group: SRG-NET-000019-ALG-000018

**Group ID:** `V-251010`

### Rule: The Sentry must restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-251010r802252_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. Blocking or restricting detected harmful or suspicious communications between interconnected networks enforces approved authorizations for controlling the flow of traffic. This requirement applies to the flow of information between the Sentry when used as a gateway or boundary device which allows traffic flow between interconnected networks of differing security policies. The Sentry and MobileIron UEM must be configured with policy filters (e.g., security policy and compliance rules) that restrict or block information system services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry restricts or blocks harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on mobile device security posture reported by the MobileIron UEM. 1. Log in to the Core Admin Portal. 2. Go to Policies and Configurations >> Policies. 3. Verify the appropriate Security Policies are applied to the devices accessing systems behind the Sentry. 4. Click "Edit". 5. In the Access Control section of the policy, verify the Block Email and AppConnect apps compliance action is selected for the "when a compromised device is detected" control for the iOS and Android device operating systems sections. 6. Click "Cancel". If "when a compromised device is detected" control for the iOS and Android device operating systems is not selected in the Access control section, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-251011`

### Rule: The Sentry providing intermediary services for remote access communications traffic must use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-251011r802255_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Encryption provides a means to secure the remote connection so as to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry uses encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. On the MobileIron Sentry CLI console, do the following: 1. SSH to MobileIron Sentry Server from any SSH client. 2. Enter the administrator credentials established when MobileIron Sentry was installed. 3. Enter "enable". 4. When prompted, enter the "enable secret" set when MobileIron Sentry was installed. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If the MobileIron Sentry Server does not report that FIPS mode is "enabled", this is a finding.

## Group: SRG-NET-000062-ALG-000092

**Group ID:** `V-251012`

### Rule: If Sentry stores secret or private keys, it must use FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys.

**Rule ID:** `SV-251012r802258_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry uses encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. On the MobileIron Sentry CLI console, do the following: 1. SSH to MobileIron Sentry Server from any SSH client. 2. Enter the administrator credentials set when MobileIron Sentry was installed. 3. Enter "enable". 4. When prompted, enter the "enable secret" set when MobileIron Sentry was installed. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If the MobileIron Sentry Server does not report that FIPS mode is "enabled", this is a finding.

## Group: SRG-NET-000062-ALG-000150

**Group ID:** `V-251013`

### Rule: The Sentry that provides intermediary services for TLS must be configured to comply with the required TLS settings in NIST SP 800-52.

**Rule ID:** `SV-251013r802261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SP 800-52 provides guidance on using the most secure version and configuration of the TLS/SSL protocol. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks which exploit vulnerabilities in this protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry is configured to implement the applicable required TLS settings in NIST PUB SP 800-52. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Services >> Sentry. 3. For each of the following configurations, follow the step 4 procedure: a. Incoming SSL configuration b. Outgoing SSL configuration c. UEM SSL configuration d. Access SSL configuration 4. Verify only TLS 1.2 is selected. If any other protocol is selected, this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 guide for Core" and refer the main section "Standalone Sentry Settings", which includes subsections on how TLS 1.2 is set as the default protocol: 1. Incoming SSL configuration 2. Outgoing SSL configuration 3. UEM SSL configuration 4. Access SSL configuration MobileIron Sentry conforms to the NIST SP 800-52 TLS settings by setting TLS 1.2 by default.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-251014`

### Rule: The Sentry providing intermediary services for remote access communications traffic must use NIST FIPS-validated cryptography to protect the integrity of remote access sessions.

**Rule ID:** `SV-251014r802264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry uses encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. On the MobileIron Sentry CLI console, do the following: 1. SSH to MobileIron Sentry Server from any SSH client. 2. Enter the administrator credentials set when MobileIron Sentry was installed. 3. Enter "enable". 4. When prompted, enter the "enable secret" set when MobileIron Sentry was installed. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If the MobileIron Sentry Server does not report that FIPS mode is "enabled", this is a finding.

## Group: SRG-NET-000074-ALG-000043

**Group ID:** `V-251015`

### Rule: The Sentry must produce audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-251015r802267_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the gateway logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element. This requirement does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry produces audit records containing information to establish what type of events occurred. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Syslog. 3. Verify a syslog server is configured. 4. Click on the syslog server(s) and in the "Modify Syslog" pop-up dialog, under the "Facility Type", verify the checkbox for "Audit" is selected. If the syslog server is not configured or "Audit" is not selected under "Modify Syslog", this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the section "Standalone Sentry Settings", which includes a subsection detailing the log representation format in "Audit log representation and format". The audit logs contain additional information on the type of events that occurred. Also included is date and timestamp, the source of the event, the location of the event, and the result of the action whether a success or failure.

## Group: SRG-NET-000075-ALG-000044

**Group ID:** `V-251016`

### Rule: The Sentry must produce audit records containing information to establish when (date and time) the events occurred.

**Rule ID:** `SV-251016r802270_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment, and provide forensic analysis of network traffic patterns, it is essential for security personnel to know when flow control events occurred within the infrastructure. Associating event types with detected events in the network audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element. This requirement does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry produces audit records containing information to establish when (date and time) the events occurred. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Syslog. 3. Verify a syslog server is configured. 4. Click on the syslog server(s) and in the "Modify Syslog" pop-up dialog, under the "Facility Type", verify the checkbox for "Audit" is selected. If the syslog server is not configured or "Audit" is not selected under "Modify Syslog", this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the main section "Standalone Sentry Settings", which includes a subsection detailing the log representation format in "Audit log representation and format". The audit logs contain additional information on the type of events that occurred. Also included is the date and timestamp, the source of the event, the location of the event, and the result of the action whether a success/failure.

## Group: SRG-NET-000076-ALG-000045

**Group ID:** `V-251017`

### Rule: The Sentry must produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-251017r802273_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment, and provide forensic analysis, it is essential for security personnel to know where events occurred, such as network element components, modules, device identifiers, node names, and functionality. Associating information about where the event occurred within the network provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element. This requirement does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry produces audit records containing information to establish where the events occurred. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Syslog. 3. Verify a syslog server is configured. 4. Click on the syslog server(s) and in the "Modify Syslog" pop-up dialog, under the "Facility Type", verify the checkbox for "Audit" is selected. If the syslog server is not configured or "Audit" is not selected under "Modify Syslog", this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the main section "Standalone Sentry Settings", which includes a subsection detailing the log representation format in "Audit log representation and format". The audit logs contain additional information on the type of events that occurred. Also included is the date and timestamp, the source of the event, the location of the event, the result of the action whether a success or failure.

## Group: SRG-NET-000077-ALG-000046

**Group ID:** `V-251018`

### Rule: The Sentry must produce audit records containing information to establish the source of the events.

**Rule ID:** `SV-251018r802276_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry produces audit records containing information to establish the source of the events. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Syslog. 3. Verify a syslog server is configured. 4. Click on the syslog server(s) and in the "Modify Syslog" pop-up dialog, under the "Facility Type", verify the checkbox for "Audit" is selected. If the syslog server is not configured or "Audit" is not selected under "Modify Syslog", this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the main section "Standalone Sentry Settings", which includes a subsection detailing the log representation format in "Audit log representation and format". The audit logs contain additional information on the type of events that occurred. Also included is date and timestamp, the source of the event, the location of the event, and the result of the action whether a success or failure.

## Group: SRG-NET-000078-ALG-000047

**Group ID:** `V-251019`

### Rule: The Sentry must produce audit records containing information to establish the outcome of the events.

**Rule ID:** `SV-251019r802279_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the network. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the network after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response. This requirement does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry produces audit records containing information to establish the outcome of the events. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Syslog. 3. Verify a syslog server is configured. 4. Click on the syslog server(s) and in the "Modify Syslog" pop-up dialog, under the "Facility Type", verify the checkbox for "Audit" is selected. If the syslog server is not configured or if "Audit" is not selected under "Modify Syslog", this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer the following main section "Standalone Sentry Settings" under which there is a sub-section detailing the log representation format in "Audit log representation and format". The audit logs contain additional information on the type of events that occurred. Also included is the date and timestamp, the source of the event, the location of the event, and the result of the action whether a success/failure.

## Group: SRG-NET-000079-ALG-000048

**Group ID:** `V-251020`

### Rule: The Sentry must generate audit records containing information to establish the identity of any individual or process associated with the event.

**Rule ID:** `SV-251020r802282_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event. Associating information about where the event occurred within the network provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element. This requirement does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry produces audit records containing information to establish the outcome of the events. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Syslog. 3. Verify a syslog server is configured. 4. Click on the syslog server(s) and in the "Modify Syslog" pop-up dialog, under the "Facility Type", verify the checkbox for "Audit" is selected. If the syslog server is not configured or "Audit" is not selected under "Modify Syslog", this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the main section "Standalone Sentry Settings", which includes a subsection detailing the log representation format in "Audit log representation and format". The audit logs contain additional information on the type of events that occurred. Also included is date and timestamp, the source of the event, the location of the event, and the result of the action whether a success/failure.

## Group: SRG-NET-000088-ALG-000054

**Group ID:** `V-251021`

### Rule: The Sentry must send an alert to, at a minimum, the ISSO and SCA when an audit processing failure occurs.

**Rule ID:** `SV-251021r802285_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Possible audit processing failures also include the inability of Sentry to write to the central audit log. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations, (i.e., all audit data storage repositories combined), or both. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry sends an alert to, at a minimum, the ISSO and SCA when an audit processing failure occurs. 1. Log in to MobileIron Sentry. 2. Go to Monitoring >> Alert Configuration. 3. Verify "Send Notifications" is enabled. 4. Verify an email list containing the ISSM and SCA is input in the Email List. 5. Verify "Alert Notification Management" section is set to meet organizational requirements. If the "Alert Notification Management" section is not set to meet organizational requirements, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-251022`

### Rule: The Sentry must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-251022r802288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The ALG is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements. Satisfies: SRG-NET-000132-ALG-000087, SRG-NET-000512-ALG-000062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the configuration and vendor documentation of the Sentry application to find the minimum ports, protocols, and services required for Sentry operation. 1. Log in to MobileIron Sentry System Manager. 2. Go to Security >> Access Control Lists >> ACLs. 3. Check all the ACLs to determine if the service restricted has an ACL already available. If it does not, this is a finding.

## Group: SRG-NET-000138-ALG-000088

**Group ID:** `V-251023`

### Rule: The Sentry providing mobile device access control intermediary services must be configured with a pre-established trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or AAA server) which validate mobile device account access authorizations and privileges.

**Rule ID:** `SV-251023r802291_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User account and privilege validation must be centralized in order to prevent unauthorized access using changed or revoked privileges. ALGs can implement functions such as traffic filtering, authentication, access, and authorization functions based on computer and user privileges. However, the directory service (e.g., Active Directory or LDAP) must not be installed on the ALG, particularly if the gateway resides on the untrusted zone of the Enclave.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the MobileIron Core configured with the MobileIron Sentry is enabled with Active Directory or LDAP server. 1. Log in to the MobileIron Core MIFS portal. 2. Go to Services >> LDAP. 3. Verify an LDAP server is configured and enabled. If an LDAP server is not configured and enabled, this is a finding.

## Group: SRG-NET-000138-ALG-000089

**Group ID:** `V-251024`

### Rule: The Sentry providing mobile device authentication intermediary services must restrict mobile device authentication traffic to specific authentication server(s).

**Rule ID:** `SV-251024r802294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User authentication can be used as part of the policy filtering rule sets. Some URLs or network resources can be restricted to authenticated users only. Users are prompted by the application or browser for credentials. Authentication service may be provided by the ALG as an intermediary for the application; however, the authentication credential must be stored in the site's directory services server. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., proxy capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Sentry does not provide user authentication intermediary services, this is not applicable. Verify the Sentry is configured with a preestablished trust relationship and mechanisms with appropriate authorities that validate each user access authorization and privileges. If Sentry provides user authentication intermediary services for ActiveSync, verify them as follows: 1. In the MobileIron Core Admin Portal, go to Services >> Sentry. 2. Click the "Edit" icon next to Sentry, which opens the "Edit Standalone Sentry" dialog. 3. Determine if the fields in the form are configured for ActiveSync. 4. Look under "ActiveSync Server(s)". 5. Verify only the ActiveSync Servers' end users are on this list. If ActiveSync Servers' end users are not the only entities on this list, this is a finding. If Sentry provides user authentication intermediary services for AppTunnel, verify only the Servers that users should be authenticating to are specified in the Services list. 1. In the MobileIron Core Admin Portal, go to Services >> Sentry. 2. Select the "Edit" icon for an existing Standalone Sentry entry. 3. Review the Approved AppTunnel Services and verify only the Servers that users should be authenticating to are specified in the services list. If end users are able to access AppTunnel services they should not be accessing, this is a finding.

## Group: SRG-NET-000140-ALG-000094

**Group ID:** `V-251025`

### Rule: The Sentry providing mobile device authentication intermediary services must use multifactor authentication for network access to non-privileged accounts.

**Rule ID:** `SV-251025r802297_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1. Something you know (e.g., password/PIN) 2. Something you have (e.g., cryptographic, identification device, token) 3. Something you are (e.g., biometric) Non-privileged accounts are not authorized access to the network element regardless of access method. Network access is any access to an application by a user (or process acting on behalf of a user) where said access is obtained through a network connection. Authenticating with a PKI credential and entering the associated PIN is an example of multifactor authentication. This requirement applies to ALGs that provide user authentication intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the MobileIron Core has a device-level password policy enforcing password or biometric and is applied to managed devices. This should be done by default. Verify the Sentry is configured for certificate based authentication. Verify the Sentry is set up to provide user authentication intermediary services. 1. In the MobileIron Core Portal, select Services >> Sentry. 2. Click the "Edit" icon for the Standalone Sentry entry. 3. In the "Device Authentication Configuration" section, select an option appropriate for this implementation. 4. Depending on the option selected, follow the instructions in one of the following sections to complete the configuration: - Group Certificate - Identity Certificate - Identity Certificate with Kerberos constrained delegation If Sentry is not configured for certificate-based authentication, this is a finding.

## Group: SRG-NET-000147-ALG-000095

**Group ID:** `V-251026`

### Rule: The Sentry providing mobile device authentication intermediary services must implement replay-resistant authentication mechanisms for network access to non-privileged accounts.

**Rule ID:** `SV-251026r802300_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A non-privileged account is any account with the authorizations of a non-privileged user. Privileged roles are organization-defined roles assigned to individuals that allow those individuals to perform certain security-relevant functions that ordinary users are not authorized to perform. Security relevant roles include key management, account management, network and system administration, database administration, and web administration. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one time use) or challenges (e.g., TLS). Additional techniques include time-synchronous or challenge-response one-time authenticators. This requirement applies to ALGs that provide user authentication intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Sentry is configured with TLS by default. The Sentry enables TLS 1.2 by default. To check the status: 1. Log in to MobileIron Sentry. 2. Go to Settings >> Services >> Sentry. 3. For each of the following configurations, follow step 4: a. Incoming SSL configuration b. Outgoing SSL configuration c. UEM SSL configuration d. Access SSL configuration 4. In Protocols, verify TLS 1.2 is enabled. If TLS 1.2 is not enabled for each configuration, this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the main section "Standalone Sentry Settings", which includes subsections on how TLS 1.2 is set as the default protocol: 1. Incoming SSL configuration 2. Outgoing SSL configuration 3. UEM SSL configuration 4. Access SSL configuration MobileIron Sentry conforms to the NIST SP 800-52 TLS settings by setting TLS 1.2 by default.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-251027`

### Rule: The Sentry that provides intermediary services for TLS must validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-251027r802303_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Sentry is configured with TLS by default. The Sentry enables TLS 1.2 by default. To check the status: 1. Log in to MobileIron Sentry. 2. Go to Settings >> Services >> Sentry. 3. For each of the following configurations, follow step 4: a. Incoming SSL configuration b. Outgoing SSL configuration c. UEM SSL configuration d. Access SSL configuration 4. In Protocols, verify TLS 1.2 is enabled. If TLS 1.2 is not enabled for each configuration, this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the main section "Standalone Sentry Settings", which includes subsections on how TLS 1.2 is set as the default protocol: 1. Incoming SSL configuration 2. Outgoing SSL configuration 3. UEM SSL configuration 4. Access SSL configuration MobileIron Sentry conforms to the NIST SP 800-52 TLS settings by setting TLS 1.2 by default.

## Group: SRG-NET-000166-ALG-000101

**Group ID:** `V-251028`

### Rule: The Sentry providing PKI-based mobile device authentication intermediary services must map authenticated identities to the mobile device account.

**Rule ID:** `SV-251028r802306_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authorization for access to any network element requires an approved and assigned individual account identifier. To ensure only the assigned individual is using the account, the account must be bound to a user certificate when PKI-based authentication is implemented. This requirement applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry is configured with certificate-based authentication with the appropriate certificate field user mappings. 1. In the MobileIron Core Portal, select Services >> Sentry. 2. Click the "Edit" icon for the Standalone Sentry entry. 3. In the "Device Authentication Configuration" section, verify certificate mappings are configured in the "certificate mapping" field. If Sentry is not configured to map authenticated identities to the user accounts, this is a finding.

## Group: SRG-NET-000213-ALG-000107

**Group ID:** `V-251029`

### Rule: The Sentry must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for mobile device sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity.

**Rule ID:** `SV-251029r802309_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system level network connection. ALGs may provide session control functionality as part of content filtering, load balancing, or proxy services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Log in to the Core Admin Portal. 2. Go to Policies and Configurations >> Configurations. 3. Click on existing VPN Configuration for MobileIron Tunnel; verify "Connection Type" is set to "MobileIron Tunnel". 4. Go to "Custom Data" section at the bottom and find the following Key Value pair: "TcpIdleTmoMs" The default idle timeout for the session is 1 hour. Therefore, if the key value pair is missing, this is a finding. If the key value pair is present, verify the value is no greater than 900000 millisec (15 min). If key value pair is not present or is set to a value greater than 900000, this is a finding.

## Group: SRG-NET-000334-ALG-000050

**Group ID:** `V-251030`

### Rule: The Sentry must offload audit records onto a centralized log server.

**Rule ID:** `SV-251030r802312_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to select a user session to capture or view, investigations into suspicious or harmful events would be hampered by the volume of information captured. The intent of this requirement is to ensure the capability to select specific sessions to capture is available in order to support general auditing/incident investigation, or to validate suspected misuse by a specific user. Examples of session events that may be captured include, port mirroring, tracking websites visited, and recording information and/or file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Sentry offloads audit records onto a centralized log server. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Syslog. 3. Verify a syslog server is configured. If it is not configured, this is a finding. 4. Click on the syslog server(s) and in the "Modify Syslog" pop-up dialog, under the "Facility Type", verify the checkbox for "Audit" is selected. If Sentry is not configured to offload audit records, this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the main section "Standalone Sentry Settings", which includes a subsection detailing the log representation format in "Audit log representation and format". The audit logs contain additional information on the type of events that occurred. Also included is date and timestamp, the source of the event, the location of the event, and the result of the action whether success/failure.

## Group: SRG-NET-000339-ALG-000090

**Group ID:** `V-251031`

### Rule: The Sentry providing mobile device authentication intermediary services must implement multifactor authentication for remote access to non-privileged accounts such that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-251031r802315_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For remote access to non-privileged accounts, the purpose of requiring a device that is separate from the information system gaining access for one of the factors during multifactor authentication is to reduce the likelihood of compromising authentication credentials stored on the system. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. An example of compliance with this requirement is the use of a one-time password token and PIN coupled with a password; or the use of a CAC/PIV card and PIN coupled with a password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Sentry does not provide user authentication intermediary services, this is not applicable. Verify the Sentry implements multifactor authentication for remote access to non-privileged accounts. Verify the MobileIron Core has a device-level password policy enforcing password or biometric and is applied to managed devices. This should be done by default. Verify the Sentry is configured for certificate-based authentication. If the Sentry is set up as an intermediary service for backend resources: 1. In the MobileIron Core Portal, select Services >> Sentry. 2. Click the "Edit" icon for the Standalone Sentry entry. 3. In the "Device Authentication Configuration" section, select an option appropriate for this implementation. 4. Depending on the option selected, follow the instructions in one of the following sections to verify the configuration is correct: - Group Certificate - Identity Certificate - Identity Certificate with Kerberos constrained delegation If the "Device Authentication Configuration" is not set up correctly, this is a finding.

## Group: SRG-NET-000355-ALG-000117

**Group ID:** `V-251032`

### Rule: The Sentry providing mobile device authentication intermediary services using PKI-based mobile device authentication must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of protected sessions.

**Rule ID:** `SV-251032r802318_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD-approved PKIs have not been evaluated to ensure they have security controls and identity vetting procedures in place that are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at https://cyber.mil/pki-pke/interoperability. DoD-approved PKI CAs may include Category I, II, and III certificates. Category I DoD-approved External PKIs are PIV issuers. Category II DoD-approved External PKIs are Non-Federal Agency PKIs cross-certified with the Federal Bridge Certification Authority (FBCA). Category III DoD-approved External PKIs are Foreign, Allied, or Coalition Partner PKIs. Deploying the ALG with TLS enabled will require the installation of DoD and/or DoD-approved CA certificates in the trusted root certificate store of each proxy to be used for TLS traffic. This requirement focuses on communications protection for the application session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Sentry only accepts end entity certificates issued by DoD PKI or DoD-approved PKI CAs for the establishment of protected sessions. Verify the MobileIron Core has a device-level password policy enforcing password or biometric and is applied to managed devices. This should be done by default. Verify the Sentry is configured for certificate-based authentication: Verify the Sentry is set up to provide user authentication intermediary services: 1. In the MobileIron Core Portal, select Services >> Sentry. 2. Click the "Edit" icon for the Standalone Sentry entry. 3. In the "Device Authentication Configuration" section, select an option appropriate for this implementation. 4. Depending on the option selected, follow the instructions in one of the following sections to complete the configuration: - Group Certificate - Identity Certificate - Identity Certificate with Kerberos constrained delegation 5. Select "View Certificate" and verify DoD and/or DoD-approved CA certificates are presented. If non-DoD-approved certificates are used, this is a finding.

## Group: SRG-NET-000362-ALG-000120

**Group ID:** `V-251033`

### Rule: The Sentry must implement load balancing to limit the effects of known and unknown types of Denial-of-Service (DoS) attacks.

**Rule ID:** `SV-251033r802321_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Load balancing provides service redundancy; which service redundancy reduces the susceptibility of the ALG to many DoS attacks. The ALG must be configured to prevent or mitigate the impact on network availability and traffic flow of DoS attacks that have occurred or are ongoing. This requirement applies to the network traffic functionality of the device as it pertains to handling network traffic. Some types of attacks may be specialized to certain network technologies, functions, or services. For each technology, known and potential DoS attacks must be identified and solutions for each type implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry is implemented behind a load balancer to limit the effects of known and unknown types of DoS attacks. If the device is not implemented behind a load balancer to limit the effects of known and unknown types of DoS attacks, this is a finding.

## Group: SRG-NET-000364-ALG-000122

**Group ID:** `V-251034`

### Rule: The Sentry must only allow incoming communications from organization-defined authorized sources routed to organization-defined authorized destinations.

**Rule ID:** `SV-251034r802324_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Access control policies and access control lists implemented on devices that control the flow of network traffic (e.g., application level firewalls and Web content filters), ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the internet or CDS) must be kept separate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only approved network routes are added to the Sentry. 1. Log in to Sentry System Manager. 2. Go to Settings >> Network >> Routes. 3. Verify only approved network routes are configured. If non-approved network routes are configured, this is a finding.

## Group: SRG-NET-000402-ALG-000130

**Group ID:** `V-251035`

### Rule: The Sentry must reveal error messages only to the ISSO, ISSM, and SCA.

**Rule ID:** `SV-251035r802327_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can give configuration details about the network element. Limiting access to system logs and administrative consoles to authorized personnel will help to mitigate this risk. However, user feedback and error messages should also be restricted by type and content in accordance with security best practices (e.g., ICMP messages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry reveals error messages only to the ISSO, ISSM, and SCA. 1. Log in to MobileIron Sentry. 2. Go to Monitoring >> Alert Configuration. 3. Verify "Send Notifications" is enabled. 4. Verify an email list containing the ISSO, ISSM, and SCA is input in the Email List. 5. Verify the "Alert Notification Management" section is set to meet organizational requirements. If Sentry is not configured to reveal error messages only to the ISSO, ISSM, and SCA, this is a finding.

## Group: SRG-NET-000510-ALG-000025

**Group ID:** `V-251036`

### Rule: The Sentry providing encryption intermediary services must implement NIST FIPS-validated cryptography to generate cryptographic hashes.

**Rule ID:** `SV-251036r802330_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry uses encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. On the MobileIron Sentry CLI console, do the following: 1. SSH to MobileIron Sentry Server from any SSH client. 2. Enter the administrator credentials set when MobileIron Sentry was installed. 3. Enter "enable". 4. When prompted, enter the "enable secret" set when MobileIron Sentry was installed. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If the MobileIron Sentry Server does not report that FIPS mode is "enabled", this is a finding.

## Group: SRG-NET-000510-ALG-000040

**Group ID:** `V-251037`

### Rule: The Sentry providing encryption intermediary services must implement NIST FIPS-validated cryptography for digital signatures.

**Rule ID:** `SV-251037r802333_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry uses encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. On the MobileIron Sentry CLI console, do the following: 1. SSH to MobileIron Sentry Server from any SSH client. 2. Enter the administrator credentials set when MobileIron Sentry was installed. 3. Enter "enable". 4. When prompted, enter the "enable secret" set when MobileIron Sentry was installed. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If the MobileIron Sentry Server does not report that FIPS mode is "enabled", this is a finding.

## Group: SRG-NET-000510-ALG-000111

**Group ID:** `V-251038`

### Rule: The Sentry providing encryption intermediary services must use NIST FIPS-validated cryptography to implement encryption services.

**Rule ID:** `SV-251038r802336_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry uses encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. On the MobileIron Sentry CLI console, do the following: 1. SSH to MobileIron Sentry Server from any SSH client. 2. Enter the administrator credentials set when MobileIron Sentry was installed. 3. Enter "enable". 4. When prompted, enter the "enable secret" set when MobileIron Sentry was installed. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If the MobileIron Sentry Server does not report that FIPS mode is "enabled", this is a finding.

## Group: SRG-NET-000511-ALG-000051

**Group ID:** `V-251039`

### Rule: The Sentry must offload audit records onto a centralized log server in real time.

**Rule ID:** `SV-251039r802339_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Offloading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. Offloading is a common process in information systems with limited audit storage capacity. The audit storage on the ALG is used only in a transitory fashion until the system can communicate with the centralized log server designated for storing the audit records, at which point the information is transferred. However, DoD requires that the log be transferred in real time which indicates that the time from event detection to offloading is seconds or less. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry produces audit records onto a centralized log server in real time. 1. Log in to MobileIron Sentry. 2. Go to Settings >> Syslog. 3. Verify a syslog server is configured. If it is not configured, this is a finding. 4. Click on the syslog server(s) and in the "Modify Syslog" pop-up dialog, under the "Facility Type", verify the checkbox for "Audit" is selected. If it is not selected, this is a finding. For more information, go to the "MobileIron Sentry 9.8.0 Guide for Core" and refer to the main section "Standalone Sentry Settings", which includes a subsection detailing the log representation format in "Audit log representation and format". The audit logs contain additional information on the type of events that occurred. Also included is date and timestamp, the source of the event, the location of the event, and the result of the action whether a success/failure.

