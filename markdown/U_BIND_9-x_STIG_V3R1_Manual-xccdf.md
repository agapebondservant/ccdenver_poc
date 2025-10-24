# STIG Benchmark: BIND 9.x Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DNS-000001

**Group ID:** `V-272364`

### Rule: A BIND 9.x primary name server must limit the number of concurrent zone transfers between authorized secondary name servers.

**Rule ID:** `SV-272364r1124029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of concurrent sessions reduces the risk of denial of service (DoS) to the DNS implementation. Name servers do not have direct user connections but accept client connections for queries. Original restriction on client connections should be high enough to prevent a self-imposed DoS, after which the connections are monitored and fine-tuned to best meet the organization's specific requirements. Primary name servers also make outbound connection to secondary name servers to provide zone transfers and accept inbound connection requests from clients wishing to provide a dynamic update. Primary name servers should explicitly limit zone transfers to only be made to designated secondary name servers. Because zone transfers involve the transfer of entire zones and use TCP connections, they place substantial demands on network resources relative to normal DNS queries. Errant or malicious frequent zone transfer requests on the name servers of the enterprise can overload the primary zone server and result in DoS to legitimate users. Primary name servers should be configured to limit the hosts from which they will accept dynamic updates. Additionally, the number of concurrent clients, especially TCP clients, needs to be kept to a level that does not risk placing the system in a DoS state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is not a primary name server, this requirement is not applicable. Verify that the name server is configured to limit the number of zone transfers from authorized secondary name servers. Inspect the "named.conf" file for the following: server <ip_address> { transfers 2; }; If each "server" statement does not contain a "transfers" sub-statement, this is a finding. If the transfers value is greater than three, this is a finding.

## Group: SRG-APP-000001-DNS-000001

**Group ID:** `V-272365`

### Rule: The BIND 9.x secondary name server must limit the number of zones requested from a single primary name server.

**Rule ID:** `SV-272365r1124031_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of concurrent sessions reduces the risk of denial of service (DoS) to the DNS implementation. Name servers do not have direct user connections but accept client connections for queries. Original restriction on client connections should be high enough to prevent a self-imposed DoS, after which the connections are monitored and fine-tuned to best meet the organization's specific requirements. Primary name servers also make outbound connection to secondary name servers to provide zone transfers and accept inbound connection requests from clients wishing to provide a dynamic update. Primary name servers should explicitly limit zone transfers to only be made to designated secondary name servers. Because zone transfers involve the transfer of entire zones and use TCP connections, they place substantial demands on network resources relative to normal DNS queries. Errant or malicious frequent zone transfer requests on the name servers of the enterprise can overload the primary zone server and result in DoS to legitimate users. Primary name servers should be configured to limit the hosts from which they will accept dynamic updates. Additionally, the number of concurrent clients, especially TCP clients, needs to be kept to a level that does not risk placing the system in a DoS state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is not a secondary name server, this requirement is not applicable. Verify that the secondary name server is configured to limit the number of zones requested from a single primary name server. Inspect the "named.conf" file for the following: options { transfers-per-ns 2; }; If the "options" statement does not contain a "transfers-per-ns" sub-statement, this is a finding. If the transfers-per-ns value is greater than three, this is a finding.

## Group: SRG-APP-000001-DNS-000001

**Group ID:** `V-272366`

### Rule: The BIND 9.x secondary name server must limit the total number of zones the name server can request at any one time.

**Rule ID:** `SV-272366r1124033_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of concurrent sessions reduces the risk of denial of service (DoS) to the DNS implementation. Name servers do not have direct user connections but accept client connections for queries. Original restriction on client connections should be high enough to prevent a self-imposed denial of service, after which the connections are monitored and fine-tuned to best meet the organization's specific requirements. Primary name servers also make outbound connection to secondary name servers to provide zone transfers and accept inbound connection requests from clients wishing to provide a dynamic update. Primary name servers should explicitly limit zone transfers to only be made to designated secondary name servers. Because zone transfers involve the transfer of entire zones and use TCP connections, they place substantial demands on network resources relative to normal DNS queries. Errant or malicious frequent zone transfer requests on the name servers of the enterprise can overload the Primary zone server and result in DoS to legitimate users. Primary name servers should be configured to limit the hosts from which they will accept dynamic updates. Additionally, the number of concurrent clients, especially TCP clients, needs to be kept to a level that does not risk placing the system in a DoS state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is not a secondary name server, this requirement is not applicable. Verify the name server is configured to limit the total number of zones that can be requested at one time. Inspect the "named.conf" file for the following: options { transfers-in 10; }; If the "options" statement does not contain a "transfers-in" sub-statement, this is a finding.

## Group: SRG-APP-000001-DNS-000115

**Group ID:** `V-272367`

### Rule: The BIND 9.x server implementation must limit the number of concurrent session client connections.

**Rule ID:** `SV-272367r1123978_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of concurrent sessions reduces the risk of denial of service (DoS) to the DNS implementation. Name servers do not have direct user connections but accept client connections for queries. Original restriction on client connections should be high enough to prevent a self-imposed denial of service, after which the connections are monitored and fine-tuned to best meet the organization's specific requirements. Primary name servers also make outbound connections to secondary name servers to provide zone transfers and accept inbound connection requests from clients wishing to provide a dynamic update. Primary name servers should explicitly limit zone transfers to only be made to designated secondary name servers. Because zone transfers involve the transfer of entire zones and use TCP connections, they place substantial demands on network resources relative to normal DNS queries. Errant or malicious frequent zone transfer requests on the name servers of the enterprise can overload the primary zone server and result in DoS to legitimate users. Primary name servers should be configured to limit the hosts from which they will accept dynamic updates. Additionally the number of concurrent clients, especially TCP clients, needs to be kept to a level that does not risk placing the system in a DoS state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the name server is configured to limit the number of concurrent client connections: Inspect the "named.conf" file for the following: options { transfers-out 10; }; If the "options" statement does not contain a "transfers-out" sub-statement, this is a finding.

## Group: SRG-APP-000095-DNS-000006

**Group ID:** `V-272368`

### Rule: The print-severity variable for the configuration of BIND 9.x server logs must be configured to produce audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-272368r1123822_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. It is essential for security personnel to know what is being performed on the system, where an event occurred, when an event occurred, and by whom the event was triggered, to compile an accurate risk assessment. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or to simply identify an improperly configured DNS implementation. Without log records that aid in the establishment of what types of events occurred and when those events occurred, there is no traceability for forensic or analytical purposes, and the cause of events is severely hindered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each logging channel that is defined, verify that the "print-severity" substatement is listed. Inspect the "named.conf" file for the following: logging { channel channel_name { print-severity yes; }; }; If the "print-severity" statement is missing, this is a finding. If the "print-severity" statement is not set to "yes", this is a finding.

## Group: SRG-APP-000096-DNS-000007

**Group ID:** `V-272369`

### Rule: The print-time variable for the configuration of BIND 9.x server logs must be configured to establish when (date and time) the events occurred.

**Rule ID:** `SV-272369r1123825_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events relating to an incident. Associating event types with detected events in the application and audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured application. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know when events occurred (date and time).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each logging channel that is defined, verify that the "print-time" substatement is listed. Inspect the "named.conf" file for the following: logging { channel channel_name { print-time yes; }; }; If the "print-time" statement is missing, this is a finding. If the "print-time" statement is not set to "yes", this is a finding.

## Group: SRG-APP-000097-DNS-000008

**Group ID:** `V-272370`

### Rule: The print-category variable for the configuration of BIND 9.x server logs must be configured to record information indicating which process generated the events.

**Rule ID:** `SV-272370r1123423_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events relating to an incident. Associating information about where the event occurred within the application provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured application. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as application components, modules, session identifiers, filenames, host names, and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each logging channel that is defined, verify that the "print-category" sub statement is listed. Inspect the "named.conf" file for the following: logging { channel channel_name { print-category yes; }; }; If the "print-category" statement is missing, this is a finding. If the "print-category" statement is not set to "yes", this is a finding.

## Group: SRG-APP-000089-DNS-000004

**Group ID:** `V-272371`

### Rule: A BIND 9.x server implementation must be configured to allow DNS administrators to audit all DNS server components based on selectable event criteria and produce audit records within all DNS server components that contain information for failed security verification tests, information to establish the outcome and source of the events, any information necessary to determine cause of failure, and any information necessary to return to operations with least disruption to mission processes.

**Rule ID:** `SV-272371r1124008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. The actual auditing is performed by the OS/NDM, but the configuration to trigger the auditing is controlled by the DNS server. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. The DOD has defined the list of events for which the application will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. The DOD has defined the data which the application will provide an audit record generation capability for an event as the following: (i) Establish the source of the event; (ii) The outcome of the event; and (iii) Identify the application itself as the source of the event. Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. Associating information about the source of the event within the application provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured application. Without information about the outcome of events, security personnel cannot make an accurate assessment about whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving application state information helps to facilitate application restart and return to the operational mode of the organization with less disruption to mission-essential processes. The DNS server should be configured to generate audit records whenever a self-test fails. The OS/NDM is responsible for generating notification messages related to this audit record. If authorized individuals do not have the ability to modify auditing parameters in response to a changing threat environment, the organization may not be able to effectively respond, and important forensic information may be lost. This requirement enables organizations to extend or limit auditing as necessary to meet organizational requirements. Auditing that is limited to conserve information system resources may be extended to address certain threat situations. In addition, auditing may be limited to a specific set of events to facilitate audit reduction, analysis, and reporting. Organizations can establish time thresholds in which audit actions are changed, for example, near real-time, within minutes, or within hours. In addition to logging where events occur within the application, the application must also produce audit records that identify the application itself as the source of the event. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event, particularly in the case of centralized logging. In the case of centralized logging, the source would be the application name accompanied by the host or client name. Satisfies: SRG-APP-000089-DNS-000004, SRG-APP-000098-DNS-000009, SRG-APP-000099-DNS-000010, SRG-APP-000275-DNS-000040, SRG-APP-000226-DNS-000032</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the name server is configured to generate audit records: Inspect the "named.conf" file for the following: logging { channel channel_name { severity info; print-time yes; print-category yes; print-severity yes; }; category default { channel_name; }; }; If there is no "logging" statement, this is a finding. If the "logging" statement does not contain a "channel", this is a finding. If the "logging" statement does not contain a "category" that uses a "channel", this is a finding.

## Group: SRG-APP-000176-DNS-000094

**Group ID:** `V-272372`

### Rule: The BIND 9.x server private key corresponding to the zone-signing key (ZSK) pair must be the only DNSSEC key kept on a name server that supports dynamic updates.

**Rule ID:** `SV-272372r1123853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The private key in the ZSK key pair must be protected from unauthorized access. If possible, the private key should be stored offline (with respect to the internet-facing, DNSSEC-aware name server) in a physically secure, nonnetwork-accessible machine along with the zone file primary copy. This strategy is not feasible in situations in which the DNSSEC-aware name server has to support dynamic updates. To support dynamic update transactions, the DNSSEC-aware name server (which usually is a primary authoritative name server) has to have both the zone file primary copy and the private key corresponding to the zone-signing key (ZSK-private) online to immediately update the signatures for the updated RRsets. Failure to protect the private ZSK opens it to being maliciously obtained and opens the DNS zone to being populated with invalid data. The integrity of the DNS zone would be compromised, leading to a loss of trust whether a DNS response has originated from an authentic source, the response is complete and has not been tampered with during transit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the ZSK private key is the only key stored on the name server. For each signed zone file, identify the ZSK "key id" number: # cat <signed_zone_file> | grep -i "zsk" ZSK; alg = ECDSAP256SHA256; key id = 22335 Using the ZSK "key id", verify that the only private key stored on the system matches the "key id". Kexample.com.+008+22335.private If any ZSK private keys exist on the server other than the one corresponding to the active ZSK pair, this is a finding.

## Group: SRG-APP-000176-DNS-000096

**Group ID:** `V-272373`

