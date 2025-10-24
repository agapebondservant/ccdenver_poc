# STIG Benchmark: Okta Identity as a Service (IDaaS) Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000003

**Group ID:** `V-273186`

### Rule: Okta must log out a session after a 15-minute period of inactivity.

**Rule ID:** `SV-273186r1098825_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session timeout lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications must be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock. However, it may be at the application level where the application interface window is secured instead. Satisfies: SRG-APP-000003, SRG-APP-000190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Global Session Policy. 2. In the Default Policy, verify a rule is configured at Priority 1 that is not named "Default Rule". 3. Click the edit icon next to the Priority 1 rule. 4. Verify the "Maximum Okta global session idle time" is set to 15 minutes. If "Maximum Okta global session idle time" is not set to 15 minutes, this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-273187`

### Rule: The Okta Admin Console must log out a session after a 15-minute period of inactivity.

**Rule ID:** `SV-273187r1098828_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session timeout lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications must be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock. However, it may be at the application level where the application interface window is secured instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Applications >> Applications >> Okta Admin Console. 2. In the Sign On tab, under "Okta Admin Console session", verify the "Maximum app session idle time" is set to 15 minutes. If the "Maximum app session idle time" is not set to 15 minutes, this is a finding.

## Group: SRG-APP-000025

**Group ID:** `V-273188`

### Rule: Okta must automatically disable accounts after a 35-day period of account inactivity.

**Rule ID:** `SV-273188r1098831_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers that are able to exploit an inactive account can potentially obtain and maintain undetected access to an application. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Applications must track periods of user inactivity and disable accounts after 35 days of inactivity. Such a process greatly reduces the risk that accounts will be hijacked, leading to a data compromise. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality. This policy does not apply to emergency accounts or infrequently used accounts. Infrequently used accounts are local login administrator accounts used by system administrators when network or normal login/access is not available. Emergency accounts are administrator accounts created in response to crisis situations. Satisfies: SRG-APP-000025, SRG-APP-000163, SRG-APP-000700</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Okta Services rely on external directory services for user sourcing, this is not applicable, and the connected directory services must perform this function. Go to Workflows >> Automations and verify that an Automation has been created to disable accounts after 35 days of inactivity. If the Okta configuration does not automatically disable accounts after a 35-day period of account inactivity, this is a finding.

## Group: SRG-APP-000065

**Group ID:** `V-273189`

### Rule: Okta must enforce the limit of three consecutive invalid login attempts by a user during a 15-minute time period.

**Rule ID:** `SV-273189r1098834_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. Satisfies: SRG-APP-000065, SRG-APP-000345</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Okta Services rely on external directory services for user sourcing, this check is not applicable, and the connected directory services must perform this function. From the Admin Console: 1. Go to Security >> Authenticators. 2. Click the "Actions" button next to "Password" and select "Edit". 3. For each Password Policy, verify the "Lock Out" section has the following values: - "Lock out after 3 unsuccessful attempts" is checked. - The value is set to "3". If Okta Services are not configured to automatically lock user accounts after three consecutive invalid login attempts, this is a finding.

## Group: SRG-APP-000065

**Group ID:** `V-273190`

### Rule: The Okta Dashboard application must be configured to allow authentication only via non-phishable authenticators.

**Rule ID:** `SV-273190r1099763_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring the use of non-phishable authenticators protects against brute force/password dictionary attacks. This provides a better level of security while removing the need to lock out accounts after three attempts in 15 minutes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Go to Security >> Authentication Policies. 2. Click the "Okta Dashboard" policy. 3. Click the "Actions" button next to the top rule and select "Edit". 4. In the "Possession factor constraints are" section, verify the "Phishing resistant" box is checked. This will ensure that only phishing-resistant factors are used to access the Okta Dashboard. If in the "Possession factor constraints are" section the "Phishing resistant" box is not checked, this is a finding.

## Group: SRG-APP-000065

**Group ID:** `V-273191`

