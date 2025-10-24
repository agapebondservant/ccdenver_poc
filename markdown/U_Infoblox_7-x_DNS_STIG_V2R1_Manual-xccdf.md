# STIG Benchmark: Infoblox 7.x DNS Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DNS-000001

**Group ID:** `V-214159`

### Rule: Infoblox systems which perform zone transfers to non-Infoblox Grid DNS servers must be configured to limit the number of concurrent sessions for zone transfers.

**Rule ID:** `SV-214159r612370_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Limiting the number of concurrent sessions reduces the risk of Denial of Service (DoS) to the DNS implementation. Infoblox DNS servers configured in a Grid do not utilize zone transfers; data is replicated using an encrypted management connection. However when a zone contains both Infoblox Grid DNS servers and non-Grid DNS servers a protocol compliant zone transfer is performed. Name servers do not have direct user connections but accept client connections for queries. Original restriction on client connections should be high enough to prevent a self-imposed denial of service, after which the connections are monitored and fine-tuned to best meet the organization's specific requirements. Primary name servers also make outbound connection to secondary name servers to provide zone transfers and accept inbound connection requests from clients wishing to provide a dynamic update. Primary name servers should explicitly limit zone transfers to only be made to designated secondary name servers. Because zone transfers involve the transfer of entire zones and use TCP connections, they place substantial demands on network resources relative to normal DNS queries. Errant or malicious frequent zone transfer requests on the name servers of the enterprise can overload the master zone server and result in DoS to legitimate users. Primary name servers should be configured to limit the hosts from which they will accept dynamic updates. Additionally, the number of concurrent clients, especially TCP clients, needs to be kept to a level that does not risk placing the system in a DoS state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify inbound and outbound zone transfer limits are configured. These values control the amount of concurrent zone transfers to non-Grid DNS servers. Navigate to Data Management >> DNS >> Members/Servers tab. Review each server with the DNS service enabled. Select each server, click "Edit", toggle Advanced Mode and select General >> Advanced tab. Verify zone transfer limitations are configured. If all name servers for all zones utilize a single Infoblox Grid, zone data is transferred via the encrypted Infoblox Grid, this is not a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000516-DNS-000095

**Group ID:** `V-214160`

### Rule: Primary authoritative name servers must be configured to only receive zone transfer requests from specified secondary name servers.

**Rule ID:** `SV-214160r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authoritative name servers (especially primary name servers) should be configured with an allow-transfer access control substatement designating the list of hosts from which zone transfer requests can be accepted. These restrictions address the denial-of-service threat and potential exploits from unrestricted dissemination of information about internal resources. Based on the need-to-know, the only name servers that need to refresh their zone files periodically are the secondary name servers. Zone transfer from primary name servers should be restricted to secondary name servers. The zone transfer should be completely disabled in the secondary name servers. The address match list argument for the allow-transfer substatement should consist of IP addresses of secondary name servers and stealth secondary name servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox grid members do not utilize DNS zone transfers to exchange DNS data. Communication between grid members is via a distributed database over a secure Virtual Private Network (VPN). If configured to utilize zone transfers to external DNS servers, ensure Access Control Lists are configured to restrict data flow. If Access Controls Lists are not configured for zone transfers to external non-Grid servers, this is a finding.

## Group: SRG-APP-000001-DNS-000115

**Group ID:** `V-214161`

### Rule: The Infoblox system must limit the number of concurrent client connections to the number of allowed dynamic update clients.

**Rule ID:** `SV-214161r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of concurrent sessions reduces the risk of Denial of Service (DoS) to the DNS implementation. Name servers do not have direct user connections but accept client connections for queries. Original restriction on client connections should be high enough to prevent a self-imposed denial of service, after which the connections are monitored and fine-tuned to best meet the organization's specific requirements. Primary name servers also make outbound connections to secondary name servers to provide zone transfers and accept inbound connection requests from clients wishing to provide a dynamic update. Primary name servers should explicitly limit zone transfers to only be made to designated secondary name servers. Because zone transfers involve the transfer of entire zones and use TCP connections, they place substantial demands on network resources relative to normal DNS queries. Errant or malicious frequent zone transfer requests on the name servers of the enterprise can overload the master zone server and result in DoS to legitimate users. Primary name servers should be configured to limit the hosts from which they will accept dynamic updates. Additionally the number of concurrent clients, especially TCP clients, needs to be kept to a level that does not risk placing the system in a DoS state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox Systems can be configured in two ways to limit DDNS client updates. For clients that support GSS-TSIG, navigate to Data Management >> DNS >> Members/Servers tab. Review each server with the DNS service enabled. Select each server, click "Edit", toggle Advanced Mode and select GSS-TSIG. Verify that "Enable GSS-TSIG authentication of clients" is enabled. For clients that do not support GSS-TSIG, navigate to Data Management >> DNS >> Members/Servers tab. Review each server with the DNS service enabled. Select each server, click "Edit". Select the "Updates" tab. Verify that either a Named ACL or Set of ACEs are defined to limit client DDNS. When complete, click "Cancel" to exit the "Properties" screen. If "Enable GSS-TSIG authentication of clients" is disabled for clients supporting GSS-TSIG or a Named ACL or Set of ACEs are not defined to limit DDNS for clients without GSS-TSIG support, this is a finding.

## Group: SRG-APP-000125-DNS-000012

**Group ID:** `V-214162`

### Rule: The Infoblox system audit records must be backed up at least every seven days onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-214162r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Backing up audit records to a different system or onto separate media than the system being audited on a defined frequency helps to assure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. This requirement only applies to applications that have a native backup capability for audit records. Operating system backup requirements cover applications that do not provide native backup functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Grid >> Grid Manager >> Grid Properties >> Monitoring tab. If "Log to External Syslog Servers" is enabled, an External Syslog Server must be configured. If no external SYSLOG server is available verify local procedure to retain audit logs. Logs can be downloaded by navigation to Administration >> Logs >> Audit Log tab and pressing the "Download" button. When complete, click "Cancel" to exit the "Properties" screen. If neither an external SYSLOG server is configured, or a local policy is in place to store audit logs, this is a finding.

## Group: SRG-APP-000142-DNS-000014

**Group ID:** `V-214163`

### Rule: Infoblox systems configured to run the DNS service must be configured to prohibit or restrict unapproved ports and protocols.

**Rule ID:** `SV-214163r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements by providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. By default all services other than those required for management are disabled. Validate that no additional services have been enabled for DNS members. Navigate to Grid >> Grid Manager >> Services tab and review each service and member status at the top of the panel. Depending upon purchased options, Infoblox DNS members may be running DNS, Reporting, Threat Protection, Threat Analytics, and TAXII services, this is not a finding. If any unnecessary services such as file distribution services are enabled on the DNS members, this is a finding. Note: Once DNSSEC is enabled, the DNS service will be required to be running on the Grid Master.

## Group: SRG-APP-000158-DNS-000015

**Group ID:** `V-214164`

### Rule: Infoblox systems which are configured to perform zone transfers to non-Grid name servers must utilize transaction signatures (TSIG).

**Rule ID:** `SV-214164r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. This applies to server-to-server (zone transfer) transactions only and is provided by TSIG, which enforces mutual server authentication using a key that is unique to each server pair (TSIG), thus uniquely identifying the other server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Data Management >> DNS >> Zones tab. Review each zone by clicking Edit and inspecting the "Name Servers" tab. If the all entries in the "Type" column are configured as "Grid", this check is not applicable. Verify that each zone which contains non-Grid name servers is further verified by inspection of the "Zone Transfers" tab and configuration of TSIG Access Control Entry (ACE). If there is a non-Grid system which utilizes zone transfers but does not have a TSIG key, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000176-DNS-000094

**Group ID:** `V-214165`

### Rule: Only the private key corresponding to the ZSK alone must be kept on the name server that does support dynamic updates.

**Rule ID:** `SV-214165r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Infoblox systems when deployed in a Grid configuration store DNSSEC keys on the designated Grid Master system. As the central point of administration, the Grid Master should be configured for administration of the DNS, DHCP, and IP Address Management (IPAM) system. No clients should be configured to utilize the Grid Master or backup Candidate systems for protocol transactions. An alternative solution is through deployment of a Hardware Security Module (HSM), which provides hardware encrypted storage of key data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. By default ZSK private keys are stored encrypted within the Infoblox database on the Grid Master. The Grid Master will by default enable the DNS service when DNSSEC is enabled for internal processing. No clients should be permitted to utilize the Grid Master DNS service. Refer to the Infoblox STIG Overview document for additional information on HSM usage. Navigate to Data Management >> DNS >> Zones. Review each zone by selecting the zone and clicking "Edit", and selecting the "Name Servers" tab. If the Grid Master is a listed name server and not marked "Stealth", this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000176-DNS-000096

**Group ID:** `V-214166`

### Rule: Signature generation using the KSK must be done off-line, using the KSK-private stored off-line.

