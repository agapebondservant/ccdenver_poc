# STIG Benchmark: VMW vRealize Automation 7.x PostgreSQL Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-240276`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240276r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the DBMS (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the DBMS will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities, or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Organizations may define additional events requiring continuous or ad hoc auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-240277`

### Rule: The vRA PostgreSQL configuration file must not be accessible by unauthorized users.

**Rule ID:** `SV-240277r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, enter the following command: # ls -l /storage/db/pgdata/*conf* If the permissions on any of the listed files are not "600", this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-240278`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240278r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000092-DB-000208

**Group ID:** `V-240279`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240279r879562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session auditing is for use when a user's activities are under investigation. To be sure of capturing all activity during those periods when session auditing is in use, it needs to be in operation for the whole time the DBMS is running.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000095-DB-000039

**Group ID:** `V-240280`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240280r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit record content that may be necessary to satisfy the requirement of this policy includes, for example, time stamps, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly what actions were performed. This requires specific information regarding the event type an audit record is referring to. If event type information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000096-DB-000040

**Group ID:** `V-240281`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240281r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events relating to an incident. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the date and time when events occurred. Associating the date and time with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly when specific actions were performed. This requires the date and time an audit record is referring to. If date and time information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000097-DB-000041

**Group ID:** `V-240282`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240282r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events relating to an incident. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as application components, modules, session identifiers, filenames, host names, and functionality. Associating information about where the event occurred within the application provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000098-DB-000042

**Group ID:** `V-240283`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240283r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events relating to an incident. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as application components, modules, session identifiers, filenames, host names, and functionality. In addition to logging where events occur within the application, the application must also produce audit records that identify the application itself as the source of the event. Associating information about the source of the event within the application provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000099-DB-000043

**Group ID:** `V-240284`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240284r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000100-DB-000201

**Group ID:** `V-240285`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240285r879568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event. Identifiers (if authenticated or otherwise known) include, but are not limited to, user database tables, primary key values, user names, or process identifiers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000101-DB-000044

**Group ID:** `V-240286`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240286r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. To support analysis, some types of events will need information to be logged that exceeds the basic requirements of event type, time stamps, location, source, outcome, and user identity. If additional information is not available, it could negatively impact forensic investigations into user actions or other malicious events. The organization must determine what additional information is required for complete analysis of the audited events. The additional information required is dependent on the type of information (e.g., sensitivity of the data and the environment within which it resides). At a minimum, the organization must employ either full-text recording of privileged commands or the individual identities of group users, or both. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Examples of detailed information the organization may require in audit records are full-text recording of privileged commands or the individual identities of group account users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000109-DB-000321

**Group ID:** `V-240287`

### Rule: vRA PostgreSQL database must have log_truncate_on_rotation enabled.

**Rule ID:** `SV-240287r879571_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical that when the DBMS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, approved actions in response to an audit failure are as follows: (i) If the failure was caused by the lack of audit record storage capacity, the DBMS must continue generating audit records, if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. (ii) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the DBMS must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server. Systems where availability is paramount will most likely be MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. In any case, sufficient auditing resources must be allocated to avoid audit data loss in all but the most extreme situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_truncate_on_rotation\b' /storage/db/pgdata/postgresql.conf If "log_truncate_on_rotation" is not set to "on", this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-240288`

### Rule: The vRA PostgreSQL database must have the correct permissions on the log files.

**Rule ID:** `SV-240288r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, enter the following command: # ls -l /storage/db/pgdata/pg_log/*.log If the permissions on any log files are not "600", this is a finding.

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-240289`

### Rule: The vRA PostgreSQL database must have the correct ownership on the log files.

**Rule ID:** `SV-240289r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods that will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, enter the following command: # ls -l /storage/db/pgdata/pg_log/*.log If the owner of any log files are not "postgres:users", this is a finding.

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-240290`

### Rule: The vRA PostgreSQL database must have the correct group-ownership on the log files.

