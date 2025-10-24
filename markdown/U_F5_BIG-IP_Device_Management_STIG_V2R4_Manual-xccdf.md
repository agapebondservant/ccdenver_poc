# STIG Benchmark: F5 BIG-IP Device Management Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-217381`

### Rule: The BIG-IP appliance must limit the number of concurrent sessions to the Configuration Utility to 10 or an organization-defined number.

**Rule ID:** `SV-217381r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to limit the number of concurrent sessions to 10 or an organization-defined number. Navigate to the BIG-IP System manager >> System >> Preferences. Set "System Settings:" to "Advanced". Verify "Maximum HTTP Connections to Configuration Utility" is set to the organization-defined number of concurrent sessions. If neither of these configurations is present, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-217383`

### Rule: The BIG-IP appliance must automatically audit account creation.

**Rule ID:** `SV-217383r960777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server that automatically audits account creation. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that automatically audits account creation. If the BIG-IP appliance is not configured to use a remote authentication server that automatically audits account creation, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-217384`

### Rule: The BIG-IP appliance must automatically audit account modification.

**Rule ID:** `SV-217384r960780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification along with an automatic notification to appropriate individuals will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server that automatically audits account modifications. Verify the BIG-IP appliance is configured to utilize a properly configured authentication server. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured to use an approved remote authentication server that automatically audits account modification. If account modification is not automatically audited, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-217385`

### Rule: The BIG-IP appliance must automatically audit account-disabling actions.

**Rule ID:** `SV-217385r960783_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account disabling actions will support account management procedures. When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server that automatically audits account-disabling actions. Verify the BIG-IP appliance is configured to use a properly configured authentication server. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured to use an approved remote authentication server that automatically audits account-disabling actions. If account disabling is not automatically audited, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-217386`

### Rule: The BIG-IP appliance must automatically audit account removal actions.

**Rule ID:** `SV-217386r960786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server that automatically audits account removal actions. Verify the BIG-IP appliance is configured to use a properly configured authentication server. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured to use an approved remote authentication server that automatically audits account removal actions. If account removal is not automatically audited, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-217387`

### Rule: The BIG-IP appliance must be configured to enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level in accordance with applicable policy for the device.

**Rule ID:** `SV-217387r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Network devices use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the network device to control access between administrators (or processes acting on behalf of administrators) and objects (e.g., device commands, files, records, processes) in the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level in accordance with applicable policy for the device. Verify the BIG-IP appliance is configured to utilize a properly configured authentication server. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured to use an approved remote authentication server that enforces the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level. If the BIG-IP appliance is not configured to enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-217388`

### Rule: The BIG-IP appliance must be configured to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-217388r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period. If the BIG-IP appliance is not configure to use a remote authentication server to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-217389`

### Rule: The BIG-IP appliance must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-217389r960843_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to present a DoD-approved banner formatted in accordance with DTM-08-060. Navigate to the BIG-IP System manager >> System >> Preferences. Verify "Show The Security Banner On The Login Screen" is Enabled. Review the "Security Banner Text To Show On The Login Screen" under the "Security Settings" section for the following verbiage: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If such a banner is not presented, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-217390`

### Rule: The BIG-IP appliance must be configured to protect against an individual (or process acting on behalf of an individual) falsely denying having performed system configuration changes.

**Rule ID:** `SV-217390r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required in order to maintain the integrity of the configuration management process. All configuration changes to the network device are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. To meet this requirement, the network device must log administrator access and activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that protects against an individual (or process acting on behalf of an individual) falsely denying having performed system configuration changes. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that protects against an individual falsely denying having performed system configuration changes. If the BIG-IP appliance is not configured to protect against an individual (or process acting on behalf of an individual) falsely denying having performed system configuration changes, this is a finding.

## Group: SRG-APP-000119-NDM-000236

**Group ID:** `V-217392`

### Rule: The BIG-IP appliance must be configured to protect audit information from unauthorized modification.

**Rule ID:** `SV-217392r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit network device activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity would be impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance protects audit information from any type of unauthorized modification. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Verify authorized access is configured for each role under "Log Access". If the BIG-IP appliance is not configured to protect audit information from unauthorized modification, this is a finding.

## Group: SRG-APP-000120-NDM-000237

**Group ID:** `V-217393`

### Rule: The BIG-IP appliance must be configured to protect audit information from unauthorized deletion.

**Rule ID:** `SV-217393r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity would be impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files receive the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order to make access decisions regarding the deletion of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance protects audit information from any type of unauthorized deletion. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Verify authorized access is configured for each role under "Log Access". If the BIG-IP appliance is not configured to protect audit information from unauthorized deletion, this is a finding.

## Group: SRG-APP-000121-NDM-000238

**Group ID:** `V-217394`

### Rule: The BIG-IP appliance must be configured to protect audit tools from unauthorized access.

**Rule ID:** `SV-217394r960939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance protects audit tools from unauthorized access. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Verify authorized access is configured for each role under "Log Access". If the BIG-IP appliance is not configured to protect its audit tools from unauthorized access, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-217396`

### Rule: The BIG-IP appliance must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and vulnerability assessments.

**Rule ID:** `SV-217396r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance prohibits the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. Navigate to the BIG-IP System manager >> System >> Services. Verify no unauthorized services are configured or running. If any unnecessary or nonsecure functions are permitted, this is a finding.

