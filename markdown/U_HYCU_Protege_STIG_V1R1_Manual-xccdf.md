# STIG Benchmark: HYCU Protege Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000920-NDM-000320

**Group ID:** `V-268216`

### Rule: The HYCU virtual appliance must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-268216r1038348_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must use an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source. Satisfies: SRG-APP-000920-NDM-000320, SRG-APP-000925-NDM-000330</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "chronyd" service is up and running, execute the following command: systemctl status chronyd If service is not active (running), this is a finding. To verify chronyd has synced time and can reach the servers execute the following command: chronyc sources If there are not two NTP servers listed, this is a finding. If the "Reach" value is lower than "377" for the source with S column marked with "*" this is a finding.

## Group: SRG-APP-000845-NDM-000220

**Group ID:** `V-268217`

### Rule: The HYCU virtual appliance must not have any default manufacturer passwords when deployed.

**Rule ID:** `SV-268217r1038727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virtual machines not protected with strong password schemes provide the opportunity for anyone to crack the password and gain access to the device, which can result in loss of availability, confidentiality, or integrity of network traffic. Many default vendor passwords are well known or are easily guessed; therefore, not removing them prior to deploying the network device into production provides an opportunity for a malicious user to gain unauthorized access to the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console with the default vendor credentials. If the login to the console is successful with the default credentials, this is a finding. Log in to the HYCU Web UI with the default vendor credentials. If the login to the HYCU Web UI is successful with the default credentials, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-268219`

### Rule: The HYCU virtual appliance must limit the number of concurrent sessions to an organization-defined number for each administrator account and/or administrator account type.

**Rule ID:** `SV-268219r1038638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the HYCU Web UI, only one login can be used at a time. If the user is still logged into the HYCU Web UI upon logging in to the Web UI again, in a different browser tab, with the same credentials, this is a finding. Log in to the HYCU VM console. To check the number of allowed concurrent session connections, grep file "/etc/security/limits.conf" by executing the following command: grep maxlogins /etc/security/limits.conf Verify the following line exists: hycu hard maxlogins 1 If the "maxlogins" value is not set to 1 or is missing, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-268222`

### Rule: The HYCU virtual appliance must enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level in accordance with applicable policy for the device.

**Rule ID:** `SV-268222r1038366_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Network devices use access control policies and enforcement mechanisms to implement this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Self-Service menu within HYCU to view accounts and user roles (Administrator, Backup Operator, Restore Operator, Backup and Restore Operator, or Viewer). User roles have a predefined and nonchangeable set of user privileges. To check exact set of privileges of each user, navigate to Self-Service context in the HYCU UI. Click on the question mark in the upper-right corner, followed by "Help with This Page". Scroll down to the "User Roles" section. If users can perform more functions than those specified for their role, this is a finding.

## Group: SRG-APP-000329-NDM-000287

**Group ID:** `V-268223`

### Rule: If the HYCU virtual appliance uses role-based access control, it must enforce organization-defined role-based access control policies over defined subjects and objects.

**Rule ID:** `SV-268223r1038369_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on organizational information systems associated with the organization-defined roles. When administrators are assigned to the organizational roles, they inherit the authorizations or privileges defined for those roles. Role-Based Access Control (RBAC) simplifies privilege administration for organizations because privileges are not assigned directly to every administrator (which can be a significant number of individuals for mid- to large-size organizations) but are instead acquired through role assignments. RBAC can be implemented either as a mandatory or discretionary form of access control. The RBAC policies and the subjects and objects are defined uniquely for each network device, so they cannot be specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
HYCU offers the capability to leverage RBAC controls within the Web UI's Self-Service menu. The organization would need to generate and document its own specific requirements around using RBAC in HYCU. For the HYCU VM console, administrators should only allow access to anyone else deemed to be qualified as a server administrator for the system. Review the groups and accounts within Web UI's Self-Service menu. If any RBAC setting does not meet the organization's guidelines, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-268225`

### Rule: The HYCU virtual appliance must enforce approved authorizations for controlling the flow of management information within the appliance based on information flow control policies.

**Rule ID:** `SV-268225r1038375_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Satisfies: SRG-APP-000038-NDM-000213, SRG-APP-000880-NDM-000290</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the firewall is running by executing the following command: sudo firewall-cmd --state If service is not running, this is a finding. Determine which services and ports are open by executing the following command: sudo firewall-cmd --list-all Output should show the following two lines: 'services: cockpit dhcpv6-client iscsi-target samba ssh' 'ports: 8443/tcp' If more services than those listed above are open, this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-268226`

### Rule: The HYCU virtual appliance must audit the execution of privileged functions.