**Rule ID:** `SV-214166r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Infoblox systems when deployed in a Grid configuration store DNSSEC keys on the designated Grid Master system. As the central point of administration, the Grid Master should be configured for administration of the DNS, DHCP, and IP Address Management (IPAM) system. No clients should be configured to utilize the Grid Master or backup Candidate systems for protocol transactions. An alternative solution is through deployment of a Hardware Security Module (HSM), which provides hardware encrypted storage of key data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. By default KSK private keys are stored on the Grid Master. The Grid Master will by default enable the DNS service when DNSSEC is enabled for internal processing. No clients are permitted to utilize the Grid Master DNS service. Navigate to Data Management >> DNS >> Zones. Review each zone by selecting the zone and clicking edit, and selecting the "Name Servers" tab. If the Grid Master is a listed name server and not marked "Stealth", this is a finding. If a HSM is utilized, no further checks are necessary. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000185-DNS-000021

**Group ID:** `V-214167`

### Rule: The Infoblox system must be configured to employ strong authenticators in the establishment of nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-214167r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. The act of managing systems and applications includes the ability to access sensitive application information, such as system configuration details, diagnostic information, user information, and potentially sensitive application data. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric. Lack of authentication enables anyone to gain access to the network or possibly a network element that provides opportunity for intruders to compromise resources within the network infrastructure. Network access control mechanisms interoperate to prevent unauthorized access and to enforce the organization's security policy. Authorization for access to any network element requires an individual account identifier that has been approved, assigned, and configured on an authentication server. Authentication of all administrator accounts for all privilege levels must be accomplished using two or more factors that include the following: (i) something you know (e.g., password/PIN); (ii) something you have (e.g., cryptographic identification device, token); or (iii) something you are (e.g., biometric). Infoblox systems support authentication using multiple authenticators including; LDAP, RADIUS, Microsoft Active Directory, OCSP, and local user database. Strong authentication can be enabled by implementation of two or more authentication forms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of external authentication methods to validate multi-factor authentication is enabled. Navigate to Administration >> Administrators >> Authentication Policy. Ensure multi factor authentication is enabled by validation that the multiple authentication methods are enabled and that local database is the last entry in the list. When complete, click "Cancel" to exit the "Properties" screen. If the aggregate authentication policy does not provide two or more factors, this is a finding.

## Group: SRG-APP-000213-DNS-000024

**Group ID:** `V-214168`

### Rule: The Infoblox system must be configured to provide additional data origin artifacts along with the authoritative data the system returns in response to external name/address resolution queries.

**Rule ID:** `SV-214168r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The underlying feature in the major threat associated with DNS query/response (i.e., forged response or response failure) is the integrity of DNS data returned in the response. The security objective is to verify the integrity of each response received. An integral part of integrity verification is to ensure that valid data has originated from the right source. Establishing trust in the source is called data origin authentication. The security objectives—and consequently the security services—that are required for securing the DNS query/response transaction are data origin authentication and data integrity verification. The specification for a digital signature mechanism in the context of the DNS infrastructure is in IETF’s DNSSEC standard. In DNSSEC, trust in the public key (for signature verification) of the source is established not by going to a third party or a chain of third parties (as in public key infrastructure [PKI] chaining), but by starting from a trusted zone (such as the root zone) and establishing the chain of trust down to the current source of response through successive verifications of signature of the public key of a child by its parent. The public key of the trusted zone is called the trust anchor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Navigate to Data Management >> DNS >> Grid DNS properties. Toggle Advanced Mode click on "DNSSEC" tab, verify "Enable DNSSEC" is enabled. Navigate to Data Management >> DNS >> Zones. Verify that the "Signed" column is displayed. Validate that all external authoritative zones are signed by displaying "Yes". When complete, click "Cancel" to exit the "Properties" screen. If DNSSEC is not enabled, and external authoritative zones are not signed, this is a finding.

## Group: SRG-APP-000214-DNS-000025

**Group ID:** `V-214169`

### Rule: A DNS server implementation must provide the means to indicate the security status of child zones.

**Rule ID:** `SV-214169r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If name server replies are invalid or cannot be validated, many networking functions and communication would be adversely affected. With DNS, the presence of Delegation Signer (DS) records associated with child zones informs clients of the security status of child zones. These records are crucial to the DNSSEC chain of trust model. Each parent domain's DS record is used to verify the DNSKEY record in its subdomain, from the top of the DNS hierarchy down. A DNS server is an example of an information system providing name/address resolution service. Digital signatures and cryptographic keys are examples of additional artifacts. DNS resource records are examples of authoritative data. Applications other than the DNS, to map between host/service names and network addresses, must provide other means to assure the authenticity and integrity of response data. In DNS, trust in the public key of the source is established by starting from a trusted name server and establishing the chain of trust down to the current source of response through successive verifications of signature of the public key of a child by its parent. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and Domain Name System Security Extensions (DNSSEC). When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor. A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate. In DNS, a trust anchor is a DNSKEY that is placed into a validating resolver so the validator can cryptographically validate the results for a given request back to a known public key (the trust anchor). An example means to indicate the security status of child subspaces is through the use of delegation signer (DS) resource records in the DNS. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Without path validation and a chain of trust, there can be no trust that the data integrity authenticity has been maintained during a transaction.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Infoblox systems within a Grid configuration automatically publish DS records to the parent zone when the child zone is signed. If all name servers for parent and child zones are within an Infoblox Grid, this is not a finding. Review the parent zones hosted on the Infoblox server for which the child zone is NOTE on the same Infoblox Grid. Each zone must include the Delegation Signer (DS) records for the child zone. If DS records are not published in the parent zone for DNSSEC signed child zones, this is a finding.

## Group: SRG-APP-000214-DNS-000079

**Group ID:** `V-214170`

### Rule: The Key Signing Key (KSK) rollover interval must be configured to no less than one year.

**Rule ID:** `SV-214170r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DNS root key is a cryptographic public-private key pair used for DNSSEC signing of the DNS root zone records. The root zone KSK serves as the anchor for the “chain of trust” that enables DNS resolvers to validate the authenticity of any signed data in the DNS. The integrity of the DNS depends on a secure root key. Rolling the KSK means generating a new cryptographic public and private key pair and distributing the new public component to parties who operate validating resolvers, including: Internet Service Providers; enterprise network administrators and other Domain Name System (DNS) resolver operators; DNS resolver software developers; system integrators; and hardware and software distributors who install or ship the root's "trust anchor." The KSK is used to cryptographically sign the Zone Signing Key (ZSK), which is used by the Root Zone Maintainer to DNSSEC-sign the root zone of the Internet's DNS. Maintaining an up-to-date KSK is essential to ensuring DNSSEC-validating DNS resolvers continue to function following the rollover. Failure to have the current root zone KSK will mean that DNSSEC-validating DNS resolvers will be unable to resolve any DNS queries. An attacker that has compromised a KSK can use that key for only as long as the signature interval of the RRSIG covering the DS RR in the delegating parent. To prevent the impact of a compromised KSK, a delegating parent should also set the signature validity period for RRSIGs covering DS RRs in the range of a few days to one week. This re-signing does not require frequent rollover of the parent's ZSK, but scheduled ZSK rollover should still be performed at regular intervals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Navigate to Data Management >> DNS >> Grid DNS properties. Toggle "Advanced Mode" and click on the "DNSSEC" tab. Validate the “Key-Signing Key Rollover Interval” is configured to a value of no less than one year. If the “Key-Signing Key Rollover Interval” is configured to more than one year, this is a finding.

## Group: SRG-APP-000215-DNS-000003

**Group ID:** `V-214171`

### Rule: The Infoblox system implementation must enforce approved authorizations for controlling the flow of information between DNS servers and between DNS servers and DNS clients based on DNSSEC policies.

**Rule ID:** `SV-214171r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If information flow is not enforced based on approved authorizations, the system may become compromised. Information flow control regulates where information is allowed to travel within a system and between interconnected systems. The flow of all application information must be monitored and controlled so it does not introduce any unacceptable risk to the systems or data. Application-specific examples of enforcement occurs in systems that employ rule sets or establish configuration settings that restrict information system services or provide a message filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of information between interconnected systems in accordance with applicable policy. Within the context of DNS, this is applicable in terms of controlling the flow of DNS information between systems, such as DNS zone transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Review the Infoblox DNS configuration to verify only approved communications are allowed. Usage of Access Control Lists to control clients, DNS zone transfer configuration to systems external to the Infoblox grid, and grid member configuration can be used to control communications as desired. Infoblox systems within the same Grid utilize internal database transfer and do not perform zone transfers. If all systems are within the same Infoblox Grid, this is not a finding.

## Group: SRG-APP-000215-DNS-000026

**Group ID:** `V-214172`

### Rule: A DNS server implementation must provide the means to enable verification of a chain of trust among parent and child domains (if the child supports secure resolution services).

**Rule ID:** `SV-214172r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If name server replies are invalid or cannot be validated, many networking functions and communication would be adversely affected. With DNS, the presence of Delegation Signer (DS) records associated with child zones informs clients of the security status of child zones. These records are crucial to the DNSSEC chain of trust model. Each parent domain's DS record is used to verify the DNSKEY record in its subdomain, from the top of the DNS hierarchy down. A DNS server is an example of an information system providing name/address resolution service. Digital signatures and cryptographic keys are examples of additional artifacts. DNS resource records are examples of authoritative data. Applications other than the DNS to map between host/service names and network addresses must provide other means to assure the authenticity and integrity of response data. DNSSEC provides the means to verify integrity assurances for the host/service name to network address resolution information obtained through the service. By using the delegation signer (DS) resource records in the DNS, the security status of a child domain can be validated. The DS resource record is used to identify the DNSSEC signing key of a delegated zone. Starting from a trusted name server (such as the root name server) and down to the current source of response through successive verifications of signature of the public key of a child by its parent, the chain of trust is established. The public key of the trusted name servers is called the trust anchor. After authenticating the source, the next process DNSSEC calls for is to authenticate the response. This requires that responses consist of not only the requested RRs but also an authenticator associated with them. In DNSSEC, this authenticator is the digital signature of a Resource Record (RR) Set. The digital signature of an RRSet is encapsulated through a special RRType called RRSIG. The DNS client using the trusted public key of the source (whose trust has just been established) then verifies the digital signature to detect if the response is valid or bogus. This control enables the DNS to obtain origin authentication and integrity verification assurances for the host/service name to network address resolution information obtained through the service. Without indication of the security status of a child domain and enabling verification of a chain of trust, integrity and availability of the DNS infrastructure cannot be assured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Authoritative Check: Navigate to Data Management >> DNS >> Zones. Ensure external authoritative zones are DNSSEC signed. Recursive Check: Navigate to Data Management >> DNS >> Zones. Note: DNSSEC validation is only applicable on a grid member where recursion is active. Edit "Grid DNS Properties", toggle Advanced Mode, and select the DNSSEC tab. Validate that both "Enable DNSSEC" and "Enable DNSSEC Validation" are enabled. When complete, click "Cancel" to exit the "Properties" screen. If DNSSEC is not utilized for authoritative DNS and recursive clients this is a finding. Note: To add "Signed" column, select an existing column, select the down arrow, select "Columns", select "Edit Columns", select the check box for "Visible" and select "Apply".

