# STIG Benchmark: F5 BIG-IP Access Policy Manager Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-215714`

### Rule: The BIG-IP APM module must enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies.

**Rule ID:** `SV-215714r557355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user access control intermediary services as part of the traffic management functions of the BIG-IP Core, this is not applicable. Verify the BIG-IP APM module is configured to enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies. Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles >> Access Profiles List. Review Access Policy Profiles to verify configuration for authorization by employing identity-based, role-based, and/or attribute-based security policies. If the BIG-IP APM is not configured to enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies, this is a finding.

## Group: SRG-NET-000041-ALG-000022

**Group ID:** `V-215715`

### Rule: The F5 BIG-IP appliance providing user access control intermediary services must display the Standard Mandatory DOD-approved Notice and Consent Banner before granting access to resources.

**Rule ID:** `SV-215715r947409_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to ALGs (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide user access control intermediary services, this is not applicable. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify a Decision Box object exists that displays the DOD-approved Notice and Consent Banner. 6. Review the "Security Banner Text To Show On The Login Screen" under the "Security Settings" section for the following verbiage: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If a DOD-approved Notice and Consent Banner does not exist in the Access Profile VPE, this is a finding.

## Group: SRG-NET-000042-ALG-000023

**Group ID:** `V-215716`

### Rule: The BIG-IP APM module must retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users accessing virtual servers acknowledge the usage conditions and take explicit actions to log on for further access.

**Rule ID:** `SV-215716r557355_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The banner must be acknowledged by the user prior to allowing the user access to the network. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the application usage policy, a click-through banner at application logon is required. The network element must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user access control intermediary services, this is not applicable. Verify the BIG-IP APM module is configured to retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and takes explicit actions to log on for further access. Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for granting access. Verify the Access Profile is configured to retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users accessing virtual servers acknowledge the usage conditions and take explicit actions to log on for further access. If the BIG-IP APM module is not configured to retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access, this is a finding.

## Group: SRG-NET-000043-ALG-000024

**Group ID:** `V-215717`

### Rule: The BIG-IP APM module must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to publicly accessible applications.

**Rule ID:** `SV-215717r557355_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible network element ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to network elements that have the concept of a user account and have the logon function residing on the network element. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services off-loaded from the application. Publicly access systems are used in DoD to provide benefit information, pay information, or public services. There may also be self-registration and authorization services provided by these gateways.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user access control intermediary services, this is not applicable. Verify the BIG-IP APM module is configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to publicly accessible applications. Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for granting access. Verify the Access Profile is configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to publicly accessible applications. If the BIG-IP APM module is not configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to publicly accessible applications, this is a finding.

## Group: SRG-NET-000138-ALG-000063

**Group ID:** `V-215718`

### Rule: The BIG-IP APM module must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users) when connecting to virtual servers.

**Rule ID:** `SV-215718r557355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement applies to ALGs that provide user proxy services, including identification and authentication. This service must use the site's directory service (e.g., Active Directory). Directory services must not be installed onto the gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for granting access. Verify the Access Profile is configured to uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users). If the BIG-IP APM is not configured to uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users), this is a finding.

## Group: SRG-NET-000138-ALG-000088

**Group ID:** `V-215719`

### Rule: The BIG-IP APM module must be configured with a pre-established trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or authentication, authorization, and accounting (AAA) server) that validate user account access authorizations and privileges when providing access control to virtual servers.

**Rule ID:** `SV-215719r557355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User account and privilege validation must be centralized in order to prevent unauthorized access using changed or revoked privileges. ALGs can implement functions such as traffic filtering, authentication, access, and authorization functions based on computer and user privileges. However, the directory service (e.g., Active Directory or LDAP) must not be installed on the ALG, particularly if the gateway resides on the untrusted zone of the Enclave.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user access control intermediary services, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for granting access. Verify the Access Profile is configured with a pre-established trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or AAA server) that validate user account access authorizations and privileges. If the BIG-IP APM is not configured with a pre-established trust relationship and mechanisms with appropriate authorities that validate each user access authorization and privileges, this is a finding.