**Rule ID:** `SV-240290r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files enjoy the proper file system permissions utilizing file system protections; restricting access; and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, enter the following command: # ls -l /storage/db/pgdata/pg_log/*.log If the group-owner of any log files are not "postgres:users", this is a finding.

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-240291`

### Rule: The vRA PostgreSQL configuration files must have the correct permissions.

**Rule ID:** `SV-240291r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, enter the following command: # ls -l /storage/db/pgdata/*conf* If the permissions on any of the listed files are not "600", this is a finding.

## Group: SRG-APP-000122-DB-000203

**Group ID:** `V-240292`

### Rule: The vRA PostgreSQL configuration files must have the correct ownership.

**Rule ID:** `SV-240292r879580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, enter the following command: # ls -l /storage/db/pgdata/*conf* If the owner of any configuration file is not "postgres:users", this is a finding.

## Group: SRG-APP-000123-DB-000204

**Group ID:** `V-240293`

### Rule: The vRA PostgreSQL configuration files must have the correct group-ownership.

**Rule ID:** `SV-240293r879581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, enter the following command: # ls -l /storage/db/pgdata/*conf* If the group-owner of any configuration file is not "postgres:users", this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-240294`

### Rule: vRA PostgreSQL database objects must only be accessible to the postgres account.

**Rule ID:** `SV-240294r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who utilizes the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. Conversely, if critical tables or other objects rely on unauthorized owner accounts, these objects may be lost when an account is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -c "\dp;" Review the Access Privileges column.   If any tables have permissions to users other than "postgres", this is a finding. 

## Group: VRAU-PG-000140

**Group ID:** `V-240295`

### Rule: The vRA PostgreSQL database must limit modify privileges to authorized accounts.

**Rule ID:** `SV-240295r668729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -c "\du;" If the accounts other than "postgres" and "vcac_replication" have "create" privileges, this is a finding.

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-240296`

### Rule: The vRA PostgreSQL database must not contain sample data.

**Rule ID:** `SV-240296r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plugins not related to requirements or providing a wide array of functionality, not required for every mission, that cannot be disabled. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the DBMS and host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -c "SELECT datname FROM pg_database WHERE datistemplate = false;" If the output is not the following lines, this is a finding. datname ---------- postgres vcac (2 rows)

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-240297`

### Rule: The vRA PostgreSQL database must be limited to authorized accounts.

**Rule ID:** `SV-240297r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command to enter the psql prompt: # cat /storage/db/pgdata/pg_hba.conf If any rows have "trust" specified for the "METHOD" column, this is a finding.

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-240298`

### Rule: The vRA PostgreSQL database must use md5 for authentication.

**Rule ID:** `SV-240298r879608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, database passwords stored in clear text, using reversible encryption, or using unsalted hashes would be vulnerable to unauthorized disclosure. Database passwords must always be in the form of one-way, salted hashes when stored internally or externally to the DBMS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command to enter the psql prompt: # cat /storage/db/pgdata/pg_hba.conf If any rows have "trust" specified for the "METHOD" column, this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-240299`

### Rule: The vRA PostgreSQL database must be configured to use ssl.