## Group: SRG-APP-000219-DNS-000028

**Group ID:** `V-214174`

### Rule: Infoblox DNS servers must protect the authenticity of communications sessions for zone transfers.

**Rule ID:** `SV-214174r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS is a fundamental network service that is prone to various attacks, such as cache poisoning and man-in-the middle attacks. If communication sessions are not provided appropriate validity protections, such as the employment of DNSSEC, the authenticity of the data cannot be guaranteed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Data Management >> DNS >> Zones tab. Review each zone by clicking "Edit" and inspecting the "Name Servers" tab. If the all entries in the "Type" column are configured as "Grid", this check is not applicable. Verify that each zone which contains non-Grid name servers is further verified by inspection of the "Zone Transfers" tab and configuration of TSIG Access Control Entry (ACE). If there is a non-Grid system which utilizes zone transfers but does not have a TSIG key, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000219-DNS-000029

**Group ID:** `V-214175`

### Rule: Infoblox DNS servers must be configured to protect the authenticity of communications sessions for dynamic updates.

**Rule ID:** `SV-214175r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS is a fundamental network service that is prone to various attacks, such as cache poisoning and man-in-the middle attacks. If communication sessions are not provided appropriate validity protections, such as the employment of DNSSEC, the authenticity of the data cannot be guaranteed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Infoblox Systems can be configured in two ways to limit DDNS client updates. For clients that support GSS-TSIG, navigate to Data Management >> DNS >> Members/Servers tab. Review each server with the DNS service enabled. Select each server, click "Edit", toggle Advanced Mode and select GSS-TSIG. Verify that "Enable GSS-TSIG authentication of clients" is enabled. For clients that do not support GSS-TSIG, navigate to Data Management >> DNS >> Members/Servers tab. Review each server with the DNS service enabled. Select each server, click "Edit". Select the "Updates" tab. Verify that either a Named ACL or Set of ACEs are defined to limit client DDNS. When complete, click "Cancel" to exit the "Properties" screen. If clients that support GSS-TSIG do not have "Enable GSS-TSIG authentication of clients" set or a named ACL or set of ACEs for clients that do not support GSS-TSIG, this is a finding.

## Group: SRG-APP-000219-DNS-000030

**Group ID:** `V-214176`

### Rule: Infoblox DNS servers must be configured to protect the authenticity of communications sessions for queries.

**Rule ID:** `SV-214176r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The underlying feature in the major threat associated with DNS query/response (i.e., forged response or response failure) is the integrity of DNS data returned in the response. An integral part of integrity verification is to ensure that valid data has originated from the right source. DNSSEC is required for securing the DNS query/response transaction by providing data origin authentication and data integrity verification through signature verification and the chain of trust.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties, toggle Advanced Mode click on "DNSSEC" tab. When complete, click "Cancel" to exit the "Properties" screen. Note: DNSSEC validation is only applicable on a grid member where recursion is active. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000226-DNS-000032

**Group ID:** `V-214177`

### Rule: In the event of a system failure, The Infoblox system must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to mission processes.

**Rule ID:** `SV-214177r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving application state information helps to facilitate application restart and return to the operational mode of the organization with less disruption to mission-essential processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default all system events are logged to the local SYSLOG. To ensure logging of data in the event of system failure, an external log server must be configured. Navigate to Grid >> Grid Manager >> Grid Properties >> Monitoring tab. When complete, click "Cancel" to exit the "Properties" screen. If "Log to External Syslog Servers" is enabled, an External Syslog Server must be configured and "Copy Audit Log Message to Syslog" must be configured otherwise, this is a finding.

## Group: SRG-APP-000246-DNS-000035

**Group ID:** `V-214178`

### Rule: The Infoblox system must be configured to restrict the ability of individuals to use the DNS server to launch Denial of Service (DoS) attacks against other information systems.

**Rule ID:** `SV-214178r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A DoS is a condition where a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Individuals of concern can include hostile insiders or external adversaries that have successfully breached the information system and are using the system as a platform to launch cyber attacks on third parties. Applications and application developers must take the steps needed to ensure users cannot use an authorized application to launch DoS attacks against other systems and networks. For example, applications may include mechanisms that throttle network traffic so users are not able to generate unlimited network traffic via the application. Limiting system resources that are allocated to any user to a bare minimum may also reduce the ability of users to launch some DoS attacks. When it comes to DoS attacks, most of the attention is paid to ensuring that systems and applications are not victims of these attacks. A DoS attack against the DNS infrastructure has the potential to cause a denial of service to all network users. As the DNS is a distributed backbone service of the Internet, numerous forms of attacks result in DoS, and they are still prevalent on the Internet today. Some potential DoS attacks against the DNS include malformed packet flood, spoofed source addresses, and distributed DoS, and the DNS can be exploited to launch amplification attacks upon other systems. While it is true that those accountable for systems want to ensure they are not affected by a DoS attack, they also need to ensure their systems and applications are not used to launch such an attack against others. To that end, a variety of technologies exist to limit the effects of DoS attacks, such as careful configuration of resolver and recursion functionality. DNS administrators must take the steps needed to ensure other systems and tools cannot use exploits to launch DoS attacks against other systems and networks. An example would be designing the DNS architecture to include mechanisms that throttle DNS traffic and resources so that users/other DNS servers are not able to generate unlimited DNS traffic via the application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox systems have a number of options that can be configured to reduce the ability to be exploited in a DoS attack. Primary consideration for this check should be given to client restrictions such as disabling open recursive servers, using ACLs to limit client communication, placement in secure network architecture to prevent address spoofing. If there is an open recursive DNS service on external name servers, or unrestricted access to internal name servers, this is a finding.

## Group: SRG-APP-000247-DNS-000036

**Group ID:** `V-214179`

### Rule: The Infoblox system must be configured to manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-214179r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. In the case of application DoS attacks, care must be taken when designing the application to ensure the application makes the best use of system resources. SQL queries have the potential to consume large amounts of CPU cycles if they are not tuned for optimal performance. Web services containing complex calculations requiring large amounts of time to complete can bog down if too many requests for the service are encountered within a short period of time. A denial of service (DoS) attack against the DNS infrastructure has the potential to cause a DoS to all network users. As the DNS is a distributed backbone service of the Internet, various forms of amplification attacks resulting in DoS, while utilizing the DNS, are still prevalent on the Internet today. Some potential DoS flooding attacks against the DNS include malformed packet flood, spoofed source addresses, and distributed DoS. Without the DNS, users and systems would not have the ability to perform simple name to IP resolution. Configuring the DNS implementation to defend against cache poisoning, employing increased capacity and bandwidth, building redundancy into the DNS architecture, utilizing DNSSEC, limiting and securing recursive services, DNS black holes, etc., may reduce the susceptibility to some flooding types of DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox systems have a number of options that can be configured to reduce the ability to be exploited in a DoS attack. Usage of rate limiting can reduce risk from cache poisoning attacks and DoS attacks. Log on to the Infoblox system and issue the commands: "show ip_rate_limit" and "show dns_rrl" Review the output from these commands with the network architecture. If rate limiting is not configured on the Infoblox system or within the network security architecture, this is a finding. Note: "set dns_rrl" is only applicable to code version 7.2 and above.

## Group: SRG-APP-000268-DNS-000039

**Group ID:** `V-214180`

### Rule: The Infoblox system must be configured to activate a notification to the system administrator when a component failure is detected.

**Rule ID:** `SV-214180r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Predictable failure prevention requires organizational planning to address system failure issues. If components key to maintaining systems security fail to function, the system could continue operating in an insecure state. The organization must be prepared and the application must support requirements that specify if the application must alarm for such conditions and/or automatically shut down the application or the system. This can include conducting a graceful application shutdown to avoid losing information. Automatic or manual transfer of components from standby to active mode can occur, for example, upon detection of component failures. If a component such as the DNSSEC or TSIG/SIG(0) signing capabilities were to fail, the DNS server should shut itself down to prevent continued execution without the necessary security components in place. Transactions such as zone transfers would not be able to work correctly anyway in this state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox systems are capable of providing notifications via remote SYSLOG, SNMP, and SMTP. Navigate to the "Grid" tab and select "Grid Properties", toggle Advanced Mode, and review "Monitoring", "SNMP", "SNMP Threshold", "Email", and "Notifications" tabs. When complete, click "Cancel" to exit the "Properties" screen. If no external notifications are enabled, this is a finding.