## Group: SRG-APP-000153-NDM-000249

**Group ID:** `V-217397`

### Rule: The BIG-IP appliance must be configured to ensure administrators are authenticated with an individual authenticator prior to using a group authenticator.

**Rule ID:** `SV-217397r984091_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, administrators must be individually identified and authenticated. Individual accountability mandates that each administrator is uniquely identified. A group authenticator is a shared account or some other form of authentication that allows multiple unique individuals to access the network device using a single account. If a device allows or provides for group authenticators, it must first individually authenticate administrators prior to implementing group authenticator functionality. Some devices may not have the need to provide a group authenticator; this is considered a matter of device design. In those instances where the device design includes the use of a group authenticator, this requirement will apply. This requirement applies to accounts created and managed on or by the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to authenticate administrators with an individual authenticator prior to using a group authenticator. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that authenticates administrators to an administrators group. Navigate to System >> Users >> Remote Role Groups. Verify that administrators are assigned to the Administrator Role. If the BIG-IP appliance is not configured to authenticate administrators with an individual authenticator prior to using a group authenticator, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-217398`

### Rule: The BIG-IP appliance must be configured to enforce a minimum 15-character password length.

**Rule ID:** `SV-217398r984092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that enforces a minimum 15-character password length. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that enforces a minimum of 15-character password length. If the BIG-IP appliance is not configured to use a properly configured authentication server to enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-217399`

### Rule: If multifactor authentication is not supported and passwords must be used, the BIG-IP appliance must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-217399r984095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that enforce password complexity by requiring that at least one upper-case character be used. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that enforces password complexity by requiring that at least one upper-case character be used. If the BIG-IP appliance is not configured to use a properly configured authentication server that enforces password complexity by requiring that at least one upper-case character be used, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-217400`

### Rule: If multifactor authentication is not supported and passwords must be used, the BIG-IP appliance must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-217400r984098_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that enforces password complexity by requiring that at least one lower-case character be used. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that enforces password complexity by requiring that at least one lower-case character be used. If the BIG-IP appliance is not configured to use a properly configured authentication server that enforces password complexity by requiring that at least one lower-case character be used, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-217401`

### Rule: If multifactor authentication is not supported and passwords must be used, the BIG-IP appliance must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-217401r984099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that enforces password complexity by requiring that at least one numeric character be used. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that enforces password complexity by requiring that at least one numeric character be used. If the BIG-IP appliance is not configured to use a properly configured authentication server that enforces password complexity by requiring that at least one numeric character be used, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-217402`

### Rule: If multifactor authentication is not supported and passwords must be used, the BIG-IP appliance must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-217402r984100_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that enforces password complexity by requiring that at least one special character be used. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that enforces password complexity by requiring that at least one special character be used. If the BIG-IP appliance is not configured to use a properly configured authentication server that enforces password complexity by requiring that at least one special character be used, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-217403`

### Rule: If multifactor authentication is not supported and passwords must be used, the BIG-IP appliance must require that when a password is changed, the characters are changed in at least eight (8) of the positions within the password.

**Rule ID:** `SV-217403r1043189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that requires when a password is changed, the characters are changed in at least eight (8) of the positions within the password. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that requires when a password is changed, the characters are changed in at least eight (8) of the positions within the password. If the BIG-IP appliance is not configured to use a properly configured authentication server that requires when a password is changed, the characters are changed in at least eight (8) of the positions within the password, this is a finding.

## Group: SRG-APP-000171-NDM-000258

**Group ID:** `V-217404`

### Rule: The BIG-IP appliance must only store encrypted representations of passwords.

**Rule ID:** `SV-217404r984103_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices must enforce password encryption using an approved cryptographic hash function, when storing passwords.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that enforces password encryption for storage. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that only stores encrypted representations of passwords. If the BIG-IP appliance is not configured to use a properly configured authentication server that stores encrypted representations of passwords, this is a finding.

## Group: SRG-APP-000172-NDM-000259

**Group ID:** `V-217405`

### Rule: The BIG-IP appliance must only transmit encrypted representations of passwords.

**Rule ID:** `SV-217405r961029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices can accomplish this by making direct function calls to encryption modules or by leveraging operating system encryption capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that transmits only encrypted representations of passwords. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that only transmits encrypted representations of passwords. If the BIG-IP appliance is not configured to use a properly configured authentication server that only transmits encrypted representations of passwords, this is a finding.

## Group: SRG-APP-000178-NDM-000264

**Group ID:** `V-217406`

### Rule: The BIG-IP appliance must be configured to obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-217406r961047_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent the compromise of authentication information such as passwords during the authentication process, the feedback from the network device must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided information when typed into the system is a method used in addressing this risk. For example, displaying asterisks when a user types in a password is an example of obscuring feedback of authentication information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the BIG-IP appliance is configured to obscure feedback of authentication information during the authentication process. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Encryption" is configured to use SSL for the authentication process with a properly configured authentication server. If the BIG-IP appliance is not configured to obscure feedback of authentication information during the authentication process, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-217407`

### Rule: The BIG-IP appliance must be configured to use mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

