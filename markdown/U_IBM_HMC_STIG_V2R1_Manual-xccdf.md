# STIG Benchmark: IBM Hardware Management Console (HMC) Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256857`

### Rule: The Enterprise System Connection (ESCON) Director (ESCD)  Application Console must be located in a secure location

**Rule ID:** `SV-256857r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The ESCD Application Console is used to add, change, and delete port configurations and dynamically switch paths between devices. If the ESCON Director Application Console is not located in a secured location, unauthorized personnel can bypass security, access the system, and alter the environment. This could impact the integrity and confidentiality of operations. NOTE: Many newer installations no longer support the ESCD Application Console. For installations not supporting the ESCD Application Console, this check is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESCD Application Console is present, verify the location of the ESCD Application Console, otherwise this check is not applicable. If the ESCON Director Application console is not located in a secure location this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-256858`

### Rule: Sign-on to the ESCD Application Console must be restricted to only authorized personnel.

**Rule ID:** `SV-256858r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESCD Application Console is used to add, change, and delete port configurations and to dynamically switch paths between devices. Access to the ESCD Application Console is restricted to three classes of personnel: Administrators, service representatives and operators. The administrator sign-on controls passwords at all levels, the service representative sign-on allows access to maintenance procedures, and the operator sign-on allows for configuration changes and use of the Director utilities. Unrestricted use by unauthorized personnel could impact the integrity of the environment. This would result in a loss of secure operations and impact data operating environment integrity. NOTE: Many newer installations no longer support the ESCD Application Console. For installations not supporting the ESCD Application Console, this check is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESCD Application Console is present, have the ESCON System Administrator verify that sign-on access to the ESCD Application Console is restricted to authorized personnel by signing on without a valid userid and password, otherwise this check is not applicable. If the ESCD Application Console sign-on access is not restricted, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-256859`

### Rule: The ESCON Director Application Console Event log must be enabled.

**Rule ID:** `SV-256859r958442_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The ESCON Director Console Event Log is used to record all ESCON Director Changes. Failure to create an ESCON Director Application Console Event log results in the lack of monitoring and accountability of configuration changes. In addition, its use in the execution of a contingency plan could be compromised and security degraded. NOTE: Many newer installations no longer support the ESCON Director Console. For installations not supporting the ESCON Director Console, this check is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESCON Director Console is present, verify on the ESCON Director Application Console that the Event log is in use, otherwise this check is not applicable. If no Event log exists, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-256860`

### Rule: The Distributed Console Access Facility (DCAF) Console must be restricted to only authorized personnel.

**Rule ID:** `SV-256860r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DCAF Console enables an operator to access the ESCON Director Application remotely. Access to a DCAF Console by unauthorized personnel could result in varying of ESCON Directors online or offline and applying configuration changes. Unrestricted use by unauthorized personnel could lead to bypass of security, unlimited access to the system, and an altering of the environment. This would result in a loss of secure operations and will impact data operating integrity of the environment. NOTE: Many newer installations no longer support the ESCON Director Application. For installations not supporting the ESCON Director Application, this check is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESCON Director Application is present, verify that sign-on access to the DCAF Console is restricted to authorized personnel, otherwise, this check is not applicable. If sign-on access to the DCAF Console is not restricted, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-256861`

### Rule: DCAF Console access must require a password to be entered by each user.


**Rule ID:** `SV-256861r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DCAF Console enables an operator to access the ESCON Director Application remotely. Access to a DCAF Console by unauthorized personnel could result in varying of ESCON Directors online or offline and applying configuration changes. Unrestricted use by unauthorized personnel could lead to bypass of security, unlimited access to the system, and an altering of the environment. This would result in a loss of secure operations and will impact data operating integrity of the environment. NOTE: Many newer installations no longer support the ESCON Director Application. For installations not supporting the ESCON Director Application, this check is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESCON Director Application is present, have the System Administrator attempt to sign on to the DCAF Console and validate that a password is required, otherwise, this check is not applicable. If sign-on access to the DCAF Console does not require a password this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256862`

