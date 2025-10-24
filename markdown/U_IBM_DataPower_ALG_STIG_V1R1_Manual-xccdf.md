# STIG Benchmark: IBM DataPower ALG Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-64979`

### Rule: The DataPower Gateway must enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies.

**Rule ID:** `SV-79469r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Privileged account user log on to default domain >> Administration >> Access >> User Group >> Select the group to be confirmed >> Confirm that the access profiles are configured appropriately for the desired security policy. If the group profile(s) is/are not present, this is a finding Privileged account user log on to default domain >> Administration >> Access >> RBM Settings >> Select "Credential Mapping". If Credential-mapping method is not "Local user group" or "Search LDAP for group name" is off, this is a finding.

## Group: SRG-NET-000018-ALG-000017

**Group ID:** `V-65191`

### Rule: The DataPower Gateway must enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-79681r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, devices) within information systems. Examples of information flow control restrictions include keeping export controlled information from being transmitted in the clear to the Internet or blocking information marked as classified but is being transported to an unapproved destination. ALGs enforce approved authorizations by employing security policy and/or rules that restrict information system services, provide packet filtering capability based on header or protocol information and/or message filtering capability based on data content (e.g., implementing key word searches or using document characteristics).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Privileged Account User logon to the WebGUI >> Open the service to be modified: From the Control Panel, select the type of service to be edited (e.g., Multi-Protocol Gateway) >> The list of available services will be displayed >> Click the name of the service to be edited. Verify configuration of the processing policy: Click the “…” button adjacent to the configured Processing Policy (in the case of a Web Service Proxy, click the “Policy” processing policy tab) >> The processing policy is displayed >> Select the rule to be edited by clicking the “Rule Name” >> Double-click on the “Conditional” action. Confirm the XPath statement for the positive condition (i.e., the condition that, if met, would allow the message to be processed) would result in a “Set Variable” Action being triggered >> Click on the corresponding Set Variable action and confirm that the target URL is correct and that the variable being set is “service/routing-url” >> Click “Done”. Confirm the XPath statement for the negative condition (i.e., the condition that, if met, would result in the message being blocked) would result in a “Call Processing Rule” Action being triggered >> Click on the corresponding Call Processing Rule action and confirm that the service’s error rule is selected >> Click “Done” >> Click “Done” >> Click “Cancel” >> Click “Cancel”. If any of the configuration conditions are not met, this is a finding.

## Group: SRG-NET-000019-ALG-000018

**Group ID:** `V-65193`

### Rule: The DataPower Gateway must restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-79683r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. Blocking or restricting detected harmful or suspicious communications between interconnected networks enforces approved authorizations for controlling the flow of traffic. This requirement applies to the flow of information between the ALG when used as a gateway or boundary device which allows traffic flow between interconnected networks of differing security policies. The ALG is installed and configured such that it restricts or blocks information flows based on guidance in the PPSM regarding restrictions for boundary crossing for ports, protocols and services. Information flow restrictions may be implemented based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. The ALG must be configured with policy filters (e.g., security policy, rules, and/or signatures) that restrict or block information system services; provide a packet-filtering capability based on header information; and/or perform message-filtering based on message content. The policy filters used depends upon the type of application gateway (e.g., web, email, or TLS).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Privileged Account User logon to the WebGUI >> Open the service to be modified: From the Control Panel, select the type of service to be edited (e.g., Multi-Protocol Gateway) >> The list of available services will be displayed >> Click the name of the service to be edited. Verify configuration of the processing policy: Click the “…” button adjacent to the configured Processing Policy (in the case of a Web Service Proxy, click the “Policy” processing policy tab) >> The processing policy is displayed >> Select the rule to be edited by clicking the “Rule Name” >> Double-click on the “Conditional” action. Confirm the XPath statement for the positive condition (i.e., the condition that, if met, would allow the message to be processed) would result in a “Set Variable” Action being triggered >> Click on the corresponding Set Variable action and confirm that the target URL is correct and that the variable being set is “service/routing-url” >> Click “Done”. Confirm the XPath statement for the negative condition (i.e., the condition that, if met, would result in the message being blocked) would result in a “Call Processing Rule” Action being triggered >> Click on the corresponding Call Processing Rule action and confirm that the service’s error rule is selected >> Click “Done” >> Click “Done” >> Click “Cancel” >> Click “Cancel”. If any of the configuration conditions are not met, this is a finding.

## Group: SRG-NET-000041-ALG-000022

**Group ID:** `V-65195`

### Rule: The DataPower Gateway providing user access control intermediary services must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the network.

**Rule ID:** `SV-79685r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the network ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to network elements that have the concept of a user account and have the logon function residing on the network element. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to ALGs (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Privileged user opens browser and navigates to the DataPower logon page. Confirm that the logon page displays the Standard Mandatory DoD Notice and Consent Banner: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the standard banner is not displayed, this is a finding.

## Group: SRG-NET-000042-ALG-000023

**Group ID:** `V-65197`

### Rule: The DataPower Gateway providing user access control intermediary services must retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access.

**Rule ID:** `SV-79687r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the user prior to allowing the user access to the network. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the application usage policy, a click-through banner at application logon is required. The network element must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For an HTTPS application hosted on DataPower to display a landing page, the application designer will need to make that landing page available on the DataPower appliance or remotely accessible on a server. This landing page will be the page that the user sees, and the user will have to acknowledge this page before being redirected to the application/logon. If the banner page does not load when first accessing an application, this is a finding.

## Group: SRG-NET-000043-ALG-000024

**Group ID:** `V-65199`

### Rule: The DataPower Gateway providing user access control intermediary services for publicly accessible applications must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-79689r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible network element ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to network elements that have the concept of a user account and have the logon function residing on the network element. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services off-loaded from the application. Publicly access systems are used in DoD to provide benefit information, pay information, or public services. There may also be self-registration and authorization services provided by these gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For an HTTP application hosted on DataPower to display a landing page, the application designer will need to make that landing page available on the DataPower appliance or remotely accessible on a server. This landing page will be the page that the user sees, and the user will have to acknowledge this page before being redirected to the application/logon. If the banner page does not load when first accessing an application, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-65201`

### Rule: The DataPower Gateway providing intermediary services for remote access communications traffic must use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-79691r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Encryption provides a means to secure the remote connection so as to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For FIPS 140-2 Level 1 Mode: Privileged account user log on to default domain via the WebGUI >> In the search field type "crypto" >> Press "enter". From the search results, click "Cryptographic Mode Status"; the "Cryptographic Mode Status" table is displayed. If the "Target" is not "FIPS 140-2 Level 1", this is a finding. For FIPS 140-2 Level 1 Mode: Privileged account user log on to default domain via the CLI >> Enter "show crypto-engine" >> Confirm "Crypto Accelerator Type" is "hsm2" >> Confirm "Crypto Accelerator Status" is "fully operational" >> Confirm "Crypto Accelerator FIPS 140-2 Level" is "3". If these three settings cannot be confirmed, this is a finding.

## Group: SRG-NET-000062-ALG-000092

**Group ID:** `V-65203`

### Rule: The DataPower Gateway that stores secret or private keys must use FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys.

**Rule ID:** `SV-79693r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder. Private key data associated with software certificates, including those issued to an ALG, is required to be generated and protected in at least a FIPS 140-2 Level 1 validated cryptographic module.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For FIPS 140-2 Level 1 Mode: Privileged account user log on to default domain via the WebGUI >> In the search field type "crypto" >> Press "enter". From the search results, click "Cryptographic Mode Status"; the "Cryptographic Mode Status" table is displayed. If the "Target" is not "FIPS 140-2 Level 1", this is a finding. For FIPS 140-2 Level 1 Mode: Privileged account user log on to default domain via the CLI >> Enter "show crypto-engine" >> Confirm "Crypto Accelerator Type" is "hsm2" >> Confirm "Crypto Accelerator Status" is "fully operational" >> Confirm "Crypto Accelerator FIPS 140-2 Level" is "3". If these three settings cannot be confirmed, this is a finding.

## Group: SRG-NET-000062-ALG-000150

**Group ID:** `V-65205`

### Rule: The DataPower Gateway that provides intermediary services for TLS must be configured to comply with the required TLS settings in NIST SP 800-52.

**Rule ID:** `SV-79695r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SP 800-52 provides guidance on using the most secure version and configuration of the TLS/SSL protocol. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks which exploit vulnerabilities in this protocol. This requirement applies to TLS gateways (also known as SSL gateways) and is not applicable to VPN devices. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol thus are in scope for this requirement. NIS SP 800-52 provides guidance. SP 800-52 sets TLS version 1.1 as a minimum version, thus all versions of SSL are not allowed (including for client negotiation) either on DoD-only or on public facing servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the search field, enter "SSL Server Profile" >> Select "SSL Server Profile" from the results >> Click the name of the SSL Server Profile object to be inspected >> Confirm that the TLS 1.1 and TLS 1.2 protocol options are checked. If they are not checked, this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-65207`

### Rule: The DataPower Gateway providing intermediary services for remote access communications traffic must use NIST FIPS-validated cryptography to protect the integrity of remote access sessions.

**Rule ID:** `SV-79697r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For FIPS 140-2 Level 1 Mode: Privileged account user log on to default domain via the WebGUI >> In the search field type "crypto" >> Press "enter". From the search results, click "Cryptographic Mode Status"; the "Cryptographic Mode Status" table is displayed. If the "Target" is not "FIPS 140-2 Level 1", this is a finding. For FIPS 140-2 Level 1 Mode: Privileged account user log on to default domain via the CLI >> Enter "show crypto-engine" >> Confirm "Crypto Accelerator Type" is "hsm2" >> Confirm "Crypto Accelerator Status" is "fully operational" >> Confirm "Crypto Accelerator FIPS 140-2 Level" is "3". If these three settings cannot be confirmed, this is a finding.

## Group: SRG-NET-000088-ALG-000054

**Group ID:** `V-65209`

### Rule: The DataPower Gateway must send an alert to, at a minimum, the ISSO and SCA when an audit processing failure occurs.

**Rule ID:** `SV-79699r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Possible audit processing failures also include the inability of ALG to write to the central audit log. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations, (i.e., all audit data storage repositories combined), or both. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Administration >> Miscellaneous >> "Manage Log Targets" >> Click the appropriate log target (e.g., "logTargetSystemResources" >> Click the "Event Filters" tab >> Confirm subscriptions to the following event codes: 0x00330034, 0x01a40001, 0x01a30002, 0x01a30003, 0x01a40005, 0x01a30006, 0x01a30014, 0x01a30015, 0x01a30017. If any of these codes are not subscribed to, this is a finding.

## Group: SRG-NET-000098-ALG-000056

**Group ID:** `V-65211`

### Rule: The DataPower Gateway must protect audit information from unauthorized read access.

**Rule ID:** `SV-79701r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or to simply identify an improperly configured network element. Thus, it is imperative that the collected log data from the various network elements, as well as the auditing tools, be secured and can only be accessed by authorized personnel. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Login page >> Enter non-admin user id and password, select Default for domain >> Click Login. If non-admin user can log on, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-65213`

### Rule: The DataPower Gateway must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-79703r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The ALG is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of authorized applications, services, and protocols that has been added to the PPSM database. Privileged Account User logon to the WebGUI >> Log on to the Default domain >> Click Status >> Main >> Active Services >> Click Show All Domains. If any of the Active Services allows traffic that is prohibited by the PPSM CAL, this is a finding.

## Group: SRG-NET-000138-ALG-000063

**Group ID:** `V-65215`

### Rule: The DataPower Gateway providing user authentication intermediary services must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-79705r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication. 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement applies to ALGs that provide user proxy services, including identification and authentication. This service must use the site's directory service (e.g., Active Directory). Directory services must not be installed onto the gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the appliance's WebGUI, navigate to DataPower Gateway's Configure AAA Policy (authentication, authorization, audit) at Objects >> XML Processing >> AAA Policy. Open the applicable AAA policy. On the Identity extraction tab, confirm that the appropriate methods are checked and appropriate processing option specified. On the Authentication tab, confirm that all parameters associated with the authentication method (e.g., LDAP) are correctly specified. If these items are not configured, this is a finding.

## Group: SRG-NET-000138-ALG-000088

**Group ID:** `V-65217`

### Rule: The DataPower Gateway providing user access control intermediary services must be configured with a pre-established trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or AAA server) which validate user account access authorizations and privileges.

**Rule ID:** `SV-79707r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User account and privilege validation must be centralized in order to prevent unauthorized access using changed or revoked privileges. ALGs can implement functions such as traffic filtering, authentication, access, and authorization functions based on computer and user privileges. However, the directory service (e.g., Active Directory or LDAP) must not be installed on the ALG, particularly if the gateway resides on the untrusted zone of the Enclave.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the appliance's WebGUI, navigate to DataPower Gateway's Configure AAA Policy (authentication, authorization, audit) at Objects >> XML Processing >> AAA Policy. On the Resource extraction tab, confirm that the correct resource information categories are checked. If these items are not configured, this is a finding.

## Group: SRG-NET-000138-ALG-000089

**Group ID:** `V-65219`

### Rule: The DataPower Gateway providing user authentication intermediary services must restrict user authentication traffic to specific authentication server(s).

**Rule ID:** `SV-79709r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User authentication can be used as part of the policy filtering rule sets. Some URLs or network resources can be restricted to authenticated users only. Users are prompted by the application or browser for credentials. Authentication service may be provided by the ALG as an intermediary for the application; however, the authentication credential must be stored in the site's directory services server. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., proxy capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a DataPower service processing policy includes an appropriately configured AAA policy action. For example, for a Multi-Protocol Gateway service, this may be accomplished as follows: On the main Control Panel of the DataPower WebGUI, click on Multi-Protocol Gateway >> Open the existing target Multi-Protocol Gateway instance >> Click on the "..." to the right of the Multi-Protocol Gateway Policy dropdown list box to open its processing policy. Confirm that the rule in the processing policy includes an AAA action. Double click on the AAA action (on the rule line) >> Click on the "..." to the right of the selected AAA Policy to open it >> Confirm that the values configured on the Main, Identity extraction, Authentication (specific authentication server specified), and Resource extraction tabs are correct. If any of the configuration conditions are not met, this is a finding.

## Group: SRG-NET-000140-ALG-000094

**Group ID:** `V-65221`

### Rule: The DataPower Gateway providing user authentication intermediary services must use multifactor authentication for network access to non-privileged accounts.

**Rule ID:** `SV-79711r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1) Something you know (e.g., password/PIN), 2) Something you have (e.g., cryptographic, identification device, token), and 3) Something you are (e.g., biometric) Non-privileged accounts are not authorized access to the network element regardless of access method. Network access is any access to an application by a user (or process acting on behalf of a user) where said access is obtained through a network connection. Authenticating with a PKI credential and entering the associated PIN is an example of multifactor authentication. This requirement applies to ALGs that provide user authentication intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Scenario 1: Prerequisites: 1. The user’s identity/attributes are stored in LDAP, including Distinguished Name (DN) and DataPower group membership (users can only be a member of one group). 2. The user has a device that has access to their digital certificate (e.g., via a CAC/PIV card reader connected to a laptop/desktop computer). The user opens a browser and navigates to the URL for the DataPower WebGUI. The user provides their assigned ID and password, which are authenticated by DataPower. If the user does not gain access to the DataPower appliance Control Panel screen, this is a finding. Scenario 2: Prerequisites: 1. The user’s identity/attributes are stored in LDAP, including Distinguished Name (DN) and DataPower group membership (users can only be a member of one group). 2. The user has a device that has access to a different user’s digital certificate (e.g., via a CAC/PIV card reader connected to a laptop/desktop computer). The user opens a browser and navigates to the URL for the DataPower WebGUI. The user provides their assigned ID and password, which are authenticated by DataPower. If the user gains access to the DataPower appliance Control Panel screen, this is a finding. Scenario 3: Prerequisites: 1. The user’s identity/attributes are stored in LDAP, including Distinguished Name (DN). In this case, the DataPower group membership is either not defined, or a group name is specified for which there is no corresponding group definition on the DataPower appliance. 2. The user has a device that has access to a different user’s digital certificate (e.g., via a CAC/PIV card reader connected to a laptop/desktop computer). The user opens a browser and navigates to the URL for the DataPower WebGUI. The user provides their assigned ID and password, which are authenticated by DataPower. If the user gains access to the DataPower appliance Control Panel screen, this is a finding.