**Rule ID:** `SV-217407r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that uses mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that uses mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module. If the BIG-IP appliance is not configured to use a properly configured authentication server that uses mechanisms that meet the requirements for authentication to a cryptographic module, this is a finding.

## Group: SRG-APP-000186-NDM-000266

**Group ID:** `V-217408`

### Rule: The BIG-IP appliance must be configured to terminate all management sessions after 10 minutes of inactivity.

**Rule ID:** `SV-217408r984105_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If a device management session or connection remains open after management is completed, it may be hijacked by an attacker and used to compromise or damage the network device. Nonlocal device management and diagnostic activities are activities conducted by individuals communicating through an external network (e.g., the internet) or an internal network. If the remote node has abnormally terminated or an upstream link from the managed device is down, BIG IP F5 terminates the management session and associated connection by default, and this is not configurable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to terminate all sessions and network connections when nonlocal device maintenance is completed. Navigate to the BIG-IP System manager >> System >> Preferences. Verify "Idle Time Before Automatic Logout" is set to 900 seconds (or less) and "Enforce Idle Timeout While View Dashboard" is enabled. If the BIG-IP appliance is not configured to terminate all idle sessions after 10 minutes or less, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-217410`

### Rule: The BIG-IP appliance must be configured to automatically audit account-enabling actions.

**Rule ID:** `SV-217410r961290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured remote authentication server that automatically audits account-enabling actions. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that automatically audits account-enabling actions. If the BIG-IP appliance is not configured to use a properly configured remote authentication server to automatically audit account-enabling actions, this is a finding.

## Group: SRG-APP-000329-NDM-000287

**Group ID:** `V-217411`

### Rule: The BIG-IP appliance must be configured to enforce organization-defined role-based access control policies over defined subjects and objects.

**Rule ID:** `SV-217411r987662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on organizational information systems associated with the organization-defined roles. When administrators are assigned to the organizational roles, they inherit the authorizations or privileges defined for those roles. RBAC simplifies privilege administration for organizations because privileges are not assigned directly to every administrator (which can be a significant number of individuals for mid- to large-size organizations) but are instead acquired through role assignments. RBAC can be implemented either as a mandatory or discretionary form of access control. The RBAC policies and the subjects and objects are defined uniquely for each network device, so they cannot be specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance enforces organization-defined role-based access control policy over defined subjects and objects. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server that assigns authenticated users to an appropriate group. Navigate to System >> Users >> Remote Role Groups. Verify Remote Role Groups are assigned proper Role Access and Partition Access. If the BIG-IP appliance is not configured to enforce organization-defined role-based access control policies over defined subjects and objects, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-217413`

### Rule: The BIG-IP appliance must be configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-217413r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to off-load audit records to a remote syslog server that allocates audit record storage capacity in accordance with organization-defined audit record storage requirements. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Remote Logging. Verify a syslog destination is configured that allocates audit record storage capacity in accordance with organization-defined audit record storage requirements. If audit record store capacity is not allocated in accordance with organization-defined audit record storage requirements, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-217414`

### Rule: The BIG-IP appliance must be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources.

**Rule ID:** `SV-217414r987682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region from the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the BIG-IP appliance is configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources. Navigate to the BIG-IP System manager >> Configuration >> Device >> NTP. Verify there is a primary time source and a secondary time source configured that are in different geographic regions. If the BIG-IP appliance is not configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000380-NDM-000304

**Group ID:** `V-217415`

### Rule: The BIG-IP appliance must be configured to enforce access restrictions associated with changes to device configuration.

**Rule ID:** `SV-217415r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to device configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the device can potentially have significant effects on the overall security of the device. Accordingly, only qualified and authorized individuals should be allowed to obtain access to device components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to enforce access restrictions associated with changes to device configuration. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server that assigns authenticated users to an appropriate group. Navigate to System >> Users >> Remote Role Groups. Verify Remote Role Groups are assigned proper Role Access and Partition Access to enforce access restrictions associated with changes to device configuration. If the BIG-IP appliance is not configured to enforce such access restrictions, this is a finding.

## Group: SRG-APP-000381-NDM-000305

**Group ID:** `V-217416`

### Rule: The BIG-IP appliance must be configured to audit the enforcement actions used to restrict access associated with changes to the device.

**Rule ID:** `SV-217416r984111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the device configuration, it will be difficult to identify attempted attacks, and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to audit the enforcement actions used to restrict access associated with changes to the device. Navigate to the BIG-IP System manager >> Logs >> Configuration >> Options. Review configuration in the "Audit Logging" section. Verify that "MCP" is set to Debug. If the BIG-IP appliance is not configured to audit the enforcement actions used to restrict access associated with changes to the device, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-217417`

### Rule: The BIG-IP appliance must be configured to protect against or limit the effects of all known types of Denial of Service (DoS) attacks on the BIG-IP appliance management network by limiting the number of concurrent sessions.

**Rule ID:** `SV-217417r961620_rule`
**Severity:** high

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to protect against or to limit the effects of DoS attacks by limiting the number of concurrent sessions. Review organizational Standard Operating Procedures (SOP) to ensure there is an organizational-defined threshold for the number of allowed connections to the management console. Navigate to the BIG-IP System manager >> System >> Preferences. Set "System Settings:" to "Advanced". Verify "Maximum HTTP Connections To Configuration Utility" is set to the number of allowed connections defined in the local SOP. If the BIG-IP appliance is not configured to protect against or limit the effects of DoS attacks by limiting the number of concurrent sessions, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-217418`

### Rule: The BIG-IP appliance must be configured to off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-217418r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to off-load audit records onto a different system or media than the system being audited. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Remote Logging. Verify a syslog destination is configured that off-loads audit records from the BIG-IP appliance that is different from the system being audited. If BIG-IP appliance is not configured to off-load audit records onto a different system or media, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-217419`

