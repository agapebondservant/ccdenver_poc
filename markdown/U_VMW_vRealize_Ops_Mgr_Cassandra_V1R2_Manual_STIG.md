# STIG Benchmark: VMware vRealize Ops Mgr - Cassandra Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-238509`

### Rule: The Cassandra database must have the correct authorizer value.

**Rule ID:** `SV-238509r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authentication with a DoD-approved PKI certificate does not necessarily imply authorization to access the DBMS. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems, including databases, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes database management systems. If the DBMS does not follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Cassandra Server settings to determine whether users are restricted from accessing objects and data they are not authorized to access. At the command prompt, execute the following command: # grep '^\s*authorizer:' /usr/lib/vmware-vcops/user/conf/cassandra/cassandra.yaml If the line below is returned, this is a finding: authorizer: AllowAllAuthorizer

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-238510`

### Rule: The Cassandra database must provide audit record generation capability for DoD-defined auditable events within all database components.

**Rule ID:** `SV-238510r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the DBMS (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the DBMS will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities, or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Organizations may define additional events requiring continuous or ad hoc auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Cassandra Server auditing settings to determine whether organization-defined auditable events are being audited by the system. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-238511`

### Rule: The Cassandra database must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-238511r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Cassandra Server settings and documentation to determine whether designated personnel are able to select which auditable events are being audited. At the command prompt, execute the following command: # ls -al /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If the permissions are not "0640", this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-238512`

### Rule: The Cassandra database must be able to generate audit records when privileges/permissions are retrieved.

**Rule ID:** `SV-238512r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure that audit records can be produced when privileges/permissions/role memberships are retrieved. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000091-DB-000325

**Group ID:** `V-238513`

### Rule: The Cassandra database must be able to generate audit records when unsuccessful attempts to retrieve privileges/permissions occur.

**Rule ID:** `SV-238513r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure that audit records can be produced when the system denies or fails to complete attempts to retrieve privileges/permissions/role membership. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000092-DB-000208

**Group ID:** `V-238514`

### Rule: The Cassandra database must initiate session auditing upon startup.

**Rule ID:** `SV-238514r879562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session auditing is for use when a user's activities are under investigation. To be sure of capturing all activity during those periods when session auditing is in use, it needs to be in operation for the whole time the DBMS is running.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure session auditing is initiated upon startup. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000095-DB-000039

**Group ID:** `V-238515`

### Rule: The Cassandra database must produce audit records containing sufficient information to establish what type of events occurred.

**Rule ID:** `SV-238515r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit record content that may be necessary to satisfy the requirement of this policy includes, for example, time stamps, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly what actions were performed. This requires specific information regarding the event type an audit record is referring to. If event type information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure audit records containing sufficient information to establish what type of events occurred are produced. Navigate to and open /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml. Navigate to the <appender> node with the name="FILE" attribute. Navigate to <encoder> node. If the <pattern> node does not look like the expected result, this is a finding. Expected result: <pattern>%-5level [%thread] %date{ISO8601, UTC} %F:%L - %msg%n</pattern>

## Group: SRG-APP-000096-DB-000040

**Group ID:** `V-238516`

### Rule: The Cassandra database must produce audit records containing time stamps to establish when the events occurred.

**Rule ID:** `SV-238516r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events relating to an incident. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the date and time when events occurred. Associating the date and time with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly when specific actions were performed. This requires the date and time an audit record is referring to. If date and time information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server setting to ensure audit records containing time stamps to establish when the events occurred are produced. Navigate to and open /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml. Navigate to the <appender> node with the name="FILE" attribute. Navigate to <encoder> node. If the <pattern> node does not look like the expected result, this is a finding. Expected result: <pattern>%-5level [%thread] %date{ISO8601, UTC} %F:%L - %msg%n</pattern>

## Group: SRG-APP-000099-DB-000043

**Group ID:** `V-238517`

### Rule: The Cassandra database must produce audit records containing sufficient information to establish the outcome (success or failure) of the events.

**Rule ID:** `SV-238517r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure audit records containing sufficient information to establish the outcome (success or failure) of the events are produced. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000101-DB-000044

**Group ID:** `V-238518`

### Rule: The Cassandra database must include additional, more detailed, organization-defined information in the audit records for audit events identified by type, location, or subject.