### Rule: Unauthorized partitions must not exist on the system complex.

**Rule ID:** `SV-256862r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The running of unauthorized Logical Partitions (LPARs) could allow a “Trojan horse” version of the operating environment to be introduced into the system complex. This could impact the integrity of the system complex and the confidentiality of the data that resides in it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the Hardware Management Console, do the following: Access the Change LPAR Control Panel. (This will list the LPARs.) Compare the partition names listed on the Partition Page to the names entered on the Central Processor Complex Domain/LPAR Names table. Note: Each site should maintain a list of valid LPARS that are configured on thier system , what operating system, and the purpose of each LPAR. If unauthorized partitions exist on the system complex and the deviation is not documented, this is a FINDING.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-256863`

### Rule: On Classified Systems, Logical Partition must be restricted with read/write access to only its own IOCDS.

**Rule ID:** `SV-256863r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted control over the IOCDS files could result in unauthorized updates and impact the configuration of the environment by allowing unauthorized access to a restricted resource. This could severely damage the integrity of the environment and the system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the Hardware Management Console, verify that a logical partition cannot read or write to any IOCDS. Use the Security Definitions Page panel to do this by checking to see if the Input/Output (I/O) Configuration Control option has been turned on. NOTE: The default is applicable to only classified systems. Confirm whether or not the I/O Configuration Control option is checked. If the Logical Partition is not restricted with read/write access to only its own IOCDS, this is a FINDING.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-256864`

### Rule: Processor Resource/Systems Manager (PR/SM) must not allow unrestricted issuing of control program commands.

**Rule ID:** `SV-256864r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted control over the issuing of system commands by a Logical Partition could result in unauthorized data access and inadvertent updates. This could result in severe damage to system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the Hardware Management Console, verify that the Logical Partitions cannot issue control program commands to another Logical Partition. Use the PR/SM panel, known as the Security Definitions Page, to do this. The Cross Partition Control option must be turned off. NOTE: The default is that the Cross Partition Control option is turned off. If Processor Resource/Systems Manager (PR/SM) allows unrestricted issuing of control program commands then this is a FINDING

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-256865`

### Rule: Classified Logical Partition (LPAR) channel paths must be restricted.

**Rule ID:** `SV-256865r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Restricted LPAR channel paths are necessary to ensure data integrity. Unrestricted LPAR channel path access could result in a compromise of data integrity. When a classified LPAR exists on a mainframe which requires total isolation, all paths to that LPAR must be restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator or Systems Programmer on classified systems use the Hardware Management Console to verify that the LPAR channel paths are reserved from the rest of the LPARs. Use the Security Definitions Panel to verify this. The Logical Partition Isolation option must be turned on. If the Classified LPAR channel paths are not restricted then this is a FINDING.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-256866`

### Rule: On Classified Systems the Processor Resource/Systems Manager (PR/SM) must not allow access to system complex data.



**Rule ID:** `SV-256866r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing unrestricted access to all Logical Partition data could result in the possibility of unauthorized access and updating of data. This could also impact the integrity of the processing environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the Systems Administrator or Systems Programmer use the Hardware Management Console; to verify that the classified Logical Partition system data cannot be viewed by other Logical Partitions. Use the Security Definitions Panel to do this. The Global Performance Data Control option must be turned off. NOTE: The default is that the Global Performance Data Control option is turned off. If the PR/SM allows access to system complex data then, this is a FINDING.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-256867`

### Rule: Central processors must be restricted for classified/restricted Logical Partitions (LPARs).

**Rule ID:** `SV-256867r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing unrestricted access to classified processors for all LPARs could cause the corruption and loss of classified data sets, which could compromise classified processing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the system administrator or systems programmer use the Hardware Management Console; to verify that the LPAR processors are dedicated for exclusive use by classified LPARs. Use the Processor Page to do this. The Dedicated Central Processors option must be turned on. If Central processors are not restricted for classified/restricted LPARs, this is a FINDING.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256868`