### Rule: The BIG-IP appliance must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-217419r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network device to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network device. Security-related parameters are those parameters impacting the security state of the network device, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured in accordance with the security configuration settings based on applicable DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs. If the BIG-IP appliance is not configured in accordance with the designated security configuration settings, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-217420`

### Rule: The BIG-IP appliance must be configured to employ automated mechanisms to centrally manage authentication settings.

**Rule ID:** `SV-217420r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server to centrally manage authentication settings. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that employs automated mechanisms to centrally manage authentication settings. If authentication settings are not managed centrally using automated mechanisms, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-217421`

### Rule: The BIG-IP appliance must create backups of system-level information contained in the information system when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-217421r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is capable of creating backups of system-level information contained in the information system when changes occur. Navigate to the BIG-IP System manager >> System >> Archives. Review the list of archives to verify backups are conducted in accordance with the local backup policy. If the BIG-IP appliance does not support the creating backups of system-level information contained in the information system when changes occur or weekly, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-217422`

### Rule: The BIG-IP appliance must be configured to create backups of information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-217422r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to off-load logs to a remote log server when changes occur. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Remote Logging. Verify a log destination is configured to allow for backups of information system documentation when changes occur. If the BIG-IP appliance does not backup the information system documentation, including security-related documentation, when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-217423`

### Rule: The BIG-IP appliance must be configured to obtain its public key certificates from an appropriate certificate policy through a DoD-approved service provider.

**Rule ID:** `SV-217423r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to obtain public key certificates from an appropriate certificate policy through a DoD-approved service provider. Navigate to the BIG-IP System manager >> System >> Device Certificates >> Device Certificate. Verify the device certificate has been obtained from an approved service provider. If the BIG-IP appliance does not obtain its public key certificates from an appropriate certificate policy through a DoD-approved service provider, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-217424`

### Rule: The F5 BIG-IP must ensure SSH is disabled for root user logon to prevent remote access using the root account.

**Rule ID:** `SV-217424r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The F5 BIG-IP shell must be locked down to limit the ability to modify the configuration through the shell. Preventing attackers from remotely accessing management functions using root account mitigates the risk that unauthorized individuals or processes may gain superuser access to information or privileges. Additionally, the audit records for actions taken using the group account will not identify the specific person who took the actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the F5 BIG-IP shell is locked down to limit the ability to modify the configuration through the shell. Log in to the Configuration utility as the administrative user. Navigate to System > Platform. Under Root Account, verify the Disable login and Disable bash check boxes are checked. If the value of systemauth.disablerootlogin and db systemauth.disablebash is not set to “true”, then this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228978`

### Rule: The BIG-IP appliance must provide automated support for account management functions.

**Rule ID:** `SV-228978r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management functions include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The network device must be configured to automatically provide account management functions, and these functions must immediately enforce the organization's current account policy. All accounts used for access to the network device are privileged or system-level accounts. Therefore, if account management functions are not automatically enforced, an attacker could gain privileged access to a vital element of the network security architecture. This control does not include emergency administration accounts that provide access to the network device components in case of network failure. There must be only one such locally defined account. All other accounts must be defined. All other accounts must be created and managed on the site's authentication server (e.g., RADIUS, LDAP, or Active Directory). This requirement is applicable to account management functions provided by the network device application. If the function is provided by the underlying OS or an authentication server, it must be secured using the applicable security guide or STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server that provides automated account management. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that provides automated support for account management functions. If the BIG-IP appliance is not configured to use a remote authentication server to provide automated account management, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228979`

### Rule: The BIG-IP appliance must automatically remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-228979r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts remain active when no longer needed, they may be used to gain unauthorized access. The risk is greater for the network device since these accounts have elevated privileges. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server to automatically disable or remove temporary accounts after 72 hours. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that automatically removes or disables temporary user accounts after 72 hours. If the use of temporary accounts is prohibited, this is not a finding. If the BIG-IP appliance is not configured to use a remote authentication server that automatically disables or removes temporary accounts after 72 hours, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228980`

### Rule: The BIG-IP appliance must automatically disable accounts after a 35-day period of account inactivity.

**Rule ID:** `SV-228980r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Inactive accounts could be reactivated or compromised by unauthorized users, allowing exploitation of vulnerabilities and undetected access to the network device. This control does not include emergency administration accounts, which are meant for access to the network device components in case of network failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server that automatically disables accounts after 35 days of inactivity. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that automatically disables accounts after a 35-day period of account inactivity. If the BIG-IP appliance is not configured to use a remote authentication server that automatically disables accounts after a 35-day period of account inactivity, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228981`

### Rule: Upon successful logon, the BIG-IP appliance must be configured to notify the administrator of the date and time of the last logon.

**Rule ID:** `SV-228981r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their network device management account. Providing administrators with information regarding the date and time of their last successful logon allows them to determine if any unauthorized activity has occurred. This incorporates all methods of logon, including, but not limited to, SSH, HTTP, HTTPS, and physical connectivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server to notify the administrator of the date and time of their last logon. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server to notify the administrator of the date and time of the last logon. If the administrator is not notified of the date and time of the last logon upon successful logon, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228982`