### Rule: The Okta Admin Console application must be configured to allow authentication only via non-phishable authenticators.

**Rule ID:** `SV-273191r1099764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring the use of non-phishable authenticators protects against brute force/password dictionary attacks. This provides a better level of security while removing the need to lock out accounts after three attempts in 15 minutes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Go to Security >> Authentication Policies. 2. Click the "Okta Admin Console" policy. 3. Click the "Actions" button next to the top rule and select "Edit". 4. In the "Possession factor constraints are" section, verify the "Phishing resistant" box is checked. This will ensure that only phishing-resistant factors are used to access the Okta Dashboard. If in the "Possession factor constraints are" section the "Phishing resistant" box is not checked, this is a finding.

## Group: SRG-APP-000068

**Group ID:** `V-273192`

### Rule: Okta must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the application.

**Rule ID:** `SV-273192r1098843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the application ensures that privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-APP-000068, SRG-APP-000069, SRG-APP-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Attempt to log in to the Okta tenant and verify the DOD-approved warning banner is in place. If the required warning banner is not present and complete, this is a finding.

## Group: SRG-APP-000149

**Group ID:** `V-273193`

### Rule: The Okta Admin Console application must be configured to use multifactor authentication.

**Rule ID:** `SV-273193r1098846_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). Satisfies: SRG-APP-000149, SRG-APP-000154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Go to Security >> Authentication Policies. 2. Click the "Okta Admin Console" policy. 3. Click the "Actions" button next to the top rule and select "Edit". 4. In the "User must authenticate with" field, verify that either "Password/IdP + Another factor" or "Any 2 factor types" is selected. If either of these settings is incorrect, this is a finding.

## Group: SRG-APP-000150

**Group ID:** `V-273194`

### Rule: The Okta Dashboard application must be configured to use multifactor authentication.

**Rule ID:** `SV-273194r1098849_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, nonprivileged users must use multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: (i) Something you know (e.g., password/PIN); (ii) Something you have (e.g., cryptographic identification device, token); or (iii) Something you are (e.g., biometric). A nonprivileged account is any information system account with authorizations of a nonprivileged user. Network access is any access to an application by a user (or process acting on behalf of a user) where the access is obtained through a network connection. Applications integrating with the DOD Active Directory and using the DOD CAC are examples of compliant multifactor authentication solutions. Satisfies: SRG-APP-000150, SRG-APP-000155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Go to Security >> Authentication Policies. 2. Click the "Okta Dashboard" policy. 3. Click the "Actions" button next to the top rule and select "Edit". 4. In the "User must authenticate with" field, verify that either "Password/IdP + Another factor" or "Any 2 factor types" is selected. If either of these settings is incorrect, this is a finding.

## Group: SRG-APP-000164

**Group ID:** `V-273195`

### Rule: Okta must enforce a minimum 15-character password length.