### Rule: The Hardware Management Console must be located in a secure location.

**Rule ID:** `SV-256868r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Hardware Management Console is used to perform Initial Program Load (IPLs) and control the Processor Resource/System Manager (PR/SM). If the Hardware Management Console is not located in a secure location, unauthorized personnel can bypass security, access the system, and alter the environment. This can lead to loss of secure operations if not corrected immediately.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the location of the Hardware Management Console. It should be located in a controlled area. Access to it should be restricted. If the Hardware Management Console is not located in a secure location this is a FINDING.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256869`

### Rule: Dial-out access from the Hardware Management Console Remote Support Facility (RSF) must be restricted to an authorized vendor site.

**Rule ID:** `SV-256869r1001084_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Dial-out access from the Hardware Management Console could impact the integrity of the environment, by enabling the possible introduction of spyware or other malicious code. It is important to note that it should be properly configured to only go to an authorized vendor site. Note: This feature will be activated for Non-Classified Systems only. Also, many newer processors (e.g., zEC12/zBC12 processors) will not have modems. If there is no modem, this check is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Whenever dial-out hardware is present, have the System Administrator or Systems Programmer validate that dial-out access from the Hardware Management Console is enabled for any non-classified system. Note: This is accomplished by going to Hardware Management Console and selecting Customize Remote Services. Then verify that Enable Remote Services is active. If automatic dial-out access from the Hardware Management Console is enabled, have the Systems Administrator or Systems Programmer validate that remote phone number and remote service parameters values are valid authorized venders in the remote Service Panel of the Hardware Management Console. If all the above values are not correct, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256870`

### Rule: Dial-out access from the Hardware Management Console Remote Support Facility (RSF) must be disabled for all classified systems. 

**Rule ID:** `SV-256870r1001085_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This feature will not be activated for any classified systems. Allowing dial-out access from the Hardware Management Console could impact the integrity of the environment by enabling the possible introduction of spyware or other malicious code. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the Systems Administrator or Systems Programmer validate that dial-out access from the Hardware Management Console is not activated for any classified systems. Note: This can be accomplished by going to the Customize Remote Service Panel on the Hardware Management Console and verifying that enable remote service is not enabled. If this is a classified system and enable remote service is enabled, then this is a FINDING.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-256871`

### Rule: Access to the Hardware Management Console must be restricted to only authorized personnel.


**Rule ID:** `SV-256871r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access to the Hardware Management Console if not properly restricted to authorized personnel could lead to a bypass of security, access to the system, and an altering of the environment. This would result in a loss of secure operations and can cause an impact to data operating environment integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that sign-on access to the Hardware Management Console is restricted to authorize personnel and that a DD2875 is on file for each user ID. Note: Sites must have a list of valid HMC users, indicating their USER IDs, Date of DD2875, and roles and responsibilities To display user roles chose User Profiles and then select the user for modification. View Task Roles and Manager Resources Roles. If each user displayed by the System Administrator does not have a DD2875, then this is a FINDING.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-256872`

### Rule: Access to the Hardware Management Console (HMC) must be restricted by assigning users proper roles and responsibilities.

**Rule ID:** `SV-256872r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access to the HMC if not properly controlled and restricted by assigning users proper roles and responsibilities, could allow modification to areas outside the need-to-know and abilities of the individual resulting in a bypass of security and an altering of the environment. This would result in a loss of secure operations and can cause an impact to data operating environment integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator verify to the reviewer that the Roles and Responsibilities assigned are assigned to the proper individuals by their areas of responsibility. Note: Sites must have a list of valid HMC users, indicating their USERID, Date of DD2875, and roles and responsibilities. Have the System Administrator verify to the reviewer that the Roles and Responsibilities assigned are assigned to the proper individuals by their areas of responsibility. To display user roles chose User Profiles and then select the user for modification. View Task Roles and Manager Resources Roles. If the HMC user-IDs displayed by the System Administrator are not properly assigned by Roles and Responsibilities, then this is a FINDING.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-256873`