### Rule: The BIND 9.x server signature generation using the key signing key (KSK) must be done offline, using the KSK-private key stored offline.

**Rule ID:** `SV-272373r1124070_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The private key in the KSK key pair must be protected from unauthorized access. The private key must be stored offline (with respect to the internet-facing, DNSSEC-aware name server) in a physically secure, nonnetwork-accessible machine along with the zone file primary copy. Failure to protect the private KSK may have significant effects on the overall security of the DNS infrastructure. A compromised KSK could lead to an inability to detect unauthorized DNS zone data resulting in network traffic being redirected to a rogue site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that no private KSKs are stored on the name sever. With the assistance of the DNS administrator, obtain a list of all DNSSEC private keys that are stored on the name server. Inspect the signed zone files(s) and if there are local zones, look for the KSK key ID: DNSKEY 257 3 8 ( <hash_algorithm) ; KSK ; alg = ECDSAP256SHA256; key id = 52807 Verify that none of the identified private keys are KSKs. An example private KSK would look like the following: Kexample.com.+008+52807.private If private KSKs are stored on the name server, this is a finding.

## Group: SRG-APP-000176-DNS-000019

**Group ID:** `V-272375`

### Rule: The read and write access to a TSIG key file used by a BIND 9.x server must be restricted to only the account that runs the name server software.

**Rule ID:** `SV-272375r1123858_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Weak permissions of a TSIG key file could allow an adversary to modify the file, thus defeating the security objective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify permissions assigned to the TSIG keys enforce read-write access to the key owner and deny access to group or system users. With the assistance of the DNS administrator, determine the location of the TSIG keys used by the BIND 9.x implementation: # ls -al <TSIG_Key_Location> -rw-r-----. 1 root named 76 May 10 20:35 tsig-example.key If the key files are more permissive than 640, this is a finding.

## Group: SRG-APP-000176-DNS-000076

**Group ID:** `V-272376`

### Rule: A unique TSIG key used by a BIND 9.x server must be generated for each pair of communicating hosts.

**Rule ID:** `SV-272376r1123860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enable zone transfer (requests and responses) through authenticated messages, it is necessary to generate a key for every pair of name servers. The key also can be used for securing other transactions, such as dynamic updates, DNS queries, and responses. The binary key string that is generated by most key generation utilities used with DNSSEC is Base64 encoded. TSIG is a string used to generate the message authentication hash stored in a TSIG RR and used to authenticate an entire DNS message. The process of authenticating the source of a message and its integrity through hash-based message authentication codes (HMAC) is specified through a set of DNS specifications known collectively as TSIG. The sender of the message uses the HMAC function to generate a MAC and sends this MAC along with the message to the receiver. The receiver, who shares the same secret key, uses the key and HMAC function used by the sender to compute the MAC on the received message. The receiver then compares the computed MAC with the received MAC; if the two values match, it provides assurance that the message has been received correctly and that the sender belongs to the community of users sharing the same secret key. Thus, message source authentication and integrity verification are performed in a single process. To enable zone transfer (requests and responses) through authenticated messages, it is necessary to generate a key for every pair of name servers. The key also can be used for securing other transactions, such as dynamic updates, DNS queries, and responses. The binary key string that is generated by most key generation utilities used with DNSSEC is Base64 encoded. TSIG is a string used to generate the message authentication hash stored in a TSIG RR and used to authenticate an entire DNS message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is configured to use separate TSIG key-pairs when securing server-to-server transactions. Inspect the "named.conf" file for the presence of TSIG key statements: On the primary name server, this is an example of a configured key statement: key tsig_example. { algorithm hmac-SHA256; include "tsig-example.key"; }; zone "disa.mil" { type Primary; file "db.disa.mil"; allow-transfer { key tsig_example.; }; }; On the secondary name server, this is an example of a configured key statement: key tsig_example. { algorithm hmac-SHA256; include "tsig-example.key"; }; server <ip_address> { keys { tsig_example }; }; zone "disa.mil" { type Secondary; Primarys { <ip_address>; }; file "db.disa.mil"; }; Verify that each TSIG key-pair listed is only used by a single key statement: # cat <tsig_key_file> If any TSIG key-pair is being used by more than one key statement, this is a finding.

## Group: SRG-APP-000176-DNS-000018

**Group ID:** `V-272377`

### Rule: The TSIG keys used with the BIND 9.x implementation must be owned by a privileged account.

**Rule ID:** `SV-272377r1123862_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incorrect ownership of a TSIG key file could allow an adversary to modify the file, thus defeating the security objective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify all of the TSIG keys used by the BIND 9.x implementation. Identify the account that the "named" process is running as: # ps -ef | grep named named 3015 1 0 12:59 ? 00:00:00 /usr/sbin/named -u named -t /var/named/chroot With the assistance of the DNS administrator, determine the location of the TSIG keys used by the BIND 9.x implementation. # ls -al <TSIG_Key_Location> -rw-r-----. 1 root named 76 May 10 20:35 tsig-example.key If any of the TSIG keys are not owned by the above account, this is a finding.

## Group: SRG-APP-000176-DNS-000018

**Group ID:** `V-272378`

### Rule: The TSIG keys used with the BIND 9.x implementation must be group owned by a privileged account.

**Rule ID:** `SV-272378r1123864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incorrect ownership of a TSIG key file could allow an adversary to modify the file, thus defeating the security objective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify all of the TSIG keys used by the BIND 9.x implementation. Identify the account that the "named" process is running as: # ps -ef | grep named named 3015 1 0 12:59 ? 00:00:00 /usr/sbin/named -u named -t /var/named/chroot With the assistance of the DNS administrator, determine the location of the TSIG keys used by the BIND 9.x implementation. # ls -al <TSIG_Key_Location> -rw-r-----. 1 root named 76 May 10 20:35 tsig-example.key If any of the TSIG keys are not group owned by the above account, this is a finding.

## Group: SRG-APP-000516-DNS-000091

**Group ID:** `V-272379`

### Rule: On a BIND 9.x server, for zones split between the external and internal sides of a network, the RRs for the external hosts must be separate from the RRs for the internal hosts.

**Rule ID:** `SV-272379r1124035_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authoritative name servers for an enterprise may be configured to receive requests from both external and internal clients. External clients need to receive RRs that pertain only to public services (public web server, mail server, etc.). Internal clients need to receive RRs pertaining to public services as well as internal hosts. The zone information that serves the RRs on both the inside and outside of a firewall must be split into different physical files for these two types of clients (one file for external clients and one file for internal clients).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIND 9.x name server is not configured for split DNS, this is not applicable. Verify that the BIND 9.x server is configured to use separate views and address space for internal and external DNS operations when operating in a split configuration. Inspect the "named.conf" file for the following: view "internal" { match-clients { <ip_address> | <address_match_list> }; zone "example.com" { type Primary; file "internals.example.com"; }; }; view "external" { match-clients { <ip_address> | <address_match_list> }; zone "example.com" { type Primary; file "externals.db.example.com"; allow-transfer { Secondarys; }; }; }; If the internal and external view statements are configured to use the same zone file, this is a finding. Inspect the zone file defined in the internal and external view statements. If any resource record is listed in both the internal and external zone files, this is a finding.

## Group: SRG-APP-000516-DNS-000093

**Group ID:** `V-272380`

### Rule: On a BIND 9.x server in a split DNS configuration, where separate name servers are used between the external and internal networks, the internal name server must be configured to not be reachable from outside resolvers.

**Rule ID:** `SV-272380r1124037_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Instead of having the same set of authoritative name servers serve different types of clients, an enterprise could have two different sets of authoritative name servers. One set, called external name servers, can be located within a DMZ. These would be the only name servers that are accessible to external clients and would serve RRs pertaining to hosts with public services (web servers that serve external web pages or provide B2C services, mail servers, etc.). The other set, called internal name servers, must be located within the firewall. They must be configured so they are not reachable from outside and therefore provide naming services exclusively to internal clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIND 9.x name server is not configured for split DNS, this is not applicable. Verify that the BIND 9.x server is configured to use the "match-clients" sub-statement to limit the reach of the internal view from the external view. Inspect the "named.conf" file for the following: view "internal" { match-clients { <ip_address> | <address_match_list>; }; }; If the "match-clients" sub-statement is missing for the internal view, this is a finding. If the "match-clients" sub-statement for the internal view does not limit the view to authorized hosts, this is a finding. If any of the IP addresses defined for the "match-clients" sub-statement in the internal view are assigned to external hosts, this is a finding.

## Group: SRG-APP-000516-DNS-000092

**Group ID:** `V-272381`

### Rule: On a BIND 9.x server in a split DNS configuration, where separate name servers are used between the external and internal networks, the external name server must be configured to not be reachable from inside resolvers.

**Rule ID:** `SV-272381r1124039_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Instead of having the same set of authoritative name servers serve different types of clients, an enterprise could have two different sets of authoritative name servers. One set, called external name servers, can be located within a DMZ. These would be the only name servers that are accessible to external clients and would serve RRs pertaining to hosts with public services (web servers that serve external web pages or provide B2C services, mail servers, etc.). The other set, called internal name servers, must be located within the firewall. They must be configured so they are not reachable from outside and therefore provide naming services exclusively to internal clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIND 9.x name server is not configured for split DNS, this is not applicable. Verify that the external view of the BIND 9.x server is configured to only serve external hosts. Inspect the "named.conf" file for the following: view "external" { match-clients { <ip_address> | <address_match_list>; }; }; If the "match-clients" sub-statement does not limit the external view to external hosts only, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-272382`

### Rule: A BIND 9.x implementation operating in a split DNS configuration must be approved by the organization's authorizing official (AO).

**Rule ID:** `SV-272382r1124041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>BIND 9.x has implemented an option to use "view" statements to allow for split DNS architecture to be configured on a single name server. If the split DNS architecture is improperly configured, there is a risk that internal IP addresses and host names could leak into the external view of the DNS server. Allowing private IP space to leak into the public DNS system may provide a person with malicious intent the ability to footprint the network and identify potential attack targets residing on the private network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIND 9.x name server is not configured for split DNS, this is not applicable. Verify that the split DNS implementation has been approved by the organizations AO. With the assistance of the DNS administrator, obtain the AO's letter of approval for the split DNS implementation. If the split DNS implementation has not been approved by the organizations AO, this is a finding.

## Group: SRG-APP-000516-DNS-000108

**Group ID:** `V-272383`

### Rule: On the BIND 9.x server the IP address for hidden primary authoritative name servers must not appear in the name servers set in the zone database.

**Rule ID:** `SV-272383r1124043_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A hidden primary authoritative server is an authoritative DNS server whose IP address does not appear in the name server set for a zone. All of the name servers that do appear in the zone database as designated name servers get their zone data from the hidden primary via a zone transfer request. In effect, all visible name servers are actually secondary servers. This prevents potential attackers from targeting the primary name server because its IP address may not appear in the zone database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify if the BIND 9.x implementation is using a hidden primary name server. If it is not, this is not applicable. In a split DNS configuration that is using a hidden primary name server, verify that the name server IP address is not listed in the zone file. With the assistance of the DNS administrator, obtain the IP address of the hidden primary name server. Inspect each zone file used by the hidden primary name server and its secondary zones. If the IP address for the hidden primary name server is listed in any of the zone files, this is a finding.

## Group: SRG-APP-000516-DNS-000084

**Group ID:** `V-272384`

### Rule: A BIND 9.x server NSEC3 must be used for all internal DNS zones.

**Rule ID:** `SV-272384r1123744_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure that RRs associated with a query are really missing in a zone file and have not been removed in transit, the DNSSEC mechanism provides a means for authenticating the nonexistence of an RR. It generates a special RR called an NSEC (or NSEC3) RR that lists the RRTypes associated with an owner name as well as the next name in the zone file. It sends this special RR, along with its signatures, to the resolving name server. By verifying the signature, a DNSSEC-aware resolving name server can determine which authoritative owner name exists in a zone and which authoritative RRTypes exist at those owner names.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the server is on an internal, restricted network with reserved IP space, this is Not Applicable. With the assistance of the DNS administrator, identify each internal DNS zone listed in the "named.conf" file. For each internal zone identified, inspect the signed zone file for the NSEC resource records: 86400 NSEC example.com. A RRSIG NSEC If the zone file does not contain an NSEC record for the zone, this is a finding.

