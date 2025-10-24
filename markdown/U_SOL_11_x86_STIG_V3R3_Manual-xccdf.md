# STIG Benchmark: Solaris 11 X86 Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000255

**Group ID:** `V-216011`

### Rule: The audit system must produce records containing sufficient information to establish the identity of any user/subject associated with the event.

**Rule ID:** `SV-216011r986460_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling the audit system will produce records with accurate time stamps, source, user, and activity information. Without this information malicious activity cannot be accurately tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone to be secured. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report the following, this is a finding. audit condition = auditing

## Group: SRG-OS-000054

**Group ID:** `V-216014`

### Rule: The operating system must provide the capability to automatically process audit records for events of interest based upon selectable, event criteria.

**Rule ID:** `SV-216014r958430_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an audit reporting capability, users find it difficult to identify specific patterns of attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000062

**Group ID:** `V-216015`

### Rule: The audit records must provide data for all auditable events defined at the organizational level for the organization-defined information system components.

**Rule ID:** `SV-216015r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account. Without accurate time stamps, source, user, and activity information, malicious activity cannot be accurately tracked. Without an audit reduction and reporting capability, users find it difficult to identify specific patterns of attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000064

**Group ID:** `V-216016`

### Rule: The operating system must generate audit records for the selected list of auditable events as defined in DoD list of events.

**Rule ID:** `SV-216016r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account. Without accurate time stamps, source, user, and activity information, malicious activity cannot be accurately tracked. Without an audit reduction and reporting capability, users find it difficult to identify specific patterns of attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000037

**Group ID:** `V-216018`

### Rule: Audit records must include what type of events occurred.

**Rule ID:** `SV-216018r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without proper system auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000038

**Group ID:** `V-216019`

### Rule: Audit records must include when (date and time) the events occurred.

**Rule ID:** `SV-216019r958414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without accurate time stamps malicious activity cannot be accurately tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000039

**Group ID:** `V-216020`

### Rule: Audit records must include where the events occurred.

**Rule ID:** `SV-216020r958416_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account. Without accurate time stamps, source, user, and activity information, malicious activity cannot be accurately tracked. Without an audit reduction and reporting capability, users find it difficult to identify specific patterns of attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000040

**Group ID:** `V-216021`

### Rule: Audit records must include the sources of the events that occurred.

**Rule ID:** `SV-216021r958418_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without accurate source information malicious activity cannot be accurately tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000041

**Group ID:** `V-216022`

### Rule: Audit records must include the outcome (success or failure) of the events that occurred.

**Rule ID:** `SV-216022r958420_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tracking both the successful and unsuccessful attempts aids in identifying threats to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216023`

### Rule: The audit system must be configured to audit file deletions.

**Rule ID:** `SV-216023r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, malicious activity cannot be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the OS version you are currently securing. # uname –v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active |cut -f2 -d= If "fd" audit flag is not included in output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "fd" audit flag is not included in output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000004

**Group ID:** `V-216024`

### Rule: The audit system must be configured to audit account creation.

**Rule ID:** `SV-216024r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, malicious activity cannot be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone currently being secured. # zonename If the command output is "global", this check applies. Determine the OS version currently being secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "ps" audit flag is not included in the output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "cusa,fm,fd,-fa,-ps,-ex" audit flags are not included in the output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000239

**Group ID:** `V-216025`

### Rule: The audit system must be configured to audit account modification.

**Rule ID:** `SV-216025r958590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, malicious activity cannot be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone currently being secured. # zonename If the command output is "global", this check applies. Determine the OS version currently being secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "ps" audit flag is not included in the output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "cusa,fm,fd,-fa,-ps,-ex" audit flags are not included in the output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000240

**Group ID:** `V-216026`

### Rule: The operating system must automatically audit account disabling actions.

**Rule ID:** `SV-216026r958592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, malicious activity cannot be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone currently being secured. # zonename If the command output is "global", this check applies. Determine the OS version currently being secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "ps" audit flag is not included in the output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "cusa,fm,fd,-fa,-ps,-ex" audit flags are not included in the output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000241

**Group ID:** `V-216027`

### Rule: The operating system must automatically audit account termination.

**Rule ID:** `SV-216027r958594_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, malicious activity cannot be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone currently being secured. # zonename If the command output is "global", this check applies. Determine the OS version currently being secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "ps" audit flag is not included in the output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "cusa,fm,fd,-fa,-ps,-ex" audit flags are not included in the output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216028`

### Rule: The operating system must ensure unauthorized, security-relevant configuration changes detected are tracked.

**Rule ID:** `SV-216028r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, malicious activity cannot be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone currently being secured. # zonename If the command output is "global", this check applies. Determine the OS version currently being secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "as" audit flag is not included in the output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "cusa,fm,fd,-fa,-ps,-ex" audit flags are not included in the output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216029`

### Rule: The audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-216029r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone currently being secured. # zonename If the command output is "global", this check applies. Determine the OS version currently being secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "as" audit flag is not included in the output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "cusa,fm,fd,-fa,-ps,-ex" audit flags are not included in the output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000032

**Group ID:** `V-216030`

### Rule: The audit system must be configured to audit login, logout, and session initiation.

**Rule ID:** `SV-216030r958406_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. Check that the audit flag for auditing login and logout is enabled. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the OS version you are currently securing. # uname –v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "lo" audit flag is not included in output, this is a finding # pfexec auditconfig -getnaflags | grep active | cut -f2 -d= If "na" and "lo" audit flags are not included in output, this is a finding For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "cusa" or if the "ft,lo,ap,ss,as,ua,pe” audit flag(s) are not included in output, this is a finding # pfexec auditconfig -t -getnaflags | cut -f2 -d= If "na" and "lo" audit flags are not included in output, this is a finding Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216033`

### Rule: The audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-216033r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. Check that the audit flag for auditing file access is enabled. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the OS version you are currently securing. # uname –v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "-fa" and "-ps" audit flags are not displayed, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "-fa", "-ex", and "-ps" audit flags are not displayed, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000061

**Group ID:** `V-216034`

### Rule: The operating system must protect against an individual falsely denying having performed a particular action. In order to do so the system must be configured to send audit records to a remote audit server.

**Rule ID:** `SV-216034r958440_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Keeping audit records on a remote system reduces the likelihood of audit records being changed or corrupted. Duplicating and protecting the audit trail on a separate system reduces the likelihood of an individual being able to deny performing an action. Solaris has supported rsyslog since version 11.1 and the differences between syslog and rsyslog are numerous. Solaris 11.4 installs rsyslog by default, but previous versions require a manual installation. When establishing a rsyslog server to forward to, it is important to consider the network requirements for this action. Note the following configuration options: There are three ways to forward message: the traditional UDP transport, which is extremely lossy but standard; the plain TCP based transport, which loses messages only during certain situations but is widely available; and the RELP transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above. Examples of each configuration: UDP *.* @remotesystemname TCP *.* @@remotesystemname RELP *.* :omrelp:remotesystemname:2514 Please note that a port number was given as there is no standard port for RELP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Audit Configuration rights profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check that the syslog audit plugin is enabled. # pfexec auditconfig -getplugin | grep audit_syslog If "inactive" appears, this is a finding. Determine which system-log service instance is online. # pfexec svcs system-log Check that the /etc/syslog.conf or /etc/rsyslog.conf file is configured properly: # grep audit.notice /etc/syslog.conf or # grep @@ /etc/rsyslog.conf If audit.notice @remotesystemname , audit.notice !remotesystemname (syslog configuration) or *.* @@remotesystemname (rsyslog configuration) points to an invalid remote system or is commented out, this is a finding. If no output is produced, this is a finding. Check the remote syslog host to ensure that audit records can be found for this host.

## Group: SRG-OS-000480

**Group ID:** `V-216035`

### Rule: The auditing system must not define a different auditing level for specific users.

**Rule ID:** `SV-216035r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. For each user on the system (not including root), check to see if special auditing flag configurations are set. # userattr audit_flags [username] If any flags are returned, this is a finding.

## Group: SRG-OS-000046

**Group ID:** `V-216038`

### Rule: The operating system must alert designated organizational officials in the event of an audit processing failure.

**Rule ID:** `SV-216038r958424_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Proper alerts to system administrators and IA officials of audit failures ensure a timely response to critical system issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. The root role is required. Verify the presence of an audit_warn entry in /etc/mail/aliases. # /usr/lib/sendmail -bv audit_warn If the response is: audit_warn... User unknown this is a finding. Review the output of the command and verify that the audit_warn alias notifies the appropriate users in this form: audit_warn:user1,user2 If an appropriate user is not listed, this is a finding.

## Group: SRG-OS-000047

**Group ID:** `V-216041`

### Rule: The operating system must shut down by default upon audit failure (unless availability is an overriding concern).

**Rule ID:** `SV-216041r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Continuing to operate a system without auditing working properly can result in undocumented access or system changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. # pfexec auditconfig -getpolicy | grep ahlt If the output does not include "ahlt" as an active audit policy, this is a finding. # pfexec auditconfig -getpolicy | grep active | grep cnt If the output includes "cnt" as an active audit policy, this is a finding.

## Group: SRG-OS-000057

**Group ID:** `V-216042`

### Rule: The operating system must protect audit information from unauthorized access.

**Rule ID:** `SV-216042r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. To ensure the veracity of audit data, the operating system must protect audit information from unauthorized access. Satisfies: SRG-OS-000057, SRG-OS-000058, SRG-OS-000059</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check that the directory storing the audit files is owned by root and has permissions 750 or less. Note: By default in Solaris 11.1, /var/audit is a link to /var/share/audit which is mounted on rpool/VARSHARE. Determine the location of the audit trail files # pfexec auditconfig -getplugin audit_binfile The output will appear in this form: Plugin: audit_binfile (active) Attributes: p_dir=/var/audit;p_fsize=0;p_minfree=1 The p_dir attribute defines the location of the audit directory. # ls -ld /var/share/audit Check the audit directory is owned by root, group is root, and permissions are 750 (rwx r-- ---) or less. If the permissions are excessive, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216045`

### Rule: The System packages must be up to date with the most recent vendor updates and security fixes.

**Rule ID:** `SV-216045r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to install security updates can provide openings for attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Software Installation Profile is required. An up-to-date Solaris repository must be accessible to the system. Enter the command: # pkg publisher to determine the current repository publisher. If a repository is not accessible, it may need to be locally installed and configured. Check for Solaris software package updates: # pfexec pkg update -n If the command does not report "No updates available for this image," this is a finding.

## Group: SRG-OS-000256

**Group ID:** `V-216047`

### Rule: The operating system must protect audit tools from unauthorized access.

**Rule ID:** `SV-216047r958610_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to maintain system configurations may result in privilege escalation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Software Installation Profile is required. Determine what the signature policy is for pkg publishers: # pkg property | grep signature-policy Check that output produces: signature-policy verify If the output does not confirm that signature-policy verify is active, this is a finding. Check that package permissions are configured and signed per vendor requirements. # pkg verify If the command produces any output unrelated to STIG changes, this is a finding. There is currently a Solaris 11 bug 16267888 which reports pkg verify errors for a variety of python packages. These can be ignored.

## Group: SRG-OS-000257

**Group ID:** `V-216048`

### Rule: The operating system must protect audit tools from unauthorized modification.

**Rule ID:** `SV-216048r958612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to maintain system configurations may result in privilege escalation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Software Installation Profile is required. Determine what the signature policy is for pkg publishers: # pkg property | grep signature-policy Check that output produces: signature-policy verify If the output does not confirm that signature-policy verify is active, this is a finding. Check that package permissions are configured and signed per vendor requirements. # pkg verify If the command produces any output unrelated to STIG changes, this is a finding. There is currently a Solaris 11 bug 16267888 which reports pkg verify errors for a variety of python packages. These can be ignored.

## Group: SRG-OS-000258

**Group ID:** `V-216049`

### Rule: The operating system must protect audit tools from unauthorized deletion.

**Rule ID:** `SV-216049r958614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to maintain system configurations may result in privilege escalation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Software Installation Profile is required. Determine what the signature policy is for pkg publishers: # pkg property | grep signature-policy Check that output produces: signature-policy verify If the output does not confirm that signature-policy verify is active, this is a finding. Check that package permissions are configured and signed per vendor requirements. # pkg verify If the command produces any output unrelated to STIG changes, this is a finding. There is currently a Solaris 11 bug 16267888 which reports pkg verify errors for a variety of python packages. These can be ignored.

## Group: SRG-OS-000278

**Group ID:** `V-216050`

### Rule: System packages must be configured with the vendor-provided files, permissions, and ownerships.

**Rule ID:** `SV-216050r958634_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to maintain system configurations may result in privilege escalation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Software Installation Profile is required. Determine what the signature policy is for pkg publishers: # pkg property | grep signature-policy Check that output produces: signature-policy verify If the output does not confirm that signature-policy verify is active, this is a finding. Check that package permissions are configured and signed per vendor requirements. # pkg verify If the command produces any output unrelated to STIG changes, this is a finding. There is currently a Solaris 11 bug 16267888 which reports pkg verify errors for a variety of python packages. These can be ignored.

## Group: SRG-OS-000480

**Group ID:** `V-216051`

### Rule: The finger daemon package must not be installed.

**Rule ID:** `SV-216051r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Finger is an insecure protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the finger package is installed. # pkg list service/network/finger If an installed package named service/network/finger is listed, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216052`

### Rule: The legacy remote network access utilities daemons must not be installed.

**Rule ID:** `SV-216052r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Legacy remote access utilities allow remote control of a system without proper authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the legacy remote access package is installed. # pkg list service/network/legacy-remote-utilities If an installed package named service/network/legacy-remote-utilities is listed, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216053`

### Rule: The NIS package must not be installed.

**Rule ID:** `SV-216053r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>NIS is an insecure protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the NIS package is installed. # pkg list service/network/nis If an installed package named "service/network/nis" is listed, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216054`

### Rule: The pidgin IM client package must not be installed.

**Rule ID:** `SV-216054r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Instant messaging is an insecure protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the pidgin package is installed. # pkg list communication/im/pidgin If an installed package named communication/im/pidgin is listed, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216055`

### Rule: The FTP daemon must not be installed unless required.

**Rule ID:** `SV-216055r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>FTP is an insecure protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the FTP package is installed. # pkg list service/network/ftp If an installed package named "service/network/ftp" is listed and not required for operations, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216056`

### Rule: The TFTP service daemon must not be installed unless required.

**Rule ID:** `SV-216056r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>TFTP is an insecure protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the TFTP package is installed. # pkg list service/network/tftp If an installed package named "/service/network/tftp" is listed and not required for operations, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216057`

### Rule: The telnet service daemon must not be installed unless required.

**Rule ID:** `SV-216057r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Telnet is an insecure protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the telnet daemon package in installed. # pkg list service/network/telnet If an installed package named "service/network/telnet" is listed and vntsd is not in use for LDoms, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216058`

### Rule: The UUCP service daemon must not be installed unless required.

**Rule ID:** `SV-216058r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>UUCP is an insecure protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the UUCP package is installed. # pkg list /service/network/uucp If an installed package named "/service/network/uucp" is listed, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216059`

### Rule: The rpcbind service must be configured for local only services unless organizationally defined.

**Rule ID:** `SV-216059r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The portmap and rpcbind services increase the attack surface of the system and should only be used when needed. The portmap or rpcbind services are used by a variety of services using remote procedure calls (RPCs). The organization may define and document the limited use of services (for example NFS) that may use these services with approval from their Authorizing Official.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the status of the rpcbind service local_only property. # svcprop -p config/local_only network/rpc/bind If the state is not "true", this is a finding, unless it is required for system operations, then this is not a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216060`

### Rule: The VNC server package must not be installed unless required.

**Rule ID:** `SV-216060r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The VNC service uses weak authentication capabilities and provides the user complete graphical system access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the VNC server package is installed. # pkg list x11/server/xvnc If an installed package named "x11/server/xvnc is listed" is listed, this is a finding.

## Group: SRG-OS-000095

**Group ID:** `V-216062`

### Rule: The operating system must be configured to provide essential capabilities.

**Rule ID:** `SV-216062r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating systems are capable of providing a wide variety of functions and services. Execution must be disabled based on organization-defined specifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify the packages installed on the system. # pkg list Any unauthorized software packages listed in the output are a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216064`

### Rule: All run control scripts must have mode 0755 or less permissive.

