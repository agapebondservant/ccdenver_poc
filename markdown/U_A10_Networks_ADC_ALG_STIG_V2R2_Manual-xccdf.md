# STIG Benchmark: A10 Networks ADC ALG Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000062-ALG-000150

**Group ID:** `V-237032`

### Rule: The A10 Networks ADC, when used for TLS encryption and decryption, must be configured to comply with the required TLS settings in NIST SP 800-52.

**Rule ID:** `SV-237032r639543_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SP 800-52 provides guidance on using the most secure version and configuration of the TLS/SSL protocol. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks which exploit vulnerabilities in this protocol. This requirement applies to TLS gateways (also known as SSL gateways) and is not applicable to VPN devices. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol thus are in scope for this requirement. NIS SP 800-52 provides guidance. SP 800-52 sets TLS version 1.1 as a minimum version, thus all versions of SSL are not allowed (including for client negotiation) either on DoD-only or on public facing servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS), this is not applicable. Review the device configuration. View the configured cipher templates (if any): show slb template cipher The following cipher suites are in compliance: TLS1_RSA_AES_128_SHA TLS1_RSA_AES_128_SHA256 TLS1_RSA_AES_256_SHA TLS1_RSA_AES_256_SHA256 If any of the configured cipher templates contain any cipher suites that are not in compliance, this is a finding. View the configured SLB SSL templates: show slb template server-ssl If any of the configured SLB SSL templates list version 30, 31, 32, this is a finding. If any of the configured SLB SSL templates contain any cipher suites that are not in compliance, this is a finding.

## Group: SRG-NET-000077-ALG-000046

**Group ID:** `V-237033`

### Rule: The A10 Networks ADC, when used to load balance web applications, must enable external logging for accessing Web Application Firewall data event messages.

**Rule ID:** `SV-237033r639546_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. External logging must be enabled for WAF data event messages. Create a server configuration for each log server, and then add a TCP or UDP port to each server configuration, with the port number on which the external log server listens for log messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device is not used to load balance web servers, this is not applicable. Review the device configuration and ask the device Administrator which templates are used. If no SLB instance for the log server(s) is configured, this is a finding. If there is no service group with assigned members for the log servers or the service group is not included in the logging template, this is a finding. If no logging template is configured and bound to the WAF template, this is a finding.

## Group: SRG-NET-000088-ALG-000054

**Group ID:** `V-237034`

### Rule: The A10 Networks ADC must send an alert to, at a minimum, the ISSO and SCA when connectivity to the Syslog servers is lost.

**Rule ID:** `SV-237034r639549_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Possible audit processing failures also include the inability of device to write to the central audit log. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations, (i.e., all audit data storage repositories combined), or both. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the configured Server Load Balancing instances: show run | sec slb If no Server Load Balancing instance is configured with a health check to the Syslog server, this is a finding. The following command shows the device configuration and filters the output on the string "snmp": show run | inc snmp This will include which SNMP traps the device is configured to send. If the output does not include "snmp-server enable traps slb server-down", this is a finding.

## Group: SRG-NET-000131-ALG-000085

**Group ID:** `V-237035`

### Rule: The A10 Networks ADC must not have unnecessary scripts installed.

**Rule ID:** `SV-237035r639552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the device. Unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The A10 Networks ADC can use a TCL-based scripting language called aFleX. Scripts used by an A10 Networks ADC must be documented so that Administrative and Security personnel understand them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ALG configuration to determine if any aFleX scripts are used on the device. The following command displays all of the configured aFleX scripts: show aflex all If any scripts are present, ask the Administrator for documentation of each script. If no documents can be provided explaining the script and showing where the ISSM or other responsible Security personnel acknowledged the script is being used, this is a finding.

## Group: SRG-NET-000131-ALG-000086

**Group ID:** `V-237036`

### Rule: The A10 Networks ADC must use DNS Proxy mode when Global Server Load Balancing is used.

**Rule ID:** `SV-237036r639555_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrelated or unneeded proxy services increase the attack vector and add excessive complexity to the securing of the device. Multiple application proxies can be installed on many devices. However, proxy types must be limited to related functions. The A10 Networks ADC is capable of DNS-based Global Server Load Balancing (GSLB), which uses Domain Name Service (DNS) to expand load balancing to larger scales, including globally. Global Server Load Balancing can operate in either Proxy mode or Server mode. In Proxy mode, all DNS queries arriving at the DNS Proxy IP address are forwarded to the existing DNS server. In Server mode, the device directly responds to queries for specific service IP addresses in the GSLB zone and can reply with A, AAAA, MX, NS, PTR, SRV, and SOA records. For all other records, the ACOS device will attempt Proxy mode unless configured as fully authoritative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If DNS-based Global Server Load Balancing is not configured, this is not applicable. If DNS-based Global Server Load Balancing is configured, review the configuration. Check if real servers are configured for DNS. If they are not, then the device is in Server mode, and this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-237037`