## Group: SRG-APP-000516-DNS-000112

**Group ID:** `V-272385`

### Rule: On the BIND 9.x server, the private keys corresponding to both the zone signing key (ZSK) and the key signing key (KSK) must not be kept on the BIND 9.x DNSSEC-aware primary authoritative name server when the name server does not support dynamic updates.

**Rule ID:** `SV-272385r1124044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The private keys in the KSK and ZSK key pairs must be protected from unauthorized access. If possible, the private keys should be stored offline (with respect to the internet-facing, DNSSEC-aware name server) in a physically secure, nonnetwork-accessible machine along with the zone file primary copy. This strategy is not feasible in situations in which the DNSSEC-aware name server has to support dynamic updates. To support dynamic update transactions, the DNSSEC-aware name server (which usually is a primary authoritative name server) has to have both the zone file primary copy and the private key corresponding to the zone-signing key (ZSK-private) online to immediately update the signatures for the updated RRsets. The private key corresponding to the key-signing key (KSK-private) can still be kept offline.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the BIND 9.x server is configured to allow dynamic updates. Review the "named.conf" file for any instance of the "allow-update" statement. The following example disables dynamic updates: allow-update {none;}; If the BIND 9.x implementation is not configured to allow dynamic updates or inline signing, verify with the system administrator (SA) that the private ZSKs and private KSKs are stored offline. If not, this is a finding.

## Group: SRG-APP-000516-DNS-000086

**Group ID:** `V-272386`

### Rule: The two files generated by the BIND 9.x server dnssec-keygen program must be owned by the administrator account or deleted once they have been copied to the key file in the name server.

**Rule ID:** `SV-272386r1123985_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enable zone transfer (requests and responses) through authenticated messages, it is necessary to generate a key for every pair of name servers. The key also can be used for securing other transactions, such as dynamic updates, DNS queries, and responses. The binary key string that is generated by most key generation utilities used with DNSSEC is Base64 encoded. A TSIG is a string used to generate the message authentication hash stored in a TSIG RR and used to authenticate an entire DNS message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify all dnssec-keygen key files that reside on the BIND 9.x server. An example dnssec-keygen key file will look like the following: Kns1.example.com_ns2.example.com.+161+28823.key OR Kns1.example.com_ns2.example.com.+161+28823.private For each key file identified, verify that the key file is owned by "named": # ls -al -rw-r-----. 1 named named 76 May 10 20:35 dnssec-example.key If the key files are not owned by named, this is a finding.

## Group: SRG-APP-000516-DNS-000086

**Group ID:** `V-272387`

### Rule: The two files generated by the BIND 9.x server dnssec-keygen program must be group owned by the server administrator account or deleted once they have been copied to the key file in the name server.

**Rule ID:** `SV-272387r1123881_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enable zone transfer (requests and responses) through authenticated messages, it is necessary to generate a key for every pair of name servers. The key also can be used for securing other transactions such as dynamic updates, DNS queries, and responses. The binary key string that is generated by most key generation utilities used with DNSSEC is Base64 encoded. A TSIG is a string used to generate the message authentication hash stored in a TSIG RR and used to authenticate an entire DNS message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify all dnssec-keygen key files that reside on the BIND 9.x server. An example dnssec-keygen key file will look like the following: Kns1.example.com_ns2.example.com.+161+28823.key OR Kns1.example.com_ns2.example.com.+161+28823.private For each key file identified, verify that the key file is owned by "named": # ls -al -rw-r-----. 1 named named 77 Jul 1 15:00 Kns1.example.com_ns2.example.com+161+28823.key If the key files are not owned by named, this is a finding.

## Group: SRG-APP-000516-DNS-000086

**Group ID:** `V-272388`

### Rule: Permissions assigned to the dnssec-keygen keys used with the BIND 9.x implementation must enforce read-only access to the key owner and deny access to all other users.

**Rule ID:** `SV-272388r1124010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enable zone transfer (requests and responses) through authenticated messages, it is necessary to generate a key for every pair of name servers. The key also can be used for securing other transactions such as dynamic updates, DNS queries, and responses. The binary key string that is generated by most key generation utilities used with DNSSEC is Base64 encoded. A TSIG is a string used to generate the message authentication hash stored in a TSIG RR and used to authenticate an entire DNS message. Weak permissions could allow an adversary to modify the file(s), thus defeating the security objective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify all dnssec-keygen key files that reside on the BIND 9.x server. An example dnssec-keygen key file will look like the following: Kns1.example.com_ns2.example.com.+161+28823.key OR Kns1.example.com_ns2.example.com.+161+28823.private For each key file identified, verify that the key file is owned by "named" and permissions are set to 400: # ls -al -r-------- 1 named named 77 Jul 1 15:00 Kns1.example.com_ns2.example.com+161+28823.key If the key files are not owned by “named”, this is a finding. If the key files are more permissive than 400, this is a finding.

## Group: SRG-APP-000516-DNS-000078

**Group ID:** `V-272389`

### Rule: A BIND 9.x server validity period for the RRSIGs covering a zones DNSKEY RRSet must be no less than two days and no more than one week.

**Rule ID:** `SV-272389r1123885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The best way for a zone administrator to minimize the impact of a key compromise is by limiting the validity period of RRSIGs in the zone and in the parent zone. This strategy limits the time during which an attacker can take advantage of a compromised key to forge responses. An attacker that has compromised a zone signing key (ZSK) can use that key only during the key signing key's (KSK's) signature validity interval. An attacker that has compromised a KSK can use that key for only as long as the signature interval of the RRSIG covering the DS RR in the delegating parent. These validity periods should be short, which will require frequent re-signing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify the RRSIGs that cover the DNSKEY resource record set for each zone. Each record will list an expiration and inception date, the difference of which will provide the validity period. This check also applies to inline signing. The dates are listed in the following format: YYYYMMDDHHMMSS For each RRSIG identified, verify that the validity period is no less than two days and no longer than seven days. If the validity period is outside of the specified range, this is a finding.

## Group: SRG-APP-000516-DNS-000111

**Group ID:** `V-272390`

### Rule: On the BIND 9.x server, the private key corresponding to the zone signing key (ZSK), stored on name servers accepting dynamic updates, must be owned by named.

**Rule ID:** `SV-272390r1123888_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The private keys in the key signing key (KSK) and ZSK key pairs must be protected from unauthorized access. If possible, the private keys should be stored offline (with respect to the internet-facing, DNSSEC-aware name server) in a physically secure, nonnetwork-accessible machine along with the zone file primary copy. This strategy is not feasible in situations in which the DNSSEC-aware name server has to support dynamic updates. To support dynamic update transactions, the DNSSEC-aware name server (which usually is a primary authoritative name server) has to have both the zone file primary copy and the private key corresponding to the zone-signing key (ZSK-private) online to immediately update the signatures for the updated RRsets. The private key corresponding to the key-signing key (KSK-private) can still be kept offline.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check only verifies for ZSK key file ownership. Permissions for key files are required under BIND-9X-001132 and BIND-9X-001142. For each signed zone file, identify the ZSK "key id" number: # cat <signed_zone_file> | grep -i "zsk" ZSK; alg = ECDSAP256SHA256; key id = 22335 Using the ZSK "key id", identify the private ZSK: Kexample.com.+008+22335.private Verify that the private ZSK is owned by named: # ls -l <ZSK_key_file> -r------- 1 named named 1776 Jul 3 17:56 Kexample.com.+008+22335.private If the key file is not owned by named, this is a finding.

## Group: SRG-APP-000516-DNS-000111

**Group ID:** `V-272391`

### Rule: On the BIND 9.x server, the private key corresponding to the zone signing key (ZSK), stored on name servers accepting dynamic updates, must be group owned by named.

**Rule ID:** `SV-272391r1123891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The private keys in the key signing key (KSK) and ZSK key pairs must be protected from unauthorized access. If possible, the private keys should be stored offline (with respect to the internet-facing, DNSSEC-aware name server) in a physically secure, nonnetwork-accessible machine along with the zone file primary copy. This strategy is not feasible in situations in which the DNSSEC-aware name server has to support dynamic updates. To support dynamic update transactions, the DNSSEC-aware name server (which usually is a primary authoritative name server) has to have both the zone file primary copy and the private key corresponding to the zone-signing key (ZSK-private) online to immediately update the signatures for the updated RRsets. The private key corresponding to the key-signing key (KSK-private) can still be kept offline.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check only verifies for ZSK key file ownership. Permissions for key files are required under BIND-9X-001132 and BIND-9X-001142. For each signed zone file, identify the ZSK "key id" number: # cat <signed_zone_file> | grep -i "zsk" ZSK; alg = ECDSAP256SHA256; key id = 22335 Using the ZSK "key id", verify the private ZSK. Kexample.com.+008+22335.private Verify that the private ZSK is owned by "named": # ls -l <ZSK_key_file> -r------- 1 named named 1776 Jul 3 17:56 Kexample.com.+008+22335.private If the key file is not group owned by named, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-272392`

### Rule: The BIND 9.x server implementation must prohibit the forwarding of queries to servers controlled by organizations outside of the U.S. government.

**Rule ID:** `SV-272392r1124046_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If remote servers to which DOD DNS servers send queries are controlled by entities outside of the U.S. government the possibility of a DNS attack is increased. The Enterprise Recursive Service (ERS) provides the ability to apply enterprise-wide policy to all recursive DNS traffic that traverses the NIPRNet-to-Internet boundary. All recursive DNS servers on the NIPRNet must be configured to exclusively forward DNS traffic traversing NIPRNet-to-Internet boundary to the ERS anycast IPs. Organizations need to carefully configure any forwarding that is being used by their caching name servers. They should only configure "forwarding of all queries" to servers within the DOD. Systems configured to use domain-based forwarding should not forward queries for mission critical domains to any servers that are not under the control of the U.S. government.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the server is not a caching server, this is not applicable. Note: The use of the Defense Research and Engineering Network (DREN) Enterprise Recursive DNS servers, as mandated by the DODIN service provider DREN, meets the intent of this requirement. Verify that the server is configured to forward all DNS traffic to the DISA ERS anycast IP addresses ( <IP_ADDRESS_LIST>; ). Inspect the "named.conf" file for the following: forward only; forwarders { <IP_ADDRESS_LIST>; }; If the "named.conf" options are not set to forward queries only to the ERS anycast IPs, this is a finding.

## Group: SRG-APP-000516-DNS-000088

**Group ID:** `V-272393`

### Rule: The secondary name servers in a BIND 9.x implementation must be configured to initiate zone update notifications to other authoritative zone name servers.

**Rule ID:** `SV-272393r1124048_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is important to maintain the integrity of a zone file. The serial number of the SOA record is used to indicate to secondary name server that a change to the zone has occurred and a zone transfer should be performed. The serial number used in the SOA record provides the DNS administrator a method to verify the integrity of the zone file based on the serial number of the last update and ensure that all secondary servers are using the correct zone file. When a primary name server notices that the serial number of a zone has changed, it sends a special announcement to all of the secondary name servers for that zone. The primary name server determines which servers are the secondaries for the zone by looking at the list of NS records in the zone and taking out the record that points to the name server listed in the MNAME field of the zone's SOA record as well as the domain name of the local host. When a secondary name server receives a NOTIFY announcement for a zone from one of its configured primary name servers, it responds with a NOTIFY response. The response tells the primary that the secondary received the NOTIFY announcement so that the primary can stop sending it NOTIFY announcements for the zone. Then the secondary proceeds just as if the refresh timer for that zone had expired: it queries the primary name server for the SOA record for the zone that the primary claims has changed. If the serial number is higher, the secondary transfers the zone. The secondary should next issue its own NOTIFY announcements to the other authoritative name servers for the zone. The idea is that the primary may not be able to notify all of the secondary name servers for the zone itself, since it is possible some secondaries cannot communicate directly with the primary (they use another secondary as their primary). Older BIND 8 secondaries do not send NOTIFY messages unless explicitly configured to do so.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is a primary name server, this is not applicable. On a secondary name server, verify that the global notify is disabled. The global entry for the name server is under the "Options" section, and notify must be disabled at this section. Inspect the "named.conf" file for the following: options { notify no; }; If the "notify" statement is missing, this is a finding. If the "notify" statement is set to "yes", this is a finding. Verify that zones for which the secondary server is authoritative are configured to notify other authorized secondary name servers when a zone file update has been received from the primary name server for the zone. Each zone has its own zone section. Inspect the "named.conf" file for the following: zone example.com { notify explicit; also-notify { <ip_address>; | <address_match_list>; }; If an "address match list" is used, verify that each IP address listed is an authorized secondary name server for that zone. If the "notify explicit" statement is missing, this is a finding. If the "also-notify" statement is missing, this is a finding. If the "also-notify" statement is configured to notify name servers that are not authorized for that zone, this is a finding.

