# STIG Benchmark: RUCKUS ICX NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-273784`

### Rule: The RUCKUS ICX device must be configured to assign appropriate user roles or access levels to authenticated users.

**Rule ID:** `SV-273784r1111052_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Successful identification and authentication must not automatically give an entity full access to a network device or security domain. The lack of authorization-based access control could result in the immediate compromise of and unauthorized access to sensitive information. All DOD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset or set of resources. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Some network devices are preconfigured with security groups. Other network devices enable operators to create custom security groups with custom permissions. For example, an information system security manager (ISSM) may require read-only access to audit the network device. Operators may create an audit security group, define permissions and access levels for members of the group, and then assign the ISSM's user persona to the audit security group. This is still considered privileged access, but the ISSM's security group is more restrictive than the network administrator's security group. Network devices that rely on AAA brokers for authentication and authorization services may need to identify the available security groups or access levels available on the network devices and convey that information to the AAA operator. Once the AAA broker identifies the user persona on the centralized directory service, the user's security group memberships can be retrieved. The AAA operator may need to create a mapping that links target security groups from the directory service to the appropriate security groups or access levels on the network device. Once these mappings are configured, authorizations can happen dynamically, based on each user's directory service group membership.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the network device is configured to assign appropriate user roles or access levels to authenticated users. 1. Confirm login authentication is configured for a AAA server followed by local authentication. SSH@ICX(config)# show running-config | include (aaa.*login|aaa.*exec) aaa authentication login default radius local aaa authorization exec default radius 2. Verify local accounts have desired privilege levels. SSH@ICX# show user Username Password Encrypt Priv Status Expire Time ====================================================================================================================== local $1$b6Mn/o0q$/HIqAT.num4n80Pyd0um7 enabled 0 enabled Never If using a AAA for authentication and "aaa authorization exec" line is not present, this is a finding. If the local user account does not have the correct privilege level assigned, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-273785`

### Rule: The RUCKUS ICX device must enforce approved authorizations for controlling the flow of management information within the network device based on information flow control policies.

**Rule ID:** `SV-273785r1110836_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify management access is limited to the desired subnets: SSH@ICX(config)# show management access management access src-ip 192.168.1.0 255.255.255.0 allow ssh If the ICX switch does not enforce approved authorizations for controlling the flow of management information within the device based on information control policies, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-273786`

### Rule: The RUCKUS ICX device must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-273786r1110837_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to verify that it enforces the limit of three consecutive invalid logon attempts. show running-config | include disable-on-login-failure enable user disable-on-login-failure 3 login-recovery-time in-secs 900 If the device is not configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-273787`

### Rule: The RUCKUS ICX device must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-273787r1110838_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users. Satisfies: SRG-APP-000068-NDM-000215, SRG-APP-000069-NDM-000216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for presence of "banner motd ..." command and verify the subsequent text complies: show running-config | begin banner If the Standard Mandatory DOD Notice and Consent Banner is not configured, this is a finding.

## Group: SRG-APP-000092-NDM-000224

**Group ID:** `V-273788`

### Rule: The RUCKUS ICX device must initiate session auditing upon startup.

**Rule ID:** `SV-273788r1110839_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the startup process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Satisfies: SRG-APP-000092-NDM-000224, SRG-APP-000026-NDM-000208, SRG-APP-000027-NDM-000209, SRG-APP-000028-NDM-000210, SRG-APP-000029-NDM-000211, SRG-APP-000080-NDM-000220, SRG-APP-000091-NDM-000223, SRG-APP-000095-NDM-000225, SRG-APP-000096-NDM-000226, SRG-APP-000097-NDM-000227, SRG-APP-000098-NDM-000228, SRG-APP-000099-NDM-000229, SRG-APP-000100-NDM-000230, SRG-APP-000319-NDM-000283, SRG-APP-000343-NDM-000289, SRG-APP-000381-NDM-000305, SRG-APP-000495-NDM-000318, SRG-APP-000499-NDM-000319, SRG-APP-000503-NDM-000320, SRG-APP-000504-NDM-000321, SRG-APP-000505-NDM-000322, SRG-APP-000506-NDM-000323, SRG-APP-000516-NDM-000334</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that logging is enabled: SSH@ICX(config)# show running-config | include logging logging console logging persistence logging cli-command logging host x.x.x.x logging host y.y.y.y If "no logging on" exists, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-273789`