**Rule ID:** `SV-238518r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. To support analysis, some types of events will need information to be logged that exceeds the basic requirements of event type, time stamps, location, source, outcome, and user identity. If additional information is not available, it could negatively impact forensic investigations into user actions or other malicious events. The organization must determine what additional information is required for complete analysis of the audited events. The additional information required is dependent on the type of information (e.g., sensitivity of the data and the environment within which it resides). At a minimum, the organization must employ either full-text recording of privileged commands or the individual identities of group users, or both. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Examples of detailed information the organization may require in audit records are full-text recording of privileged commands or the individual identities of group account users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure additional, more detailed, organization-defined information in the audit records for audit events identified by type, location, or subject are included. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-238519`

### Rule: The Cassandra database logs must be protected from unauthorized read access.

**Rule ID:** `SV-238519r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure logs are protected from unauthorized read access. At the command prompt, execute the following command: # ls -lL /storage/log/vcops/log/cassandra If any file does not have permissions of "0640", this is a finding.

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-238520`

### Rule: The Cassandra database logs must have the correct owner.

**Rule ID:** `SV-238520r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods that will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server to ensure logs have the correct owner. At the command prompt, execute the following command: # ls -lL /storage/log/vcops/log/cassandra If any file is not owned by "admin", this is a finding.

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-238521`

### Rule: The Cassandra database logs must have the correct group-owner.

**Rule ID:** `SV-238521r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files enjoy the proper file system permissions utilizing file system protections; restricting access; and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure logs have the correct group-owner. At the command prompt, execute the following command: # ls -lL /storage/log/vcops/log/cassandra If any file is not group-owned by "admin", this is a finding.

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-238522`

### Rule: The Cassandra database log configuration file must be protected from unauthorized read access.

**Rule ID:** `SV-238522r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure the log configuration file is protected from unauthorized read access. At the command prompt, execute the following command: # ls -l /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If the file does not have permissions of "0640", this is a finding.

## Group: SRG-APP-000122-DB-000203

**Group ID:** `V-238523`

### Rule: The Cassandra database log configuration file must have the correct owner.

**Rule ID:** `SV-238523r879580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure the log configuration file has the correct owner. At the command prompt, execute the following command: # ls -l /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If the file is not owned by "admin", this is a finding.

## Group: SRG-APP-000123-DB-000204

**Group ID:** `V-238524`

### Rule: The Cassandra database log configuration file must have the correct group-owner.

**Rule ID:** `SV-238524r879581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure the log configuration file has the correct group-owner. At the command prompt, execute the following command: # ls -l /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If the file is not group-owned by "admin", this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-238525`

### Rule: The Cassandra software, including configuration files, must be stored in dedicated directories, or direct-access storage device (DASD) pools, separate from the host OS and other applications.

**Rule ID:** `SV-238525r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server Configuration to ensure its software, including configuration files, is stored in dedicated directories, or direct-access storage device (DASD) pools, separate from the host OS and other applications. Run following commands from Cassandra host server console: "cd $VCOPS_BASE/Cassandra/<installed Cassandra release name (current example - apache-cassandra-2.1.8)> ls -l" If the Cassandra software, including configuration files, is not stored separate from the host OS and other applications, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-238526`

### Rule: Database objects (including but not limited to tables, indexes, storage, stored procedures, functions, triggers, links to software external to the DBMS, etc.) must be owned by database/DBMS principals authorized for ownership.

**Rule ID:** `SV-238526r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who utilizes the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. Conversely, if critical tables or other objects rely on unauthorized owner accounts, these objects may be lost when an account is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to identify accounts authorized to own database objects. Review accounts that own objects in the database(s). If any database objects are found to be owned by users not authorized to own database objects, this is a finding. Open cqlsh prompt in the Cassandra Server and type "LIST ALL PERMISSIONS;" command. Review the list of access privileges available. If all the objects are owned by superuser account (cassandra in default Cassandra Server configuration), this is not a finding. Otherwise, it is a finding.

## Group: VROM-CS-000110

**Group ID:** `V-238527`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to the DBMS, etc.) must be restricted to authorized users.

**Rule ID:** `SV-238527r655649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS were to allow any user to make changes to database structure or logic, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure the role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to the DBMS, etc.) are restricted to authorized users. At the command prompt, execute the following command: # find /usr/lib/vmware-vcops/cassandra -type f ! \( -user admin -o -user root \) If any files are listed that are not owned by either "admin" or "root", this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-238528`

### Rule: Unused Cassandra database components, software, and database objects must be removed.