## Group: SRG-APP-000347-DNS-000041

**Group ID:** `V-214181`

### Rule: An Infoblox DNS server must strongly bind the identity of the DNS server with the DNS information using DNSSEC.

**Rule ID:** `SV-214181r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Weakly bound credentials can be modified without invalidating the credential; therefore, non-repudiation can be violated. This requirement supports audit requirements that provide organizational personnel with the means to identify who produced specific information in the event of an information transfer. Organizations and/or data owners determine and approve the strength of the binding between the information producer and the information based on the security category of the information and relevant risk factors. DNSSEC uses digital signatures to verify the identity of the producer of particular pieces of information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties, toggle Advanced Mode click on "DNSSEC" tab. Note: DNSSEC validation is only applicable on a grid member where recursion is active. When complete, click "Cancel" to exit the "Properties" screen. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000348-DNS-000042

**Group ID:** `V-214182`

### Rule: The Infoblox system must be configured to provide the means for authorized individuals to determine the identity of the source of the DNS server-provided information.

**Rule ID:** `SV-214182r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without a means for identifying the individual that produced the information, the information cannot be relied upon. Identifying the validity of information may be delayed or deterred. This requirement provides organizational personnel with the means to identify who produced specific information in the event of an information transfer. DNSSEC and TSIG/SIG(0) both use digital signatures to establish the identity of the producer of particular pieces of information. These signatures can be examined and verified to determine the identity of the producer of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties, toggle Advanced Mode click on "DNSSEC" tab. Note: DNSSEC validation is only applicable on a grid member where recursion is active. When complete, click "Cancel" to exit the "Properties" screen. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000349-DNS-000043

**Group ID:** `V-214183`

### Rule: The Infoblox system must be configured to validate the binding of the other DNS servers identity to the DNS information for a server-to-server transaction (e.g., zone transfer).

**Rule ID:** `SV-214183r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Validation of the binding of the information prevents the modification of information between production and review. The validation of bindings can be achieved, for example, by the use of cryptographic checksums. Validations must be performed automatically. DNSSEC and TSIG/SIG(0) technologies are not effective unless the digital signatures they generate are validated to ensure that the information has not been tampered with and that the producer's identity is legitimate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Navigate to Data Management >> DNS >> Zones tab. Review each zone by clicking "Edit" and inspecting the "Name Servers" tab. If the all entries in the "Type" column are configured as "Grid", this check is not applicable. Verify that each zone which contains non-Grid name servers is further verified by inspection of the "Zone Transfers" tab and configuration of TSIG Access Control Entry (ACE). If there is a non-Grid system which utilizes zone transfers but does not have a TSIG key, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000383-DNS-000047

**Group ID:** `V-214185`

### Rule: Recursion must be disabled on Infoblox DNS servers which are configured as authoritative name servers.

**Rule ID:** `SV-214185r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A potential vulnerability of DNS is that an attacker can poison a name server's cache by sending queries that will cause the server to obtain host-to-IP address mappings from bogus name servers that respond with incorrect information. Once a name server has been poisoned, legitimate clients may be directed to non-existent hosts (which constitutes a denial of service), or, worse, hosts that masquerade as legitimate ones to obtain sensitive data or passwords. To guard against poisoning, name servers authoritative for .mil domains should be separated functionally from name servers that resolve queries on behalf of internal clients. Organizations may achieve this separation by dedicating machines to each function or, if possible, by running two instances of the name server software on the same machine: one for the authoritative function and the other for the resolving function. In this design, each name server process may be bound to a different IP address or network interface to implement the required segregation. DNSSEC ensures that the answer received when querying for name resolution actually comes from a trusted name server. Since DNSSEC is still far from being globally deployed external to DoD, and many resolvers either have not been updated or do not support DNSSEC, maintaining cached zone data separate from authoritative zone data mitigates the gap until all DNS data is validated with DNSSEC. Since DNS forwarding of queries can be accomplished in some DNS applications without caching locally, DNS forwarding is the method to be used when providing external DNS resolution to internal clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Data Management >> DNS >> Members/Servers tab. Select each grid member and click "Edit". Review the "Queries" tab. When complete, click "Cancel" to exit the "Properties" screen. If recursion is not disabled on an authoritative name server, this is a finding.

## Group: SRG-APP-000394-DNS-000049

**Group ID:** `V-214186`

### Rule: The Infoblox system must authenticate the other DNS server before responding to a server-to-server transaction.

**Rule ID:** `SV-214186r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific pre-authorized devices can access the system. This requirement applies to server-to-server (zone transfer) transactions only and is provided by TSIG/SIG(0), which enforces mutual server authentication using a key that is unique to each server pair (TSIG) or using PKI-based authentication (SIG(0)).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Data Management >> DNS >> Zones tab. Review each zone by clicking "Edit" and inspecting the "Name Servers" tab. If the all entries in the "Type" column are configured as "Grid", this check is not applicable. Verify that each zone which contains non-Grid name servers is further verified by inspection of the "Zone Transfers" tab and configuration of TSIG Access Control Entry (ACE). If there is a non-Grid system which utilizes zone transfers but does not have a TSIG key, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000395-DNS-000050

**Group ID:** `V-214187`

### Rule: The DNS server implementation must authenticate another DNS server before establishing a remote and/or network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-214187r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. This requirement applies to server-to-server (zone transfer) transactions only and is provided by TSIG/SIG(0), which enforces mutual server authentication using a key that is unique to each server pair (TSIG) or using PKI-based authentication (SIG(0)).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Data Management >> DNS >> Zones tab. Review each zone by clicking "Edit" and inspecting the "Name Servers" tab. If the all entries in the "Type" column are configured as "Grid", this check is not applicable. Verify that each zone which contains non-Grid name servers is further verified by inspection of the "Zone Transfers" tab and configuration of TSIG Access Control Entry (ACE). If there is a non-Grid system which utilizes zone transfers but does not have a TSIG key, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000420-DNS-000053

**Group ID:** `V-214188`

### Rule: A DNS server implementation must provide data origin artifacts for internal name/address resolution queries.

**Rule ID:** `SV-214188r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The major threat associated with DNS forged responses or failures is the integrity of the DNS data returned in the response. The principle of DNSSEC is to mitigate this threat by providing data origin authentication, establishing trust in the source. This requirement enables remote clients to obtain origin authentication and integrity verification assurances for the host/service name to network address resolution information obtained through the service. A DNS server is an example of an information system providing name/address resolution service. Digital signatures and cryptographic keys are examples of additional artifacts. DNS resource records are examples of authoritative data. Applications other than the DNS to map between host/service names and network addresses must provide other means to assure the authenticity and integrity of response data. In the case of DNS, employ DNSSEC to provide an additional data origin and integrity artifacts along with the authoritative data the system returns in response to DNS name/address resolution queries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties. Note: DNSSEC validation is only applicable on a grid member where recursion is active. Toggle Advanced Mode click on "DNSSEC" tab. When complete, click "Cancel" to exit the "Properties" screen. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000421-DNS-000054

**Group ID:** `V-214189`

### Rule: A DNS server implementation must provide data integrity protection artifacts for internal name/address resolution queries.

**Rule ID:** `SV-214189r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The major threat associated with DNS forged responses or failures is the integrity of the DNS data returned in the response. The principle of DNSSEC is to mitigate this threat by providing data origin authentication, establishing trust in the source. This requirement enables remote clients to obtain origin authentication and integrity verification assurances for the host/service name to network address resolution information obtained through the service. A DNS server is an example of an information system providing name/address resolution service. Digital signatures and cryptographic keys are examples of additional artifacts. DNS resource records are examples of authoritative data. Applications other than the DNS to map between host/service names and network addresses must provide other means to assure the authenticity and integrity of response data. In the case of DNS, employ DNSSEC to provide an additional data origin and integrity artifacts along with the authoritative data the system returns in response to DNS name/address resolution queries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties. Note: DNSSEC validation is only applicable on a grid member where recursion is active. Toggle Advanced Mode click on "DNSSEC" tab. When complete, click "Cancel" to exit the "Properties" screen. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000422-DNS-000055

**Group ID:** `V-214190`

### Rule: A DNS server implementation must provide additional integrity artifacts along with the authoritative name resolution data the system returns in response to external name/address resolution queries.

**Rule ID:** `SV-214190r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The major threat associated with DNS forged responses or failures is the integrity of the DNS data returned in the response. The principle of DNSSEC is to mitigate this threat by providing data origin authentication, establishing trust in the source. This requirement enables remote clients to obtain origin authentication and integrity verification assurances for the host/service name to network address resolution information obtained through the service. A DNS server is an example of an information system providing name/address resolution service. Digital signatures and cryptographic keys are examples of additional artifacts. DNS resource records are examples of authoritative data. Applications other than the DNS to map between host/service names and network addresses must provide other means to assure the authenticity and integrity of response data. In the case of DNS, employ DNSSEC to provide an additional data origin and integrity artifacts along with the authoritative data the system returns in response to DNS name/address resolution queries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties. Note: DNSSEC validation is only applicable on a grid member where recursion is active. Toggle Advanced Mode click on "DNSSEC" tab. When complete, click "Cancel" to exit the "Properties" screen. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000423-DNS-000056

