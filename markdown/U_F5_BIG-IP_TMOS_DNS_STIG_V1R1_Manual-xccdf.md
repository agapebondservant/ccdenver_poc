# STIG Benchmark: F5 BIG-IP TMOS DNS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000383-DNS-000047

**Group ID:** `V-265980`

### Rule: The F5 BIG-IP DNS implementation must prohibit recursion on authoritative name servers.

**Rule ID:** `SV-265980r1024486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A potential vulnerability of DNS is that an attacker can poison a name server's cache by sending queries that will cause the server to obtain host-to-IP address mappings from bogus name servers that respond with incorrect information. Once a name server has been poisoned, legitimate clients may be directed to nonexistent hosts (which constitutes a denial of service), or worse, hosts that masquerade as legitimate ones to obtain sensitive data or passwords. To guard against poisoning, name servers authoritative for .mil domains must be separated functionally from name servers that resolve queries on behalf of internal clients. Organizations may achieve this separation by dedicating machines to each function or, if possible, by running two instances of the name server software on the same machine: one for the authoritative function and the other for the resolving function. In this design, each name server process may be bound to a different IP address or network interface to implement the required segregation. DNSSEC ensures that the answer received when querying for name resolution actually comes from a trusted name server. Since DNSSEC is still far from being globally deployed external to DOD, and many resolvers either have not been updated or do not support DNSSEC, maintaining cached zone data separate from authoritative zone data mitigates the gap until all DNS data is validated with DNSSEC. Since DNS forwarding of queries can be accomplished in some DNS applications without caching locally, DNS forwarding is the method to be used when providing external DNS resolution to internal clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP does not have the role of authoritative DNS server, this is not applicable. From the BIG-IP GUI: 1. DNS. 2. Delivery. 3. Profiles. 4. DNS. 5. Click the name of the profile used for the authoritative listener. 6. Verify the following settings: a. Use BIND Server on BIG-IP: Disabled b. DNS Cache: Disabled If the BIG-IP appliance is not configured to prohibit recursion on authoritative name servers, this is a finding.

## Group: SRG-APP-000516-DNS-000078

**Group ID:** `V-265981`

### Rule: The validity period for the RRSIGs covering a zone's DNSKEY RRSet must be no less than two days and no more than one week.

**Rule ID:** `SV-265981r1024487_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The best way for a zone administrator to minimize the impact of a key compromise is by limiting the validity period of RRSIGs in the zone and in the parent zone. This strategy limits the time during which an attacker can take advantage of a compromised key to forge responses. An attacker that has compromised a ZSK can use that key only during the KSK's signature validity interval. An attacker that has compromised a KSK can use that key for only as long as the signature interval of the RRSIG covering the DS RR in the delegating parent. These validity periods must be short, which will require frequent re-signing. To minimize the impact of a compromised ZSK, a zone administrator must set a signature validity period of one week for RRSIGs covering the DNSKEY RRSet in the zone (the RRSet that contains the ZSK and KSK for the zone). The DNSKEY RRSet can be re-signed without performing a ZSK rollover, but scheduled ZSK rollover must still be performed at regular intervals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
KSK validity period: From the BIG-IP GUI: 1. DNS. 2. Delivery. 3. Keys. 4. DNSSEC Key List. 5. Click the Name of the KSK. 6. Verify the "Signature Validity Period" is between two and seven days. ZSK validity period: From the BIG-IP GUI: 1. DNS. 2. Delivery. 3. Keys. 4. DNSSEC Key List. 5. Click the Name of the ZSK. 6. Verify the "Signature Validity Period" is between two and seven days. If the BIG-IP appliance is not configured with a validity period for the RRSIGs covering a zones DNSKEY RRSet of no less than two days and no more than one week, this is a finding.

## Group: SRG-APP-000516-DNS-000089

**Group ID:** `V-265982`

### Rule: An authoritative name server must be configured to enable DNSSEC Resource Records.