## Group: SRG-APP-000383-DNS-000047

**Group ID:** `V-272394`

### Rule: A BIND 9.x server implementation must prohibit recursion on authoritative name servers.

**Rule ID:** `SV-272394r1124050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A potential vulnerability of DNS is that an attacker can poison a name server's cache by sending queries that will cause the server to obtain host-to-IP address mappings from bogus name servers that respond with incorrect information. Once a name server has been poisoned, legitimate clients may be directed to nonexistent hosts (which constitutes a denial of service), or worse, hosts that masquerade as legitimate ones to obtain sensitive data or passwords. To guard against poisoning, name servers authoritative for .mil domains should be separated functionally from name servers that resolve queries on behalf of internal clients. Organizations may achieve this separation by dedicating machines to each function or, if possible, by running two instances of the name server software on the same machine: one for the authoritative function and the other for the resolving function. In this design, each name server process may be bound to a different IP address or network interface to implement the required segregation. DNSSEC ensures that the answer received when querying for name resolution actually comes from a trusted name server. Since DNSSEC is still far from being globally deployed external to DOD, and many resolvers either have not been updated or do not support DNSSEC, maintaining cached zone data separate from authoritative zone data mitigates the gap until all DNS data is validated with DNSSEC. Since DNS forwarding of queries can be accomplished in some DNS applications without caching locally, DNS forwarding is the method to be used when providing external DNS resolution to internal clients. Satisfies: SRG-APP-000383-DNS-000047, SRG-APP-000246-DNS-000035</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is a recursive name server, this is not applicable. Note: A recursive name server must NOT be configured as an authoritative name server for any zone. Verify that the BIND 9.x server is configured to prohibit recursion on authoritative name servers. Inspect the "named.conf" file for the following: options { recursion no; allow-recursion {none;}; allow-query {none;}; }; If the "recursion" sub-statement is missing or set to "yes", this is a finding.

## Group: SRG-APP-000516-DNS-000088

**Group ID:** `V-272395`

### Rule: The primary servers in a BIND 9.x implementation must notify authorized secondary name servers when zone files are updated.

**Rule ID:** `SV-272395r1124052_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is important to maintain the integrity of a zone file. The serial number of the SOA record is used to indicate to secondary name server that a change to the zone has occurred and a zone transfer should be performed. The serial number used in the SOA record provides the DNS administrator a method to verify the integrity of the zone file based on the serial number of the last update and ensure that all secondary servers are using the correct zone file. When a primary name server notices that the serial number of a zone has changed, it sends a special announcement to all of the secondary name servers for that zone. The primary name server determines which servers are the secondaries for the zone by looking at the list of NS records in the zone and taking out the record that points to the name server listed in the MNAME field of the zone's SOA record as well as the domain name of the local host. When a secondary name server receives a NOTIFY announcement for a zone from one of its configured primary name servers, it responds with a NOTIFY response. The response tells the primary that the secondary received the NOTIFY announcement so that the primary can stop sending it NOTIFY announcements for the zone. Then the secondary proceeds just as if the refresh timer for that zone had expired: it queries the primary name server for the SOA record for the zone that the primary claims has changed. If the serial number is higher, the secondary transfers the zone. The secondary should issue its own NOTIFY announcements to the other authoritative name servers for the zone. The idea is that the primary may not be able to notify all of the secondary name servers for the zone itself, since it is possible some secondaries cannot communicate directly with the primary (they use another secondary as their primary). Older BIND 8 secondaries do not send NOTIFY messages unless explicitly configured to do so.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is a secondary name server, this is not applicable. On a primary name server, verify that the global notify is disabled. The global entry for the name server is under the "Options" section, and "notify" must be disabled at this section. Inspect the "named.conf" file for the following: options { notify no; }; If the "notify" statement is missing, this is a finding. If the "notify" statement is set to "yes", this is a finding. Verify that each zone is configured to notify authorized secondary name servers when a zone file has been updated. Each zone has its own zone section. Inspect the "named.conf" file for the following: zone example.com { notify explicit; also-notify { <ip_address>; | <address_match_list>; }; If an "address match list" is used, verify that each IP address listed is an authorized secondary name server for that zone. If the "notify explicit" statement is missing, this is a finding. If the "also-notify" statement is missing, this is a finding. If the "also-notify" statement is configured to notify name servers that are not authorized for that zone, this is a finding.

## Group: SRG-APP-000516-DNS-000102

**Group ID:** `V-272396`

### Rule: On a BIND 9.x server, all root name servers listed in the local root zone file hosted on a BIND 9.x authoritative name server must be valid for that zone.

**Rule ID:** `SV-272396r1124054_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All caching name servers must be authoritative for the root zone because, without this starting point, they would have no knowledge of the DNS infrastructure and thus would be unable to respond to any queries. The security risk is that an adversary could change the root hints and direct the caching name server to a bogus root server. At that point, every query response from that name server is suspect, which would give the adversary substantial control over the network communication of the name servers' clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is an authoritative name server, this is not applicable. Use command dig @<serverip> . ns and examine results. Answer results . 518400 IN NS e.root-servers.net. . 518400 IN NS a.root-servers.net. . 518400 IN NS g.root-servers.net. . 518400 IN NS i.root-servers.net. . 518400 IN NS h.root-servers.net. . 518400 IN NS d.root-servers.net. . 518400 IN NS c.root-servers.net. . 518400 IN NS k.root-servers.net. . 518400 IN NS f.root-servers.net. . 518400 IN NS m.root-servers.net. . 518400 IN NS b.root-servers.net. . 518400 IN NS j.root-servers.net. . 518400 IN NS l.root-servers.net. ;; ADDITIONAL SECTION: m.root-servers.net. 518400 IN A 202.12.27.33 l.root-servers.net. 518400 IN A 199.7.83.42 k.root-servers.net. 518400 IN A 193.0.14.129 j.root-servers.net. 518400 IN A 192.58.128.30 i.root-servers.net. 518400 IN A 192.36.148.17 h.root-servers.net. 518400 IN A 198.97.190.53 g.root-servers.net. 518400 IN A 192.112.36.4 f.root-servers.net. 518400 IN A 192.5.5.241 e.root-servers.net. 518400 IN A 192.203.230.10 d.root-servers.net. 518400 IN A 199.7.91.13 c.root-servers.net. 518400 IN A 192.33.4.12 b.root-servers.net. 518400 IN A 170.247.170.2 a.root-servers.net. 518400 IN A 198.41.0.4 m.root-servers.net. 518400 IN AAAA 2001:dc3::35 l.root-servers.net. 518400 IN AAAA 2001:500:9f::42 k.root-servers.net. 518400 IN AAAA 2001:7fd::1 j.root-servers.net. 518400 IN AAAA 2001:503:c27::2:30 i.root-servers.net. 518400 IN AAAA 2001:7fe::53 h.root-servers.net. 518400 IN AAAA 2001:500:1::53 g.root-servers.net. 518400 IN AAAA 2001:500:12::d0d f.root-servers.net. 518400 IN AAAA 2001:500:2f::f e.root-servers.net. 518400 IN AAAA 2001:500:a8::e d.root-servers.net. 518400 IN AAAA 2001:500:2d::d c.root-servers.net. 518400 IN AAAA 2001:500:2::c b.root-servers.net. 518400 IN AAAA 2801:1b8:10::b a.root-servers.net. 518400 IN AAAA 2001:503:ba3e::2:30 If names and addresses do not match the current IANA list, this is a finding. Perform command dig @<serverip> . dnskey +multi and examine results. answer results 77555 IN DNSKEY 257 3 8 ( AwEAAaz/tAm8yTn4Mfeh5eyI96WSVexTBAvkMgJzkKTO iW1vkIbzxeF3+/4RgWOq7HrxRixHlFlExOLAJr5emLvN 7SWXgnLh4+B5xQlNVz8Og8kvArMtNROxVQuCaSnIDdD5 LKyWbRd2n9WGe2R8PzgCmr3EgVLrjyBxWezF0jLHwVN8 efS3rCj/EWgvIWgb9tarpVUDK/b58Da+sqqls3eNbuv7 pr+eoZG+SrDK6nWeL3c6H5Apxz7LjVc1uTIdsIXxuOLY A4/ilBmSVIzuDWfdRUfhHdY6+cn8HFRm+2hM8AnXGXws 9555KrUB5qihylGa8subX2Nn6UwNR1AkUTV74bU= ) ; KSK; alg = RSASHA256 ; key id = 20326 . 77555 IN DNSKEY 256 3 8 ( AwEAAbEbGCpGTDrcZTWqWWE72nphyshpRcILdzCVlBGU 9Ln1Fui9kkseUOP+g5GLUeVFKdTloeRTA9+EYiQdXgWX mXmuW/nGxZjAikluF/O9NzLVrr5iZnth2xu+F48nrJlA gWWiMNau54NI5sZ3iVQfhFsq2pZmf43RauRPniYMShOL O7EBWWXr5glDSgZGS9fSm6xHwwF+g8D4m8oanjvdCBNx XzSEKS31ibxjLifTfvwCg3y4XXcNW9U6Nu3JmoKUdxqp PPIkBvVQbIz4UO2FwaR13uXC03ALP1Yx2QNSS4SZlcIM tAftQR9wtCiuPWQnFv4jkzWqlhp1Lmf7bcoL9yk= ) ; ZSK; alg = RSASHA256 ; key id = 53148 . 77555 IN DNSKEY 257 3 8 ( AwEAAa96jeuknZlaeSrvyAJj6ZHv28hhOKkx3rLGXVaC 6rXTsDc449/cidltpkyGwCJNnOAlFNKF2jBosZBU5eeH spaQWOmOElZsjICMQMC3aeHbGiShvZsx4wMYSjH8e7Vr hbu6irwCzVBApESjbUdpWWmEnhathWu1jo+siFUiRAAx m9qyJNg/wOZqqzL/dL/q8PkcRU5oUKEpUge71M3ej2/7 CPqpdVwuMoTvoB+ZOT4YeGyxMvHmbrxlFzGOHOijtzN+ u1TQNatX2XBuzZNQ1K+s2CXkPIZo7s6JgZyvaBevYtxP vYLw4z9mR7K2vaF18UYH9Z9GNUUeayffKC73PYc= ) ; KSK; alg = RSASHA256 ; key id = 38696 If the dnssec keys and root anchors do not match the IANA list, this is a finding.

## Group: SRG-APP-000516-DNS-000102

**Group ID:** `V-272397`

### Rule: On a BIND 9.x server, all root name servers listed in the local root zone file hosted on a BIND 9.x authoritative name server must be empty or removed.

**Rule ID:** `SV-272397r1124056_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A potential vulnerability of DNS is that an attacker can poison a name server's cache by sending queries that will cause the server to obtain host-to-IP address mappings from bogus name servers that respond with incorrect information. The DNS architecture needs to maintain one name server whose zone records are correct and the cache is not poisoned. In this effort, the authoritative name server may not forward queries; one of the ways to prevent this is to delete the root hints file. When authoritative servers are sent queries for zones that they are not authoritative for and they are configured as a noncaching server (as recommended), they can either be configured to return a referral to the root servers or to refuse to answer the query. The requirement is to configure authoritative servers to refuse to answer queries for any zones for which they are not authoritative. This is more efficient for the server and allows it to spend more of its resources for its intended purpose of answering authoritatively for its zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this server is a caching name server, this is not applicable. Verify there is not a local root zone on the name server. Inspect the "named.conf" file for the following: zone "." IN { type hint; file "<file_name>" }; If the file name identified is not empty or does exist, this is a finding.

