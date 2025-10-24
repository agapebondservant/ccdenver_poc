# STIG Benchmark: F5 BIG-IP TMOS ALG Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000053-ALG-000001

**Group ID:** `V-266137`

### Rule: The F5 BIG-IP appliance providing user access control intermediary services must limit the number of concurrent sessions to one or an organization-defined number for each access profile.

**Rule ID:** `SV-266137r1024833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "Max In Progress Sessions Per Client IP" setting in an APM Access Profile is a security configuration that limits the number of simultaneous sessions that can be initiated from a single IP address. This is particularly helpful in preventing a session flood, where a hacker might attempt to overwhelm the system by initiating many sessions from a single source. By capping the number of sessions per IP, this setting can help maintain the system's stability and integrity while also providing a layer of protection against such potential attacks. False positives may result from this setting in networks where users are behind a shared proxy. Sites must conduct operational testing to determine if there are adverse operational impacts. View Log reports to identify recurring IP sources within the user community. Max In Progress Sessions per Client IP represents the maximum number of sessions that can be in progress for a client IP address. When setting this value, take into account whether users will come from a NAT-ed or proxied client address and, if so, increase the value accordingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide user access control intermediary services, this is not applicable. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the Name of the Access profile. 5. Under "Settings", verify "Max Sessions per User" is set to "1" or to an organization-defined number. If the BIG-IP appliance is not configured to limit the number of concurrent sessions for user accounts to 1 or to an organization-defined number, this is a finding.

## Group: SRG-NET-000061-ALG-000009

**Group ID:** `V-266138`

### Rule: The F5 BIG-IP appliance providing intermediary services for remote access communications traffic must ensure inbound and outbound traffic is monitored for compliance with remote access security policies.

**Rule ID:** `SV-266138r1024835_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access traffic allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by inspecting connection activities of remote access capabilities. Remote access methods include both unencrypted and encrypted traffic (e.g., web portals, web content filter, TLS, and webmail). With inbound TLS inspection, the traffic must be inspected prior to being allowed on the enclave's web servers hosting TLS or HTTPS applications. With outbound traffic inspection, traffic must be inspected prior to being forwarded to destinations outside of the enclave, such as external email traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not serve as an intermediary for remote access traffic, this is not applicable. From the BIG-IP GUI: 1. Security. 2. Application Security. 3. Security Policies. 4. Policies List. 5. Review the list of policies and confirm they are applied to virtual servers being used for intermediary services for remote access communications traffic. If the BIG-IP appliance is not configured to ensure inbound and outbound traffic is monitored for compliance with remote access security policies, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-266139`

### Rule: The F5 BIG-IP appliance providing intermediary services for remote access must use FIPS-validated cryptographic algorithms, including TLS 1.2 at a minimum.

**Rule ID:** `SV-266139r1024837_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or SSL VPN gateway). Satisfies: SRG-NET-000062-ALG-000011, SRG-NET-000062-ALG-000150, SRG-NET-000063-ALG-000012, SRG-NET-000230-ALG-000113, SRG-NET-000355-ALG-000117</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary services for remote access (e.g., web content filter, TLS, and webmail), TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS), this is not applicable. Client SSL Profile From the BIG-IP GUI: 1. Local Traffic. 2. Profiles. 3. SSL. 4. Client. 5. Click on the name of the SSL Profile. 6. Change "Configuration" to "Advanced". 7. Verify "Ciphers" is configured to use NIST FIPS-validated ciphers. 8. Repeat for other SSL Profiles in use. Virtual Server From the BIG-IP GUI: 1. Local Traffic. 2. Virtual Servers. 3. Virtual Server List. 4. Click the name of the virtual server. 5. Verify that the "SSL Profile (Client)" is using a NIST FIPS-validated SSL Profile. 6. Repeat these steps to review all other virtual servers. If the BIG-IP appliance is not configured to use TLS 1.2 or higher, this is a finding.

## Group: SRG-NET-000318-ALG-000014

**Group ID:** `V-266140`

### Rule: To protect against data mining, the F5 BIG-IP appliance providing content filtering must prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-266140r1024838_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. Compliance requires the ALG to have the capability to prevent code injections. Examples include a Web Application Firewalls (WAFs) or database application gateways. Satisfies: SRG-NET-000318-ALG-000014, SRG-NET-000319-ALG-000015</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ALG does not perform content filtering as part of the traffic management functions, this is not applicable. From the BIG-IP GUI: 1. Security. 2. Application Security. 3. Security Policies. 4. Policies List. 5. Click the name of the policy. 6. Verify "Enforcement Mode" is set to "Blocking". 7. Select "Attack Signatures". 8. Click the filter at the top left of the signatures window. 9. Select "XPath Injection" in the "Attack Type" field and click "Apply". 10. Verify "Block" is checked for all signatures and "Status" is set to "Enforced". 11. Click the filter at the top left of the signatures window. 12. Select "LDAP Injection" in the "Attack Type" field and click "Apply". 13. Verify "Block" is checked for all signatures and "Status" is set to "Enforced". If the BIG-IP appliance is not configured to prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields, this is a finding.

## Group: SRG-NET-000318-ALG-000151

**Group ID:** `V-266141`

### Rule: To protect against data mining, the F5 BIG-IP appliance providing content filtering must prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-266141r1024839_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. Compliance requires the ALG to have the capability to prevent code injections. Examples include a Web Application Firewalls (WAFs) or database application gateways. Satisfies: SRG-NET-000318-ALG-000151, SRG-NET-000319-ALG-000153</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ALG does not perform content filtering as part of the traffic management functions, this is not applicable. From the BIG-IP GUI: 1. Security. 2. Application Security. 3. Security Policies. 4. Policies List. 5. Click the name of the policy. 6. Verify "Enforcement Mode" is set to "Blocking". 7. Select "Attack Signatures". 8. Click the filter at the top left of the signatures window. 9. Select "Buffer Overflow" in the "Attack Type" field and click "Apply". 10. Verify "Block" is checked for all signatures and "Status" is set to "Enforced". 11. Click the filter at the top left of the signatures window. 12. Select "Server Side Code Injection" in the "Attack Type" field and click "Apply". 13. Verify "Block" is checked for all signatures and "Status" is set to "Enforced". If the BIG-IP appliance is not configured to prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code, this is a finding.

## Group: SRG-NET-000318-ALG-000152

**Group ID:** `V-266142`

### Rule: To protect against data mining, the F5 BIG-IP appliance providing content filtering must prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-266142r1024368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. Compliance requires the ALG to have the capability to prevent SQL code injections. Examples include a Web Application Firewalls (WAFs) or database application gateways. Satisfies: SRG-NET-000318-ALG-000152, SRG-NET-000319-ALG-000020</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ALG does not perform content filtering as part of the traffic management functions, this is not applicable. From the BIG-IP GUI: 1. Security. 2. Application Security. 3. Security Policies. 4. Policies List. 5. Click the name of the policy. 6. Verify "Enforcement Mode" is set to "Blocking". 7. Select "Attack Signatures". 8. Click the filter at the top left of the signatures window. 9. Select "SQL-Injection" in the "Attack Type" field and click "Apply". 10. Verify "Block" is checked for all signatures and "Status" is set to "Enforced". If the BIG-IP appliance is not configured to prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields, this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-266143`

