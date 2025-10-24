# STIG Benchmark: Citrix Virtual Apps and Desktop 7.x License Server Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014

**Group ID:** `V-234222`

### Rule: Citrix License Server must implement DoD-approved encryption to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-234222r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the License Management Console, click "Administration", and select the "Server Configuration" tab. Click the "Secure Web Server Configuration" bar and verify "Select Enable HTTPS (Default 443)" is selected. If "Select Enable HTTPS (Default 443)" is not selected, this is a finding.

## Group: SRG-APP-000090

**Group ID:** `V-234223`

### Rule: Citrix License Server must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-234223r960882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify all License Server administrators as the appropriate Active Directory domain/user or domain/group account. 1. Log on to the License Server with an administrator account. 2. To open the License Administration Console on the computer on which it is installed: Start menu, choose All Programs >> Citrix >> License Administration Console. 3. To open the console on a remote server or cluster, navigate the browser to one of the following URL options: a. Caution-https://License server name:Web service port b. Caution-https://Client access point name:Web service port c. Caution-https://IP:Web service port 4. In the top right corner of the console, select Administration. 5. Select >> Settings >> Accounts. 6. Identify all License Server administrators as the appropriate Active Directory domain/user or domain/group account. If the desired License Server administrator account is not returned, this is a finding.

## Group: SRG-APP-000219

**Group ID:** `V-234224`

### Rule: Citrix License Server must protect the authenticity of communications sessions.

**Rule ID:** `SV-234224r1043178_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. Application communication sessions are protected using transport encryption protocols, such as SSL or TLS. SSL/TLS provide web applications with a way to authenticate user sessions and encrypt application traffic. Session authentication can be single (one-way) or mutual (two-way) in nature. Single authentication authenticates the server for the client, whereas mutual authentication provides a means for both the client and the server to authenticate each other. This requirement applies to applications that use communications sessions. This includes but is not limited to web-based applications and Service-Oriented Architectures (SOA). This requirement addresses communications protection at the application session, versus the network packet, and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of SSL/TLS mutual authentication (two-way/bidirectional).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Look in \\Citrix\Licensing\LS\conf\ folder of the License Server installation directory for cert file/cert key file. Open the License Management Console, click "Administration", and select the "Server Configuration" tab. Click the "Secure Web Server Configuration" bar and verify "Select Enable HTTPS (Default 443)" is selected. If "Select Enable HTTPS (Default 443)" is not selected, this is a finding. NOTE: The user may be prompted to log in after "Administration".

## Group: SRG-APP-000400

**Group ID:** `V-234225`

### Rule: Citrix License Server must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-234225r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Click "Administration" and select the "Server Configuration" tab. 2. Click the "Web Server Configuration" bar and "Session Timeout". 3. Verify Session Timeout is set to “10”. If Session Timeout is not set to “10”, this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-234226`

### Rule: Citrix License Server must protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-234226r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and read or altered. This requirement applies only to applications that are distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the License Management Console, click "Administration", and select the "Server Configuration" tab. Click the "Secure Web Server Configuration" bar and verify "Select Enable HTTPS (Default 443)" is selected. If "Select Enable HTTPS (Default 443)" is not selected, this is a finding.

## Group: SRG-APP-000440

**Group ID:** `V-234227`

### Rule: Citrix License Server must implement cryptographic mechanisms to prevent unauthorized disclosure of information and/or detect changes to information during transmission unless otherwise protected by alternative physical safeguards, such as, at a minimum, a Protected Distribution Systems (PDS).

**Rule ID:** `SV-234227r961635_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encrypting information for transmission protects information from unauthorized disclosure and modification. Cryptographic mechanisms implemented to protect information integrity include, for example, cryptographic hash functions that have common application in digital signatures, checksums, and message authentication codes. This requirement applies only to applications that are distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. Alternative physical protection measures include PDS. PDSs are used to transmit unencrypted classified National Security Information (NSI) through an area of lesser classification or control. Since the classified NSI is unencrypted, the PDS must provide adequate electrical, electromagnetic, and physical safeguards to deter exploitation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the License Management Console, click "Administration", and select the "Server Configuration" tab. Click the "Secure Web Server Configuration" bar and verify "Select Enable HTTPS (Default 443)" is selected. If "Select Enable HTTPS (Default 443)" is not selected, this is a finding.

## Group: SRG-APP-000442

**Group ID:** `V-234228`

### Rule: Citrix License Server must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-234228r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be unintentionally or maliciously disclosed or modified during reception including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to applications that are distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, applications need to leverage protection mechanisms, such as TLS, SSL VPNs, or IPsec.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the License Management Console, click "Administration", and select the "Server Configuration" tab. Click the "Secure Web Server Configuration" bar and verify "Select Enable HTTPS (Default 443)" is selected. If "Select Enable HTTPS (Default 443)" is not selected, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-275968`

### Rule: The version of Virtual Apps and Desktop License Server running on the system must be a supported version.

**Rule ID:** `SV-275968r1115776_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Virtual Apps and Desktop License Server 7.x is no longer supported by the vendor. If the system is running Virtual Apps and Desktop License Server 7.x, this is a finding.