**Rule ID:** `SV-240299r879609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. DBMS passwords sent in clear text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*ssl\b' /storage/db/pgdata/postgresql.conf If "ssl" is not "on", this is a finding.

## Group: SRG-APP-000226-DB-000147

**Group ID:** `V-240300`

### Rule: The vRA PostgreSQL database must complete writing log entries prior to returning results.

**Rule ID:** `SV-240300r879641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving information system state information helps to facilitate system restart and return to the operational mode of the organization with less disruption of mission/business processes. Since it is usually not possible to test this capability in a production environment, systems should either be validated in a testing environment or prior to installation. This requirement is usually a function of the design of the IDPS component. Compliance can be verified by acceptance/validation processes or vendor attestation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -c "SELECT name,setting FROM pg_settings WHERE name IN ('fsync','full_page_writes','synchronous_commit');" If "fsync", "full_page_writes", and "synchronous_commit" are not all "on", this is a finding. The command will return the following lines: name | setting ---------------------------+--------- fsync | on full_page_writes | on synchronous_commit | on (3 rows)

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-240301`

### Rule: The vRA PostgreSQL must not allow access to unauthorized accounts.

**Rule ID:** `SV-240301r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database Management Systems typically separate security functionality from non-security functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and non-security functionality are commingled, users who have access to non-security functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -c "\dp .*.;" Review the Access Privilege column for all Schemas listed as "information_schema" and "pg_catalog". If access privilege is granted to any users other than "postgres", this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-240302`

### Rule: Data from the vRA PostgreSQL database must be protected from unauthorized transfer.

**Rule ID:** `SV-240302r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the site data-transfer policy from the ISSO. Review the policies and procedures used to ensure that all vRA data are being protected from unauthorized and unintended information transformation in accordance with site policy. If the site data-transfer policy is not followed, this is a finding.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-240303`

### Rule: The vRA PostgreSQL error file must be protected from unauthorized access.

**Rule ID:** `SV-240303r879656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Some default DBMS error messages can contain information that could aid an attacker in, among others things, identifying the database type, host address, or state of the database. Custom errors may contain sensitive customer information. It is important that detailed error messages be visible only to those who are authorized to view them; that general users receive only generalized acknowledgment that errors have occurred; and that these generalized messages appear only when relevant to the user's task. For example, a message along the lines of, "An error has occurred. Unable to save your changes. If this problem persists, please contact your help desk" would be relevant. A message such as "Warning: your transaction generated a large number of page splits" would likely not be relevant. Administrative users authorized to review detailed error messages typically are the ISSO, ISSM, SA and DBA. Other individuals or roles may be specified according to organization-specific needs, with DBA approval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # ls -l /storage/db/pgdata/serverlog If the file permissions are more permissive than "600", this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-240304`

### Rule: The vRA PostgreSQL database must have log collection enabled.

**Rule ID:** `SV-240304r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*logging_collector\b' /storage/db/pgdata/postgresql.conf If "logging_collector" is not "on", this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-240305`

### Rule: The vRA PostgreSQL database must be configured to use a syslog facility.

**Rule ID:** `SV-240305r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so, under normal conditions, the audit space allocated to the DBMS on its own server will not be an issue. However, space will still be required on the DBMS server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*logging_collector\b' /storage/db/pgdata/postgresql.conf If "logging_collector" is not "on", this is a finding.

## Group: VRAU-PG-000295

**Group ID:** `V-240306`

### Rule: The vRA PostgreSQL database must be configured to use a syslog facility.

**Rule ID:** `SV-240306r668762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*logging_collector\b' /storage/db/pgdata/postgresql.conf If "logging_collector" is not "on", this is a finding.

## Group: SRG-APP-000374-DB-000322

**Group ID:** `V-240307`

### Rule: The vRA PostgreSQL database must use UTC for log timestamps.