**Rule ID:** `SV-238528r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server to ensure unused database components, software, and database objects are removed. Open console on server Cassandra DB is hosted on and run following command: "find / | grep "cassandra"". Review the list of files displayed. If no unused components or features are displayed, this is not a finding. Otherwise, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-238529`

### Rule: The Cassandra Server must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-238529r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain document containing the list of approved ports, protocols and services from https://disa.deps.mil/ext/cop/iase/ppsm/Pages/cal.aspx. Review the Cassandra Server database settings and local documentation for functions, ports, protocols, and services that are not approved. Open the console to the server Cassandra DB is hosted at and type: "find / | grep "cassandra.yaml"". Open cassandra.yaml and review "native_transport_port" parameter value. Run "netstat -ntl | grep <"native_transport_port" parameter value >" command from the console on the host. If protocol, port, and IP address Cassandra communicates on are not found in https://disa.deps.mil/ext/cop/iase/ppsm/Pages/cal.aspx, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-238530`

### Rule: The Cassandra Server must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-238530r879589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure organizational users are uniquely identified and authenticated when logging on/connecting to the system. Open "cqlsh" prompt in the Cassandra Server and type in "LIST USERS;" command. Review the list of accounts available against product documentation and determine if any shared accounts exist. If accounts are determined to be shared, determine if individuals are first individually authenticated. If individuals are not individually authenticated before using the shared account, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-238531`

### Rule: The Cassandra database must enforce the DoD standards for password complexity and lifetime.

**Rule ID:** `SV-238531r879601_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Native DBMS authentication may be used only when circumstances make it unavoidable. In such cases, the DoD standards for password complexity and lifetime must be implemented. The rules must be enforced using available configuration parameters or custom code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra database configuration to ensure the DoD standards for password complexity and lifetime are enforced. Review the DBMS settings relating to password complexity. Determine whether the following rules are enforced. If any are not, this is a finding. a. minimum of 15 characters, including at least one of each of the following character sets: - Upper-case - Lower-case - Numeric - Special characters (e.g., ~ ! @ # $ % ^ & * ( ) _ + = - ' [ ] / ? > <) b. Minimum number of characters changed from previous password: 50 percent of the minimum password length; that is, eight Review the DBMS settings relating to password lifetime. Determine whether the following rules are enforced. If any are not, this is a finding. c. Password lifetime limits: Minimum 24 hours, maximum 60 days d. Number of password changes before an old one may be reused: Minimum of five

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-238532`

### Rule: The Cassandra database log configuration file must set internode encryption.

**Rule ID:** `SV-238532r879609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. DBMS passwords sent in clear text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings for encrypting passwords in transit across the network. If passwords are not encrypted, this is a finding. At the command prompt, execute the following command: # grep '^\s*internode_encryption:' /usr/lib/vmware-vcops/user/conf/cassandra/cassandra.yaml If the line below is returned, this is a finding: internode_encryption: all

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-238533`

### Rule: The Cassandra Server must isolate security functions from non-security functions.

**Rule ID:** `SV-238533r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database Management Systems typically separate security functionality from non-security functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and non-security functionality are commingled, users who have access to non-security functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure objects or code implementing security functionality are located in a separate security domain, such as a separate database or schema created specifically for security functionality. If security-related database objects or code are not kept separate, this is a finding. Open "cqlsh" prompt of Cassandra Server and run "LIST ALL PERMISSIONS" command from it. Review username resource and permissions columns. If for any of the objects under system, system_auth, or system_traces schemas privileges are given to any other users than a superuser (cassandra in default configuration), this is a finding.

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-238534`

### Rule: Access to database files must be limited to relevant processes and to authorized, administrative users.

**Rule ID:** `SV-238534r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Permitting only DBMS processes and authorized, administrative users to have access to the files where the database resides helps ensure that those files are not shared inappropriately and are not open to backdoor access and manipulation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions granted to users by the operating system/file system on the database files, database log files, and database backup files. At the command prompt, execute the following command: # find /storage/db/vcops/cassandra/data -type f ! \( -user admin -o -user root \) If any files are listed that are not owned by either "admin" or "root", this is a finding.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-238535`

### Rule: The Cassandra Server must reveal detailed error messages only to the ISSO, ISSM, SA, and DBA.