## Group: SRG-APP-000516-DNS-000101

**Group ID:** `V-272399`

### Rule: The BIND 9.x server implementation must implement internal/external role separation.

**Rule ID:** `SV-272399r1124058_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS servers with an internal role only process name/address resolution requests from within the organization (i.e., internal clients). DNS servers with an external role only process name/address resolution information requests from clients external to the organization (i.e., on the external networks, including the internet). The set of clients that can access an authoritative DNS server in a particular role is specified by the organization using address ranges, explicit access control lists, etc. To protect internal DNS resource information, it is important to isolate the requests to internal DNS servers. Failure to separate internal and external roles in DNS may lead to address space that is private (e.g., 10.0.0.0/24) or is otherwise concealed by some form of Network Address Translation from leaking into the public DNS system. Allowing private IP space to leak into the public DNS system may provide a person with malicious intent the ability to footprint the network and identify potential attack targets residing on the private network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Severity override guidance: If the internal and external views are on separate network segments, this finding may be downgraded to a CAT II. If the BIND 9.x name server is not configured for split DNS, this is not applicable. Verify that the BIND 9.x server is configured to use separate views and address space for internal and external DNS operations when operating in a split configuration. Inspect the "named.conf" file for the following: view "internal" { match-clients { <ip_address> | <address_match_list> }; zone "example.com" { type Primary; file "internals.example.com"; }; }; view "external" { match-clients { <ip_address> | <address_match_list> }; zone "example.com" { type Primary; file "externals.db.example.com"; allow-transfer { Secondarys; }; }; }; If an external view is listed before an internal view, this is a finding. If the internal and external views are on the same network segment, this is a finding. Note: BIND 9.x reads the "named.conf" file from top to bottom. If a less stringent "match-clients" statement is processed before a more stringent "match-clients" statement, the more stringent statement will be ignored. With this in mind, all internal view statements must be listed before any external view statement in the "named.conf" file.

## Group: SRG-APP-000516-DNS-000085

**Group ID:** `V-272400`

### Rule: Every NS record in a zone file on a BIND 9.x server must point to an active name server and that name server must be authoritative for the domain specified in that record.

**Rule ID:** `SV-272400r1123993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Poorly constructed NS records pose a security risk because they create conditions under which an adversary might be able to provide the missing authoritative name services that are improperly specified in the zone file. The adversary could issue bogus responses to queries that clients would accept because they learned of the adversary's name server from a valid authoritative name server, one that need not be compromised for this attack to be successful. The list of secondary servers must remain current with any changes to the zone architecture that would affect the list of secondaries. If a secondary server has been retired or is not operational but remains on the list, an adversary might have a greater opportunity to impersonate that secondary without detection, rather than if the secondary were actually online. For example, the adversary may be able to spoof the retired secondary's IP address without an IP address conflict, which would not be likely to occur if the true secondary were active.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that each name server listed on the BIND 9.x server is authoritative for the domain it supports. Inspect the "named.conf" file and identify all of the zone files that the BIND 9.x server is using. zone "example.com" { file "zone_file"; }; Inspect each zone file and identify each NS record listed. 86400 NS ns1.example.com 86400 NS ns2.example.com With the assistance of the DNS administrator, verify that each name server listed is authoritative for that domain. If name servers are listed in the zone file that are not authoritative for the specified domain, this is a finding.

## Group: SRG-APP-000516-DNS-000087

**Group ID:** `V-272401`

### Rule: On a BIND 9.x server, all authoritative name servers for a zone must be located on different network segments.

**Rule ID:** `SV-272401r1124059_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most enterprises have an authoritative primary server and a host of authoritative secondary name servers. It is essential that these authoritative name servers for an enterprise be located on different network segments. This dispersion ensures the availability of an authoritative name server not only in situations in which a particular router or switch fails but also during events involving an attack on an entire network segment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that each name server listed on the BIND 9.x server is on a separate network segment. Inspect the "named.conf" file and identify all of the zone files that the BIND 9.x server is using. zone "example.com" { file "zone_file"; }; Inspect each zone file and identify each A record for each NS record listed: ns1.example.com 86400 IN A 192.168.1.4 ns2.example.com 86400 IN A 192.168.2.4 If name servers are listed in the zone file that are not on different network segments for the specified domain, this is a finding.

## Group: SRG-APP-000516-DNS-000110

**Group ID:** `V-272402`

### Rule: On the BIND 9.x server, the platform on which the name server software is hosted must be configured to send outgoing DNS messages from a random port.

**Rule ID:** `SV-272402r1124060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OS configuration practices as issued by the U.S. Computer Emergency Response Team (US CERT) and the National Institute of Standards and Technology's (NIST's) National Vulnerability Database (NVD), based on identified vulnerabilities that pertain to the application profile into which the name server software fits should be always followed. In particular, hosts that run the name server software should not provide any other services and therefore should be configured to respond to DNS traffic only. In other words, the only allowed incoming ports/protocols to these hosts should be 53/udp and 53/tcp. Outgoing DNS messages should be sent from a random port to minimize the risk of an attacker guessing the outgoing message port and sending forged replies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server does not limit outgoing DNS messages to a specific port. Inspect the "named.conf" file. The "query-source" and "query-source-v6" must not limit the ports available to be used. options { query-source address <v4_address>; query-source-v6 address <v6_address>; }; If the port flag is used on the query-source address or query-source-v6 address, this is a finding.

## Group: SRG-APP-000516-DNS-000103

**Group ID:** `V-272403`

### Rule: A BIND 9.x server implementation must be operating on a Current-Stable version as defined by ISC.

**Rule ID:** `SV-272403r1123995_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The BIND STIG was written to incorporate capabilities and features provided in BIND version 9.9.x. However, security vulnerabilities in BIND are identified and then addressed on a regular, ongoing basis. Therefore, the product must be maintained at the latest stable versions to address vulnerabilities that are subsequently identified and can then be remediated via product updates. Failure to run a version of BIND that has the capability to implement all of the required security features and provide services compliant with the DNS RFCs can have a severe impact on the security posture of a DNS infrastructure. Without the required security in place, a DNS implementation is vulnerable to many types of attacks and could be used as a launching point for further attacks on the organizational network that is using the DNS implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is at a version that is considered "Current-Stable" by ISC or the latest supported version of BIND when BIND is installed as part of a specific vendor implementation where the vendor maintains the BIND patches. # named -v The above command should produce a version number similar to the following: BIND 9.18.36-RedHat-9.9.4-29.el7_2.3 If the server is running a version that is not listed as "Current-Stable" by ISC, this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-272404`

### Rule: The host running a BIND 9.x implementation must use a dedicated management interface to separate management traffic from DNS-specific traffic.

**Rule ID:** `SV-272404r1123996_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing out-of-band (OOB) management is the best first step in any management strategy. No production traffic resides on an OOB network. The biggest advantage to implementation of an OOB network is providing support and maintenance to the network that has become degraded or compromised. During an outage or degradation period, the in-band management link may not be available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is configured to use a dedicated management interface: # ifconfig -a eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500 inet 10.0.1.252 netmask 255.255.255.0 broadcast 10.0.1.255 inet6 fd80::21c:d8ff:fab7:1dba prefixlen 64 scopeid 0x20<link> ether 00:1a:b8:d7:1a:bf txqueuelen 1000 (Ethernet) RX packets 2295379 bytes 220126493 (209.9 MiB) RX errors 0 dropped 31 overruns 0 frame 0 TX packets 70507 bytes 12284940 (11.7 MiB) TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0 eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1458 inet 10.0.0.5 netmask 255.255.255.0 broadcast 10.0.0.255 inet6 fe81::21c:a8bf:fad7:1dca prefixlen 64 scopeid 0x20<link> ether 00:1d:d8:b5:1c:dd txqueuelen 1000 (Ethernet) RX packets 39090 bytes 4196802 (4.0 MiB) RX errors 0 dropped 0 overruns 0 frame 0 TX packets 93250 bytes 18614094 (17.7 MiB) TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0 If one of the interfaces listed is not dedicated to only process management traffic, this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-272405`

### Rule: The host running a BIND 9.x implementation must use an interface that is configured to process only DNS traffic.

**Rule ID:** `SV-272405r1123528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring hosts that run a BIND 9.x implementation to only accept DNS traffic on a DNS interface allows a system to be configured to segregate DNS traffic from all other host traffic. The TCP/IP stack in DNS hosts (stub resolver, caching/resolving/recursive name server, authoritative name server, etc.) could be subjected to packet flooding attacks (such as SYNC and smurf), resulting in disruption of communication. The use of a dedicated interface for DNS traffic allows for these threats to be mitigated by creating a means to limit what types of traffic can be processed using a host-based firewall solution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is configured to use an interface that is configured to process only DNS traffic. # ifconfig -a eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500 inet 10.0.1.252 netmask 255.255.255.0 broadcast 10.0.1.255 inet6 fd80::21c:d8ff:fab7:1dba prefixlen 64 scopeid 0x20<link> ether 00:1a:b8:d7:1a:bf txqueuelen 1000 (Ethernet) RX packets 2295379 bytes 220126493 (209.9 MiB) RX errors 0 dropped 31 overruns 0 frame 0 TX packets 70507 bytes 12284940 (11.7 MiB) TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0 eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1458 inet 10.0.0.5 netmask 255.255.255.0 broadcast 10.0.0.255 inet6 fe81::21c:a8bf:fad7:1dca prefixlen 64 scopeid 0x20<link> ether 00:1d:d8:b5:1c:dd txqueuelen 1000 (Ethernet) RX packets 39090 bytes 4196802 (4.0 MiB) RX errors 0 dropped 0 overruns 0 frame 0 TX packets 93250 bytes 18614094 (17.7 MiB) TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0 If one of the interfaces listed is not dedicated to only process DNS traffic, this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-272406`

### Rule: The platform on which the name server software is hosted must only run processes and services needed to support the BIND 9.x implementation.

**Rule ID:** `SV-272406r1123998_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Hosts that run the name server software must not provide any other services. Unnecessary services running on the DNS server can introduce additional attack vectors, leading to the compromise of an organization's DNS architecture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is dedicated for DNS traffic. With the assistance of the DNS administrator, identify all of the processes running on the BIND 9.x server: # ps -ef | less If any of the identified processes are not in support of normal OS functionality or in support of the BIND 9.x process, this is a finding.

## Group: SRG-APP-000516-DNS-000099

**Group ID:** `V-272407`

### Rule: The core BIND 9.x server files must be group owned by a group designated for DNS administration only.

**Rule ID:** `SV-272407r1123534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the premise that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired because of creating the object or via specified ownership assignment. In a DNS implementation, DAC should be granted to a minimal number of individuals and objects because DNS does not interact directly with users and users do not store and share data with the DNS application directly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the core BIND 9.x server files are group owned by a group designated for DNS administration only. With the assistance of the DNS administrator, identify the following files: named.conf root hints Primary zone file(s) Secondary zone file(s) Note: The name of the root hints file is defined in named.conf. Common names for the file are root.hints, named.cache, or db.cache. If the identified files are not group owned by a group designated for DNS administration, this is a finding.

## Group: SRG-APP-000516-DNS-000099

**Group ID:** `V-272408`