## Group: SRG-NET-000138-ALG-000089

**Group ID:** `V-215720`

### Rule: The BIG-IP APM module must restrict user authentication traffic to specific authentication server(s) when providing user authentication to virtual servers.

**Rule ID:** `SV-215720r557355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User authentication can be used as part of the policy filtering rule sets. Some URLs or network resources can be restricted to authenticated users only. Users are prompted by the application or browser for credentials. Authentication service may be provided by the ALG as an intermediary for the application; however, the authentication credential must be stored in the site's directory services server. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., proxy capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for granting access. Verify the Access Profile is configured to restrict user authentication traffic to specific authentication server(s). If the BIG-IP APM module is not configured to restrict user authentication traffic to a specific authentication server(s), this is a finding.

## Group: SRG-NET-000140-ALG-000094

**Group ID:** `V-215721`

### Rule: The BIG-IP APM module must use multifactor authentication for network access to non-privileged accounts.

**Rule ID:** `SV-215721r954210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: 1) Something you know (e.g., password/PIN); 2) Something you have (e.g., cryptographic, identification device, token); and 3) Something you are (e.g., biometric). Non-privileged accounts are not authorized on the network element regardless of configuration. Network access is any access to an application by a user (or process acting on behalf of a user) where said access is obtained through a network connection. The DoD CAC with DoD-approved PKI is an example of multifactor authentication. This requirement applies to ALGs that provide user authentication intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services, this is not applicable. Verify the BIG-IP APM is configured to use multifactor authentication for network access to non-privileged accounts. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for granting access. Verify the Access Profile is configured to use multifactor authentication for network access to non-privileged accounts. If the BIG-IP APM module is not configured to use multifactor authentication for network access to non-privileged accounts, this is a finding.

## Group: SRG-NET-000166-ALG-000101

**Group ID:** `V-215722`

### Rule: The BIG-IP APM module must map the authenticated identity to the user account for PKI-based authentication to virtual servers.

**Rule ID:** `SV-215722r557355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authorization for access to any network element requires an approved and assigned individual account identifier. To ensure only the assigned individual is using the account, the account must be bound to a user certificate when PKI-based authentication is implemented. This requirement applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide PKI-based, user authentication intermediary services, this is not applicable. Verify the BIG-IP APM module maps the authenticated identity to the user account for PKI-based authentication. Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for PKI-based authentication. Verify the Access Profile is configured to map the authenticated identity to the user account for PKI-based authentication. If the BIG-IP APM module does not map the authenticated identity to the user account for PKI-based authentication, this is a finding.

## Group: SRG-NET-000169-ALG-000102

**Group ID:** `V-215723`

### Rule: The BIG-IP APM module must be configured to uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users) when connecting to virtual servers.

**Rule ID:** `SV-215723r557355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication enables anyone to gain access to the network or possibly a network element that provides opportunity for intruders to compromise resources within the network infrastructure. By identifying and authenticating non-organizational users, their access to network resources can be restricted accordingly. Non-organizational users will be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access. Authorization requires an individual account identifier that has been approved, assigned, and configured on an authentication server. Authentication of user identities is accomplished through the use of passwords, tokens, biometrics, or in the case of multifactor authentication, some combination thereof. This control applies to application layer gateways that provide content filtering and proxy services on network segments (e.g., DMZ) that allow access by non-organizational users. This requirement focuses on authentication requests to the proxied application for access to destination resources and policy filtering decisions rather than administrator and management functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services to non-organizational users, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used to identify and authenticate non-organizational users. Verify the Access Profile is configured to uniquely identify and authenticate non-organizational users. If the BIG-IP APM module is not configured to uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users) when connecting to virtual servers, this is a finding.

## Group: SRG-NET-000313-ALG-000010

**Group ID:** `V-215726`

### Rule: The BIG-IP APM module access policy profile must control remote access methods to virtual servers.