**Rule ID:** `SV-238535r879656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Some default DBMS error messages can contain information that could aid an attacker in, among others things, identifying the database type, host address, or state of the database. Custom errors may contain sensitive customer information. It is important that detailed error messages be visible only to those who are authorized to view them; that general users receive only generalized acknowledgment that errors have occurred; and that these generalized messages appear only when relevant to the user's task. For example, a message along the lines of, "An error has occurred. Unable to save your changes. If this problem persists, please contact your help desk" would be relevant. A message such as "Warning: your transaction generated a large number of page splits" would likely not be relevant. Administrative users authorized to review detailed error messages typically are the ISSO, ISSM, SA and DBA. Other individuals or roles may be specified according to organization-specific needs, with DBA approval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server to ensure detailed error messages are only revealed to the ISSO, ISSM, SA and DBA. At the command prompt, execute the following command: # ls -l /usr/lib/vmware-vcops/user/conf/cassandra If any file is not owned by "admin", this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-238536`

### Rule: The Cassandra Server must utilize centralized management of the content captured in audit records generated by all components of the system.

**Rule ID:** `SV-238536r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure centralized management of the content captured in audit records generated by all components of the system are utilized. At the command prompt, execute the following command: # grep SyslogAppender /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000374-DB-000322

**Group ID:** `V-238537`

### Rule: The Cassandra Server must record time stamps, in audit records and application data that can be mapped to Coordinated Universal Time (UTC, formerly GMT).

**Rule ID:** `SV-238537r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the DBMS must include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. Some DBMS products offer a data type called TIMESTAMP that is not a representation of date and time. Rather, it is a database state counter and does not correspond to calendar and clock time. This requirement does not refer to that meaning of TIMESTAMP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure time stamps, in audit records and application data that can be mapped to Coordinated Universal Time (UTC, formerly GMT) are recorded. Navigate to and open /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml. Navigate to the <appender> node with the name="FILE" attribute. Navigate to <encoder> node. If the <pattern> node does not look like the expected result, this is a finding. Expected result: <pattern>%-5level [%thread] %date{ISO8601, UTC} %F:%L - %msg%n</pattern>

## Group: SRG-APP-000375-DB-000323

**Group ID:** `V-238538`

### Rule: The Cassandra Server must generate time stamps, for audit records and application data, with a minimum granularity of one second.

**Rule ID:** `SV-238538r879748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the DBMS must include date and time. Granularity of time measurements refers to the precision available in time stamp values. Granularity coarser than one second is not sufficient for audit trail purposes. Time stamp values are typically presented with three or more decimal places of seconds; however, the actual granularity may be coarser than the apparent precision. For example, SQL Server's GETDATE()/CURRENT_TMESTAMP values are presented to three decimal places, but the granularity is not one millisecond: it is about 1/300 of a second. Some DBMS products offer a data type called TIMESTAMP that is not a representation of date and time. Rather, it is a database state counter and does not correspond to calendar and clock time. This requirement does not refer to that meaning of TIMESTAMP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server settings to ensure time stamps, for audit records and application data, with a minimum granularity of one second are generated. Navigate to and open /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml. Navigate to the <appender> node with the name="FILE" attribute. Navigate to <encoder> node. If the <pattern> node does not look like the expected result, this is a finding. Expected result: <pattern>%-5level [%thread] %date{ISO8601, UTC} %F:%L - %msg%n</pattern>

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-238539`

### Rule: The Cassandra database must protect the truststore file.

**Rule ID:** `SV-238539r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure the truststore file is protected. At the command prompt, execute the following command: # ls -l /storage/vcops/user/conf/ssl/tcserver.truststore If the file permissions are not "0640", this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-238540`

### Rule: The Cassandra Server must disable network functions, ports, protocols, and services deemed by the organization to be nonsecure, in accord with the Ports, Protocols, and Services Management (PPSM) guidance.

**Rule ID:** `SV-238540r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure network functions, ports, protocols, and services exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server to ensure network functions, ports, protocols, and services deemed by the organization to be nonsecure, in accordance with the Ports, Protocols, and Services Management (PPSM) guidance are disabled. Open the console to the server that Cassandra DB is hosted at and type: "find / | grep "cassandra.yaml"". Open "cassandra.yaml" file and review "start_rpc", "start_native_transport", and "native_transport_port" parameters values. If "start_rpc" is not set to "false" and "start_native_transport" is not set to "true", this is a finding. Run following command from the console of server, hosting Cassandra: "netstat -ntl | grep <native_transport_port > parameter value". Review output of this command record for the protocol and port Cassandra listens at. Obtain the document containing the list of approved ports, protocols, and services from https://disa.deps.mil/ext/cop/iase/ppsm/Pages/cal.aspx. If protocol and port Cassandra listens at are not approved, this is a finding.

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-238541`