### Rule: The A10 Networks ADC must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-237037r639558_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. The device must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of authorized applications, endpoints, services, and protocols that have been added to the PPSM database. Review the configured servers, service groups, and virtual servers. The following command shows information for SLB servers: show slb server The following command shows information for service groups (multiple servers): show slb service-group The following command shows information for virtual servers (the services visible to outside hosts): show slb virtual-server If any of the servers, service groups, or virtual servers allows traffic that is prohibited by the PPSM CAL, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-237038`

### Rule: The A10 Networks ADC when used for TLS encryption and decryption must validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-237038r639561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses. The A10 Networks ADC can be configured to use Open Certificate Status Protocol (OCSP) and/or certificate revocation lists (CRLs) to verify the revocation status of certificates. OCSP is preferred since it reduces the overhead associated with CRLs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ALG does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS), this is not applicable. Verify the ALG validates certificates used for TLS functions by performing RFC 5280-compliant certification path validation. If the ALG does not validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation, this is a finding.

## Group: SRG-NET-000202-ALG-000124

**Group ID:** `V-237039`

### Rule: The A10 Networks ADC must not have any unnecessary or unapproved virtual servers configured.

**Rule ID:** `SV-237039r639564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A deny-all, permit-by-exception network communications traffic policy ensures that only those connections which are essential and approved are allowed. A virtual server is an instance where the device accepts traffic from outside hosts and redirects traffic to one or more real servers. In keeping with a deny-all, permit-by-exception policy, the services that the device provides to outside hosts must be only those that are necessary, documented, and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configured servers, service groups, and virtual servers. The following command shows information for SLB servers: show slb server The following command shows information for service groups (multiple servers): show slb service-group The following command shows information for virtual servers (the services visible to outside hosts): show slb virtual-server Ask the Administrator for the list of approved services being provided by the device and compare this against the output of the command listed above. If there are more configured virtual servers than are approved, this is a finding.

## Group: SRG-NET-000273-ALG-000129

**Group ID:** `V-237040`

### Rule: The A10 Networks ADC, when used to load balance web applications, must strip HTTP response headers.

**Rule ID:** `SV-237040r639567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing too much information in error messages risks compromising the data and security of the application and system. HTTP response headers can disclose vulnerabilities about a web server. This information can be used by an attacker. The A10 Networks ADC can filter response headers; this removes the web server’s identifying headers in outgoing responses (such as Server, X-Powered-By, and X-AspNet-Version).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device is not used to load balance web servers, this is not applicable. If the device is used to load balance web servers, verify that the A10 Networks ADC strips HTTP response headers. The following command displays WAF templates: show slb template waf If the configured WAF templates do not have the "filter-resp-hdrs" option configured, this is a finding.

## Group: SRG-NET-000273-ALG-000129

**Group ID:** `V-237041`

### Rule: The A10 Networks ADC, when used to load balance web applications, must replace response codes.