**Group ID:** `V-214191`

### Rule: A DNS server implementation must request data origin authentication verification on the name/address resolution responses the system receives from authoritative sources.

**Rule ID:** `SV-214191r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed that would result in query failure or denial of service. Data origin authentication must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching DNS servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties. Note: DNSSEC validation is only applicable on a grid member where recursion is active. Toggle Advanced Mode click on "DNSSEC" tab. When complete, click "Cancel" to exit the "Properties" screen. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000424-DNS-000057

**Group ID:** `V-214192`

### Rule: A DNS server implementation must request data integrity verification on the name/address resolution responses the system receives from authoritative sources.

**Rule ID:** `SV-214192r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed that would result in query failure or denial of service. Data integrity verification must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching DNS servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties. Note: DNSSEC validation is only applicable on a grid member where recursion is active. Toggle Advanced Mode click on "DNSSEC" tab. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled this is a finding. When complete, click "Cancel" to exit the "Properties" screen. If DNSSEC validation is not enabled, this is a finding.

## Group: SRG-APP-000425-DNS-000058

**Group ID:** `V-214193`

### Rule: A DNS server implementation must perform data integrity verification on the name/address resolution responses the system receives from authoritative sources.

**Rule ID:** `SV-214193r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed that would result in query failure or denial of service. Data integrity verification must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching DNS servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties. Note: DNSSEC validation is only applicable on a grid member where recursion is active. Toggle Advanced Mode click on "DNSSEC" tab. When complete, click "Cancel" to exit the "Properties" screen. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000426-DNS-000059

**Group ID:** `V-214194`

### Rule: A DNS server implementation must perform data origin verification authentication on the name/address resolution responses the system receives from authoritative sources.

**Rule ID:** `SV-214194r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data origin authentication and data integrity verification are not performed, the resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed which would result in query failure or denial of service. Data origin authentication verification must be performed to thwart these types of attacks. Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Information systems that provide name and address resolution services for local clients include, for example, recursive resolving or caching DNS servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC validation is enabled by navigating to Data Management >> DNS >> Grid DNS properties. Note: DNSSEC validation is only applicable on a grid member where recursion is active. Toggle Advanced Mode click on "DNSSEC" tab. When complete, click "Cancel" to exit the "Properties" screen. If both "Enable DNSSEC" and "Enable DNSSEC validation" are not enabled, this is a finding.

## Group: SRG-APP-000439-DNS-000063

**Group ID:** `V-214195`

### Rule: The Infoblox system must be configured to must protect the integrity of transmitted information.

**Rule ID:** `SV-214195r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Confidentiality is not an objective of DNS, but integrity is. DNSSEC and TSIG/SIG(0) both digitally sign DNS information to authenticate its source and ensure its integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Verify that DNSSEC is enabled by navigating to Data Management >> DNS >> Grid DNS properties tab. Toggle Advanced Mode and review the "DNSSEC" tab to verify DNSSEC is enabled. When complete, click "Cancel" to exit the "Properties" screen. If DNSSEC validation is not enabled, this is a finding.

## Group: SRG-APP-000440-DNS-000065

**Group ID:** `V-214196`

### Rule: The Infoblox system must implement cryptographic mechanisms to detect changes to information during transmission unless otherwise protected by alternative physical safeguards, such as, at a minimum, a Protected Distribution System (PDS).

**Rule ID:** `SV-214196r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encrypting information for transmission protects information from unauthorized disclosure and modification. Cryptographic mechanisms implemented to protect information integrity include, for example, cryptographic hash functions which have common application in digital signatures, checksums, and message authentication codes. Confidentiality is not an objective of DNS, but integrity is. DNSSEC and TSIG/SIG(0) both digitally sign DNS information to authenticate its source and ensure its integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Verify that DNSSEC is enabled by navigating to Data Management >> DNS >> Grid DNS Properties tab. Toggle Advanced Mode and review the "DNSSEC" tab to verify DNSSEC is enabled. When complete, click "Cancel" to exit the "Properties" screen. If DNSSEC is not enabled, this is a finding.

## Group: SRG-APP-000441-DNS-000066

**Group ID:** `V-214197`

### Rule: The DNS server implementation must maintain the integrity of information during preparation for transmission.

**Rule ID:** `SV-214197r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Confidentiality is not an objective of DNS, but integrity is. DNS is responsible for maintaining the integrity of DNS information while it is being prepared for transmission.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Data Management >> DNS >> Zones tab. Review each zone by clicking "Edit" and inspecting the "Name Servers" tab. If the all entries in the "Type" column are configured as "Grid", this check is not applicable. Verify that each zone which contains non-Grid name servers is further verified by inspection of the "Zone Transfers" tab and configuration of TSIG Access Control Entry (ACE). If there is a non-Grid system which utilizes zone transfers but does not have a TSIG key, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000442-DNS-000067

**Group ID:** `V-214198`

### Rule: The DNS server implementation must maintain the integrity of information during reception.

**Rule ID:** `SV-214198r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Confidentiality is not an objective of DNS, but integrity is. DNS is responsible for maintaining the integrity of DNS information while it is being received.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Data Management >> DNS >> Zones tab. Review each zone by clicking "Edit" and inspecting the "Name Servers" tab. If the all entries in the "Type" column are configured as "Grid", this check is not applicable. Verify that each zone which contains non-Grid name servers is further verified by inspection of the "Zone Transfers" tab and configuration of TSIG Access Control Entry (ACE). If there is a non-Grid system which utilizes zone transfers but does not have a TSIG key, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000451-DNS-000069

**Group ID:** `V-214199`

### Rule: The DNS server implementation must follow procedures to re-role a secondary name server as the master name server should the master name server permanently lose functionality.

**Rule ID:** `SV-214199r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to an unsecure condition negatively impacts application security and can lead to system compromise. Failure conditions include, for example, loss of communications among critical system components or between system components and operational facilities. Fail-safe procedures include, for example, alerting operator personnel and providing specific instructions on subsequent steps to take (e.g., do nothing, reestablish system settings, shut down processes, restart the system, or contact designated organizational personnel). If a component such as the DNSSEC or TSIG/SIG(0) signing capabilities were to fail, the DNS server should shut itself down to prevent continued execution without the necessary security components in place. Transactions such as zone transfers would not be able to work correctly anyway in this state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Within an Infoblox Grid, configuration control is done through the Grid Master. In the event of a Grid Member failure, upon replacement, the Grid Master will configure the new system to replace the failed member. A Grid Master Candidate can be configured to alleviate issues in the event of a Grid Master failure. The Grid Master will replicate the entire database to the Grid Master Candidate, which can be promoted to the Grid Master role if needed. Review Grid, Grid Manger configuration to ensure a Grid Master Candidate is configured. If the site does not have a Grid Master Candidate, or local backup and policy guidance on system recovery, this is a finding.

## Group: SRG-APP-000474-DNS-000073

**Group ID:** `V-214200`

### Rule: The DNS server implementation must log the event and notify the system administrator when anomalies in the operation of the signed zone transfers are discovered.

**Rule ID:** `SV-214200r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. If anomalies are not acted upon, security functions may fail to secure the system. The DNS server does not have the capability of shutting down or restarting the information system. The DNS server can be configured to generate audit records when anomalies are discovered, and the OS/NDM can then trigger notification messages to the system administrator based on the presence of those audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox systems are capable of providing notifications via remote SYSLOG, SNMP, and SMTP. Navigate to the "Grid" tab and select "Grid Properties". Toggle Advanced mode, and review "Monitoring", "SNMP", "SNMP Threshold", "Email", and "Notifications" tabs. When complete, click "Cancel" to exit the "Properties" screen. If no external notifications are enabled, this is a finding.

## Group: SRG-APP-000514-DNS-000075

**Group ID:** `V-214201`

### Rule: The DNS server must implement NIST FIPS-validated cryptography for provisioning digital signatures, generating cryptographic hashes, and protecting unclassified information requiring confidentiality.

**Rule ID:** `SV-214201r612370_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Navigate to Data Management >> DNS >> Grid DNS properties. Toggle Advanced Mode click on "DNSSEC" tab. Validate that all Key Signing Keys (KSK) and Zone Signing Keys (ZSK) utilize FIPS approved algorithms. When complete, click "Cancel" to exit the "Properties" screen. If non FIPS-approved algorithms are in use, this is a finding.

## Group: SRG-APP-000516-DNS-000078

**Group ID:** `V-214202`

### Rule: The Zone Signing Key (ZSK) rollover interval must be configured to less than two months.

**Rule ID:** `SV-214202r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker that has compromised a ZSK can use that key only during the KSK's signature validity interval. An attacker that has compromised a KSK can use that key for only as long as the signature interval of the RRSIG covering the DS RR in the delegating parent. These validity periods should be short, which will require frequent re-signing. To minimize the impact of a compromised ZSK, a zone administrator should set a rollover interval of no less than two months for the ZSK. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Review the Infoblox DNSSEC configuration and validate the ZSK rollover interval is configured for a range of no more than two months. Navigate to Data Management >> DNS >> Grid DNS properties. Toggle Advanced Mode and click on the "DNSSEC" tab. Validate the “Zone-Signing Key Rollover Interval” is configured to a value of less than two months. If the “Zone-Signing Key Rollover Interval” is configured to a value more than two months, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000516-DNS-000084