### Rule: When invalid inputs are received, the Cassandra Server must behave in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-238541r879818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server to ensure that it behaves in a predictable and documented manner that reflects organizational and system objectives when invalid inputs are received. Open the "cqlsh" prompt in the Cassandra Server and type "DESCRIBE KEYSPACES;". Type "DESCRIBE <keyspace name>" for all the keyspace names that have been displayed as output for the first command. Review keyspaces content. Open the console to the server that Cassandra DB is hosted at and type: "find / | grep "logback.xml"". Open "logback.xml" file and review "level" parameter value under <root />. If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-238542`

### Rule: Security-relevant software updates to the Cassandra Server must be installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-238542r879827_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure security-relevant software updates are installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). Run "find / | grep "cassandra-"" from console and review all the Cassandra DB related packages currently installed on the host. Check at the http://cassandra.apache.org/download/ for the latest updates and patches available. Check product documentation for the time period updates have to be installed on the host. If there is an update that has to be installed, but is not displayed in the list of Cassandra DB related packages currently installed on the host, this is a finding.

## Group: SRG-APP-000492-DB-000332

**Group ID:** `V-238543`

### Rule: The Cassandra Server must be able to generate audit records when security objects are accessed.

**Rule ID:** `SV-238543r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when security objects are accessed. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000492-DB-000333

**Group ID:** `V-238544`

### Rule: The Cassandra Server must generate audit records when unsuccessful attempts to access security objects occur.

**Rule ID:** `SV-238544r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when unsuccessful attempts to access security objects occur. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000495-DB-000326

**Group ID:** `V-238545`

### Rule: The Cassandra Server must generate audit records when privileges/permissions are added.

**Rule ID:** `SV-238545r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, adding permissions is typically done via the GRANT command, or, in the negative, the DENY command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when privileges/permissions are added. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000495-DB-000327

**Group ID:** `V-238546`

### Rule: The Cassandra Server must generate audit records when unsuccessful attempts to add privileges/permissions occur.

**Rule ID:** `SV-238546r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, adding permissions is typically done via the GRANT command, or, in the negative, the DENY command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when unsuccessful attempts to add privileges/permissions occur. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000495-DB-000328

**Group ID:** `V-238547`

### Rule: The Cassandra Server must generate audit records when privileges/permissions are modified.

**Rule ID:** `SV-238547r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, modifying permissions is typically done via the GRANT, REVOKE, and DENY commands.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when privileges/permissions are modified. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000495-DB-000329

**Group ID:** `V-238548`

### Rule: The Cassandra Server must generate audit records when unsuccessful attempts to modify privileges/permissions occur.

**Rule ID:** `SV-238548r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, modifying permissions is typically done via the GRANT, REVOKE, and DENY commands. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when unsuccessful attempts to modify privileges/permissions occur. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000496-DB-000334

**Group ID:** `V-238549`

### Rule: The Cassandra Server must generate audit records when security objects are modified.

**Rule ID:** `SV-238549r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when security objects are modified. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000496-DB-000335

**Group ID:** `V-238550`

### Rule: The Cassandra Server must generate audit records when unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-238550r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when unsuccessful attempts to modify security objects occur. Open console to the server, Cassandra DB is hosted at, and type: "find / | grep "logback.xml"". Open "logback.xml" file and review "level" parameter value under <root />. If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000499-DB-000330

**Group ID:** `V-238551`

### Rule: The Cassandra Server must generate audit records when privileges/permissions are deleted.

**Rule ID:** `SV-238551r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, deleting permissions is typically done via the REVOKE or DENY command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when privileges/permissions are deleted. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000499-DB-000331

**Group ID:** `V-238552`

### Rule: The Cassandra Server must generate audit records when unsuccessful attempts to delete privileges/permissions occur.

**Rule ID:** `SV-238552r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, deleting permissions is typically done via the REVOKE or DENY command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when unsuccessful attempts to delete privileges/permissions occur. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000501-DB-000336

**Group ID:** `V-238553`

### Rule: The Cassandra Server must generate audit records when security objects are deleted.

**Rule ID:** `SV-238553r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an event occurs, it must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when security objects are deleted. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000501-DB-000337

**Group ID:** `V-238554`

