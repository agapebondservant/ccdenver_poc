# STIG Benchmark: F5 BIG-IP Local Traffic Manager Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-215738`

### Rule: The BIG-IP Core implementation must be configured to enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies.

**Rule ID:** `SV-215738r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary and access control mechanisms are required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to enforce approved authorizations for logical access to information and system resources employing identity-based, role-based, and/or attribute-based security policies. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an access policy to enforce approved authorizations for logical access to information. If the BIG-IP Core is not configured to enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies, this is a finding.

## Group: SRG-NET-000018-ALG-000017

**Group ID:** `V-215739`

### Rule: The BIG-IP Core implementation must be configured to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-215739r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, devices) within information systems. Examples of information flow control restrictions include keeping export-controlled information from being transmitted in the clear to the Internet or blocking information marked as classified but being transported to an unapproved destination. ALGs enforce approved authorizations by employing security policy and/or rules that restrict information system services, provide packet-filtering capability based on header or protocol information, and/or message filtering capability based on data content (e.g., implementing key word searches or using document characteristics).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform packet-filtering intermediary services for virtual servers, this is not applicable. When packet-filtering intermediary services are performed, verify the BIG-IP Core is configured as follows: Verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an AFM policy to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Network Firewall" Enforcement is set to "Policy Rules..." and "Policy" is set to use an AFM policy to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. If the BIG-IP Core is not configured to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic, this is a finding.

## Group: SRG-NET-000019-ALG-000018

**Group ID:** `V-215740`

### Rule: The BIG-IP Core implementation must be configured to restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-215740r557356_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. Blocking or restricting detected harmful or suspicious communications between interconnected networks enforces approved authorizations for controlling the flow of traffic. This requirement applies the Application Layer Gateway (ALG) when used as a gateway or boundary device that allows traffic flow between interconnected networks of differing security policies. The ALG is installed and configured in such a way that it restricts or blocks information flows based on guidance in the Ports, Protocols, and Services Management (PPSM) regarding restrictions for boundary crossing for ports, protocols and services. Information flow restrictions may be implemented based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. The ALG must be configured with policy filters (e.g., security policy, rules, and/or signatures) that restrict or block information system services; provide a packet-filtering capability based on header information; and/or perform message filtering based on message content. The policy filters used depend upon the type of application gateway (e.g., web, email, or TLS).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform packet-filtering intermediary services for virtual servers, this is not applicable. When packet-filtering intermediary services are performed, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module is configured with an AFM policy to restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Network Firewall" Enforcement is set to "Policy Rules..." and "Policy" is set to use an AFM policy to restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. If the BIG-IP Core is not configured to restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic, this is a finding.

## Group: SRG-NET-000041-ALG-000022

**Group ID:** `V-215741`

### Rule: The BIG-IP Core implementation must be configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to virtual servers.

**Rule ID:** `SV-215741r557356_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the virtual servers ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to network elements that have the concept of a user account and have the logon function residing on the network element. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to ALGs (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the virtual servers. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an access policy to display the Standard Mandatory DoD-approved Notice and Consent Banner. If the BIG-IP Core is not configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the virtual servers, this is a finding.

## Group: SRG-NET-000042-ALG-000023

**Group ID:** `V-215742`

### Rule: The BIG-IP Core implementation must be configured to retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users accessing virtual servers acknowledge the usage conditions and take explicit actions to log on for further access.

**Rule ID:** `SV-215742r557356_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The banner must be acknowledged by the user prior to allowing the user access to virtual servers. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the application usage policy, a click-through banner at application logon is required. The network element must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an access policy to retain the Standard Mandatory DoD-approved Notice and Consent Banner. If the BIG-IP Core is not configured to retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access, this is a finding.

## Group: SRG-NET-000043-ALG-000024

**Group ID:** `V-215743`

### Rule: The BIG-IP Core implementation must be configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to publicly accessible applications.

**Rule ID:** `SV-215743r557356_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible network element ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to network elements that have the concept of a user account and have the logon function residing on the network element. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services off-loaded from the application. Publicly accessed systems are used in DoD to provide benefit information, pay information, or public services. There may also be self-registration and authorization services provided by these gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to publicly accessible applications. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an access policy to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to publicly accessible applications. If the BIG-IP Core is not configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the publicly accessible systems, this is a finding.

## Group: SRG-NET-000053-ALG-000001

**Group ID:** `V-215744`

### Rule: The BIG-IP Core implementation must be configured to limit the number of concurrent sessions to an organization-defined number for virtual servers.

**Rule ID:** `SV-215744r557356_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network element management includes the ability to control the number of users and user sessions that utilize a network element. Limiting the number of current sessions per user is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The organization-defined number of concurrent sessions must be the same as the requirements specified for the application for which it serves as intermediary. This policy only applies to application gateways/firewalls (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP Core limits the number of concurrent sessions to an organization-defined number for virtual servers. Review organizational Standard Operating Procedures (SOP) to ensure there is an organization-defined threshold for the maximum number of concurrent session for each application the BIG-IP Core serves as intermediary. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select a Virtual Server from the list to verify that the connection limit is set. Select "Advanced" for "Configuration". Review the following under the "Configuration" section. Verify that 'Connection Limit' is set to the organization-defined number of concurrent connections and not set to zero (0). Verify that "Connection Rate Limit" is set to the organization-defined number of concurrent connections per second and not set to zero (0). If the BIG-IP Core is not configured to limit the number of concurrent sessions to an organization-defined number or is set to zero (0) for virtual servers, this is a finding.

## Group: SRG-NET-000061-ALG-000009

**Group ID:** `V-215745`

### Rule: The BIG-IP Core implementation must be configured to monitor inbound traffic for remote access policy compliance when accepting connections to virtual servers.

**Rule ID:** `SV-215745r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access traffic allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by inspecting connection activities of remote access capabilities. A remote access policy establishes and documents usage restrictions, configuration/connection requirements, and implementation guidance for each type of remote access allowed prior to allowing connections to the information systems. Remote access methods include both unencrypted and encrypted traffic (e.g., web portals, web content filter, TLS, and webmail). With inbound TLS inspection, the traffic must be inspected prior to being allowed on the enclave's web servers hosting TLS or HTTPS applications. With outbound traffic inspection, traffic must be inspected prior to being forwarded to destinations outside of the enclave, such as external email traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not serve as an intermediary for remote access traffic (e.g., web content filter, TLS, and webmail) for virtual servers, this is not applicable. When intermediary services for remote access communications traffic are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to inspect traffic or forward to a monitoring device for inspection prior to forwarding to inbound destinations. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to use an ASM policy to monitor inbound traffic for remote access policy compliance when accepting remote access connections to virtual servers. If the BIG-IP Core is not configured to monitor inbound traffic for compliance with remote access security policies, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-215746`

### Rule: The BIG-IP Core implementation must be configured to use encryption services that implement NIST SP 800-52 Revision 2 compliant cryptography to protect the confidentiality of connections to virtual servers.

**Rule ID:** `SV-215746r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Encryption provides a means to secure the remote connection so as to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. This requirement applies to ALGs providing remote access proxy services as part of their intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not serve as an intermediary for remote access traffic (e.g., web content filter, TLS, and webmail) for virtual servers, this is not applicable. When intermediary services for remote access communications are provided, verify the BIG-IP Core is configured to use encryption services that implement NIST SP 800-52 Revision 2 compliant cryptography to protect the confidentiality of connections to virtual servers. Navigate to the BIG-IP System manager >> Local Traffic >> Profiles >> SSL >> Client Verify a profile exists that is FIPS compliant. Select FIPS-compliant profile. Verify "Ciphers" under "Configuration" section is configured to use FIPS-compliant ciphers. Verify the BIG-IP Core is configured to use a FIPS-compliant profile: Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Configuration" section, that FIPS-compliant profile is in the "Selected" area for "SSL Profile (Client)". If the BIG-IP Core is not configured to use encryption services that implement NIST SP 800-52 Revision 1 compliant cryptography to protect the confidentiality of connections to virtual servers, this is a finding.

## Group: SRG-NET-000062-ALG-000150

**Group ID:** `V-215747`

### Rule: The BIG-IP Core implementation must be configured to comply with the required TLS settings in NIST SP 800-52 Revision 1 for TLS services to virtual servers.

**Rule ID:** `SV-215747r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIST SP 800-52 Revision 1 provides guidance on using the most secure version and configuration of the TLS/SSL protocol. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to TLS gateways (also known as SSL gateways) and is not applicable to VPN devices. Application protocols such as HTTPS and DNSSEC use TLS/SSL as the underlying security protocol and thus are in scope for this requirement. NIST SP 800-52 Revision 1 provides guidance. NIST SP 800-52 Revision 1 sets TLS version 1.1 as a minimum version, thus all versions of SSL are not allowed (including for client negotiation) either on DoD-only or on public facing servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS) for virtual servers, this is not applicable. When intermediary services for TLS are provided, verify the BIG-IP Core is configured to implement the applicable required TLS settings in NIST PUB SP 800-52 Revision 1. Navigate to the BIG-IP System manager >> Local Traffic >> Profiles >> SSL >> Client Verify a profile exists that is FIPS compliant. Select FIPS-compliant profile. Select "Advanced" next to "Configuration". Verify "Ciphers" under "Configuration" section is configured to use FIPS-compliant ciphers. Verify the BIG-IP Core is configured to use FIPS-compliant server profile: Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Configuration" section, that the FIPS-compliant profile is in the "Selected" area for "SSL Profile (Client)". If the BIG-IP Core is not configured to implement the applicable required TLS settings in NIST PUB SP 800-52 Revision 1, this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-215748`