## Group: SRG-NET-000147-ALG-000095

**Group ID:** `V-65223`

### Rule: The DataPower Gateway providing user authentication intermediary services must implement replay-resistant authentication mechanisms for network access to non-privileged accounts.

**Rule ID:** `SV-79713r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A non-privileged account is any account with the authorizations of a non-privileged user. Privileged roles are organization-defined roles assigned to individuals that allow those individuals to perform certain security-relevant functions that ordinary users are not authorized to perform. Security relevant roles include key management, account management, network and system administration, database administration, and web administration. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one time use) or challenges (e.g., TLS). Additional techniques include time-synchronous or challenge-response one-time authenticators. This requirement applies to ALGs that provide user authentication intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that DataPower requires mutual authentication when establishing TLS connections to remote hosts, click on the Multi-Protocol Gateway or Web Service Proxy icons on the Control Panel (the initial screen). Click on the configured available service(s) to view its configuration. For Multi-Protocol Gateway, scroll down to view User Agent Settings >> Verify that the SSL Configuration is set to Client Profile or Proxy Profile >> Click the ellipses (...) button to view the configuration of the Client Profile or Proxy Profile. For SSL Client Profile, verify that only TLS v1.1 and v1.2 are enabled. For SSL Client Profile, verify that a validation credential is configured. For SSL Proxy Profile, click the ellipses (…) button to view the configuration of the Crypto Profile >> Verify that all Options are disabled except TLS version 1.1 and 1.2 >> Verify that a Validation Credential is configured. To verify that DataPower requires mutual authentication when accepting TLS connections from remote hosts, click on the Multi-Protocol Gateway or Web Service Proxy icons on the Control Panel (the initial screen) >> Click on the configured available service(s) to view its configuration. For Multi-Protocol Gateway, scroll down to view the Front Side Protocol settings >> Select the current HTTPS Front Side Handler from the dropdown list >> Click “…” to view configuration of the Handler >> Click “...” to view the configuration of the SSL Server Profile or SSL Proxy Profile. For SSL Server Profile, verify that only TLS v1.1 and v1.2 are enabled. For SSL Server Profile, verify that a validation credential is configured. For SSL Proxy Profile, click “…” to view the configuration of the Crypto Profile >> Verify that the Ciphers are only HIGH >> Verify that all Options are disabled except TLS version 1.1 and 1.2 >> Verify that Always Request Client Authentication is set to On >> Verify that a Validation Credential is configured. If they are not, this is a finding. Use the WebGUI Control panel to select and open a specific service, then open its processing policy. Confirm that a rule with a filter action exists and that the method is "Replay Filter". If they are not, this is a finding. To confirm interface isolation has been correctly maintained, use the WebGUI at Network >> Interface >> Network Settings. Confirm that Relax interface Isolation is Off. Confirm Disable interface isolation is Off. If they are not, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-65225`