**Rule ID:** `SV-216064r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the startup files are writable by other users, these users could modify the startup files to insert malicious commands into the startup files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check run control script modes. # ls -lL /etc/rc* /etc/init.d /lib/svc/method If any run control script has a mode more permissive than 0755, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216065`

### Rule: All run control scripts must have no extended ACLs.

**Rule ID:** `SV-216065r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the startup files are writable by other users, these users could modify the startup files to insert malicious commands into the startup files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts have no extended ACLs. # ls -lL /etc/rc* /etc/init.d If the permissions include a "+", the file has an extended ACL and this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216066`

### Rule: Run control scripts executable search paths must contain only authorized paths.

**Rule ID:** `SV-216066r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory or other relative paths, executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, two consecutive colons, or a single period, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' executable search paths. Procedure: # find /etc/rc* /etc/init.d /lib/svc/method -type f -print | xargs grep -i PATH This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/), or has not been documented with the ISSO, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216067`

### Rule: Run control scripts library search paths must contain only authorized paths.

**Rule ID:** `SV-216067r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library search path environment variable(s) contain a list of directories for the dynamic linker to search to find libraries. If this path includes the current working directory or other relative paths, libraries in these directories may be loaded instead of system libraries. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, two consecutive colons, or a single period, this is interpreted as the current working directory. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' library search paths. # find /etc/rc* /etc/init.d -type f -print | xargs grep LD_LIBRARY_PATH This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/), or has not been documented with the ISSO, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216068`

### Rule: Run control scripts lists of preloaded libraries must contain only authorized paths.

**Rule ID:** `SV-216068r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The library preload list environment variable contains a list of libraries for the dynamic linker to load before loading the libraries required by the binary. If this list contains paths to libraries to the current working directory that have not been authorized, unintended libraries may be preloaded. This variable is formatted as a space-separated list of libraries. Paths starting with a slash (/) are absolute paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify run control scripts' library preload list. Procedure: # find /etc/rc* /etc/init.d -type f -print | xargs grep LD_PRELOAD This variable is formatted as a colon-separated list of paths. If there is an empty entry, such as a leading or trailing colon, or two consecutive colons, this is a finding. If an entry begins with a character other than a slash (/), or has not been documented with the ISSO, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216069`

### Rule: Run control scripts must not execute world writable programs or scripts.