### Rule: The BIG-IP Core implementation must be configured to use NIST SP 800-52 Revision 1 compliant cryptography to protect the integrity of remote access sessions to virtual servers.

**Rule ID:** `SV-215748r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of their intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not serve as an intermediary for remote access traffic (e.g., web content filter, TLS gateways, and webmail proxy views) for virtual servers, this is not applicable. When intermediary services for remote access communication traffic are provided, verify the BIG-IP Core uses NIST SP 800-52 Revision 1 compliant cryptography to protect the integrity of remote access sessions to virtual servers. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Configuration" section, that a FIPS-compliant profile is in the "Selected" area for "SSL Profile (Client)" and "SSL Profile (Server)". If the BIG-IP Core is not configured to use NIST SP 800-52 Revision 1 compliant cryptography to protect the integrity of remote access sessions, this is a finding.

## Group: SRG-NET-000098-ALG-000056

**Group ID:** `V-215749`

### Rule: The BIG-IP Core implementation must be configured to protect audit information from unauthorized read access.

**Rule ID:** `SV-215749r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or to simply identify an improperly configured network element. Thus, it is imperative that the collected log data from the various network elements, as well as the auditing tools, be secured and can only be accessed by authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to protect audit information from unauthorized read access. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Under 'Log Access', verify unauthorized roles are set to 'Deny'. If the BIG-IP Core is not configured to protect audit information from unauthorized read access, this is a finding.

## Group: SRG-NET-000099-ALG-000057

**Group ID:** `V-215750`

### Rule: The BIG-IP Core implementation must be configured to protect audit information from unauthorized modification.

**Rule ID:** `SV-215750r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to protect audit information from unauthorized modification. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Under 'Log Access', verify unauthorized roles are set to 'Deny'. If the BIG-IP Core is not configured to protect audit information from unauthorized modification, this is a finding.

## Group: SRG-NET-000100-ALG-000058

**Group ID:** `V-215751`

### Rule: The BIG-IP Core implementation must be configured to protect audit information from unauthorized deletion.

**Rule ID:** `SV-215751r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions, and limiting log data locations. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. This requirement does not apply to audit logs generated on behalf of the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to protect audit information from unauthorized deletion. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Under 'Log Access', verify unauthorized roles are set to 'Deny'. If the BIG-IP Core is not configured to protect audit information from unauthorized deletion, this is a finding.

## Group: SRG-NET-000101-ALG-000059

**Group ID:** `V-215752`

### Rule: The BIG-IP Core implementation must be configured to protect audit tools from unauthorized access.

**Rule ID:** `SV-215752r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network elements providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to protect audit tools from unauthorized access. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Under 'Log Access', verify unauthorized roles are set to 'Deny'. If the BIG-IP Core is not configured to protect audit tools from unauthorized access, this is a finding.

## Group: SRG-NET-000102-ALG-000060

**Group ID:** `V-215753`

### Rule: The BIG-IP Core implementation must be configured to protect audit tools from unauthorized modification.

**Rule ID:** `SV-215753r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network elements providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to protect audit tools from unauthorized modification. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Under 'Log Access', verify unauthorized roles are set to 'Deny'. If the BIG-IP Core is not configured to protect audit tools from unauthorized modification, this is a finding.

## Group: SRG-NET-000103-ALG-000061

**Group ID:** `V-215754`

### Rule: The BIG-IP Core implementation must be configured to protect audit tools from unauthorized deletion.

**Rule ID:** `SV-215754r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network elements providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to protect audit information from unauthorized read access. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Under 'Log Access', verify unauthorized roles are set to 'Deny'. If the BIG-IP Core is not configured to protect audit information from unauthorized deletion, this is a finding.

## Group: SRG-NET-000131-ALG-000085

**Group ID:** `V-215755`

### Rule: The BIG-IP Core implementation must be configured so that only functions, ports, protocols, and/or services that are documented for the server/application for which the virtual servers are providing connectivity.

**Rule ID:** `SV-215755r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the ALG. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The primary function of an ALG is to provide application-specific content filtering and/or proxy services. The ALG application suite may integrate related content filtering and analysis services and tools (e.g., IPS, proxy, malware inspection, black/white lists). Some gateways may also include email scanning, decryption, caching, and DLP services. However, services and capabilities which are unrelated to this primary functionality must not be installed (e.g., DNS, email client or server, FTP server, or web server). Next Generation ALGs (NGFW) and Unified Threat Management (UTM) ALGs integrate functions which have been traditionally separated. These products integrate content filtering features to provide more granular policy filtering. There may be operational drawbacks to combining these services into one device. Another issue is that NGFW and UTM products vary greatly with no current definitive industry standard.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BIG-IP Core configuration to determine if functions, ports, protocols, and/or services not required for operation, or not related to BIG-IP Core functionality (e.g., DNS, email client or server, FTP server, or web server) are enabled. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Review the Virtual Service List and validate all ports listed in the "Service Port" column are documented for each virtual server and are required for operation. If unnecessary services and functions are enabled on the BIG-IP Core, this is a finding. If the BIG-IP Core implementation is configured with functions, ports, protocols, and/or services that are not documented for the server/application for which the virtual servers are providing connectivity, this is a finding.