**Rule ID:** `SV-268226r1038378_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of the "/var/log/audit/audit.log" file. HYCU also maintains Event (Audit) information in the HYCU Web UI Events menu. Verify the audit log contains records showing when the execution of privileged functions occurred. If the audit log is not configured or does not have the required contents, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-268227`

### Rule: The HYCU virtual appliance must be configured to enforce the limit of three consecutive invalid login attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-268227r1038750_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console and go to the "/etc/pam.d/" folder. Verify that "password-auth" and "system-auth" contain the following three lines, and the values for deny and unlock_time are as shown. Commands: sudo grep pam_faillock.so /etc/pam.d/password-auth sudo grep pam_faillock.so /etc/pam.d/system-auth Both should displays the following three lines: auth required pam_faillock.so preauth silent audit deny=3 even_deny_root fail_interval=60 unlock_time=900 auth required pam_faillock.so authfail audit unlock_time=900 account required pam_faillock.so If the required content is not present, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-268228`

### Rule: The HYCU virtual appliance must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-268228r1038752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console and verify the banner setting is in use in the "/etc/ssh/sshd_config" file by executing the following command: grep Banner /etc/ssh/sshd_config If the banner is not set to "/etc/issue", this is a finding. Verify "/etc/issue" contains valid DOD notice text by executing the following command: sudo cat /etc/issue If the DOD notice is not present in the "/etc/issue" file, this is a finding. Open the HYCU Web UI login page and verify the mandatory notice is present on the welcome page. If the mandatory notice is not present at the HYCU Web UI welcome page, this is a finding.

## Group: SRG-APP-000069-NDM-000216

**Group ID:** `V-268229`

### Rule: The HYCU virtual appliance must retain the Standard Mandatory DOD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log in for further access.

**Rule ID:** `SV-268229r1038748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the administrator prior to the device allowing the administrator access to the network device. This provides assurance that the administrator has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the administrator, DOD will not comply with system use notifications required by law.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console and verify the banner setting is in use in the "/etc/ssh/sshd_config" file by executing the following command: grep Banner /etc/ssh/sshd_config If the banner is not set to "/etc/issue", this is a finding. Verify "/etc/issue" contains valid DOD notice text by executing the following command: sudo cat /etc/issue If DOD Notice is not present in the "/etc/issue" file, this is a finding. Open the HYCU Web UI login page and verify the mandatory notice is present on the Welcome page. If the mandatory notice is not present at HYCU Web UI Welcome page, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-268231`

### Rule: The HYCU virtual appliance must automatically audit account creation.

**Rule ID:** `SV-268231r1038648_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system must generate audit records for all account creations events. Check the auditing rules in "/etc/audit/audit.rules" with the following command: # grep -E "/etc/passwd|/etc/gshadow|/etc/shadow|/etc/security/opasswd|/etc/group|/etc/sudoers|/etc/sudoers.d/" /etc/audit/audit.rules -w /etc/passwd -p wa -k identity -w /etc/gshadow -p wa -k identity -w /etc/shadow -p wa -k identity -w /etc/security/opasswd -p wa -k identity -w /etc/group -p wa -k identity -w /etc/sudoers -p wa -k identity -w /etc/sudoers.d/ -p wa -k identity If the command does not return all the lines above, or one or more of the lines are commented out, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-268232`

### Rule: The HYCU virtual appliance must automatically audit account modification.

**Rule ID:** `SV-268232r1038650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification along with an automatic notification to appropriate individuals will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system must generate audit records for all account modification events. Check the auditing rules in "/etc/audit/audit.rules" with the following command: # grep -E "/etc/passwd|/etc/gshadow|/etc/shadow|/etc/security/opasswd|/etc/group|/etc/sudoers|/etc/sudoers.d/" /etc/audit/audit.rules -w /etc/passwd -p wa -k identity -w /etc/gshadow -p wa -k identity -w /etc/shadow -p wa -k identity -w /etc/security/opasswd -p wa -k identity -w /etc/group -p wa -k identity -w /etc/sudoers -p wa -k identity -w /etc/sudoers.d/ -p wa -k identity If the command does not return all the lines above, or one or more of the lines are commented out, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-268233`

### Rule: The HYCU virtual appliance must automatically audit account disabling actions.

**Rule ID:** `SV-268233r1038652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account disabling actions will support account management procedures. When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system must generate audit records for all account disabling events. Check the auditing rules in "/etc/audit/audit.rules" with the following command: # grep -E "/etc/passwd|/etc/gshadow|/etc/shadow|/etc/security/opasswd|/etc/group|/etc/sudoers|/etc/sudoers.d/" /etc/audit/audit.rules -w /etc/passwd -p wa -k identity -w /etc/gshadow -p wa -k identity -w /etc/shadow -p wa -k identity -w /etc/security/opasswd -p wa -k identity -w /etc/group -p wa -k identity -w /etc/sudoers -p wa -k identity -w /etc/sudoers.d/ -p wa -k identity If the command does not return all the lines above, or one or more of the lines are commented out, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-268234`