### Rule: Upon successful logon, the BIG-IP appliance must be configured to notify the administrator of the number of unsuccessful logon attempts since the last successful logon.

**Rule ID:** `SV-228982r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their network device management account. Providing administrators with information regarding the number of unsuccessful attempts made to logon to their account allows them to determine if any unauthorized activity has occurred. Without this information, the administrator may not be aware that unauthorized activity has occurred. This incorporates all methods of logon, including, but not limited to, SSH, HTTP, HTTPS, and physical connectivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server to notify the administrator of the number of unsuccessful logon attempts since the last successful logon. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server to notify the administrator of the number of unsuccessful logon attempts since the last successful logon. If the administrator is not notified of the number of unsuccessful logon attempts since the last successful logon, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228983`

### Rule: The BIG-IP appliance must be configured to alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-228983r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to alert the ISSO and SA (at a minimum) in the event of an audit processing failure. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Verify "MCP" under the "Audit Logging" section is set to Debug. If the BIG-IP appliance is not configured to alert in the event of an audit processing failure, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228985`

### Rule: The BIG-IP appliance must be configured to protect audit information from any type of unauthorized read access.

**Rule ID:** `SV-228985r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could use to his or her advantage. To ensure the veracity of audit data, the information system and/or the network device must protect audit information from any and all unauthorized read access. This requirement can be achieved through multiple methods that will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, network devices with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the device interface. If the device provides access to the audit data, the device becomes accountable for ensuring audit information is protected from unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to protect audit information from any type of unauthorized read access. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Options. Verify authorized access is configured for each role under "Log Access". If the BIG-IP appliance does not protect audit information from any type of unauthorized read access, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228987`

### Rule: The BIG-IP appliance must be configured to use NIAP evaluated cryptographic mechanisms to protect the integrity of audit information at rest.

**Rule ID:** `SV-228987r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records may be tampered with. If the integrity of audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. Protection of audit records and audit data, including audit configuration settings, is of critical importance. Cryptographic mechanisms are the industry-established standard used to protect the integrity of audit data. An example of a cryptographic mechanism is the computation and application of a cryptographic-signed hash using asymmetric cryptography. This requirement is not intended to cause a new cryptographic hash to be generated every time a record is added to a log file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to off-load audit information to a logging system that uses NIAP evaluated cryptographic mechanisms to protect the integrity of audit information at rest. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Remote Logging. Verify a syslog destination is configured that uses NIAP evaluated cryptographic mechanisms to protect the integrity of audit information at rest. If the BIG-IP appliance does not off-load audit information to a remote logging system that uses NIAP evaluated cryptographic mechanisms to protect the integrity of audit information at rest, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228988`

### Rule: The BIG-IP appliance must be configured to uniquely identify and authenticate organizational administrators (or processes acting on behalf of organizational administrators).

**Rule ID:** `SV-228988r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational administrators must be uniquely identified and authenticated for all network management accesses to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that uniquely identifies and authenticates organizational administrators. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that uniquely identifies and authenticates organizational administrators. If the BIG-IP appliance is not configured to use a properly configured authentication server that uniquely identifies and authenticates organizational administrators, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228989`

### Rule: The BIG-IP appliance must be configured to prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-228989r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the network device allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that prohibits password reuse for a minimum of five generations. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that prohibits password reuse for a minimum of five generations. If the BIG-IP appliance is not configured to use an associated authentication server that prohibits password reuse for a minimum of five generations, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228990`

### Rule: The BIG-IP appliance must be configured to enforce 24 hours/1 day as the minimum password lifetime.

**Rule ID:** `SV-228990r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. Restricting this setting limits the user's ability to change their password. Passwords need to be changed at specific policy-based intervals; however, if the network device allows the user to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that enforces 24 hours/1 day as the minimum password lifetime. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that enforces 24 hours/1 day as the minimum password lifetime. If the BIG-IP appliance is not configured to use a properly configured authentication server that enforces 24 hours/1 day as the minimum password lifetime, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228991`

### Rule: The BIG-IP appliance must be configured to enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-228991r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the network device does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the passwords could be compromised. This requirement does not include emergency administration accounts that are meant for access to the network device in case of failure. These accounts are not required to have maximum password lifetime restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that enforces a 60-day maximum password lifetime. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify "Authentication: User Directory" is configured for an approved remote authentication server that enforces a 60-day maximum password lifetime restriction. If the BIG-IP appliance is not configured to use a properly configured authentication server that enforces a 60-day maximum password lifetime, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228992`

### Rule: The BIG-IP appliance must be configured to automatically remove or disable emergency accounts after 72 hours.

**Rule ID:** `SV-228992r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are administrator accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If emergency accounts remain active when no longer needed, they may be used to gain unauthorized access. The risk is greater for the network device since these accounts have elevated privileges. To mitigate this risk, automated termination of all emergency accounts must be set upon account creation. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by network administrators when network or normal logon/access is not available). Infrequently used accounts also remain available and are not subject to automatic termination dates. However, an emergency account is normally a different account that is created for use by vendors or system maintainers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured remote authentication server to automatically disable or remove emergency accounts after 72 hours. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that automatically removes or disables emergency accounts after 72 hours. If the use of emergency accounts is prohibited, this is not a finding. If the BIG-IP appliance is not configured to use a properly configured authentication server to automatically disable or remove emergency accounts after 72 hours, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228993`