**Rule ID:** `SV-237041r639570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing too much information in error messages risks compromising the data and security of the application and system. HTTP response codes can be used by an attacker to learn how a web server responds to particular inputs. Certain codes reveal that a security device or the web server defended against a particular attack, which enables the attacker to eliminate that attack as an option. Using ambiguous response codes makes it more difficult for an attacker to determine what defenses are in place. The A10 Networks ADC can be configured to cloak 4xx and 5xx response codes for outbound responses from a web server. The acceptable HTTP response codes are contained in the preconfigured WAF policy file named "allowed_resp_codes".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device is not used to load balance web servers, this is not applicable. If the device is used to load balance web servers, verify that the A10 Networks ADC replaces error response codes. The following command displays WAF templates: show slb template waf If the configured WAF templates do not have the "hide-resp-codes" option configured, this is a finding.

## Group: SRG-NET-000318-ALG-000014

**Group ID:** `V-237042`

### Rule: To protect against data mining, the A10 Networks ADC must detect and prevent SQL and other code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-237042r831317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. The A10 Networks ADC contains a WAF policy file that provides a basic collection of SQL special characters and keywords that are common to SQL injection attacks. The terms in this policy file can trigger commands in the back-end SQL database and allow unauthorized users to obtain sensitive information. If a request contains a term that matches a search definition in the “sqlia_defs” policy file, the device can be configured to sanitize the request of the SQL command or deny the request entirely. The "sanitize" option uses more processor cycles than the preferred option of “drop”.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ADC is not used to load balance web servers where data can be entered and used in databases or other applications, this is not applicable. Interview the device administrator to determine which WAF template is used for web servers where data can be entered and used in databases or other applications. Review the device configuration. The following command displays WAF templates: show slb template waf If the configured WAF template does not have the "sqlia-check" option configured, this is a finding.

## Group: SRG-NET-000318-ALG-000151

**Group ID:** `V-237043`

### Rule: To protect against data mining, the A10 Networks ADC must detect and prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-237043r831318_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ADC is not used to load balance web servers where data can be entered and used in databases or other applications, this is not applicable. Interview the device administrator to determine which WAF template is used for web servers where data can be entered and used in databases or other applications. Review the device configuration. The following command displays WAF templates: show slb template waf If the configured WAF template does not have the "sqlia-check" option configured, this is a finding.

## Group: SRG-NET-000318-ALG-000152

**Group ID:** `V-237044`

### Rule: To protect against data mining, the A10 Networks ADC providing content filtering must prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-237044r831319_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ADC is not used to load balance web servers where data can be entered and used in databases or other applications, this is not applicable. Interview the device administrator to determine which WAF template is used for web servers where data can be entered and used in databases or other applications. Review the device configuration. The following command displays WAF templates: show slb template waf If the configured WAF template does not have the "sqlia-check" option configured, this is a finding.

## Group: SRG-NET-000319-ALG-000015

**Group ID:** `V-237045`

### Rule: To protect against data mining, the A10 Networks ADC providing content filtering must detect code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-237045r831320_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ADC is not used to load balance web servers where data can be entered and used in databases or other applications, this is not applicable. Interview the device administrator to determine which WAF template is used for web servers where data can be entered and used in databases or other applications. Review the device configuration. The following command displays WAF templates: show slb template waf If the configured WAF template does not have the "sqlia-check" option configured, this is a finding.

## Group: SRG-NET-000319-ALG-000020

**Group ID:** `V-237046`

### Rule: To protect against data mining, the A10 Networks ADC providing content filtering must detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-237046r831321_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational databases may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ADC is not used to load balance web servers where data can be entered and used in databases or other applications, this is not applicable. Interview the device administrator to determine which WAF template is used for web servers where data can be entered and used in databases or other applications. Review the device configuration. The following command displays WAF templates: show slb template waf If the configured WAF template does not have the "sqlia-check" option configured, this is a finding.

## Group: SRG-NET-000319-ALG-000153

**Group ID:** `V-237047`

### Rule: To protect against data mining, the A10 Networks ADC providing content filtering as part of its intermediary services must detect code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-237047r831322_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational applications may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ADC is not used to load balance web servers where data can be entered and used in databases or other applications, this is not applicable. Interview the device administrator to determine which WAF template is used for web servers where data can be entered and used in databases or other applications. Review the device configuration. The following command displays WAF templates: show slb template waf If the configured WAF template does not have the "sqlia-check" option configured, this is a finding.

## Group: SRG-NET-000355-ALG-000117

**Group ID:** `V-237048`

### Rule: The A10 Networks ADC being used for TLS encryption and decryption using PKI-based user authentication must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certificate Authorities (CAs) for the establishment of protected sessions.

**Rule ID:** `SV-237048r831323_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at http://iase.disa.mil/pki-pke/interoperability. DoD-approved PKI CAs may include Category I, II, and III certificates. Category I DoD-Approved External PKIs are PIV issuers. Category II DoD-Approved External PKIs are Non-Federal Agency PKIs cross certified with the Federal Bridge Certification Authority (FBCA). Category III DoD-Approved External PKIs are Foreign, Allied, or Coalition Partner PKIs. Deploying the device with TLS enabled will require the installation of DoD and/or DoD-Approved CA certificates in the trusted root certificate store of each proxy to be used for TLS traffic. This requirement focuses on communications protection for the application session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the A10 Networks ADC is not used for TLS/SSL decryption for application traffic, this is not applicable. If the A10 Networks ADC is used for TLS/SSL decryption for application traffic, verify the A10 Networks ADC only accepts end entity certificates issued by DoD PKI or DoD-approved PKI CAs for the establishment of protected sessions. If the A10 Networks ADC accepts non-DoD-approved PKI end entity certificates, this is a finding.