**Group ID:** `V-214203`

### Rule: NSEC3 must be used for all internal DNS zones.

**Rule ID:** `SV-214203r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure that RRs associated with a query are really missing in a zone file and have not been removed in transit, the DNSSEC mechanism provides a means for authenticating the nonexistence of an RR. It generates a special RR called an NSEC (or NSEC3) RR that lists the RRTypes associated with an owner name as well as the next name in the zone file. It sends this special RR, along with its signatures, to the resolving name server. By verifying the signature, a DNSSEC-aware resolving name server can determine which authoritative owner name exists in a zone and which authoritative RRTypes exist at those owner names. IETF's design criteria consider DNS data to be public. Confidentiality is not one of the security goals of DNSSEC. DNSSEC is not designed to directly protect against denial-of-service threats but does so indirectly by providing message integrity and source authentication. An artifact of how DNSSEC performs negative responses allows a client to map all the names in a zone (zone walking). A zone which contains zone data that the administrator does not want to be made public should use the NSEC3 RR option for providing authenticated denial of existence. If DNSSEC is enabled for a server, the ability to verify a particular server which may attempt to update the DNS server actually exists. This is done through the use of NSEC3 records to provide an "authenticated denial of existence" for specific systems whose addresses indicate that they lie within a particular zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Review the zone configuration and confirm that, if DNSSEC is enabled NSEC3 is utilized. Review zone data or use Global Search string ".". Type Equals NSEC Record to verify no undesired NSEC records exists. If NSEC records exist in an active zone, this is a finding.

## Group: SRG-APP-000516-DNS-000085

**Group ID:** `V-214204`

### Rule: The Infoblox system must ensure each NS record in a zone file points to an active name server authoritative for the domain specified in that record.

**Rule ID:** `SV-214204r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Poorly constructed NS records pose a security risk because they create conditions under which an adversary might be able to provide the missing authoritative name services that are improperly specified in the zone file. The adversary could issue bogus responses to queries that clients would accept because they learned of the adversary's name server from a valid authoritative name server, one that need not be compromised for this attack to be successful. The list of slave servers must remain current within 72 hours of any changes to the zone architecture that would affect the list of slaves. If a slave server has been retired or is not operational but remains on the list, then an adversary might have a greater opportunity to impersonate that slave without detection, rather than if the slave were actually online. For example, the adversary may be able to spoof the retired slave's IP address without an IP address conflict, which would not be likely to occur if the true slave were active.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Infoblox Grid Members, log on to the Grid Master. Navigate to Data Management >> DNS >> Members/Servers tab. Verify that all assigned members have a status of "Running". For non-Infoblox systems, review DNS zone data and confirm that all systems external to the Infoblox grid have NS records which point to an active name server authoritative for the domain. If the Infoblox Grid Members do not have a status of "Running" or non-Infoblox systems do not have NS records pointing to an active name server authoritative for the domain, this is a finding.

## Group: SRG-APP-000516-DNS-000087

**Group ID:** `V-214205`

### Rule: All authoritative name servers for a zone must be located on different network segments.

**Rule ID:** `SV-214205r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most enterprises have an authoritative primary server and a host of authoritative secondary name servers. It is essential that these authoritative name servers for an enterprise be located on different network segments. This dispersion ensures the availability of an authoritative name server not only in situations in which a particular router or switch fails but also during events involving an attack on an entire network segment. A network administrator may choose to use a "hidden" master authoritative server and only have secondary servers visible on the network. A hidden master authoritative server is an authoritative DNS server whose IP address does not appear in the name server set for a zone. If the master authoritative name server is "hidden", a secondary authoritative name server may reside on the same network as the hidden master.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DNS configuration to determine all of the NS records for each zone. Based upon the NS records for each zone, determine location of each of the name servers. Verify all authoritative name servers are located on different network segments. If all authoritative name servers are not located on different network segments, this is a finding.

## Group: SRG-APP-000516-DNS-000089

**Group ID:** `V-214206`

### Rule: An authoritative name server must be configured to enable DNSSEC Resource Records.

**Rule ID:** `SV-214206r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The specification for a digital signature mechanism in the context of the DNS infrastructure is in IETF's DNSSEC standard. In DNSSEC, trust in the public key (for signature verification) of the source is established not by going to a third party or a chain of third parties (as in public key infrastructure [PKI] chaining), but by starting from a trusted zone (such as the root zone) and establishing the chain of trust down to the current source of response through successive verifications of signature of the public key of a child by its parent. The public key of the trusted zone is called the trust anchor. After authenticating the source, the next process DNSSEC calls for is to authenticate the response. DNSSEC mechanisms involve two main processes: sign and serve, and verify signature. Before a DNSSEC-signed zone can be deployed, a name server must be configured to enable DNSSEC processing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Validate that DNSSEC is enabled by navigating to Data Management >> DNS >> Grid DNS properties. Toggle Advanced Mode click on "DNSSEC" tab. When complete, click "Cancel" to exit the "Properties" screen. If "Enable DNSSEC" is not configured this is a finding.

## Group: SRG-APP-000516-DNS-000090

**Group ID:** `V-214207`

### Rule: Digital signature algorithm used for DNSSEC-enabled zones must be FIPS-compatible.

**Rule ID:** `SV-214207r612370_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The choice of digital signature algorithm will be based on recommended algorithms in well-known standards. NIST's Digital Signature Standard (DSS) [FIPS186] provides three algorithm choices: * Digital Signature Algorithm (DSA) * RSA * Elliptic Curve DSA (ECDSA). Of these three algorithms, RSA and DSA are more widely available and hence are considered candidates of choice for DNSSEC. In terms of performance, both RSA and DSA have comparable signature generation speeds, but DSA is much slower for signature verification. Hence, RSA is the recommended algorithm as far as this guideline is concerned. RSA with SHA-1 is currently the only cryptographic algorithm mandated to be implemented with DNSSEC, although other algorithm suites (i.e. RSA/SHA-256, ECDSA) are also specified. It can be expected that name servers and clients will be able to use the RSA algorithm at the minimum. It is suggested that at least one ZSK for a zone use the RSA algorithm. NIST's Secure Hash Standard (SHS) (FIPS 180-3) specifies SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 as approved hash algorithms to be used as part of the algorithm suite for generating digital signatures using the digital signature algorithms in NIST's DSS[FIPS186]. It is expected that there will be support for Elliptic Curve Cryptography in the DNSSEC. The migration path for USG DNSSEC operation will be to ECDSA (or similar) from RSA/SHA-1 and RSA/SHA-256 before September 30th, 2015.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Infoblox supports FIPS compliant DSA and RSA; SHA-1, SHA-256, and SHA-512 algorithms. Navigate to Data Management >> DNS >> Grid DNS properties. Toggle Advanced Mode click on "DNSSEC" tab. Validate that all Key Signing Keys (KSK) and Zone Signing Keys (ZSK) utilize FIPS approved algorithms. When complete, click "Cancel" to exit the "Properties" screen. If FIPS approved algorithms are not used for the Key Signing Keys (KSK) and Zone Signing Keys (ZSK), this is a finding.

## Group: SRG-APP-000516-DNS-000091

**Group ID:** `V-214208`

### Rule: For zones split between the external and internal sides of a network, the RRs for the external hosts must be separate from the RRs for the internal hosts.

**Rule ID:** `SV-214208r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authoritative name servers for an enterprise may be configured to receive requests from both external and internal clients. External clients need to receive RRs that pertain only to public services (public Web server, mail server, etc.) Internal clients need to receive RRs pertaining to public services as well as internal hosts. The zone information that serves the RRs on both the inside and the outside of a firewall should be split into different physical files for these two types of clients (one file for external clients and one file for internal clients).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
There are two primary configuration options for this requirement. 1. DNS Views allow a single zone to have two different data sets, with the response based on a client match list. If DNS Views are used and the client match list is validated, this is not a finding. 2. Review the Resource Records (RRs) of each zone which is split between external and internal networks. For those internal hosts which are intended to be accessed by both internal and external users, a different RR should be listed on each of the internal and external name servers, with IP addresses reflective of the external or internal network. Traffic destined for those internal hosts will resolve to the IP address in the external name server and then should be NATd through the perimeter firewall. If a different Resource Record (RR) is not listed on each of the internal and external name servers, this is a finding.

## Group: SRG-APP-000516-DNS-000092

**Group ID:** `V-214209`

### Rule: In a split DNS configuration, where separate name servers are used between the external and internal networks, the external name server must be configured to not be reachable from inside resolvers.