**Rule ID:** `SV-273195r1098852_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Authenticators. 2. Click the "Actions" button next to the "Password" row and select "Edit". 3. For each listed policy, verify the "Minimum Length" field is set to at least "15" characters. If any policy is not set to at least "15", this is a finding.

## Group: SRG-APP-000166

**Group ID:** `V-273196`

### Rule: Okta must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-273196r1098855_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Authenticators. 2. Click the "Actions" button next to the "Password" row and select "Edit". 3. For each listed policy, verify "Upper case letter" is checked. For each policy, if "Upper case letter" is not checked, this is a finding.

## Group: SRG-APP-000167

**Group ID:** `V-273197`

### Rule: Okta must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-273197r1098858_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Authenticators. 2. Click the "Actions" button next to the "Password" row and select "Edit". 3. For each listed policy, verify "Lower case letter" is checked. For each policy, if "Lower case letter" is not checked, this is a finding.

## Group: SRG-APP-000168

**Group ID:** `V-273198`

### Rule: Okta must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-273198r1098861_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Authenticators. 2. Click the "Actions" button next to the "Password" row and select "Edit". 3. For each listed policy, verify "Number (0-9)" is checked. For each policy, if "Number (0-9)" is not checked, this is a finding.

## Group: SRG-APP-000169

**Group ID:** `V-273199`

### Rule: Okta must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-273199r1098864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Authenticators. 2. Click the "Actions" button next to the "Password" row and select "Edit". 3. For each listed policy, verify "Symbol (e.g., !@#$%^&*)" is checked. For each policy, if "Symbol (e.g., !@#$%^&*)" is not checked, this is a finding.

## Group: SRG-APP-000173

**Group ID:** `V-273200`

### Rule: Okta must enforce 24 hours/one day as the minimum password lifetime.

**Rule ID:** `SV-273200r1098867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. Restricting this setting limits the user's ability to change their password. Passwords must be changed at specific policy-based intervals; however, if the application allows the user to immediately and continually change their password, it could be changed repeatedly in a short period of time to defeat the organization's policy regarding password reuse. Satisfies: SRG-APP-000173, SRG-APP-000870</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Authenticators. 2. Click the "Actions" button next to the "Password" row and select "Edit". 3. For each listed policy, verify "Minimum password age is XX hours" is set to at least "24". For each policy, if "Minimum password age is XX hours" is not set to at least "24", this is a finding.

## Group: SRG-APP-000174

**Group ID:** `V-273201`

### Rule: Okta must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-273201r1098870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords must be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. This requirement does not include emergency administration accounts, which are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Authenticators. 2. Click the "Actions" button next to the "Password" row and select "Edit". 3. For each listed policy, verify "Password expires after XX days" is set to "60". For each policy, if "Password expires after XX days" is not set to "60", this is a finding.

## Group: SRG-APP-000358

**Group ID:** `V-273202`

### Rule: Okta must off-load audit records onto a central log server.

**Rule ID:** `SV-273202r1099766_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-APP-000358, SRG-APP-000080, SRG-APP-000125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Go to Reports >> Log Streaming. 2. Verify that a Log Stream connection is configured and active. Alternately, interview the information system security manager (ISSM) and verify that an external Security Information and Event Management (SIEM) system is pulling Okta logs via an Application Programming Interface (API). If either of these is not configured, this is a finding.

## Group: SRG-APP-000389

**Group ID:** `V-273203`

### Rule: Okta must be configured to limit the global session lifetime to 18 hours.

**Rule ID:** `SV-273203r1099958_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When applications provide the capability to change security roles or escalate the functional capability of the application, it is critical the user reauthenticate. In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of individuals and/or devices in other situations, including (but not limited to) the following circumstances. (i) When authenticators change; (ii) When roles change; (iii) When security categories of information systems change; (iv) When the execution of privileged functions occurs; (v) After a fixed period of time; or (vi) Periodically. Within the DOD, the minimum circumstances requiring reauthentication are privilege escalation and role changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Global Session Policy. 2. In the Default Policy, verify a rule is configured at Priority 1 that is not named "Default Rule". 3. Click the "Edit" icon next to the Priority 1 rule. 4. Verify "Maximum Okta global session lifetime" is set to 18 hours. If the above is not set, this is a finding.

## Group: SRG-APP-000391

**Group ID:** `V-273204`

### Rule: Okta must be configured to accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-273204r1098879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DOD has mandated the use of the common access card (CAC) to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems. Satisfies: SRG-APP-000391, SRG-APP-000402, SRG-APP-000403</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Go to Security >> Authenticators. 2. Verify that "Smart Card Authenticator" is listed and has "Status" listed as "Active". If "Smart Card Authenticator" is not listed or is not listed as "Active", this is a finding.

## Group: SRG-APP-000395

**Group ID:** `V-273205`

### Rule: The Okta Verify application must be configured to connect only to FIPS-compliant devices.

