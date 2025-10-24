# STIG Benchmark: Akamai KSD Service Impact Level 2 NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000075-NDM-000217

**Group ID:** `V-76457`

### Rule: Upon successful login, the Akamai Luna Portal must notify the administrator of the date and time of the last login.

**Rule ID:** `SV-91153r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their network device management account. Providing administrators with information regarding the date and time of their last successful login allows them to determine if any unauthorized activity has occurred. This incorporates all methods of login, including but not limited to SSH, HTTP, HTTPS, and physical connectivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the activity log is showing user login data: 1. Log in to the Luna Portal. 2. Verify that one of the four widgets includes the activity log. If the activity log is not showing, this is a finding.

## Group: SRG-APP-000516-NDM-000332

**Group ID:** `V-76459`

### Rule: The Akamai Luna Portal must notify the administrator of the number of successful login attempts.

**Rule ID:** `SV-91155r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their network device management account. Providing administrators with information regarding the date and time of their last successful login allows the administrator to determine if any unauthorized activity has occurred. This incorporates all methods of login, including but not limited to SSH, HTTP, HTTPS, and physical connectivity. The organization-defined time period is dependent on the frequency with which administrators typically log in to the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the activity log is showing user login data: 1. Log in to the Luna Portal. 2. Verify that one of the four widgets includes the activity log. If the activity log is not showing, this is a finding.

## Group: SRG-APP-000003-NDM-000202

**Group ID:** `V-76461`

### Rule: The Akamai Luna Portal must initiate a session logoff after a 15-minute period of inactivity.

**Rule ID:** `SV-91157r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary network device or administrator-initiated action taken when the administrator stops work but does not log out of the network device. Rather than relying on the user to manually lock their management session prior to vacating the vicinity, network devices need to be able to identify when a management session has idled and take action to initiate the session lock. Once invoked, the session lock must remain in place until the administrator reauthenticates. No other system activity aside from reauthentication must unlock the management session. When the network device is remotely administered, a session logoff may be the only practical option in lieu of a session lock. For a web portal, a session logoff must be invoked when idle time is exceeded for an administrator. Note that CCI-001133 requires that administrative network sessions be disconnected after 10 minutes of idle time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all portal users have the session timeout duration set to 15 minutes: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Manage Users & Groups. 3. Select each administrator and inspect the "Timeout" setting to verify it reads "After 15 Minutes". 4. Click "Save" button. If any user has a "Timeout" value other than "After 15 Minutes", this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-76463`

### Rule: The Akamai Luna Portal must automatically audit account creation.

**Rule ID:** `SV-91159r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click the "Settings" button and click on "Properties" tab. 5. Verify that the following setting is selected: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-76465`

### Rule: The Akamai Luna Portal must automatically audit account modification.

**Rule ID:** `SV-91161r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification along with an automatic notification to appropriate individuals will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click the "Settings" button and click on "Properties" tab. 5. Verify that the following setting is selected: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-76467`

### Rule: The Akamai Luna Portal must automatically audit account removal actions.

**Rule ID:** `SV-91163r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click the "Settings" button and click on "Properties" tab. 5. Verify that the following setting is selected: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000291-NDM-000275

**Group ID:** `V-76469`

### Rule: The Akamai Luna Portal must generate alerts that can be forwarded to the SAs and ISSO when accounts are created.

**Rule ID:** `SV-91165r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of accounts and notifies the SAs and ISSO. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click on "account creation". 5. Verify that the following settings are selected by clicking the "Settings" button: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000292-NDM-000276

**Group ID:** `V-76471`

### Rule: The Akamai Luna Portal must generate alerts that can be forwarded to the SAs and ISSO when accounts are modified.

**Rule ID:** `SV-91167r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply modify an existing account. Notification of account modification is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the modification of device administrator accounts and notifies the SAs and ISSO. Such a process greatly reduces the risk that accounts will be surreptitiously modified and provides logging that can be used for forensic purposes. The network device must generate the alert. Notification may be done by a management server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click on "account modification". 5. Verify that the following settings are selected by clicking the "Settings" button: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000294-NDM-000278

**Group ID:** `V-76473`

### Rule: The Akamai Luna Portal must generate alerts that can be forwarded to the SAs and ISSO when accounts are removed.

**Rule ID:** `SV-91169r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are removed, administrator accessibility is affected. Accounts are used for identifying individual device administrators or for identifying the device processes themselves. In order to detect and respond to events that affect administrator accessibility and device processing, devices must audit account removal actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that device accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click on "account removal". 5. Verify that the following settings are selected by clicking the "Settings" button: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-76475`

### Rule: The Akamai Luna Portal must automatically audit account enabling actions.

**Rule ID:** `SV-91171r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of application user accounts and notifies administrators and ISSOs. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click on "account enabling". 5. Verify that the following settings are selected by clicking the "Settings" button: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000320-NDM-000284

**Group ID:** `V-76477`

### Rule: The Akamai Luna Portal must notify the SAs and ISSO when accounts are created, or enabled when previously disabled.

**Rule ID:** `SV-91173r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies the SAs and ISSO. Such a process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes. In order to detect and respond to events that affect network administrator accessibility and device processing, network devices must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending the expected Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click on "account creation". 5. Verify that the following settings are selected by clicking the "Settings" button: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-76479`