**Rule ID:** `SV-265982r1024488_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The specification for a digital signature mechanism in the context of the DNS infrastructure is in IETF's DNSSEC standard. In DNSSEC, trust in the public key (for signature verification) of the source is established not by going to a third party or a chain of third parties (as in public key infrastructure [PKI] chaining), but by starting from a trusted zone (such as the root zone) and establishing the chain of trust down to the current source of response through successive verifications of signature of the public key of a child by its parent. The public key of the trusted zone is called the trust anchor. After authenticating the source, the next process DNSSEC calls for is to authenticate the response. DNSSEC mechanisms involve two main processes: sign and serve, and verify signature. Before a DNSSEC-signed zone can be deployed, a name server must be configured to enable DNSSEC processing. Satisfies: SRG-APP-000516-DNS-000089, SRG-APP-000347-DNS-000041, SRG-APP-000348-DNS-000042, SRG-APP-000420-DNS-000053, SRG-APP-000421-DNS-000054, SRG-APP-000158-DNS-000015, SRG-APP-000422-DNS-000055, SRG-APP-000215-DNS-000003, SRG-APP-000423-DNS-000056, SRG-APP-000424-DNS-000057, SRG-APP-000425-DNS-000058, SRG-APP-000426-DNS-000059, SRG-APP-000219-DNS-000030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
DNSSEC Keys: From the BIG-IP GUI: 1. DNS. 2. Zones. 3. DNSSEC Zones. 4. DNSSEC Zone List. 5. Click the name of the zone. 6. Verify a key is selected for both "Zone Signing Key" and "Key Signing Key". TSIG Key: 1. DNS. 2. Delivery. 3. Nameservers. 4. Nameserver List. 5. Click the name of the Nameserver. 6. Verify a value is selected for "TSIG Key". If the BIG-IP DNS implementation is not configured to enable DNSSEC Resource Records, this is a finding.

## Group: SRG-APP-000516-DNS-000095

**Group ID:** `V-265983`

### Rule: Primary authoritative name servers must be configured to only receive zone transfer requests from specified secondary name servers.

**Rule ID:** `SV-265983r1024490_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authoritative name servers (especially primary name servers) must be configured with an allow-transfer access control substatement designating the list of hosts from which zone transfer requests can be accepted. These restrictions address the denial-of-service (DoS) threat and potential exploits from unrestricted dissemination of information about internal resources. Based on the need-to-know, the only name servers that need to refresh their zone files periodically are the secondary name servers. Zone transfer from primary name servers must be restricted to secondary name servers. The zone transfer must be completely disabled in the secondary name servers. The address match list argument for the allow-transfer substatement must consist of IP addresses of secondary name servers and stealth secondary name servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP is transferring zones from another non-BIG-IP DNS server perform the following. From the BIG-IP GUI: 1. DNS. 2. Zones. 3. Zone List. 4. Click on the name of the Zone. 5. Verify "Zone Transfer Clients" >> "Active" column shows only the nameservers that are allowed to request zone transfers. If the BIG-IP appliance is not configured to limit the secondary name servers from which an authoritative name server receives zone transfer requests, this is a finding.

## Group: SRG-APP-000516-DNS-000102

**Group ID:** `V-265984`

### Rule: The F5 BIG-IP DNS must use valid root name servers in the local root zone file.

**Rule ID:** `SV-265984r1024858_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All caching name servers must be authoritative for the root zone because, without this starting point, they would have no knowledge of the DNS infrastructure and thus would be unable to respond to any queries. The security risk is that an adversary could change the root hints and direct the caching name server to a bogus root server. At that point, every query response from that name server is suspect, which would give the adversary substantial control over the network communication of the name servers' clients. When authoritative servers are sent queries for zones that they are not authoritative for, and they are configured as a noncaching server (as recommended), they can either be configured to return a referral to the root servers or they can be configured to refuse to answer the query. The recommendation is to configure authoritative servers to refuse to answer queries for any zones for which they are not authoritative. This is more efficient for the server and allows it to spend more of its resources doing what its intended purpose is, answering authoritatively for its zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is only applicable if DNS recursion is being performed by the BIG-IP AND a custom root hint list must be defined. From the BIG-IP GUI: 1. DNS. 2. Zones. 3. ZoneRunner. 4. Zone List. 5. Verify there is no Zone Name called ".". 6. If a "." Zone Name exists, log in to the BIG-IP CLI and run the following commands: cat /var/named/config/namedb/db.external.named.root. 7. Verify valid root name servers are configured. If the BIG-IP appliance is not configured to use valid root name servers in the local root zone file, this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-265985`

### Rule: The platform on which the name server software is hosted must be configured to respond to DNS traffic only.