**Rule ID:** `SV-215726r831441_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). ALGs that proxy remote access must be capable of taking enforcement action (i.e., blocking, restricting, or forwarding to an enforcement mechanism) if traffic monitoring reveals unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not serve as an intermediary for remote access traffic (e.g., web content filter, TLS and webmail), this is not applicable. Verify the BIG-IP APM module is configured to control remote access methods. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for managing remote access. Verify the Access Profile is configured to control remote access methods. If the BIG-IP APM module is not configured to control remote access methods, this is a finding.

## Group: SRG-NET-000337-ALG-000096

**Group ID:** `V-215727`

### Rule: The BIG-IP APM module must require users to reauthenticate when the user's role or information authorizations are changed.

**Rule ID:** `SV-215727r1050784_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which authorization has been removed. In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of individuals and/or devices in other situations. Within the DOD, the minimum circumstances requiring reauthentication are privilege escalation and role changes. This requirement only applies to components where this is specific to the function of the device or has the concept of user authentication (e.g., VPN or ALG capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for each Access Profile used for organizational access. If the BIG-IP APM module is not configured or process is not documented to require users to reauthenticate when the user's role or information authorizations are changed, this is a finding.

## Group: SRG-NET-000339-ALG-000090

**Group ID:** `V-215728`

### Rule: The BIG-IP APM module must be configured to require multifactor authentication for remote access with non-privileged accounts to virtual servers in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-215728r981642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For remote access to non-privileged accounts, the purpose of requiring a device that is separate from the information system gaining access for one of the factors during multifactor authentication is to reduce the likelihood of compromising authentication credentials stored on the system. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. An example of compliance with this requirement is the use of a one-time password token and PIN coupled with a password or the use of a CAC/PIV card and PIN coupled with a password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for remote access for non-privileged accounts. Verify the Access Profile is configured to require multifactor authentication for remote access with non-privileged accounts. If the BIG-IP APM module is not configured to require multifactor authentication for remote access to non-privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access, this is a finding.

## Group: SRG-NET-000340-ALG-000091

**Group ID:** `V-215729`

### Rule: The BIG-IP APM module must be configured to require multifactor authentication for remote access with privileged accounts to virtual servers in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-215729r981643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For remote access to privileged accounts, the purpose of requiring a device that is separate from the information system gaining access for one of the factors during multifactor authentication is to reduce the likelihood of compromising authentication credentials stored on the system. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for remote access for privileged accounts. Verify the Access Profile is configured to require multifactor authentication for remote access with privileged accounts. If the BIG-IP APM module is not configured to require multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access, this is a finding.

## Group: SRG-NET-000349-ALG-000106

**Group ID:** `V-215735`

### Rule: The BIG-IP APM module must conform to FICAM-issued profiles.

**Rule ID:** `SV-215735r981646_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without conforming to Federal Identity, Credential, and Access Management (FICAM)-issued profiles, the information system may not be interoperable with FICAM-authentication protocols, such as SAML 2.0 and OpenID 2.0. Use of FICAM-issued profiles addresses open identity management standards. This requirement only applies to components where this is specific to the function of the device or has the concept of a non-organizational user, (e.g., ALG capability that is the front end for an application in a DMZ).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services to non-organizational users, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used to identify and authenticate non-organizational users. Verify the Access Profile is configured to conform to FICAM-issued profiles. If the BIG-IP APM module is not configured to conform to FICAM-issued profiles, this is a finding.

## Group: SRG-NET-000380-ALG-000128

**Group ID:** `V-215736`

### Rule: The BIG-IP APM module must be configured to handle invalid inputs in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-215736r831446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability of network elements is unpredictable behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notifying the appropriate personnel, creating an audit record, and rejecting invalid input. This requirement applies to gateways and firewalls that perform content inspection or have higher layer proxy functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP APM module is configured to handle invalid inputs in a predictable and documented manner that reflects organizational and system objectives. This can be demonstrated by the SA sending an invalid input to a virtual server. Provide evidence that the virtual server was able to handle the invalid input and maintain operation. If the BIG-IP APM module is not configured to handle invalid inputs in a predictable and documented manner that reflects organizational and system objectives, this is a finding.

## Group: SRG-NET-000517-ALG-000006

**Group ID:** `V-230211`

### Rule: The BIG-IP APM module access policy profile must be configured to automatically terminate user sessions for users connected to virtual servers when organization-defined conditions or trigger events occur that require a session disconnect.

**Rule ID:** `SV-230211r856822_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. This capability is typically reserved for specific system functionality where the system owner, data owner, or organization requires additional trigger events based on specific mission needs. Conditions or trigger events requiring automatic session termination can include, for example, targeted responses to certain types of incidents and time-of-day restrictions on information system use. This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP Am module does not provide user access control intermediary services, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for organizational access. Verify the Access Profile is configured to automatically terminate user sessions when organization-defined conditions or trigger events occur that require a session disconnect. If the BIG-IP APM module is not configured to automatically terminate a user session when organization-defined conditions or trigger events occur that require a session disconnect, this is a finding.

## Group: SRG-NET-000519-ALG-000008

**Group ID:** `V-230212`

### Rule: The BIG-IP APM module access policy profile must be configured to display an explicit logoff message to users, indicating the reliable termination of authenticated communications sessions when disconnecting from virtual servers.

**Rule ID:** `SV-230212r856824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user cannot explicitly end a session, the session may remain open and be exploited by an attacker; this is referred to as a zombie session. Users need to be aware of whether or not the session has been terminated. Logoff messages for access, for example, can be displayed after authenticated sessions have been terminated. However, for some types of interactive sessions, including, for example, remote logon, information systems typically send logoff messages as final messages prior to terminating sessions. This policy only applies to ALGs (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user access control intermediary services, this is not applicable. Verify the BIG-IP APM module is configured as follows: Navigate to the BIG-IP System manager >> Access Policy >> Access Profiles. Click "Edit..." in the "Access Policy" column for an Access Profile used for connecting to virtual servers. Verify the Access Profile is configured to display an explicit logoff message to users, indicating the reliable termination of authenticated communications sessions. If the BIG-IP APM module is not configured to display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions, this is a finding.

## Group: SRG-NET-000337-ALG-000096

**Group ID:** `V-259330`

### Rule: The F5 BIG-IP appliance must be configured to set a "Maximum Session Timeout" value of 8 hours or less.

**Rule ID:** `SV-259330r1050784_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Maximum Session Timeout setting configures a limit on the maximum amount of time a user's session is active without needing to reauthenticate. If the value is set to 0 (zero), the user's session is active until either the user terminates the session or the Inactivity Timeout value is reached (the default value is set to 604,800 seconds). When determining how long the maximum user session can last, it may be useful to review the access policy. For example, if the access policy requires that the user's antivirus signatures cannot be older than 8 hours, the Maximum Session Timeout should not exceed that time limit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP APM module does not provide user authentication intermediary services, this is not applicable. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the Access profile name. 5. In the "Settings" section, verify the value for "Maximum Session Timeout" is set to 28800 seconds (8 hours) or less. If the F5 BIG-IP APM access policy is not configured for a "Maximum Session Timeout" value of 28,800 seconds (8 hours) or less, this is a finding.

## Group: SRG-NET-000345-ALG-000099

**Group ID:** `V-260050`

### Rule: The F5 BIG-IP appliance must be configured to deny access when revocation data is unavailable using OCSP.

**Rule ID:** `SV-260050r981644_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without configuring a local cache of revocation data, there is the potential to allow access to users who are no longer authorized (users with revoked certificates). Caching of CRL files on BIG-IP is not feasible or possible due to the large sizes of DOD/DISA CRL files. Use the alternate mitigation, configuring the system to deny access when revocation data is unavailable, which is done in the APM VPE.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide PKI-based user authentication intermediary services, this is not applicable. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify an "OSCP Auth" object is configured in the Access Profile VPE AND that the fallback branch of this object leads to a "Deny" ending. If the BIG-IP appliance is not configured to deny access when revocation data is unavailable, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-260051`

### Rule: The F5 BIG-IP appliance must configure OCSP to ensure revoked user credentials are prohibited from establishing an allowed session.

**Rule ID:** `SV-260051r947407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity, and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS), this is not applicable. Access Policy: From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify an "OCSP Auth" object is configured in the Access Profile for "User" type or a CRLDP object is configured. If the BIG-IP appliance is not configured to use OCSP or CRLDP to ensure revoked user credentials are prohibited from establishing an allowed session, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-260052`

### Rule: The F5 BIG-IP appliance must configure OCSP to ensure revoked machine credentials are prohibited from establishing an allowed session.

**Rule ID:** `SV-260052r947419_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity, and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide intermediary services for TLS, or application protocols that use TLS (e.g., DNSSEC or HTTPS), this is not applicable. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify an "OCSP Auth" object is configured in the Access Profile for "Machine" type or a CRLDP object is configured. If the BIG-IP appliance is not configured to use OCSP or CRLDP to ensure revoked machine credentials are prohibited from establishing an allowed session, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-260053`

### Rule: The F5 BIG-IP appliance must not use the On-Demand Cert Auth VPE agent as part of the APM Policy Profiles.

**Rule ID:** `SV-260053r947421_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By requiring mutual authentication before any communication, it becomes significantly challenging for attackers to impersonate a client or server and exploit vulnerabilities. Furthermore, the encryption of all data transmitted between the client and server ensures that even if an attacker intercepts the data, it remains unintelligible without the correct keys. To ensure the use of the mutual TLS (mTLS) for session authentication, the On-Demand Cert Auth VPE agent should not be used. Typically, when a client makes an HTTPS request, an SSL handshake request occurs at the start of an SSL session. However, if On-Demand is configured, the client SSL profile skips the initial SSL handshake, and On-Demand Cert Auth action can renegotiate the SSL connection from an access policy by sending a certificate request to the user. This prompts a certificate screen to open. Setting ODCA to "require" the client cert means the client cannot get any further in the APM VPE without providing a valid certificate. "Request" would ask the client for a certificate, but the client could still continue if they did not provide one. Thus, the Client Certificate should be set to "require" in the client SSL profile (F5BI-LT-000213) since removing ODCA from the VPE alone will result in the client never being prompted for a certificate. Within the Virtual Policy Editor (VPE) of the relevant Access Profile, do not use the On-Demand Cert Auth VPE agent. Configure only the Client Certification Inspection VPE Agent. This adjustment directs the BIG-IP to scrutinize the Client Certificate during the mTLS handshake process and extract the Certificate's details into APM session variables.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify removal of the On-Demand Cert Auth VPE agent. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Verify the On-Demand Cert Auth agent is not configured in any part of the profile. If the On-Demand Cert Auth agent is used in any Access Policy Profile, this is a finding.

## Group: SRG-NET-000355-ALG-000117

**Group ID:** `V-260054`

### Rule: The F5 BIG-IP appliance APM Access Policies that grant access to web application resources must allow only client certificates that have the User Persona Name (UPN) value in the User Persona Client Certificates.

**Rule ID:** `SV-260054r947386_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To enhance the security, it is advisable to append additional checks and APM Deny/Fallback branches to APM Access Profiles in scenarios where a UPN cannot be extracted. To guarantee the exclusive use of User Persona DISA Certificates for accessing Web Applications, it is recommended to carry out additional APM Access Policy checks against the Client Certificate. DISA incorporates a User Principal Name (UPN) in their User Persona Client Certificates. However, this key/value pair is not present in the DISA server certificates. Based on DOD session authentication policy, the LTM+APM configuration will include Client Certificate Authentication, OCSP Revocation Check, a Variable Assignment to extract the UserPrincipalName, followed by an LDAP query. This query verifies the existence of a corresponding Active Directory User object for the provided UserPrincipalName. Subsequently, the identified sAMAccountName is set as an APM Session variable for use by the SSO Profile. Once an APM LTM+APM session is granted, the User-Agent is permitted to transmit data to the Server-Side of the proxy, which will invoke the SSO Profile if applicable. To ensure that only DISA Client Certificates from CACs can access the Web Application, an additional branch was added to the Variable Assignment. The scripts were adjusted to verify the existence of the UserPrincipalName. If it does not exist, the value of the UserPrincipalName APM session variable is set to "UPN Collection Error", which would be directed to an APM Policy Deny. NPE Certificates issued by DISA incorporate both the TLS WWW Client Authentication (OID.1.3.6.1.5.5.7.3.2) and TLS WWW Server Authentication (OID.1.3.6.1.5.5.7.3.1) key usage policies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP appliance does not provide user authentication intermediary services, this is not applicable. If the site has documented that this setting has been tested operationally and is operationally harmful because of false positives, this is not a finding. 1. Review the applicable Access Control Profiles that give access to web application resources. 2. Verify that a Branch Rule exists to check for the UPN on the session certificate. 3. Verify there is a check for failed extractions that results in an APM Policy Deny. If any BIG-IP appliance APM Access Policies do not deny sessions using client certificates that do not have the DISA UPN, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-260055`

### Rule: The F5 BIG-IP appliance must be configured to limit authenticated client sessions to initial session source IP.

**Rule ID:** `SV-260055r947390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The "Restrict to Single Client IP" is a safeguard against session hijacking or cookie theft. Even if an attacker manages to steal a session cookie, the cookie cannot be used from a different source IP address that the address used to initiate the session. This security measure is set within the APM Access Pro?les. Sites should test this setting within their network prior to implementing. Users behind a shared proxy address may be denied access. Optionally, the F5 BIG-IP APM can be installed and used to produce access reports to find recurring IP sources within the user community.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the site has documented that this setting has been tested operationally and is operationally harmful because of false positives, this is not a finding. From the BIG-IP GUI: 1. System. 2. Access. 3. Profiles/Policies. 4. Access Profiles. 5. Click the Access profile name. 6. Under "Settings", verify "Restrict to Single Client IP" is checked. If the BIG-IP appliance is not configured to limit authenticated client sessions to initial session source IP, this is a finding.

## Group: SRG-NET-000053-ALG-000001

**Group ID:** `V-260056`

### Rule: The F5 BIG-IP appliance must be configured to set the "Max In Progress Sessions per Client IP" value to 10 or less.

**Rule ID:** `SV-260056r947393_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The "Max In Progress Sessions Per Client IP" setting in an APM Access Pro?le is a security con?guration that limits the number of simultaneous sessions that can be initiated from a single IP address. This is particularly helpful in preventing a session ?ood, where a hacker might attempt to overwhelm the system by initiating many sessions from a single source. By capping the number of sessions per IP, this setting can help maintain the system's stability and integrity while also providing a layer of protection against such potential attacks. False positives may result from this setting in networks where users are behind a shared proxy. Sites should conduct operational testing to determine if there are adverse operational impacts. Log reports should be obtained to identify recurring IP sources within the user community.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the site has documented that this setting has been tested operationally and is operationally harmful because of false positives, this is not a finding. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the Access profile name. 5. In the "Settings" section, verify "Max In Progress Sessions per Client IP" is set to 10 or less. If the F5 BIG-IP APM access policy is not configured to set a "Max In Progress Sessions per Client IP" value to 10 or less, this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-260057`

### Rule: The F5 BIG-IP appliance must enforce approved authorizations for logical access to resources by explicitly configuring assigned resources with an authorization list.

**Rule ID:** `SV-260057r947423_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication alone must not be sufficient to assign APM resources to a connecting client. Access to APM resources (e.g., Portal, VPN, Webtop, Remote Desktop, etc.,) must be granted only after a successful authorization check occurs. Resource assignments can be configured using APM Access Policy Advanced Resource Assign VPE agents and Resource Assign VPE agents. These agents must be configured explicitly with an authorization list. If resources are assigned to these types of agents with empty expressions, that expression acts as the default authorization list.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Advanced Resource Assign VPE agent is not used in any policy, this is not a finding. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" under "Per-Session Policy" for the Access Profile. 5. Review each Resource. - If the Advanced Resource Assign agent is used, verify that each Expression listed is explicitly configured to use an authorization list. If the F5 BIG-IP appliance Access Policy has any assigned resources that are not configured with a specific authorization list, this is a finding.

## Group: SRG-NET-000233-ALG-000115

**Group ID:** `V-260058`

### Rule: When the Access Profile Type is LTM+APM and it is not using any connectivity resources (such as Network Access, Portal Access, etc.) in the VPE, the F5 BIG-IP appliance must be configured to enable the HTTP Only flag.

**Rule ID:** `SV-260058r947399_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To guard against cookie hijacking, only the BIG-IP APM controller and client must be able to view the full session ID. Setting the APM HTTP Only flag ensures that a third party will not have access to the active session cookies. This option is only applicable to the LTM+APM access profile type. Other access profile types require access to various session cookies to fully function. Sites must conduct operational testing prior to enabling this setting. For implementations with connectivity resources (such as Network Access, Portal Access, etc.), do not set BIG-IP APM cookies with the HTTP Only flag.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Access Profile Type is not LTM+APM and it uses connectivity resources (such as Network Access, Portal Access, etc.) in the VPE, this is not a finding. From the BIG-IP GUI: 1. Access >> Profiles/Policies >> Access profile name >> SSO/Auth Domains. 2. Under "Cookie Options", verify "HTTP Only" is enabled. If the F5 BIG-IP appliance does not enable the HTTP Only flag, this is a finding.

## Group: SRG-NET-000233-ALG-000115

**Group ID:** `V-260059`

### Rule: The F5 BIG-IP appliance must be configured to enable the "Secure" cookie flag.

**Rule ID:** `SV-260059r947425_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To guard against cookie hijacking, only the BIG-IP APM controller and client must be able to view the full session ID. Session cookies are set only after the SSL handshake between the BIG-IP APM system and the user has completed, ensuring that the session cookies are protected from interception with SSL encryption. To ensure that the client browser will not send session cookies unencrypted, the HTTP header that the BIG-IP APM uses when sending the session cookie is set with the secure option (default). This option is only applicable to the LTM+APM access profile type.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the Access profile name. 5. "SSO/Auth Domains" tab. 6. Under "Cookie Options", verify "Secure" is enabled. If the F5 BIG-IP appliance APM Policy does not enable the "Secure" cookie flag, this is a finding.

## Group: SRG-NET-000233-ALG-000115

**Group ID:** `V-260060`

### Rule: The F5 BIG-IP appliance must be configured to disable the "Persistent" cookie flag.

**Rule ID:** `SV-260060r947405_rule`
**Severity:** low

**Description:**
<VulnDiscussion>For BIG-IP APM deployments with connectivity resources (such as Network Access, Portal Access, etc.), BIG-IP APM cookies cannot be set as "Persistent". This is by design since cookies are stored locally on the client's hard disk and thus could be exposed to unauthorized external access. For some deployments of the BIG-IP APM system, cookie persistence may be required. When cookie persistence is selected, persistence is hard coded at 60 seconds.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Access Profile is used for applications that require cookie persistence, this is not a finding. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click the Access profile name. 5. "SSO/Auth Domains" tab. 6. Under "Cookie Options", verify "Persistent" is disabled. If the F5 BIG-IP appliance APM Policy has the "Persistent" cookie flag enabled, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-270901`

### Rule: The version of F5 BIG-IP must be a supported version.

**Rule ID:** `SV-270901r1056147_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified period from the availability of the update. The specific period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
BIG-IP versions supported by this STIG (version 15.1x and earlier) are no longer supported by the vendor. If the system is running BIG-IP version 15.1x or earlier, this is a finding.