## Group: SRG-NET-000131-ALG-000086

**Group ID:** `V-215756`

### Rule: The BIG-IP Core implementation must be configured to remove or disable any functions, ports, protocols, and/or services that are not documented as required.

**Rule ID:** `SV-215756r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrelated or unneeded proxy services increase the attack vector and add excessive complexity to the securing of the ALG. Multiple application proxies can be installed on many ALGs. However, proxy types must be limited to related functions. At a minimum, the web and email gateway represent different security domains/trust levels. Organizations should also consider separation of gateways that service the DMZ and the trusted network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BIG-IP Core configuration to determine if application proxies are installed that are not related to the purpose of the gateway. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Review the Virtual Service List and validate there are only ports listed in the "Service Port" column that are providing proxy services related to the purpose of the BIG-IP Core. If the BIG-IP Core has unrelated or unneeded application proxy services installed, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-215757`

### Rule: The BIG-IP Core implementation must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the Ports, Protocol, and Service Management (PPSM) Category Assurance List (CAL) and vulnerability assessments.

**Rule ID:** `SV-215757r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols, or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The ALG is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older versions of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BIG-IP Core to verify the minimum ports, protocols, and services that are required for operation of the BIG-IP Core are configured. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Compare enabled ports, protocols, and/or services in the "Service Port" column with the PPSM and IAVM requirements. If the BIG-IP Core is configured with ports, protocols, and/or services that are not required for operations or restricted by the PPSM, this is a finding.

## Group: SRG-NET-000138-ALG-000063

**Group ID:** `V-215758`

### Rule: The BIG-IP Core implementation must be configured to uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users) when connecting to virtual servers.

**Rule ID:** `SV-215758r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication. 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement applies to ALGs that provide user proxy services, including identification and authentication. This service must use the site's directory service (e.g., Active Directory). Directory services must not be installed onto the gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify the BIG-IP Core is configured with an APM policy to uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users). Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an APM access policy to uniquely identify and authenticate organizational users when connecting to virtual servers. If the BIG-IP Core does not uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users), this is a finding.

## Group: SRG-NET-000138-ALG-000088

**Group ID:** `V-215759`

### Rule: The BIG-IP Core implementation must be configured with a pre-established trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or authentication, authorization, and accounting (AAA) server) that validate user account access authorizations and privileges when providing access control to virtual servers.

**Rule ID:** `SV-215759r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User account and privilege validation must be centralized in order to prevent unauthorized access using changed or revoked privileges. ALGs can implement functions such as traffic filtering, authentication, access, and authorization functions based on computer and user privileges. However, the directory service (e.g., Active Directory or LDAP) must not be installed on the ALG, particularly if the gateway resides on the untrusted zone of the Enclave.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP Core is configured an APM policy with a pre-established trust relationship and mechanisms with appropriate authorities that validate each user access authorization and privileges. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an APM access policy that has been configured with a pre-established trust relationship and mechanisms with appropriate authorities that validate each user access authorization and privileges. If the BIG-IP Core is not configured with a pre-established trust relationship and mechanisms with appropriate authorities that validate each user access authorization and privileges, this is a finding.

## Group: SRG-NET-000138-ALG-000089

**Group ID:** `V-215760`

### Rule: The BIG-IP Core implementation providing user authentication intermediary services must restrict user authentication traffic to specific authentication server(s) when providing access control to virtual servers.

**Rule ID:** `SV-215760r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User authentication can be used as part of the policy filtering rule sets. Some URLs or network resources can be restricted to authenticated users only. Users are prompted by the application or browser for credentials. Authentication service may be provided by the ALG as an intermediary for the application; however, the authentication credential must be stored in the site's directory services server. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., proxy capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to use a specific authentication server(s). Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section that "Access Policy" has been set to use an APM access policy that has been configured with a pre-established trust relationship and mechanisms with appropriate authorities that validate each user access authorization and privileges. If the BIG-IP Core provides user authentication intermediary services and does not restrict user authentication traffic to a specific authentication server(s), this is a finding.

## Group: SRG-NET-000140-ALG-000094

**Group ID:** `V-215761`

### Rule: The BIG-IP Core implementation providing user authentication intermediary services must use multifactor authentication for network access to non-privileged accounts when granting access to virtual servers.

**Rule ID:** `SV-215761r954210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1) Something you know (e.g., password/PIN); 2) Something you have (e.g., cryptographic, identification device, token); and 3) Something you are (e.g., biometric). Non-privileged accounts are not authorized on the network element regardless of configuration. Network access is any access to an application by a user (or process acting on behalf of a user) where said access is obtained through a network connection. The DoD CAC with DoD-approved PKI is an example of multifactor authentication. This requirement applies to ALGs that provide user authentication intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to use multifactor authentication for network access to non-privileged accounts. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an APM access policy that uses multifactor authentication for network access to non-privileged accounts when granting access to virtual servers. If the BIG-IP Core provides user authentication intermediary services and does not use multifactor authentication for network access to non-privileged accounts, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-215762`

### Rule: The BIG-IP Core implementation must be configured to validate certificates used for TLS functions for connections to virtual servers by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-215762r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A trust anchor is an authoritative entity represented via a public key. Within a chain of trust, the top entity to be trusted is the "root certificate" or "trust anchor" such as a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Deploying the ALG with TLS enabled may require the CA certificates for each proxy to be used for TLS traffic decryption/encryption. The installation of these certificates in each trusted root certificate store is used by proxied applications and browsers on each client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS) for virtual servers, this is not applicable. When intermediary services for TLS are provided, verify the BIG-IP Core is configured to validate certificates used for TLS functions by constructing a certification path to an accepted trust anchor. Navigate to the BIG-IP System manager >> Local traffic >> Profiles >> SSL >> Server. Select a FIPS-compliant profile. Review the configuration under "Server Authentication" section. Verify "Server Certificate" is set to "Required". Verify "Trusted Certificate Authorities" is set to a DoD-approved CA bundle. If the BIG-IP Core is not configured to validate certificates used for TLS functions by constructing a certification path to an accepted trust anchor, this is a finding.

## Group: SRG-NET-000166-ALG-000101

**Group ID:** `V-215763`

### Rule: The BIG-IP Core implementation providing PKI-based, user authentication intermediary services must be configured to map the authenticated identity to the user account for PKI-based authentication to virtual servers.

**Rule ID:** `SV-215763r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authorization for access to any network element requires an approved and assigned individual account identifier. To ensure only the assigned individual is using the account, the account must be bound to a user certificate when PKI-based authentication is implemented. This requirement applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide PKI-based, user authentication intermediary services for virtual servers, this is not applicable. When PKI-based, user authentication intermediary services are provided, verify the BIG-IP LTM module is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to map the authenticated identity to the user account for PKI-based authentication. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an APM access policy that maps the authenticated identity to the user account for PKI-based authentication to virtual servers. If the BIG-IP Core does not map the authenticated identity to the user account for PKI-based authentication, this is a finding.

## Group: SRG-NET-000169-ALG-000102

**Group ID:** `V-215764`

### Rule: The BIG-IP Core implementation must be configured to uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users) when connecting to virtual servers.

**Rule ID:** `SV-215764r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication enables anyone to gain access to the network or possibly a network element that provides opportunity for intruders to compromise resources within the network infrastructure. By identifying and authenticating non-organizational users, their access to network resources can be restricted accordingly. Non-organizational users will be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access. Authorization requires an individual account identifier that has been approved, assigned, and configured on an authentication server. Authentication of user identities is accomplished through the use of passwords, tokens, biometrics, or in the case of multifactor authentication, some combination thereof. This control applies to application layer gateways that provide content filtering and proxy services on network segments (e.g., DMZ) that allow access by non-organizational users. This requirement focuses on authentication requests to the proxied application for access to destination resources and policy filtering decisions rather than administrator and management functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services are provided, review the BIG-IP LTM module authentication functions to verify identification and authentication are required for non-organizational users. Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users) when connecting to virtual servers. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. If the BIG-IP Core does not uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users) when connecting to virtual servers, this is a finding.