**Rule ID:** `SV-265985r1024493_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Hosts that run the name server software must not provide any other services and therefore must be configured to respond to DNS traffic only. In other words, the only allowed incoming ports/protocols to these hosts must be 53/udp and 53/tcp. Outgoing DNS messages must be sent from a random port to minimize the risk of an attacker's guessing the outgoing message port and sending forged replies. BIG-IP is often used to proxy DNS along with other services. The requirement speaks to the "name server software", but if we are proxying for the name server then we do not need to limit listeners to DNS only.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP does not have the role of authoritative DNS server, this is not applicable. From the BIG-IP GUI: 1. Local Traffic. 2. Virtual Servers. 3. Verify the list of virtual servers are not configured to listen for non-DNS services. If the BIG-IP appliance is configured to respond traffic other than DNS, this is a finding.

## Group: SRG-APP-000516-DNS-000090

**Group ID:** `V-265986`

### Rule: The digital signature algorithm used for DNSSEC-enabled zones must be set to use RSA/SHA256 or RSA/SHA512.

**Rule ID:** `SV-265986r1024860_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The choice of digital signature algorithm will be based on recommended algorithms in well-known standards. NIST's Digital Signature Standard (DSS) (FIPS186) provides three algorithm choices: - Digital Signature Algorithm (DSA); - RSA; - Elliptic Curve DSA (ECDSA). Of these three algorithms, RSA and DSA are more widely available, and hence are considered candidates of choice for DNSSEC. In terms of performance, both RSA and DSA have comparable signature generation speeds, but DSA is much slower for signature verification. Hence, RSA is the recommended algorithm as far as this guideline is concerned. RSA with SHA-1 is currently the only cryptographic algorithm mandated to be implemented with DNSSEC, although other algorithm suites (e.g., RSA/SHA-256, ECDSA) are also specified. It can be expected that name servers and clients will be able to use the RSA algorithm at the minimum. It is suggested that at least one ZSK for a zone use the RSA algorithm. SHA-256, SHA-384, and SHA-512 are approved hash algorithms to be used as part of the algorithm suite for generating digital signatures. It is expected that there will be support for Elliptic Curve Cryptography in the DNSSEC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify automatically managed zone-signing keys for BIG-IP DNS to use in the DNSSEC authentication process have been configured. On the Main tab, click "DNS Delivery Keys DNSSEC Key List". The DNSSEC Key List screen opens. If the Digital signature algorithm used for DNSSEC-enabled zones is not set to use RSA/SHA256 or RSASHA512, this is a finding.

## Group: SRG-APP-000349-DNS-000043

**Group ID:** `V-265987`

### Rule: The F5 BIG-IP DNS server implementation must validate the binding of the other DNS server's identity to the DNS information for a server-to-server transaction (e.g., zone transfer).

**Rule ID:** `SV-265987r1024862_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Validation of the binding of the information prevents the modification of information between production and review. The validation of bindings can be achieved, for example, by the use of cryptographic checksums. Validations must be performed automatically. DNSSEC and TSIG/SIG(0) technologies are not effective unless the digital signatures they generate are validated to ensure that the information has not been tampered with and that the producer's identity is legitimate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. DNS. 2. Delivery. 3. Nameservers. 4. Click the Name of the Nameserver. 5. Verify that a value is selected for "TSIG Key". If the BIG-IP appliance is not configured to validate the binding of the other DNS server's identity to the DNS information for a server-to-server transaction (e.g., zone transfer), this is a finding.

## Group: SRG-APP-000213-DNS-000024

**Group ID:** `V-265988`

### Rule: A BIG-IP DNS server implementation must provide additional data origin artifacts along with the authoritative data the system returns in response to external name/address resolution queries.

**Rule ID:** `SV-265988r1024496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The underlying feature in the major threat associated with DNS query/response (e.g., forged response or response failure) is the integrity of DNS data returned in the response. The security objective is to verify the integrity of each response received. An integral part of integrity verification is to ensure that valid data has originated from the right source. Establishing trust in the source is called data origin authentication. The security objectives—and consequently the security services—that are required for securing the DNS query/response transaction are data origin authentication and data integrity verification. The specification for a digital signature mechanism in the context of the DNS infrastructure is in IETF’s DNSSEC standard. In DNSSEC, trust in the public key (for signature verification) of the source is established not by going to a third party or a chain of third parties (as in public key infrastructure [PKI] chaining), but by starting from a trusted zone (such as the root zone) and establishing the chain of trust down to the current source of response through successive verifications of signature of the public key of a child by its parent. The public key of the trusted zone is called the trust anchor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP Console, type the following commands: Note: Assuming you are checking a DNSSEC Zone, from the command line of a management computer, run: dig +dnssec @<DNS Server IP> <DNSSEC zonename> #verify the existence of an RRSET for each zone, which will include, at a minimum, an RRType RRSIG (Resource Record Signature) as well as an RRType DNSKEY and RRType NSEC (Next Secure). DNS Profile: From the BIG-IP GUI: 1. DNS. 2. Delivery. 3. Profiles. 4. DNS. 5. Click the name of the DNS profile being used by the listener. 6. Under DNS Features verify "DNSSEC" is set to "Enabled". If the BIG-IP DNS appliance is not configured to provide additional data origin artifacts along with the authoritative data the system returns in response to external name/address resolution queries, this is a finding.