### Rule: The RUCKUS ICX device must generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-273789r1110840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging is enabled: SSH@ICX(config)# show running-config | include logging logging console logging persistence logging cli-command logging host x.x.x.x logging host y.y.y.y If "logging cli-command" is not present or "no logging on" exists, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-273798`

### Rule: The RUCKUS ICX device must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services

**Rule ID:** `SV-273798r1110830_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the configuration for unnecessary/nonsecure functions including any of the below commands: ip dns server … web-management http web-management https telnet server ip proxy-arp If the above or any other service/function deemed unnecessary or unsecure is listed, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-273799`

### Rule: The RUCKUS ICX device must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-273799r1110841_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit must be added to the envelope as a record. Administrators must secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View configuration for locally defined user accounts: SSH@ICX(config)#show running-config | include username If there is more than one locally defined user account, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-273802`

### Rule: The RUCKUS ICX device must enforce password complexity and length requirements.

**Rule ID:** `SV-273802r1110842_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Satisfies: SRG-APP-000164-NDM-000252, SRG-APP-000166-NDM-000254, SRG-APP-000167-NDM-000255, SRG-APP-000168-NDM-000256, SRG-APP-000169-NDM-000257</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify strict password enforcement is configured: SSH@ICX(config)#show running-config | include strict-password-enforcement If strict-password-enforcement is not configured, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-273808`

### Rule: The RUCKUS ICX device must use FIPS 140-2/140-3 approved algorithms for authentication to a cryptographic module.

**Rule ID:** `SV-273808r1111022_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not validated and therefore cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms. Satisfies: SRG-APP-000179-NDM-000265, SRG-APP-000156-NDM-000250, SRG-APP-000172-NDM-000259, SRG-APP-000411-NDM-000330, SRG-APP-000412-NDM-000331, SRG-APP-000880-NDM-000290</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the FIPS module has been enabled. Router#fips show Cryptographic Module Version: FI-IP-CRYPTO FIPS mode: Administrative status ON: Operational status ON Common-Criteria: Administrative status ON: Operational status ON System Specific: OS monitor access status is: Disabled Management Protocol Specific: Telnet server: Disabled Telnet client: Disabled TFTP client: Disabled SNMP Access to security objects: Disabled Critical security Parameter updates across FIPS boundary: Protocol Shared secret and host passwords: Clear Password Display: Disabled Certificate Specific: HTTPS RSA Host Keys and Signature: Clear SSH DSA Host keys: Clear SSH RSA Host keys: Clear CC Enable AAA Server Any: Retain If the fips show command does not output "FIPS mode: Administrative status ON: Operational status ON", this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-273809`

### Rule: The RUCKUS ICX device must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after five minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-273809r1110832_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check CLI configuration: SSH@ICX(config)#show cli config CLI Session Configuration session timeout : 5 min skip-page mode : disabled skip-page config : disabled rconsole-off : disabled alias : There are no entries in the alias list. If the idle timeout is greater than five minutes or equal to 0 (i.e., no timeout), this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-273820`

### Rule: The RUCKUS ICX device must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-273820r1110843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure network devices have a sufficient storage capacity in which to write the audit logs, they must be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the log size complies with organization-defined audit record storage: ICX# show logging Syslog logging: enabled ( 0 messages dropped, 0 flushes, 7 overruns) Buffer logging: level ACDMEINW, 4000 messages logged level code: A=alert C=critical D=debugging M=emergency E=error I=informational N=notification W=warning Static Log Buffer: May 01 19:30:50:I:System: Stack unit 1 POE PS 1, Internal Power supply with 370000 mwatts capacity is up May 01 19:30:55:I:System: Stack unit 1 Fan 1 (Rear Side Right), ok May 01 19:30:55:I:System: Stack unit 1 Fan 2 (Rear Side Left), ok Dynamic Log Buffer (4000 lines): Jul 31 14:24:54:I:CLI CMD: "show logging" by local user from ssh If the size of the Dynamic Log Buffer does not meet organization-defined audit record storage requirements, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-273821`