## Group: SRG-NET-000213-ALG-000107

**Group ID:** `V-215765`

### Rule: The BIG-IP Core implementation must terminate all communications sessions at the end of the session or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity, and for user sessions (nonprivileged sessions), the session must be terminated after 15 minutes of inactivity.

**Rule ID:** `SV-215765r971530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system level network connection. ALGs may provide session control functionality as part of content filtering, load balancing, or proxy services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to terminate all communications at the end of the session as follows: Verify a Protocol Profile is configured to terminate a session at the end of a specified time. Navigate to the BIG-IP System manager >> Local Traffic >> Profiles >> Protocol >> TCP. Select a profile for an in-band managed session. Verify the TCP profile "idle-timeout" is set to 600/900 seconds. Select a profile for a user session. Verify the TCP profile "idle-timeout" is set to 600/900 seconds. Verify the BIG-IP LTM is configured to use the Protocol Profile. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select the appropriate virtual server. Verify the TCP profile "idle-timeout" is set to 600/900 seconds. If the BIG-IP Core is not configured to terminate all communications session at the end of the session or as follows, this is a finding: - For in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity. - For user sessions (nonprivileged sessions), the session must be terminated after 15 minutes of inactivity.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-215766`

### Rule: The BIG-IP Core implementation must be configured to protect the authenticity of communications sessions.

**Rule ID:** `SV-215766r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. This requirement focuses on communications protection for the application session rather than for the network packet and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of TLS/TLS mutual authentication (two-way/bidirectional).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to protect the authenticity of communications sessions. Navigate to the BIG-IP System manager >> Local Traffic >> Profiles >> SSL >> Client Verify a profile exists that is FIPS compliant. Select FIPS-compliant profile. Select "Advanced" next to "Configuration". Verify "Ciphers" under "Configuration" section is configured to use FIPS-compliant ciphers. Verify the BIG-IP Core is configured to use FIPS-compliant profile: Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Server(s) from the list that the LTM module is managing the Client SSL side traffic. Verify under "Configuration" section, that FIPS-compliant profile is in the "Selected" area for "SSL Profile (Client)". If the BIG-IP Core is not configured to protect the authenticity of communications sessions, this is a finding.

## Group: SRG-NET-000313-ALG-000010

**Group ID:** `V-215772`

### Rule: The BIG-IP Core implementation providing intermediary services for remote access communications traffic must control remote access methods to virtual servers.

**Rule ID:** `SV-215772r831460_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). ALGs that proxy remote access must be capable of taking enforcement action (i.e., blocking, restricting, or forwarding to an enforcement mechanism) if traffic monitoring reveals unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not serve as an intermediary for remote access traffic (e.g., web content filter, TLS, and webmail) for virtual servers, this is not applicable. When intermediary services for remote access communications are provided, verify the BIG-IP Core is configured to control remote access methods. Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to control remote access methods. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section that "Access Policy" has been set to use an APM access policy that controls remote access methods to virtual servers. If the BIG-IP Core does not control remote access methods, this is a finding.

## Group: SRG-NET-000318-ALG-000014

**Group ID:** `V-215773`

### Rule: To protect against data mining, the BIG-IP Core implementation must be configured to prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields when providing content filtering to virtual servers.

**Rule ID:** `SV-215773r831461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware into a computer to execute remote commands that can read or modify a database or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. Compliance requires the ALG to have the capability to prevent code injections. Examples include Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to use an ASM policy to prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields when providing content filtering to virtual servers. If the BIG-IP Core is not configured to prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields, this is a finding.

## Group: SRG-NET-000318-ALG-000151

**Group ID:** `V-215774`

### Rule: To protect against data mining, the BIG-IP Core implementation providing content filtering must be configured to prevent code injection attacks from being launched against application objects, including, at a minimum, application URLs and application code.

**Rule ID:** `SV-215774r831462_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware into a computer to execute remote commands that can read or modify a database or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. Compliance requires the ALG to have the capability to prevent code injections. Examples include Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to prevent code injection attacks from being launched against application objects, including, at a minimum, application URLs, and application code and application. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to use an ASM policy to prevent code injection attacks from being launched against application objects, including, at a minimum, application URLs and application code. If the BIG-IP Core is not configured to prevent code injection attacks from being launched against application objects, including, at a minimum, application URLs and application code, this is a finding.

## Group: SRG-NET-000318-ALG-000152

**Group ID:** `V-215775`

### Rule: To protect against data mining, the BIG-IP Core implementation providing content filtering must be configured to prevent SQL injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-215775r831463_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. Compliance requires the ALG to have the capability to prevent SQL code injections. Examples include Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to prevent SQL injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, and database fields. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to use an ASM policy to prevent SQL injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, and database fields. If the BIG-IP Core is not configured to prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields, this is a finding.

## Group: SRG-NET-000319-ALG-000015

**Group ID:** `V-215776`

### Rule: To protect against data mining, the BIG-IP Core implementation providing content filtering must be configured to detect code injection attacks being launched against data storage objects.

**Rule ID:** `SV-215776r831464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware into a computer to execute remote commands that can read or modify a database or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. ALGs with anomaly detection must be configured to protect against unauthorized code injections. These devices must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses. Examples include Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to detect code injection attacks being launched against data storage objects. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to detect code injection attacks being launched against data storage objects. If the BIG-IP Core is not configured to detect code injection attacks being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields, this is a finding.

## Group: SRG-NET-000319-ALG-000020

**Group ID:** `V-215777`

### Rule: To protect against data mining, the BIG-IP Core implementation providing content filtering must be configured to detect SQL injection attacks being launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-215777r831465_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational databases may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. ALGs with anomaly detection must be configured to protect against unauthorized data mining attacks. These devices must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses. Examples include Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to detect SQL injection attacks being launched against data storage objects, including, at a minimum, databases, database records, and database fields. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to detect SQL injection attacks being launched against data storage objects, including, at a minimum, databases, database records, and database fields. If the BIG-IP Core is not configured to detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields, this is a finding.

## Group: SRG-NET-000319-ALG-000153

**Group ID:** `V-215778`

### Rule: The BIG-IP Core implementation must be configured to detect code injection attacks being launched against application objects, including, at a minimum, application URLs and application code, when providing content filtering to virtual servers.

**Rule ID:** `SV-215778r831466_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational applications may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware into a computer to execute remote commands that can read or modify a database or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. ALGs with anomaly detection must be configured to protect against unauthorized code injections. These devices must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses. Examples include Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to detect code injection attacks being launched against application objects, including, at a minimum, application URLs and application code. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to detect code injection attacks being launched against application objects, including, at a minimum, application URLs and application code, when providing content filtering to virtual servers. If the BIG-IP Core is not configured to detect code injection attacks from being launched against application objects, including, at a minimum, application URLs and application code, this is a finding.