## Group: SRG-APP-000214-DNS-000079

**Group ID:** `V-265989`

### Rule: The validity period for the RRSIGs covering the DS RR for a zones delegated children must be no less than two days and no more than one week.

**Rule ID:** `SV-265989r1024498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The best way for a zone administrator to minimize the impact of a key compromise is by limiting the validity period of RRSIGs in the zone and in the parent zone. This strategy limits the time during which an attacker can take advantage of a compromised key to forge responses. An attacker that has compromised a ZSK can use that key only during the KSK's signature validity interval. An attacker that has compromised a KSK can use that key for only as long as the signature interval of the RRSIG covering the DS RR in the delegating parent. These validity periods must be short, which will require frequent resigning. To prevent the impact of a compromised KSK, a delegating parent must set the signature validity period for RRSIGs covering DS RRs in the range of a few days to one week. This resigning does not require frequent rollover of the parent's ZSK, but scheduled ZSK rollover must still be performed at regular intervals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
KSK validity period From the BIG-IP GUI: 1. DNS. 2. Delivery. 3. Keys. 4. DNSSEC Key List. 5. Click the Name of the KSK. 6. Verify the "Signature Validity Period" is between two and seven days. ZSK validity period From the BIG-IP GUI: 1. DNS. 2. Delivery. 3. Keys. 4. DNSSEC Key List. 5. Click the name of the ZSK. 6. Verify the "Signature Validity Period" is between two and seven days. If the BIG-IP appliance is not configured with a validity period for the RRSIGs covering a zones DNSKEY RRSet of no less than two days and no more than one week, this is a finding.

## Group: SRG-APP-000219-DNS-000028

**Group ID:** `V-265990`

### Rule: The F5 BIG-IP DNS implementation must protect the authenticity of communications sessions for zone transfers.

**Rule ID:** `SV-265990r1024864_rule`
**Severity:** high

**Description:**
<VulnDiscussion>DNS is a fundamental network service that is prone to various attacks, such as cache poisoning and man-in-the middle attacks. If communication sessions are not provided appropriate validity protections, such as the employment of DNSSEC, the authenticity of the data cannot be guaranteed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP is transferring zones from another non-BIG-IP DNS server perform the following. From the BIG-IP GUI: 1. DNS. 2. Zones. 3. Click on the Zone Name. 4. Under the TSIG section verify a "Server Key" is selected. From the BIG-IP Console, type the following commands: tmsh list ltm dns zone <name> server-tsig-key Note: Must return a value other than "none". If the BIG-IP appliance is not configured to protect the authenticity of communications sessions for zone transfers, this is a finding.

## Group: SRG-APP-000247-DNS-000036

**Group ID:** `V-265991`

### Rule: The F5 BIG-IP DNS server implementation must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-265991r1024501_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. In the case of application DoS attacks, care must be taken when designing the application to ensure the application makes the best use of system resources. SQL queries have the potential to consume large amounts of CPU cycles if they are not tuned for optimal performance. Web services containing complex calculations requiring large amounts of time to complete can bog down if too many requests for the service are encountered within a short period of time. A DoS attack against the DNS infrastructure has the potential to cause a DoS to all network users. As the DNS is a distributed backbone service of the internet, various forms of amplification attacks resulting in DoS, while using the DNS, are still prevalent on the internet today. Some potential DoS flooding attacks against the DNS include malformed packet flood, spoofed source addresses, and distributed DoS. Without the DNS, users and systems would not have the ability to perform simple name-to-IP resolution. Configuring the DNS implementation to defend against cache poisoning, employing increased capacity and bandwidth, building redundancy into the DNS architecture, using DNSSEC, limiting and securing recursive services, DNS black holes, etc., may reduce the susceptibility to some flooding types of DoS attacks. Satisfies: SRG-APP-000247-DNS-000036, SRG-APP-000246-DNS-000035</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. DoS Protection. 3. Device Protection. 4. Expand DNS and verify the "State" is set to "Mitigate" for all signatures. If the BIG-IP appliance is not configured to restrict the ability of individuals to use the DNS server to launch DoS attacks against other information systems, this is a finding.