### Rule: The HYCU virtual appliance must automatically audit account removal actions.

**Rule ID:** `SV-268234r1038654_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system generates audit records for all account removal events. Check the auditing rules in "/etc/audit/audit.rules" with the following command: # grep -E "/etc/passwd|/etc/gshadow|/etc/shadow|/etc/security/opasswd|/etc/group|/etc/sudoers|/etc/sudoers.d/" /etc/audit/audit.rules -w /etc/passwd -p wa -k identity -w /etc/gshadow -p wa -k identity -w /etc/shadow -p wa -k identity -w /etc/security/opasswd -p wa -k identity -w /etc/group -p wa -k identity -w /etc/sudoers -p wa -k identity -w /etc/sudoers.d/ -p wa -k identity If the command does not return all the lines above, or one or more of the lines are commented out, this is a finding.

## Group: SRG-APP-000175-NDM-000262

**Group ID:** `V-268235`

### Rule: The HYCU virtual appliance must be configured to use DOD-approved online certificate status protocol (OCSP) responders or certificate revocation lists (CRLs) to validate certificates used for PKI-based authentication.

**Rule ID:** `SV-268235r1038742_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Once issued by a DOD certificate authority (CA), public key infrastructure (PKI) certificates are typically valid for three years or shorter within the DOD. However, there are many reasons a certificate may become invalid before the prescribed expiration date. For example, an employee may leave or be terminated and still possess the smartcard on which the PKI certificates were stored. Another example is that a smartcard containing PKI certificates may become lost or stolen. A more serious issue could be that the CA or server which issued the PKI certificates has become compromised, thereby jeopardizing every certificate keypair that was issued by the CA. These examples of revocation use cases and many more can be researched further using internet cybersecurity resources. PKI user certificates presented as part of the identification and authentication criteria (e.g., DOD PKI as multifactor authentication [MFA]) must be checked for validity by network devices. For example, valid PKI certificates are digitally signed by a trusted DOD CA. Additionally, valid PKI certificates are not expired, and valid certificates have not been revoked by a DOD CA. Network devices can verify the validity of PKI certificates by checking with an authoritative CA. One method of checking the status of PKI certificates is to query databases referred to as certificate revocation lists (CRL). These are lists which are published, updated, and maintained by authoritative DOD CAs. For example, once certificates are expired or revoked, issuing CAs place the certificates on a CRL. Organizations can download these lists periodically (i.e., daily or weekly) and store them locally on the devices themselves or even onto another nearby local enclave resource. Storing them locally ensures revocation status can be checked even if internet connectivity is severed at the enclave's point of presence (PoP). However, CRLs can be rather large in storage size and further, the use of CRLs can be rather taxing on some computing resources. Another method of validating certificate status is to use the OCSP. Using OCSP, a requestor (i.e., the network device which the user is trying to authenticate to) sends a request to an authoritative CA challenging the validity of a certificate that has been presented for identification and authentication. The CA receives the request and sends a digitally signed response indicating the status of the user's certificate as valid, revoked, or unknown. Network devices should only allow access for responses that indicate the certificates presented by the user were considered valid by an approved DOD CA. OCSP is the preferred method because it is fast, provides the most current status, and is lightweight. Satisfies: SRG-APP-000175-NDM-000262, SRG-APP-000177-NDM-000263, SRG-APP-000080-NDM-000220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU console and execute the following command: sudo cat /opt/grizzly/config.properties | grep cert.path.revocation.checking.enabled=true If the variable is not set to true, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-268236`

### Rule: The HYCU virtual appliance must be configured to use at least two authentication servers for authenticating users prior to granting administration access.

**Rule ID:** `SV-268236r1038659_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU Web UI, select the gear menu, and then choose the Identity Providers option. Verify that two authentication servers are configured. If no authentication server is configured or only a single server is configured, this is a finding.

## Group: SRG-APP-000149-NDM-000247

**Group ID:** `V-268237`

### Rule: The HYCU virtual appliance must be configured to use DOD PKI as multifactor authentication (MFA) for interactive logins.