## Group: SRG-NET-000337-ALG-000096

**Group ID:** `V-215779`

### Rule: The BIG-IP Core implementation must require users to reauthenticate when the user's role, the information authorizations, and/or the maximum session timeout is exceeded for the virtual server(s).

**Rule ID:** `SV-215779r1050784_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which authorization has been removed. In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of individuals and/or devices in other situations. Within the DOD, the minimum circumstances requiring reauthentication are privilege escalation, idle timeout, maximum session timeout, and/or role changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to require users to reauthenticate when required by organization-defined circumstances or situations. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section that "Access Policy" has been set to use an APM access policy that requires users to reauthenticate to virtual servers when the user's role, the information authorizations, and/or the maximum session timeout is exceeded for the virtual server(s). If the BIG-IP Core is not configured to require users to reauthenticate when the user's role, the information authorizations, and/or the maximum session timeout is exceeded for the virtual server(s), this is a finding.

## Group: SRG-NET-000339-ALG-000090

**Group ID:** `V-215780`

### Rule: A BIG-IP Core implementation providing user authentication intermediary services must be configured to require multifactor authentication for remote access to non-privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-215780r981642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For remote access to non-privileged accounts, the purpose of requiring a device that is separate from the information system gaining access for one of the factors during multifactor authentication is to reduce the likelihood of compromising authentication credentials stored on the system. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. An example of compliance with this requirement is the use of a one-time password token and PIN coupled with a password; or the use of a CAC/PIV card and PIN coupled with a password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to require multifactor authentication for remote access to non-privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section that "Access Policy" has been set to use an APM access policy to require multifactor authentication for remote access to non-privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access. If the BIG-IP Core does not implement multifactor authentication for remote access to non-privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access, this is a finding.

## Group: SRG-NET-000340-ALG-000091

**Group ID:** `V-215781`

### Rule: The BIG-IP Core implementation providing user authentication intermediary services must be configured to require multifactor authentication for remote access with privileged accounts to virtual servers in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-215781r981643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For remote access to privileged accounts, the purpose of requiring a device that is separate from the information system gaining access for one of the factors during multifactor authentication is to reduce the likelihood of compromising authentication credentials stored on the system. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to require multifactor authentication for remote access with privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an APM access policy to require multifactor authentication for remote access with privileged accounts to virtual servers in such a way that one of the factors is provided by a device separate from the system gaining access. If the BIG-IP Core does not implement multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access, this is a finding.

## Group: SRG-NET-000345-ALG-000099

**Group ID:** `V-215784`

### Rule: The BIG-IP Core implementation must be configured to deny-by-default all PKI-based authentication to virtual servers supporting path discovery and validation if unable to access revocation information via the network.

**Rule ID:** `SV-215784r981644_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When revocation data is unavailable from the network, the system should be configured to deny-by-default to mitigate the risk of a user with a revoked certificate gaining unauthorized access. Local cached revocation data can be out of date or not able to be installed on the local system, which increases administration burden for the system. The intent of this requirement is to deny unauthenticated users access to virtual servers in case access to OCSP (required by CCI-000185) is not available. This requirement applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services are provided, verify the BIG-IP Core is configured to deny-by-default user access when revocation information is not accessible via the network. Navigate to the BIG-IP System manager >> Local Traffic >> Profiles >> SSL >> Client. Select an SSL client profile that is used for client authentication with Virtual Server(s). Review the configuration under the "Client Authentication" section. Verify that "Client Certificate" is set to "require" if not using the APM. Verify that “On Demand Cert Auth” in the access profile is set to “Require” if using APM. If the BIG-IP Core is not configured to deny-by-default when unable to access revocation information via the network, this is a finding.

## Group: SRG-NET-000349-ALG-000106

**Group ID:** `V-215788`

### Rule: The BIG-IP Core implementation must be able to conform to FICAM-issued profiles when providing authentication to virtual servers.

**Rule ID:** `SV-215788r981646_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without conforming to Federal Identity, Credential, and Access Management (FICAM)-issued profiles, the information system may not be interoperable with FICAM-authentication protocols, such as SAML 2.0 and OpenID 2.0. Use of FICAM-issued profiles addresses open identity management standards. This requirement only applies to components where this is specific to the function of the device or has the concept of a non-organizational user, (e.g., ALG capability that is the front end for an application in a DMZ).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user authentication intermediary services for virtual servers, this is not applicable. When user authentication intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to conform to FICAM-issued profiles when providing authentication. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section that "Access Policy" has been set to conform to FICAM-issued profiles when providing authentication to pools/nodes. If the BIG-IP Core is not configured to conform to FICAM-issued profiles, this is a finding.

## Group: SRG-NET-000355-ALG-000117

**Group ID:** `V-215789`

### Rule: The F5 BIG-IP appliance providing user authentication intermediary services must only accept end entity certificates issued by DOD PKI or DOD-approved PKI Certification Authorities (CAs) for the establishment of protected sessions.

**Rule ID:** `SV-215789r947428_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DOD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place that are sufficient for DOD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DOD-approved PKIs is published at https://cyber.mil/pki-pke/interoperability. DOD-approved PKI CAs may include Category I, II, and III certificates. Category I DOD-Approved External PKIs are PIV issuers. Category II DOD-Approved External PKIs are Non-Federal Agency PKIs cross-certified with the Federal Bridge Certification Authority (FBCA). Category III DOD-Approved External PKIs are Foreign, Allied, or Coalition Partner PKIs. This requirement focuses on communications protection for the application session rather than for the network packet. Thus, a critical part of the PKI configuration for BIG-IP appliances includes requiring mutual TLS (mTLS). Use of mTLS ensures session nonrepudiation, communication integrity, and confidentiality. This approach substantially reduces the likelihood of successful server-side exploits and cookie hijacking. In the Client Authentication section of the Client SSL Profile applied to the pertinent Virtual Server, the Client Certificate configuration session must be altered from "request/ignore" to "require". This modification mandates all connecting clients to furnish a Client Certificate issued from a credible source. If a client fails to comply with this requirement, they will be issued a TCP reset.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide PKI-based user authentication intermediary services, this is not applicable. Client SSL Profile: From the BIG-IP GUI: 1. Local Traffic. 2. Profiles. 3. SSL. 4. Client. 5. Click the name of the client SSL profile. 6. Change "Configuration" to "Advanced". 7. Under "Client Authentication", verify a DOD PKI certificate or bundle is used for "Trusted Certificate Authorities". 8. Verify the Client Certificate configuration setting is set to "require" and frequency is set to "always". Virtual Server: From the BIG-IP GUI: 1. Local Traffic. 2. Virtual Servers. 3. Virtual Server List. 4. Click the name of the Virtual Server. 5. Verify that "SSL Profile (Client)" is using an SSL profile that uses a DOD PKI certificate or bundle for "Trusted Certificate Authorities". 6. Repeat for other Virtual Servers. If the BIG-IP appliance accepts non-DOD approved PKI end entity certificates, this is a finding.

## Group: SRG-NET-000362-ALG-000112

**Group ID:** `V-215790`

### Rule: The BIG-IP Core implementation must be configured to protect against known and unknown types of Denial of Service (DoS) attacks by employing rate-based attack prevention behavior analysis when providing content filtering to virtual servers.