### Rule: The core BIND 9.x server files must be owned by the root or BIND 9.x process account.

**Rule ID:** `SV-272408r1124015_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the premise that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired because of creating the object or via specified ownership assignment. In a DNS implementation, DAC should be granted to a minimal number of individuals and objects because DNS does not interact directly with users and users do not store and share data with the DNS application directly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the core BIND 9.x server files are owned by the root or BIND 9.x process account. With the assistance of the DNS administrator, identify the following files: named.conf root hints Primary zone file(s) Secondary zone file(s) Note: The name of the root hints file is defined in named.conf. Common names for the file are root.hints, named.cache, or db.cache. If the identified files are not owned by the root or BIND 9.x process account, this is a finding.

## Group: SRG-APP-000516-DNS-000088

**Group ID:** `V-272410`

### Rule: On a BIND 9.x server, all authoritative name servers for a zone must have the same version of zone information.

**Rule ID:** `SV-272410r1124061_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is important to maintain the integrity of a zone file. The serial number of the SOA record is used to indicate to secondary name server that a change to the zone has occurred and a zone transfer should be performed. The serial number used in the SOA record provides the DNS administrator a method to verify the integrity of the zone file based on the serial number of the last update and ensure that all secondary servers are using the correct zone file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SOA record is at the same version for all authoritative servers for a specific zone. With the assistance of the DNS administrator, identify each name server that is authoritative for each zone. Inspect each zone file that the server is authoritative for and identify the following: example.com. 86400 IN SOA ns1.example.com. root.example.com. (17760704;serial) If the SOA "serial" numbers are not identical on each authoritative name server, this is a finding.

## Group: SRG-APP-000516-DNS-000114

**Group ID:** `V-272411`

### Rule: On the BIND 9.x server, CNAME records must not point to a zone with lesser security for more than six months.