**Rule ID:** `SV-268237r1038754_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MFA is when two or more factors are used to confirm the identity of an individual who is requesting access to digital information resources. Valid factors include something the individual knows (e.g., username and password), something the individual has (e.g., a smartcard or token), or something the individual is (e.g., a fingerprint or biometric). Legacy information system environments only use a single factor for authentication, typically a username and password combination. Although two pieces of data are used in a username and password combination, this is still considered single factor because an attacker can obtain access simply by learning what the user knows. Common attacks against single-factor authentication are attacks on user passwords. These attacks include brute force password guessing, password spraying, and password credential stuffing. MFA, along with strong user account hygiene, helps mitigate against the threat of having account passwords discovered by an attacker. Even in the event of a password compromise, with MFA implemented and required for interactive login, the attacker still needs to acquire something the user has or replicate a piece of user's biometric digital presence. Private industry recognizes and uses a wide variety of MFA solutions. However, DOD public key infrastructure (PKI) is the only prescribed method approved for DOD organizations to implement MFA. For authentication purposes, centralized DOD certificate authorities (CA) issue PKI certificate key pairs (public and private) to individuals using the prescribed x.509 format. The private certificates that have been generated by the issuing CA are downloaded and saved to smartcards which, within DOD, are referred to as common access cards (CAC) or personal identity verification (PIV) cards. This happens at designated DOD badge facilities. The CA maintains a record of the corresponding public keys for use with PKI-enabled environments. Privileged user smartcards, or "alternate tokens", function in the same manner, so this requirement applies to all interactive user sessions (authorized and privileged users). Note: This requirement is used in conjunction with the use of a centralized authentication server (e.g., AAA, RADIUS, LDAP), which is a separate but equally important requirement. The MFA configuration of this requirement provides identification and the first phase of authentication (the challenge and validated response, thereby confirming the PKI certificate that was presented by the user). The centralized authentication server will provide the second phase of authentication (the digital presence of the PKI ID as a valid user in the requested security domain) and authorization. The centralized authentication server will map validated PKI identities to valid user accounts and determine access levels for authenticated users based on security group membership and role. In cases where the centralized authentication server is not used by the network device for user authorization, the network device must map the authenticated identity to the user account for PKI-based authentication. Satisfies: SRG-APP-000149-NDM-000247, SRG-APP-000820-NDM-000170, SRG-APP-000825-NDM-000180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU Web UI, select the gear menu, and then choose the Identity Providers option. Verify that at least one Identity Provider authentication server is configured. If no Identity Provider is configured, this is a finding. When using certificate authentication using client certificate or smart card (CAC authentication), verify "Enable Certificate Authentication" is enabled. If "Enable Certification Authentication" is not enabled, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-268238`

### Rule: The HYCU virtual appliance must generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-268238r1038665_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
HYCU Web UI user access accounts cannot be edited, only removed and readded from/to user groups in the Web UI Self-Service menu. After adding a user to a group, log in to the HYCU Web UI, navigate into Events context, and search for message of category "USER_GROUP" and text "Successfully added user to group". If the message is not in Events, this is a finding. Log in to the VM console and run the following command: chkconfig auditd If the Audit Service is not in a running state, this is a finding. Check the contents of the "/var/log/audit/audit.log" file. Verify the operating system generates audit records when successful/unsuccessful attempts to access privileges occur. If the audit log is not configured or does not have required contents, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-268239`

### Rule: The HYCU virtual appliance must generate audit records when successful/unsuccessful attempts to modify administrator privileges occur.

**Rule ID:** `SV-268239r1038771_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of the "/var/log/audit/audit.log" file. HYCU also maintains Event (Audit) information in the "HYCU Web UI Events" menu. Verify the audit log contains records showing successful/unsuccessful attempts to modify or delete administrator privileges. If the audit log is not configured or does not have required contents, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-268240`

### Rule: The HYCU virtual appliance must generate audit records when successful/unsuccessful attempts to delete administrator privileges occur.

**Rule ID:** `SV-268240r1038772_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of the "/var/log/audit/audit.log" file. HYCU also maintains Event (Audit) information in the "HYCU Web UI Events" menu. Verify the audit log contains records showing successful/unsuccessful attempts to modify or delete administrator privileges. If the audit log is not configured or does not have required contents, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-268241`

### Rule: The HYCU virtual appliance must generate audit records when successful/unsuccessful login attempts occur.

**Rule ID:** `SV-268241r1038672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of the "/var/log/audit/audit.log" file. Verify the audit log contains records showing when successful/unsuccessful login attempts occur. If the audit log is not configured or does not have required contents, this is a finding. HYCU also maintains Event (Audit) information in the "HYCU Web UI Events" menu. Log in with correct and incorrect credentials and check the HYCU Events. If the HYCU events of category "SECURITY" are not logged for each of the attempts, status is not "Success" for the correct credentials and status is not "Warning" for the incorrect credentials, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-268242`

### Rule: The HYCU virtual appliance must generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-268242r1038675_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the VM console and run the following command: chkconfig auditd If the Audit Service is not in a running state, this is a finding. Also, if no logs are present in the "/var/log/secure" file, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-268244`