### Rule: The RUCKUS ICX device must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-273821r1111025_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in UTC, a modern continuation of GMT, or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a time zone is configured on the device: SSH@ICX# show clock 15:13:51.679 GMT+00 Mon Jan 15 2024 If the time does not reflect a time zone that can be mapped to GMT, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-273825`

### Rule: The RUCKUS ICX device must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-273825r1110845_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View SNMP users: SSH@ICX# show snmp user username = admin1 acl name = <none> group = lab security model = v3 group acl name = <none> group ipv6 acl name = <none> authtype = sha authkey = 6e3e368283194dffcdabde95c9c44e795de911c2 privtype = aes privkey = c8b94fccfc1c845ed8a0d7b172405feb engine ID= 80 0 7c7 3d4c19e609a58 If any users are not configured for authtype sha, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-273826`

### Rule: The RUCKUS ICX device must authenticate Network Time Protocol sources using authentication that is cryptographically based.

**Rule ID:** `SV-273826r1110846_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol (NTP) is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View NTP configuration: SSH@ICX# show running-config | begin ntp ntp disable authenticate md5 authenticate authentication-key key-id 1 sha1 2 $VWlkRGkt server x.x.x.x key 1 server y.y.y.y key 1 If the NTP servers are not configured for authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-273829`

### Rule: The RUCKUS ICX device must be configured to protect against known types of denial-of-service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-273829r1110847_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition that occurs when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DOD-level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check whether DDoS protection in place: SSH@ICX# show running-config | include burst ip icmp attack-rate burst-normal 50 burst-max 100 lockup 300 ip tcp burst-normal 30 burst-max 100 lockup 300 * burst-normal, burst-max, and lockup values may vary by site. If the switch is not configured with DDoS protection this is a finding.

## Group: SRG-APP-000457-NDM-000352

**Group ID:** `V-273830`

### Rule: Security-relevant firmware updates must be installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-273830r1110848_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with firmware are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant firmware updates. Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant firmware may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install firmware patches across the enclave (e.g., mobile device management solutions). Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant firmware updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant firmware updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain evidence that firmware updates are consistently applied to the network device within the time frame defined for each patch. If such evidence cannot be obtained, or the evidence that is obtained indicates a pattern of noncompliance, this is a finding. If the network device does not install security-relevant updates within the time period directed by the authoritative source, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-273832`

### Rule: The RUCKUS ICX device must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-273832r1110849_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-APP-000515-NDM-000325, SRG-APP-000360-NDM-000295</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify external syslog server is configured and online: show running-config | include logging host If there is no output or the host displayed is unreachable, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-273835`

### Rule: The RUCKUS ICX device must be configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access.

**Rule ID:** `SV-273835r1110833_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's RUCKUS ICX devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each RUCKUS ICX device. Satisfies: SRG-APP-000516-NDM-000336, SRG-APP-000700-NDM-000100, SRG-APP-000705-NDM-000110</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AAA authentication and authorization are configured along with RADIUS/TACACS+ servers. SSH@ICX#show running-config | include (aaa|radius) aaa authentication dot1x default radius radius-server host x.x.x.x auth-port 1812 acct-port 1813 default key 2 $VWlkRGkt dot1x mac-auth radius-server host y.y.y.y auth-port 1812 acct-port 1813 default key 2 $UGlkRGktdG5v dot1x mac-auth radius-server key 2 $UGlkRGktdG5v aaa authentication login default radius local aaa authorization commands 0 default radius aaa authorization exec default radius If two central authentication servers are not configured, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-273838`