### Rule: Automatic Call Answering to the Hardware Management Console must be disabled.

**Rule ID:** `SV-256873r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic Call Answering to the Hardware Management Console allows unrestricted access by unauthorized personnel and could lead to a bypass of security, access to the system, and an altering of the environment. This would result in a loss of secure operations and impact the integrity of the operating environment, files, and programs. Note: Dial-in access to the Hardware Management Console is prohibited. Also, many newer processors (e.g., zEC12/zBC12 processors) will not have modems. If there is no modem, this check is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator verify if either the Enable Remote Operations parameter or the Automatic Call Answering parameter are active on the Enable Hardware Management Console Services panel. The Enable Remote Operations is found under Customize Remote Services and Automatic Call Answering is found under Customize Auto Answer Settings. If either of the above options are active, then this is a FINDING.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-256874`

### Rule: The Hardware Management Console Event log must be active.

**Rule ID:** `SV-256874r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Hardware Management Console controls the operation and availability of the Central Processor Complex (CPC). Failure to create and maintain the Hardware Management Console Event log could result in the lack of monitoring and accountability of CPC control activity. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify on the Hardware Management Console that the Event log is in use. This is done by selecting the View Console Events panel under Console Actions. From this panel you can display: Console Information on EC Changes Console Service History displays HMC Problems Console Tasks Displays Last 2000 tasks performed on console View Licenses View LIC (Licensed Internal Code) View Security Logs tracks an object’s operational state, status, or settings change or involves user access to tasks, actions, and objects. If no Event log exists, this is a FINDING. If the Event log exists and is not collecting data, this is a FINDING.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256875`

### Rule: The manufacturer’s default passwords must be changed for all Hardware Management Console   (HMC) Management software.

**Rule ID:** `SV-256875r1001086_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The changing of passwords from the HMC default values, blocks malicious users with knowledge of these default passwords, from creating a denial of service or from reconfiguring the HMC topology leading to a compromise of sensitive data. The system administrator will ensure that the manufacturer’s default passwords are changed for all HMC management software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator logon to the HMC and validate that all default passwords have been changed. Go to task Modify User, select user, select Modify and enter and confirm new password. User ID Default Password • OPERATOR PASSWORD • ADVANCED PASSWORD • SYSPROG PASSWORD • ACSADMIN PASSWORD The System Administrator is to validate that each user has his/her own user ID and password and that sharing of user-IDs and passwords is not permitted. Default user IDs and passwords are established as part of a base HMC. The System Administrator must assign new user IDs and passwords for each user and remove the default user IDs as soon as the HMC is installed by using the User Profiles task or the Manage Users Wizard. If all the default passwords have not been changed, and each user is not assigned a separate user ID and password, then this is a FINDING

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-256876`

### Rule: Predefined task roles to the Hardware Management Console (HMC) must be specified to limit capabilities of individual users.

**Rule ID:** `SV-256876r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Individual task roles with access to specific resources if not created and restricted, will allow unrestricted access to system functions. The following is an example of some managed resource categories: Tasks are functions that a user can perform, and the managed resource role defines where those tasks might be carried out. The Access Administrator assigns a user ID and user roles to each user of the Hardware Management Console. • OPERATOR OPERATOR • ADVANCED ADVANCED OPERATOR • ACSADMIN ACCESS ADMINISTRTOR • SYSPROG SYSTEM PROGRAMMER • SERVICE SRVICE REPRESENTATIVE Failure to establish this environment may lead to uncontrolled access to system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator display the user profiles and demonstrate that valid users are defined to valid roles and that authorities are restricted to the site list of users. Note: Sites must have a list of valid HMC users, indicating their USER IDs, Date of DD2875, and roles and responsibilities. To display user roles chose User Profiles and then select the user for modification. View Task Roles and Manager Resources Roles. If the different roles are not properly displayed or are not properly restricted, then this is a FINDING.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-256877`