**Rule ID:** `SV-214209r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Instead of having the same set of authoritative name servers serve different types of clients, an enterprise could have two different sets of authoritative name servers. One set, called external name servers, can be located within a DMZ; these would be the only name servers that are accessible to external clients and would serve RRs pertaining to hosts with public services (Web servers that serve external Web pages or provide B2C services, mail servers, etc.) The other set, called internal name servers, is to be located within the firewall and should be configured so they are not reachable from outside and hence provide naming services exclusively to internal clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validation of this configuration item requires review of the network architecture and security configuration in addition to DNS server configuration to validate external name servers are not accessible from the internal network when a split DNS configuration is implemented. Navigate to Data Management >> DNS >> Members/Servers tab. Review both the network configuration, and access control of each Infoblox member which has the DNS service running. Select each grid member and click "Edit". Review the "Queries" tab to ensure both queries and recursion options are enabled and allowed only from the respective client networks. If a split DNS configuration is not utilized, this is not a finding. If there is no access control configured or access control does not restrict queries and recursion to the respective client network, this is a finding.

## Group: SRG-APP-000516-DNS-000093

**Group ID:** `V-214210`

### Rule: In a split DNS configuration, where separate name servers are used between the external and internal networks, the internal name server must be configured to not be reachable from outside resolvers.

**Rule ID:** `SV-214210r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Instead of having the same set of authoritative name servers serve different types of clients, an enterprise could have two different sets of authoritative name servers. One set, called external name servers, can be located within a DMZ; these would be the only name servers that are accessible to external clients and would serve RRs pertaining to hosts with public services (Web servers that serve external Web pages or provide B2C services, mail servers, etc.) The other set, called internal name servers, is to be located within the firewall and should be configured so they are not reachable from outside and hence provide naming services exclusively to internal clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validation of this configuration item requires review of the network architecture and security configuration in addition to DNS server configuration to validate internal name servers are not accessible from the external network when a split DNS configuration is implemented. Navigate to Data Management >> DNS >> Members/Servers tab. Review both the network configuration, and access control of each Infoblox member which has the DNS service running. Select each grid member and click "Edit". Review the "Queries" tab to ensure both queries and recursion options are enabled and allowed only from the respective client networks. If a split DNS configuration is not utilized, this is not a finding. If there is no access control configured or access control does not restrict queries and recursion to the respective client network, this is a finding.

## Group: SRG-APP-000516-DNS-000099

**Group ID:** `V-214211`

### Rule: The DNS implementation must enforce a Discretionary Access Control (DAC) policy that limits propagation of access rights.

**Rule ID:** `SV-214211r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the premise that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. In a DNS implementation, DAC should be granted to a minimal number of individuals and objects because DNS does not interact directly with users and users do not store and share data with the DNS application directly. The primary objective of DNS authentication and access control is the integrity of DNS records; only authorized personnel must be able to create and modify resource records, and name servers should only accept updates from authoritative master servers for the relevant zones. Integrity is best assured through authentication and access control features within the name server software and the file system the name server resides on. In order to protect the zone files and configuration data, which should only be accessed by the name service or an administrator, access controls need to be implemented on files, and rights should not be easily propagated to other users. Lack of a stringent access control policy places the DNS infrastructure at risk to malicious persons and attackers, in addition to potential denial of service to network resources. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. DAC models have the potential for the access controls to propagate without limit, resulting in unauthorized access to said objects. When applications provide a DAC mechanism, the DNS implementation must be able to limit the propagation of those access rights.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox utilizes a robust permission structure that provides for granular configuration of user access to the administrative interface. Review the Infoblox Overview document for more information on access control and inheritance. If an access policy limiting propagation of access rights is not configured, this is a finding.

## Group: SRG-APP-000516-DNS-000101

**Group ID:** `V-214212`

### Rule: The DNS implementation must implement internal/external role separation.

**Rule ID:** `SV-214212r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS servers with an internal role only process name/address resolution requests from within the organization (i.e., internal clients). DNS servers with an external role only process name/address resolution information requests from clients external to the organization (i.e., on the external networks, including the Internet). The set of clients that can access an authoritative DNS server in a particular role is specified by the organization using address ranges, explicit access control lists, etc. In order to protect internal DNS resource information, it is important to isolate the requests to internal DNS servers. Separating internal and external roles in DNS prevents address space that is private (e.g., 10.0.0.0/24) or is otherwise concealed by some form of Network Address Translation from leaking into the public DNS system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Infoblox Grid configuration to verify that the appropriate zones are served by the correct internal or external member. Review the usage of DNS views as necessary. Navigate to Data Management >> DNS >> Members/Servers and Zones tabs. Review each zone and member assignment to ensure it is configured correctly with respect to its network assignment. If an external server contains internal data, or vice versa, this is a finding.

## Group: SRG-APP-000516-DNS-000102

**Group ID:** `V-214213`

### Rule: The Infoblox system must utilize valid root name servers in the local root zone file.

**Rule ID:** `SV-214213r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All caching name servers must be authoritative for the root zone because, without this starting point, they would have no knowledge of the DNS infrastructure and thus would be unable to respond to any queries. The security risk is that an adversary could change the root hints and direct the caching name server to a bogus root server. At that point, every query response from that name server is suspect, which would give the adversary substantial control over the network communication of the name servers' clients. When authoritative servers are sent queries for zones that they are not authoritative for, and they are configured as a non-caching server (as recommended), they can either be configured to return a referral to the root servers or they can be configured to refuse to answer the query. The recommendation is to configure authoritative servers to refuse to answer queries for any zones for which they are not authoritative. This is more efficient for the server and allows it to spend more of its resources doing what its intended purpose is, answering authoritatively for its zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the entries within the root hints file and validate that the entries are correct. "G" and "H" root servers are required on the NIPRNet, as a minimum. All default settings on servers must be verified and corrected if necessary. If valid root name servers are not configured, this is a finding. Navigate Data Management >> DNS >> Grid DNS Properties. Toggle Advanced mode and review "Root Name Servers" tab to ensure it is configured correctly. Note: Validate against the current available DNS root list at the time of check.

## Group: SRG-APP-000516-DNS-000103

**Group ID:** `V-214214`

### Rule: The Infoblox NIOS version must be at the appropriate version.

**Rule ID:** `SV-214214r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Infoblox NIOS is updated on a regular basis to add feature support, implement bug fixes, and address security vulnerabilities. NIOS is a hardened system with no direct user access to the software components. The review of security vulnerabilities such as MITRE Common Vulnerabilities and Exposure (CVE) can be accomplished by review of the running system NIOS version and published security information. Review of specific or individual software component versions within NIOS is not sufficient validation, as Infoblox modifies these software components and may or may not be subject to vulnerabilities that exist in unmodified publicly available source code. Infoblox may support multiple versions of NIOS, each of which may address the same security vulnerability at different patch releases. It is not necessary for an Infoblox customer to run the highest possible version, rather they should run the supported version applicable to their environment and ensure it is patched to address all known vulnerabilities. Infoblox publishes security information within each NIOS version release notes and on the Infoblox Support Knowledge Base. Infoblox customers can also use the support portal to validate security questions and applicability of vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox systems utilize a modified version of BIND DNS software which adds features as well as addresses security issues outside of those provided by ISC. Infoblox systems are provided as a hardened appliance, and do not allow user access or upgrading of software components including BIND. The Infoblox support portal is the authoritative source to validate version and applicability of vulnerabilities. Verify the NIOS version by review of "Grid, Upgrade" tab to show all members are at the current version. Utilize the Infoblox support knowledgebase to obtain current version information. If Infoblox NIOS is not at the current approved version level, this is a finding.

## Group: SRG-APP-000516-DNS-000108

**Group ID:** `V-214215`

### Rule: The IP address for hidden master authoritative name servers must not appear in the name servers set in the zone database.

**Rule ID:** `SV-214215r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A hidden master authoritative server is an authoritative DNS server whose IP address does not appear in the name server set for a zone. All of the name servers that do appear in the zone database as designated name servers get their zone data from the hidden master via a zone transfer request. In effect, all visible name servers are actually secondary slave servers. This prevents potential attackers from targeting the master name server because its IP address may not appear in the zone database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Infoblox Grid Master should not be configured to service DNS requests from clients. Navigate to Data Management >> DNS >> Zones. Review each zone by selecting the zone and clicking "Edit", and selecting the "Name Servers" tab. If the Grid Master is a listed name server and not marked "Stealth", this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-214216`

### Rule: The platform on which the name server software is hosted must be configured to respond to DNS traffic only.

**Rule ID:** `SV-214216r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OS configuration practices as issued by the US Computer Emergency Response Team (US CERT) and the National Institute of Standards and Technology's (NIST's) National Vulnerability Database (NVD), based on identified vulnerabilities that pertain to the application profile into which the name server software fits, should be always followed. In particular, hosts that run the name server software should not provide any other services and therefore should be configured to respond to DNS traffic only. In other words, the only allowed incoming ports/protocols to these hosts should be 53/udp and 53/tcp. Outgoing DNS messages should be sent from a random port to minimize the risk of an attacker's guessing the outgoing message port and sending forged replies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default all services other than those required for management are disabled. Review the Infoblox Grid for extra services turned on and turn them off. Configuration of Out of Band (OOB) management can be enabled to separate DNS from management traffic if desired. Navigate to Grid >> Grid Manager >> Services tab. Click on each service which is running and review the Service Status of each member. If an external authoritative server is running any service other than DNS, this is a finding.

## Group: SRG-APP-000516-DNS-000110

**Group ID:** `V-214217`

### Rule: The platform on which the name server software is hosted must be configured to send outgoing DNS messages from a random port.

**Rule ID:** `SV-214217r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OS configuration practices as issued by the US Computer Emergency Response Team (US CERT) and the National Institute of Standards and Technology's (NIST's) National Vulnerability Database (NVD), based on identified vulnerabilities that pertain to the application profile into which the name server software fits, should be always followed. In particular, hosts that run the name server software should not provide any other services and therefore should be configured to respond to DNS traffic only. In other words, the only allowed incoming ports/protocols to these hosts should be 53/udp and 53/tcp. Outgoing DNS messages should be sent from a random port to minimize the risk of an attacker guessing the outgoing message port and sending forged replies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default Infoblox systems utilize a random port for both DNS queries and notify messages. Verify the default configuration is not overridden. Navigate to Data Management >> DNS >> Members/Servers tab. Review each server with the DNS service enabled. Select each server, click "Edit", toggle Advanced Mode and select General >> Advanced tab. Verify that the options under "Source Port Settings"; "Set static source UDP port for queries (not recommended)" and "Set static source UDP port for notify messages" use the default value of not enabled. If configuration of either of these values exists, this is a finding. When complete, click "Cancel" to exit the "Properties" screen.