### Rule: The HYCU virtual appliance must generate log records for a locally developed list of auditable events.

**Rule ID:** `SV-268244r1038775_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console. Review the /etc/audit/auditd.conf file and verify the settings are in accordance with a locally developed list of auditable events. If it is not configured in accordance with organizational policies, this is a finding. Check for the value of the "max_log_file_action" option in "/etc/audit/auditd.conf" with the following command: sudo grep max_log_file_action /etc/audit/auditd.conf If the "max_log_file_action" value is not set to "ROTATION", this is a finding.

## Group: SRG-APP-000096-NDM-000226

**Group ID:** `V-268245`

### Rule: The HYCU virtual appliance must produce audit records containing information to establish when events occurred, where events occurred, the source of the event, the outcome of the event, and identity of any individual or process associated with the event.

**Rule ID:** `SV-268245r1038756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done to compile an accurate risk assessment. Logging the date and time of each detected event provides a means of investigating an attack; recognizing resource usage or capacity thresholds; or identifying an improperly configured network device. To establish and correlate the series of events leading up to an outage or attack, it is imperative the date and time are recorded in all log records. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as device hardware components, device software modules, session identifiers, filenames, host names, and functionality. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event. The source may be a component, module, or process within the device or an external session, administrator, or device. Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the device after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Satisfies: SRG-APP-000096-NDM-000226, SRG-APP-000097-NDM-000227, SRG-APP-000098-NDM-000228, SRG-APP-000099-NDM-000229, SRG-APP-000100-NDM-000230</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of the "/var/log/audit/audit.log" file. HYCU also maintains Event (Audit) information in the "HYCU Web UI Events" menu. Verify the audit log contains records for: - When (date and time) events occurred. - Where events occurred. - The source of the event(s). - The outcome of the event(s). - The identity of any individual or process associated with the event(s). If the audit log is not configured or does not have required contents, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-268246`

### Rule: The HYCU virtual appliance must generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-268246r1038438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if HYCU is configured to audit the execution of the "execve" system call, by running the following command: $ sudo grep execve /etc/audit/audit.rules -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-APP-000095-NDM-000225

**Group ID:** `V-268247`

### Rule: The HYCU virtual appliance must produce audit log records containing sufficient information to establish what type of event occurred.

**Rule ID:** `SV-268247r1038776_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done to compile an accurate risk assessment. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource usage or capacity thresholds; or identifying an improperly configured network device. Without this capability, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the VM console and run the following command: chkconfig auditd If the Audit Service is not in a running state, this is a finding. Check the contents of the "/var/log/audit/audit.log" file. If the audit log does not have the required contents, this is a finding.

## Group: SRG-APP-000092-NDM-000224

**Group ID:** `V-268248`

### Rule: The HYCU virtual appliance must initiate session auditing upon startup.

**Rule ID:** `SV-268248r1038777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done to compile an accurate risk assessment. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource usage or capacity thresholds; or identifying an improperly configured network device. Without this capability, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. If auditing is enabled late in the startup process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the VM console and run the following command: chkconfig auditd If the Audit Service is not in a running state, this is a finding. Check the contents of the "/var/log/audit/audit.log" file. If the audit log does not have the required contents, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-268249`

### Rule: The HYCU virtual appliance must automatically audit account enabling actions.

**Rule ID:** `SV-268249r1038778_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done to compile an accurate risk assessment. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource usage or capacity thresholds; or identifying an improperly configured network device. Without this capability, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. If auditing is enabled late in the startup process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the VM console and run the following command: chkconfig auditd If the Audit Service is not in a running state, this is a finding. Check the contents of the "/var/log/audit/audit.log" file. If the audit log does not have the required contents, this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-268250`

### Rule: The HYCU virtual appliance must generate audit records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-268250r1038779_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done to compile an accurate risk assessment. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource usage or capacity thresholds; or identifying an improperly configured network device. Without this capability, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. If auditing is enabled late in the startup process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the VM console and run the following command: chkconfig auditd If the Audit Service is not enabled, this is a finding. Check the contents of the "/var/log/audit/audit.log" file. If the audit log does not have the required contents, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-268251`

### Rule: The HYCU virtual appliance must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-268251r1038695_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure network devices have a sufficient storage capacity in which to write the audit logs, they must be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it can be modified.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console. Review the /etc/audit/auditd.conf file and verify that the settings are in accordance with organizational policies. If it is not configured in accordance with organizational policies, this is a finding. Check for the value of the "max_log_file_action" option in "/etc/audit/auditd.conf" with the following command: sudo grep max_log_file_action /etc/audit/auditd.conf If the "max_log_file_action" value is not set to "ROTATION", this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-268252`