### Rule: Individual user accounts with passwords must be maintained for the Hardware Management Console operating system and application.

**Rule ID:** `SV-256877r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identification and authentication, unauthorized users could reconfigure the Hardware Management Console or disrupt its operation by logging in to the system or application and execute unauthorized commands. The System Administrator will ensure individual user accounts with passwords are set up and maintained for the Hardware Management Console. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator prove that individual USER IDs are specified for each user and DD2875 are on file for each user. If USERIDs are shared among multiple users and crresponding DD2875 forms do not exist for each user, then this is a FINDING.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-256878`

### Rule: The PASSWORD History Count value must be set to 10 or greater.

**Rule ID:** `SV-256878r998329_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>History Count specifies the number of previous passwords saved for each USERID and compares it with an intended new password. If there is a match with one of the previous passwords, or with the current password, it will reject the intended new password. The improper setting of any of these fields, individually or in combination with another, can compromise the security of the processing environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the system administrator (SA) display the Password Profile Task window on the Hardware Management Console and validate that the History Count is set to 10. If the History Count is less than 10, then this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-256879`

### Rule: The PASSWORD expiration day(s) value must be set to equal or less then 60 days.

**Rule ID:** `SV-256879r998332_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Expiration Day(s) specifies the maximum number of days that each user's password is valid. When a user logs on to the Hardware Management Console it compares the system password interval value specified in the user profile and it uses the lower of the two values to determine if the user's, password has expired. The improper setting of any of these fields, individually or in combination with another, can compromise the security of the processing environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the system administrator (SA) display the Password Profile Task window on the Hardware Management Console and validate that the Expiration day(s) is set to equal or less than 60 days. If the expiration day(s) is set to equal or less then 60 days, this is not a finding. If the expiration day(s) is greater than 60 days, then this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-256880`

### Rule: Maximum failed password attempts before disable delay must be set to 3 or less.

**Rule ID:** `SV-256880r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Maximum failed attempts before disable delay is not set to 3. This specifies the number of consecutive incorrect password attempts the Hardware Management Console allows as 3 times, before setting a 60-minute delay to attempt to retry the password. The improper setting of any of these fields, individually or in combination with another, can compromise the security of the processing environment. Note: The Hardware Management Console does not allow a revoke of a userID. A 60- minute delay time setting is being substituted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator display the maximum failed attempts on the user properties table on the Hardware Management Console before disable delay is invoked. Maximum Failed Attempts and Disable Delay are found in User Profiles by selecting the user, selecting modify user and then selecting User Properties. If the Maximum failed attempts before disable delay is invoked is set at greater than 3, then this is a FINDING.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-256881`

### Rule: A maximum of 60-minute delay must be specified for the password retry after 3 failed attempts to enter your password

**Rule ID:** `SV-256881r958736_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Maximum failed attempts before disable delay is not set to 3. This specifies the number of consecutive incorrect password attempts the Hardware Management Console allows as 3 times, before setting a 60-minute delay to attempt to retry the password. The improper setting of any of these fields, individually or in combination with another, can compromise the security of the processing environment. Note: The Hardware Management Console does not allow a revoke of a user ID.A 60-minute delay time setting is being substituted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator display the Disable delay in minutes. Disable Delay is found in User Profiles by selecting the user, selecting modify user and then selecting User Properties. If this is les than 60 minutes then this is a finding. Note: Hardware Management Console does not have the ability to revoke a user ID, so a 60-minute delay has been imposed instead.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-256882`

### Rule: The password values must be set to meet the requirements in accordance with DODI 8500.2 for DoD information systems processing sensitive information and above, and CJCSI 6510.01E (INFORMATION ASSURANCE [IA] AND COMPUTER NETWORK DEFENSE [CND]).

