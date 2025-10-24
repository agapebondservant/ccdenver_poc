# STIG Benchmark: VMware vSphere 8.0 vCenter Appliance Envoy Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-259161`

### Rule: The vCenter Envoy and Rhttpproxy service log files permissions must be set correctly.

**Rule ID:** `SV-259161r935387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, usernames, etc. The web server must protect the log data from unauthorized read, write, copy, etc. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from access by nonprivileged users. Satisfies: SRG-APP-000118-WSR-000068, SRG-APP-000119-WSR-000069, SRG-APP-000120-WSR-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following commands: # find /var/log/vmware/rhttpproxy/ -xdev -type f -a '(' -perm -o+w -o -not -user rhttpproxy -o -not -group rhttpproxy ')' -exec ls -ld {} \; # find /var/log/vmware/envoy/ -xdev -type f -a '(' -perm -o+w -o -not -user envoy -o -not -group envoy ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-APP-000176-WSR-000096

**Group ID:** `V-259162`

### Rule: The vCenter Envoy service private key file must be protected from unauthorized access.

**Rule ID:** `SV-259162r935390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy's private key is used to prove the identity of the server to clients and securely exchange the shared secret key used to encrypt communications between the web server and clients. By gaining access to the private key, an attacker can pretend to be an authorized server and decrypt the Transport Layer Security (TLS) traffic between a client and the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # stat -c "%n permissions are %a, is owned by %U and group owned by %G" /etc/vmware-rhttpproxy/ssl/rui.key Expected result: /etc/vmware-rhttpproxy/ssl/rui.key permissions are 600, is owned by rhttpproxy and group owned by rhttpproxy If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000358-WSR-000063

**Group ID:** `V-259163`

### Rule: The vCenter Rhttpproxy service log files must be sent to a central log server.

**Rule ID:** `SV-259163r935393_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Writing events to a centralized management audit system offers many benefits to the enterprise over having dispersed logs. Centralized management of audit records and logs provides for efficiency in maintenance and management of records, enterprise analysis of events, and backup and archiving of event records enterprise-wide. The web server and related components are required to be capable of writing logs to centralized audit log servers. Satisfies: SRG-APP-000358-WSR-000063, SRG-APP-000125-WSR-000071</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, there is a vmware-services-rhttpproxy.conf rsyslog configuration file that includes the service logs when syslog is configured on vCenter, but it must be verified. At the command prompt, run the following command: # cat /etc/vmware-syslog/vmware-services-rhttpproxy.conf Expected result: #rhttpproxy log input(type="imfile" File="/var/log/vmware/rhttpproxy/rhttpproxy.log" Tag="rhttpproxy-main" Severity="info" Facility="local0") #rhttpproxy init stdout input(type="imfile" File="/var/log/vmware/rhttpproxy/rproxy_init.log.stdout" Tag="rhttpproxy-stdout" Severity="info" Facility="local0") #rhttpproxy init stderr input(type="imfile" File="/var/log/vmware/rhttpproxy/rproxy_init.log.stderr" Tag="rhttpproxy-stderr" Severity="info" Facility="local0") If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000358-WSR-000063

**Group ID:** `V-259164`

### Rule: The vCenter Envoy service log files must be sent to a central log server.

**Rule ID:** `SV-259164r935396_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Writing events to a centralized management audit system offers many benefits to the enterprise over having dispersed logs. Centralized management of audit records and logs provides for efficiency in maintenance and management of records, enterprise analysis of events, and backup and archiving of event records enterprise-wide. The web server and related components are required to be capable of writing logs to centralized audit log servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, there is a vmware-services-envoy.conf rsyslog configuration file that includes the service logs when syslog is configured on vCenter, but it must be verified. At the command prompt, run the following command: # cat /etc/vmware-syslog/vmware-services-envoy.conf Expected result: #envoy service log input(type="imfile" File="/var/log/vmware/envoy/envoy.log" Tag="envoy-main" Severity="info" Facility="local0") #envoy access log input(type="imfile" File="/var/log/vmware/envoy/envoy-access.log" Tag="envoy-access" Severity="info" Facility="local0") #envoy init stdout input(type="imfile" File="/var/log/vmware/envoy/envoy_init.log.stdout" Tag="envoy-stdout" Severity="info" Facility="local0") #envoy init stderr input(type="imfile" File="/var/log/vmware/envoy/envoy_init.log.stderr" Tag="envoy-stderr" Severity="info" Facility="local0") If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-259165`

### Rule: The vCenter Envoy service must set a limit on remote connections.

**Rule ID:** `SV-259165r935399_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy client connections must be limited to preserve system resources and continue servicing connections without interruption. Without a limit set, the system would be vulnerable to a trivial denial-of-service attack where connections are created en masse and vCenter resources are entirely consumed. Envoy comes hard coded with a tested and supported value for "maxRemoteHttpsConnections" and "maxRemoteHttpConnections" that must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following commands: # xmllint --xpath '/config/envoy/L4Filter/maxRemoteHttpsConnections/text()' /etc/vmware-rhttpproxy/config.xml # xmllint --xpath '/config/envoy/L4Filter/maxRemoteHttpConnections/text()' /etc/vmware-rhttpproxy/config.xml Example result: 2048 or XPath set is empty If the output is not "2048" or "XPath set it empty", this is a finding. Note: If "XPath set is empty" is returned the default values are in effect and is 2048.