## Group: SRG-NET-000362-ALG-000112

**Group ID:** `V-237049`

### Rule: The A10 Networks ADC must protect against TCP and UDP Denial of Service (DoS) attacks by employing Source-IP based connection-rate limiting.

**Rule ID:** `SV-237049r831324_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Detection components that use rate-based behavior analysis can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. Rate-based behavior analysis can detect sophisticated, Distributed DoS (DDoS) attacks by correlating traffic information from multiple network segments or components. This requirement applies to the communications traffic functionality of the device as it pertains to handling communications traffic, rather than to the device itself. The A10 Networks ADC provides Source-IP based connection-rate limiting to mitigate UDP floods and similar attacks. Source-IP based connection-rate limiting protects the system from excessive connection requests from individual clients. If traffic from a client exceeds the configured threshold, the device should be configured to lock out the client for a specified number of seconds. During the lockout period, all connection requests from the client are dropped. The lockout period ranges from 1-3600 seconds (1 hour); there is no default value.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the device configuration and filters the output on the string "slb conn-rate-limit": show run | inc slb conn-rate-limit If Source-IP based connection rate limiting is not configured, this is a finding. If no lockout period is configured as an action, this is a finding.

## Group: SRG-NET-000362-ALG-000120

**Group ID:** `V-237050`

### Rule: The A10 Networks ADC must implement load balancing to limit the effects of known and unknown types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-237050r831325_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Although maintaining high availability is normally an operational consideration, load balancing is also a useful strategy in mitigating network-based DoS attacks. If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Load balancing provides service redundancy which reduces the susceptibility of the enclave to many DoS attacks. Since one of the primary purposes of the Application Delivery Controller is to balance loads across multiple servers, it would be extremely unusual for it to not be configured to perform this function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. Ask the Administrator which Application Delivery Services are being provided by the device. The following command displays information for Server Load Balancing: show slb If no Server Load Balancing sessions exist, this is a finding.

## Group: SRG-NET-000362-ALG-000126

**Group ID:** `V-237051`

### Rule: The A10 Networks ADC must enable DDoS filters.

**Rule ID:** `SV-237051r831326_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume, type, or protocol usage. Detection components that use signatures can detect known attacks by using known attack signatures. Signatures are usually obtained from and updated by the vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the device configuration and filters the output on the string "anomaly-drop": show run | inc anomaly-drop The output should display the following commands: ip anomaly-drop ip-option ip anomaly-drop land-attack ip anomaly-drop ping-of-death ip anomaly-drop frag ip anomaly-drop tcp-no-flag ip anomaly-drop tcp-syn-fin ip anomaly-drop tcp-syn-frag ip anomaly-drop out-of-sequence [threshold] ip anomaly-drop ping-of-death ip anomaly-drop zero-window [threshold] ip anomaly-drop bad-content If the output does not show these commands, this is a finding.

## Group: SRG-NET-000364-ALG-000122

**Group ID:** `V-237052`

### Rule: The A10 Networks ADC, when used to load balance web applications, must examine incoming user requests against the URI White Lists.

**Rule ID:** `SV-237052r831327_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic, which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Access control policies and access control lists implemented on devices that control the flow of network traffic (e.g., application level firewalls and Web content filters), ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the Internet or CDS) must be kept separate. The URI White List defines acceptable destination URIs allowed for incoming requests. The White List Check compares the URI of an incoming request against the rules contained in the URI White List policy file. Connection requests are accepted only if the URI matches a rule in the URI White List. Note: A URI Black List can also be configured, which takes priority over a URI White List. However, since deny-all, permit by exception is a fundamental principle, a URI White List is necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device is not used to load balance web servers, this is not applicable. Review the device configuration. The following command displays WAF templates: show slb template waf If the configured WAF template does not have the "uri-wlistcheck" option configured, this is a finding.

## Group: SRG-NET-000383-ALG-000135

**Group ID:** `V-237053`

### Rule: The A10 Networks ADC, when used to load balance web applications, must enable external logging for WAF data event messages.

**Rule ID:** `SV-237053r831328_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without coordinated reporting between separate devices, it is not possible to identify the true scale and possible target of an attack. External logging must be enabled for WAF data event messages. External logging is activated once the WAF template that uses the logging template is bound to an HTTP/HTTPS virtual port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device is not used to load balance web servers, this is not applicable. Review the device configuration and ask the device Administrator which templates are used. If no SLB instance for the log server(s) is configured, this is a finding. If there is no service group with assigned members for the log servers or the service group is not included in the logging template, this is a finding. If no logging template is configured and bound to the WAF template, this is a finding.