**Rule ID:** `SV-256882r998335_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In accordance with DODI 8500.2 for DOD information systems processing sensitive information and above and CJCSI 6510.01E (INFORMATION ASSURANCE [IA] AND COMPUTER NETWORK DEFENSE [CND]). The following recommendations concerning password requirements are mandatory and apply equally to both classified and unclassified systems: (1) Passwords are to be 14 characters. (2) Passwords are to be a mix of uppercase, lowercase alphabetic, numeric, and special characters, including at least one of each. Special characters include the national characters (i.e., @, #, and $) and other nonalphabetic and nonnumeric characters typically found on a keyboard. The improper setting of any of these fields, individually or in combination with another, can compromise the security of the processing environment. In addition, failure to establish standardized settings for the Hardware Management Console control options introduces the possibility of exposure during the migration process or contingency plan activation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the system administrator (SA) display the Password Profile Task window on the Hardware Management Console and check that: Passwords are to be a minimum of 14 characters in length. Passwords are to be a mix of uppercase, lowercase alphabetic, numeric, and special characters, including at least one of each. Special characters include the national characters (i.e., @, #, and $) and other nonalphabetic and nonnumeric characters typically found on a keyboard. Each character of the password is to be unique, prohibiting the use of repeating characters. Passwords are to contain no consecutive characters (e.g., 12, AB, etc.). If the Password Profile does not have the specifications for the above options then this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-256883`

### Rule: The terminal or workstation must lock out after a maximum of 15 minutes of inactivity, requiring the account password to resume.

**Rule ID:** `SV-256883r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system, workstation, or terminal does not lock the session after more than15 minutes of inactivity, requiring a password to resume operations, the system or individual data could be compromised by an alert intruder who could exploit the oversight.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator display the User Properties window on the Hardware Management Console and check that the timeout minutes are set to a maximum of 15. If the Verify Timeout minutes are set to more than 15, then this is a FINDING.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-256884`

### Rule: The Department of Defense (DoD) logon banner must be displayed prior to any login attempt.

**Rule ID:** `SV-256884r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to display the required DoD logon banner prior to a login attempt may void legal proceedings resulting from unauthorized access to system resources and may leave the SA, IAO, IAM, and Installation Commander open to legal proceedings for not advising users that keystrokes are being audited.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the reviewer verify that the logon banner reads as follows:on the Create Welcome Text window: STANDARD MANDATORY DOD NOTICE AND CONSENT BANNER You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. If any item in above is untrue, this is a FINDING.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-256885`

### Rule: A private web server must subscribe to certificates, issued from any DOD-authorized Certificate Authority (CA), as an access control mechanism for web users.

**Rule ID:** `SV-256885r998338_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Hardware Management Consoles (HMC) is network-connected, use SSL encryption techniques, through digital certificates to provide message privacy, message integrity and mutual authentication between clients and servers. To maintain data integrity the IBM Certificate distributed with the HMC's is to be replaced by a DOD-authorized Certificate. Note: This check applies only to network-connected HMCs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The System Reviewer will have the system administrator (SA) use the Hardware Management Console Certificate Management Task to validate that the private key and certificate shipped with any network-connected HMC from IBM was replaced with an approved DOD-authorized Certificate. Note: This check applies only to network-connected HMCs. Note: DOD certificates should display the following Information: 'OU=PKI.OU=DoD.O=U.S. Government.C=US' If private web server does not subscribe to certificates issued from any DOD-authorized Certificate Authority (CA) as an access control mechanism for web users, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-256886`

### Rule: Hardware Management Console audit record content data must be backed up.

**Rule ID:** `SV-256886r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Hardware Management Console has the ability to backup and display the following data: 1) Critical console data 2) Critical hard disk information 3) Backup of critical CPC data and 4) Security Logs. Failure to backup and archive the listed data could make auditing of system incidents and history unavailable and could impact recovery for failed components. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator produce a log by date validating that backups are being performed for Security logs and Critical console data on a routine scheduled basis (e.g., daily, weekly, monthly, quarterly, annually) and copies are rotated to off site storage. Compare the list of backups made to a physical inventory of storage media to verify that HMC backups are being retained as expected. If backups are either not being made, or there are obvious gaps in storage and retention of the backups, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-256887`