**Rule ID:** `SV-273205r1098882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without device-to-device authentication, communications with malicious devices may be established. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Currently, DOD requires the use of AES for bidirectional authentication because it is the only FIPS-validated AES cipher block algorithm. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network; the internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to apply the requirement only to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Go to Security >> Authenticators. 2. From the "Setup" tab, select "Edit Okta Verify". 3. Review the "FIPS Compliance" field. If FIPS-compliant authentication is not enabled, this is a finding.

## Group: SRG-APP-000400

**Group ID:** `V-273206`

### Rule: Okta must be configured to disable persistent global session cookies.

**Rule ID:** `SV-273206r1098885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable. Satisfies: SRG-APP-000400, SRG-APP-000157</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Global Session Policy. 2. In the Default Policy, verify a rule is configured at Priority 1 that is not named "Default Rule". 3. Click the "Edit" icon next to the Priority 1 rule. 4. Verify "Okta global session cookies persist across browser sessions" is set to "Disabled". If the above it not set, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-273207`

### Rule: Okta must be configured to use only DOD-approved certificate authorities.

**Rule ID:** `SV-273207r1098888_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not DOD approved, trust of this CA has not been established. The DOD will accept only PKI certificates obtained from a DOD-approved internal or external CA. Reliance on CAs for the establishment of secure sessions includes, for example, the use of Transport Layer Security (TLS) certificates. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that use communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA). Satisfies: SRG-APP-000427, SRG-APP-000910</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Identity Providers (IdPs). 2. Review the list of IdPs with "Type" as "Smart Card". If the IdP is not listed as "Active", this is a finding. 3. Select Actions >> Configure. 4. Under "Certificate chain", verify the certificate is from a DOD-approved CA. If the certificate is not from a DOD-approved CA, this is a finding.

## Group: SRG-APP-000830

**Group ID:** `V-273208`

### Rule: Okta must validate passwords against a list of commonly used, expected, or compromised passwords.

**Rule ID:** `SV-273208r1099769_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password-based authentication applies to passwords regardless of whether they are used in single-factor or multifactor authentication. Long passwords or passphrases are preferable over shorter passwords. Enforced composition rules provide marginal security benefits while decreasing usability. However, organizations may choose to establish certain rules for password generation (e.g., minimum character length for long passwords) under certain circumstances and can enforce this requirement in IA-5(1)(h). Account recovery can occur, for example, in situations when a password is forgotten. Cryptographically protected passwords include salted one-way cryptographic hashes of passwords. The list of commonly used, compromised, or expected passwords includes passwords obtained from previous breach corpuses, dictionary words, and repetitive or sequential characters. The list includes context-specific words, such as the name of the service, username, and derivatives thereof.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Navigate to Security >> Authenticators. 2. Click the "Actions" button next to the Password authenticator and select "Edit". 3. Under the "Password Settings" section, verify the "Common Password Check" box is checked. If "Common Password Check" is not selected, this is a finding.

## Group: SRG-APP-000845

**Group ID:** `V-273209`

### Rule: Okta must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-273209r1098894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password-based authentication applies to passwords regardless of whether they are used in single-factor or multifactor authentication. Long passwords or passphrases are preferable over shorter passwords. Enforced composition rules provide marginal security benefits while decreasing usability. However, organizations may choose to establish certain rules for password generation (e.g., minimum character length for long passwords) under certain circumstances and can enforce this requirement in IA-5(1)(h). Account recovery can occur, for example, in situations when a password is forgotten. Cryptographically protected passwords include salted one-way cryptographic hashes of passwords. The list of commonly used, compromised, or expected passwords includes passwords obtained from previous breach corpuses, dictionary words, and repetitive or sequential characters. The list includes context-specific words, such as the name of the service, username, and derivatives thereof.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Admin Console: 1. Select Security >> Authenticators. 2. Click the "Actions" button next to the "Password row" and select "Edit". 3. For each listed policy, verify "Enforce password history for last XX passwords" is set to "5". If any policy is not set to at least "5", this is a finding.