### Rule: The HYCU virtual appliance must support organizational requirements to conduct backups of information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-268252r1038698_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up, and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial-of-service condition is possible for all who use this critical network component. Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that HYCU is backing itself up by logging in to the HYCU Web UI and checking the HYCU Controller widget at the HYCU Dashboard. If the message "Controller VM is not protected" is found and highlighted in orange, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-268253`

### Rule: The HYCU virtual appliance must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-268253r1038701_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial-of-service condition is possible for all who use this critical network component. Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-APP-000515-NDM-000325, SRG-APP-000516-NDM-000340</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that HYCU is backing itself up by logging in to the HYCU Web UI and checking the HYCU Controller widget at the HYCU Dashboard. If the message "Controller VM is not protected" is found and highlighted in orange, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-268254`

### Rule: The HYCU virtual appliance must generate an immediate real-time alert of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-268254r1038704_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Satisfies: SRG-APP-000360-NDM-000295, SRG-APP-000795-NDM-000130</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU Web UI and review the "Events" menu and "Email Notifications" to verify that all appropriate/relevant audit failure events are included in the "Category" drop-down menu. If these events are not shown (reference a recent event capturing a login to HYCU for validation), this is a finding.

## Group: SRG-APP-000120-NDM-000237

**Group ID:** `V-268255`

### Rule: The HYCU virtual appliance must protect audit information from unauthorized deletion.

**Rule ID:** `SV-268255r1039643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions using file system protections, restricting access, and backing up log data to ensure log data is retained. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys to make access decisions regarding the deletion of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system audit records have proper permissions and ownership. Log in to the HYCU console and list the full permissions and ownership of the audit log files with the following command: # sudo ls -la /var/log/audit total 4512 drwx------. 2 root root 23 Apr 25 16:53 . drwxr-xr-x. 17 root root 4096 Aug 9 13:09 .. -rw-------. 1 root root 8675309 Aug 9 12:54 audit.log Audit logs must be mode 0600 or less permissive. If any are more permissive, this is a finding. The owner and group owner of all audit log files must both be "root". If any other owner or group owner is listed, this is a finding.

## Group: SRG-APP-000121-NDM-000238

**Group ID:** `V-268256`

### Rule: The HYCU virtual appliance must protect audit tools from unauthorized access, modification, and deletion.

**Rule ID:** `SV-268256r1038708_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-APP-000121-NDM-000238, SRG-APP-000122-NDM-000239, SRG-APP-000123-NDM-000240</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system audit tools and config files have proper permissions and ownership. Log in to the HYCU console and list the full permissions and ownership of the audit folder with the following command: sudo ls -al /etc/audit Folder and files must be owned by root and the following permissions must be set: drwxr-x---. 4 root root 126 Mar 15 10:16 . drwxr-xr-x. 106 root root 8192 May 6 13:58 .. -rw-r-----. 1 root root 751 Apr 24 2020 audisp-remote.conf -rw-r-----. 1 root root 856 Apr 24 2020 auditd.conf -rw-r-----. 1 root root 107 Feb 3 13:18 audit.rules -rw-r-----. 1 root root 127 Apr 24 2020 audit-stop.rules drwxr-x---. 2 root root 67 Mar 15 10:16 plugins.d drwxr-x---. 2 root root 25 Feb 3 13:13 rules.d Audit files must be mode 0640 or less permissive. If any are more permissive, this is a finding. The owner and group owner of all audit files must both be "root". If any other owner or group owner is listed, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-268257`

### Rule: The HYCU virtual appliance must be running a release that is currently supported by the vendor.

**Rule ID:** `SV-268257r1038710_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the HYCU device is running a supported version. Log in to the HYCU Web UI. On the menu on the left side of the page, scroll to the bottom, where it shows the running version of HYCU. If HYCU version is not on the list of supported versions, as specified in the End-of-Life Milestones and Dates, this is a finding. Note: The HYCU support portal specifies the HYCU end of life policies. To determine if the system is using a supported version, visit: https://download.hycu.com/docs/HYCU-EOL-dates.pdf.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-268258`

### Rule: The HYCU virtual appliance must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-268258r1039645_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice. Satisfies: SRG-APP-000516-NDM-000344, SRG-APP-000910-NDM-000300</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open a new HYCU Web UI browser tab and verify there is no warning prompt before proceeding to the Web UI login page. If a warning appears in the web browser stating, "Not secure", this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-268259`

### Rule: The HYCU virtual appliance must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services.