### Rule: Audit records content must contain valid information to allow for proper incident reporting.

**Rule ID:** `SV-256887r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The content of audit data must validate that the information contains: User IDs Successful and unsuccessful attempts to access security files (e.g., audit records, password files, access control files, etc) Date and time of the event Type of event Success or failure of event Successful and unsuccessful logons Denial of access resulting from excessive number of logon attempts Failure to not contain this information may hamper attempts to trace events and not allow proper tracking of incidents during a forensic investigation</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator validate the audit records contain valid information to allow for a proper incident tracking. Use the View Console Events task to display contents of security logs. Use the View Console Events task to view security logs and validate that it has the following information: User IDs Successful and unsuccessful attempts to access security files (e.g., audit records, password files, access control files, etc) Date and time of the event Type of event Success or failure of event Successful and unsuccessful logons Denial of access resulting from excessive number of logon attempts

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256888`

### Rule: Hardware Management Console management must be accomplished by using the out-of-band or direct connection method.

**Rule ID:** `SV-256888r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing the management traffic from the production network diminishes the security profile of the Hardware Management Console servers by allowing all the management ports to be closed on the production network. The System Administrator will ensure that Hardware Management Console management is accomplished using the out-of-band or direct connection method.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The System Administrator will validate that the Hardware Management Console management connection will use TCP/IP with encryption on an out-of-band network. If the Hardware Management Console management connection does not use TCP/IP with encryption on an out-of-band network then this is a FINDING.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-256889`

### Rule: Product engineering access to the Hardware Management Console must be disabled.

**Rule ID:** `SV-256889r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Hardware Management Console has a built-in feature that allows Product Engineers access to the console. With access authority, IBM Product Engineering can log on the Hardware Management Console with an exclusive user identification (ID) that provides tasks and operations for problem determination. Product Engineering access is provided by a reserved password and permanent user ID. You cannot view, discard, or change the password and user ID, but you can control their use for accessing the Hardware Management Console. User IDs and passwords that are hard-coded and cannot be modified are a violation of NIST 800-53 and multiple other compliance regulations. Failure to disable this access would allow unauthorized access and could lead to security violations on the HMC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator or System Programmer validate that IBM Product Engineering access to the Hardware Management Console is disabled. This can be checked under the classic style user interface; this task is found under the Hardware Management Console Settings console action. Open the Customize Product Engineering Access task. The Customize Product Engineering Access window is displayed. Select the appropriate accesses for product engineering or remote product engineering. (Both should be disabled.) Click OK to save the changes and exit the task. If access to the Customize Product Engineering Access is not disabled, than this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256890`

### Rule: Connection to the Internet for IBM remote support must be in compliance with the Remote Access STIGs.

**Rule ID:** `SV-256890r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to securely connect to remote sites can leave systems open to multiple attacks and security violations through the network. Failure to securely implement remote support connections can lead to unauthorized access or denial of service attacks on the Hardware Management Console.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the Network Security Engineer or system Programmer check, that the remote Internet connection for IBM RSF support has met the requirements of the Remote Access STIGs. For controls that are a part of IBM’s closed system that cannot be updated or changed by customers, review provided documentation, such as found in the HMC Broadband Support manuals or a letter of Attestation provided by IBM assuring compliance. If the security measures in the Remote Access STIGs are not fully compliant and there is no supporting documentation or Letter of attestation on file with the IAM/IAO this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256891`

### Rule: Connection to the Internet for IBM remote support must be in compliance with mitigations specified in the Ports and Protocols and Services Management (PPSM) requirements.

**Rule ID:** `SV-256891r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to securely connect to remote sites can leave systems open to multiple attacks and security violations through the network. Failure to securely implement remote support connections can lead to unauthorized access or denial of service attacks on theHardware Management Console.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the Network Security Engineer check, that the remote Internet connection for IBM RSF support has met the mitigations outlined in Vulnerability Analysis for port 443/SSL in the PPSM requirements.