**Rule ID:** `SV-215790r831473_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Detection components that use rate-based behavior analysis can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks, which are new attacks for which vendors have not yet developed signatures. Rate-based behavior analysis can detect sophisticated, Distributed DoS (DDoS) attacks by correlating traffic information from multiple network segments or components. This requirement applies to the functionality of the ALG as it pertains to handling communications traffic rather than to the ALG device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with a security policy to protect against or limit the effects of known and unknown types of DoS attacks by employing rate-based attack prevention behavior analysis. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "DoS Protection Profile" is Enabled and "Profile" is set to use locally configured DoS protection Profile. Verify the DoS protection profile that is set for the Virtual Server is set to employ rate-based attack prevention: Navigate to the BIG-IP System manager >> Security >> DoS Protection >> DoS Profiles. Select the DoS Protection Profile set for the Virtual Server. Verify that "Application Security" is Enabled under "General Configuration". Verify that the following are selected for "Prevention Policy" under TPS-base Anomaly in accordance with the organization requirements: "Source IP-Based Client Side Integrity Defense" "URL-Based Client Side Integrity Defense" "Site-wide" Client-Side Integrity Defense" "Source IP-Base Rate Limiting" "URL-Based Rate Limiting" "Site-wide Rate Limiting" Verify the Criteria for each of the selected Prevention Policies is set in accordance with organization requirements. If the BIG-IP Core is not configured to protect against or limit the effects of known and unknown types of DoS attacks by employing rate-based attack prevention behavior analysis, this is a finding.

## Group: SRG-NET-000362-ALG-000120

**Group ID:** `V-215791`

### Rule: The BIG-IP Core implementation must be configured to implement load balancing to limit the effects of known and unknown types of Denial of Service (DoS) attacks to virtual servers.

**Rule ID:** `SV-215791r831474_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Load balancing provides service redundancy; which service redundancy reduces the susceptibility of the ALG to many DoS attacks. The ALG must be configured to prevent or mitigate the impact on network availability and traffic flow of DoS attacks that have occurred or are ongoing. This requirement applies to the functionality of the device as it pertains to handling network traffic. Some types of attacks may be specialized to certain network technologies, functions, or services. For each technology, known and potential DoS attacks must be identified and solutions for each type implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core implements load balancing to limit the effects of known and unknown types of Denial of Service (DoS) attacks. Navigate to the BIG-IP System manager >> System >> Configuration >> Local Traffic >> General. Verify "Reaper High-water Mark" is set to 95 and "Reaper Low-water Mark" is set to 85. If the device does not implement load balancing to limit the effects of known and unknown types of Denial of Service (DoS) attacks, this is a finding.

## Group: SRG-NET-000362-ALG-000126

**Group ID:** `V-215792`

### Rule: The BIG-IP Core implementation must be configured to protect against known types of Denial of Service (DoS) attacks by employing signatures when providing content filtering to virtual servers.

**Rule ID:** `SV-215792r831475_rule`
**Severity:** high

**Description:**
<VulnDiscussion> If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume, type, or protocol usage. Detection components that use signatures can detect known attacks by using known attack signatures. Signatures are usually obtained from and updated by the ALG component vendor. This requirement applies to the communications traffic functionality of the ALG as it pertains to handling communications traffic rather than to the ALG device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured to protect against known types of DoS attacks by employing signatures. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "DoS Protection Profile" is Enabled and "Profile" is set to use locally configured DoS protection Profile. If the BIG-IP Core does not protect against known types of DoS attacks by employing signatures, this is a finding.

## Group: SRG-NET-000362-ALG-000155

**Group ID:** `V-215793`

### Rule: The BIG-IP Core implementation must be configured to protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing pattern recognition pre-processors when providing content filtering to virtual servers.

**Rule ID:** `SV-215793r831476_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks. Detection components that use pattern recognition pre-processors can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks, which are new attacks for which vendors have not yet developed signatures. This requirement applies to the communications traffic functionality of the ALG as it pertains to handling communications traffic, rather than to the ALG device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core protects against or limits the effects of known and unknown types of DoS attacks by employing pattern recognition pre-processors. Verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing pattern recognition pre-processors when providing content filtering to virtual servers. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "DoS Protection Profile" is Enabled and "Profile" is set to use a locally configured DoS protection Profile. Verify the DoS protection profile that is set for the Virtual Server is set to employ pattern recognition pre-processors: Navigate to the BIG-IP System manager >> Security >> DoS Protection >> DoS Profiles. Select the DoS Protection Profile set for the Virtual Server. Verify that "Application Security" is Enabled under "General Configuration". Verify that the following are selected for "Prevention Policy" under TPS-base Anomaly in accordance with the organization requirements: "Source IP-Based Client Side Integrity Defense" "URL-Based Client Side Integrity Defense" "Site-wide" Client-Side Integrity Defense" Verify the Criteria for each of the selected Prevention Policies is set in accordance with organization requirements. If the BIG-IP Core is not configured to protect against or limit the effects of known and unknown types of DoS attacks by employing pattern recognition pre-processors, this is a finding.

## Group: SRG-NET-000364-ALG-000122

**Group ID:** `V-215794`

### Rule: The BIG-IP Core implementation must be configured to only allow incoming communications from authorized sources routed to authorized destinations.

**Rule ID:** `SV-215794r831477_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Access control policies and access control lists implemented on devices that control the flow of network traffic (e.g., application-level firewalls and Web content filters), ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the Internet or CDS) must be kept separate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform packet-filtering intermediary services for virtual servers, this is not applicable. When packet-filtering intermediary services are performed, verify the BIG-IP Core is configured to only allow incoming communications from authorized sources routed to authorized destinations as follows: Verify Virtual Server(s) are configured in the BIG-IP LTM module with policies to only allow incoming communications from authorized sources routed to authorized destinations. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Network Firewall" Enforcement is set to "Policy Rules..." and "Policy" is set to use an AFM policy to only allow incoming communications from authorized sources routed to authorized destinations. If the BIG-IP Core is configured to allow incoming communications from unauthorized sources routed to unauthorized destinations, this is a finding.

## Group: SRG-NET-000380-ALG-000128

**Group ID:** `V-215795`

### Rule: The BIG-IP Core implementation must be configured to handle invalid inputs in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-215795r831478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability of network elements is unpredictable behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This requirement applies to gateways and firewalls that perform content inspection or have higher-layer proxy functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP Core is configured to handle invalid inputs in a predictable and documented manner that reflects organizational and system objectives. This can be demonstrated by the SA sending an invalid input to a virtual server. Provide evidence that the virtual server was able to handle the invalid input and maintain operation. If the BIG-IP Core is not configured to handle invalid inputs in a predictable and documented manner that reflects organizational and system objectives, this is a finding.

## Group: SRG-NET-000390-ALG-000139

**Group ID:** `V-215796`

### Rule: The BIG-IP Core implementation must continuously monitor inbound communications traffic crossing internal security boundaries for unusual or unauthorized activities or conditions.