## Group: SRG-NET-000392-ALG-000141

**Group ID:** `V-237054`

### Rule: The A10 Networks ADC must enable logging for packet anomaly events.

**Rule ID:** `SV-237054r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. These systems must generate an alert when detection events from real-time monitoring occur. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The device must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The A10 Networks ADC must be configured to generate a log message when IP anomalies are detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the device configuration and filters the output on the string "log": show run | inc log If the output does not include the command "system anomaly log", this is a finding.

## Group: SRG-NET-000392-ALG-000142

**Group ID:** `V-237055`

### Rule: The A10 Networks ADC must generate an alert to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources (e.g., IAVMs or CTOs) are detected.

**Rule ID:** `SV-237055r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. The device generates an alert which notifies designated personnel of the Indicators of Compromise (IOCs) which require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The device must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the device administrator which method is used to send messages when threats are detected. Review the device configuration. If there is no method and target configured, this is a finding.

## Group: SRG-NET-000392-ALG-000148

**Group ID:** `V-237056`

### Rule: The A10 Networks ADC must enable logging of Denial of Service (DoS) attacks.

**Rule ID:** `SV-237056r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action, and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The device must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The A10 Networks ADC must be configured to generate a log message when IP anomalies and DoS attacks are detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the device configuration and filters the output on the string "log": show run | inc log If the output does not include the command "system attack log", this is a finding.

## Group: SRG-NET-000401-ALG-000127

**Group ID:** `V-237057`

### Rule: The A10 Networks ADC, when used for load-balancing web servers, must not allow the HTTP TRACE and OPTIONS methods.

**Rule ID:** `SV-237057r639618_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>HTTP offers a number of methods that can be used to perform actions on the web server. Some of these HTTP methods can be used for nefarious purposes if the web server is misconfigured. The two HTTP methods used for normal requests are GET and POST, so incoming requests should be limited to those methods. Although the HTTP TRACE method is useful for debugging, it enables cross-site scripting attacks. By exploiting certain browser vulnerabilities, an attacker may manipulate the TRACE method. The HEAD, GET, POST, and CONNECT methods are generally regarded as safe. For a WAF template, the GET and POST are the default values and are the safest options, so restriction the methods to GET and POST is recommended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ADC is not used to load balance web servers, this is not applicable. Interview the device administrator to determine which WAF template is used for web servers. Review the device configuration. The following command displays the configuration and filters the output on the WAF template section: show run | sec slb template waf If there is no WAF template, this is a finding. If the WAF template allows the HTTP TRACE method, this is a finding.

## Group: SRG-NET-000402-ALG-000130

**Group ID:** `V-237058`

### Rule: The A10 Networks ADC must reveal error messages only to authorized individuals (ISSO, ISSM, and SA).