### Rule: The DataPower Gateway that provides intermediary services for TLS must validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-79715r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the WebGUI, go to Objects >> Crypto Configuration >> SSL Client Profile and SSL Server Profile. Confirm that each Profile's parameters are set correctly (as defined in the Fix column) and that each profile is using a correctly defined Crypto Validation Credentials (as defined in the Fix column). If they are not correctly defined, this is a finding.

## Group: SRG-NET-000166-ALG-000101

**Group ID:** `V-65227`

### Rule: The DataPower Gateway providing PKI-based user authentication intermediary services must map authenticated identities to the user account.

**Rule ID:** `SV-79717r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authorization for access to any network element requires an approved and assigned individual account identifier. To ensure only the assigned individual is using the account, the account must be bound to a user certificate when PKI-based authentication is implemented. This requirement applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a DataPower service processing policy includes an appropriately configured AAA policy action. For example, for a Multi-Protocol Gateway service, this may be accomplished as follows: On the main Control Panel of the DataPower WebGUI, click on Multi-Protocol Gateway >> Open the existing target Multi-Protocol Gateway instance >> Click on the "..." to the right of the Multi-Protocol Gateway Policy dropdown list box to open its processing policy >> Confirm that the rule in the processing policy includes an AAA action >> Double click on the AAA action (on the rule line) >> Click on the "..." to the right of the selected AAA Policy to open it >> Review the values configured on the Main, Identity extraction, Authentication, Resource extraction, and Credential mapping tabs If any of the configuration conditions are not met, this is a finding.

## Group: SRG-NET-000169-ALG-000102

**Group ID:** `V-65229`

### Rule: The DataPower Gateway providing user authentication intermediary services must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-79719r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication enables anyone to gain access to the network or possibly a network element that provides opportunity for intruders to compromise resources within the network infrastructure. By identifying and authenticating non-organizational users, their access to network resources can be restricted accordingly. Non-organizational users will be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access. Authorization requires an individual account identifier that has been approved, assigned, and configured on an authentication server. Authentication of user identities is accomplished through the use of passwords, tokens, biometrics, or in the case of multifactor authentication, some combination thereof. This control applies to application layer gateways that provide content filtering and proxy services on network segments (e.g., DMZ) that allow access by non-organizational users. This requirement focuses on authentication requests to the proxied application for access to destination resources and policy filtering decisions rather than administrator and management functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a DataPower service processing policy includes an appropriately configured AAA policy action. For example, for a Multi-Protocol Gateway service, this may be accomplished as follows: On the main Control Panel of the DataPower WebGUI, click on Multi-Protocol Gateway >> Open the existing target Multi-Protocol Gateway instance >> Click on the "..." to the right of the Multi-Protocol Gateway Policy dropdown list box to open its processing policy >> Confirm that the rule in the processing policy includes an AAA action >> Double-click on the AAA action (on the rule line) >> Click on the "..." to the right of the selected AAA Policy to open it >> Confirm that the values configured on the Main, Identity extraction, Authentication, and Resource extraction tabs are correct >> If any of the configuration conditions are not met, this is a finding.

## Group: SRG-NET-000192-ALG-000121

**Group ID:** `V-65231`

### Rule: The DataPower Gateway providing content filtering must not have a front side handler configured facing an internal network.

**Rule ID:** `SV-79721r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS attacks can take multiple forms but have the common objective of overloading or blocking a network or host to deny or seriously degrade performance. If the network does not provide safeguards against DoS attack, network resources will be unavailable to users. Installation of an ALG at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. The ALG must include protection against DoS attacks that originate from inside the enclave which can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. These attacks can be simple "floods" of traffic to saturate circuits or devices, malware that consumes CPU and memory on a device or causes it to crash, or a configuration issue that disables or impairs the proper function of a device. For example, an accidental or deliberate misconfiguration of a routing table can misdirect traffic for multiple networks. To comply with this requirement, the ALG must monitor outbound traffic for indications of known and unknown DoS attacks. Audit log capacity management along with techniques which prevent the logging of redundant information during an attack also guard against DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the initial Web interface screen (the Control Panel), select Objects >> Protocol Handlers >>HTTPS Front Side Handler. Click on each of the Handlers in the list that appears >> Click the Advanced tab of the Handler configuration >> Verify that there is an Access Control List selected >> Click the ellipses (…) button beside the list. On the Access Control List page, click the Entry tab >> Verify that the network segments representing internal networks are denied. If these items are not configured, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-65233`

### Rule: The DataPower Gateway must protect the authenticity of communications sessions.

**Rule ID:** `SV-79723r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. This requirement focuses on communications protection for the application session rather than for the network packet and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of mutual authentication (two-way/bidirectional).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the WebGUI at Objects >> Crypto Configuration >> SSL Client Profile and SSL Server Profile. Select the profiles that are configured for the application session requiring mutual authentication. Confirm that the correct protocol and cipher parameters are set and that the correct identification and validation credentials are specified. If these items are not configured, this is a finding.