**Rule ID:** `SV-240307r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the DBMS must include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. Some DBMS products offer a data type called TIMESTAMP that is not a representation of date and time. Rather, it is a database state counter and does not correspond to calendar and clock time. This requirement does not refer to that meaning of TIMESTAMP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_timezone\b' /storage/db/pgdata/postgresql.conf If "log_timezone" is not "utc", this is a finding.

## Group: SRG-APP-000375-DB-000323

**Group ID:** `V-240308`

### Rule: vRA PostgreSQL database log file data must contain required data elements.

**Rule ID:** `SV-240308r879748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the DBMS must include date and time. Granularity of time measurements refers to the precision available in time stamp values. Granularity coarser than one second is not sufficient for audit trail purposes. Time stamp values are typically presented with three or more decimal places of seconds; however, the actual granularity may be coarser than the apparent precision. For example, SQL Server's GETDATE()/CURRENT_TMESTAMP values are presented to three decimal places, but the granularity is not one millisecond: it is about 1/300 of a second. Some DBMS products offer a data type called TIMESTAMP that is not a representation of date and time. Rather, it is a database state counter and does not correspond to calendar and clock time. This requirement does not refer to that meaning of TIMESTAMP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_line_prefix\b' /storage/db/pgdata/postgresql.conf If "log_line_prefix" is not set to "%m %d %u %r %p %l %c", this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-240309`

### Rule: The DBMS must enforce access restrictions associated with changes to the configuration of the DBMS or database(s).

**Rule ID:** `SV-240309r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, enter the following command: # ls -l /storage/db/pgdata/*conf* If the permissions on any of the listed files are not "600", this is a finding.

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-240310`

### Rule: vRA PostgreSQL database must be configured to validate character encoding to UTF-8.

**Rule ID:** `SV-240310r879818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*client_encoding\b' /storage/db/pgdata/postgresql.conf If "client_encoding" is not "UTF8", this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-240311`

### Rule: The vRA PostgreSQL database security updates and patches must be installed in a timely manner in accordance with site policy.

**Rule ID:** `SV-240311r879827_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g. IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review the policies and procedures used to ensure that all security-related upgrades are being installed within the configured time period directed by an authoritative source. If all security-related upgrades are not being installed within the configured time period directed by an authoritative source, this is a finding.

## Group: SRG-APP-000492-DB-000332

**Group ID:** `V-240312`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240312r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000492-DB-000333

**Group ID:** `V-240313`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240313r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000495-DB-000326

**Group ID:** `V-240314`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240314r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, adding permissions is typically done via the GRANT command, or, in the negative, the DENY command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000495-DB-000327

**Group ID:** `V-240315`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240315r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, adding permissions is typically done via the GRANT command, or, in the negative, the DENY command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000495-DB-000328

**Group ID:** `V-240316`

### Rule: The DBMS must generate audit records when privileges/permissions are modified.

**Rule ID:** `SV-240316r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, modifying permissions is typically done via the GRANT, REVOKE, and DENY commands.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000495-DB-000329

**Group ID:** `V-240317`

### Rule: The DBMS must generate audit records when unsuccessful attempts to modify privileges/permissions occur.

**Rule ID:** `SV-240317r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In PostgreSQL environment, modifying permissions is typically done via the GRANT and REVOKE commands. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000496-DB-000334

**Group ID:** `V-240318`

### Rule: The DBMS must generate audit records when security objects are modified.

**Rule ID:** `SV-240318r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000496-DB-000335

**Group ID:** `V-240319`

### Rule: The DBMS must generate audit records when unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-240319r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not all, this is a finding.

## Group: SRG-APP-000499-DB-000330

**Group ID:** `V-240320`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240320r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, deleting permissions is typically done via the REVOKE or DENY command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000499-DB-000331

**Group ID:** `V-240321`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240321r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, deleting permissions is typically done via the REVOKE or DENY command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement is not all", this is a finding.

## Group: SRG-APP-000501-DB-000336

**Group ID:** `V-240322`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240322r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an event occurs, it must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not all, this is a finding.

## Group: SRG-APP-000501-DB-000337

**Group ID:** `V-240323`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240323r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an action is attempted, it must be logged. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement is not all", this is a finding.

## Group: SRG-APP-000502-DB-000348

**Group ID:** `V-240324`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240324r879873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000503-DB-000350

**Group ID:** `V-240325`

### Rule: The vRA PostgreSQL database must set log_connections to on.

**Rule ID:** `SV-240325r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who/what (a user or other principal) logs on to the DBMS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_connections\b' /storage/db/pgdata/postgresql.conf If log_connections is not on, this is a finding.

## Group: SRG-APP-000503-DB-000351

**Group ID:** `V-240326`

### Rule: The vRA PostgreSQL database must set the log_min_messages to warning.

**Rule ID:** `SV-240326r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track failed attempts to log on to the DBMS. While positive identification may not be possible in a case of failed authentication, as much information as possible about the incident must be captured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_min_messages\b' /storage/db/pgdata/postgresql.conf If "log_min_messages" is not "warning", this is a finding.