### Rule: The application must be configured to reveal error messages only to authorized individuals (ISSO, ISSM, and SA).

**Rule ID:** `SV-228993r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state. Additionally, sensitive account information must not be revealed through error messages to unauthorized personnel or their designated representatives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to reveal error messages only to authorized individuals (ISSO, ISSM, and SA). Navigate to the BIG-IP System manager >> Logs >> Configuration >> Options. Verify that "Log Access" is granted only to authorized individuals (ISSO, ISSM, and SA). If the BIG-IP appliance reveals error messages to any unauthorized individuals (ISSO, ISSM, and SA), this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228994`

### Rule: The BIG-IP appliance must be configured to activate a system alert message, send an alarm, and/or automatically shut down when a component failure is detected.

**Rule ID:** `SV-228994r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Predictable failure prevention requires organizational planning to address device failure issues. If components key to maintaining the device's security fail to function, the device could continue operating in an unsecure state. If appropriate actions are not taken when a network device failure occurs, a denial of service condition may occur that could result in mission failure since the network would be operating without a critical security monitoring and prevention function. Upon detecting a failure of network device security components, the network device must activate a system alert message, send an alarm, or shut down.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to activate a system alert message, send an alarm, and/or automatically shut down when a component failure is detected. Navigate to the BIG-IP System manager >> Logs >> Configuration >> Options. Verify that "MCP" under the "Audit Logging" section is set to Debug. Navigate to the BIG-IP System manager >> System >> High Availability >> Fail-Safe >> System. Verify "Switch Board Failure" under the "System Trigger Properties" section is set to perform the appropriate action based on the location of the device. If the BIG-IP appliance is not configured to activate a system alert message, send an alarm, or automatically shut down when a component failure is detected, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228995`

### Rule: The BIG-IP appliance must be configured to generate alerts that can be forwarded to the administrators and Information System Security Officer (ISSO) when accounts are created.

**Rule ID:** `SV-228995r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of accounts and notifies administrators and the ISSO. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to generate alerts that can be forwarded to the administrators and ISSO when accounts are created. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that generates alerts that can be forwarded to the administrators and ISSO when accounts are created. If the BIG-IP appliance is not configured to use an authentication server that would perform this function, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228996`

### Rule: The BIG-IP appliance must be configured to generate alerts that can be forwarded to the administrators and Information System Security Officer (ISSO) when accounts are modified.

**Rule ID:** `SV-228996r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply modify an existing account. Notification of account modification is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the modification of device administrator accounts and notifies administrators and the ISSO. Such a process greatly reduces the risk that accounts will be surreptitiously modified and provides logging that can be used for forensic purposes. The network device must generate the alert. Notification may be done by a management server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that generates alerts that can be forwarded to the administrators and ISSO when accounts are modified. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that generates alerts that can be forwarded to the administrators and ISSO when accounts are modified. If the BIG-IP appliance is not configured to use an authentication server that would perform this function, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228997`

### Rule: The BIG-IP appliance must be configured to generate alerts that can be forwarded to the administrators and Information System Security Officer (ISSO) when accounts are disabled.

**Rule ID:** `SV-228997r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are disabled, administrator accessibility is affected. Accounts are utilized for identifying individual device administrators or for identifying the device processes themselves. In order to detect and respond to events that affect administrator accessibility and device processing, devices must audit account-disabling actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that device accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that generates alerts that can be forwarded to the administrators and ISSO when accounts are disabled. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that generates alerts that can be forwarded to the administrators and ISSO when accounts are disabled. If the BIG-IP appliance is not configured to use an authentication server that would perform this function, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228998`

### Rule: The BIG-IP appliance must be configured to generate alerts that can be forwarded to the administrators and Information System Security Officer (ISSO) when accounts are removed.

**Rule ID:** `SV-228998r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are removed, administrator accessibility is affected. Accounts are utilized for identifying individual device administrators or for identifying the device processes themselves. In order to detect and respond to events that affect administrator accessibility and device processing, devices must audit account removal actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that device accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that generates alerts that can be forwarded to the administrators and ISSO when accounts are removed. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that generates alerts that can be forwarded to the administrators and ISSO when accounts are removed. If the BIG-IP appliance is not configured to use an authentication server that would perform this function, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229000`

### Rule: The BIG-IP appliance must be configured to generate an immediate alert for account-enabling actions.

**Rule ID:** `SV-229000r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of application user accounts and notifies administrators and ISSOs. Such a process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes. In order to detect and respond to events that affect network administrator accessibility and device processing, network devices must audit account-enabling actions and, as required, notify the appropriate individuals so they can investigate the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured remote authentication server to generate an immediate alert for account-enabling actions. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type to generate an immediate alert for account-enabling actions. If the BIG-IP appliance is not configured to use a properly configured remote authentication server to generate an immediate alert for account-enabling actions, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229001`

### Rule: The BIG-IP appliance must be configured to transmit access authorization information using approved security safeguards to authorized information systems that enforce access control decisions.