## Group: SRG-NET-000231-ALG-000114

**Group ID:** `V-65235`

### Rule: The DataPower Gateway must invalidate session identifiers upon user logout or other session termination.

**Rule ID:** `SV-79725r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Captured sessions can be reused in "replay" attacks. This requirement limits the ability of adversaries from capturing and continuing to employ previously valid session IDs. Session IDs are tokens generated by web applications to uniquely identify an application user's session. Unique session identifiers or IDs are the opposite of sequentially generated session IDs, which can be easily guessed by an attacker. Unique session IDs help to reduce predictability of said identifiers. When a user logs out, or when any other session termination event occurs, the network element must terminate the user session to minimize the potential for an attacker to hijack that particular user session. ALGs act as an intermediary for application; therefore, session control is part of the function provided. This requirement focuses on communications protection at the application session, versus network packet level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the web interface for DataPower device management, verify that the DataPower Gateway Cryptographic Mode is Set to FIPS 140-2 Level 1; Status >> Crypto >> Cryptographic Mode Status. Then, verify that the session identifiers (TIDs) in the System Log are random; Status >> View Logs >> Systems Logs. If the device is not set to FIPS 140-2 Level 1, this is a finding.

## Group: SRG-NET-000233-ALG-000115

**Group ID:** `V-65237`

### Rule: The DataPower Gateway must recognize only system-generated session identifiers.

**Rule ID:** `SV-79727r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network elements (depending on function) utilize sessions and session identifiers to control application behavior and user access. If an attacker can guess the session identifier, or can inject or manually insert session information, the valid user's application session can be compromised. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. This requirement focuses on communications protection for the application session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the web interface for DataPower device management, verify that the DataPower Gateway Cryptographic Mode is Set to FIPS 140-2 Level 1; Status >> Crypto >> Cryptographic Mode Status Then, verify that the session identifiers (TIDs) in the System Log are random; Status >> View Logs >> Systems Logs. If these items are not configured, this is a finding.

## Group: SRG-NET-000236-ALG-000119

**Group ID:** `V-65239`

### Rule: In the event of a system failure of the DataPower Gateway function, the DataPower Gateway must save diagnostic information, log system messages, and load the most current security policies, rules, and signatures when restarted.

**Rule ID:** `SV-79729r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure in a secure state can address safety or security in accordance with the mission needs of the organization. Failure to a secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving state information helps to facilitate the restart of the ALG application and a return to the operational mode with less disruption. This requirement applies to a failure of the ALG function rather than the device or operating system as a whole which is addressed in the Network Device Management SRG. Since it is usually not possible to test this capability in a production environment, systems should either be validated in a testing environment or prior to installation. This requirement is usually a function of the design of the IDPS component. Compliance can be verified by acceptance/validation processes or vendor attestation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all desired optional failure notification functions are configured by going to the WebGUI at Administration >> Device >> Failure Notification. If this is not configured, this is a finding.

## Group: SRG-NET-000273-ALG-000129

**Group ID:** `V-65241`

### Rule: The DataPower Gateway must have ICMP responses disabled on all interfaces facing untrusted networks.

**Rule ID:** `SV-79731r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing too much information in error messages risks compromising the data and security of the application and system. Organizations carefully consider the structure/content of error messages. The required information within error messages will vary based on the protocol and error condition. Information that could be exploited by adversaries includes, for example, ICMP messages that reveal the use of firewalls or access-control lists. The DataPower appliance, by default, will respond to ICMP pings, Info requests, and Address Mask queries. This must be disabled on any interface facing an untrusted network or network with a lower security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View each interface that is connected to a network that is less trusted or untrusted. In the DataPower web interface, navigate to Ethernet interface >> Network settings >> Internet Control Message Protocol (ICMP) Disable. If the Administrative State is not "Disable", this is a finding.

## Group: SRG-NET-000318-ALG-000014

**Group ID:** `V-65243`

### Rule: To protect against data mining, the DataPower Gateway providing content filtering must prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-79733r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. Compliance requires the ALG to have the capability to prevent code injections. Examples include a Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Processing Rule” >> Processing rule. If “Rule Action” does not contain a “Filter” action, this is a finding.

## Group: SRG-NET-000318-ALG-000151

**Group ID:** `V-65245`

### Rule: To protect against data mining, the DataPower Gateway providing content filtering must prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-79735r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. Compliance requires the ALG to have the capability to prevent code injections. Examples include a Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Processing Rule” >> Processing rule. If “Rule Action” does not contain a “Filter” action, this is a finding.

## Group: SRG-NET-000318-ALG-000152

**Group ID:** `V-65247`

### Rule: To protect against data mining, the DataPower Gateway providing content filtering must prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-79737r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. Compliance requires the ALG to have the capability to prevent SQL code injections. Examples include a Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Processing Rule” >> Processing rule. If “Rule Action” does not contain a “Filter” action, this is a finding.