**Rule ID:** `SV-272411r1124063_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of CNAME records for exercises, tests, or zone-spanning aliases should be temporary (e.g., to facilitate a migration). When a host name is an alias for a record in another zone, an adversary has two points of attack: the zone in which the alias is defined and the zone authoritative for the alias's canonical name. This configuration also reduces the speed of client resolution because it requires a second lookup after obtaining the canonical name. Furthermore, in the case of an authoritative name server, this information is promulgated throughout the enterprise to caching servers and thus compounds the vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the zone files used by the BIND 9.x server do not contain resource records for a domain in which the server is not authoritative. Inspect the "named.conf" file for the following: zone example.com { file "db.example.com.signed"; }; Inspect each zone file for "CNAME" records and verify with the DNS administrator that these records are less than six months old. The exceptions are glue records supporting zone delegations, CNAME records supporting a system migration, or CNAME records that point to third-party Content Delivery Networks (CDN) or cloud computing platforms. In the case of third-party CDNs or cloud offerings, an approved mission need must be demonstrated. If there are CNAME records that point to third-party Content Delivery Networks (CDNs) or cloud computing platforms without an authorizing official (AO)-approved and documented mission need, this is a finding. If a CNAME record is more than six months old, excluding the above, this is a finding.

## Group: SRG-APP-000516-DNS-000113

**Group ID:** `V-272412`

### Rule: On the BIND 9.x server, a zone file must not include resource records that resolve to a fully qualified domain name residing in another zone.

**Rule ID:** `SV-272412r1124064_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a name server were able to claim authority for a resource record in a domain for which it was not authoritative, this would pose a security risk. In this environment, an adversary could use illicit control of a name server to impact IP address resolution beyond the scope of that name server (i.e., by claiming authority for records outside of that server's zones). Fortunately, all but the oldest versions of BIND and most other DNS implementations do not allow for this behavior. Nevertheless, the best way to eliminate this risk is to eliminate from the zone files any records for hosts in another zone. The exceptions are glue records supporting zone delegations, CNAME records supporting a system migration, or CNAME records that point to third-party Content Delivery Networks (CDN) or cloud computing platforms. In the case of third-party CDNs or cloud offerings, an approved mission need must be demonstrated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the zone files used by the BIND 9.x server do not contain resource records for a domain in which the server is not authoritative. The exceptions are glue records supporting zone delegations, CNAME records supporting a system migration, or CNAME records that point to third-party Content Delivery Networks (CDN) or cloud computing platforms. In the case of third-party CDNs or cloud offerings, an approved mission need must be demonstrated. Inspect the "named.conf" file to identify the zone files, for which the server is authoritative: zone example.com { file "db.example.com.signed"; }; Inspect each zone file for which the server is authoritative. If there are CNAME records that point to third-party Content Delivery Networks (CDN) or cloud computing platforms without an authorizing official (AO)-approved and documented mission need, this is a finding. If a zone file contains records that resolve to another zone, excluding the above, this is a finding.

## Group: SRG-APP-000516-DNS-000105

**Group ID:** `V-272413`

### Rule: The BIND 9.x name server software must run with restricted privileges.

**Rule ID:** `SV-272413r1123923_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to application configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to application components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover). If the name server software is run as a privileged user (e.g., root in Unix systems), any break-in into the software can have disastrous consequences in terms of resources resident in the name server platform. Specifically, a hacker who breaks into the software acquires unrestricted access and therefore can execute any commands or modify or delete any files. It is necessary to run the name server software as a nonprivileged user with access restricted to specified directories to contain damages resulting from break-in.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIND 9.x process is not running as root: # ps -ef | grep named named 3015 1 0 12:59 ? 00:00:00 /usr/sbin/named -u named -t /var/named/chroot If the owner of the process is root, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-272414`

### Rule: The BIND 9.x implementation must not use a TSIG or DNSSEC key for more than one year.

**Rule ID:** `SV-272414r1123797_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements. Configuring the DNS server implementation to follow organizationwide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DOD that reflects the most restrictive security posture consistent with operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify all of the cryptographic key files used by the BIND 9.x implementation. With the assistance of the DNS administrator, determine the location of the cryptographic key files used by the BIND 9.x implementation. # ls -al <Crypto_Key_Location> -rw-------. 1 named named 76 May 10 20:35 crypto-example.key If the server is in a classified network, the DNSSEC portion of the requirement is Not Applicable. For DNSSEC keys: Verify that the "Created" date is less than one year from the date of inspection: Note: The date format will be displayed in YYYYMMDDHHMMSS. # cat <DNSSEC_Key_File> | grep -i "created" Created: 20160704235959 If the "Created" date is more than one year old, this is a finding. For TSIG keys: Verify with the information system security officer (ISSO)/information system security manager (ISSM) that the TSIG keys are less than one year old. If a TSIG key is more than one year old, this is a finding.

## Group: SRG-APP-000516-DNS-000099

**Group ID:** `V-272415`

### Rule: The permissions assigned to the core BIND 9.x server files must be set to use the least privilege possible.

**Rule ID:** `SV-272415r1123926_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the premise that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired because of creating the object or via specified ownership assignment. In a DNS implementation, DAC should be granted to a minimal number of individuals and objects because DNS does not interact directly with users and users do not store and share data with the DNS application directly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify the following files: named.conf : rw-r----- root hints : rw-r----- Primary zone file(s): rw-rw---- Secondary zone file(s): rw-rw---- Note: The name of the root hints file is defined in named.conf. Common names for the file are root.hints, named.cache, or db.cache. Verify that the permissions for the core BIND 9.x server files are at least as restrictive as listed above. If the identified files are not as least as restrictive as listed above, this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-272416`

### Rule: The host running a BIND 9.x implementation must implement a set of firewall rules that restrict traffic on the DNS interface.

**Rule ID:** `SV-272416r1124000_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring hosts that run a BIND 9.x implementation to only accept DNS traffic on a DNS interface allows a system firewall to be configured to limit the allowed incoming ports/protocols to 53/tcp and 53/udp. Sending outgoing DNS messages from a random port minimizes the risk of an attacker guessing the outgoing message port and sending forged replies. The TCP/IP stack in DNS hosts (stub resolver, caching/resolving/recursive name server, authoritative name server, etc.) could be subjected to packet flooding attacks (such as SYNC and smurf), resulting in disruption of communication. By implementing a specific set of firewall rules that limit accepted traffic to the interface, these risk of packet flooding and other TCP/IP based attacks is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, verify that the OS firewall is configured to only allow incoming messages on ports 53/tcp and 53/udp. Note: The following rules are for the IPTables firewall. If the system is using a different firewall, the rules may be different. Inspect the hosts firewall rules for the following rules: -A INPUT -i [DNS Interface] -p tcp --dport 53 -j ACCEPT -A INPUT -i [DNS Interface] -p udp --dport 53 -j ACCEPT -A INPUT -i [DNS Interface] -j DROP If any of the above rules do not exist, this is a finding. If rules are listed that allow traffic on ports other than 53/tcp and 53/udp, this is a finding.

## Group: SRG-APP-000348-DNS-000042

**Group ID:** `V-272417`

### Rule: A BIND 9.x server implementation must maintain the integrity and confidentiality of DNS information while it is being prepared for transmission, in transmission, and in use and must perform integrity verification and data origin verification for all DNS information.

**Rule ID:** `SV-272417r1124018_rule`
**Severity:** high

**Description:**
<VulnDiscussion>DNSSEC is required for securing the DNS query/response transaction by providing data origin authentication and data integrity verification through signature verification and the chain of trust. Failure to accomplish data origin authentication and data integrity verification could have significant effects on DNS infrastructure. The resultant response could be forged, it may have come from a poisoned cache, the packets could have been intercepted without the resolver's knowledge, or resource records could have been removed that would result in query failure or denial of service. Failure to validate name server replies would cause many networking functions and communications to be adversely affected. With DNS, the presence of Delegation Signer (DS) records associated with child zones informs clients of the security status of child zones. These records are crucial to the DNSSEC chain of trust model. Each parent domain's DS record is used to verify the DNSKEY record in its subdomain, from the top of the DNS hierarchy down. Failure to validate the chain of trust used with DNSSEC would have a significant impact on the security posture of the DNS server. Nonvalidated trust chains may contain rouge DNS servers and allow those unauthorized servers to introduce invalid data into an organization's DNS infrastructure. A compromise of this type would be difficult to detect and may have devastating effects on the validity and integrity of DNS zone information. Satisfies: SRG-APP-000348-DNS-000042, SRG-APP-000420-DNS-000053, SRG-APP-000213-DNS-000024, SRG-APP-000219-DNS-000028, SRG-APP-000219-DNS-000029, SRG-APP-000219-DNS-000030, SRG-APP-000215-DNS-000026, SRG-APP-000347-DNS-000041, SRG-APP-000349-DNS-000043, SRG-APP-000441-DNS-000066, SRG-APP-000442-DNS-000067, SRG-APP-000422-DNS-000055, SRG-APP-000421-DNS-000054, SRG-APP-000423-DNS-000056, SRG-APP-000424-DNS-000057, SRG-APP-000425-DNS-000058, SRG-APP-000426-DNS-000059, SRG-APP-000251-DNS-000037</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For a recursive server, verify that dnssec-validation yes is enabled. Inspect the "named.conf" file for the following: dnssec-validation yes; If "dnssec-validation yes" does not exist or is not set to "yes", this is a finding. For an authoritative server, verify that each zone on the name server has been signed. Identify each zone file for which the name server is responsible and search each file for the "DNSKEY" entries: # less <signed_zone_file> 86400 DNSKEY 257 3 8 ( HASHED_KEY ) ; KSK; alg = ECDSAP256SHA256; key id = 31225 86400 DNSKEY 256 3 8 ( HASHED_KEY ) ; ZSK; alg = ECDSAP256SHA256; key id = 52179 Verify that there are separate "DNSKEY" entries for the "KSK" and the "ZSK". If the "DNSKEY" entries are missing, the zone file is not signed. If the zone files are not signed, this is a finding.

## Group: SRG-APP-000350-DNS-000044

**Group ID:** `V-272418`

### Rule: In the event of an error when validating the binding of other DNS servers' identity to the BIND 9.x information, when anomalies in the operation of the signed zone transfers are discovered, for the success and failure of start and stop of the name server service or daemon, and for the success and failure of all name server events, a BIND 9.x server implementation must generate a log entry.

**Rule ID:** `SV-272418r1124003_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. It is essential for security personnel to know what is being performed on the system, where an event occurred, when an event occurred, and by whom the event was triggered to compile an accurate risk assessment. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or identify an improperly configured DNS system. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis. The DNS server must audit all failed attempts at server authentication through DNSSEC and TSIG. The actual auditing is performed by the OS/NDM, but the configuration to trigger the auditing is controlled by the DNS server. Failing to act on the validation errors may result in the use of invalid, corrupted, or compromised information. The validation of bindings can be achieved, for example, by the use of cryptographic checksums. Validations must be performed automatically. The DNS server does not have the capability of shutting down or restarting the information system. The DNS server can be configured to generate audit records when anomalies are discovered. Satisfies: SRG-APP-000350-DNS-000044, SRG-APP-000089-DNS-000005, SRG-APP-000504-DNS-000074, SRG-APP-000504-DNS-000082, SRG-APP-000474-DNS-000073</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the name server is configured to log error messages with a severity of "info": Inspect the "named.conf" file for the following: logging { channel channel_name { severity info; }; If the "severity" sub-statement is not set to "info", this is a finding. Note: Setting the "severity" sub-statement to "info" will log all messages for the following severity levels: Critical, Error, Warning, Notice, and Info.

## Group: SRG-APP-000142-DNS-000014

**Group ID:** `V-272419`

### Rule: The BIND 9.x server implementation must be configured to use only approved ports and protocols.

**Rule ID:** `SV-272419r1123570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements by providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIND 9.x server is configured to listen on UDP/TCP port 53. Inspect the "named.conf" file for the following: options { listen-on port 53 { <ip_address>; }; }; If the "port" variable is missing, this is a finding. If the "port" variable is not set to "53", this is a finding. Note: "<ip_address>" should be replaced with the DNS server IP address.

## Group: SRG-APP-000158-DNS-000015

**Group ID:** `V-272421`

### Rule: The BIND 9.x server implementation must use separate TSIG key-pairs when securing server-to-server transactions.

**Rule ID:** `SV-272421r1124019_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. This applies to server-to-server (zone transfer) transactions only and is provided by TSIG/SIG(0), which enforces mutual server authentication using a key that is unique to each server pair (TSIG) or using PKI-based authentication (SIG[0]), thus uniquely identifying the other server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is configured to use separate TSIG key-pairs when securing server-to-server transactions. Inspect the "named.conf" file for the presence of TSIG key statements: On the primary name server, this is an example of a configured key statement: key tsig_example. { algorithm hmac-SHA256; include "tsig-example.key"; }; zone "disa.mil" { type Primary; file "db.disa.mil"; allow-transfer { key tsig_example.; }; }; On the secondary name server, this is an example of a configured key statement: key tsig_example. { algorithm hmac-SHA256; include "tsig-example.key"; }; server <ip_address> { keys { tsig_example }; }; zone "disa.mil" { type Secondary; Primarys { <ip_address>; }; file "db.disa.mil"; }; Verify that each TSIG key-pair listed is only used by a single key statement: # cat <tsig_key_file> If any TSIG key-pair is being used by more than one key statement, this is a finding.

## Group: SRG-APP-000243-DNS-000034

**Group ID:** `V-272422`

### Rule: A BIND 9.x server implementation must be running in a chroot(ed) directory structure.

**Rule ID:** `SV-272422r1124005_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With any network service, there is the potential that an attacker can exploit a vulnerability within the program that allows the attacker to gain control of the process and even run system commands with that control. One possible defense against this attack is to limit the software to particular quarantined areas of the file system, memory, or both. This effectively restricts the service so that it will not have access to the full file system. If such a defense were in place, even if an attacker gained control of the process, the attacker would be unable to reach other commands or files on the system. This approach often is referred to as a padded cell, jail, or sandbox. All of these terms allude to the fact that the software is contained in an area where it cannot harm itself or others. A more technical term is a chroot(ed) directory structure. BIND must be configured to run in a padded cell or chroot(ed) directory structure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the directory structure where the primary BIND 9.x server configuration files are stored is running in a chroot(ed) environment or a containerized environment: # ps -ef | grep named named 3015 1 0 12:59 ? 00:00:00 /usr/sbin/named -u named -t /var/named/chroot If the output does not contain "-t <chroot_path>" and the named process is not running in a container, this is a finding.

## Group: SRG-APP-000246-DNS-000035

**Group ID:** `V-272423`

### Rule: A BIND 9.x implementation configured as a caching name server must restrict recursive queries to only the IP addresses and IP address ranges of known supported clients.

**Rule ID:** `SV-272423r1123940_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any host that can query a resolving name server has the potential to poison the server's name cache or take advantage of other vulnerabilities that may be accessed through the query service. The best way to prevent this type of attack is to limit queries to internal hosts, which need to have this service available to them. To guard against poisoning, name servers authoritative for .mil domains must be separated functionally from name servers that resolve queries on behalf of internal clients. Organizations may achieve this separation by dedicating machines to each function or, if possible, by running two instances of the name server software on the same machine: one for the authoritative function and the other for the resolving function. In this design, each name server process may be bound to a different IP address or network interface to implement the required segregation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is only applicable to caching name servers. Verify the allow-query and allow-recursion phrases are properly configured. Inspect the "named.conf" file for the following: allow-query {trustworthy_hosts;}; allow-recursion {trustworthy_hosts;}; The name of the ACL does not need to be "trustworthy_hosts", but the name must match the ACL name defined earlier in "named.conf" for this purpose. If not, this is a finding. Verify noninternal IP addresses do not appear in either the referenced ACL (e.g., trustworthy_hosts) or directly in the statements themselves. If noninternal IP addresses appear, this is a finding.

## Group: SRG-APP-000247-DNS-000036

**Group ID:** `V-272424`

### Rule: A BIND 9.x server implementation must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-272424r1124066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. A DoS attack against the DNS infrastructure has the potential to cause a DoS to all network users. As the DNS is a distributed backbone service of the internet, various forms of amplification attacks resulting in DoS, while using the DNS, are still prevalent on the internet today. Some potential DoS flooding attacks against the DNS include malformed packet flood, spoofed source addresses, and distributed DoS. Without the DNS, users and systems would not have the ability to perform simple name to IP resolution. Configuring the DNS implementation to defend against cache poisoning, employing increased capacity and bandwidth, building redundancy into the DNS architecture, using DNSSEC, limiting and securing recursive services, DNS black holes, etc., may reduce the susceptibility to some flooding types of DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is a recursive name server, this is not applicable. Excessive, almost-identical UDP responses can be controlled by configuring a rate-limit clause in an options or view statement. This mechanism keeps authoritative BIND 9 from being used to amplify reflection denial-of-service (DoS) attacks. Inspect the "named.conf" file for the following: options { ... rate-limit { responses-per-second <integer>; window <integer>; }; If the rate-limit sub-statements are missing, this is a finding.

## Group: SRG-APP-000214-DNS-000025

**Group ID:** `V-272425`

### Rule: A BIND 9.x server must provide secure delegation to all child zones.

**Rule ID:** `SV-272425r1123944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If name server replies are invalid or cannot be validated, many networking functions and communication would be adversely affected. With DNS, the presence of Delegation Signer (DS) records associated with child zones informs clients of the security status of child zones. These records are crucial to the DNSSEC chain of trust model. Each parent domain's DS record is used to verify the DNSKEY record in its subdomain, from the top of the DNS hierarchy down. A DNS server is an example of an information system providing name/address resolution service. Digital signatures and cryptographic keys are examples of additional artifacts. DNS resource records are examples of authoritative data. Applications other than the DNS, to map between host/service names and network addresses, must provide other means to ensure the authenticity and integrity of response data. In DNS, trust in the public key of the source is established by starting from a trusted name server and establishing the chain of trust down to the current source of response through successive verifications of signature of the public key of a child by its parent. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor. A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate. In DNS, a trust anchor is a DNSKEY that is placed into a validating resolver so the validator can cryptographically validate the results for a given request back to a known public key (the trust anchor). An example means to indicate the security status of child subspaces is using delegation signer (DS) resource records in the DNS. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Without path validation and a chain of trust, there can be no trust that the data integrity authenticity has been maintained during a transaction.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that there is a DS record set for each child zone defined in "/etc/named.conf" file. For each child zone listed in "/etc/named.conf" file, verify there is a corresponding "dsset-zone_name" file. If any child zone does not have a corresponding DS record set, this is a finding.

## Group: SRG-APP-000214-DNS-000079

**Group ID:** `V-272426`

### Rule: The BIND 9.x server validity period for the RRSIGs covering the DS RR for zones delegated children must be no less than two days and no more than one week.

**Rule ID:** `SV-272426r1124021_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The best way for a zone administrator to minimize the impact of a key compromise is by limiting the validity period of RRSIGs in the zone and in the parent zone. This strategy limits the time during which an attacker can take advantage of a compromised key to forge responses. An attacker that has compromised a zone-signing key (ZSK) can use that key only during the key signing key's (KSK's) signature validity interval. An attacker that has compromised a KSK can use that key for only as long as the signature interval of the RRSIG covering the DS RR in the delegating parent. These validity periods should be short, which will require frequent re-signing. To prevent the impact of a compromised KSK, a delegating parent should set the signature validity period for RRSIGs covering DS RRs in the range of a few days to 1 week. This re-signing does not require frequent rollover of the parent's ZSK, but scheduled ZSK rollover should still be performed at regular intervals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement does not validate the sig-validity-interval. This requirement ensures the signature validity period (i.e., the time from the signature's inception until the signature's expiration). It is recommended to ensure the Start of Authority (SOA) expire period (how long a secondary will still treat its copy of the zone data as valid if it cannot contact the primary) is configured to ensure the SOA does not expire during the period of signature inception and signature expiration. With the assistance of the DNS administrator, identify the RRSIGs that cover the DS resource records for each child zone. Each record will list an expiration and inception date, the difference of which will provide the validity period. The dates are listed in the following format: YYYYMMDDHHMMSS For each RRSIG identified, verify that the validity period is no less than two days and no longer than seven days. If the validity period is outside of the specified range, this is a finding.

## Group: SRG-APP-000231-DNS-000033

**Group ID:** `V-272427`

### Rule: Permissions assigned to the DNSSEC keys used with the BIND 9.x implementation must enforce read-only access to the key owner and deny access to all other users.

**Rule ID:** `SV-272427r1124022_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device within an organizational information system. Mobile devices, laptops, desktops, and storage devices can be either lost or stolen, and the contents of their data storage (e.g., hard drives and nonvolatile memory) can be read, copied, or altered. Applications and application users generate information throughout the course of their application use. The DNS server must protect the confidentiality and integrity of the DNSSEC keys and must protect the integrity of DNS information. There is no need to protect the confidentiality of DNS information because it is accessible by all devices that can contact the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify permissions assigned to the DNSSEC keys enforce read-only access to the key owner and deny access to group or system users. With the assistance of the DNS administrator, determine the location of the DNSSEC keys used by the BIND 9.x implementation: # ls -al <DNSSEC_Key_Location> -r--------. 1 named named 76 May 10 20:35 DNSSEC-example.key If the key files are more permissive than 400, this is a finding.

## Group: SRG-APP-000231-DNS-000033

**Group ID:** `V-272428`

### Rule: The DNSSEC keys used with the BIND 9.x implementation must be owned by a privileged account.

**Rule ID:** `SV-272428r1123761_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device within an organizational information system. Mobile devices, laptops, desktops, and storage devices can be either lost or stolen, and the contents of their data storage (e.g., hard drives and nonvolatile memory) can be read, copied, or altered. Applications and application users generate information throughout the course of their application use. The DNS server must protect the confidentiality and integrity of the DNSSEC keys and must protect the integrity of DNS information. There is no need to protect the confidentiality of DNS information because it is accessible by all devices that can contact the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify all of the DNSSEC keys used by the BIND 9.x implementation. Identify the account that the "named" process is running as: # ps -ef | grep named named 3015 1 0 12:59 ? 00:00:00 /usr/sbin/named -u named -t /var/named/chroot With the assistance of the DNS administrator, determine the location of the DNSSEC keys used by the BIND 9.x implementation. # ls -al <DNSSEC_Key_Location> -r--------. 1 named named 76 May 10 20:35 DNSSEC-example.key If any of the DNSSEC keys are not owned by the above account, this is a finding.

## Group: SRG-APP-000231-DNS-000033

**Group ID:** `V-272429`

### Rule: The DNSSEC keys used with the BIND 9.x implementation must be group owned by a privileged account.

**Rule ID:** `SV-272429r1123762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device within an organizational information system. Mobile devices, laptops, desktops, and storage devices can be either lost or stolen, and the contents of their data storage (e.g., hard drives and nonvolatile memory) can be read, copied, or altered. Applications and application users generate information throughout the course of their application use. The DNS server must protect the confidentiality and integrity of the DNSSEC keys and must protect the integrity of DNS information. There is no need to protect the confidentiality of DNS information because it is accessible by all devices that can contact the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the assistance of the DNS administrator, identify all of the DNSSEC keys used by the BIND 9.x implementation. Identify the account that the "named" process is running as: # ps -ef | grep named named 3015 1 0 12:59 ? 00:00:00 /usr/sbin/named -u named -t /var/named/chroot With the assistance of the DNS administrator, determine the location of the DNSSEC keys used by the BIND 9.x implementation. # ls -al <DNSSEC_Key_Location> -r--------. 1 named named 76 May 10 20:35 DNSSEC-example.key If any of the DNSSEC keys are not group owned by the above account, this is a finding.

## Group: SRG-APP-000125-DNS-000012

**Group ID:** `V-272430`

### Rule: The BIND 9.x server implementation must maintain at least three file versions of the local log file.

**Rule ID:** `SV-272430r1123947_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS software administrators require DNS transaction logs for a wide variety of reasons including troubleshooting, intrusion detection, and forensics. Ensuring that the DNS transaction logs are recorded on the local system will provide the capability needed to support these actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is configured to retain at least three versions of the local log file. Inspect the "named.conf" file for the following: logging { channel local_file_channel { file "path_name" versions 3; size 10m; }; If the "versions" variable is not defined, this is a finding. If the "versions" variable is configured to retain fewer than three versions of the local log file, this is a finding.

## Group: SRG-APP-000125-DNS-000012

**Group ID:** `V-272431`

### Rule: The BIND 9.x server implementation must be configured with a channel to send audit records to a local file.

**Rule ID:** `SV-272431r1123606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS software administrators require DNS transaction logs for a wide variety of reasons including troubleshooting, intrusion detection, and forensics. Ensuring that the DNS transaction logs are recorded on the local system will provide the capability needed to support these actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is configured to send audit logs to a local log file. Note: syslog and local file channel must be defined for every defined category. Inspect the "named.conf" file for the following: logging { channel local_file_channel { file "path_name" versions 3; print-time yes; print-severity yes; print-category yes; }; category category_name { local_file_channel; }; If a logging channel is not defined for a local file, this is a finding. If a category is not defined to send messages to the local file channel, this is a finding.

## Group: SRG-APP-000125-DNS-000012

**Group ID:** `V-272432`

### Rule: The BIND 9.x server implementation must be configured with a channel to send audit records to at least two remote syslogs.

**Rule ID:** `SV-272432r1123950_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Backing up audit records to a different system or onto separate media than the system being audited on a defined frequency helps to ensure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is configured to send audit logs to at least two syslog servers. Note: syslog and local file channel must be defined for every defined category. Inspect the "named.conf" file for the following: logging { channel <syslog_channel> { syslog <syslog_facility>; }; category <category_name> { <syslog_channel>; }; logging { channel <syslog_channel> { syslog <syslog_facility>; }; category <category_name> { <syslog_channel>; }; If a logging channel is not defined for each syslog, this is a finding. If a category is not defined to send messages to the syslog channels, this is a finding.

## Group: SRG-APP-000125-DNS-000012

**Group ID:** `V-272433`

### Rule: The BIND 9.x server implementation must not be configured with a channel to send audit records to null.

**Rule ID:** `SV-272433r1123612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS software administrators require DNS transaction logs for a wide variety of reasons including troubleshooting, intrusion detection, and forensics. Ensuring that the DNS transaction logs are recorded on the local system will provide the capability needed to support these actions. Sending DNS transaction data to the null channel would cause a loss of important data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the BIND 9.x server is not configured to send audit logs to the null channel. Inspect the "named.conf" file for the following: category null { null; } If there is a category defined to send audit logs to the "null" channel, this is a finding.

## Group: SRG-APP-000439-DNS-000063

**Group ID:** `V-272435`

### Rule: The BIND 9.x server implementation must uniquely identify and authenticate the other DNS server before responding to a server-to-server transaction, zone transfer, and/or dynamic update request using cryptographically based bidirectional authentication to protect the integrity of the information in transit.

**Rule ID:** `SV-272435r1124068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Server-to-server (zone transfer) transactions are provided by TSIG, which enforces mutual server authentication using a key that is unique to each server pair (TSIG), thus uniquely identifying the other server. DNS does perform server authentication when TSIG is used, but this authentication is transactional in nature (each transaction has its own authentication performed). Enforcing mutually authenticated communication sessions during zone transfers provides the assurance that only authorized servers are requesting and receiving DNS zone data. Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Failure to properly implement transactional security may have significant effects on the overall security of the DNS infrastructure. The lack of mutual authentication between name servers during a DNS transaction would allow a threat actor to launch a Man-In-The-Middle attack against the DNS infrastructure. This attack could lead to unauthorized DNS zone data being introduced, resulting in network traffic being redirected to a rogue site. Satisfies: SRG-APP-000439-DNS-000063, SRG-APP-000394-DNS-000049, SRG-APP-000395-DNS-000050, SRG-APP-000440-DNS-000065</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If zone transfers are disabled with the "allow-transfer { none; };" directive, this is not applicable. Verify that the BIND 9.x server is configured to uniquely identify a name server before responding to a zone transfer. Inspect the "named.conf" file for the presence of TSIG key statements. On the primary name server, this is an example of a configured key statement: key tsig_example. { algorithm hmac-SHA256; include "tsig-example.key"; }; zone "disa.mil" { type Primary; file "db.disa.mil"; allow-transfer { key tsig_example.; }; }; On the secondary name server, this is an example of a configured key statement: key tsig_example. { algorithm hmac-SHA256; include "tsig-example.key"; }; server <ip_address> { keys { tsig_example }; }; zone "disa.mil" { type Secondary; Primarys { <ip_address>; }; file "db.disa.mil"; }; If a primary name server does not have a key defined in the "allow-transfer" block, this is a finding. If a secondary name server does not have a server statement that contains a "keys" sub-statement, this is a finding.

## Group: SRG-APP-000514-DNS-000075

**Group ID:** `V-272436`

### Rule: A BIND 9.x server must implement NIST FIPS-validated cryptography for provisioning digital signatures and generating cryptographic hashes.

**Rule ID:** `SV-272436r1123956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the DNSSEC and TSIG keys used by the BIND 9.x implementation are FIPS compliant. If the server is in a classified network, the DNSSEC portion of the requirement is Not Applicable. DNSSEC keys: Inspect the "named.conf" file and identify all of the DNSSEC signed zone files: zone "example.com" { file "signed_zone_file"; }; For each signed zone file identified, inspect the file for the "DNSKEY" records: 86400 DNSKEY 257 3 8 ( <KEY HASH> ) ; KSK; 86400 DNSKEY 256 3 8 ( <KEY HASH> ) ; ZSK; The fifth field in the above example identifies what algorithm was used to create the DNSKEY. If the fifth field, if the KSK DNSKEY is less than "8" (SHA256), this is a finding. If the algorithm used to create the ZSK is less than "8" (SHA256), this is a finding. TSIG keys: Inspect the "named.conf" file and identify all of the TSIG key statements: key tsig_example. { algorithm hmac-SHA256; include "tsig-example.key"; }; If each key statement does not use "hmac-SHA256" or a stronger algorithm, this is a finding.

## Group: SRG-APP-000516-DNS-000500

**Group ID:** `V-275935`

### Rule: The BIND 9.x server implementation must have QNAME minimization set to "strict".

**Rule ID:** `SV-275935r1124025_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>QNAME minimization limits the amount of information sent in DNS queries to intermediate nameservers, improving privacy by reducing the potential for DNS leak. It modifies the flow of DNS queries to reveal only what is necessary for the current server to find the next one in the resolution chain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify QNAME minimization is set to "strict". Inspect the named.conf file for the following: options { qname-minimization strict; If the qname minimization is not set to "strict", this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-275936`

### Rule: The BIND 9.x server implementation must have fetches-per-zone enabled.

**Rule ID:** `SV-275936r1124069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The fetches-per-zone option in BIND 9.x is a configuration parameter that controls the maximum number of simultaneous iterative queries a recursive resolver can send to a single authoritative server for a specific domain. This helps protect authoritative servers from being overwhelmed by queries, especially during a denial-of-service (DoS) attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify fetches-per-zone is enabled with an organization-defined number. Inspect the named.conf file for the following: options { fetches-per-zone <integer> drop ; If fetches-per-zone is not enabled and set to drop, this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-275937`

### Rule: The BIND 9.x server implementation must have fetches-per-server enabled.

**Rule ID:** `SV-275937r1123965_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The fetches-per-server option in BIND 9.x configures a limit on the number of outstanding requests (fetches) allowed for a single DNS server. This rate-limiting mechanism helps protect the BIND 9.x server from being overwhelmed by excessive requests to a specific server, particularly when that server is slow or unresponsive. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify fetches-per-server is enabled with an organization-defined number. Inspect the named.conf file for the following: options { fetches-per-server <integer> drop ; If fetches-per-server is not enabled and set to drop, this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-275938`

### Rule: The host running a BIND 9.x implementation must have DNS cookies enabled.

**Rule ID:** `SV-275938r1123968_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS cookies can help prevent spoofing and cache poisoning attacks by verifying the identity of both the client and server. They do this by including a cryptographic identifier (the cookie) in DNS messages, which can be verified in future messages. This makes it difficult for an attacker to learn the cookie values and thus spoof them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify answer-cookie is enabled. Inspect the named.conf file for the following: options { answer-cookie yes; If answer-cookie is missing or set to "no", this is a finding.

## Group: SRG-APP-000516-DNS-000109

**Group ID:** `V-275939`

### Rule: The BIND 9.x server implementation must limit the  number of allowed dynamic update clients.

**Rule ID:** `SV-275939r1123971_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of concurrent sessions reduces the risk of denial of service (DoS) to the DNS implementation. Name servers do not have direct user connections but accept client connections for queries. Original restriction on client connections should be high enough to prevent a self-imposed denial of service, after which the connections are monitored and fine-tuned to best meet the organization's specific requirements. Primary name servers also make outbound connections to secondary name servers to provide zone transfers and accept inbound connection requests from clients wishing to provide a dynamic update. Primary name servers should explicitly limit zone transfers to be made only to designated secondary name servers. Because zone transfers involve the transfer of entire zones and use TCP connections, they place substantial demands on network resources relative to normal DNS queries. Errant or malicious frequent zone transfer requests on the name servers of the enterprise can overload the primary zone server and result in DoS to legitimate users. Primary name servers should be configured to limit the hosts from which they will accept dynamic updates. Additionally, the number of concurrent clients, especially TCP clients, must be kept to a level that does not risk placing the system in a DoS state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the update-quota option is present and set to an organization defined limit. Inspect the named.conf file for the following options { ... update-quota <integer>; ... }; If update-quota option is missing or limit not set, this is a finding.