**Rule ID:** `SV-229001r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting access authorization information (i.e., access control decisions) ensures that authorization information cannot be altered, spoofed, or otherwise compromised during transmission. In distributed information systems, authorization processes and access control decisions may occur in separate parts of the systems. In such instances, authorization information is transmitted securely so timely access control decisions can be enforced at the appropriate locations. To support the access control decisions, it may be necessary to transmit, as part of the access authorization information, supporting security attributes. This is because, in distributed information systems, there are various access control decisions that need to be made, and different entities (e.g., services) make these decisions in a serial fashion, each requiring some security attributes to make the decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that transmits access authorization information using approved security safeguards to authorized information systems that enforce access control decisions. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server and SSL is set to use TLS. If the BIG-IP appliance transmits access authorization information without using approved security safeguards to authorized information systems that enforce access control decisions, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229002`

### Rule: The BIG-IP appliance must be configured to automatically lock the account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded.

**Rule ID:** `SV-229002r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured remote authentication server to automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that automatically locks the account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded. If an account is not automatically locked out until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229003`

### Rule: The BIG-IP appliance must be configured to notify the administrator, upon successful logon (access), of the location of last logon (terminal or IP address) in addition to the date and time of the last logon (access).

**Rule ID:** `SV-229003r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their account. Providing them with information deemed important by the organization may aid in the discovery of unauthorized access or thwart a potential attacker. Organizations should consider the risks to the specific information system being accessed and the threats presented by the device to the environment when configuring this option. An excessive or unnecessary amount of information presented to the administrator at logon is not recommended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that is able to notify the administrator upon successful logon of the location of last logon (terminal or IP address) in addition to the date and time of the last logon. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that is able to notify the administrator upon successful logon of the location of last logon (terminal or IP address) in addition to the date and time of the last logon. If the administrator is not notified of the location of last logon (terminal or IP address) upon successful logon (terminal or IP address) in addition to the date and time of the last logon, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229005`

### Rule: The BIG-IP appliance must be configured to generate an immediate alert when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity.

**Rule ID:** `SV-229005r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If security personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion. This could lead to the loss of audit information. Note that while the network device must generate the alert, notification may be done by a management server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured syslog server that generates an immediate alert when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Remote Logging. Verify a syslog destination is configured that generates an immediate alert when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity. If an immediate alert is not generated when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229006`

### Rule: The BIG-IP appliance must be configured to implement automated security responses if baseline configurations are changed in an unauthorized manner.

**Rule ID:** `SV-229006r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the device vulnerable to various attacks or allow unauthorized access to the device. Changes to device configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the device. Examples of security responses include, but are not limited to, the following: halting application processing; halting selected functions; or issuing alerts/notifications to organizational personnel when there is an unauthorized modification of a configuration item. The appropriate automated security response may vary depending on the nature of the baseline configuration change, the role of the network device, the availability of organizational personnel to respond to alerts, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to implement automated security responses if baseline configurations are changed in an unauthorized manner. Navigate to the BIG-IP System manager >> Logs >> Configuration >> Options. Review configuration in the "Audit Logging" section. Verify that "MCP" is set to Debug. If the BIG-IP appliance is not configured to implement automated security responses if baseline configurations are changed in an unauthorized manner, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229007`

### Rule: The BIG-IP appliance must be configured to dynamically manage user accounts.

**Rule ID:** `SV-229007r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Dynamic user account management prevents disruption of operations by minimizing the need for system restarts. Dynamic establishment of new user accounts will occur while the system is operational. New user accounts or changes to existing user accounts must take effect without the need for a system or session restart. Pre-established trust relationships and mechanisms with appropriate authorities (e.g., Active Directory or authentication server) that validate each user account are essential to prevent unauthorized access by changed or revoked accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that dynamically manages user accounts. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that is configured to dynamically manage user accounts. If the BIG-IP appliance is not configured to use a properly configured authentication server to dynamically manage user accounts, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229008`

### Rule: The BIG-IP appliance must be configured to allow the use of a temporary password for system logons with an immediate change to a permanent password.

**Rule ID:** `SV-229008r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without providing this capability, an account may be created without a password. Non-repudiation cannot be guaranteed once an account is created if a user is not forced to change the temporary password upon initial logon. Temporary passwords are typically used to allow access to applications when new accounts are created or passwords are changed. It is common practice for administrators to create temporary passwords for user accounts that allow the users to log on yet force them to change the password once they have successfully authenticated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use an authentication server that allows the use of a temporary password for system logons with an immediate change to a permanent password. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that allows the use of a temporary password for system logons with an immediate change to a permanent password. If the BIG-IP appliance is not configured to authenticate through an authentication server that allows the use of a temporary password for system logons with an immediate change to a permanent password, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229009`

### Rule: The BIG-IP appliance must be configured to notify the administrator of the number of successful logon attempts occurring during an organization-defined time period.

**Rule ID:** `SV-229009r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their network device management account. Providing administrators with information regarding the date and time of their last successful logon allows the administrator to determine if any unauthorized activity has occurred. This incorporates all methods of logon, including, but not limited to, SSH, HTTP, HTTPS, and physical connectivity. The organization-defined time period is dependent on the frequency with which administrators typically log on to the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a properly configured authentication server that notifies the administrator of the number of successful logon attempts occurring during an organization-defined time period. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that notifies the administrator of the number of successful logon attempts occurring during an organization-defined time period. If the BIG-IP appliance is not configured to use a properly configured authentication server to notify the administrator of the number of successful logon attempts occurring during an organization-defined time period, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229010`

### Rule: The BIG-IP appliance must be configured to use automated mechanisms to alert security personnel to threats identified by authoritative sources (e.g., CTOs) and IAW with CJCSM 6510.01B.