### Rule: The Cassandra Server must generate audit records when unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-238554r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an action is attempted, it must be logged. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when unsuccessful attempts to delete security objects occur. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000502-DB-000348

**Group ID:** `V-238555`

### Rule: The Cassandra Server must generate audit records when categories of information (e.g., classification levels/security levels) are deleted.

**Rule ID:** `SV-238555r879873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when categories of information (e.g., classification levels/security levels) are deleted. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000504-DB-000354

**Group ID:** `V-238556`

### Rule: The Cassandra Server must generate audit records for all privileged activities or other system-level access.

**Rule ID:** `SV-238556r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples in SQL include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, audit logging may be achieved by means of DBMS auditing features, database triggers, other mechanisms, or a combination of these. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated for all privileged activities or other system-level access. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000504-DB-000355

**Group ID:** `V-238557`

### Rule: The Cassandra Server must generate audit records when unsuccessful attempts to execute privileged activities or other system-level access occur.

**Rule ID:** `SV-238557r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when unsuccessful attempts to execute privileged activities or other system-level access occur. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000507-DB-000356

**Group ID:** `V-238558`

### Rule: The Cassandra Server must be able to generate audit records when successful accesses to objects occur.

**Rule ID:** `SV-238558r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when successful accesses to objects occur. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000507-DB-000357

**Group ID:** `V-238559`

### Rule: The Cassandra Server must generate audit records when unsuccessful accesses to objects occur.

**Rule ID:** `SV-238559r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure audit records are generated when unsuccessful accesses to objects occur. At the command prompt, execute the following command: # grep '<root' /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-238560`

### Rule: The Cassandra Server must off-load audit data to a separate log management facility; this must be continuous and in near real time for systems with a network connection to the storage facility and weekly or more often for stand-alone systems.

**Rule ID:** `SV-238560r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server to ensure audit data is off-loaded to a separate log management facility. At the command prompt, execute the following command: # grep SyslogAppender /usr/lib/vmware-vcops/user/conf/cassandra/logback.xml If level is not set to "ALL", this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-238561`

### Rule: The DBMS must be configured in accordance with the security configuration settings based on DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs.

**Rule ID:** `SV-238561r879887_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring the DBMS to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. In addition to this SRG, sources of guidance on security and information assurance exist. These include NSA configuration guides, CTOs, DTMs, and IAVMs. The DBMS must be configured in compliance with guidance from all such relevant sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra documentation and configuration to determine if the server is configured in accordance with DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs. Obtain supporting documentation from the ISSO. Verify that this Security Technical Implementation Guide (STIG) is the most current STIG available for Cassandra on vROps. Assess all of the organization's vROps installations to ensure that they are fully compliant with the most current Cassandra STIG. If the Cassandra configuration is not compliant with the most current Cassandra STIG, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-238562`

### Rule: The Cassandra Server must use NIST FIPS 140-2 validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-238562r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the DBMS. Applications, including DBMSs, utilizing cryptography are required to use approved NIST FIPS 140-2 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The security functions validated as part of FIPS 140-2 for cryptographic modules are described in FIPS 140-2 Annex A. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to ensure NIST FIPS 140-2 validated cryptographic modules are used for cryptographic operations. Review the Apache2 configuration by opening the /etc/apache2/ssl-global.conf file. Search for the <IfModule mod_ssl.c> line and ensure the SSLFIPS directive is below it. If the SSLFIPS directive is not under the <IfModule mod_ssl.c> line, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-238563`

### Rule: The Cassandra Server must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-238563r879642_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server configuration to protect the confidentiality and integrity of all information at rest. Inspect the server configuration to ensure a full disk encryption solution has been implemented. If the disk is unencrypted, this is a finding.

## Group: SRG-APP-000429-DB-000387

**Group ID:** `V-238564`

### Rule: The Cassandra Server must implement cryptographic mechanisms preventing the unauthorized disclosure of information at rest.

**Rule ID:** `SV-238564r879800_rule`
**Severity:** high

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cassandra Server to ensure cryptographic mechanisms are implemented preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components. Inspect the server configuration to ensure a full disk encryption solution has been implemented. If the disk is unencrypted, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-258449`

### Rule: The version of vRealize Operations Manager Cassandra running on the system must be a supported version.

**Rule ID:** `SV-258449r928866_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Operations Manager Cassandra is no longer supported by the vendor. If the system is running vRealize Operations Manager Cassandra, this is a finding.