## Group: SRG-NET-000319-ALG-000015

**Group ID:** `V-65249`

### Rule: To protect against data mining, the DataPower Gateway providing content filtering must detect code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-79739r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. ALGs with anomaly detection must be configured to protect against unauthorized code injections. These devices must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses. Examples include a Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Processing Rule” >> Processing rule. If “Rule Action” does not contain a “Filter” action, this is a finding.

## Group: SRG-NET-000319-ALG-000020

**Group ID:** `V-65251`

### Rule: To protect against data mining, the DataPower Gateway providing content filtering must detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-79741r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational databases may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. ALGs with anomaly detection must be configured to protect against unauthorized data mining attacks. These devices must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses. Examples include a Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Processing Rule” >> Processing rule. If “Rule Action” does not contain a “Filter” action, this is a finding.

## Group: SRG-NET-000319-ALG-000153

**Group ID:** `V-65253`

### Rule: To protect against data mining, the DataPower Gateway providing content filtering as part of its intermediary services must detect code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-79743r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks launched against organizational applications may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. ALGs with anomaly detection must be configured to protect against unauthorized code injections. These devices must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses. Examples include a Web Application Firewalls (WAFs) or database application gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Processing Rule” >> Processing rule. If “Rule Action” does not contain a “Filter” action, this is a finding.

## Group: SRG-NET-000331-ALG-000041

**Group ID:** `V-65255`

### Rule: The DataPower Gateway providing user access control intermediary services must provide the capability for authorized users to select a user session to capture or view.

**Rule ID:** `SV-79745r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to select a user session to capture or view, investigations into suspicious or harmful events would be hampered by the volume of information captured. The intent of this requirement is to ensure the capability to select specific sessions to capture is available in order to support general auditing/incident investigation, or to validate suspected misuse by a specific user. Examples of session events that may be captured include, port mirroring, tracking websites visited, and recording information and/or file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Log Target” >> Log target >> Event Subscription tab. If “audit” is not listed under Event Category, this is a finding. (Note: If the only Log Target available is “default-log”, this is a finding.)

## Group: SRG-NET-000333-ALG-000049

**Group ID:** `V-65257`

### Rule: The DataPower Gateway must be configured to support centralized management and configuration.

**Rule ID:** `SV-79747r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Network components requiring centralized audit log management must have the capability to support centralized management. The DoD requires centralized management of all network component audit record content. This requirement does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In default domain >> Search Bar “SNMP Settings”. If SNMP object is disabled, this is a finding.

## Group: SRG-NET-000334-ALG-000050

**Group ID:** `V-65259`

### Rule: The DataPower Gateway must off-load audit records onto a centralized log server.

**Rule ID:** `SV-79749r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Log Target” >> Log target >> Event Subscription tab. If “audit” is not listed under Event Category, this is a finding. If “Rule Action” does not contain a “Filter” action, this is a finding.

## Group: SRG-NET-000335-ALG-000053

**Group ID:** `V-65261`

### Rule: The DataPower Gateway must provide an immediate real-time alert to, at a minimum, the SCA and ISSO, of all audit failure events where the detection and/or prevention function is unable to write events to either local storage or the centralized server.

**Rule ID:** `SV-79751r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less). This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine configuration of Log targets (type “Log Target” in navigation search box) to verify a target that delivers Critical messages. If no log targets are configured, this is a finding.

## Group: SRG-NET-000344-ALG-000098

**Group ID:** `V-65263`

### Rule: The DataPower Gateway must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-79753r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the cached authenticator information is out of date, the validity of the authentication information may be questionable. This requirement applies to all ALGs which may cache user authenticators for use throughout a session. This requirement also applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “AAA Policy” >> Select AAA Policy. If no AAA Policy is present, this is a finding. Search Bar “AAA Policy” >> Select AAA Policy >> AAA policy >> Authentication. If cache authentication results “Disabled”, this is a finding. Search Bar “Processing Policy” >> processing policy >> Policy Maps tab processing rule >> Rule Action. If no AAA action exists, this is a finding.

## Group: SRG-NET-000345-ALG-000099

**Group ID:** `V-65265`

### Rule: The DataPower Gateway providing user authentication intermediary services using PKI-based user authentication must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network.

**Rule ID:** `SV-79755r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without configuring a local cache of revocation data, there is the potential to allow access to users who are no longer authorized (users with revoked certificates). The intent of this requirement is to require support for a secondary certificate validation method using a locally cached revocation data, such as Certificate Revocation List (CRL), in case access to OCSP (required by CCI-000185) is not available. Based on a risk assessment, an alternate mitigation is to configure the system to deny access when revocation data is unavailable. This requirement applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “AAA Policy” >> Select AAA Policy. If no AAA Policy is present, this is a finding. Search Bar “AAA Policy” >> Select AAA Policy >> AAA policy >> Authentication. If cache authentication results “Disabled”, this is a finding. Search Bar “Processing Policy” >> processing policy >> Policy Maps tab processing rule >> Rule Action. If no AAA action exists, this is a finding.

## Group: SRG-NET-000349-ALG-000106

**Group ID:** `V-65267`

### Rule: The DataPower Gateway providing user authentication intermediary services must conform to FICAM-issued profiles.

**Rule ID:** `SV-79757r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without conforming to Federal Identity, Credential, and Access Management (FICAM)-issued profiles, the information system may not be interoperable with FICAM-authentication protocols, such as SAML 2.0 and OpenID 2.0. Use of FICAM-issued profiles addresses open identity management standards. This requirement only applies to components where this is specific to the function of the device or has the concept of a non-organizational user, (e.g., ALG capability that is the front end for an application in a DMZ).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar "AAA Policy" >> Select AAA Policy >> Identity Extraction "Name from SAML Authentication assertion" >> Authentication >> Method "Accept SAML assertion with valid signature". If no AAA Policy is present, this is a finding.

## Group: SRG-NET-000355-ALG-000117

**Group ID:** `V-65269`

### Rule: The DataPower Gateway providing user authentication intermediary services using PKI-based user authentication must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of protected sessions.

**Rule ID:** `SV-79759r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at http://iase.disa.mil/pki-pke/interoperability. DoD-approved PKI CAs may include Category I, II, and III certificates. Category I DoD-Approved External PKIs are PIV issuers. Category II DoD-Approved External PKIs are Non-Federal Agency PKIs cross certified with the Federal Bridge Certification Authority (FBCA). Category III DoD-Approved External PKIs are Foreign, Allied, or Coalition Partner PKIs. Deploying the ALG with TLS enabled will require the installation of DoD and/or DoD-Approved CA certificates in the trusted root certificate store of each proxy to be used for TLS traffic. This requirement focuses on communications protection for the application session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type “Validation Credential” in the nav search. Verify that ValCred has only DoD certs. If ValCred does not contain DoD certs, this is a finding. Check config of active SSL Proxy Profiles to ensure use of ValCred. If SSL Proxy does not contain a ValCred, this is a finding.

## Group: SRG-NET-000362-ALG-000112

**Group ID:** `V-65271`

### Rule: The DataPower Gateway providing content filtering must protect against known and unknown types of Denial of Service (DoS) attacks by employing rate-based attack prevention behavior analysis (traffic thresholds).

**Rule ID:** `SV-79761r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Detection components that use rate-based behavior analysis can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. Rate-based behavior analysis can detect sophisticated, Distributed DoS (DDoS) attacks by correlating traffic information from multiple network segments or components. This requirement applies to the communications traffic functionality of the ALG as it pertains to handling communications traffic, rather than to the ALG device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type “Message Count Monitor” in nav search. Verify that Count Monitor exists. Check configuration of any active service to see that count monitor is in effect. If no monitor is configured for each active service, this is a finding.