**Rule ID:** `SV-237058r639621_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can give configuration details about the network element. Limiting access to system logs and administrative consoles to authorized personnel will help to mitigate this risk. However, user feedback and error messages should also be restricted by type and content in accordance with security best practices (e.g., ICMP messages). In the A10 Networks ADC, the audit log is maintained in a separate file separate from the system log. Access to the audit log is role-based. The audit log messages that are displayed for an admin depend upon that administrator’s role (privilege level). Administrators with Root, Read Write, or Read Only privileges who view the audit log can view all the messages, for all system partitions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. Enter the following command to view detailed information about the administrative accounts: show admin detail The output of this command will show the Access type, the Privilege level, and GUI role among other parameters. If persons other than other than the authorized individuals (ISSO, ISSM, and SA) have Root, Read Write, or Read Only privileges, this is a finding.

## Group: SRG-NET-000511-ALG-000051

**Group ID:** `V-237059`

### Rule: The A10 Networks ADC must, at a minimum, off-load audit log records onto a centralized log server.

**Rule ID:** `SV-237059r831332_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. Off-loading is a common process in information systems with limited audit storage capacity. The audit storage on the device is used only in a transitory fashion until the system can communicate with the centralized log server designated for storing the audit records, at which point the information is transferred. However, DoD requires that the log be transferred in real time which indicates that the time from event detection to off-loading is seconds or less. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the portion of the device configuration that includes the string "host": show run | inc host If the output does not display the "logging auditlog host" commands, this is a finding. The following command shows the logging policy: show log policy If Syslog logging is disabled, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-237060`

### Rule: The A10 Networks ADC, when used for load balancing web servers, must deploy the WAF in active mode.

**Rule ID:** `SV-237060r639627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Web Application Firewall (WAF) supports three operational modes - Learning, Passive, and Active. Active is the standard operational mode and must be used in order to drop or sanitize traffic. Learning mode is used in lab environments to initially set thresholds for certain WAF checks and should not be used in production networks. Passive mode applies enabled WAF checks, but no action is taken upon matching traffic. This mode is useful in identifying false positives for filtering. Only Active mode filters web traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the configuration and filters the output on the WAF template section: show run | sec slb template waf If the output contains either "deploy-mode passive" or "deploy-mode learning", this is a finding. Note: Since deploy-mode active is the default value, it will not appear in the output.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-237061`

### Rule: If the Data Owner requires it, the A10 Networks ADC must be configured to perform CCN Mask, SSN Mask, and PCRE Mask Request checks.

**Rule ID:** `SV-237061r639630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not continuously monitored, hostile activity may not be detected and prevented. Output from application and traffic monitoring serves as input to continuous monitoring and incident response programs. The A10 Networks ADC can be configured to mask data traversing outbound through the device. This is useful in preventing data exfiltration. If any data must be masked before it leaves the enclave (such as Credit Card Numbers, Social Security Numbers, or other sensitive information), a WAF template can be configured with CCN Mask, SSN Mask, and PCRE Mask Request checks. The Mask Request check depends on what information must be masked. This includes using Perl Compatible Regular Expressions (PCRE) for custom masks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration and ask the device Administrator which templates are used for masking sensitive data. The following command displays the configuration and filters the output on the WAF template section: show run | sec slb template waf If there is no WAF template with the required Mask Request checks, this is a finding.

## Group: SRG-NET-000362-ALG-000112

**Group ID:** `V-237062`

### Rule: The A10 Networks ADC must protect against ICMP-based Denial of Service (DoS) attacks by employing ICMP Rate Limiting.

**Rule ID:** `SV-237062r831333_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Detection components that use rate-based behavior analysis can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. Rate-based behavior analysis can detect sophisticated, Distributed DoS (DDoS) attacks by correlating traffic information from multiple network segments or components. The A10 Networks ADC provides an ICMP Rate Limiting feature that monitors the rate of ICMP traffic and drops ICMP packets when the configured thresholds (the normal rate) are exceeded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the device configuration and filters the output on the string "icmp-rate-limit": show run | inc icmp-rate-limit If ICMP rate limiting is not configured, this is a finding. If no lockout period and maximum rates are configured as an action, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-237063`

### Rule: The A10 Networks ADC must protect against TCP SYN floods by using TCP SYN Cookies.

**Rule ID:** `SV-237063r639636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A SYN flood is a form of denial-of-service attack in which an attacker sends a succession of SYN requests to a target in an attempt to consume resources, making the device unresponsive to legitimate traffic. TCP SYN Cookies are commonly implemented by the Operating System on endpoints, but are also often implemented on network devices. A10 Networks ADCs provide protection against TCP SYN flood attacks by using SYN cookies. SYN cookies enable the device to continue to serve legitimate clients during a TCP SYN flood attack without allowing illegitimate traffic to consume system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the device configuration and filters the output on the string "syn-cookie": show run | inc syn-cookie If SYN cookies are not enabled, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-237064`

### Rule: The A10 Networks ADC must be a FIPS-compliant version.

**Rule ID:** `SV-237064r639639_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. FIPS compliance is mandated for many functions of network devices. The A10 Networks ADC platforms are either FIPS-compliant versions or non-compliant versions. It is necessary to deploy the FIPS-compliant versions of the model(s). FIPS versions are identified by the designation "FIPS" in the stock keeping unit (SKU).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following command shows the version of ACOS used and other related information: show version If the output does not include "Platform features: fips", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-264425`

### Rule: The A10 Networks ALG must be using a version supported by the vendor.

**Rule ID:** `SV-264425r992072_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