**Rule ID:** `SV-215796r831479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If inbound communications traffic is not continuously monitored, hostile activity may not be detected and prevented. Output from application and traffic monitoring serves as input to continuous monitoring and incident response programs. Internal monitoring includes the observation of events occurring on the network crossing internal boundaries at managed interfaces such as web content filters. Depending on the type of ALG, organizations can monitor information systems by monitoring audit activities, application access patterns, characteristics of access, content filtering, or unauthorized exporting of information across boundaries. Unusual/unauthorized activities or conditions may include large file transfers, long-time persistent connections, unusual protocols and ports in use, and attempted communications with suspected malicious external addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content filtering as part of the traffic management functionality for virtual servers, this is not applicable. When content filtering is performed as part of the traffic management functionality, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to continuously monitor inbound communications traffic crossing internal security boundaries for unusual or unauthorized activities or conditions. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to use an ASM policy to continuously monitor inbound communications traffic crossing internal security boundaries for unusual or unauthorized activities or conditions. If the BIG-IP Core is not configured to continuously monitor inbound communications traffic for unusual or unauthorized activities or conditions, this is a finding.

## Group: SRG-NET-000401-ALG-000127

**Group ID:** `V-215797`

### Rule: The BIG-IP Core implementation must be configured to check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-215797r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior potentially leading to an application or information system compromise. Invalid input is one of the primary methods employed when attempting to compromise an application. Network devices with the functionality to perform application layer inspection may be leveraged to validate data content of network communications. Checking the valid syntax and semantics of information system inputs (e.g., character set, length, numerical range, and acceptable values) verifies that inputs match specified definitions for format and content. Software typically follows well-defined protocols that use structured messages (i.e., commands or queries) to communicate between software modules or system components. Structured messages can contain raw or unstructured data interspersed with metadata or control information. If network elements use attacker-supplied inputs to construct structured messages without properly encoding such messages, then the attacker could insert malicious commands or special characters that can cause the data to be interpreted as control information or metadata. Consequently, the module or component that receives the tainted output will perform the wrong operations or otherwise interpret the data incorrectly. Pre-screening inputs prior to passing to interpreters prevents the content from being unintentionally interpreted as commands. Input validation helps to ensure accurate and correct inputs and prevent attacks such as cross-site scripting and a variety of injection attacks. This requirement applies to gateways and firewalls that perform content inspection or have higher-layer proxy functionality. Note: A limitation of ~200 policies per cluster currently exists on the BIG-IP Core. If this requirement cannot be met due to this limitation, documentation from the AO is required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not perform content inspection as part of the traffic management functionality for virtual servers, this is not applicable. When content inspection is performed as part of the traffic management functionality, verify the BIG-IP Core is configured to check the validity of all data inputs except those specifically identified by the organization. Verify Virtual Server(s) in the BIG-IP LTM module are configured with an ASM policy to check the validity of all data inputs except those specifically identified by the organization. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Application Security Policy" is Enabled and "Policy" is set to use an ASM policy to check the validity of all data inputs except those specifically identified by the organization. If the BIG-IP Core is not configured to check the validity of all data inputs except those specifically identified by the organization, this is a finding.

## Group: SRG-NET-000510-ALG-000025

**Group ID:** `V-215798`

### Rule: The BIG-IP Core implementation must be configured to implement NIST FIPS-validated cryptography to generate cryptographic hashes when providing encryption traffic to virtual servers.

**Rule ID:** `SV-215798r831480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. This requirement applies only to ALGs that provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC) for virtual servers, this is not applicable. When encryption intermediary services are provided, verify the BIG-IP Core is configured to implement NIST FIPS-validated cryptography to generate cryptographic hashes. Navigate to the BIG-IP System manager >> Local traffic >> Profiles >> SSL >> Client. Verify a profile exists that is FIPS Compliant. Select a FIPS-compliant profile. Select "Advanced" next to "Configuration". Verify "Ciphers" under "Configuration" section is configured to use FIPS-compliant ciphers. Verify applicable virtual servers are configured in the BIG-IP LTM to use a FIPS-compliant client profile: Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Configuration" section, that a FIPS-compliant profile is in the "Selected" area of "SSL Profile (Client)". If the BIG-IP Core is not configured to implement NIST FIPS-validated cryptography to generate cryptographic hashes, this is a finding.

## Group: SRG-NET-000510-ALG-000040

**Group ID:** `V-215799`

### Rule: The BIG-IP Core implementation must be configured to implement NIST FIPS-validated cryptography for digital signatures when providing encrypted traffic to virtual servers.

**Rule ID:** `SV-215799r831481_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. This requirement applies only to ALGs that provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC) for virtual servers, this is not applicable. When encryption intermediary services are provided, verify the BIG-IP Core is configured to implement NIST FIPS-validated cryptography for digital signatures. Navigate to the BIG-IP System manager >> Local traffic >> Profiles >> SSL >> Client. Verify a profile exists that is FIPS Compliant. Select a FIPS-compliant profile. Select "Advanced" next to "Configuration". Verify "Ciphers" under "Configuration" section is configured to use FIPS-compliant ciphers. Verify applicable virtual servers are configured in the BIG-IP LTM to use a FIPS-compliant client profile: Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Configuration" section, that a FIPS-compliant profile is in the "Selected" area of "SSL Profile (Client)". If the BIG-IP Core does not implement NIST FIPS-validated cryptography for digital signatures, this is a finding.

## Group: SRG-NET-000510-ALG-000111

**Group ID:** `V-215800`

### Rule: The BIG-IP Core implementation must be configured to use NIST FIPS-validated cryptography to implement encryption services when providing encrypted traffic to virtual servers.

**Rule ID:** `SV-215800r831482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. This requirement applies only to ALGs that provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC) for virtual servers, this is not applicable. When encryption intermediary services are provided, verify the BIG-IP Core is configured to use NIST FIPS-validated cryptography to implement encryption services. Navigate to the BIG-IP System manager >> Local traffic >> Profiles >> SSL >> Client. Verify a profile exists that is FIPS Compliant. Select a FIPS-compliant profile. Select "Advanced" next to "Configuration". Verify "Ciphers" under "Configuration" section is configured to use FIPS-compliant ciphers. Verify applicable virtual servers are configured in the BIG-IP LTM to use a FIPS-compliant client profile: Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Configuration" section, that a FIPS-compliant profile is in the "Selected" area of "SSL Profile (Client)". If the BIG-IP Core is not configured to use NIST FIPS-validated cryptography to implement encryption services, this is a finding.

## Group: SRG-NET-000512-ALG-000064

**Group ID:** `V-215801`

### Rule: The BIG-IP Core implementation must be configured to inspect for protocol compliance and protocol anomalies in inbound SMTP and Extended SMTP communications traffic to virtual servers.