## Group: SRG-NET-000362-ALG-000120

**Group ID:** `V-65273`

### Rule: The DataPower Gateway must implement load balancing to limit the effects of known and unknown types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-79763r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Load balancing provides service redundancy; which service redundancy reduces the susceptibility of the ALG to many DoS attacks. The ALG must be configured to prevent or mitigate the impact on network availability and traffic flow of DoS attacks that have occurred or are ongoing. This requirement applies to the network traffic functionality of the device as it pertains to handling network traffic. Some types of attacks may be specialized to certain network technologies, functions, or services. For each technology, known and potential DoS attacks must be identified and solutions for each type implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type “Load Balancer Group” in nav search. Check the configuration of all active services and verify that the XML Manager used by the service has an active Load Balancer Group. If no Load Balancer group is present, this is a finding.

## Group: SRG-NET-000362-ALG-000126

**Group ID:** `V-65275`

### Rule: The DataPower Gateway providing content filtering must protect against known types of Denial of Service (DoS) attacks by employing signatures.

**Rule ID:** `SV-79765r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume, type, or protocol usage. Detection components that use signatures can detect known attacks by using known attack signatures. Signatures are usually obtained from and updated by the ALG component vendor. This requirement applies to the communications traffic functionality of the ALG as it pertains to handling communications traffic, rather than to the ALG device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
XML DoS Single message attacks: Jumbo Payload, Recursion, Mega Tags, Coercive parsing, Public key; Multiple message: XML flood, Resource hijack. WebGUI Services >> XML Firewall >> Edit XML Firewall XML, Threat Protection tab. AAA DoS Protection against DoS flooding attacks. WebGUI Objects >> XML Processing >> AAA Policy, Main tab. PKCS #7 Document DoS signature-limit protection. WebGUI Objects >> XML Processing >> Processing Action, select Crypto Binary action type. Service level monitor (SLM) policy. WebGUI Objects >> Monitoring >> SLM Policy. If these items are not configured, this is a finding.

## Group: SRG-NET-000362-ALG-000155

**Group ID:** `V-65277`

### Rule: The DataPower Gateway providing content filtering must protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing pattern recognition pre-processors.

**Rule ID:** `SV-79767r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks. Detection components that use pattern recognition pre-processors can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. This requirement applies to the communications traffic functionality of the ALG as it pertains to handling communications traffic, rather than to the ALG device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
XML DoS Single message attacks: Jumbo Payload, Recursion, Mega Tags, Coercive parsing, Public key; Multiple message: XML flood, Resource hijack. WebGUI Services >> XML Firewall >> Edit XML Firewall XML, Threat Protection tab. AAA DoS Protection against DoS flooding attacks. WebGUI Objects >> XML Processing >> AAA Policy, Main tab. PKCS #7 Document DoS signature-limit protection. WebGUI Objects >> XML Processing >> Processing Action, select Crypto Binary action type. Service level monitor (SLM) policy. WebGUI Objects >> Monitoring >> SLM Policy. If these items are not configured, this is a finding.

## Group: SRG-NET-000364-ALG-000122

**Group ID:** `V-65279`

### Rule: The DataPower Gateway must only allow incoming communications from organization-defined authorized sources routed to organization-defined authorized destinations.

**Rule ID:** `SV-79769r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Access control policies and access control lists implemented on devices that control the flow of network traffic (e.g., application level firewalls and Web content filters), ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the Internet or CDS) must be kept separate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type “Access Control List” in nav search. Verify that Access Control Lists are used for all services. If Access Control lists are not used, this is a finding.

## Group: SRG-NET-000380-ALG-000128

**Group ID:** `V-65281`

### Rule: The DataPower Gateway must behave in a predictable and documented manner that reflects organizational and system objectives when invalid inputs are received.

**Rule ID:** `SV-79771r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability of network elements is unpredictable behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This requirement applies to gateways and firewalls that perform content inspection or have higher-layer proxy functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the WebGUI, go to Objects >> XML Processing >> Matching Rule to verify there is a rule that defines the expected form of the incoming message. If there is no match, the message will be discarded. Go to Objects >> XML Processing >> Processing Rule to verify there are error rules that provide appropriate system responses to invalid and unexpected inputs. If no error rules discarding invalid messages are configured, this is a finding.

## Group: SRG-NET-000383-ALG-000135

**Group ID:** `V-65283`

### Rule: The DataPower Gateway providing content filtering must be configured to integrate with a system-wide intrusion detection system.

**Rule ID:** `SV-79773r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without coordinated reporting between separate devices, it is not possible to identify the true scale and possible target of an attack. Integration of the ALG with a system-wide intrusion detection system supports continuous monitoring and incident response programs. This requirement applies to monitoring at internal boundaries using TLS gateways, web content filters, email gateways, and other types of ALGs. ALGs can work as part of the network monitoring capabilities to off-load inspection functions from the external boundary IDPS by performing more granular content inspection of protocols at the upper layers of the OSI reference model.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the DataPower web interface, navigate to Administration >> Access >> SNMP Settings. Verify that Trap Event Subscriptions are associated with intrusion detection. Verify that Trap and Notification Targets includes an approved SNMP server that generates alerts that will be forwarded to the system-wide intrusion detection system. If no trap event subscriptions are configured on no SNMP server configured as a target, this is a finding.

## Group: SRG-NET-000385-ALG-000137

**Group ID:** `V-65285`

### Rule: The DataPower Gateway providing content filtering must generate a log record when unauthorized network services are detected.

**Rule ID:** `SV-79775r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Examples of network services include service-oriented architectures (SOAs), cloud-based services (e.g., infrastructure as a service, platform as a service, or software as a service), cross-domain, Voice Over Internet Protocol, Instant Messaging, auto-execute, and file sharing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the WebGUI, go to Network >> Management >> Web Management Service. Verify that the "WS-Management endpoint" checkbox is checked and that an IP and port for the WS-Management endpoint to connect to is configured. If the WS-Management endpoint is not enabled (checked) or not configured, this is a finding.

## Group: SRG-NET-000385-ALG-000138

**Group ID:** `V-65287`

### Rule: The DataPower Gateway providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when unauthorized network services are detected.