**Rule ID:** `SV-268259r1038477_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSHD daemon has been disabled using the following command: $ sudo systemctl status sshd Loaded: loaded (/usr/lib/systemd/system/sshd.service; disabled) Active: inactive (dead) If the SSHD daemon is not disabled and inactive or is not documented and approved for use, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-268260`

### Rule: The HYCU virtual appliance must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-268260r1038716_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The use of SSH-2 protocol for network/remote access prevents replay attacks. The SSH-2 protocol is the standard for the SSH daemon in the Linux OS used by HYCU. To determine the SSH version in use, log in to the HYCU console and execute the following command: ssh -v localhost If the output does not show remote protocol version 2.0 in use, this is a finding. HYCU web access uses TLS, which addresses this threat. HYCU web access cannot be configured to not use TLS.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-268262`

### Rule: The HYCU virtual appliance must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-268262r1038718_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console. Check for the value of the "minclass" option in "/etc/security/pwquality.conf" with the following command: grep minclass /etc/security/pwquality.conf If the minclass value is not set to "5", this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-268263`

### Rule: The HYCU virtual appliance must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-268263r1038720_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console. Check for the value of the "minclass" option in "/etc/security/pwquality.conf" with the following command: grep minclass /etc/security/pwquality.conf If the minclass value is not set to "5", this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-268264`

### Rule: The HYCU virtual appliance must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-268264r1038722_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console. Check for the value of the "minclass" option in "/etc/security/pwquality.conf" with the following command: grep minclass /etc/security/pwquality.conf If the minclass value is not set to "5", this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-268265`

### Rule: The HYCU virtual appliance must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-268265r1038724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console. Check for the value of the "minclass" option in "/etc/security/pwquality.conf" with the following command: grep minclass /etc/security/pwquality.conf If the minclass value is not set to "5", this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-268266`

### Rule: The HYCU virtual appliance must enforce a minimum 15-character password length.

**Rule ID:** `SV-268266r1038758_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the value of the "minlen" option in "/etc/security/pwquality.conf" with the following command: grep minlen /etc/security/pwquality.conf If the minlen value is not set to "15", this is a finding. Check for the value of the "user.password.min.length" variable in "/opt/grizzly/config.properties" HYCU configuration file with the following command: grep user.password.min.length /opt/grizzly/config.properties If the value is not set to 15 or more, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-268267`

### Rule: The HYCU virtual appliance must require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-268267r1038760_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value of the "difok" option with the following command: $ sudo grep -r difok /etc/security/pwquality.conf* /etc/security/pwquality.conf:difok = 8 If the value of "difok" is set to less than "8" or is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-268269`

### Rule: The HYCU virtual appliance must use FIPS 140-2-approved algorithms for authentication to a cryptographic module.

**Rule ID:** `SV-268269r1038744_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not validated and therefore cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When FIPS mode is enabled, the HYCU application will use FIPS-compliant behavior. Validate the FIPS status using the following command: 'cat /proc/sys/crypto/fips_enabled' If command output does not show "1", this is a finding. 'fips-mode-setup --check' If command output does not show "FIPS mode is enabled", this is a finding. 'update-crypto-policies --show' If command output does not show "FIPS", this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-268270`

### Rule: The HYCU virtual appliance must use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-268270r1038745_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DOD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2-validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, NTP, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When FIPS mode is enabled, the HYCU application will use FIPS-compliant behavior. Validate the FIPS status using the following command: 'cat /proc/sys/crypto/fips_enabled' If command output does not show "1", this is a finding. 'fips-mode-setup --check' If command output does not show "FIPS mode is enabled", this is a finding. 'update-crypto-policies --show' If command output does not show "FIPS", this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-268271`

### Rule: The HYCU virtual appliance must be configured to implement cryptographic mechanisms using a FIPS 140-2-approved algorithm to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-268271r1038746_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When FIPS mode is enabled, the HYCU application will use FIPS-compliant behavior. Validation of FIPS status can be done using the following commands: 'cat /proc/sys/crypto/fips_enabled' If command output does not show "1", this is a finding. 'fips-mode-setup --check' If command output does not show "FIPS mode is enabled", this is a finding. 'update-crypto-policies --show' If command output does not show "FIPS", this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-268274`

### Rule: The HYCU virtual appliance must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-268274r1038763_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to HYCU UI and ensure that admin user is the only user configured with HYCU Authentication type. If any other user except for built-in admin is configured with HYCU Authentication type, this is a finding. Log in to HYCU console, run the command "cat /etc/passwd" within the HYCU console and ensure no nondefault user account configured. If any other user apart from HYCU user is configured to access HYCU console, this is a finding.

## Group: SRG-APP-000381-NDM-000305