### Rule: The RUCKUS ICX device must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-273838r1110850_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this certification authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the certificate used by the system using the command: SSH@ICX# show ip ssl device-certificate Certificate: Data: Version: 3 (0x2) Serial Number: 3488150 (0x353996) Signature Algorithm: sha256WithRSAEncryption Issuer: CN=RuckusPKI-DeviceSubCA-2, O=Ruckus Wireless Inc., L=Sunnyvale, ST=California, C=US Validity Not Before: Jun 9 09:40:52 2023 GMT Not After : Jun 9 09:40:52 2048 GMT Subject: CN=SN-FNNxxxxxxxx, O=Ruckus Wireless Inc., L=Sunnyvale, ST=California, C=US Subject Public Key Info: Public Key Algorithm: rsaEncryption Public-Key: (2048 bit) Modulus: 00:c5:c0:60:9a:cb:4a:a3:9f:fb:63:c6:21:c2:55: 1f:66:95:f2:9a:fb:eb:37:33:d1:73:28:4b:14:8a: ... If the certificate is not from an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-273839`

### Rule: The RUCKUS ICX device must be configured to send log data to at least two central log servers for the purpose of forwarding alerts to the administrators and the information system security officer (ISSO).

**Rule ID:** `SV-273839r1110834_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can be used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging is enabled: SSH@ICX(config)# show running-config | include logging logging console logging persistence logging cli-command logging host x.x.x.x logging host y.y.y.y If the site does not have two or more logging hosts, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-273840`

### Rule: The RUCKUS ICX device  must be running an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-273840r1110835_rule`
**Severity:** high

**Description:**
<VulnDiscussion>RUCKUS ICX devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use "show version" to determine the version being used. Verify with the RUCKUS Networks support portal that the release is supported. If the switch is not running at the most current federally compliant release, this is a finding.

## Group: SRG-APP-000910-NDM-000300

**Group ID:** `V-273848`

### Rule: The RUCKUS ICX device must be configured to include only approved trust anchors in trust stores or certificate stores managed by the organization.