**Rule ID:** `SV-229010r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By immediately displaying an alarm message, potential security violations can be identified more quickly even when administrators are not logged onto the network device. An example of a mechanism to facilitate this would be through the utilization of SNMP traps.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use automated mechanisms to alert security personnel to threats identified by authoritative sources (e.g., CTOs) and IAW with CJCSM 6510.01B. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Log Destinations. Verify a log destination is configured for a CNDSP or other mechanism that is monitored by security personnel. If the BIG-IP appliance is not configured to use automated mechanisms to alert security personnel to threats identified by authoritative sources (e.g., CTOs) and IAW with CJCSM 6510.01B, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229011`

### Rule: The BIG-IP appliance must be configured to employ automated mechanisms to centrally apply authentication settings.

**Rule ID:** `SV-229011r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server to centrally apply authentication settings. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that employs automated mechanisms to centrally apply authentication settings. If authentication settings are not applied centrally using automated mechanisms, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229012`

### Rule: The BIG-IP appliance must be configured to employ automated mechanisms to centrally verify authentication settings.

**Rule ID:** `SV-229012r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to use a remote authentication server to centrally verify authentication settings. Navigate to the BIG-IP System manager >> System >> Users >> Authentication. Verify that "User Directory" is set to an approved authentication server type that employs automated mechanisms to centrally verify authentication settings. If authentication settings are not verified centrally using automated mechanisms, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229013`

### Rule: The BIG-IP appliance must be configured to employ automated mechanisms to assist in the tracking of security incidents.

**Rule ID:** `SV-229013r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Despite the investment in perimeter defense technologies, enclaves are still faced with detecting, analyzing, and remediating network breaches and exploits that have made it past the network device. An automated incident response infrastructure allows network operations to immediately react to incidents by identifying, analyzing, and mitigating any network device compromise. Incident response teams can perform root cause analysis, determine how the exploit proliferated, and identify all affected nodes, as well as contain and eliminate the threat. The network device assists in the tracking of security incidents by logging detected security events. The audit log and network device application logs capture different types of events. The audit log tracks audit events occurring on the components of the network device. The application log tracks the results of the network device content filtering function. These logs must be aggregated into a centralized server and can be used as part of the organization's security incident tracking and analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP appliance is configured to employ automated mechanisms to assist in the tracking of security incidents. Navigate to the BIG-IP System manager >> System >> Logs >> Configuration >> Log Destinations. Verify a log destination is configured for a system that employs automated mechanisms to assist in the tracking of security incidents. If such automated mechanisms are not employed, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-230217`

### Rule: If the BIG-IP appliance is being used to authenticate users for web applications, the HTTPOnly flag must be set.

**Rule ID:** `SV-230217r961620_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The HttpOnly attribute directs browsers to use cookies by way of the HTTP and HTTPS protocols only, ensuring that the cookie is not available by other means, such as JavaScript function calls. This setting mitigates the risk of attack utilizing Cross Site Scripting (XSS). This vulnerability allows an attacker to impersonate any authenticated user that has visited a page with the attack deployed, allowing them to potentially allowing the user to raise their permissions level. The vulnerability can be mitigated by setting HTTPOnly on the appropriate Access Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP ASM module is not used to support user authentication, this is not applicable. Navigate to Security >> Options >> Application Security >> Advanced Configuration >> System Variables Verify cookie_httponly_attr is set to 1. If the BIG-IP appliance is being used to authenticate users for web applications, the HTTPOnly flag must be set, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-259332`

### Rule: The F5 BIG-IP appliance must be configured to restrict a consistent inbound IP for the entire management session.

**Rule ID:** `SV-259332r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This security measure helps limit the effects of denial-of-service attacks by employing anti-session hijacking security safeguards. Session hijacking, also called cookie hijacking, is the exploitation of a valid computer session to gain unauthorized access to an application. The attacker steals (or hijacks) the cookies from a valid user and attempts to use them for authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. System. 2. Preferences. 3. Under "Security Settings", verify "Require A Consistent Inbound IP For The Entire Web Session" box is checked. If the BIG-IP appliance is not configured to require a consistent inbound IP for the entire session for management sessions, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-260049`

### Rule: The F5 BIG-IP appliance providing user access control intermediary services must display the Standard Mandatory DOD-approved Notice and Consent Banner before granting access to SSH.

**Rule ID:** `SV-260049r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DoD banner is added to SSH. From the BIG-IP GUI: 1. System. 2. Configuration. 3. Device. 4. SSHD. 5. Verify the box for "Show The Security Banner On The Login Screen" is checked. 6. Review the "Security Banner Text To Show On The Login Screen" under the "Security Settings" section for the following verbiage: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." From the BIG-IP Console: tmsh list sys sshd banner # should return a value of 'enabled' tmsh list sys sshd banner-text # should return a value of: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. At any time, the USG may inspect and seize data stored on this IS. Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If such a banner is not presented, this is a finding.

## Group: SRG-APP-000457-NDM-000352

**Group ID:** `V-270898`

### Rule: The version of F5 BIG-IP must be a supported version.

**Rule ID:** `SV-270898r1056138_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified period from the availability of the update. The specific period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
BIG-IP versions supported by this STIG (version 15.1x and earlier) are no longer supported by the vendor. If the system is running BIG-IP version 15.1x or earlier, this is a finding.