**Rule ID:** `SV-79777r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore, may be unreliable or serve as malicious rogues for valid services. Automated mechanisms can be used to send automatic alerts or notifications. Such automatic alerts or notifications can be conveyed in a variety of ways (e.g., telephonically, via electronic mail, via text message, or via websites). The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the WebGUI, go to Network >> Management >> Web Management Service. The "WS-Management endpoint" checkbox should be checked. Verify an IP and port for the WS-Management endpoint to connect to. If the WS-Management endpoint is not enabled (checked) or not configured, this is a finding.

## Group: SRG-NET-000390-ALG-000139

**Group ID:** `V-65289`

### Rule: The DataPower Gateway providing content filtering must continuously monitor inbound communications traffic crossing internal security boundaries for unusual or unauthorized activities or conditions.

**Rule ID:** `SV-79779r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If inbound communications traffic is not continuously monitored, hostile activity may not be detected and prevented. Output from application and traffic monitoring serves as input to continuous monitoring and incident response programs. Internal monitoring includes the observation of events occurring on the network crosses internal boundaries at managed interfaces such as web content filters. Depending on the type of ALG, organizations can monitor information systems by monitoring audit activities, application access patterns, characteristics of access, content filtering, or unauthorized exporting of information across boundaries. Unusual/unauthorized activities or conditions may include large file transfers, long-time persistent connections, unusual protocols and ports in use, and attempted communications with suspected malicious external addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a service, such as a MultiProtocol Gateway, by clicking the icon on the Control Panel. Click the name of the service in the list >> Set the Name and back end destination for the service. Under MultiProtocol Gateway Policy, click “...” to inspect the Policy >> Verify the Rule Direction is set to Client to Server. Double-click the existing Match Action on the rule line and verify it is set to default-accept-service providers. Double-click the Validate action >> Verify that it is set to a schema file. Double-click the AAA action to open it >> Click “...” to inspect the AAA Policy >> Follow the wizard steps to review the desired policy. When done, click cancel >> Click Cancel or Close window to close the Policy. If these items have not been configured, this is a finding.

## Group: SRG-NET-000391-ALG-000140

**Group ID:** `V-65291`

### Rule: The DataPower Gateway providing content filtering must continuously monitor outbound communications traffic crossing internal security boundaries for unusual/unauthorized activities or conditions.

**Rule ID:** `SV-79781r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not continuously monitored, hostile activity may not be detected and prevented. Output from application and traffic monitoring serves as input to continuous monitoring and incident response programs. Internal monitoring includes the observation of events occurring on the network crosses internal boundaries at managed interfaces such as web content filters. Depending on the type of ALG, organizations can monitor information systems by monitoring audit activities, application access patterns, characteristics of access, content filtering, or unauthorized exporting of information across boundaries. Unusual/unauthorized activities or conditions may include large file transfers, long-time persistent connections, unusual protocols and ports in use, and attempted communications with suspected malicious external addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a service, such as a MultiProtocol Gateway, by clicking the icon on the Control Panel. Click the name of the service in the list >> Set the Name and back end destination for the service. Under MultiProtocol Gateway Policy, click “...” to inspect the Policy >> Verify one Rule Direction is set to Client to Server. Double-click the existing Match Action on the rule line and verify it is set default-accept-service providers. Double-click the Validate action >> Verify that it is set to a schema file. Upload the necessary schema definition file to the action >> Click Done. Double-click the AAA action to open it >> Click “...” to inspect the AAA Policy >> Follow the wizard steps to review the desired policy. When done, click cancel. Verify one Rule Direction is set to Server to Client. Double-click the existing Match Action on the rule line and verify it is set default-accept-service providers. Double-click the Validate action >> Verify that it is set to a schema file. Double-click the AAA action to open it >> Click “...” to inspect the AAA Policy >> Follow the wizard steps to review the desired policy. When done, click cancel. Click Cancel or Close Window to close the Policy. If these items have not been configured, this is a finding.

## Group: SRG-NET-000392-ALG-000141

**Group ID:** `V-65293`

### Rule: The DataPower Gateway providing content filtering must send an alert to, at a minimum, the ISSO and ISSM when detection events occur.

**Rule ID:** `SV-79783r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. In accordance with CCI-001242, the ALG which provides content inspection services are a real-time intrusion detection system. These systems must generate an alert when detection events from real-time monitoring occur. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the DataPower web interface, navigate to Administration >> Access >> SNMP Settings. Verify that the desired event codes are included on the "Trap Event Subscriptions" tab. Type "Log Target" in to the Search bar >> Select "Log Targets" from the results list >> Select the desired Log Target >> Verify that the desired event codes are included in the Event Subscriptions tab. If no Log Target is configured or the assigned event codes are not included, this is a finding.

## Group: SRG-NET-000392-ALG-000142

**Group ID:** `V-65295`

### Rule: The DataPower Gateway providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources (e.g., IAVMs or CTOs) are detected.

**Rule ID:** `SV-79785r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. The ALG generates an alert which notifies designated personnel of the Indicators of Compromise (IOCs) which require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the DataPower WebGUI, navigate to Administration >> Access >> SNMP Settings. On the "Trap Event Subscriptions" tab, verify the inclusion of Event Subscriptions that are judged to be associated with threats identified by authoritative sources. If the Event Subscriptions are not present, this is a finding. On the "Trap and Notification Targets" tab, verify the inclusion of an approved SNMP server. If no SNMP Server is configured as a Trap and Notification Target, this is a finding.

## Group: SRG-NET-000392-ALG-000143

**Group ID:** `V-65297`

### Rule: The DataPower Gateway providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when root level intrusion events which provide unauthorized privileged access are detected.

**Rule ID:** `SV-79787r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. The ALG generates an alert which notifies designated personnel of the Indicators of Compromise (IOCs) which require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the DataPower WebGUI, navigate to Administration >> Access >> SNMP Settings. On the "Trap Event Subscriptions" tab, verify the inclusion of Event Subscriptions that are judged to be associated with the detection of root level intrusion events which provide unauthorized privileged access. If the Event Subscriptions are not configured, this is a finding. On the "Trap and Notification Targets" tab, verify the inclusion of an approved SNMP server. If no SNMP Server is configured as a Trap and Notification Target, this is a finding.

## Group: SRG-NET-000392-ALG-000147

**Group ID:** `V-65299`

### Rule: The DataPower Gateway providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when user level intrusions which provide non-privileged access are detected.

**Rule ID:** `SV-79789r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. The ALG generates an alert which notifies designated personnel of the Indicators of Compromise (IOCs) which require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the DataPower WebGUI, navigate to Administration >> Access >> SNMP Settings. On the "Trap Event Subscriptions" tab, verify the inclusion of Event Subscriptions that are judged to be associated with the detection of root level intrusion events that provide unauthorized privileged access. If the Event Subscriptions are not configured, this is a finding. On the "Trap and Notification Targets" tab, verify the inclusion of an approved SNMP server. If no SNMP Server is configured as a Trap and Notification Target, this is a finding.

## Group: SRG-NET-000392-ALG-000148

**Group ID:** `V-65301`

### Rule: The DataPower Gateway providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when denial of service incidents are detected.

**Rule ID:** `SV-79791r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. The ALG generates an alert which notifies designated personnel of the Indicators of Compromise (IOCs) which require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the WebGUI, go to Objects >> Logging Configuration>> Log Target. On the Main tab, SNMP should be selected. On the Event Subscriptions tab, confirm that there is an event subscription where Event Category = multistep and Minimum Event Priority = error. In the DataPower WebGUI, navigate to Administration >> Access >> SNMP Settings. Verify that the "Trap and Notification Targets" tab includes an approved SNMP server that generates alerts that will be forwarded, at a minimum, to the ISSO and ISSM. If no SNMP server is configured as a Log Target, this is a finding.

## Group: SRG-NET-000392-ALG-000149

**Group ID:** `V-65303`

### Rule: The DataPower Gateway providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when new active propagation of malware infecting
DoD systems or malicious code adversely affecting the operations and/or security
of DoD systems is detected.