**Rule ID:** `SV-273848r1111027_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Public key infrastructure (PKI) certificates are certificates with visibility external to organizational systems and certificates related to the internal operations of systems, such as application-specific time services. In cryptographic systems with a hierarchical structure, a trust anchor is an authoritative source (i.e., a certificate authority) for which trust is assumed and not derived. A root certificate for a PKI system is an example of a trust anchor. A trust store or certificate store maintains a list of trusted root certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the network device is configured to include only approved trust anchors in trust stores or certificate stores managed by the organization. Verify Device Certificate: device# show ip ssl device-certificate Certificate: Data: Version: 3 (0x2) Serial Number: 238779085 (0xe3b7acd) Signature Algorithm: sha256WithRSAEncryption Issuer: C=US, ST=fe044db7a0ec05cf9736bfbcc2e186a76da5a13e49b1f12c8717e5c5bf5c32f2, L=10.176.156.30, O=cc:4e:24:8c:67:e8, OU=JLSAWZOIFZMD, CN=ICX Validity Not Before: Dec 3 22:40:24 2019 GMT Not After : Nov 19 22:40:24 2079 GMT Subject: C=US, ST=fe044db7a0ec05cf9736bfbcc2e186a76da5a13e49b1f12c8717e5c5bf5c32f2, L=10.176.156.30, O=cc:4e:24:8c:67:e8, OU=JLSAWZOIFZMD, CN=ICX Subject Public Key Info: Public Key Algorithm: rsaEncryption Public-Key: (2048 bit) Modulus: 00:9f:87:35:01:dd:c3:63:52:7b:9d:aa:13:b7:39: a9:0a:12:51:84:6e:57:ed:62:65:b7:79:31:72:35: 08:9a:d8:36:8b:f3:c8:76:47:90:5f:88:37:bc:6b: 1d:1f:5c:fd:0e:94:2d:7b:3a:54:d0:17:3c:96:d7: be:a5:d8:0a:9c:54:08:08:30:06:84:a3:cb:1c:9f: e0:ab:25:ac:59:02:7e:7b:cd:c2:bf:58:8d:63:09: Verify SSL Certificate: device(config)# show ip ssl certificate Trusted Certificates: Dynamic: Index 0: Signature Algorithm: sha256WithRSAEncryption Issuer: CN: 10.25.105.201 Validity: Not Before: 2014 Aug 22 05:12:45 Not After : 2079 Aug 21 05:12:45 Subject: CN: 10.25.105.201 X509v3 extensions: X509v3 Subject Alternative Name: IP Address: 10.25.105.201 Signature: 12:ec:41:d8:01:45:61:ce:cf:7e:80:de:a6:7c:a7:2e:01:7f: 42:27:22:1d:ac:a2:47:c5:0d:4f:e3:68:24:de:bf:50:40:65: 25:8c:30:bd:ff:a7:d0:21:73:d2:ba:5e:67:42:1f:bb:97:4a: d9:1d:c3:ca:31:c4:59:10:79:d1:42:f4:b6:1a:b0:98:4e:a8: ef:e2:a2:98:c3:14:16:63:50:02:a0:18:9c:7a:e3:17:39:0d: b7:30:ab:23:9f:63:bd:0f:9e:d8:67:b0:fe:ec:3b:fa:4c:f4: 3d:34:e2:99:0e:99:24:ec:93:fb:8a:e5:4a:bf:74:d6:ff:91: 0a:dc:fb:b9:4f:91:5d:d4:f6:77:23:eb:ec:eb:3a:62:08:e1: a6:ea:a8:52:b6:39:62:db:29:fa:61:1d:fd:d5:02:31:04:73: 50:ad:de:41:54:a5:e2:96:2d:9c:f4:68:b2:68:05:bb:39:47: ee:74:89:a2:8c:30:f0:f9:d7:d5:4b:3b:e2:95:6f:82:61:a3: c2:79:4c:f2:11:56:f8:2f:cc:fc:2b:4b:cb:3b:54:59:f0:8b: 5b:70:e1:27:c3:57:25:eb:35:c6:07:ea:6d:0b:34:04:95:81: 35:e6:64:c6:b8:72:e8:24:18:bd:ca:90:99:74:45:44:85:71: 9e:7f:13:96: If the network device is not configured to include only approved trust anchors in trust stores or certificate stores managed by the organization, this is a finding.

## Group: SRG-APP-000920-NDM-000320

**Group ID:** `V-273850`

### Rule: The RUCKUS ICX device must be configured to synchronize system clocks within and between systems or system components.

**Rule ID:** `SV-273850r1111029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Time synchronization of system clocks is essential for the correct execution of many system services, including identification and authentication processes that involve certificates and time-of-day restrictions as part of access control. Denial of service or failure to deny expired credentials may result without properly synchronized clocks within and between systems and system components. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. The granularity of time measurements refers to the degree of synchronization between system clocks and reference clocks, such as clocks synchronizing within hundreds of milliseconds or tens of milliseconds. Organizations may define different time granularities for system components. Time service can be critical to other security capabilities such as access control and identification and authentication depending on the nature of the mechanisms used to support the capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the network device is configured to synchronize system clocks within and between systems or system components: device#show ntp association address Domain name Reference Clock st when poll Reach delay offset disp ~ 216.239.35.8 None 1 1 64 1 34.449 21474836 187.55 * synced, # selected, + candidate, - outlayer, x falseticker, ~ configured, **More characters in domain name If the network device is not configured to synchronize system clocks within and between systems or system components, this is a finding.

## Group: SRG-APP-000925-NDM-000330

**Group ID:** `V-273851`

### Rule: The RUCKUS ICX device must be configured to compare the internal system clocks on an organization-defined frequency with two organization-defined authoritative time sources.

**Rule ID:** `SV-273851r1110853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Synchronization of internal system clocks with an authoritative source provides uniformity of time stamps for systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NTP is configured and synchronizing with two peers: device#show ntp association address Domain name Reference Clock st when poll Reach delay offset disp *~ 216.239.35.8 None GOOG 1 56 64 377 30.444 2.0021 2.884 +~ 23.150.40.242 pool.ntp.org 204.9.54.119 2 61 64 377 44.339 -0.6625 1.220 * synced, # selected, + candidate, - outlayer, x falseticker, ~ configured, **More characters in domain name