## Group: SRG-APP-000504-DB-000354

**Group ID:** `V-240327`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240327r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples in SQL include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, audit logging may be achieved by means of DBMS auditing features, database triggers, other mechanisms, or a combination of these. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000504-DB-000355

**Group ID:** `V-240328`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240328r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000505-DB-000352

**Group ID:** `V-240329`

### Rule: The vRA PostgreSQL database must set log_connections to on.

**Rule ID:** `SV-240329r879876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to know how long a user's (or other principal's) connection to the DBMS lasts. This can be achieved by recording disconnections, in addition to logons/connections, in the audit logs. Disconnection may be initiated by the user or forced by the system (as in a timeout) or result from a system or network failure. To the greatest extent possible, all disconnections must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_connections\b' /storage/db/pgdata/postgresql.conf If "log_connections" is not "on", this is a finding.

## Group: SRG-APP-000506-DB-000353

**Group ID:** `V-240330`

### Rule: The vRA PostgreSQL database must set log_connections to on.

**Rule ID:** `SV-240330r879877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who logs on to the DBMS. Concurrent connections by the same user from multiple workstations may be valid use of the system; or such connections may be due to improper circumvention of the requirement to use the CAC for authentication; or they may indicate unauthorized account sharing; or they may be because an account has been compromised. (If the fact of multiple, concurrent logons by a given user can be reliably reconstructed from the log entries for other events (logons/connections; voluntary and involuntary disconnections), then it is not mandatory to create additional log entries specifically for this.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_connections\b' /storage/db/pgdata/postgresql.conf If "log_connections" is not "on", this is a finding.

## Group: SRG-APP-000507-DB-000356

**Group ID:** `V-240331`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240331r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000507-DB-000357

**Group ID:** `V-240332`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240332r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000508-DB-000358

**Group ID:** `V-240333`

### Rule: The vRA PostgreSQL database must set the log_statement to all.

**Rule ID:** `SV-240333r879879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In this context, direct access is any query, command, or call to the DBMS that comes from any source other than the application(s) that it supports. Examples would be the command line or a database management utility program. The intent is to capture all activity from administrative and non-standard sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*log_statement\b' /storage/db/pgdata/postgresql.conf If "log_statement" is not "all", this is a finding.

## Group: SRG-APP-000514-DB-000381

**Group ID:** `V-240334`

### Rule: The vRA PostgreSQL database must use FIPS 140-2 ciphers.

**Rule ID:** `SV-240334r879885_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. For detailed information, refer to NIST FIPS Publication 140-2, Security Requirements For Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*ssl_ciphers\b' /storage/db/pgdata/postgresql.conf If "ssl_ciphers" is not "FIPS: +3DES:!aNULL", this is a finding.

## Group: SRG-APP-000514-DB-000382

**Group ID:** `V-240335`

### Rule: The vRA PostgreSQL database must use FIPS 140-2 ciphers.

**Rule ID:** `SV-240335r879885_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. For detailed information, refer to NIST FIPS Publication 140-2, Security Requirements For Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*ssl_ciphers\b' /storage/db/pgdata/postgresql.conf If "ssl_ciphers" is not "FIPS: +3DES:!aNULL", this is a finding.

## Group: SRG-APP-000514-DB-000383

**Group ID:** `V-240336`

### Rule: The vRA PostgreSQL database must use FIPS 140-2 ciphers.

**Rule ID:** `SV-240336r879885_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. For detailed information, refer to NIST FIPS Publication 140-2, Security Requirements For Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*ssl_ciphers\b' /storage/db/pgdata/postgresql.conf If "ssl_ciphers" is not "FIPS: +3DES:!aNULL", this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-240337`

### Rule: The vRA PostgreSQL database must be configured to use a syslog facility.

**Rule ID:** `SV-240337r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*syslog_facility\b' /storage/db/pgdata/postgresql.conf If "syslog_facility" is not "local0", this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-240338`

### Rule: vRA PostgreSQL must have the latest approved security-relevant software updates installed.

**Rule ID:** `SV-240338r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the DBMS to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. In addition to this SRG, sources of guidance on security and information assurance exist. These include NSA configuration guides, CTOs, DTMs, and IAVMs. The DBMS must be configured in compliance with guidance from all such relevant sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Verify that this Security Technical Implementation Guide (STIG) is the most current STIG available for PostgreSQL on vRA Assess all of the organization's vRA installations to ensure that they are fully compliant with the most current PostgreSQL STIG. If the PostgreSQL configuration is not compliant with the most current PostgreSQL STIG, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-240339`

### Rule: The DBMS must use NIST FIPS 140-2 validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-240339r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the DBMS. Applications, including DBMSs, utilizing cryptography are required to use approved NIST FIPS 140-2 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The security functions validated as part of FIPS 140-2 for cryptographic modules are described in FIPS 140-2 Annex A. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*ssl_ciphers\b' /storage/db/pgdata/postgresql.conf If "ssl_ciphers" is not "FIPS: +3DES:!aNULL", this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-240340`

### Rule: vRA Postgres must be configured to use the correct port.

**Rule ID:** `SV-240340r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*port\b' /storage/db/pgdata/postgresql.conf If the port is set to "5432", this is NOT a finding. If the port is not set to "5432" and if the ISSO does not have documentation of an approved variance for using a non-standard port, this is a finding.

## Group: SRG-APP-000356-DB-000315

**Group ID:** `V-240341`

### Rule: The vRA PostgreSQL database must have log collection enabled.

**Rule ID:** `SV-240341r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the configuration of the DBMS's auditing is spread across multiple locations in the database management software, or across multiple commands, only loosely related, it is harder to use and takes longer to reconfigure in response to events. The DBMS must provide a unified tool for audit configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*logging_collector\b' /storage/db/pgdata/postgresql.conf If "logging_collector" is not "on", this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-240342`

### Rule: vRA Postgres must be configured to use the correct port.

**Rule ID:** `SV-240342r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure network functions, ports, protocols, and services exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*port\b' /storage/db/pgdata/postgresql.conf If the port is set to "5432", this is NOT a finding. If the port is not set to "5432" and if the ISSO does not have documentation of an approved variance for using a non-standard port, this is a finding.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-240343`

### Rule: vRA PostgreSQL must limit the number of connections.

**Rule ID:** `SV-240343r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions utilizing a DBMS. Unlimited concurrent connections to the DBMS could allow a successful Denial of Service (DoS) attack by exhausting connection resources; and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. This requirement addresses concurrent session control for a single account. It does not address concurrent sessions by a single user via multiple system accounts; and it does not deal with the total number of sessions across all accounts. The capability to limit the number of concurrent sessions per user must be configured in or added to the DBMS (for example, by use of a logon trigger), when this is technically feasible. Note that it is not sufficient to limit sessions via a web server or application server alone, because legitimate users and adversaries can potentially connect to the DBMS by other means. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to consider the work requirements of the various types of users. For example, 2 might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session. (Sessions may also be referred to as connections or logons, which for the purposes of this requirement are synonyms.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: # grep '^\s*max_connections\b' /storage/db/pgdata/postgresql.conf If "max_connections" is not "210", this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-258453`

### Rule: The version of vRealize Automation 7.x PostgreSQL running on the system must be a supported version.

**Rule ID:** `SV-258453r928885_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Automation 7.x PostgreSQL is no longer supported by the vendor. If the system is running vRealize Automation 7.x PostgreSQL, this is a finding.