**Group ID:** `V-268282`

### Rule: The HYCU virtual appliance must audit the enforcement actions used to restrict access associated with changes to the device.

**Rule ID:** `SV-268282r1038736_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the device configuration, it will be difficult to identify attempted attacks, and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the contents of the "/var/log/audit/audit.log" file. Verify the audit log contains records showing when unsuccessful login attempts occur. If the audit log is not configured or does not have required contents, this is a finding. HYCU also maintains Event (Audit) information in the "HYCU Web UI Events" menu. Log in with incorrect credentials and check the HYCU Events. If the HYCU event of category "SECURITY" and status "Warning" is not logged, this is a finding.

## Group: SRG-APP-000131-NDM-000243

**Group ID:** `V-268283`

### Rule: The HYCU virtual appliance must prevent the installation of patches, service packs, or application components without verification the software component has been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-268283r1038766_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the network device. Verifying software components have been digitally signed using a certificate that is recognized and approved by the organization ensures the software has not been tampered with and has been provided by a trusted vendor. Accordingly, patches, service packs, or application components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The device should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system prevents the installation of patches, service packs, device drivers, or operating system components from a repository without verification that they have been digitally signed using a certificate that is recognized and approved by the organization. Check that YUM verifies the signature of packages from a repository prior to install with the following command: $ sudo grep -E '^\[.*\]|gpgcheck' /etc/yum.repos.d/*.repo /etc/yum.repos.d/appstream.repo:[appstream] /etc/yum.repos.d/appstream.repo:gpgcheck=1 /etc/yum.repos.d/baseos.repo:[baseos] /etc/yum.repos.d/baseos.repo:gpgcheck=1 If "gpgcheck" is not set to "1", or if options are missing or commented out, this is a finding. Execute the following command to check the kernel and cryptographic libraries, as well as the SHA256 checksums of the application files: $ sudo /opt/grizzly/bin/hycu-selftest.sh If the output is not OK for the OS, this is a finding. If the output reports an error for any other file than /etc/issue for the App section, this is a finding.

## Group: SRG-APP-000457-NDM-000352

**Group ID:** `V-268296`

### Rule: The HYCU virtual appliance must install security-relevant software updates within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-268296r1038767_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates. Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install software patches across the enclave (e.g., mobile device management solutions). Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain evidence that software updates are consistently applied to the HYCU virtual appliance within the time frame defined for each patch. If such evidence cannot be obtained, or the evidence obtained indicates a pattern of noncompliance, this is a finding. If the HYCU virtual appliance does not install security-relevant updates within the time period directed by the authoritative source, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-268301`

### Rule: The HYCU virtual appliance must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after five minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-268301r1038739_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU VM console. For console connections, check for the value of the "TMOUT" option in "/home/hycu/.bashrc" with the following command: grep TMOUT /home/hycu/.bashrc If the "TMOUT" value is not set to "300" or less, this is a finding. For SSH connections, check for the value of the "ClientAliveInterval" option in "/etc/ssh/sshd_config" with the following command: grep ClientAliveInterval /etc/ssh/sshd_config If the "ClientAliveInterval" value is not set to "5" or less, this is a finding. For UI connections, run the following command to check configured HYCU session timeout: cat /opt/grizzly/config.properties | grep api.session.expiration.minutes If not configured at "5" or less, this is a finding.

## Group: SRG-APP-000224-NDM-000270

**Group ID:** `V-268302`

### Rule: The HYCU virtual appliance must generate unique session identifiers using a FIPS 140-2 approved random number generator.

**Rule ID:** `SV-268302r1038606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sequentially generated session IDs can be easily guessed by an attacker. Employing the concept of randomness in the generation of unique session identifiers helps to protect against brute-force attacks to determine future session identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. This requirement is applicable to devices that use a web interface for device management.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When FIPS mode is enabled, HYCU will use FIPS-compliant behavior. Validation of FIPS status can be done using the following command: 'cat /proc/sys/crypto/fips_enabled' If command output does not show "1", this is a finding. 'fips-mode-setup --check' If command output does not show "FIPS mode is enabled", this is a finding. 'update-crypto-policies --show' If command output does not show "FIPS", this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-268303`

### Rule: The HYCU virtual appliance must be configured to send log data to at least two central log servers for the purpose of forwarding alerts to the administrators and the information system security officer (ISSO).

**Rule ID:** `SV-268303r1038770_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, is important in showing whether someone is an internal employee or an outside threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the HYCU Web UI, navigate to Events >> Notifications >> Webhooks and verify that HYCU is sending required logs to at least at least two central log servers. If two webhooks sending required HYCU events to at least two central log servers are not configured, this is a finding.