### Rule: The F5 BIG-IP appliance providing user access control intermediary services must enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies.

**Rule ID:** `SV-266143r1024370_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise of and unauthorized access to sensitive information. All DOD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide user access control intermediary services, this is not applicable. If Advanced Resource Assign VPE agent is not used in any policy, this is not a finding. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Review each Resource. - If the Advanced Resource Assign agent is used, verify that each expression listed is explicitly configured to use an authorization list. If the Big IP F5 appliance Access Policy has any assigned resources that are not configured with a specific authorization list, this is a finding.

## Group: SRG-NET-000018-ALG-000017

**Group ID:** `V-266144`

### Rule: The F5 BIG-IP appliance providing user access control intermediary services must implement attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-266144r1024371_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, devices) within information systems. Examples of information flow control restrictions include keeping export controlled information from being transmitted in the clear to the internet or blocking information marked as classified but is being transported to an unapproved destination. ALGs enforce approved authorizations by employing security policy and/or rules that restrict information system services, provide packet filtering capability based on header or protocol information and/or message filtering capability based on data content (e.g., implementing key word searches or using document characteristics). Satisfies: SRG-NET-000018-ALG-000017, SRG-NET-000019-ALG-000018</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Active Rules. 4. Verify "Policy Type" is set to "Enforced". 5. Inspect the different "Context" choices and verify rules are configured to enforce approved authorizations for controlling the flow of information within the network. If the BIG-IP appliance is not configured to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic, this is a finding.

## Group: SRG-NET-000041-ALG-000022

**Group ID:** `V-266145`

### Rule: The F5 BIG-IP appliance providing user access control intermediary services must display the Standard Mandatory DOD-approved Notice and Consent Banner before granting access to the network.

**Rule ID:** `SV-266145r1024372_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the network ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to network elements that have the concept of a user account and have the logon function residing on the network element. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to ALGs (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services. Satisfies: SRG-NET-000041-ALG-000022, SRG-NET-000042-ALG-000023, SRG-NET-000043-ALG-000024</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit..." in the "Per-Session Policy" column for an Access Profile used for granting access. 5. Verify the Access Profile is configured to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system. The banner must be exactly formatted in accordance with the policy (see below). "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the BIG-IP APM module is not configured to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system, this is a finding.

## Group: SRG-NET-000492-ALG-000027

**Group ID:** `V-266146`

### Rule: The F5 BIG-IP appliance must generate event log records that can be forwarded to the centralized events log.

**Rule ID:** `SV-266146r1024841_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that log usage of objects by subjects and other objects, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. The device logs internal users associated with denied outgoing communications traffic posing a threat to external information systems. Audit records can be generated from various components within the information system (e.g., module or policy filter). Security objects are data objects which are controlled by security policy and bound to security attributes. Satisfies: SRG-NET-000492-ALG-000027, SRG-NET-000494-ALG-000029, SRG-NET-000495-ALG-000030, SRG-NET-000496-ALG-000031, SRG-NET-000497-ALG-000032, SRG-NET-000498-ALG-000033, SRG-NET-000499-ALG-000034, SRG-NET-000500-ALG-000035, SRG-NET-000501-ALG-000036, SRG-NET-000502-ALG-000037, SRG-NET-000503-ALG-000038, SRG-NET-000505-ALG-000039, SRG-NET-000513-ALG-000026, SRG-NET-000074-ALG-000043, SRG-NET-000075-ALG-000044, SRG-NET-000076-ALG-000045, SRG-NET-000077-ALG-000046, SRG-NET-000078-ALG-000047, SRG-NET-000079-ALG-000048, SRG-NET-000249-ALG-000146, SRG-NET-000383-ALG-000135, SRG-NET-000385-ALG-000138, SRG-NET-000392-ALG-000141, SRG-NET-000392-ALG-000142, SRG-NET-000392-ALG-000143, SRG-NET-000392-ALG-000147, SRG-NET-000392-ALG-000148, SRG-NET-000392-ALG-000149, SRG-NET-000370-ALG-000125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
APM Default Log Profile: From the BIG-IP GUI: 1. Access. 2. Overview. 3. Event Logs. 4. Settings. 5. Check the box for the "default-log-setting" and click "Edit". 6. Verify "Enable Access System Logs" is checked. 7. On the "Access System Logs" tab, verify all items are set to "Notice". Access Profile Log Setting: From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles (Per-Session Policies). 4. Click the Name of the Access Profile. 5. Logs tab. 6. Verify "default-log-setting" is in the "Selected" column. If the BIG-IP appliance is not configured to generate log records, this is a finding.

## Group: SRG-NET-000512-ALG-000064

**Group ID:** `V-266147`

### Rule: The F5 BIG-IP appliance that provides intermediary services for SMTP must inspect inbound and outbound SMTP and Extended SMTP communications traffic for protocol compliance and protocol anomalies.

**Rule ID:** `SV-266147r1024374_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as SMTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits which exploit weaknesses of commonly used protocols. Since protocol anomaly analysis examines the application payload for patterns or anomalies, an SMTP proxy must be included in the ALG. This ALG will be configured to inspect inbound and outbound SMTP and extended SMTP communications traffic to detect protocol anomalies such as malformed message and command insertion attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary/proxy services for SMTP communications traffic, this is not applicable. SMTP Profile: From the BIG-IP GUI: 1. Local Traffic. 2. Profiles. 3. Services. 4. SMTP. 5. Click the name of the SMTP profile. 6. Verify "Protocol Security" is checked. SMTP Virtual Server: 1. Local Traffic. 2. Virtual Servers. 3. Virtual Server List. 4. Click the name of the SMTP virtual server. 5. Verify the SMTP profile is selected in the "SMTP Profile" drop-down list. If the BIG-IP appliance is not configured to inspect inbound and outbound SMTP and Extended SMTP communications traffic for protocol compliance and protocol anomalies, this is a finding.

## Group: SRG-NET-000512-ALG-000065

**Group ID:** `V-266148`

### Rule: The F5 BIG-IP appliance that intermediary services for FTP must inspect inbound and outbound FTP communications traffic for protocol compliance and protocol anomalies.

**Rule ID:** `SV-266148r1024375_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as FTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits which exploit weaknesses of commonly used protocols. Since protocol anomaly analysis examines the application payload for patterns or anomalies, an FTP proxy must be included in the ALG. This ALG will be configured to inspect inbound and outbound FTP communications traffic to detect protocol anomalies such as malformed message and command insertion attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary/proxy services for FTP communications traffic, this is not applicable. FTP Profile: From the BIG-IP GUI: 1. Local Traffic. 2. Profiles. 3. Services. 4. FTP. 5. Click the name of the FTP profile. 6. Verify "Protocol Security" is checked. FTP Virtual Server: 1. Local Traffic. 2. Virtual Servers. 3. Virtual Server List. 4. Click the name of the FTP virtual server. 5. Verify the FTP profile is selected in the "FTP Profile" drop-down list. If the BIG-IP appliance is not configured to inspect inbound and outbound FTP communications traffic for protocol compliance and protocol anomalies, this is a finding.

## Group: SRG-NET-000512-ALG-000066

**Group ID:** `V-266149`

### Rule: The F5 BIG-IP appliance that provides intermediary services for HTTP must inspect inbound and outbound HTTP traffic for protocol compliance and protocol anomalies.

**Rule ID:** `SV-266149r1024844_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as HTTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits which exploit weaknesses of commonly used protocols. Since protocol anomaly analysis examines the application payload for patterns or anomalies, an HTTP proxy must be included in the ALG. This ALG will be configured to inspect inbound and outbound HTTP communications traffic to detect protocol anomalies such as malformed message and command insertion attacks. All inbound and outbound traffic, including HTTPS, must be inspected. However, the intention of this policy is not to mandate HTTPS inspection by the ALG. Typically, HTTPS traffic is inspected either at the source, destination and/or is directed for inspection by organizationally-defined network termination point.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary/proxy services for HTTP communications traffic, this is not applicable. Application Security Policy: From the BIG-IP GUI: 1. Security. 2. Application Security. 3. Policy Building. 4. Learning and Blocking Settings. 5. Verify the correct policy is selected from the drop-down in the upper left. 6. Expand "HTTP protocol compliance failed". 7. Verify the proper inspection criteria are selected. HTTP Virtual Server: From the BIG-IP GUI: 1. Local Traffic. 2. Virtual Servers. 3. Virtual Server List. 4. Click the name of the HTTP Virtual Server. 5. Security >> Policies tab. 6. Verify the correct policy is selected for "Application Security Policy". If the BIG-IP appliance is not configured to inspect inbound and outbound HTTP communications traffic for protocol compliance and protocol anomalies, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-266150`

### Rule: The F5 BIG-IP appliance must be configured to prohibit or restrict the use of unnecessary or prohibited functions, ports, protocols, and/or services, including those defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-266150r1024377_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DOD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DOD policy. The ALG is a key network element for preventing these noncompliant ports, protocols, and services from causing harm to DOD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known nonsecure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements. Satisfies: SRG-NET-000132-ALG-000087, SRG-NET-000131-ALG-000085</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Local Traffic. 2. Virtual Servers. 3. Verify the list of virtual servers are not configured to listen on unnecessary and/or nonsecure functions, ports, protocols, and/or services. If any services are running that must not be, this is a finding.

## Group: SRG-NET-000138-ALG-000063

**Group ID:** `V-266152`

### Rule: The F5 BIG-IP appliance providing user authentication intermediary services must uniquely identify and authenticate users using redundant authentication servers and multifactor authentication (MFA).

**Rule ID:** `SV-266152r1024845_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. 1. Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication. 2. Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement applies to ALGs that provide user proxy services, including identification and authentication. This service must use the site's directory service (e.g., Active Directory). Directory services must not be installed onto the gateway. Satisfies: SRG-NET-000138-ALG-000063, SRG-NET-000138-ALG-000088, SRG-NET-000339-ALG-000090, SRG-NET-000340-ALG-000091, SRG-NET-000140-ALG-000094, SRG-NET-000166-ALG-000101, SRG-NET-000169-ALG-000102</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles (Per-Session Policies). 4. Click "Edit" for the Access Profile being used. 5. Verify the Access Profile uses an authentication server (e.g., LDAP, RADIUS, TACACS+) to perform user authentication. If the BIG-IP appliance is not configured to use a separate authentication server (e.g., LDAP, RADIUS, TACACS+) to perform user authentication, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-266153`

### Rule: The F5 BIG-IP appliance must configure certification path validation to ensure revoked machine credentials are prohibited from establishing an allowed session.

**Rule ID:** `SV-266153r1024380_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS), this is not applicable. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify an "OCSP Auth" object is configured in the Access Profile for "Machine" type or a CRLDP object is configured. If the BIG-IP appliance is not configured to use OCSP or CRLDP to ensure revoked machine credentials are prohibited from establishing an allowed session, this is a finding.

## Group: SRG-NET-000345-ALG-000099

**Group ID:** `V-266154`

### Rule: The F5 BIG-IP appliance providing user authentication intermediary services using PKI-based user authentication must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network.

**Rule ID:** `SV-266154r1024381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without configuring a local cache of revocation data, there is the potential to allow access to users who are no longer authorized (users with revoked certificates). The intent of this requirement is to require support for a secondary certificate validation method using a locally cached revocation data, such as Certificate Revocation List (CRL), in case access to OCSP (required by CCI-000185) is not available. Based on a risk assessment, an alternate mitigation is to configure the system to deny access when revocation data is unavailable. This requirement applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide PKI-based user authentication intermediary services, this is not applicable. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify an "OSCP Auth" and/or "CRLDP" object is configured in the Access Profile VPE AND that the fallback branch of these objects leads to a "Deny" ending. If the BIG-IP appliance is not configured to deny access when revocation data is unavailable, this is a finding.

## Group: SRG-NET-000213-ALG-000107

**Group ID:** `V-266155`

### Rule: The F5 BIG-IP appliance must terminate all network connections associated with a communications session at the end of the session or after 15 minutes of inactivity.

**Rule ID:** `SV-266155r1024382_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. Quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. ALGs may provide session control functionality as part of content filtering, load balancing, or proxy services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the name of the Access Profile. 5. Verify "Inactivity Timeout" is configured for 900 seconds. If the BIG-IP appliance is not configured to terminate all network connections associated with a user (nonprivileged) communications session after 15 minutes of inactivity, this is a finding.

## Group: SRG-NET-000362-ALG-000112

**Group ID:** `V-266156`

### Rule: The F5 BIG-IP appliance providing content filtering must employ rate-based attack prevention behavior analysis.

**Rule ID:** `SV-266156r1024848_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against denial-of-service (DoS) attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Detection components that use rate-based behavior analysis can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. Rate-based behavior analysis can detect sophisticated, distributed DoS (DDoS) attacks by correlating traffic information from multiple network segments or components. This requirement applies to the communications traffic functionality of the ALG as it pertains to handling communications traffic, rather than to the ALG device itself. Satisfies: SRG-NET-000362-ALG-000112, SRG-NET-000362-ALG-000126, SRG-NET-000192-ALG-000121</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not perform content filtering as part of the traffic management functions, this is not applicable. From the BIG-IP GUI: 1. Security. 2. DoS Protection. 3. Device Protection. 4. Expand each of the applicable families (Network, DNS, SIP) depending on the traffic being handled by the BIG-IP and verify the "State" is set to "Mitigate" for all signatures in that family. If the BIG-IP appliance is not configured to protect against known and unknown types of DoS attacks by employing rate-based attack prevention behavior analysis, this is a finding.

## Group: SRG-NET-000362-ALG-000155

**Group ID:** `V-266157`

### Rule: The F5 BIG-IP appliance providing content filtering must protect against or limit the effects of known and unknown types of denial-of-service (DoS) attacks by employing pattern recognition pre-processors.

**Rule ID:** `SV-266157r1024386_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks. Detection components that use pattern recognition pre-processors can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. This requirement applies to the communications traffic functionality of the ALG as it pertains to handling communications traffic, rather than to the ALG device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not perform content filtering as part of the traffic management functions, this is not applicable. From the BIG-IP GUI: 1. Security. 2. DoS Protection. 3. Device Protection. 4. Expand "Network" and verify "Dynamic Signatures" are enabled. 5. If applicable, expand "DNS" and verify "Dynamic Signatures" are enabled. If the BIG-IP appliance is not configured to protect against or limit the effects of known and unknown types of DoS attacks by employing pattern recognition pre-processors, this is a finding.

## Group: SRG-NET-000401-ALG-000127

**Group ID:** `V-266158`

### Rule: The F5 BIG-IP appliance must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-266158r1024387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior potentially leading to an application or information system compromise. Invalid input is one of the primary methods employed when attempting to compromise an application. Network devices with the functionality to perform application layer inspection may be leveraged to validate data content of network communications. Checking the valid syntax and semantics of information system inputs (e.g., character set, length, numerical range, and acceptable values) verifies that inputs match specified definitions for format and content. Software typically follows well-defined protocols that use structured messages (i.e., commands or queries) to communicate between software modules or system components. Structured messages can contain raw or unstructured data interspersed with metadata or control information. If network elements use attacker-supplied inputs to construct structured messages without properly encoding such messages, then the attacker could insert malicious commands or special characters that can cause the data to be interpreted as control information or metadata. Consequently, the module or component that receives the tainted output will perform the wrong operations or otherwise interpret the data incorrectly. Pre-screening inputs prior to passing to interpreters prevents the content from being unintentionally interpreted as commands. Input validation helps to ensure accurate and correct inputs and prevent attacks such as cross-site scripting and a variety of injection attacks. This requirement applies to gateways and firewalls that perform content inspection or have higher-layer proxy functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Application Security. 3. Parameters. 4. Parameters List. 5. Select the appropriate policy from the drop-down menu in the top left. 6. Verify the appropriate parameters are configured for the application (e.g., character set, length, numerical range, and acceptable values). If the BIG-IP appliance is not configured to check the validity of all data inputs except those specifically identified by the organization, this is a finding.

## Group: SRG-NET-000251-ALG-000131

**Group ID:** `V-266159`

### Rule: The F5 BIG-IP appliance providing content filtering must automatically update malicious code protection mechanisms.

**Rule ID:** `SV-266159r1024388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The malicious software detection functionality on network elements needs to be constantly updated to identify new threats as they are discovered. All malicious software detection functions must come with an update mechanism that automatically updates the application and any associated signature definitions. The organization (including any contractor to the organization) is required to promptly install security-relevant malicious code protection updates. Examples of relevant updates include antivirus signatures, detection heuristic rule sets, and/or file reputation data employed to identify and/or block malicious software from executing. Malicious code includes viruses, worms, Trojan horses, and spyware. This requirement is limited to ALGs, web content filters, and packet inspection firewalls that perform malicious code detection as part of their functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP does not perform content filtering as part of its traffic management functionality, this is not applicable. Note: Automatic signature updates can be configured, but depending on site connectivity this may not be possible. In this case manual upload of updates is possible. The below covers automatic update configuration. Automatic Update Check: From the BIG-IP GUI: 1. System. 2. Software Management. 3. Update Check. 4. Verify that "Automatic Update Check" is set to "Enabled". Real-Time Installation of Updates: 1. System. 2. Software Management. 3. Live Update. 4. Under "Updates Configuration" click on each item and check that "Real-Time" is selected for the setting "Installation of Automatically Downloaded Updates". If the BIG-IP appliance is not configured to automatically update malicious code protection mechanisms, this is a finding.

## Group: SRG-NET-000384-ALG-000136

**Group ID:** `V-266160`

### Rule: The F5 BIG-IP appliance providing content filtering must detect use of network services that have not been authorized or approved by the information system security manager (ISSM) and information system security officer (ISSO), at a minimum.

**Rule ID:** `SV-266160r1024389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation, and therefore may be unreliable or serve as malicious rogues for valid services. Examples of network services include service-oriented architectures (SOAs), cloud-based services (e.g., infrastructure as a service, platform as a service, or software as a service), cross-domain, Voice Over Internet Protocol, Instant Messaging, auto-execute, and file sharing. To comply with this requirement, the ALG may be configured to detect services either directly or indirectly (i.e., by detecting traffic associated with a service). This requirement applies to gateways/firewalls that perform content inspection or have higher-layer proxy functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not perform content filtering as part of the traffic management functions, this is not applicable. If using the BIG-IP AFM module to perform content filtering: AFM ACL: From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name>. 5. Verify a rule is configured that uses a "Classification Policy". Log Profile: From the BIG-IP GUI: 1. Security. 2. Event Logs. 3. Logging Profiles. 4. Edit the global-network profile. 5. Classification tab. 6. Verify the Log Publisher is set to the desired setting. (For production environments, F5 recommends using remote logging.) If configured rules in the policy do not detect use of network services that have not been authorized or approved by the ISSM and ISSO, at a minimum, this is a finding.

## Group: SRG-NET-000385-ALG-000137

**Group ID:** `V-266161`

### Rule: The F5 BIG-IP appliance providing content filtering must generate a log record when unauthorized network services are detected.

**Rule ID:** `SV-266161r1024391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation, and therefore may be unreliable or serve as malicious rogues for valid services. Examples of network services include service-oriented architectures (SOAs), cloud-based services (e.g., infrastructure as a service, platform as a service, or software as a service), cross-domain, Voice Over Internet Protocol, instant messaging, auto-execute, and file sharing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not perform content filtering as part of the traffic management functions, this is not applicable. If using the BIG-IP AFM module to perform content filtering: AFM ACL: From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name>. 5. Verify a rule is configured that uses a "Classification Policy". Log Profile: From the BIG-IP GUI: 1. Security. 2. Event Logs. 3. Logging Profiles. 4. Edit the global-network profile. 5. Classification tab. 6. Verify the Log Publisher is set to the desired setting. (For production environments, F5 recommends using remote logging.) If configured rules in the policy do not detect use of network services that have not been authorized or approved by the ISSM and ISSO, at a minimum, this is a finding.

## Group: SRG-NET-000233-ALG-000115

**Group ID:** `V-266162`

### Rule: When the Access Profile Type is LTM+APM and it is not using any connectivity resources (such as Network Access, Portal Access, etc.) in the VPE, the F5 BIG-IP appliance must be configured to enable the HTTP Only flag.

**Rule ID:** `SV-266162r1024392_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To guard against cookie hijacking, only the BIG-IP APM controller and client must be able to view the full session ID. Setting the APM HTTP Only flag ensures that a third party will not have access to the active session cookies. This option is only applicable to the LTM+APM access profile type. Other access profile types require access to various session cookies to fully function. Sites must conduct operational testing prior to enabling this setting. For implementations with connectivity resources (such as Network Access, Portal Access, etc.), do not set BIG-IP APM cookies with the HTTP Only flag.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Access Profile Type is not LTM+APM and it uses connectivity resources (such as Network Access, Portal Access, etc.) in the VPE, then this is not a finding. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the access profile name. 5. SSO/Auth Domains. 6. Under Cookie Options, verify HTTP Only is enabled. If the F5 BIG-IP appliance does not enable the HTTP Only flag, this is a finding.

## Group: SRG-NET-000233-ALG-000115

**Group ID:** `V-266163`

### Rule: The F5 BIG-IP appliance must be configured to enable the secure cookie flag.

**Rule ID:** `SV-266163r1024393_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To guard against cookie hijacking, only the BIG-IP APM controller and client must be able to view the full session ID. Session cookies are set only after the SSL handshake between the BIG-IP APM system and the user has completed, ensuring that the session cookies are protected from interception with SSL encryption. To ensure that the client browser will not send session cookies unencrypted, the HTTP header that the BIG-IP APM uses when sending the session cookie is set with the secure option (default). This option is only applicable to the LTM+APM access profile type.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the access profile name. 5. SSO/Auth Domains tab. 6. Under Cookie Options, verify "Secure" is enabled. If the F5 BIG-IP appliance APM Policy does not enable the Secure cookies flag, this is a finding.

## Group: SRG-NET-000233-ALG-000115

**Group ID:** `V-266164`

### Rule: The F5 BIG-IP appliance must be configured to disable the persistent cookie flag.

**Rule ID:** `SV-266164r1024395_rule`
**Severity:** low

**Description:**
<VulnDiscussion>For BIG-IP APM deployments with connectivity resources (such as Network Access, Portal Access, etc.), BIG-IP APM cookies cannot be set as Persistent. This is by design since cookies are stored locally on the client's hard disk, and thus could be exposed to unauthorized external access. For some deployments of the BIG-IP APM system, cookie persistence may be required. When selecting cookie persistence, persistence is hard coded at 60 seconds.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Access Profile is used for applications that require cookie persistence, then this is not a finding. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the access profile name. 5. SSO/Auth Domains tab. 6. Under Cookie Options, verify "Persistent" is disabled. If the F5 Big IP appliance APM Policy has the Persistent cookies flag enabled, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-266165`

### Rule: The F5 BIG-IP appliance must configure certificate path validation to ensure revoked user credentials are prohibited from establishing an allowed session.

**Rule ID:** `SV-266165r1024396_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS), this is not applicable. Access Policy: From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify an "OCSP Auth" object is configured in the Access Profile for "User" type or a CRLDP object is configured. If the BIG-IP appliance is not configured to use OCSP or CRLDP to ensure revoked user credentials are prohibited from establishing an allowed session, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-266166`

### Rule: The F5 BIG-IP appliance must not use the On-demand Cert Auth VPE agent as part of the APM Policy Profiles.

**Rule ID:** `SV-266166r1111861_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By requiring mutual authentication before any communication, it becomes significantly challenging for attackers to impersonate a client or server and exploit vulnerabilities. Furthermore, the encryption of all data transmitted between the client and server ensures that even if an attacker intercepts the data, it remains unintelligible without the correct keys. To ensure the use of the mTLS for session authentication, do not use the On-Demand Cert Auth VPE agent. Typically, when a client makes an HTTPS request, an SSL handshake request occurs at the start of an SSL session. However, if On-Demand is configured, the client SSL profile skips the initial SSL handshake, an On-Demand Cert Auth action can re-negotiate the SSL connection from an access policy by sending a certificate request to the user. This prompts a certificate screen to open. Setting ODCA to "require" the client cert means the client cannot get any farther in the APM VPE without providing a valid certificate. "Request" would ask the client for a certificate, but the client could still continue if they did not provide one. Thus, the Client Certificate must be set to "require" in the client SSL profile since just removing ODCA from the VPE alone will result in the client never getting prompted for a certificate. Within the Virtual Policy Editor (VPE) of the relevant Access Profile, do not use the On-Demand Cert Auth VPE agent. Configure only the Client Certification Inspection VPE Agent. This adjustment directs the BIG-IP to scrutinize the Client Certificate during the mTLS handshake process and extract the certificate's details into APM session variables.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify the On-Demand Cert Auth agent is not configured in any part of the profile. If the On-Demand Cert Auth agent is used in any Access Policy Profile, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-266167`

### Rule: The F5 BIG-IP appliance must be configured to restrict a consistent inbound IP for the entire management session.

**Rule ID:** `SV-266167r1024399_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This security measure helps limit the effects of denial-of-service attacks by employing antisession hijacking security safeguards. Session hijacking, also called cookie hijacking, is the exploitation of a valid computer session to gain unauthorized access to an application. The attacker steals (or hijacks) the cookies from a valid user and attempts to use them for authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. System. 2. Preferences. 3. Under Security Settings, verify "Require A Consistent Inbound IP For The Entire Web Session" box is checked. From the BIG-IP Console: tmsh list sys httpd auth-pam-validate-ip Note: This returns a value of "on". If the BIG-IP appliance is not configured to require a consistent inbound IP for the entire session for management sessions, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-266168`

### Rule: The F5 BIG-IP appliance must be configured to limit authenticated client sessions to initial session source IP.

**Rule ID:** `SV-266168r1024400_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The "Restrict to Single Client IP” is a safeguard against session hijacking or cookie theft. Even if an attacker manages to steal a session cookie, the cookie cannot be used from a different source IP address that the address used to initiate the session. This security measure is set within the APM Access Profiles. This setting has been recommended by F5 as a defense-in-depth measure. However, in some networks, this may result in false positives or rejection of legitimate connections. Users behind a shared proxy address may be denied access. Thus, sites must test this setting within their network prior to implementing to determine if there are operational impacts that prevent the use of this setting. If so, the site must document the impacts and get approval from the authorizing official (AO) if this required setting will not be implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the site has documented an adverse operational impact and has AO approval, this is not a finding. From the BIG-IP GUI: 1. System. 2. Access. 3. Profiles/Policies. 4. Access Profiles. 5. Click the access profile name. 6. Under Settings, verify "Restrict to Single Client IP" is checked. If the BIG-IP appliance is not configured to limit authenticated client sessions to initial session source IP, this is a finding.

## Group: SRG-NET-000510-ALG-000111

**Group ID:** `V-266170`

### Rule: The F5 BIG-IP appliance must be configured to use cryptographic algorithms approved by NSA to protect NSS for remote access to a classified network.

**Rule ID:** `SV-266170r1029558_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The VPN gateway must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. NIST cryptographic algorithms are approved by NSA to protect NSS. Based on an analysis of the impact of quantum computing, cryptographic algorithms specified by CNSSP-15 and approved for use in products in the CSfC program have been changed to more stringent protocols and configured with increased bit sizes and other secure characteristics to protect against quantum computing threats. The Commercial National Security Algorithm Suite (CNSA Suite) replaces Suite B.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Local Traffic. 2. Profiles. 3. SSL. 4. Client. 5. Click the name of the SSL Profile. 6. For "Ciphers", ensure only AES-256 or other cryptographic algorithms approved by NSA to protect NSS for remote access to a classified network are configured in compliance with CSNA/CNSSP-15. If the BIG-IP appliance is not configured to use cryptographic algorithms approved by NSA to protect NSS for remote access to a classified network, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-266171`

### Rule: The F5 BIG-IP must be configured to identify and authenticate all endpoint devices or peers before establishing a connection.

**Rule ID:** `SV-266171r1024403_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying and authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide remote access intermediary services, this is not applicable. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit..." in the "Per-Session Policy" column for the Access Profile. 5. Verify the Access Profile is configured to uniquely identify network devices. If the BIG-IP appliance is not configured to identify and authenticate all endpoint devices or peers before establishing a connection, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-266172`

### Rule: The F5 BIG-IP appliance providing remote access intermediary services must disable split-tunneling for remote clients' VPNs.

**Rule ID:** `SV-266172r1024404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Split tunneling would in effect allow unauthorized external connections, making the system more vulnerable to attack and to exfiltration of organizational information. A VPN hardware or software client with split tunneling enabled provides an unsecured backdoor to the enclave from the internet. With split tunneling enabled, a remote client has access to the internet while at the same time has established a secured path to the enclave via an IPsec tunnel. A remote client connected to the internet that has been compromised by an attacker on the internet, provides an attack base to the enclave’s private network via the IPsec tunnel. Hence, it is imperative that the VPN gateway enforces a no split-tunneling policy to all remote clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide remote access intermediary services, this is not applicable. Access Profile: From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the name of the Access Profile. 5. Click the Access Policy tab and note the name(s) of the Network Access listed. Network Access List: From the BIG-IP GUI: 1. Access. 2. Connectivity/VPN. 3. Network Access (VPN). 4. Network Access Lists. 5. Click on the Name of the Network Access List. 6. Network Settings tab. 7. Verify "Force all traffic through tunnel" is selected under Client Settings >> Traffic Options. If the BIG-IP appliance is not configured to disable split-tunneling for remote client VPNs, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-266173`

### Rule: The F5 BIG-IP appliance providing remote access intermediary services must be configured to route sessions to an IDPS for inspection.

**Rule ID:** `SV-266173r1024854_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices, such as those providing remote access to network devices and information systems, which lack automated, capabilities increase risk and makes remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, from a variety of information system components (e.g., servers, workstations, notebook computers, smart phones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide remote access intermediary services, this is not applicable. Verify one of these two options are configured: 1. The network architecture routes traffic inline from the BIG-IP through an IDPS. 2. A Protocol Inspection Profile is configured on the Virtual Server. From the BIG-IP GUI: 1. Local Traffic. 2. Virtual Servers. 3. Virtual Server List. 4. Click on the name of the Virtual Server. 5. Security >> Policies tab. 6. Verify "Protocol Inspection Profile" is set to "Enabled" and the "Profile" drop-down is set to the appropriate value. If the BIG-IP appliance is not configured to route sessions to an IDPS for inspection, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-266174`

### Rule: The VPN Gateway must use Always On VPN connections for remote computing.

**Rule ID:** `SV-266174r1024406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing remote users to manually toggle a VPN connection can create critical security risks. With Always On VPN, if a secured connection to the gateway is lost, hybrid-working users will simply be disconnected from the internet until the issue is solved. "Always On" is a term that describes a VPN connection that is secure and always on after the initial connection is established. An Always On VPN deployment establishes a VPN connection with the client without the need for user interaction (e.g., user credentials). The remote client must not be able to access the Internet without first established a VPN session with a DOD site. Note that device compliance checks are still required prior to connecting to DOD resources. Although out of scope for this requirement, the connection process must ensure that remote devices meet security standards before accessing DOD resources. Devices that fail to meet compliance requirements can be denied access, reducing the risk of compromised endpoints.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify at least one of these methods is configured. Always Connected Mode: From the BIG-IP GUI: 1. Access. 2. Connectivity/VPN. 3. Connectivity. 4. Profiles. 5. Click the name of the profile. 6. At the bottom, click Customize Package >> Windows. 7. Click "BIG-IP Edge Client" on the left. 8. Verify "Enable Always connected mode" is enabled. Machine Tunnels: From the BIG-IP GUI: 1. Access. 2. Connectivity/VPN. 3. Connectivity. 4. Profiles. 5. Click the name of the profile. 6. At the bottom, click Customize Package >> Windows. 7. Verify "Machine Tunnel Service" is checked. If the BIG-IP VPN Gateway is not configured to use an Always On VPN connection for remote computing, this is a finding.

## Group: SRG-NET-000053-ALG-000001

**Group ID:** `V-266175`

### Rule: The F5 BIG-IP appliance must be configured to set the "Max In Progress Sessions per Client IP" value to 10 or an organizational-defined number.

**Rule ID:** `SV-266175r1024855_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The "Max In Progress Sessions Per Client IP" setting in an APM Access Profile is a security configuration that limits the number of simultaneous sessions that can be initiated from a single IP address. This is particularly helpful in preventing a session flood, where a hacker might attempt to overwhelm the system by initiating many sessions from a single source. By capping the number of sessions per IP, this setting can help maintain the system's stability and integrity while also providing a layer of protection against such potential attacks. This setting has been recommended by F5 as a defense-in-depth measure. However, in some networks, narrowing the number of in progress sessions may in adverse impacts on legitimate connections. Thus, sites must test this setting within their network prior to implementing to determine the minimum acceptable number. This should not remain at the very high default value and should not be excessively high. Document the organizational value.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: Setting must be tested to determine if a number greater than 10 is operationally necessary. Ten is the minimum but may have operational impacts. Set to the minimum that is possible without adverse impacts, document the setting and the operational testing. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the access profile name. 5. In the "Settings" section, verify "Max In Progress Sessions per Client IP" is set to 10 or an organization-defined number. If the F5 BIG-IP APM access policy is not configured to set a "Max In Progress Sessions per Client IP" value to 10 or an organization-defined number, this is a finding.