**Rule ID:** `SV-79793r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. The ALG generates an alert which notifies designated personnel of the Indicators of Compromise (IOCs) which require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the WebGUI, expand the Services folder, expand the folder of the type of service used (such as MultiProtocol Gateway), and click on the Processing Policy menu item. In the Policy, double-click the AntiVirus action. This antivirus action must be configured to connect to organizationally approved scanning software that will generate an alert to the DataPower Gateway when new active propagation of malware infecting DoD systems or malicious code adversely affecting the operations and/or security of DoD systems is detected. Verify that the DataPower Gateway is configured to, upon receipt of an alert from the scanning software, generate notification messages to an authorized SNMP server that will, at a minimum, send an alert to the ISSO and ISSM by using the following steps: In the DataPower WebGUI, navigate to Administration >> Access >> SNMP Settings. On the "Trap Event Subscriptions" tab, verify the inclusion of Event Subscriptions that indicate virus detection. On the "Trap and Notification Targets" tab, verify that an approved SNMP server is configured as a Log Target. If no SNMP server is configured as a Log Target, this is a finding.

## Group: SRG-NET-000399-ALG-000042

**Group ID:** `V-65305`

### Rule: The DataPower Gateway providing user access control intermediary services must provide the capability for authorized users to capture, record, and log all content related to a selected user session.

**Rule ID:** `SV-79795r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to capture, record, and log content related to a user session, investigations into suspicious user activity would be hampered. The intent of this requirement is to ensure the capability to select specific sessions to capture is available in order to support general auditing/incident investigation, or to validate suspected misuse by a specific user. Examples of session events that may be captured include, port mirroring, tracking websites visited, and recording information and/or file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the WebGUI Control Panel, click on Troubleshooting >> Click on the Debug Probe tab. Verify that the desired service type and service instance has an active Probe track transaction information for that service instance. From the WebGUI, go to Objects >> Logging Configuration>> Log Target. Verify the desired filters, triggers, subscriptions, and log destination. If these items have not been configured, this is a finding.

## Group: SRG-NET-000401-ALG-000127

**Group ID:** `V-65307`

### Rule: The DataPower Gateway must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-79797r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior potentially leading to an application or information system compromise. Invalid input is one of the primary methods employed when attempting to compromise an application. Network devices with the functionality to perform application layer inspection may be leveraged to validate data content of network communications. Checking the valid syntax and semantics of information system inputs (e.g., character set, length, numerical range, and acceptable values) verifies that inputs match specified definitions for format and content. Software typically follows well-defined protocols that use structured messages (i.e., commands or queries) to communicate between software modules or system components. Structured messages can contain raw or unstructured data interspersed with metadata or control information. If network elements use attacker-supplied inputs to construct structured messages without properly encoding such messages, then the attacker could insert malicious commands or special characters that can cause the data to be interpreted as control information or metadata. Consequently, the module or component that receives the tainted output will perform the wrong operations or otherwise interpret the data incorrectly. Pre-screening inputs prior to passing to interpreters prevents the content from being unintentionally interpreted as commands. Input validation helps to ensure accurate and correct inputs and prevent attacks such as cross-site scripting and a variety of injection attacks. This requirement applies to gateways and firewalls that perform content inspection or have higher-layer proxy functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the processing policy for all flows to ensure they contain Validate actions for requests and responses. Privileged Account User logon to the WebGUI >> Open the service to modified: From the Control Panel, select the type of service to be edited (e.g., Multi-Protocol Gateway) >> The list of available services will be displayed >> Click the name of the service to be edited. Verify configuration of the processing policy: Click the “…” button adjacent to the configured Processing Policy (in the case of a Web Service Proxy, click the “Policy” processing policy tab) >> The processing policy is displayed >> Select the rule to be edited by clicking the “Rule Name” >> Ensure there is a Validate action on the rule and that the validate action contains the appropriate schema to check the message against. If these items have not been configured, this is a finding.

## Group: SRG-NET-000510-ALG-000025

**Group ID:** `V-65309`

### Rule: The DataPower Gateway providing encryption intermediary services must implement NIST FIPS-validated cryptography to generate cryptographic hashes.

**Rule ID:** `SV-79799r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. This requirement applies only to ALGs that provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the web interface for DataPower device management, verify that the DataPower Gateway Cryptographic Mode is Set to FIPS 140-2 Level 1 (Status >> Crypto >> Cryptographic Mode Status). If the Mode is not set to FIPS 140-2, this is a finding.

## Group: SRG-NET-000510-ALG-000040

**Group ID:** `V-65311`

### Rule: The DataPower Gateway providing encryption intermediary services must implement NIST FIPS-validated cryptography for digital signatures.

**Rule ID:** `SV-79801r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. This requirement applies only to ALGs that provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the web interface for DataPower device management, verify that the DataPower Gateway Cryptographic Mode is Set to FIPS 140-2 Level 1 (Status >> Crypto >> Cryptographic Mode Status). If this mode is not enabled, this is a finding. This mode bans the algorithms that are not allowed in FIPS 140-2 Level 1. The banned algorithms include Blowfish, CAST, DES, MD2, MD4, MD5, RC2, RC4, and RIPEMD. This mode also bans RSA keys less than 1024 bits and disables the cryptographic hardware that is not FIPS validated.

## Group: SRG-NET-000510-ALG-000111

**Group ID:** `V-65313`

### Rule: The DataPower Gateway providing encryption intermediary services must use NIST FIPS-validated cryptography to implement encryption services.

**Rule ID:** `SV-79803r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. This requirement applies only to ALGs that provide encryption intermediary services (e.g., HTTPS, TLS, or DNSSEC).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the web interface for DataPower device management, verify that the DataPower Gateway Cryptographic Mode is Set to FIPS 140-2 Level 1 (Status >> Crypto >> Cryptographic Mode Status). If this mode is not enabled, this is a finding. This mode bans the algorithms that are not allowed in FIPS 140-2 Level 1. The banned algorithms include Blowfish, CAST, DES, MD2, MD4, MD5, RC2, RC4, and RIPEMD. This mode also bans RSA keys less than 1024 bits and disables the cryptographic hardware that is not FIPS validated.

## Group: SRG-NET-000511-ALG-000051

**Group ID:** `V-65315`

### Rule: The DataPower Gateway must off-load audit records onto a centralized log server in real time.

**Rule ID:** `SV-79805r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. Off-loading is a common process in information systems with limited audit storage capacity. The audit storage on the ALG is used only in a transitory fashion until the system can communicate with the centralized log server designated for storing the audit records, at which point the information is transferred. However, DoD requires that the log be transferred in real time which indicates that the time from event detection to off-loading is seconds or less. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search Bar “Log Target” >> Log target >> Event Subscription tab. If “audit” is not listed under Event Category, this is a finding. If “Rule Action” does not contain a “Filter” action, this is a finding.

## Group: SRG-NET-000364-ALG-000122

**Group ID:** `V-65317`

### Rule: The DataPower Gateway must not use 0.0.0.0 as a listening IP address for any service.

**Rule ID:** `SV-79807r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using 0.0.0.0 as a listening address allows all interfaces to receive traffic for the service. This creates an unnecessary exposure when services are configured to listen on this address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Default domain. Click Status >> Main >> Active Services >> Click Show All Domains. Review IP addresses assigned to active services. If any list 0.0.0.0, this is a finding.