## Group: SRG-APP-000516-DNS-000112

**Group ID:** `V-214218`

### Rule: The private keys corresponding to both the ZSK and the KSK must not be kept on the DNSSEC-aware primary authoritative name server when the name server does not support dynamic updates.

**Rule ID:** `SV-214218r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The private keys in the KSK and ZSK key pairs must be protected from unauthorized access. If possible, the private keys should be stored off-line (with respect to the Internet-facing, DNSSEC-aware name server) in a physically secure, non-network-accessible machine along with the zone file master copy. This strategy is not feasible in situations in which the DNSSEC-aware name server has to support dynamic updates. To support dynamic update transactions, the DNSSEC-aware name server (which usually is a primary authoritative name server) has to have both the zone file master copy and the private key corresponding to the zone-signing key (ZSK-private) online to immediately update the signatures for the updated RRsets. The private key corresponding to the key-signing key (KSK-private) can still be kept off-line.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. By default KSK and ZSK private keys are stored on the Grid Master within the Infoblox database. No clients should be permitted to utilize the Grid Master DNS service. Navigate to Data Management >> DNS >> Zones Review each zone by selecting the zone and clicking "Edit", and selecting the "Name Servers" tab. If the Grid Master is a listed name server and not marked "Stealth", this is a finding. If a Hardware Security Module (HSM) is configured, KSK and ZSK private keys are encrypted and stored on the HSM, this is not a finding.

## Group: SRG-APP-000516-DNS-000114

**Group ID:** `V-214219`

### Rule: CNAME records must not point to a zone with lesser security for more than six months.

**Rule ID:** `SV-214219r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of CNAME records for exercises, tests, or zone-spanning aliases should be temporary (e.g., to facilitate a migration). When a host name is an alias for a record in another zone, an adversary has two points of attack: the zone in which the alias is defined and the zone authoritative for the alias's canonical name. This configuration also reduces the speed of client resolution because it requires a second look-up after obtaining the canonical name. Furthermore, in the case of an authoritative name server, this information is promulgated throughout the enterprise to caching servers and thus compounds the vulnerability. The exceptions are glue records supporting zone delegations, CNAME records supporting a system migration, or CNAME records that point to third-party Content Delivery Networks (CDN) or cloud computing platforms. In the case of third-party CDNs or cloud offerings, an approved mission need must be demonstrated (AO approval of use of a commercial cloud offering would satisfy this requirement). Additional exceptions are CNAME records in a multi-domain Active Directory environment pointing to hosts in other internal domains in the same multi-domain environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox DNS records the creation date of every resource record, including CNAME records in the system and the TimeStamp is attached to the CNAME object. Infoblox can also record the date when the last time this record was used or queried. CNAME records can be removed by the admin when they reach their 6 month maturity date. Navigate to Grid Manager >> Administration >> Logs >> Audit Log >> Filter >> Object Type=CNAME Record, + Action=CREATED, + TimeStamp=Before=6months Ago If there are zone-spanning CNAME records older than 6 months and the CNAME records resolve to anything other than fully qualified domain names for glue records supporting zone delegations, CNAME records supporting a system migration, or CNAME records that point to third-party Content Delivery Networks (CDN) or cloud computing platforms with an AO-approved and documented mission need, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-214220`

### Rule: The Infoblox system must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-214220r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements. Configuring the DNS server implementation to follow organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Infoblox systems are secure by design and utilize a number of access controls to prevent unauthorized usage. Infoblox systems are purpose built and do not provide privileged "root" level access, nor are they distributed as general purpose operating systems. By default all services including DNS are disabled on Infoblox systems. Services are enabled only as a result of administrator action. If any unnecessary services are running on Infoblox systems, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-214221`

### Rule: The Infoblox system must be configured to display the appropriate security classification information.

**Rule ID:** `SV-214221r612370_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuration of the informational banner displays the security classification of the Infoblox system using both color and text. Text may be added for additional security markings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the Infoblox Grid Master. The appropriate security classification color and text must be displayed on the top of each configuration screen. The output will also contain the text "Dynamic Page - Highest Possible Classification Is" and a colored bar with the classification. Additional text may appear if configured by the administrator. If the security classification color and text are not displayed at the top of each configuration screen, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-214222`

### Rule: The Infoblox system must be configured with the approved DoD notice and consent banner.

**Rule ID:** `SV-214222r612370_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuration of the DoD notice and consent banner requires all administrators to acknowledge the current DoD notice and consent by clicking an "Accept" button.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigation to the HTTPS interface on the Grid Master using a web browser will display the current DoD banner. The banner text of the document MUST read: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the correct banner is not displayed, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-214223`

### Rule: Infoblox Grid configuration must be backed up on a regular basis.

**Rule ID:** `SV-214223r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Infoblox Grid Master is the central point of management within an Infoblox Grid. The Grid Master retains a full copy of the configuration used for the entire Grid. In the event of system failure, a configuration backup must be preserved. An Infoblox member may also be configured as a Grid Master Candidate which is a synchronized to the Grid Master. The Candidate can be promoted in the event of system failure on the Grid Master.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Grid >> Grid Manager >> Members tab. In the toolbar click the drop-down menu for "Backup", "Schedule Backup". Verify configuration of a remote backup option (TFTP, FTP, or SCP). Review the existence of backup files on the remote system. If a remote backup system is not configured, or a local backup procedure is not documented, this is a finding. If no remote or local backup is configured, but the Grid contains a Grid Master candidate, the severity of the finding is reduced.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-214224`

### Rule: Infoblox systems must be configured with current DoD password restrictions.

**Rule ID:** `SV-214224r612370_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Infoblox systems must be configured to meet current DoD password policy when using the Infoblox Local User Database as the authentication source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Administration >> Administrators >> Authentication Policy. If the only authentication type under "Authenticate users in this order" is "Local User Database", perform the following additional validation: Navigate to Grid >> Grid Manager >> Grid Properties >> Password tab. Verify the settings are configured in accordance with current DoD Policy. If the Infoblox system is configured to utilize a remote authentication system (Active Directory, RADIUS, TACACS+, or LDAP) which enforces policy, or the password settings meet current guidance this is not a finding.

## Group: SRG-APP-000142-DNS-000014

**Group ID:** `V-214225`

### Rule: The DHCP service must not be enabled on an external authoritative name server.

**Rule ID:** `SV-214225r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The site DNS and DHCP architecture must be reviewed to ensure only the appropriate services are enabled on each Grid Member. An external authoritative name server must be configured to allow only authoritative DNS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Grid >> Grid Manager >> Services tab. Select "DHCP" and verify only internal Infoblox members have the service enabled. If an external authoritative name server has DHCP enabled this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-214226`

### Rule: A secure Out Of Band (OOB) network must be utilized for management of Infoblox Grid Members.

**Rule ID:** `SV-214226r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Infoblox Grid Master is the central point of management within an Infoblox Grid. The Grid Master retains a full copy of the configuration used for the entire Grid. The Grid Master should communicate to Grid Members using their Management port connected to an Out Of Band (OOB) network which clients cannot access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For Infoblox DNS systems on a Classified network, this requirement is Not Applicable. Navigate to Grid >> Grid Manager >> Members tab. Review the Grid Master network configuration and verify placement on an OOB network. Review services enabled on the Grid Master and verify that no client services are enabled. The only acceptable service allowed is DNS when the Grid utilizes DNSSEC signed zones. The Grid Master must have DNS enabled to sign DNSSEC zones. If DNSSEC is enabled, verify that the Grid Master marked as "Stealth" for any zone. If an Infoblox Grid Member does not utilize the MGMT port for configuration through an OOB connection, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-219058`

### Rule: All authoritative name servers for a zone must be geographically disbursed.

**Rule ID:** `SV-219058r612370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to network-based dispersion, authoritative name servers should be dispersed geographically as well. In other words, in addition to being located on different network segments, the authoritative name servers should not all be located within the same building. One approach that some organizations follow is to locate some authoritative name servers in their own premises and others in their ISPs' data centers or in partnering organizations. A network administrator may choose to use a "hidden" master authoritative server and only have secondary servers visible on the network. A hidden master authoritative server is an authoritative DNS server whose IP address does not appear in the name server set for a zone. If the master authoritative name server is "hidden", a secondary authoritative name server may reside in the same building as the hidden master.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the NS records for each zone hosted and confirm that each authoritative name server is located at a different physical location than the remaining name servers. Infoblox supports designation as a "stealth" name server, which will not have a NS record. If all name servers, for which NS records are listed, are not physically at different locations, this is a finding.