### Rule: The Akamai Luna Portal must audit the execution of privileged functions.

**Rule ID:** `SV-91175r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending the expected Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click on "execution of privileged functions". 5. Verify that the following settings are selected by clicking the "Settings" button: "Manage - Manage Users". If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000089-NDM-000221

**Group ID:** `V-76481`

### Rule: The Akamai Luna Portal must provide audit record generation capability for DoD-defined auditable events within the network device.

**Rule ID:** `SV-91177r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., process, module). Certain specific device functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the device will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful login attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logins from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click on the DoD-defined auditable events individually. 5. Verify that the applicable events are selected by clicking the "Settings" button. If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-76483`

### Rule: The Akamai Luna Portal must generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-91179r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the portal is sending Luna Event notifications: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Alerts. 3. Search/filter for "Luna Control Center Event". 4. Click on the event name that meets the criteria above. 5. Verify that the applicable events are selected by clicking the "Settings" button. If the Luna Control Center event notifications are not enabled, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-76485`

### Rule: The Akamai Luna Portal must enforce a minimum 15-character password length.

**Rule ID:** `SV-91181r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the minimum 15-character length for passwords. Contact the Akamai Professional Services team to verify the changes at 1-877-4-AKATEC (1-877-425-2832). If the minimum password length is not 15-character, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-76487`

### Rule: If multifactor authentication is not supported and passwords must be used, the Akamai Luna Portal must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-91183r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the password must contain at least one upper-case character. Contact the Akamai Professional Services team to verify the changes at 1-877-4-AKATEC (1-877-425-2832). If the password does not require at least one upper-case character, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-76489`

### Rule: If multifactor authentication is not supported and passwords must be used, the Akamai Luna Portal must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-91185r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the password must contain at least one lower-case character. Contact the Akamai Professional Services team to verify the changes at 1-877-4-AKATEC (1-877-425-2832). If the password does not require at least one lower-case character, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-76491`

### Rule: If multifactor authentication is not supported and passwords must be used, the Akamai Luna Portal must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-91187r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the password must contain at least one numeric character. Contact the Akamai Professional Services team to verify the changes at 1-877-4-AKATEC (1-877-425-2832). If the password does not require at least one numeric character, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-76493`

### Rule: If multifactor authentication is not supported and passwords must be used, the Akamai Luna Portal must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-91189r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the password must contain at least one special character. Contact the Akamai Professional Services team to verify the changes at 1-877-4-AKATEC (1-877-425-2832). If the password does not require at least one special character, this is a finding.

## Group: SRG-APP-000174-NDM-000261

**Group ID:** `V-76495`

### Rule: The Akamai Luna Portal must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-91191r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the network device does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the passwords could be compromised. This requirement does not include emergency administration accounts, which are meant for access to the network device in case of failure. These accounts are not required to have maximum password lifetime restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the 60-day maximum password lifetime restriction is enforced. Contact the Akamai Professional Services team to verify the changes at 1-877-4-AKATEC (1-877-425-2832). If the 60-day maximum password lifetime restriction is not enforced, this is a finding.

## Group: SRG-APP-000165-NDM-000253

**Group ID:** `V-76497`

### Rule: The Akamai Luna Portal must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-91193r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the network device allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify password reuse for a minimum of five generations is prohibited. Contact the Akamai Professional Services team to verify the changes at 1-877-4-AKATEC (1-877-425-2832). If the password reuse for a minimum of five generations is not prohibited, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-76499`

### Rule: The Akamai Luna Portal must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 15 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-91195r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all portal users have the session timeout duration set to 15 minutes: 1. Log in to the Luna Portal as an administrator. 2. Select Configure >> Manage Users & Groups. 3. Select each user and inspect the "Timeout" setting to verify it reads "After 15 Minutes". If the session timeout is not set to 15 minutes, this is a finding.

## Group: SRG-APP-000516-NDM-000337

**Group ID:** `V-76501`

### Rule: The Akamai Luna Portal must employ Security Assertion Markup Language (SAML) to automate central management of administrators.

**Rule ID:** `SV-91197r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm that only SAML logins are enabled. 1. Log in to the Akamai Luna Portal (Caution-https://control.akamai.com). 2. Click "Configure" >> "Manage SSO with SAML" 3. Verify "SAML-only login:" is set to "enabled" If the "SAML only logins:" is set to disabled, this is a finding. NOTE: During the initial deployment and testing of the Luna Portal implementation, it will be necessary to allow other logins. However, production environments must meet this requirement.

## Group: SRG-APP-000516-NDM-000338

**Group ID:** `V-76503`

### Rule: The Akamai Luna Portal must employ Single Sign On (SSO) with Security Assertion Markup Language (SAML) integration to verify authentication settings.

**Rule ID:** `SV-91199r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Luna portal is configured to use single sign-on (SSO) with SAML. 1. Log in to the Akamai Luna Portal (Caution-https://control.akamai.com). 2. Click "Configure" >> "Manage SSO with SAML" 3. Verify the identity Provider's current SSO settings are configured properly. If SSO with SAML is not configured, then this is a finding.