**Rule ID:** `SV-215801r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as SMTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits that exploit weaknesses of commonly used protocols. Since protocol anomaly analysis examines the application payload for patterns or anomalies, an SMTP proxy must be included in the ALG. This ALG will be configured to inspect inbound SMTP and Extended SMTP communications traffic to detect protocol anomalies such as malformed message and command insertion attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide intermediary/proxy services for SMTP communications traffic for virtual servers, this is not applicable. When intermediary/proxy services for SMTP communication traffic are provided, verify the BIG-IP Core is configured as follows: Verify the BIG-IP LTM module is configured to inspect for protocol compliance and protocol anomalies in inbound SMTP and Extended SMTP communications traffic. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select a Virtual Server that has been configured as an SMTP proxy. Verify that "SMTP Profile" under the "Configuration" section is set to a locally configured SMTP profile. Verify the configuration of the selected SMTP profile: Navigate to the BIG-IP System manager >> Local Traffic >> Profiles >> Services >> SMTP. Select the SMTP profile that was to configure the Virtual Server. Verify that "Protocol Security" is Enabled under the "Settings" section. If the BIG-IP Core does not inspect inbound SMTP and Extended SMTP communications traffic for protocol compliance and protocol anomalies, this is a finding.

## Group: SRG-NET-000512-ALG-000065

**Group ID:** `V-215802`

### Rule: The BIG-IP Core implementation must be configured to inspect for protocol compliance and protocol anomalies in inbound FTP and FTPS communications traffic to virtual servers.

**Rule ID:** `SV-215802r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as FTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits that exploit weaknesses of commonly used protocols. Since protocol anomaly analysis examines the application payload for patterns or anomalies, an FTP proxy must be included in the ALG. This ALG will be configured to inspect inbound FTP and FTPS communications traffic to detect protocol anomalies such as malformed message and command insertion attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide intermediary/proxy services for FTP and FTPS communications traffic for virtual servers, this is not applicable. When intermediary/proxy services for FTP and FTPS communications traffic are provided, verify the BIG-IP Core is configured as follows: Verify the BIG-IP LTM module is configured to inspect for protocol compliance and protocol anomalies in inbound FTP and FTPS communications traffic. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select a Virtual Server that has been configured as an FTP proxy. Verify that "FTP Profile" under the "Configuration" section is set to a locally configured FTP profile. Verify the configuration of the selected FTP profile: Navigate to the BIG-IP System manager >> Local Traffic >> Profiles >> Services >> FTP. Select the FTP profile that was to configure the Virtual Server. Verify that "Protocol Security" is Enabled under the "Settings" section. If the BIG-IP Core does not inspect inbound FTP and FTPS communications traffic for protocol compliance and protocol anomalies, this is a finding.

## Group: SRG-NET-000512-ALG-000066

**Group ID:** `V-215803`

### Rule: The BIG-IP Core implementation must be configured to inspect for protocol compliance and protocol anomalies in inbound HTTP and HTTPS traffic to virtual servers.

**Rule ID:** `SV-215803r557356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as HTTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits that exploit weaknesses of commonly used protocols. Since protocol anomaly analysis examines the application payload for patterns or anomalies, an HTTP proxy must be included in the ALG. This ALG will be configured to inspect inbound HTTP and HTTPS communications traffic to detect protocol anomalies such as malformed message and command insertion attacks. Note that if mutual authentication is enabled, there will be no way to inspect HTTPS traffic with MITM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide intermediary/proxy services for HTTP and HTTPS communications traffic for virtual servers, this is not applicable. When intermediary/proxy services for HTTP and HTTPS communications traffic are provided, verify the BIG-IP Core is configured as follows: Verify the BIG-IP LTM module is configured to inspect for protocol compliance and protocol anomalies in inbound HTTP and HTTPS communications traffic. Navigate to the BIG-IP System manager >> Security >> Protocol Security >> Security Profiles >> HTTP. Verify there is at least one profile for managing HTTP traffic. Select a Profile from the list to verify. Review each of the following tabs to verify the proper criteria are selected and are set to "Alarm" at a minimum: "HTTP Protocol Checks" "Request Checks" "Blocking Page" If the BIG-IP Core does not inspect inbound HTTP and HTTPS communications traffic for protocol compliance and protocol anomalies, this is a finding.

## Group: SRG-NET-000517-ALG-000006

**Group ID:** `V-230214`

### Rule: The BIG-IP Core implementation must automatically terminate a user session for a user connected to virtual servers when organization-defined conditions or trigger events occur that require a session disconnect.

**Rule ID:** `SV-230214r856822_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. This capability is typically reserved for specific system functionality where the system owner, data owner, or organization requires additional trigger events based on specific mission needs. Conditions or trigger events requiring automatic session termination can include, for example, targeted responses to certain types of incidents and time-of-day restrictions on information system use. This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to automatically terminate user sessions for users connected to virtual servers when organization-defined conditions or trigger events occur that require a session disconnect. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section that "Access Policy" has been set to use an APM access policy to automatically terminate a user session when organization-defined conditions or trigger events occur that require a session disconnect. If the BIG-IP Core is not configured to automatically terminate a user session when organization-defined conditions or trigger events occur that require a session disconnect, this is a finding.

## Group: SRG-NET-000519-ALG-000008

**Group ID:** `V-230215`

### Rule: The BIG-IP Core must display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions when providing access to virtual servers.

**Rule ID:** `SV-230215r856824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user cannot explicitly end a session, the session may remain open and be exploited by an attacker; this is referred to as a zombie session. Users need to be aware of whether or not the session has been terminated. Logoff messages for access, for example, can be displayed after authenticated sessions have been terminated. However, for some types of interactive sessions including, for example, remote logon, information systems typically send logoff messages as final messages prior to terminating sessions. This policy only applies to ALGs (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP Core is configured as follows: Verify Virtual Server(s) in the BIG-IP LTM module are configured with an APM policy to display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions when providing access to virtual servers. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select Virtual Servers(s) from the list to verify. Verify under "Access Policy" section, that "Access Policy" has been set to use an APM access policy that displays an explicit logoff message to users indicating the reliable termination of authenticated communications sessions. If the BIG-IP Core is not configured to display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions, this is a finding.

## Group: SRG-NET-000521-ALG-000002

**Group ID:** `V-230216`

### Rule: The BIG-IP Core implementation must be configured to activate a session lock to conceal information previously visible on the display for connections to virtual servers.

**Rule ID:** `SV-230216r561161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. The network element session lock event must include an obfuscation of the display screen so as to prevent other users from reading what was previously displayed. Publicly viewable images can include static or dynamic images, for example, patterns used with screen savers, photographic images, solid colors, a clock, a battery life indicator, or a blank screen, with the additional caveat that none of the images convey sensitive information. This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Core does not provide user access control intermediary services for virtual servers, this is not applicable. When user access control intermediary services are provided, verify the BIG-IP LTM is configured to conceal, via a session lock, information previously visible on the display with a publicly viewable image. Navigate to the BIG-IP System manager >> Local Traffic >> Profiles >> Protocol >> TCP. Select a TCP Profile for user sessions. Verify "Reset On Timeout" is Enabled under the "Settings" section Verify the BIG-IP LTM is configured to use the Protocol Profile. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select appropriate virtual server. Verify "Protocol Profile (Client)" is set to a profile that limits session timeout. If the BIG-IP Core does not conceal, via a session lock, information previously visible on the display with a publicly viewable image, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-260048`

### Rule: The F5 BIG-IP appliance must configure OCSP to ensure revoked credentials are prohibited from establishing an allowed session.

**Rule ID:** `SV-260048r947413_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity, and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS), this is not applicable. If the BIG-IP is performing Client Certificate Authentication: Client SSL Profile: From the BIG-IP GUI: 1. Local Traffic. 2. Profiles. 3. SSL. 4. Client. 5. Click the name of the SSL profile. 6. Under "Client Authentication", verify that "Trusted Certificate Authorities" is configured with a trusted CA certificate or bundle. 7. If the BIG-IP is performing Client Certificate Constrained Delegation, verify an OCSP responder is selected under "Client Certificate Constrained Delegation". 8. Verify the OCSP Responder is configured correctly by going to System >> Certificate Management >> Traffic Certificate Management >> OCSP. If the BIG-IP appliance is not configured to use OCSP to ensure revoked user credentials are prohibited from establishing an allowed session, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-270899`

### Rule: The version of F5 BIG-IP must be a supported version.

**Rule ID:** `SV-270899r1056141_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified period from the availability of the update. The specific period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
BIG-IP versions supported by this STIG (version 15.1x and earlier) are no longer supported by the vendor. If the system is running BIG-IP version 15.1x or earlier, this is a finding.