**Rule ID:** `SV-216069r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>World writable files could be modified accidentally or maliciously to compromise system integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions on the files or scripts executed from system startup scripts to see if they are world writable. Create a list of all potential run command level scripts. # ls -l /etc/init.d/* /etc/rc* | tr '\011' ' ' | tr -s ' ' | cut -f 9,9 -d " " Create a list of world writable files. # find / -perm -002 -type f >> WorldWritableFileList Determine if any of the world writeable files in "WorldWritableFileList" are called from the run command level scripts. Note: Depending upon the number of scripts vs. world writable files, it may be easier to inspect the scripts manually. # more `ls -l /etc/init.d/* /etc/rc* | tr '\011' ' ' | tr -s ' ' | cut -f 9,9 -d " "` If any system startup script executes any file or script that is world writable, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216070`

### Rule: All system start-up files must be owned by root.

**Rule ID:** `SV-216070r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System start-up files not owned by root could lead to system compromise by allowing malicious users or applications to modify them for unauthorized purposes. This could lead to system and network compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check run control scripts' ownership. # ls -lL /etc/rc* /etc/init.d If any run control script is not owned by root, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216071`

### Rule: All system start-up files must be group-owned by root, sys, or bin.

**Rule ID:** `SV-216071r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If system start-up files do not have a group owner of root or a system group, the files may be modified by malicious users or intruders.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check run control scripts' group ownership. Procedure: # ls -lL /etc/rc* /etc/init.d If any run control script is not group-owned by root, sys, or bin, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216072`

### Rule: System start-up files must only execute programs owned by a privileged UID or an application.

**Rule ID:** `SV-216072r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System start-up files executing programs owned by other than root (or another privileged user) or an application indicates the system may have been compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the programs executed by system start-up files. Determine the ownership of the executed programs. # cat /etc/rc* /etc/init.d/* | more Check the ownership of every program executed by the system start-up files. # ls -l <executed program> If any executed program is not owned by root, sys, bin, or in rare cases, an application account, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216073`

### Rule: Any X Windows host must write .Xauthority files.

**Rule ID:** `SV-216073r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.Xauthority files ensure the user is authorized to access the specific X Windows host. If .Xauthority files are not used, it may be possible to obtain unauthorized access to the X Windows host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If X Display Manager (XDM) is not used on the system, this is not applicable. Determine if XDM is running. Procedure: # ps -ef | grep xdm If X Display Manager (XDM) is not used on the system, this is not applicable. Determine if XDM is running. Procedure: # ps -ef | grep xdm Check for .Xauthority files being utilized by looking for such files in the home directory of a user that uses X. Procedure: # cd ~someuser # ls -la .Xauthority If the .Xauthority file does not exist, ask the SA if the user is using X Windows. If the user is utilizing X Windows and the .Xauthority file does not exist, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216074`

### Rule: All .Xauthority files must have mode 0600 or less permissive.

**Rule ID:** `SV-216074r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.Xauthority files ensure the user is authorized to access the specific X Windows host. Excessive permissions may permit unauthorized modification of these files, which could lead to Denial of Service to authorized access or allow unauthorized access to be obtained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If X Display Manager (XDM) is not used on the system, this is not applicable. Determine if XDM is running. Procedure: # ps -ef | grep xdm Check the file permissions for the .Xauthority files in the home directories of users of X. Procedure: # cd ~<X user> # ls -lL .Xauthority If the file mode is more permissive than 0600, this is finding.

## Group: SRG-OS-000480

**Group ID:** `V-216075`

### Rule: The .Xauthority files must not have extended ACLs.

**Rule ID:** `SV-216075r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.Xauthority files ensure the user is authorized to access the specific X Windows host. Extended ACLs may permit unauthorized modification of these files, which could lead to Denial of Service to authorized access or allow unauthorized access to be obtained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If X Display Manager (XDM) is not used on the system, this is not applicable. Determine if XDM is running. Procedure: # ps -ef | grep xdm Check the file permissions for the .Xauthority files. # ls -lL .Xauthority If the permissions include a "+", the file has an extended ACL and this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216076`

### Rule: X displays must not be exported to the world.

**Rule ID:** `SV-216076r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Open X displays allow an attacker to capture keystrokes and to execute commands remotely. Many users have their X Server set to xhost +, permitting access to the X Server by anyone, from anywhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If X Windows is not used on the system, this is not applicable. Check the output of the xhost command from an X terminal. Procedure: $ xhost If the output reports access control is enabled (and possibly lists the hosts that can receive X Window logins), this is not a finding. If the xhost command returns a line indicating access control is disabled, this is a finding. NOTE: It may be necessary to define the display if the command reports it cannot open the display. Procedure: $ DISPLAY=MachineName:0.0; export DISPLAY MachineName may be replaced with an Internet Protocol Address. Repeat the check procedure after setting the display.

## Group: SRG-OS-000480

**Group ID:** `V-216077`

### Rule: .Xauthority or X*.hosts (or equivalent) file(s) must be used to restrict access to the X server.

**Rule ID:** `SV-216077r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If access to the X server is not restricted, a user's X session may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If X Display Manager (XDM) is not used on the system, this is not applicable. Determine if XDM is running. Procedure: # ps -ef | grep xdm Determine if xauth is being used. Procedure: # xauth xauth> list If the above command sequence does not show any host other than the localhost, then xauth is not being used. Search the system for an X*.hosts files, where * is a display number that may be used to limit X window connections. If no files are found, X*.hosts files are not being used. If the X*.hosts files contain any unauthorized hosts, this is a finding. If both xauth and X*.hosts files are not being used, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216078`

### Rule: The .Xauthority utility must only permit access to authorized hosts.

**Rule ID:** `SV-216078r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unauthorized clients are permitted access to the X server, a user's X session may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If X Display Manager (XDM) is not used on the system, this is not applicable. Determine if XDM is running. Procedure: # ps -ef | grep xdm Check the X Window system access is limited to authorized clients. Procedure: # xauth xauth> list Ask the SA if the clients listed are authorized. If any are not, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216079`

### Rule: X Window System connections that are not required must be disabled.

**Rule ID:** `SV-216079r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unauthorized clients are permitted access to the X server, a user's X session may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the X Window system is running. Procedure: # ps -ef |grep X Ask the SA if the X Window system is an operational requirement. If it is not, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216080`

### Rule: The graphical login service provides the capability of logging into the system using an X-Windows type interface from the console. If graphical login access for the console is required, the service must be in local-only mode.

**Rule ID:** `SV-216080r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Externally accessible graphical desktop software may open the system to remote attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the X11 server system is providing remote services on the network. # svcprop -p options/tcp_listen svc:/application/x11/x11-server If the output of the command is "true" and network access to graphical user login is not required, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216081`

### Rule: Generic Security Services (GSS) must be disabled.

**Rule ID:** `SV-216081r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This service should be disabled if it is not required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the status of the Generic Security Services. # svcs -Ho state svc:/network/rpc/gss If the GSS service is reported as online, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216082`

### Rule: Systems services that are not required must be disabled.

**Rule ID:** `SV-216082r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Services that are enabled but not required by the mission may provide excessive access or additional attack vectors to penetrate the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine all of the systems services that are enabled on the system. # svcs -a | grep online Document all enabled services and disable any that are not required.

## Group: SRG-OS-000480

**Group ID:** `V-216083`

### Rule: TCP Wrappers must be enabled and configured per site policy to only allow access by approved hosts and services.

**Rule ID:** `SV-216083r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>TCP Wrappers are a host-based access control system that allows administrators to control who has access to various network services based on the IP address of the remote end of the connection. TCP Wrappers also provide logging information via syslog about both successful and unsuccessful connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TCP Wrappers are enabled and the host.deny and host.allow files exist. # inetadm -p | grep tcp_wrappers If the output of this command is "tcp_wrappers=FALSE", this is a finding. # ls /etc/hosts.deny /etc/hosts.deny # ls /etc/hosts.allow /etc/hosts.allow If these files do not exist or do not contain the names of allowed or denied hosts, this is a finding.

## Group: SRG-OS-000076

**Group ID:** `V-216086`

### Rule: User passwords must be changed at least every 60 days.

**Rule ID:** `SV-216086r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the lifespan of authenticators limits the period of time an unauthorized user has access to the system while using compromised credentials and reduces the period of time available for password-guessing attacks to run against a single password. Solaris 11.4 introduced new password security features that allow for a more granular approach to password duration parameters. The introduction of MAXDAYS, MINDAYS, and WARNDAYS allow the /etc/default/passwd configuration file to enforce a password change every 60 days.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Determine if user passwords are properly configured to be changed every 60 days. Determine the OS version to be secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # logins -ox |awk -F: '( $1 != "root" && $8 != "LK" && $8 != "NL" && ( $11 > “56" || $11 < “1" )) { print }' If output is returned and the listed account is accessed via direct logon, this is a finding. Check that /etc/default/password is configured to enforce password expiration every eight weeks or less. # grep "^MAXWEEKS=" /etc/default/passwd If the command does not report MAXWEEKS=8 or less, this is a finding. For Solaris 11.4 or newer: # logins -ox |awk -F: '( $1 != "root" && $8 != "LK" && $8 != "NL" && ($11 > "60"|| $11 < "1")) { print }' If output is returned and the listed account is accessed via direct logon, this is a finding. Check that /etc/default/password is configured to enforce password expiration every 60 days or less. Note: It is an error to set both the WEEKS and the DAYS variant for a given MIN/MAX/WARN variable. # grep "^MAXDAYS=" /etc/default/passwd If the command does not report MAXDAYS=60 or less, this is a finding. # grep "^MAXWEEKS=" /etc/default/passwd If output is returned, this is a finding.

## Group: SRG-OS-000002

**Group ID:** `V-216087`

### Rule: The operating system must automatically terminate temporary accounts within 72 hours.

**Rule ID:** `SV-216087r958364_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, the operating system must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. When temporary and emergency accounts are created, there is a risk the temporary account may remain in place and active after the need for the account no longer exists. To address this, in the event temporary accounts are required, accounts designated as temporary in nature must be automatically terminated after 72 hours. Such a process and capability greatly reduces the risk of accounts being misused, hijacked, or data compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Determine if an expiration date is set for temporary accounts. # logins -aox |awk -F: '($14 == "0") {print}' This command produces a list of accounts with no expiration date set. If any of these accounts are temporary accounts, this is a finding. # logins -aox |awk -F: '($14 != "0") {print}' This command produces a list of accounts with an expiration date set as defined in the last field. If any accounts have a date that is not within 72 hours, this is a finding.

## Group: SRG-OS-000075

**Group ID:** `V-216088`

### Rule: The operating system must enforce minimum password lifetime restrictions.

**Rule ID:** `SV-216088r1016284_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be changed at specific policy-based intervals; however, if the information system or application allows the user to immediately and continually change their password, then the password could be repeatedly changed in a short period of time, defeating the organization's policy regarding password reuse. Solaris 11.4 introduced new password security features that allow for a more granular approach to password duration parameters. The introduction of MAXDAYS, MINDAYS, and WARNDAYS allow the /etc/default/passwd configuration file to enforce a minimum password lifetime of a single day.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check whether the minimum time period between password changes for each user account is one day or greater. Determine the OS version to be secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # logins -ox |awk -F: '( $1 != "root" && $8 != "LK" && $8 != "NL" && $10 < "1" ) { print }' If output is returned and the listed account is accessed via direct logon, this is a finding. Check that /etc/default/password is configured to minimum password change time of one week. # grep "^MINWEEKS=" /etc/default/passwd If the command does not report MINWEEKS=1 or more, this is a finding. For Solaris 11.4 or newer: # logins -ox |awk -F: '( $1 != "root" && $8 != "LK" && $8 != "NL" && $10 < "1" ) { print }' If output is returned and the listed account is accessed via direct logon, this is a finding. Check that /etc/default/password is configured to minimum password change time of one day. Note: It is an error to set both the WEEKS and the DAYS variant for a given MIN/MAX/WARN variable. # grep "^MINDAYS=" /etc/default/passwd If the command does not report MINDAYS=1 or more, this is a finding. # grep "^MINWEEKS=" /etc/default/passwd If output is returned, this is a finding.

## Group: SRG-OS-000078

**Group ID:** `V-216089`

### Rule: User passwords must be at least 15 characters in length.

**Rule ID:** `SV-216089r1016285_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password is, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system password length setting. # grep ^PASSLENGTH /etc/default/passwd If PASSLENGTH is not set to 15 or more, this is a finding.

## Group: SRG-OS-000072

**Group ID:** `V-216091`

### Rule: The system must require at least eight characters be changed between the old and new passwords during a password change.

**Rule ID:** `SV-216091r1016286_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure password changes are effective in their goals, the system must ensure old and new passwords have significant differences. Without significant changes, new passwords may be easily guessed based on the value of a previously compromised password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/default/passwd to verify the MINDIFF setting. # grep ^MINDIFF /etc/default/passwd If the setting is not present, or is less than eight, this is a finding.

## Group: SRG-OS-000069

**Group ID:** `V-216092`

### Rule: The system must require passwords to contain at least one uppercase alphabetic character.

**Rule ID:** `SV-216092r1016287_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Complex passwords can reduce the likelihood of success of automated password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MINUPPER setting. # grep ^MINUPPER /etc/default/passwd If MINUPPER is not set to one or more, this is a finding.

## Group: SRG-OS-000070

**Group ID:** `V-216093`

### Rule: The operating system must enforce password complexity requiring that at least one lowercase character is used.

**Rule ID:** `SV-216093r1016288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Complex passwords can reduce the likelihood of success of automated password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MINLOWER setting. # grep ^MINLOWER /etc/default/passwd If MINLOWER is not set to one or more, this is a finding.

## Group: SRG-OS-000071

**Group ID:** `V-216094`

### Rule: The system must require passwords to contain at least one numeric character.

**Rule ID:** `SV-216094r1016289_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Complex passwords can reduce the likelihood of success of automated password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MINDIGIT setting. # grep ^MINDIGIT /etc/default/passwd If the MINDIGIT setting is less than one, this is a finding.

## Group: SRG-OS-000266

**Group ID:** `V-216095`

### Rule: The system must require passwords to contain at least one special character.

**Rule ID:** `SV-216095r1016290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Complex passwords can reduce the likelihood of success of automated password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MINSPECIAL setting. # grep ^MINSPECIAL /etc/default/passwd If the MINSPECIAL setting is less than one, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216096`

### Rule: The system must require passwords to contain no more than three consecutive repeating characters.

**Rule ID:** `SV-216096r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Complex passwords can reduce the likelihood of success of automated password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MAXREPEATS setting. # grep ^MAXREPEATS /etc/default/passwd If the MAXREPEATS setting is greater than 3, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216097`

### Rule: The system must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-216097r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Complex passwords can reduce the likelihood of success of automated password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Determine if accounts with blank or null passwords exist. # logins -po If any account is listed, this is a finding.

## Group: SRG-OS-000073

**Group ID:** `V-216098`

### Rule: Systems must employ cryptographic hashes for passwords using the SHA-2 family of algorithms or FIPS 140-2 approved successors.

**Rule ID:** `SV-216098r1016291_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptographic hashes provide quick password authentication while not actually storing the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine which cryptographic algorithms are configured. # grep ^CRYPT /etc/security/policy.conf If the command output does not include the lines below, this is a finding. CRYPT_DEFAULT=6 CRYPT_ALGORITHMS_ALLOW=5,6

## Group: SRG-OS-000021

**Group ID:** `V-216099`

### Rule: The system must disable accounts after three consecutive unsuccessful login attempts.

**Rule ID:** `SV-216099r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing continued access to accounts on the system exposes them to brute-force password-guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify RETRIES is set in the login file. # grep ^RETRIES /etc/default/login If the output is not RETRIES=3 or fewer, this is a finding. Verify the account locks after invalid login attempts. # grep ^LOCK_AFTER_RETRIES /etc/security/policy.conf If the output is not LOCK_AFTER_RETRIES=YES, this is a finding. For each user in the system, use the command: # userattr lock_after_retries [username] to determine if the user overrides the system value. If the output of this command is "no", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216100`

### Rule: The delay between login prompts following a failed login attempt must be at least 4 seconds.

**Rule ID:** `SV-216100r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As an immediate return of an error message, coupled with the capability to try again, may facilitate automatic and rapid-fire brute-force password attacks by a malicious user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SLEEPTIME parameter in the /etc/default/login file. # grep ^SLEEPTIME /etc/default/login If the output is not SLEEPTIME=4 or more, this is a finding.

## Group: SRG-OS-000028

**Group ID:** `V-216101`

### Rule: The system must require users to re-authenticate to unlock a graphical desktop environment.

**Rule ID:** `SV-216101r958400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing access to a graphical environment when the user is not attending the system can allow unauthorized users access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not running XWindows, this check does not apply. Determine if the screen saver timeout is configured properly. # grep "^\*timeout:" /usr/share/X11/app-defaults/XScreenSaver If the output is not: *timeout: 0:15:00 or a shorter time interval, this is a finding. # grep "^\*lockTimeout:" /usr/share/X11/app-defaults/XScreenSaver If the output is not: *lockTimeout: 0:00:05 or a shorter time interval, this is a finding. # grep "^\*lock:" /usr/share/X11/app-defaults/XScreenSaver If the output is not: *lock: True this is a finding. For each existing user, check the configuring of their personal .xscreensaver file. # grep "^timeout:" $HOME/.xscreensaver If the output is not: timeout: 0:15:00 or a shorter time interval, this is a finding. # grep "^lockTimeout:" $HOME/.xscreensaver If the output is not: lockTimeout: 0:00:05 or a shorter time interval, this is a finding. # grep "^lock:" $HOME/.xscreensaver If the output is not: lock: True this is a finding.

## Group: SRG-OS-000029

**Group ID:** `V-216102`

### Rule: Graphical desktop environments provided by the system must automatically lock after 15 minutes of inactivity.

**Rule ID:** `SV-216102r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing access to a graphical environment when the user is not attending the system can allow unauthorized users access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not running XWindows, this check does not apply. Determine if the screen saver timeout is configured properly. # grep "^\*timeout:" /usr/share/X11/app-defaults/XScreenSaver If the output is not: *timeout: 0:15:00 this is a finding. # grep "^\*lockTimeout:" /usr/share/X11/app-defaults/XScreenSaver If the output is not: *lockTimeout: 0:00:05 this is a finding. # grep "^\*lock:" /usr/share/X11/app-defaults/XScreenSaver If the output is not: *lock: True this is a finding. For each existing user, check the configuration of their personal .xscreensaver file. # grep "^lock:" $HOME/.xscreensaver If the output is not: *lock: True this is a finding. grep "^lockTimeout:" $HOME/.xscreensaver If the output is not: *lockTimeout: 0:00:05 this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216103`

### Rule: The system must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-216103r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of common words in passwords simplifies password-cracking attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/default/passwd for dictionary check configuration. # grep ^DICTION /etc/default/passwd If the DICTIONLIST or DICTIONDBDIR settings are not present and are not set to: DICTIONLIST=/usr/share/lib/dict/words DICTIONDBDIR=/var/passwd this is a finding. Determine if the target files exist. # ls -l /usr/share/lib/dict/words /var/passwd If the files defined by DICTIONLIST or DICTIONBDIR are not present or are empty, this is a finding.

## Group: SRG-OS-000109

**Group ID:** `V-216105`

### Rule: The operating system must require individuals to be authenticated with an individual authenticator prior to using a group authenticator.

**Rule ID:** `SV-216105r1016292_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing any user to elevate their privileges can allow them excessive control of the system tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the root user is configured as a role, rather than a normal user. # userattr type root If the command does not return the word "role", this is a finding. Verify at least one local user has been assigned the root role. # grep '[:;]roles=root[^;]*' /etc/user_attr If no lines are returned, or no users are permitted to assume the root role, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216106`

### Rule: The default umask for system and users must be 077.

**Rule ID:** `SV-216106r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting a very secure default value for umask ensures that users make a conscious choice about their file permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Determine if the default umask is configured properly. # grep -i "^UMASK=" /etc/default/login If "UMASK=077" is not displayed, this is a finding. Check local initialization files: # cut -d: -f1 /etc/passwd | xargs -n1 -iUSER sh -c "grep umask ~USER/.*" If this command does not output a line indicating "umask 077" for each user, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216107`

### Rule: The default umask for FTP users must be 077.

**Rule ID:** `SV-216107r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Setting a very secure default value for umask ensures that users make a conscious choice about their file permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The package service/network/ftp must be installed for this check. # pkg list service/network/ftp If the output of this command is: pkg list: no packages matching 'service/network/ftp' installed no further action is required. Determine if the FTP umask is set to 077. # egrep -i "^UMASK" /etc/proftpd.conf | awk '{ print $2 }' If 077 is not displayed, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216108`

### Rule: The value mesg n must be configured as the default setting for all users.

**Rule ID:** `SV-216108r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The "mesg n" command blocks attempts to use the "write" or "talk" commands to contact users at their terminals, but has the side effect of slightly strengthening permissions on the user's TTY device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if "mesg n" is the default for users. # grep "^mesg" /etc/.login # grep "^mesg" /etc/profile If either of these commands produces a line: mesg y this is a finding. For each existing user on the system, enter the command: # mesg If the command output is: is y this is a finding.

## Group: SRG-OS-000003

**Group ID:** `V-216109`

### Rule: User accounts must be locked after 35 days of inactivity.

**Rule ID:** `SV-216109r1016293_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers that are able to exploit an inactive account can potentially obtain and maintain undetected access to an application. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of user inactivity and disable accounts after 35 days of inactivity. Such a process greatly reduces the risk that accounts will be hijacked, leading to a data compromise. This policy does not apply to either emergency accounts or infrequently used accounts. Infrequently used accounts are local logon accounts used by system administrators when network or normal logon/access is not available. Emergency accounts are administrator accounts created in response to crisis situations. Satisfies: SRG-OS-000003, SRG-OS-000118</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the 35-day inactivity lock is configured properly. # useradd -D | xargs -n 1 | grep inactive |\ awk -F= '{ print $2 }' If the command returns a result other than 35, this is a finding. The root role is required for the "logins" command. For each configured user name and role name on the system, determine whether a 35-day inactivity period is configured. Replace [username] with an actual user name or role name. # logins -axo -l [username] | awk -F: '{ print $13 }' If these commands provide output other than 35, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216112`

### Rule: Login services for serial ports must be disabled.

**Rule ID:** `SV-216112r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Login services should not be enabled on any serial ports that are not strictly required to support the mission of the system. This action can be safely performed even when console access is provided using a serial port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if terminal login services are disabled. # svcs -Ho state svc:/system/console-login:terma # svcs -Ho state svc:/system/console-login:termb If the system/console-login services are not "disabled", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216113`

### Rule: The nobody access for RPC encryption key storage service must be disabled.

**Rule ID:** `SV-216113r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If login by the user "nobody" is allowed for secure RPC, there is an increased risk of system compromise. If keyserv holds a private key for the "nobody" user, it will be used by key_encryptsession to compute a magic phrase which can be easily recovered by a malicious user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the rpc-authdes package is installed: # pkg list solaris/legacy/security/rpc-authdes If the output of this command is: pkg list: no packages matching 'solaris/legacy/security/rpc-authdes' installed no further action is required. Determine if "nobody" access for keyserv is enabled. # grep "^ENABLE_NOBODY_KEYS=" /etc/default/keyserv If the output of the command is not: ENABLE_NOBODY_KEYS=NO this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216114`

### Rule: X11 forwarding for SSH must be disabled.

**Rule ID:** `SV-216114r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As enabling X11 Forwarding on the host can permit a malicious user to secretly open another X11 connection to another remote client during the session and perform unobtrusive activities such as keystroke monitoring, if the X11 services are not required for the system's intended function, they should be disabled or restricted as appropriate to the user's needs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if X11 Forwarding is enabled. # grep "^X11Forwarding" /etc/ssh/sshd_config If the output of this command is not: X11Forwarding no this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216115`

### Rule: Consecutive login attempts for SSH must be limited to 3.

**Rule ID:** `SV-216115r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Setting the authentication login limit to a low value will disconnect the attacker and force a reconnect, which severely limits the speed of such brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if consecutive login attempts are limited to 3. # grep "^MaxAuthTries" /etc/ssh/sshd_config | grep -v Log If the output of this command is not: MaxAuthTries 6 this is a finding. Note: Solaris SSH MaxAuthTries of 6 maps to 3 actual failed attempts.

## Group: SRG-OS-000480

**Group ID:** `V-216116`

### Rule: The rhost-based authentication for SSH must be disabled.

**Rule ID:** `SV-216116r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting this parameter forces users to enter a password when authenticating with SSH.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if rhost-based authentication is enabled. # grep "^IgnoreRhosts" /etc/ssh/sshd_config If the output is produced and it is not: IgnoreRhosts yes this is a finding. If the IgnoreRhosts line does not exist in the file, the default setting of "Yes" is automatically used and there is no finding.

## Group: SRG-OS-000480

**Group ID:** `V-216117`

### Rule: Direct root account login must not be permitted for SSH access.

**Rule ID:** `SV-216117r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system should not allow users to log in as the root user directly, as audited actions would be non-attributable to a specific user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if root login is disabled for the SSH service. # grep "^PermitRootLogin" /etc/ssh/sshd_config If the output of this command is not: PermitRootLogin no this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216118`

### Rule: Login must not be permitted with empty/null passwords for SSH.

**Rule ID:** `SV-216118r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Permitting login without a password is inherently risky.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if empty/null passwords are allowed for the SSH service. # grep "^PermitEmptyPasswords" /etc/ssh/sshd_config If the output of this command is not: PermitEmptyPasswords no this is a finding.

## Group: SRG-OS-000163

**Group ID:** `V-216119`

### Rule: The operating system must terminate the network connection associated with a communications session at the end of the session or after 10 minutes of inactivity.

**Rule ID:** `SV-216119r970703_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This requirement applies to both internal and external networks. Terminating network connections associated with communications sessions means de-allocating associated TCP/IP address/port pairs at the operating system level. The time period of inactivity may, as the organization deems necessary, be a set of time periods by type of network access or for specific accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if SSH is configured to disconnect sessions after 10 minutes of inactivity. # grep ClientAlive /etc/ssh/sshd_config If the output of this command is not: ClientAliveInterval 600 ClientAliveCountMax 0 this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216120`

### Rule: Host-based authentication for login-based services must be disabled.

**Rule ID:** `SV-216120r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of .rhosts authentication is an insecure protocol and can be replaced with public-key authentication using Secure Shell. As automatic authentication settings in the .rhosts files can provide a malicious user with sensitive system credentials, the use of .rhosts files should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This is the location for Solaris 11.1. For earlier versions, the information is in /etc/pam.conf. Determine if host-based authentication services are enabled. # grep 'pam_rhosts_auth.so.1' /etc/pam.conf /etc/pam.d/*| grep -vc '^#' If the returned result is not 0 (zero), this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216121`

### Rule: The use of FTP must be restricted.

**Rule ID:** `SV-216121r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>FTP is an insecure protocol that transfers files and credentials in clear text, and can be replaced by using SFTP. However, if FTP is permitted for use in the environment, it is important to ensure that the default "system" accounts are not permitted to transfer files via FTP, especially the root role. Consider also adding the names of other privileged or shared accounts that may exist on the system such as user "oracle" and the account which the web server process runs under.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Determine if the FTP server package is installed: # pkg list service/network/ftp If the output of this command is: pkg list: no packages matching 'service/network/ftp' installed no further action is required. If the FTP server is installed, determine if FTP access is restricted. # for user in `logins -s | awk '{ print $1 }'` \ aiuser noaccess nobody nobody4; do grep -w "${user}" /etc/ftpd/ftpusers >/dev/null 2>&1 if [ $? != 0 ]; then echo "User '${user}' not in /etc/ftpd/ftpusers." fi done If output is returned, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216122`

### Rule: The system must not allow autologin capabilities from the GNOME desktop.

**Rule ID:** `SV-216122r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As automatic logins are a known security risk for other than "kiosk" types of systems, GNOME automatic login should be disabled in pam.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if autologin is enabled for the GNOME desktop. # egrep "auth|account" /etc/pam.d/gdm-autologin | grep -vc ^# If the command returns other than "0", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216123`

### Rule: Unauthorized use of the at or cron capabilities must not be permitted.

**Rule ID:** `SV-216123r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>On many systems, only the system administrator needs the ability to schedule jobs. Even though a given user is not listed in the "cron.allow" file, cron jobs can still be run as that user. The "cron.allow" file only controls administrative access to the "crontab" command for scheduling and modifying cron jobs. Much more effective access controls for the cron system can be obtained by using Role-Based Access Controls (RBAC).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that "at" and "cron" users are configured correctly. # ls /etc/cron.d/cron.deny If cron.deny exists, this is a finding. # ls /etc/cron.d/at.deny If at.deny exists, this is a finding. # cat /etc/cron.d/cron.allow cron.allow should have a single entry for "root", or the cron.allow file is removed if using RBAC. If any accounts other than root that are listed and they are not properly documented with the IA staff, this is a finding. # wc -l /etc/cron.d/at.allow | awk '{ print $1 }' If the output is non-zero, this is a finding, or the at.allow file is removed if using RBAC.

## Group: SRG-OS-000480

**Group ID:** `V-216124`

### Rule: Logins to the root account must be restricted to the system console only.

**Rule ID:** `SV-216124r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use an authorized mechanism such as RBAC and the "su" command to provide administrative access to unprivileged accounts. These mechanisms provide an audit trail in the event of problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine if root login is restricted to the console. # grep "^CONSOLE=/dev/console" /etc/default/login If the output of this command is not: CONSOLE=/dev/console this is a finding.

## Group: SRG-OS-000025

**Group ID:** `V-216125`

### Rule: The operating system, upon successful logon, must display to the user the date and time of the last logon (access).

**Rule ID:** `SV-216125r987814_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Users need to be aware of activity that occurs regarding their account. Providing users with information regarding the date and time of their last successful login allows the user to determine if any unauthorized activity has occurred and gives them an opportunity to notify administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if last login will be printed for SSH users. # grep PrintLastLog /etc/ssh/sshd_config If PrintLastLog is found, not preceded with a "#" sign, and is set to "no", this is a finding. PrintLastLog should either not exist (defaulting to yes) or exist and be set to yes.

## Group: SRG-OS-000030

**Group ID:** `V-216126`

### Rule: The operating system must provide the capability for users to directly initiate session lock mechanisms.

**Rule ID:** `SV-216126r1016294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the system but does not want to log out because of the temporary nature of the absence. Rather than be forced to wait for a period of time to expire before the user session can be locked, the operating system needs to provide users with the ability to manually invoke a session lock so users may secure their account should the need arise for them to temporarily vacate the immediate physical vicinity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the lock screen function works correctly. For Solaris 11, 11.1, 11.2, and 11.3: In the GNOME 2 desktop System >> Lock Screen. For Solaris 11.4 or newer: In the GNOME 3 desktop Status Menu (top right corner) >> Lock Icon, check that the screen locks and displays the "password" prompt. Check that "Disable Screensaver" is not selected in the GNOME Screensaver preferences. If the screen does not lock or the "Disable Screensaver" option is selected, this is a finding.

## Group: SRG-OS-000031

**Group ID:** `V-216127`

### Rule: The operating system session lock mechanism, when activated on a device with a display screen, must place a publicly viewable pattern onto the associated display, hiding what was previously visible on the screen.

**Rule ID:** `SV-216127r958404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the system but does not log out because of the temporary nature of the absence. The session lock will also include an obfuscation of the display screen to prevent other users from reading what was previously displayed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Solaris 11, 11.1, 11.2, and 11.3: In the GNOME 2 desktop System >> Preferences >> Screensaver. For Solaris 11.4 or newer: If using the default GNOME desktop: Activities >> Show Applications >> select "Screensaver" icon. If using the GNOME Classic desktop: Applications >> Other >> Screensaver menu item the user can select other screens or disable screensaver. Check that "Disable Screensaver" is not selected in the Gnome Screensaver preferences. If "Disable Screensaver" is selected or "Blank Screen Only" is not selected, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216128`

### Rule: The operating system must not allow logins for users with blank passwords.

**Rule ID:** `SV-216128r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the password field is blank and the system does not enforce a policy that passwords are required, it could allow login without proper authentication of a user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system is enforcing a policy that passwords are required. # grep ^PASSREQ /etc/default/login If the command does not return: PASSREQ=YES this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216129`

### Rule: The operating system must prevent remote devices that have established a non-remote connection with the system from communicating outside of the communication path with resources in external networks.

**Rule ID:** `SV-216129r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This control enhancement is implemented within the remote device (e.g., notebook/laptop computer) via configuration settings not configurable by the user of the device. An example of a non-remote communications path from a remote device is a virtual private network. When a non-remote connection is established using a virtual private network, the configuration settings prevent split-tunneling. Split-tunneling might otherwise be used by remote users to communicate with the information system as an extension of the system and to communicate with local resources, such as a printer or file server. The remote device, when connected by a non-remote connection, becomes an extension of the information system allowing dual communications paths, such as split-tunneling, in effect allowing unauthorized external connections into the system. This is a split-tunneling requirement that can be controlled via the operating system by disabling interfaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the "RestrictOutbound" profile is configured properly: # profiles -p RestrictOutbound info If the output is not: name=RestrictOutbound desc=Restrict Outbound Connections limitpriv=zone,!net_access this is a finding. For users who are not allowed external network access, determine if a user is configured with the "RestrictOutbound" profile. # profiles -l [username] If the output does not include: [username]: RestrictOutbound this is a finding.

## Group: SRG-OS-000027

**Group ID:** `V-216130`

### Rule: The operating system must limit the number of concurrent sessions for each account to an organization-defined number of sessions.

**Rule ID:** `SV-216130r958398_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Limiting the number of allowed users and sessions per user can limit risks related to denial of service attacks. The organization may define the maximum number of concurrent sessions for an information system account globally, by account type, by account, or by a combination thereof. This requirement addresses concurrent sessions for a single information system account and does not address concurrent sessions by a single user via multiple accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify the organizational requirements for maximum number of sessions and which users must be restricted. If there are no requirements to limit concurrent sessions, this item does not apply. For each user requiring concurrent session restrictions, determine if that user is in the user.[username] project where [username] is the user's account username. # projects [username] | grep user If the output does not include the project user.[username], this is a finding. Determine the project membership for the user. # projects [username] If the user is a member of any project other than default, group.[groupname], or user.[username], this is a finding. Determine whether the max-tasks resource control is enabled properly. # projects -l user.[username] | grep attribs If the output does not include the text: attribs: project.max-tasks=(privileged,[MAX],deny) where [MAX] is the organization-defined maximum number of concurrent sessions, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216131`

### Rule: The system must disable directed broadcast packet forwarding.

**Rule ID:** `SV-216131r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This parameter must be disabled to reduce the risk of denial of service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if directed broadcast packet forwarding is disabled. # ipadm show-prop -p _forward_directed_broadcasts -co current ip If the output of this command is not "0", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216132`

### Rule: The system must not respond to ICMP timestamp requests.

**Rule ID:** `SV-216132r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By accurately determining the system's clock state, an attacker can more effectively attack certain time-based pseudorandom number generators (PRNGs) and the authentication systems that rely on them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if ICMP time stamp responses are disabled. # ipadm show-prop -p _respond_to_timestamp -co current ip If the output of both commands is not "0", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216133`

### Rule: The system must not respond to ICMP broadcast timestamp requests.

**Rule ID:** `SV-216133r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By accurately determining the system's clock state, an attacker can more effectively attack certain time-based pseudorandom number generators (PRNGs) and the authentication systems that rely on them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if response to ICMP broadcast timestamp requests is disabled. # ipadm show-prop -p _respond_to_timestamp_broadcast -co current ip If the output of this command is not "0", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216134`

### Rule: The system must not respond to ICMP broadcast netmask requests.

**Rule ID:** `SV-216134r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By determining the netmasks of various computers in your network, an attacker can better map your subnet structure and infer trust relationships.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the response to address mask broadcast is disabled. # ipadm show-prop -p _respond_to_address_mask_broadcast -co current ip If the output of this command is not "0", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216135`

### Rule: The system must not respond to broadcast ICMP echo requests.

**Rule ID:** `SV-216135r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP echo requests can be useful for reconnaissance of systems and for denial of service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if ICMP echo requests response is disabled. # ipadm show-prop -p _respond_to_echo_broadcast -co current ip If the output of this command is not "0", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216136`

### Rule: The system must not respond to multicast echo requests.

**Rule ID:** `SV-216136r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Multicast echo requests can be useful for reconnaissance of systems and for denial of service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if response to multicast echo requests is disabled. # ipadm show-prop -p _respond_to_echo_multicast -co current ipv4 # ipadm show-prop -p _respond_to_echo_multicast -co current ipv6 If the output of all commands is not "0", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216137`

### Rule: The system must ignore ICMP redirect messages.

**Rule ID:** `SV-216137r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Ignoring ICMP redirect messages reduces the likelihood of denial of service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if ICMP redirect messages are ignored. # ipadm show-prop -p _ignore_redirect -co current ipv4 # ipadm show-prop -p _ignore_redirect -co current ipv6 If the output of all commands is not "1", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216138`

### Rule: The system must set strict multihoming.

**Rule ID:** `SV-216138r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These settings control whether a packet arriving on a non-forwarding interface can be accepted for an IP address that is not explicitly configured on that interface. This rule is NA for documented systems that have interfaces that cross strict networking domains (for example, a firewall, a router, or a VPN node).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if strict multihoming is configured. # ipadm show-prop -p _strict_dst_multihoming -co current ipv4 # ipadm show-prop -p _strict_dst_multihoming -co current ipv6 If the output of all commands is not "1", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216139`

### Rule: The system must disable ICMP redirect messages.

**Rule ID:** `SV-216139r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A malicious user can exploit the ability of the system to send ICMP redirects by continually sending packets to the system, forcing the system to respond with ICMP redirect messages, resulting in an adverse impact on the CPU performance of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the version of Solaris 11 in use. # cat /etc/release If the version of Solaris is earlier than Solaris 11.2, determine if ICMP redirect messages are disabled. # ipadm show-prop -p _send_redirects -co current ipv4 # ipadm show-prop -p _send_redirects -co current ipv6 If the output of all commands is not "0", this is a finding. If the version of Solaris is Solaris 11.2 or later, determine if ICMP redirect messages are disabled. # ipadm show-prop -p send_redirects -co current ipv4 # ipadm show-prop -p send_redirects -co current ipv6 If the output of all commands is not "off", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216140`

### Rule: The system must disable TCP reverse IP source routing.

**Rule ID:** `SV-216140r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If enabled, reverse IP source routing would allow an attacker to more easily complete a three-way TCP handshake and spoof new connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if TCP reverse IP source routing is disabled. # ipadm show-prop -p _rev_src_routes -co current tcp If the output of this command is not "0", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216141`

### Rule: The system must set maximum number of half-open TCP connections to 4096.

**Rule ID:** `SV-216141r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls how many half-open connections can exist for a TCP port. It is necessary to control the number of completed connections to the system to provide some protection against denial of service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the number of half open TCP connections is set to 4096. # ipadm show-prop -p _conn_req_max_q0 -co current tcp If the value of "4096" is not returned, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216142`

### Rule: The system must set maximum number of incoming connections to 1024.

**Rule ID:** `SV-216142r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This setting controls the maximum number of incoming connections that can be accepted on a TCP port limiting exposure to denial of service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the maximum number of incoming connections is set to 1024. # ipadm show-prop -p _conn_req_max_q -co current tcp If the value returned is smaller than "1024", this is a finding. In environments where connection numbers are high, such as a busy web server, this value may need to be increased.

## Group: SRG-OS-000480

**Group ID:** `V-216143`

### Rule: The system must disable network routing unless required.

**Rule ID:** `SV-216143r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The network routing daemon, in.routed, manages network routing tables. If enabled, it periodically supplies copies of the system's routing tables to any directly connected hosts and networks and picks up routes supplied to it from other networks and hosts. Routing Internet Protocol (RIP) is a legacy protocol with a number of security weaknesses, including a lack of authentication, zoning, pruning, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if routing is disabled. # routeadm -p | egrep "routing |forwarding" | grep enabled If the command output includes "persistent=enabled" or "current=enabled", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216144`

### Rule: The system must implement TCP Wrappers.

**Rule ID:** `SV-216144r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>TCP Wrappers is a host-based access control system that allows administrators to control who has access to various network services based on the IP address of the remote end of the connection. TCP Wrappers also provides logging information via syslog about both successful and unsuccessful connections. TCP Wrappers provides granular control over what services can be accessed over the network. Its logs show attempted access to services from non-authorized systems, which can help identify unauthorized access attempts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if TCP Wrappers is configured. # inetadm -p | grep tcp_wrappers If the output of this command is "FALSE", this is a finding. The above command will check whether TCP Wrappers is enabled for all TCP-based services started by inetd. TCP Wrappers are enabled by default for sendmail and SunSSH (version 0.5.11). The use of OpenSSH access is controlled by the sshd_config file starting with Solaris 11.3. SunSSH is removed starting with Solaris 11.4. Individual inetd services may still be configured to use TCP Wrappers even if the global parameter (above) is set to "FALSE". To check the status of individual inetd services, use the command: # for svc in `inetadm | awk '/svc:\// { print $NF }'`; do val=`inetadm -l ${svc} | grep -c tcp_wrappers=TRUE` if [ ${val} -eq 1 ]; then echo "TCP Wrappers enabled for ${svc}" fi done If the required services are not configured to use TCP Wrappers, this is finding. # ls /etc/hosts.deny # ls /etc/hosts.allow If these files are not found, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216150`

### Rule: The boundary protection system (firewall) must be configured to deny network traffic by default and must allow network traffic by exception (i.e., deny all, permit by exception).

**Rule ID:** `SV-216150r1045457_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall that relies on a deny all, permit by exception strategy requires all traffic to have explicit permission before traversing an interface on the host. The firewall must incorporate stateful packet filtering and logging. Nonlocal maintenance and diagnostic communications often contain sensitive information and must be protected. The security of these remote accesses can be ensured by sending nonlocal maintenance and diagnostic communications through encrypted channels enforced via firewall configurations. Satisfies: SRG-OS-000074, SRG-OS-000096, SRG-OS-000112, SRG-OS-000113, SRG-OS-000125, SRG-OS-000250, SRG-OS-000393</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that either the IP Filter or Packet Filter Firewall is installed correctly. Determine the OS version to be secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3, which use IP Filter, the IP Filter Management profile is required. Check that the IP Filter firewall is enabled and configured so that only authorized sessions are allowed. # svcs ipfilter If "ipfilter" is not listed with a state of "online", this is a finding. The IP Filter Management profile is required. Check that the filters are configured properly. # ipfstat -io If the output of this command does not include the following lines, this is a finding. block out log all keep state keep frags block in log all block in log from any to 255.255.255.255/32 block in log from any to 127.0.0.1/32 Even if the lines above are included in the output, it is possible that other lines can contradict the firewall settings. Review the firewall rules and ensure that they conform to organizational and mission requirements. If the firewall rules are not configured to organizational standards, this is a finding. For Solaris 11.3 or newer, which use Packet Filter, the Network Firewall Management rights profile is required. Check that the Packet Filter firewall is enabled and configured so that only authorized sessions are allowed. # svcs firewall:default If "firewall" is not listed with a state of "online", this is a finding. The Network Firewall Management rights profile is required. Check that the filters are configured properly. # pfctl -s rules If the output of this command does not include a line to block and log all traffic as in the following line, this is a finding (does not have to be exactly like the example). block drop log (to pflog0) all Check that the Packet Filter firewall logging daemon is enabled. svcs firewall/pflog:default If "pflog" is not listed with a state of "online", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216157`

### Rule: The system must prevent local applications from generating source-routed packets.

**Rule ID:** `SV-216157r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the OS version you are currently securing. # uname –v Solaris 11, 11.1, 11.2, and 11.3 use IP Filter. To continue checking IP Filter, the IP Filter Management profile is required. Check the system for an IPF rule blocking outgoing source-routed packets. # ipfstat -o Examine the list for rules such as: block out log quick from any to any with opt lsrr block out log quick from any to any with opt ssrr If the listed rules do not block both lsrr and ssrr options, this is a finding. For Solaris 11.3 or newer that use Packet Filter, the Network Firewall Management rights profile is required. Ensure that IP Options are not in use: # pfctl -s rules | grep allow-opts If any output is returned, this is a finding.

## Group: SRG-OS-000023

**Group ID:** `V-216158`

### Rule: The operating system must display the DoD approved system use notification message or banner before granting access to the system for general system logons.

**Rule ID:** `SV-216158r958390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Warning messages inform users who are attempting to log in to the system of their legal status regarding the system and must include the name of the organization that owns the system and any monitoring policies that are in place. As implementing a logon banner to deter inappropriate use can provide a foundation for legal action against abuse, this warning content should be set as appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the contents of these two files and check that the proper DoD banner message is configured. # cat /etc/motd # cat /etc/issue If the DoD-approved banner text is not in the files, this is a finding.

## Group: SRG-OS-000023

**Group ID:** `V-216159`

### Rule: The operating system must display the DoD approved system use notification message or banner for SSH connections.

**Rule ID:** `SV-216159r958390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Warning messages inform users who are attempting to log in to the system of their legal status regarding the system and must include the name of the organization that owns the system and any monitoring policies that are in place. As implementing a logon banner to deter inappropriate use can provide a foundation for legal action against abuse, this warning content should be set as appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SSH configuration for banner message: # grep "^Banner" /etc/ssh/sshd_config If the output is not: Banner /etc/issue and /etc/issue does not contain the approved banner text, this is a finding.

## Group: SRG-OS-000023

**Group ID:** `V-216160`

### Rule: The GNOME service must display the DoD approved system use notification message or banner before granting access to the system.

**Rule ID:** `SV-216160r958390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Warning messages inform users who are attempting to log in to the system of their legal status regarding the system and must include the name of the organization that owns the system and any monitoring policies that are in place. As implementing a logon banner to deter inappropriate use can provide a foundation for legal action against abuse, this warning content should be set as appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This item does not apply if a graphic login is not configured. Log in to the Gnome Graphical interface. If the approved banner message does not appear, this is a finding. # cat /etc/issue # grep /etc/gdm/Init/Default zenity If /etc/issue does not contain that DoD-approved banner message or /etc/gdm/Init/Default does not contain the line: /usr/bin/zenity --text-info --width=800 --height=300 \ --title="Security Message" --filename=/etc/issue this is a finding.

## Group: SRG-OS-000023

**Group ID:** `V-216161`

### Rule: The FTP service must display the DoD approved system use notification message or banner before granting access to the system.

**Rule ID:** `SV-216161r958390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Warning messages inform users who are attempting to log in to the system of their legal status regarding the system and must include the name of the organization that owns the system and any monitoring policies that are in place. As implementing a logon banner to deter inappropriate use can provide a foundation for legal action against abuse, this warning content should be set as appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the FTP server package is installed: # pkg list service/network/ftp If the package is not installed, this check does not apply. # grep DisplayConnect /etc/proftpd.conf If: DisplayConnect /etc/issue does not appear, this is a finding. If /etc/issue does not contain the approved DoD text, this is a finding.

## Group: SRG-OS-000126

**Group ID:** `V-216162`

### Rule: The operating system must terminate all sessions and network connections when nonlocal maintenance is completed.

**Rule ID:** `SV-216162r986457_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. The operating system needs to ensure all sessions and network connections are terminated when nonlocal maintenance is completed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if SSH is configured to disconnect sessions after 10 minutes of inactivity. # grep ClientAlive /etc/ssh/sshd_config If the output of this command is not as shown below, this is a finding. ClientAliveInterval 600 ClientAliveCountMax 0

## Group: SRG-OS-000480

**Group ID:** `V-216163`

### Rule: The operating system must prevent internal users from sending out packets which attempt to manipulate or spoof invalid IP addresses.

**Rule ID:** `SV-216163r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Manipulation of IP addresses can allow untrusted systems to appear as trusted hosts, bypassing firewall and other security mechanism and resulting in system penetration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the zone that you are currently securing. # zonename If the command output is "global", then only the "phys" and "SR-IOV" interfaces assigned to the global zone require inspection. If using a non-Global zone, then all "phys" and "SR-IOV" interfaces assigned to the zone require inspection. Identify if this system has physical interfaces. # dladm show-link -Z | grep -v vnic LINK ZONE CLASS MTU STATE OVER net0 global phys 1500 unknown -- e1000g0 global phys 1500 up -- e1000g1 global phys 1500 up -- zoneD/net2 zoneD iptun 65515 up -- If "phys" appears in the third column, then the interface is physical. For each physical interface, determine if the network interface is Ethernet or InfiniBand: # dladm show-phys [interface name] LINK MEDIA STATE SPEED DUPLEX DEVICE [name] Ethernet unknown 0 half dnet0 The second column indicates either "Ethernet" or "Infiniband". For each physical interface, determine if the host is using ip-forwarding: # ipadm show-ifprop [interface name] | grep forwarding [name] forwarding ipv4 rw off -- off on,off [name] forwarding ipv6 rw off -- off on,off If "on" appears in the fifth column, then the interface is using ip-forwarding. For each interface, determine if the host is using SR-IOV’s Virtual Function (VF) driver: # dladm show-phys [interface name] | grep vf If the sixth column includes 'vf' in its name, it is using SR-IOV (ex: ixgbevf0). For each physical and SR-IOV interface, determine if network link protection capabilities are enabled. # dladm show-linkprop -p protection LINK PROPERTY PERM VALUE DEFAULT POSSIBLE net0 protection rw mac-nospoof, -- mac-nospoof, restricted, restricted, ip-nospoof, ip-nospoof, dhcp-nospoof dhcp-nospoof If the interface uses Infiniband and if restricted, ip-nospoof, and dhcp-nospoof do not appear in the "VALUE" column, this is a finding. If the interface uses ip-forwarding and if mac-nospoof, restricted, and dhcp-nospoof do not appear in the "VALUE" column, this is a finding. If the interface uses SR-IOV and if mac-nospoof, restricted, and dhcp-nospoof do not appear in the "VALUE" column, this is a finding. If the interface uses Ethernet without IP forwarding and if mac-nospoof, restricted, ip-nospoof, and dhcp-nospoof do not appear in the "VALUE" column, this is a finding.

## Group: SRG-OS-000481

**Group ID:** `V-216164`

### Rule: Wireless network adapters must be disabled.

**Rule ID:** `SV-216164r958358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of wireless networking can introduce many different attack vectors into the organization’s network. Common attack vectors such as malicious association and ad hoc networks will allow an attacker to spoof a wireless access point (AP), allowing validated systems to connect to the malicious AP and enabling the attacker to monitor and record network traffic. These malicious APs can also serve to create a man-in-the-middle attack or be used to create a denial-of-service to valid network resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is N/A for systems that do not have wireless network adapters. Verify that there are no wireless interfaces configured on the system: # ifconfig -a eth0 Link encap:Ethernet HWaddr b8:ac:6f:65:31:e5 inet addr:192.168.2.100 Bcast:192.168.2.255 Mask:255.255.255.0 inet6 addr: fe80::baac:6fff:fe65:31e5/64 Scope:Link UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1 RX packets:2697529 errors:0 dropped:0 overruns:0 frame:0 TX packets:2630541 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 RX bytes:2159382827 (2.0 GiB) TX bytes:1389552776 (1.2 GiB) Interrupt:17 lo Link encap:Local Loopback inet addr:127.0.0.1 Mask:255.0.0.0 inet6 addr: ::1/128 Scope:Host UP LOOPBACK RUNNING MTU:16436 Metric:1 RX packets:2849 errors:0 dropped:0 overruns:0 frame:0 TX packets:2849 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:0 RX bytes:2778290 (2.6 MiB) TX bytes:2778290 (2.6 MiB) If a wireless interface is configured, it must be documented and approved by the local Authorizing Official. If a wireless interface is configured and has not been documented and approved, this is a finding.

## Group: SRG-OS-000481

**Group ID:** `V-216165`

### Rule: The operating system must use mechanisms for authentication to a cryptographic module meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for such authentication.

**Rule ID:** `SV-216165r958358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified, and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. Applications utilizing encryption are required to use approved encryption modules meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance. FIPS 140-2 is the current standard for validating cryptographic modules, and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified hardware based encryption modules. Satisfies: SRG-OS-000120, SRG-OS-000169</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. The Crypto Management profile is required to execute this command. Check to ensure that FIPS-140 encryption mode is enabled. # cryptoadm list fips-140| grep -c "is disabled" If the output of this command is not "0", this is a finding.

## Group: SRG-OS-000033

**Group ID:** `V-216173`

### Rule: The operating system must implement DoD-approved encryption to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-216173r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access is any access to an organizational information system by a user (or an information system) communicating through an external, non-organization-controlled network (e.g., the Internet). Examples of remote access methods include dial-up, broadband, and wireless. Using cryptography ensures confidentiality of the remote access connections. The system will attempt to use the first cipher presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest cipher available to secure the SSH connection. Note: SSH in Solaris 11.GA-11.3 used Sun Microsystem’s proprietary SUNWssh. In Solaris 11.3 OpenSSH was offered as optional software and in Solaris 11.4 OpenSSH is the only SSH offered. Both use the same /etc/ssh/sshd_config file and both, by default do not include the ciphers line.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed ciphers. # grep -i ciphers /etc/ssh/sshd_config | grep -v '^#’ Ciphers aes256-ctr,aes192-ctr,aes128-ctr If any ciphers other than "aes256-ctr", "aes192-ctr", or "aes128-ctr" are listed, the order differs from the example above, the "Ciphers" keyword is missing, or is commented out, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216174`

### Rule: The operating system must use cryptographic mechanisms to protect and restrict access to information on portable digital media.

**Rule ID:** `SV-216174r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When data is written to portable digital media, such as thumb drives, floppy diskettes, compact disks, and magnetic tape, etc., there is risk of data loss. An organizational assessment of risk guides the selection of media and associated information contained on the media requiring restricted access. Organizations need to document in policy and procedures the media requiring restricted access, individuals authorized to access the media, and the specific measures taken to restrict access. Fewer protection measures are needed for media containing information determined by the organization to be in the public domain, to be publicly releasable, or to have limited or no adverse impact if accessed by other than authorized personnel. In these situations, it is assumed the physical access controls where the media resides provide adequate protection. The employment of cryptography is at the discretion of the information owner/steward. When the organization has determined the risk warrants it, data written to portable digital media must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the logical node of all attached removable media: # rmformat This command lists all attached removable devices. Note the device logical node name. For example: /dev/rdsk/c8t0d0p0 Determine which zpool is mapped to the device: # zpool status Determine the file system names of the portable digital media: # zfs list | grep [poolname] Using the file system name, determine if the removal media is encrypted: # zfs get encryption [filesystem] If "encryption off" is listed, this is a finding.

## Group: SRG-OS-000185

**Group ID:** `V-216176`

### Rule: The operating system must protect the confidentiality and integrity of information at rest.

**Rule ID:** `SV-216176r958552_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When data is written to digital media, such as hard drives, mobile computers, external/removable hard drives, personal digital assistants, flash/thumb drives, etc., there is risk of data loss and data compromise. An organizational assessment of risk guides the selection of media and associated information contained on the media requiring restricted access. Organizations need to document in policy and procedures the media requiring restricted access, individuals authorized to access the media, and the specific measures taken to restrict access. Fewer protection measures are needed for media containing information determined by the organization to be in the public domain, to be publicly releasable, or to have limited or no adverse impact if accessed by other than authorized personnel. In these situations, it is assumed the physical access controls where the media resides provide adequate protection. As part of a defense-in-depth strategy, the organization considers routinely encrypting information at rest on selected secondary storage devices. The employment of cryptography is at the discretion of the information owner/steward. The selection of the cryptographic mechanisms used is based upon maintaining the confidentiality and integrity of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if file system encryption is required by your organization. If not required, this item does not apply. Determine if file system encryption is enabled for user data sets. This check does not apply to the root, var, share, swap or dump datasets. # zfs list Using the file system name, determine if the file system is encrypted: # zfs get encryption [filesystem] If "encryption off" is listed, this is a finding.

## Group: SRG-OS-000216

**Group ID:** `V-216178`

### Rule: The operating system must use cryptographic mechanisms to protect the integrity of audit information.

**Rule ID:** `SV-216178r958576_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Protection of audit records and audit data is of critical importance. Cryptographic mechanisms are the industry established standard used to protect the integrity of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration and the Audit Control profiles are required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine if audit log encryption is required by your organization. If not required, this check does not apply. Determine where the audit logs are stored and whether the file system is encrypted. # pfexec auditconfig -getplugin audit_binfile The p_dir attribute lists the location of the audit log filesystem. The default location for Solaris 11.1 is /var/audit. /var/audit is a link to /var/share/audit which, by default, is mounted on rpool/VARSHARE. Determine if this is encrypted: # zfs get encryption rpool/VARSHARE If the file system where audit logs are stored reports "encryption off", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216180`

### Rule: The sticky bit must be set on all world writable directories.

**Rule ID:** `SV-216180r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files in directories that have had the "sticky bit" enabled can only be deleted by users that have both write permissions for the directory in which the file resides, as well as ownership of the file or directory, or have sufficient privileges. As this prevents users from overwriting each others' files, whether it be accidental or malicious, it is generally appropriate for most world-writable directories (e.g., /tmp).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Identify all world-writable directories without the "sticky bit" set. # find / \( -fstype nfs -o -fstype cachefs -o -fstype autofs \ -o -fstype ctfs -o -fstype mntfs -o -fstype objfs \ -o -fstype proc \) -prune -o -type d \( -perm -0002 \ -a ! -perm -1000 \) -ls Output of this command identifies world-writable directories without the "sticky bit" set. If output is created, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216181`

### Rule: Permissions on user home directories must be 750 or less permissive.

**Rule ID:** `SV-216181r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Group-writable or world-writable user home directories may enable malicious users to steal or modify other users' data or to gain another user's system privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check that the permissions on users' home directories are 750 or less permissive. # for dir in `logins -ox |\ awk -F: '($8 == "PS") { print $6 }'`; do find ${dir} -type d -prune \( -perm -g+w -o \ -perm -o+r -o -perm -o+w -o -perm -o+x \) -ls done If output is created, this is finding.

## Group: SRG-OS-000480

**Group ID:** `V-216182`

### Rule: Permissions on user . (hidden) files must be 750 or less permissive.

**Rule ID:** `SV-216182r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Group-writable or world-writable user configuration files may enable malicious users to steal or modify other users' data or to gain another user's system privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Ensure that the permissions on user "." files are 750 or less permissive. # for dir in \ `logins -ox | awk -F: '($8 == "PS") { print $6 }'`; do find ${dir}/.[A-Za-z0-9]* \! -type l \ \( -perm -0001 -o -perm -0002 -o -perm -0004 -o -perm -0020 \) -ls done If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216183`

### Rule: Permissions on user .netrc files must be 750 or less permissive.

**Rule ID:** `SV-216183r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.netrc files may contain unencrypted passwords that can be used to attack other systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check that permissions on user .netrc files are 750 or less permissive. # for dir in \ `logins -ox | awk -F: '($8 == "PS") { print $6 }'`; do find ${dir}/.netrc -type f \( \ -perm -g+r -o -perm -g+w -o -perm -g+x -o \ -perm -o+r -o -perm -o+w -o -perm -o+x \) \ -ls 2>/dev/null done If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216184`

### Rule: There must be no user .rhosts files.

**Rule ID:** `SV-216184r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Even though the .rhosts files are ineffective if support is disabled in /etc/pam.conf, they may have been brought over from other systems and could contain information useful to an attacker for those other systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check for the presence of .rhosts files. # for dir in \ `logins -ox | awk -F: '($8 == "PS") { print $6 }'`; do find ${dir}/.rhosts -type f -ls 2>/dev/null done If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216185`

### Rule: Groups assigned to users must exist in the /etc/group file.

**Rule ID:** `SV-216185r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Groups defined in passwd but not in group file pose a threat to system security since group permissions are not properly managed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check that groups are configured correctly. # logins -xo | awk -F: '($3 == "") { print $1 }' If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216186`

### Rule: Users must have a valid home directory assignment.

**Rule ID:** `SV-216186r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>All users must be assigned a home directory in the passwd file. Failure to have a home directory may result in the user being put in the root directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Determine if each user has a valid home directory. # logins -xo | while read line; do user=`echo ${line} | awk -F: '{ print $1 }'` home=`echo ${line} | awk -F: '{ print $6 }'` if [ -z "${home}" ]; then echo ${user} fi done If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216187`

### Rule: All user accounts must be configured to use a home directory that exists.

**Rule ID:** `SV-216187r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the user's home directory does not exist, the user will be placed in "/" and will not be able to write any files or have local environment variables set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check if a GUI is installed. Determine the OS version you are currently securing:. # uname –v For Solaris 11, 11.1, 11.2, and 11.3: # pkg info gdm # pkg info coherence-26 # pkg info coherence-27 If none of these packages are installed on the system, then no GUI is present. For Solaris 11.4 or newer: # pkg info gdm If gdm is not installed on the system, then no GUI is present. # pkg info uucp uucp is no longer installed by default starting in 11.4 and is deprecated. For all versions, check that all users' home directories exist. # pwck Accounts with no home directory will output "Login directory not found". If no GUI is present, then "gdm" and "upnp" accounts should generate errors. On all systems, with uucp package installed, the "uucp" and "nuucp" accounts should generate errors. If users' home directories do not exist, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216188`

### Rule: All home directories must be owned by the respective user assigned to it in /etc/passwd.

**Rule ID:** `SV-216188r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the user is accountable for files stored in the user's home directory, the user must be the owner of the directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check that home directories are owned by the correct user. # export IFS=":"; logins -uxo | while read user uid group gid gecos home rest; do result=$(find ${home} -type d -prune \! -user $user -print 2>/dev/null); if [ ! -z "${result}" ]; then echo "User: ${user}\tOwner: $(ls -ld $home | awk '{ print $3 }')"; fi; done If any output is produced, this is a finding.

## Group: SRG-OS-000104

**Group ID:** `V-216189`

### Rule: Duplicate User IDs (UIDs) must not exist for users within the organization.

**Rule ID:** `SV-216189r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users within the organization must be assigned unique UIDs for accountability and to ensure appropriate access protections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check that there are no duplicate UIDs. # logins -d If output is produced, this is a finding.

## Group: SRG-OS-000121

**Group ID:** `V-216190`

### Rule: Duplicate UIDs must not exist for multiple non-organizational users.

**Rule ID:** `SV-216190r958504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users must be assigned unique UIDs for accountability and to ensure appropriate access protections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check that there are no duplicate UIDs. # logins -d If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216191`

### Rule: Duplicate Group IDs (GIDs) must not exist for multiple groups.

**Rule ID:** `SV-216191r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User groups must be assigned unique GIDs for accountability and to ensure appropriate access protections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check that group IDs are unique. # getent group | cut -f3 -d":" | sort -n | uniq -c |\ while read x ; do [ -z "${x}" ] && break set - $x if [ $1 -gt 1 ]; then grps=`getent group | nawk -F: '($3 == n) { print $1 }' n=$2 | xargs` echo "Duplicate GID ($2): ${grps}" fi done If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216192`

### Rule: Reserved UIDs 0-99 must only be used by system accounts.

**Rule ID:** `SV-216192r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is assigned a UID that is in the reserved range, even if it is not presently in use, security exposures can arise if a subsequently installed application uses the same UID.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check that reserved UIDs are not assigned to non-system users. Determine the OS version you are currently securing: # uname –v For Solaris 11, 11.1, 11.2, and 11.3: # logins -so | awk -F: '{ print $1 }' | while read user; do found=0 for tUser in root daemon bin sys adm dladm netadm netcfg \ ftp dhcpserv sshd smmsp gdm zfssnap aiuser \ polkitd ikeuser lp openldap webservd unknown \ uucp nuucp upnp xvm mysql postgres svctag \ pkg5srv nobody noaccess nobody4; do if [ ${user} = ${tUser} ]; then found=1 fi done if [ $found -eq 0 ]; then echo "Invalid User with Reserved UID: ${user}" fi done If output is produced without justification and documentation in accordance with site policy, this is a finding. For Solaris 11.4 or newer: # logins -so | awk -F: '{ print $1 }' | while read user; do found=0 for tUser in root daemon bin sys adm dladm netadm \ netcfg dhcpserv sshd smmsp gdm zfssnap aiuser _polkitd \ ikeuser lp openldap webservd unknown \ uucp nuucp upnp xvm mysql postgres svctag \ pkg5srv nobody noaccess nobody4 _ntp; do if [ ${user} = ${tUser} ]; then found=1 fi done if [ $found -eq 0 ]; then echo "Invalid User with Reserved UID: ${user}" fi done If output is produced without justification and documentation in accordance with site policy, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216193`

### Rule: Duplicate user names must not exist.

**Rule ID:** `SV-216193r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is assigned a duplicate user name, it will create and have access to files with the first UID for that username in passwd.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Identify any duplicate user names. # getent passwd | awk -F: '{print $1}' | uniq -d If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216194`

### Rule: Duplicate group names must not exist.

**Rule ID:** `SV-216194r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a group is assigned a duplicate group name, it will create and have access to files with the first GID for that group in group. Effectively, the GID is shared, which is a security risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check for duplicate group names. # getent group | cut -f1 -d":" | sort -n | uniq -d If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216195`

### Rule: User .netrc files must not exist.

**Rule ID:** `SV-216195r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The .netrc file presents a significant security risk since it stores passwords in unencrypted form.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check for the presence of user .netrc files. # for dir in \ `logins -ox | awk -F: '($8 == "PS") { print $6 }'`; do ls -l ${dir}/.netrc 2>/dev/null done If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216196`

### Rule: The system must not allow users to configure .forward files.

**Rule ID:** `SV-216196r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of the .forward file poses a security risk in that sensitive data may be inadvertently transferred outside the organization. The .forward file also poses a secondary risk as it can be used to execute commands that may perform unintended actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. # for dir in \ `logins -ox | awk -F: '($8 == "PS") { print $6 }'`; do ls -l ${dir}/.forward 2>/dev/null done If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216197`

### Rule: World-writable files must not exist.

**Rule ID:** `SV-216197r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data in world-writable files can be read, modified, and potentially compromised by any user on the system. World-writable files may also indicate an incorrectly written script or program that could potentially be the cause of a larger compromise to the system's integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check for the existence of world-writable files. # find / \( -fstype nfs -o -fstype cachefs -o -fstype autofs \ -o -fstype ctfs -o -fstype mntfs -o -fstype objfs \ -o -fstype proc \) -prune -o -type f -perm -0002 -print If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216198`

### Rule: All valid SUID/SGID files must be documented.

**Rule ID:** `SV-216198r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>There are valid reasons for SUID/SGID programs, but it is important to identify and review such programs to ensure they are legitimate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. # find / \( -fstype nfs -o -fstype cachefs -o -fstype autofs \ -o -fstype ctfs -o -fstype mntfs -o -fstype objfs \ -o -fstype proc \) -prune -o -type f -perm -4000 -o \ -perm -2000 -print Output should only be Solaris-provided files and approved customer files. Solaris-provided SUID/SGID files can be listed using the command: # pkg contents -a mode=4??? -a mode=2??? -t file -o pkg.name,path,mode Digital signatures on the Solaris Set-UID binaries can be verified with the elfsign utility, such as this example: # elfsign verify -e /usr/bin/su elfsign: verification of /usr/bin/su passed. This message indicates that the binary is properly signed. If non-vendor provided or non-approved files are included in the list, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216199`

### Rule: The operating system must have no unowned files.

**Rule ID:** `SV-216199r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A new user who is assigned a deleted user's user ID or group ID may then end up owning these files, and thus have more access on the system than was intended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Identify all files that are owned by a user or group not listed in /etc/passwd or /etc/group # find / \( -fstype nfs -o -fstype cachefs -o -fstype autofs \ -o -fstype ctfs -o -fstype mntfs -o -fstype objfs \ -o -fstype proc \) -prune \( -nouser -o -nogroup \) -ls If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216200`

### Rule: The operating system must have no files with extended attributes.

**Rule ID:** `SV-216200r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Attackers or malicious users could hide information, exploits, etc. in extended attribute areas. Since extended attributes are rarely used, it is important to find files with extended attributes set and correct these attributes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Identify all files with extended attributes. # find / \( -fstype nfs -o -fstype cachefs -o -fstype autofs \ -o -fstype ctfs -o -fstype mntfs -o -fstype objfs \ -o -fstype proc \) -prune -o -xattr -ls If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216201`

### Rule: The root account must be the only account with GID of 0.

**Rule ID:** `SV-216201r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All accounts with a GID of 0 have root group privileges and must be limited to the group account only.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify any users with GID of 0. # awk -F: '$4 == 0' /etc/passwd # awk -F: '$3 == 0' /etc/group Confirm the only account with a group id of 0 is root. If the root account is not the only account with GID of 0, this is a finding.

## Group: SRG-OS-000206

**Group ID:** `V-216202`

### Rule: The operating system must reveal error messages only to authorized personnel.

**Rule ID:** `SV-216202r958566_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Proper file permissions and ownership ensures that only designated personnel in the organization can access error messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the /var/adm/messages file: # ls -l /var/adm/messages Check the permissions of the /var/adm directory: # ls -ld /var/adm If the owner and group of /var/adm/messages is not root and the permissions are not 640, this is a finding. If the owner of /var/adm is not root, group is not sys, and the permissions are not 750, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216204`

### Rule: The operator must document all file system objects that have non-standard access control list settings.

**Rule ID:** `SV-216204r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access Control Lists allow an object owner to expand permissions on an object to specific users and groups in addition to the standard permission model. Non-standard Access Control List settings can allow unauthorized users to modify critical files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Identify all file system objects that have non-standard access control lists enabled. # find / \( -fstype nfs -o -fstype cachefs -o -fstype autofs \ -o -fstype ctfs -o -fstype mntfs -o -fstype objfs \ -o -fstype proc \) -prune -o -acl -ls This command should return no output. If output is created, this is a finding. If the files are approved to have ACLs by organizational security policy, document the files and the reason that ACLs are required.

## Group: SRG-OS-000480

**Group ID:** `V-216205`

### Rule: The operating system must be a supported release.

**Rule ID:** `SV-216205r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An operating system release is considered supported if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the operating system version. # uname -a If the release is not supported by the vendor, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216206`

### Rule: The system must implement non-executable program stacks.

**Rule ID:** `SV-216206r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common type of exploit is the stack buffer overflow. An application receives, from an attacker, more data than it is prepared for and stores this information on its stack, writing beyond the space reserved for it. This can be designed to cause execution of the data written on the stack. One mechanism to mitigate this vulnerability is for the system to not allow the execution of instructions in sections of memory identified as part of the stack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the OS version you are currently securing. # uname –v If the OS version is 11.3 or newer, this check applies to all zones and relies on the "sxadm" command. Determine if the system implements non-executable program stacks. # sxadm status -p nxstack | cut -d: -f2 enabled.all If the command output is not "enabled.all", this is a finding. For Solaris 11, 11.1, and 11.2, this check applies to the global zone only and the "/etc/system" file is inspected. Determine the zone that you are currently securing. # zonename If the command output is "global", determine if the system implements non-executable program stacks. # grep noexec_user_stack /etc/system If the noexec_user_stack is not set to 1, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216207`

### Rule: Address Space Layout Randomization (ASLR) must be enabled.

**Rule ID:** `SV-216207r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Modification of memory area can result in executable code vulnerabilities. ASLR can reduce the likelihood of these attacks. ASLR activates the randomization of key areas of the process such as stack, brk-based heap, memory mappings, and so forth.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine if address space layout randomization is enabled. Determine the OS version you are currently securing:. # uname –v For Solaris 11, 11.1, 11.2, and 11.3: # sxadm info -p | grep aslr | grep enabled For Solaris 11.4 or newer: # sxadm status -p -o status aslr | grep enabled If no output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216208`

### Rule: Process core dumps must be disabled unless needed.

**Rule ID:** `SV-216208r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Process core dump files can be of significant size and their use can result in file systems filling to capacity, which may result in denial of service. Process core dumps can be useful for software debugging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the process core dump configuration. # coreadm | grep enabled If any lines are returned by coreadm other than "logging", this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216209`

### Rule: The system must be configured to store any process core dumps in a specific, centralized directory.

**Rule ID:** `SV-216209r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Specifying a centralized location for core file creation allows for the centralized protection of core files. Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If process core dump creation is not configured to use a centralized directory, core dumps may be created in a directory that does not have appropriate ownership or permissions configured, which could result in unauthorized access to the core dumps.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the defined directory for process core dumps: # coreadm | grep "global core file pattern" If the parameter is not set, or is not an absolute path (does not start with a slash [/]), this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216210`

### Rule: The centralized process core dump data directory must be owned by root.

**Rule ID:** `SV-216210r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If the centralized process core dump data directory is not owned by root, the core dumps contained in the directory may be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the defined directory for process core dumps. # coreadm | grep "global core file pattern" Check the ownership of the directory. # ls -lLd [core file directory] If the directory is not owned by root, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216211`

### Rule: The centralized process core dump data directory must be group-owned by root, bin, or sys.

**Rule ID:** `SV-216211r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If the centralized process core dump data directory is not group-owned by a system group, the core dumps contained in the directory may be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the defined directory for process core dumps. # coreadm | grep "global core file pattern" Check the group ownership of the directory. # ls -lLd [core file directory] If the directory is not group-owned by root, bin, or sys, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216212`

### Rule: The centralized process core dump data directory must have mode 0700 or less permissive.

**Rule ID:** `SV-216212r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Process core dumps contain the memory in use by the process when it crashed. Any data the process was handling may be contained in the core file, and it must be protected accordingly. If the process core dump data directory has a mode more permissive than 0700, unauthorized users may be able to view or to modify sensitive information contained in any process core dumps in the directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the defined directory for process core dumps. # coreadm | grep "global core file pattern" Check the permissions of the directory. # ls -lLd [core file directory] If the directory has a mode more permissive than 0700 (rwx --- ---), this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216213`

### Rule: Kernel core dumps must be disabled unless needed.

**Rule ID:** `SV-216213r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system. The kernel core dump process may increase the amount of time a system is unavailable due to a crash. Kernel core dumps can be useful for kernel debugging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Verify savecore is not used. # dumpadm | grep 'Savecore enabled' If the value is yes, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216214`

### Rule: The kernel core dump data directory must be owned by root.

**Rule ID:** `SV-216214r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. As the system memory may contain sensitive information, it must be protected accordingly. If the kernel core dump data directory is not owned by root, the core dumps contained in the directory may be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the location of the system dump directory. # dumpadm | grep directory Check the ownership of the kernel core dump data directory. # ls -ld [savecore directory] If the kernel core dump data directory is not owned by root, this is a finding. In Solaris 11, /var/crash is linked to /var/share/crash.

## Group: SRG-OS-000480

**Group ID:** `V-216215`

### Rule: The kernel core dump data directory must be group-owned by root.

**Rule ID:** `SV-216215r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. As the system memory may contain sensitive information, it must be protected accordingly. If the kernel core dump data directory is not group-owned by a system group, the core dumps contained in the directory may be subject to unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the location of the system dump directory. # dumpadm | grep directory Check ownership of the core dump data directory. # ls -l [savecore directory] If the directory is not group-owned by root, this is a finding. In Solaris 11, /var/crash is linked to /var/share/crash.

## Group: SRG-OS-000480

**Group ID:** `V-216216`

### Rule: The kernel core dump data directory must have mode 0700 or less permissive.

**Rule ID:** `SV-216216r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. As the system memory may contain sensitive information, it must be protected accordingly. If the mode of the kernel core dump data directory is more permissive than 0700, unauthorized users may be able to view or to modify kernel core dump data files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the location of the system dump directory. # dumpadm | grep directory Check the permissions of the kernel core dump data directory. # ls -ld [savecore directory] If the directory has a mode more permissive than 0700 (rwx --- ---), this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216217`

### Rule: System BIOS or system controllers supporting password protection must have administrator accounts/passwords configured, and no others. (Intel)

**Rule ID:** `SV-216217r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A system's BIOS or system controller handles the initial startup of a system and its configuration must be protected from unauthorized modification. When the BIOS or system controller supports the creation of user accounts or passwords, such protections must be used and accounts/passwords only assigned to system administrators. Failure to protect BIOS or system controller settings could result in denial of service or compromise of the system resulting from unauthorized configuration changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to X86 compatible platforms. On systems with a BIOS or system controller, verify a supervisor or administrator password is set. If a password is not set, this is a finding. If the BIOS or system controller supports user-level access in addition to supervisor/administrator access, determine if this access is enabled. If so, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216218`

### Rule: The system must require authentication before allowing modification of the boot devices or menus. Secure the GRUB Menu (Intel).

**Rule ID:** `SV-216218r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The flexibility that GRUB provides creates a security risk if its configuration is modified by an unauthorized user. The failsafe menu entry needs to be secured in the same environments that require securing the systems firmware to avoid unauthorized removable media boots.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to X86 systems only. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. # grep source /rpool/boot/grub/grub.cfg source $prefix/custom.cfg If the output does not contain "source $prefix/custom.cfg" on a line of its own, this is a finding. # grep superusers /rpool/boot/grub/custom.cfg. # grep password_pbkdf2 /rpool/boot/grub/custom.cfg If no superuser name and password are defined, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216219`

### Rule: The operating system must implement transaction recovery for transaction-based systems.

**Rule ID:** `SV-216219r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Recovery and reconstitution constitutes executing an operating system contingency plan comprised of activities to restore essential missions and business functions. Transaction rollback and transaction journaling are examples of mechanisms supporting transaction recovery. While this is typically a database function, operating systems could be transactional in nature with respect to file processing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Solaris 11 ZFS copy-on-write model allows filesystem accesses to work according to a transactional model, such that on-disk content is always consistent and cannot be configured to be out of compliance. Determine if any UFS file systems are mounted with the "nologging" option. # mount|grep nologging If any file systems are listed, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216220`

### Rule: SNMP communities, users, and passphrases must be changed from the default.

**Rule ID:** `SV-216220r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Whether active or not, default SNMP passwords, users, and passphrases must be changed to maintain security. If the service is running with the default authenticators, then anyone can gather data about the system and the network and use the information to potentially compromise the integrity of the system or network(s).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Check the SNMP configuration for default passwords. Locate and examine the SNMP configuration. Procedure: Find any occurrences of the snmpd.conf file delivered with Solaris packages: # pkg search -l -Ho path snmpd.conf | awk '{ print "/"$1 }' # more [filename] Identify any community names or user password configurations. If any community name or password is set to a default value, such as public, private, snmp-trap, or password, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216221`

### Rule: A file integrity baseline must be created, maintained, and reviewed at least weekly to determine if unauthorized changes have been made to important system files located in the root file system.

**Rule ID:** `SV-216221r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A file integrity baseline is a collection of file metadata used to evaluate the integrity of the system. A minimal baseline must contain metadata for all device files, setuid files, setgid files, system libraries, system binaries, and system configuration files. The minimal metadata must consist of the mode, owner, group owner, and modification times. For regular files, metadata must also include file size and a cryptographic hash of the file's contents.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The root role is required. Solaris 11 includes the Basic Account and Reporting Tool (BART), which uses cryptographic-strength checksums and file system metadata to determine changes. By default, the manifest generator catalogs all attributes of all files in the root (/) file system. File systems mounted on the root file system are cataloged only if they are of the same type as the root file system. A Baseline BART manifest may exist in: /var/adm/log/bartlogs/[control manifest filename] If a BART manifest does not exist, this is a finding. At least weekly, create a new BART baseline report. # bart create > /var/adm/log/bartlogs/[new manifest filename] Compare the new report to the previous report to identify any changes in the system baseline. # bart compare /var/adm/log/bartlogs/[baseline manifest filename] /var/adm/log/bartlogs/[new manifest filename] Examine the BART report for changes. If there are changes to system files in /etc that are not approved, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216223`

### Rule: Direct logins must not be permitted to shared, default, application, or utility accounts.

**Rule ID:** `SV-216223r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shared accounts (accounts where two or more people log in with the same user identification) do not provide identification and authentication. There is no way to provide for non-repudiation or individual accountability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Review profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Use the "auditreduce" command to check for multiple accesses to an account # auditreduce -c lo -u [shared_user_name] | praudit -l If users log directly into accounts, rather than using the "su" command from their own named account to access them, this is a finding. Also, ask the SA or the IAO if shared accounts are logged into directly or if users log into an individual account and switch user to the shared account.

## Group: SRG-OS-000480

**Group ID:** `V-216224`

### Rule: The system must not have any unnecessary accounts.

**Rule ID:** `SV-216224r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the system for unnecessary user accounts. # getent passwd Some examples of unnecessary accounts include games, news, gopher, ftp, and lp. If any unnecessary accounts are found, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216225`

### Rule: The operating system must conduct backups of user-level information contained in the operating system per organization-defined frequency to conduct backups consistent with recovery time and recovery point objectives.

**Rule ID:** `SV-216225r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating system backup is a critical step in maintaining data assurance and availability. User-level information is data generated by information system and/or application users. Backups shall be consistent with organizational recovery time and recovery point objectives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The operations staff shall ensure that proper backups are created, tested, and archived. Ask the operator for documentation on the backup procedures implemented. If the backup procedures are not documented then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216226`

### Rule: The operating system must conduct backups of system-level information contained in the information system per organization-defined frequency to conduct backups that are consistent with recovery time and recovery point objectives.

**Rule ID:** `SV-216226r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating system backup is a critical step in maintaining data assurance and availability. System-level information is data generated for/by the host (such as configuration settings) and/or administrative users. Backups shall be consistent with organizational recovery time and recovery point objectives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The operations staff shall ensure that proper backups are created, tested, and archived. Ask the operator for documentation on the backup procedures implemented. If the backup procedures are not documented then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216227`

### Rule: The operating system must conduct backups of operating system documentation including security-related documentation per organization-defined frequency to conduct backups that is consistent with recovery time and recovery point objectives.

**Rule ID:** `SV-216227r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating system backup is a critical step in maintaining data assurance and availability. System documentation is data generated for/by the host (such as logs) and/or administrative users. Backups shall be consistent with organizational recovery time and recovery point objectives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The operations staff shall ensure that proper backups are created, tested, and archived. Ask the operator for documentation on the backup procedures implemented. If the backup procedures are not documented then this is a finding.

## Group: SRG-OS-000181

**Group ID:** `V-216228`

### Rule: The operating system must prevent the execution of prohibited mobile code.

**Rule ID:** `SV-216228r958544_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Decisions regarding the employment of mobile code within operating systems are based on the potential for the code to cause damage to the system if used maliciously. Mobile code technologies include Java, JavaScript, ActiveX, PDF, Postscript, Shockwave movies, Flash animations, and VBScript. Usage restrictions and implementation guidance apply to both the selection and use of mobile code installed on organizational servers and mobile code downloaded and executed on individual workstations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the Firefox package is installed: # pkg list web/browser/firefox If the package is not installed, this check does not apply. If installed, ensure that it is a supported version. # pkg info firefox | grep Version Version: 52.5.2 If the version is not supported, this is a finding. Ensure that Java and JavaScript access by Firefox are disabled. Start Firefox. In the address bar type: about:config In search bar type: javascript.enabled If 'Value" is true, this is a finding In the address bar type: about:addons Click on "I accept the risk" button. Click on "Plugins". If Java is enabled, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216229`

### Rule: The operating system must employ PKI solutions at workstations, servers, or mobile computing devices on the network to create, manage, distribute, use, store, and revoke digital certificates.

**Rule ID:** `SV-216229r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of PKI systems to manage digital certificates, the operating system or other system components may be unable to securely communicate on a network or reliably verify the identity of a user via digital signatures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The operator will ensure that a DoD approved PKI system is installed, configured, and properly operating. Ask the operator to document the PKI software installation and configuration. If the operator is not able to provide a documented configuration for an installed PKI system or if the PKI system is not properly configured, maintained, or used, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216231`

### Rule: The operating system must employ malicious code protection mechanisms at workstations, servers, or mobile computing devices on the network to detect and eradicate malicious code transported by electronic mail, electronic mail attachments, web accesses, removable media, or other common means.

**Rule ID:** `SV-216231r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to minimize potential negative impact to the organization caused by malicious code, it is imperative that malicious code is identified and eradicated prior to entering protected enclaves via operating system entry and exit points. The requirement states that AV and malware protection applications must be used at entry and exit points. For the operating system, this means an anti-virus application must be installed on machines that are the entry and exit points.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The operator will ensure that anti-virus software is installed and operating. If the operator is unable to provide a documented configuration for an installed anti-virus software system or if not properly used, this is a finding.

## Group: SRG-OS-000215

**Group ID:** `V-216233`

### Rule: The operating system must back up audit records at least every seven days onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-216233r958574_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Backing up audit records to a different system or onto separate media than the system being audited on an organizationally defined frequency helps to assure in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. This requirement can be met by the operating system continuously sending records to a centralized logging server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you a currently securing. # zonename If the command output is "global" this check applies. The operator must back up audit records at least every 7 days. If the operator is unable to provide a documented procedure or the documented procedure is not being followed, then this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216234`

### Rule: All manual editing of system-relevant files shall be done using the pfedit command, which logs changes made to the files.

**Rule ID:** `SV-216234r1099908_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Editing a system file with common tools such as vi, emacs, or gedit does not allow the auditing of changes made by an operator. This reduces the capability of determining which operator made security-relevant changes to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the operators if they use vi, emacs, or gedit to make changes to system files. If vi, emacs, or gedit are used to make changes to system files, this is a finding.

## Group: SRG-OS-000142

**Group ID:** `V-216237`

### Rule: The operating system must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of denial of service attacks.

**Rule ID:** `SV-216237r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the case of denial of service attacks, care must be taken when designing the operating system so as to ensure that the operating system makes the best use of system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that you are on the global zone: # zoneadm -z global list global Note: If you see following message, you are not in the global zone: "zoneadm: global: No such zone exists" # dladm show-ether -Z | egrep "LINK|up" LINK PTYPE STATE AUTO SPEED-DUPLEX PAUSE net0 current up yes 1G-f bi Determine the OS version that is being secured: # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # dladm show-linkprop net0 | egrep "LINK|en_" | sort|uniq LINK PROPERTY PERM VALUE EFFECTIVE DEFAULT POSSIBLE net0 en_1000fdx_cap rw 1 1 1 1,0 net0 en_1000hdx_cap r- 0 0 0 1,0 net0 en_100fdx_cap rw 1 1 1 1,0 net0 en_100hdx_cap rw 1 1 1 1,0 net0 en_10fdx_cap rw 1 1 1 1,0 net0 en_10gfdx_cap -- -- -- 0 1,0 net0 en_10hdx_cap rw 1 1 1 1,0 Do the above for all available/connected network adapters. For Solaris 11.4.x.x.x or newer: # dladm show-linkprop -p speed-duplex net0 LINK PROPERTY PERM VALUE EFFECTIVE DEFAULT POSSIBLE net0 speed-duplex rw 1g-f,100m-f, 1g-f,100m-f, 1g-f, 1g-f,100m-f, 100m-h, 100m-h, 100m-f, 100m-h,10m-f, 10m-f,10m-h 10m-f,10m-h 100m-h, 10m-h 10m-f, 10m-h Do the above for all available/connected network adapters. For each link, determine if its current speed-duplex settings VALUE field is appropriate for managing any excess bandwidth capacity based on its POSSIBLE settings field; if not, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216238`

### Rule: The /etc/zones directory, and its contents, must have the vendor default owner, group, and permissions.

**Rule ID:** `SV-216238r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Incorrect ownership can result in unauthorized changes or theft of data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the ownership of the files and directories. # pkg verify system/zones The command should return no output. If output is produced, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216239`

### Rule: The limitpriv zone option must be set to the vendor default or less permissive.

**Rule ID:** `SV-216239r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Solaris zones can be assigned privileges generally reserved for the global zone using the "limitpriv" zone option. Any privilege assignments in excess of the vendor defaults may provide the ability for a non-global zone to compromise the global zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. List the non-global zones on the system. # zoneadm list -vi | grep -v global From the output list of non-global zones found, determine if any are Kernel zones. # zoneadm list -cv | grep [zonename] | grep solaris-kz Exclude any Kernel zones found from the list of local zones. List the configuration for each zone. # zonecfg -z [zonename] info |grep limitpriv If the output of this command has a setting for limitpriv and it is not: limitpriv: default this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216240`

### Rule: The systems physical devices must not be assigned to non-global zones.

**Rule ID:** `SV-216240r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Solaris non-global zones can be assigned physical hardware devices. This increases the risk of such a non-global zone having the capability to compromise the global zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. List the non-global zones on the system. # zoneadm list -vi | grep -v global List the configuration for each zone. # zonecfg -z [zonename] info | grep dev Check for device lines. If such a line exists and is not approved by security, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216241`

### Rule: The audit system must identify in which zone an event occurred.

**Rule ID:** `SV-216241r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Tracking the specific Solaris zones in the audit trail reduces the time required to determine the cause of a security event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. List the non-global zones on the system. # zoneadm list -vi | grep -v global The Audit Configuration profile is required. Determine whether the "zonename" auditing policy is in effect. # pfexec auditconfig -getpolicy | grep active | grep zonename If no output is returned, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216242`

### Rule: The audit system must maintain a central audit trail for all zones.

**Rule ID:** `SV-216242r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Centralized auditing simplifies the investigative process to determine the cause of a security event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. List the non-global zones on the system. # zoneadm list -vi | grep -v global The Audit Configuration profile is required. Determine whether the "perzone" auditing policy is in effect. # pfexec auditconfig -getpolicy | grep active | grep perzone If output is returned, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-216243`

### Rule: The operating system must monitor for unauthorized connections of mobile devices to organizational information systems.

**Rule ID:** `SV-216243r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile devices include portable storage media (e.g., USB memory sticks, external hard disk drives) and portable computing and communications devices with information storage capability (e.g., notebook/laptop computers, personal digital assistants, cellular telephones, digital cameras, audio recording devices). Organization-controlled mobile devices include those devices for which the organization has the authority to specify and the ability to enforce specific security requirements. Usage restrictions and implementation guidance related to mobile devices include configuration management, device identification and authentication, implementation of mandatory protective software (e.g., malicious code detection, firewall), scanning devices for malicious code, updating virus protection software, scanning for critical software updates and patches, conducting primary operating system (and possibly other resident software) integrity checks, and disabling unnecessary hardware (e.g., wireless, infrared). In order to detect unauthorized mobile device connections, organizations must first identify and document what mobile devices are authorized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global" this check applies. Determine if USB mass storage devices are locked out by the kernel. # grep -h "exclude: scsa2usb" /etc/system /etc/system.d/* If the output of this command is not: exclude: scsa2usb this is a finding.

## Group: SRG-OS-000349

**Group ID:** `V-219988`

### Rule: The audit system must support an audit reduction capability.

**Rule ID:** `SV-219988r958768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using the audit system will utilize the audit reduction capability. Without an audit reduction capability, users find it difficult to identify specific patterns of attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000352

**Group ID:** `V-219989`

### Rule: The audit system records must be able to be used by a report generation capability.

**Rule ID:** `SV-219989r958774_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling the audit system will produce records for use in report generation. Without an audit reporting capability, users find it difficult to identify specific patterns of attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000062

**Group ID:** `V-219990`

### Rule: The operating system must support the capability to compile audit records from multiple components within the system into a system-wide (logical or physical) audit trail that is time-correlated to within organization-defined level of tolerance.

**Rule ID:** `SV-219990r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account. Without accurate time stamps, source, user, and activity information, malicious activity cannot be accurately tracked. Without an audit reduction and reporting capability, users find it difficult to identify specific patterns of attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getcond If this command does not report: audit condition = auditing this is a finding.

## Group: SRG-OS-000062

**Group ID:** `V-219991`

### Rule: The audit system must be configured to audit all discretionary access control permission modifications.

**Rule ID:** `SV-219991r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. Check that the audit flag for auditing file access is enabled. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the OS version you are currently securing. # uname –v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "fm" audit flag is not included in output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "fm" audit flag is not included in output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000062

**Group ID:** `V-219992`

### Rule: The audit system must be configured to audit the loading and unloading of dynamic kernel modules.

**Rule ID:** `SV-219992r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing, individual system accesses cannot be tracked, and malicious activity cannot be detected and traced back to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone currently being secured. # zonename If the command output is "global", this check applies. Determine the OS version currently being secured. # uname -v For Solaris 11, 11.1, 11.2, and 11.3: # pfexec auditconfig -getflags | grep active | cut -f2 -d= If "as" audit flag is not included in the output, this is a finding. For Solaris 11.4 or newer: # pfexec auditconfig -t -getflags | cut -f2 -d= If "cusa,fm,fd,-fa,-ps,-ex" audit flags are not included in the output, this is a finding. Determine if auditing policy is set to collect command line arguments. # pfexec auditconfig -getpolicy | grep active | grep argv If the active audit policies line does not appear, this is a finding.

## Group: SRG-OS-000343

**Group ID:** `V-219993`

### Rule: The audit system must alert the SA when the audit storage volume approaches its capacity.

**Rule ID:** `SV-219993r971542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Filling the audit storage area can result in a denial of service or system outage and can lead to events going undetected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. The root role is required. Verify the presence of an audit_warn entry in /etc/mail/aliases. # /usr/lib/sendmail -bv audit_warn If the response is: audit_warn... User unknown this is a finding. Review the output of the command and verify that the audit_warn alias notifies the appropriate users in this form: audit_warn:user1,user2 If an appropriate user is not listed, this is a finding.

## Group: SRG-OS-000344

**Group ID:** `V-219994`

### Rule: The audit system must alert the System Administrator (SA) if there is any type of audit failure.

**Rule ID:** `SV-219994r958758_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Proper alerts to system administrators and Information Assurance (IA) officials of audit failures ensure a timely response to critical system issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. The root role is required. Verify the presence of an audit_warn entry in /etc/mail/aliases. # /usr/lib/sendmail -bv audit_warn If the response is: audit_warn... User unknown this is a finding. Review the output of the command and verify that the audit_warn alias notifies the appropriate users in this form: audit_warn:user1,user2 If an appropriate user is not listed, this is a finding.

## Group: SRG-OS-000341

**Group ID:** `V-219995`

### Rule: The operating system must allocate audit record storage capacity.

**Rule ID:** `SV-219995r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Proper audit storage capacity is crucial to ensuring the ongoing logging of critical events.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Review the current audit file space limitations # pfexec auditconfig -getplugin audit_binfile Plugin: audit_binfile (active) The output of the command will appear in this form. Attributes: p_dir=/var/audit;p_fsize=4M;p_minfree=2 If p_minfree is not equal to "2" of greater, this is a finding. p_dir defines the current audit file system. Note: By default in Solaris 11.1, /var/audit is a link to /var/share/audit which is mounted on rpool/VARSHARE. Check that zfs compression is enabled for the audit file system. # zfs get compression [poolname/filesystemname] If compression is off, this is a finding. Check that a ZFS quota is enforced for the audit filesystem. # zfs get quota [poolname/filesystemname] If quota is set to "none", this is a finding. Ensure that a reservation of space is enforced on /var/share so that other users do not use up audit space. # zfs get quota,reservation [poolname/filesystemname] If reservation is set to "none", this is a finding.

## Group: SRG-OS-000341

**Group ID:** `V-219996`

### Rule: The operating system must configure auditing to reduce the likelihood of storage capacity being exceeded.

**Rule ID:** `SV-219996r958752_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Overflowing the audit storage area can result in a denial of service or system outage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Audit Configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Check the status of the audit system. It must be auditing. # pfexec auditconfig -getplugin If the output of this command does not contain: p_fsize=4M this is a finding.

## Group: SRG-OS-000366

**Group ID:** `V-219997`

### Rule: The system must verify that package updates are digitally signed.

**Rule ID:** `SV-219997r1016296_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Digitally signed packages ensure that the source of the package can be identified.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine what the signature policy is for pkg publishers: # pkg property | grep signature-policy Check that output produces: signature-policy verify If the output does not confirm that signature-policy verify is active, this is a finding.

## Group: SRG-OS-000363

**Group ID:** `V-219998`

### Rule: The operating system must employ automated mechanisms, per organization-defined frequency, to detect the addition of unauthorized components/devices into the operating system.

**Rule ID:** `SV-219998r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Addition of unauthorized code or packages may result in data corruption or theft.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Software Installation Profile is required. Display the installation history of packages on the system to ensure that no undesirable packages have been installed: # pkg history -o finish,user,operation,command |grep install If the install command is listed as "/usr/bin/packagemanager", execute the command: # pkg history -l to determine which packages were installed during package manager sessions. If undocumented or unapproved packages have been installed, this is a finding.

## Group: SRG-OS-000368

**Group ID:** `V-219999`

### Rule: The operating system must employ automated mechanisms to prevent program execution in accordance with the organization-defined specifications.

**Rule ID:** `SV-219999r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating systems are capable of providing a wide variety of functions and services. Execution must be disabled based on organization-defined specifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify the packages installed on the system. # pkg list Any unauthorized software packages listed in the output are a finding.

## Group: SRG-OS-000183

**Group ID:** `V-220000`

### Rule: The operating system must disable information system functionality that provides the capability for automatic execution of code on mobile devices without user direction.

**Rule ID:** `SV-220000r958548_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile devices include portable storage media (e.g., USB memory sticks, external hard disk drives) and portable computing and communications devices with information storage capability (e.g., notebook/laptop computers, personal digital assistants, cellular telephones, digital cameras, audio recording devices). Auto execution vulnerabilities can result in malicious programs being automatically executed. Examples of information system functionality providing the capability for automatic execution of code are Auto Run and Auto Play. Auto Run and Auto Play are components of the Microsoft Windows operating system that dictate what actions the system takes when a drive is mounted. This requirement is designed to address vulnerabilities that arise when mobile devices such as USB memory sticks or other mobile storage devices are automatically mounted and applications are automatically invoked without user knowledge or acceptance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine if the removable media volume manager is running. # svcs -Ho state svc:/system/filesystem/rmvolmgr:default If the output reports that the service is "online", this is a finding.

## Group: SRG-OS-000324

**Group ID:** `V-220001`

### Rule: The system must restrict the ability of users to assume excessive privileges to members of a defined group and prevent unauthorized users from accessing administrative tools.

**Rule ID:** `SV-220001r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing any user to elevate their privileges can allow them excessive control of the system tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the root user is configured as a role, rather than a normal user. # userattr type root If the command does not return the word "role", this is a finding. Verify at least one local user has been assigned the root role. # grep '[:;]roles=root[^;]*' /etc/user_attr If no lines are returned, or no users are permitted to assume the root role, this is a finding.

## Group: SRG-OS-000396

**Group ID:** `V-220003`

### Rule: The operating system must employ FIPS-validate or NSA-approved cryptography to implement digital signatures.

**Rule ID:** `SV-220003r987791_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>FIPS 140-2 is the current standard for validating cryptographic modules, and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified hardware based encryption modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. The Crypto Management profile is required to execute this command. Check to ensure that FIPS-140 encryption mode is enabled. # cryptoadm list fips-140| grep -c "is disabled" If the output of this command is not "0", this is a finding.

## Group: SRG-OS-000423

**Group ID:** `V-220004`

### Rule: The operating system must protect the integrity of transmitted information.

**Rule ID:** `SV-220004r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring the integrity of transmitted information requires the operating system take feasible measures to employ transmission layer security. This requirement applies to communications across internal and external networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All remote sessions must be conducted via encrypted services and ports. Check that SSH is enabled: # svcs svc:/network/ssh STATE STIME FMRI online Nov_03 svc:/network/ssh:default Ask the operator to document all configured external ports and protocols. If any unencrypted connections are used, this is a finding.

## Group: SRG-OS-000424

**Group ID:** `V-220005`

### Rule: The operating system must employ cryptographic mechanisms to recognize changes to information during transmission unless otherwise protected by alternative physical measures.

**Rule ID:** `SV-220005r971547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring that transmitted information is not altered during transmission requires the operating system take feasible measures to employ transmission layer security. This requirement applies to communications across internal and external networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All remote sessions must be conducted via encrypted services and ports. Check that SSH is enabled: # svcs svc:/network/ssh STATE STIME FMRI online Nov_03 svc:/network/ssh:default Ask the operator to document all configured external ports and protocols. If any unencrypted connections are used, this is a finding.

## Group: SRG-OS-000425

**Group ID:** `V-220006`

### Rule: The operating system must maintain the integrity of information during aggregation, packaging, and transformation in preparation for transmission.

**Rule ID:** `SV-220006r958912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring the integrity of transmitted information requires the operating system take feasible measures to employ transmission layer security. This requirement applies to communications across internal and external networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All remote sessions must be conducted via encrypted services and ports. Ask the operator to document all configured external ports and protocols. If any unencrypted connections are used, this is a finding.

## Group: SRG-OS-000423

**Group ID:** `V-220007`

### Rule: The operating system must protect the confidentiality of transmitted information.

**Rule ID:** `SV-220007r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring the confidentiality of transmitted information requires the operating system take feasible measures to employ transmission layer security. This requirement applies to communications across internal and external networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All remote sessions must be conducted via encrypted services and ports. Ask the operator to document all configured external ports and protocols. If any unencrypted connections are used, this is a finding.

## Group: SRG-OS-000424

**Group ID:** `V-220008`

### Rule: The operating system must employ cryptographic mechanisms to prevent unauthorized disclosure of information during transmission unless otherwise protected by alternative physical measures.

**Rule ID:** `SV-220008r971547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring that transmitted information does not become disclosed to unauthorized entities requires the operating system take feasible measures to employ transmission layer security. This requirement applies to communications across internal and external networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All remote sessions must be conducted via encrypted services and ports. Ask the operator to document all configured external ports and protocols. If any unencrypted connections are used, this is a finding.

## Group: SRG-OS-000425

**Group ID:** `V-220009`

### Rule: The operating system must maintain the confidentiality of information during aggregation, packaging, and transformation in preparation for transmission.

**Rule ID:** `SV-220009r958912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring that transmitted information remains confidential during aggregation, packaging, and transformation requires the operating system take feasible measures to employ transmission layer security. This requirement applies to communications across internal and external networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All remote sessions must be conducted via encrypted services and ports. Ask the operator to document all configured external ports and protocols. If any unencrypted connections are used, this is a finding.

## Group: SRG-OS-000404

**Group ID:** `V-220010`

### Rule: The operating system must employ cryptographic mechanisms to protect information in storage.

**Rule ID:** `SV-220010r958870_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When data is written to digital media, such as hard drives, mobile computers, external/removable hard drives, personal digital assistants, flash/thumb drives, etc., there is risk of data loss and data compromise. An organizational assessment of risk guides the selection of media and associated information contained on the media requiring restricted access. Organizations need to document in policy and procedures the media requiring restricted access, individuals authorized to access the media, and the specific measures taken to restrict access. Fewer protection measures are needed for media containing information determined by the organization to be in the public domain, to be publicly releasable, or to have limited or no adverse impact if accessed by other than authorized personnel. In these situations, it is assumed the physical access controls where the media resides provide adequate protection. As part of a defense-in-depth strategy, the organization considers routinely encrypting information at rest on selected secondary storage devices. The employment of cryptography is at the discretion of the information owner/steward. The selection of the cryptographic mechanisms used is based upon maintaining the confidentiality and integrity of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if file system encryption is required by your organization. If not required, this item does not apply. Determine if file system encryption is enabled for user data sets. This check does not apply to the root, var, share, swap or dump datasets. # zfs list Using the file system name, determine if the file system is encrypted: # zfs get encryption [filesystem] If "encryption off" is listed, this is a finding.

## Group: SRG-OS-000404

**Group ID:** `V-220011`

### Rule: The operating system must employ cryptographic mechanisms to prevent unauthorized disclosure of information at rest unless otherwise protected by alternative physical measures.

**Rule ID:** `SV-220011r958870_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When data is written to digital media, such as hard drives, mobile computers, external/removable hard drives, personal digital assistants, flash/thumb drives, etc., there is risk of data loss and data compromise. An organizational assessment of risk guides the selection of media and associated information contained on the media requiring restricted access. Organizations need to document in policy and procedures the media requiring restricted access, individuals authorized to access the media, and the specific measures taken to restrict access. Fewer protection measures are needed for media containing information determined by the organization to be in the public domain, to be publicly releasable, or to have limited or no adverse impact if accessed by other than authorized personnel. In these situations, it is assumed the physical access controls where the media resides provide adequate protection. As part of a defense-in-depth strategy, the organization considers routinely encrypting information at rest on selected secondary storage devices. The employment of cryptography is at the discretion of the information owner/steward. The selection of the cryptographic mechanisms used is based upon maintaining the confidentiality and integrity of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if file system encryption is required by your organization. If not required, this item does not apply. Determine if file system encryption is enabled for user data sets. This check does not apply to the root, var, share, swap or dump datasets. # zfs list Using the file system name, determine if the file system is encrypted: # zfs get encryption [filesystem] If "encryption off" is listed, this is a finding.

## Group: SRG-OS-000423

**Group ID:** `V-220012`

### Rule: The operating system must protect the integrity of transmitted information.

**Rule ID:** `SV-220012r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring the integrity of transmitted information requires the operating system take feasible measures to employ transmission layer security. This requirement applies to communications across internal and external networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The operator shall determine if IPsec is being used to encrypt data for activities such as cluster interconnects or other non-SSH, SFTP data connections. On both systems review the file /etc/inet/ipsecinit.conf. Ensure that connections between hosts are configured properly in this file per the Solaris 11 documentation. Check that the IPsec policy service is online: # svcs svc:/network/ipsec/policy:default If the IPsec service is not online, this is a finding. If encrypted protocols are not used between systems, this is a finding.

## Group: SRG-OS-000327

**Group ID:** `V-220013`

### Rule: The operating system must protect the audit records resulting from non-local accesses to privileged accounts and the execution of privileged functions.

**Rule ID:** `SV-220013r958732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of audit records and audit data is of critical importance. Care must be taken to ensure privileged users cannot circumvent audit protections put in place. Auditing might not be reliable when performed by an operating system which the user being audited has privileged access to. The privileged user could inhibit auditing or directly modify audit records. To prevent this from occurring, privileged access shall be further defined between audit-related privileges and other privileges, thus limiting the users with audit-related privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The audit configuration profile is required. This check applies to the global zone only. Determine the zone that you are currently securing. # zonename If the command output is "global", this check applies. Determine the location of the local audit trail files. # auditconfig -getplugin audit_binfile Plugin: audit_binfile (active) Attributes: p_dir=/var/audit;p_fsize=4M;p_minfree=1;" In this example, the audit files can be found in /var/audit. Check that the permissions on the audit files are 640 (rw- r-- --) or less permissive. # ls -al /var/audit # ls -l /var/audit/* If the permissions are more permissive than 640, this is a finding. Note: The default Solaris 11 location for /var/audit is a link to /var/share/audit.

## Group: SRG-OS-000356

**Group ID:** `V-220014`

### Rule: The operating system must synchronize internal information system clocks with a server that is synchronized to one of the redundant United States Naval Observatory (USNO) time servers or a time server designated for the appropriate DOD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-220014r1016297_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure the accuracy of the system clock, it must be synchronized with an authoritative time source within DOD. Many system functions, including time-based login and activity restrictions, automated reports, system logs, and audit records depend on an accurate system clock. If there is no confidence in the correctness of the system clock, time-based functions may not operate as intended and records may be of diminished value.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NTP must be used and used only in the global zone. Determine the zone to be secured. # zonename If the command output is not "global", then NTP must be disabled. Check the system for a running NTP daemon. # svcs -Ho state ntp If NTP is online, this is a finding. If the output from "zonename" is "global", then NTP must be enabled. Check the system for a running NTP daemon. # svcs -Ho state ntp If NTP is not online, this is a finding. If NTP is running, confirm the servers and peers or multicast client (as applicable) are local or an authoritative U.S. DOD source. For the NTP daemon: # more /etc/inet/ntp.conf If a nonlocal/nonauthoritative (non-DOD source, non-USNO-based, or non-GPS) time server is used, this is a finding. Determine if the time synchronization frequency is correct. # grep "maxpoll" /etc/inet/ntp.conf If the command returns "File not found" or any value for maxpoll, this is a finding. Determine if the running NTP server is configured properly. # ntpq -p | awk '($6 ~ /[0-9]+/ && $6 > 86400) { print $1" "$6 }' This will print out the name of any time server whose current polling time is greater than 24 hours (along with the actual value). If there is any output, this is a finding.

## Group: SRG-OS-000445

**Group ID:** `V-220015`

### Rule: The operating system must verify the correct operation of security functions in accordance with organization-defined conditions and in accordance with organization-defined frequency (if periodic verification).

**Rule ID:** `SV-220015r958944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security functional testing involves testing the operating system for conformance to the operating system security function specifications, as well as for the underlying security model. The need to verify security functionality applies to all security functions. The conformance criteria state the conditions necessary for the operating system to exhibit the desired security behavior or satisfy a security property. For example, successful login triggers an audit entry.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the operator if DoD-approved SCAP compliance checking software is installed and run on a periodic basis. If DoD-approved SCAP compliance checking software is not installed and/or not run on a periodic basis, this is a finding.

## Group: SRG-OS-000324

**Group ID:** `V-224672`

### Rule: The operating system must prevent non-privileged users from circumventing malicious code protection capabilities.

**Rule ID:** `SV-224672r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to minimize potential negative impact to the organization caused by malicious code, it is imperative that malicious code is identified and eradicated prior to entering protected enclaves via operating system entry and exit points. The requirement states that AV and malware protection applications must be used at entry and exit points. For the operating system, this means an anti-virus application must be installed on machines that are the entry and exit points.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The operator will ensure that anti-virus software is installed and operating. If the operator is unable to provide a documented configuration for an installed anti-virus software system or if not properly used, this is a finding.

## Group: SRG-OS-000445

**Group ID:** `V-224673`

### Rule: The operating system must identify potentially security-relevant error conditions.

**Rule ID:** `SV-224673r958944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security functional testing involves testing the operating system for conformance to the operating system security function specifications, as well as for the underlying security model. The need to verify security functionality applies to all security functions. The conformance criteria state the conditions necessary for the operating system to exhibit the desired security behavior or satisfy a security property. For example, successful login triggers an audit entry.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the operator if DoD-approved SCAP compliance checking software is installed and run on a periodic basis. If DoD-approved SCAP compliance checking software is not installed and/or not run on a periodic basis, this is a finding.

## Group: SRG-OS-000480

**Group ID:** `V-233301`

### Rule: The sshd server must bind the X11 forwarding server to the loopback address.

**Rule ID:** `SV-233301r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As enabling X11 Forwarding on the host can permit a malicious user to secretly open another X11 connection to another remote client during the session and perform unobtrusive activities such as keystroke monitoring, if the X11 services are not required for the system's intended function, they should be disabled or restricted as appropriate to the user's needs. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the DISPLAY environment variable to “localhost”. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the X11 forwarding server is bound to the loopback address. # grep "^X11UseLocalhost" /etc/ssh/sshd_config If the output of this command is not: X11UseLocalhost yes this is a finding.

