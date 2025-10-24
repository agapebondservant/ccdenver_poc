# STIG Benchmark: VMware vRealize Automation 7.x Lighttpd Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-240215`

### Rule: Lighttpd must limit the number of simultaneous requests.

**Rule ID:** `SV-240215r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a web site, facilitating a denial of service attack. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. Lighttpd is used for administrative purposes only. Lighttpd provides the maxConnections attribute of the <Connector Elements> to limit the number of concurrent TCP connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'server.max-connections = 1024' /opt/vmware/etc/lighttpd/lighttpd.conf If the "server.max-connections" is not set to "1024", commented out, or does not exist, this is a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-240216`

### Rule: Lighttpd must be configured with FIPS 140-2 compliant ciphers for https connections.

**Rule ID:** `SV-240216r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is optional for a public web server. However, if authentication is being performed, then the use of the TLS protocol is required. Without the use of TLS, the authentication data would be transmitted unencrypted and would become vulnerable to disclosure. Using TLS along with DoD PKI certificates for encryption of the authentication data protects the information from being accessed by all parties on the network. To further protect the authentication data, the web server must use a FIPS 140-2 approved TLS version and all non-FIPS-approved SSL versions must be disabled. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^ssl.cipher-list' /opt/vmware/etc/lighttpd/lighttpd.conf If the value ssl.cipher-list = "FIPS: +3DES:!aNULL" is not returned or commented out, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-240217`

### Rule: Lighttpd must be configured to use the SSL engine.

**Rule ID:** `SV-240217r879520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. In order to protect the integrity and confidentiality of the remote sessions, Lighttpd uses SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^ssl.engine' /opt/vmware/etc/lighttpd/lighttpd.conf If the value "ssl.engine" is not set to "enable", this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-240218`

### Rule: Lighttpd must be configured to use mod_accesslog.

**Rule ID:** `SV-240218r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lighttpd is the administration panel for vRealize Automation. Because it is intended to provide remote access to the appliance, vRA must provide remote access information to external monitoring systems. mod_accesslog is the module in Lighttpd that configures Lighttpd to share information with external monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /opt/vmware/etc/lighttpd/lighttpd.conf | awk '/server\.modules/,/\)/' If the value "mod_accesslog" is not listed, this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-240219`

### Rule: Lighttpd must generate log records for system startup and shutdown.

**Rule ID:** `SV-240219r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. Lighttpd records system event information in the error.log file. Included in the file is system start and stop events.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: egrep 'server\sstarted|server\sstopped' /opt/vmware/var/log/lighttpd/error.log If server stopped and server started times are not listed, this is a finding.

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-240220`

### Rule: Lighttpd must produce log records containing sufficient information to establish what type of events occurred.

**Rule ID:** `SV-240220r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the correct type of event that occurred is important during forensic analysis. The correct determination of the event and when it occurred is important in relation to other events that happened at that same time. Without sufficient information establishing what type of log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. Lighttpd logs user activity in the access.log file using the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures logs all user session information related to the hosted application session. This will enable forensic analysis of server events in case of malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail -n 4 /opt/vmware/var/log/lighttpd/access.log If the GET or POST events do not exist in the access.log file, this is a finding.

## Group: SRG-APP-000096-WSR-000057

**Group ID:** `V-240221`

### Rule: Lighttpd must produce log records containing sufficient information to establish when (date and time) events occurred.

**Rule ID:** `SV-240221r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the correct order of the events that occurred is important during forensic analysis. Events that appear harmless by themselves might be flagged as a potential threat when properly viewed in sequence. By also establishing the event date and time, an event can be properly viewed with an enterprise tool to fully see a possible threat in its entirety. Without sufficient information establishing when the log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. Lighttpd logs user activity in the access.log file using the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures logs all user session information related to the hosted application session. This will enable forensic analysis of server events in case of malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail -n 1 /opt/vmware/var/log/lighttpd/access.log If the generated log records do not have date and time data, this is a finding.

## Group: SRG-APP-000097-WSR-000058

**Group ID:** `V-240222`

### Rule: Lighttpd must produce log records containing sufficient information to establish where within the web server the events occurred.

**Rule ID:** `SV-240222r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the correct location or process within the web server where the events occurred is important during forensic analysis. Correctly determining the web service, plug-in, or module will add information to the overall reconstruction of the logged event. For example, an event that occurred during communication to a cgi module might be handled differently than an event that occurred during a communication session to a user. Without sufficient information establishing where the log event occurred within the web server, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. Lighttpd logs user activity in the access.log file using the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures logs all user session information related to the hosted application session. This will enable forensic analysis of server events in case of malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail -n 1 /opt/vmware/var/log/lighttpd/access.log If any of the generated audit records are without sufficient information to establish where the event occurred, this is a finding.

## Group: SRG-APP-000098-WSR-000059

**Group ID:** `V-240223`

### Rule: Lighttpd must produce log records containing sufficient information to establish the source of events.

**Rule ID:** `SV-240223r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the correct source, e.g. source IP, of the events is important during forensic analysis. Correctly determining the source will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if the event compromised other assets within the enterprise. Without sufficient information establishing the source of the logged event, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. Lighttpd logs user activity in the access.log file using the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures logs all user session information related to the hosted application session. This will enable forensic analysis of server events in case of malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail -n 4 /opt/vmware/var/log/lighttpd/access.log If any of the generated audit records are without sufficient information to establish the source of the events, this is a finding.

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-240224`

### Rule: Lighttpd must produce log records containing sufficient information to establish the outcome (success or failure) of events.

**Rule ID:** `SV-240224r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the success or failure of an event is important during forensic analysis. Correctly determining the outcome will add information to the overall reconstruction of the logable event. By determining the success or failure of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the event occurred in other areas within the enterprise. Without sufficient information establishing the success or failure of the logged event, investigation into the cause of event is severely hindered. The success or failure also provides a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. Lighttpd logs user activity in the access.log file using the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures logs all user session information related to the hosted application session. This will enable forensic analysis of server events in case of malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: Note: The HTTP status code indicating success or failure is a 3-digit integer immediately after "HTTP/1.1". Any value other than a 3-digit code immediately following "HTTP/1.1" is a failure of the logging process. tail -n 4 /opt/vmware/var/log/lighttpd/access.log If any of the generated audit records are without sufficient information to establish the outcome of the event (success or failure), this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-240225`

### Rule: Lighttpd must have the correct ownership on the log files to ensure they are only be accessible by privileged users.

**Rule ID:** `SV-240225r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must only be accessible by privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If the owner is not "root", this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-240226`

### Rule: Lighttpd must have the correct group-ownership on the log files to ensure they are only be accessible by privileged users.

**Rule ID:** `SV-240226r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must only be accessible by privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If the group-owner is not "root", this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-240227`

### Rule: Lighttpd must have the correct permissions on the log files to ensure they are only be accessible by privileged users.

**Rule ID:** `SV-240227r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must only be accessible by privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If permissions on the log files are not "-rw-r----- (640)", this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-240228`

### Rule: Lighttpd must have the correct ownership on the log files to ensure they are protected from unauthorized modification.

**Rule ID:** `SV-240228r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If the owner is not "root", this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-240229`

### Rule: Lighttpd must have the correct group-ownership on the log files to ensure they are protected from unauthorized modification.

**Rule ID:** `SV-240229r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If the group-owner is not "root", this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-240230`

### Rule: Lighttpd must have the correct permissions on the log files to ensure they are protected from unauthorized modification.

**Rule ID:** `SV-240230r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must be protected from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If permissions on the log files are not "-rw-r----- (640)", this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-240231`

### Rule: Lighttpd must have the correct ownership on the log files to ensure they are protected from unauthorized deletion.

**Rule ID:** `SV-240231r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must be protected from unauthorized deletion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If the owner is not "root", this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-240232`

### Rule: Lighttpd must have the correct group-ownership on the log files to ensure they are protected from unauthorized deletion.

**Rule ID:** `SV-240232r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must be protected from unauthorized deletion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If the group-owner is not "root", this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-240233`

### Rule: Lighttpd must have the correct permissions on the log files to ensure they are protected from unauthorized deletion.

**Rule ID:** `SV-240233r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. Lighttpd creates its own logs. It does not use an external log system. The Lighttpd log must be protected from unauthorized deletion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/var/log/lighttpd/*.log If permissions on the log files are not "-rw-r----- (640)", this is a finding.

## Group: SRG-APP-000125-WSR-000071

**Group ID:** `V-240234`

### Rule: Lighttpd log data and records must be backed up onto a different system or media.

**Rule ID:** `SV-240234r879582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of Lighttpd log data includes assuring log data is not accidentally lost or deleted. Backing up Lighttpd log records to an unrelated system or onto separate media than the system the web server is actually running on helps to assure that, in the event of a catastrophic system failure, the log records will be retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine whether log data and records are being backed up to a different system or separate media. If log data and records are not being backed up to a different system or separate media, this is a finding.

## Group: SRG-APP-000131-WSR-000051

**Group ID:** `V-240235`

### Rule: Lighttpd files must be verified for their integrity before being added to a production web server.

**Rule ID:** `SV-240235r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Being able to verify that a patch, upgrade, certificate, etc., being added to the web server is unchanged from the producer of the file is essential for file validation and non-repudiation of the information. The Lighttpd web server files on vRA must be part of a documented build process. Checksums of the production files must be available to verify their integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine whether web server files are verified/validated before being implemented into the production environment. If the web server files are not verified or validated before being implemented into the production environment, this is a finding.

## Group: SRG-APP-000131-WSR-000073

**Group ID:** `V-240236`

### Rule: Lighttpd expansion modules must be verified for their integrity before being added to a production web server.

**Rule ID:** `SV-240236r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Being able to verify that a patch, upgrade, certificate, etc., being added to the web server is unchanged from the producer of the file is essential for file validation and non-repudiation of the information. Expansion modules that are installed on the production Lighttpd web server on vRA must be part of a documented build process. Checksums of the production files must be available to verify their integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine whether expansion modules are being fully reviewed, tested, and signed before being implemented into the production environment. If the expansion modules are not being fully reviewed, tested, and signed before being implemented into the production environment, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-240237`

### Rule: Lighttpd must prohibit unnecessary services, functions or processes.

**Rule ID:** `SV-240237r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Just as running unneeded services and protocols is a danger to the web server at the lower levels of the OSI model, running unneeded utilities and programs is also a danger at the application layer of the OSI model. Office suites, development tools, and graphical editors are examples of such programs that are troublesome. Individual productivity tools have no legitimate place or use on an enterprise, production web server and they are also prone to their own security risks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine if any unnecessary services, functions or processes are running on the web server. If any unnecessary services, functions or processes are running on the web server, this is a finding.

## Group: SRG-APP-000141-WSR-000076

**Group ID:** `V-240238`

### Rule: Lighttpd proxy settings must be configured.

**Rule ID:** `SV-240238r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that will also proxy requests into an otherwise protected network is a very common attack making the attack anonymous.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -A 6 -B 1 proxy.server /opt/vmware/etc/lighttpd/lighttpd.conf If the proxy.server "host" value is not set to "127.0.0.1" and the proxy.server "port" value is not set to "5488", this is a finding.

## Group: SRG-APP-000141-WSR-000077

**Group ID:** `V-240239`

### Rule: Lighttpd must only contain components that are operationally necessary.

**Rule ID:** `SV-240239r879587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Web server documentation, sample code, example applications, and tutorials may be an exploitable threat to a web server because this type of code has not been evaluated and approved. A production web server must only contain components that are operationally necessary (e.g., compiled code, scripts, web-content, etc.). Any documentation, sample code, example applications, and tutorials must be removed from a production web server. To make certain that the documentation and code are not installed or uninstalled completely; the web server must offer an option as part of the installation process to exclude these packages or to uninstall the packages if necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine if web server documentation, sample code, example applications, or tutorials has been deleted or removed and only contains components that are operationally necessary. If web server documentation, sample code, example applications, or tutorials has not been deleted or removed and contains components that are not operationally necessary, this is a finding.

## Group: SRG-APP-000141-WSR-000081

**Group ID:** `V-240240`

### Rule: Lighttpd must have MIME types for csh or sh shell programs disabled.

**Rule ID:** `SV-240240r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users must not be allowed to access the shell programs. Shell programs might execute shell escapes and could then perform unauthorized activities that could damage the security posture of the web server. A shell is a program that serves as the basic interface between the user and the operating system. In this regard, there are shells that are security risks in the context of a web server and shells that are unauthorized in the context of the Security Features User's Guide. Lighttpd must be configured to disable MIME types for csh or sh shell programs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /opt/vmware/etc/lighttpd/lighttpd.conf | egrep '".sh"|".csh"' If the command returns any value, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-240241`

### Rule: Lighttpd must only enable mappings to necessary and approved scripts.

**Rule ID:** `SV-240241r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lighttpd will only allow or deny script execution based on file extension. The ability to control script execution is controlled with the cgi.assign variable in lighttpd.conf. For script mappings, the ISSO must document and approve all allowable file extensions the web site allows (whitelist). The whitelist will be compared to the script mappings in Lighttpd.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine the scripts that are deemed necessary and approved (whitelist). Note: Lighttpd provides the cgi.assign parameter to specify script mappings. Navigate to and open /opt/vmware/etc/lighttpd/lighttpd.conf file Navigate to the cgi.assign parameter. If cgi.assign parameter is configured with script types that are deemed for denial, this is a finding.

## Group: SRG-APP-000141-WSR-000083

**Group ID:** `V-240242`

### Rule: Lighttpd must have resource mappings set to disable the serving of certain file types.

**Rule ID:** `SV-240242r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource mapping is the process of tying a particular file type to a process in Lighttpd that can serve that type of file to a requesting client and to identify which file types are not to be delivered to a client. Lighttpd provides the url.access-deny parameter to specify a blacklist of file types which should be denied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine the file types (blacklist) that are deemed for denial. Note: Lighttpd provides the url.access-deny parameter to specify the blacklist of files. Navigate to and open /opt/vmware/etc/lighttpd/lighttpd.conf file Navigate to the url.access-deny parameter. If url.access-deny parameter is not configured with the file types that are blacklisted, this is a finding. If url.access-deny parameter is not set properly, this is a finding.

## Group: SRG-APP-000141-WSR-000085

**Group ID:** `V-240243`

### Rule: Lighttpd must not have the Web Distributed Authoring (WebDAV) module installed.

**Rule ID:** `SV-240243r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be installed with functionality that, just by its nature, is not secure. Web Distributed Authoring (WebDAV) is an extension to the HTTP protocol that, when developed, was meant to allow users to create, change, and move documents on a server, typically a web server or web share. Allowing this functionality, development, and deployment is much easier for web authors. WebDAV is not widely used and has serious security concerns because it may allow clients to modify unauthorized files on the web server. Lighttpd uses the mod_webdav module to provide WebDAV services. This module must not be installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /opt/vmware/etc/lighttpd/lighttpd.conf | awk '/server\.modules/,/\)/' If the value "mod_webdav" module is listed, this is a finding.

## Group: SRG-APP-000141-WSR-000085

**Group ID:** `V-240244`

### Rule: Lighttpd must not have the webdav configuration file included.

**Rule ID:** `SV-240244r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be installed with functionality that, just by its nature, is not secure. Web Distributed Authoring (WebDAV) is an extension to the HTTP protocol that, when developed, was meant to allow users to create, change, and move documents on a server, typically a web server or web share. Allowing this functionality, development, and deployment is much easier for web authors. WebDAV is not widely used and has serious security concerns because it may allow clients to modify unauthorized files on the web server. The Lighttpd configuration file uses the 'include' statement to include other configuration files. The default lighttpd.conf file contains a reference to include a webdav.conf file, and it is possible for the WebDAV module to be loaded in other files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'webdav.conf' /opt/vmware/etc/lighttpd/lighttpd.conf If the return value is an include statement and it is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000086

**Group ID:** `V-240245`

### Rule: Lighttpd must prevent hosted applications from exhausting system resources.

**Rule ID:** `SV-240245r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When it comes to DoS attacks, most of the attention is paid to ensuring that systems and applications are not victims of these attacks. While it is true that those accountable for systems want to ensure they are not affected by a DoS attack, they also need to ensure their systems and applications are not used to launch such an attack against others. To that extent, a variety of technologies exist to limit, or in some cases, eliminate the effects of DoS attacks. Limiting system resources that are allocated to any user to a bare minimum may also reduce the ability of users to launch some DoS attacks. Applications and application developers must take the steps needed to ensure users cannot use these applications to launch DoS attacks against other systems and networks. An example would be preventing Lighttpd from keeping idle connections open for too long.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^server.max-keep-alive-idle' /opt/vmware/etc/lighttpd/lighttpd.conf If the "server.max-keep-alive-idle" is not set to "30", this is a finding.

## Group: SRG-APP-000141-WSR-000087

**Group ID:** `V-240246`

### Rule: Lighttpd must not use symbolic links in the Lighttpd web content directory tree.

**Rule ID:** `SV-240246r879587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A symbolic link allows a file or a directory to be referenced using a symbolic name raising a potential hazard if symbolic linkage is made to a sensitive area. When web scripts are executed and symbolic links are allowed, the Lighttpd could be allowed to access locations on the server that are outside the scope of the hosted application document root or home directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: find /opt/vmware/share/htdocs -type l If any files are listed, this is a finding.

## Group: SRG-APP-000142-WSR-000089

**Group ID:** `V-240247`

### Rule: Lighttpd must be configured to use port 5480.

**Rule ID:** `SV-240247r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lighttpd is used as the web server for vRealize Automation's Virtual Appliance Management Interface (vAMI). To segregate appliance management from appliance operation, Lighttpd can be configured to listen on a separate port. Port 5488 is the recommended port setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^server.port' /opt/vmware/etc/lighttpd/lighttpd.conf If the value of "server.port" is not "5480", this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-240248`

### Rule: Lighttpd must use SSL/TLS protocols in order to secure passwords during transmission from the client.

**Rule ID:** `SV-240248r879609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Data used to authenticate the vAMI admin must be sent to Lighttpd via SSL/TLS. To ensure that Lighttpd is using SSL/TLS, the ssl.engine must be enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^ssl.engine' /opt/vmware/etc/lighttpd/lighttpd.conf If the value of "ssl.engine" is not set to "enable", this is a finding.

## Group: SRG-APP-000176-WSR-000096

**Group ID:** `V-240249`

### Rule: Lighttpd must have private key access restricted.

**Rule ID:** `SV-240249r879613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lighttpd's private key is used to prove the identity of the server to clients and securely exchange the shared secret key used to encrypt communications between the web server and clients. Only authenticated system administrators or the designated PKI Sponsor for the web server must have access to the web servers private key. By gaining access to the private key, an attacker can pretend to be an authorized server and decrypt the encrypted traffic between a client and the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -al /opt/vmware/etc/lighttpd/server.pem If the "server.pem" file is not owned by "root" or the file permissions are not "400", this is a finding.

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-240250`

### Rule: Lighttpd must be configured to use only FIPS 140-2 approved ciphers.

**Rule ID:** `SV-240250r879616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of cryptography to provide confidentiality and non-repudiation is not effective unless strong methods are employed with its use. Many earlier encryption methods and modules have been broken and/or overtaken by increasing computing power. The NIST FIPS 140-2 cryptographic standards provide proven methods and strengths to employ cryptography effectively.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'ssl.cipher-list' /opt/vmware/etc/lighttpd/lighttpd.conf If the return value for "ssl.cipher-list" is not set to "FIPS: +3DES:!aNULL", this is a finding.

## Group: SRG-APP-000211-WSR-000030

**Group ID:** `V-240251`

### Rule: Lighttpd must prohibit non-privileged accounts from accessing the directory tree, the shell, or other operating system functions and utilities.

**Rule ID:** `SV-240251r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As a rule, accounts on the Lighttpd server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the Lighttpd server. The resources to which these accounts have access must also be closely monitored and controlled. Only the system administrator needs access to all the system's capabilities, while the web administrator and associated staff require access and control of the web content and the Lighttpd server configuration files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: stat -c "%a %g %G %n" `find /opt/vmware/share/htdocs /opt/vmware/etc/lighttpd /opt/vmware/share/lighttpd -type f` | awk '$1 !~ /^..0/ || $3 !~ /root/ {print}' If any files are returned, this is a finding.

## Group: SRG-APP-000211-WSR-000031

**Group ID:** `V-240252`

### Rule: Lighttpd must have the latest version installed.

**Rule ID:** `SV-240252r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing malicious users the capability to traverse server directory tree can create significant vulnerabilities. Such information and the contents of files listed should not be normally readable by the web users as they often contain information relevant to the configuration and security of the web service. Older version of Lighttpd, up to 1.4.34, have been found to be vulnerable to directory traversal and subsequent directory traversal exploits. See CVE-2014-2324 for details.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: /opt/vmware/sbin/vami-lighttpd -v If the Lighttpd version does not have the latest version installed, this is a finding.

## Group: SRG-APP-000225-WSR-000074

**Group ID:** `V-240253`

### Rule: The Lighttpd baseline must be maintained.

**Rule ID:** `SV-240253r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without maintenance of a baseline of current Lighttpd software, monitoring for changes cannot be complete and unauthorized changes to the software can go undetected. Changes to Lighttpd could be the result of intentional or unintentional actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine if a software baseline is being maintained. If a baseline is not being maintained, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-240254`

### Rule: Lighttpd must protect against or limit the effects of HTTP types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-240254r879650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In UNIX and related computer operating systems, a file descriptor is an indicator used to access a file or other input/output resource, such as a pipe or network connection. File descriptors index into a per-process file descriptor table maintained by the kernel, that in turn indexes into a system-wide table of files opened by all processes, called the file table. As a single-threaded server, Lighttpd must be limited in the number of file descriptors that can be allocated. This will prevent Lighttpd from being used in a form of DoS attack against the Operating System.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^server.max-fds' /opt/vmware/etc/lighttpd/lighttpd.conf If the value for "server.max-fds" is not set to "2048", this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-240255`

### Rule: Lighttpd must disable directory browsing.

**Rule ID:** `SV-240255r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If not disabled, the directory listing feature can be used to facilitate a directory traversal exploit. Directory listing must be disabled. Lighttpd provides a configuration setting, dir-listing.activate, that must be set properly in order to globally disable directory listing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^dir-listing.activate' /opt/vmware/etc/lighttpd/lighttpd.conf If the value for "dir-listing.activate" is not set to "disable", this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-240256`

### Rule: Lighttpd must not be configured to use mod_status.

**Rule ID:** `SV-240256r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any application providing too much information in error logs and in administrative messages to the screen risks compromising the data and security of the application and system. The structure and content of error messages needs to be carefully considered by the organization and development team. Lighttpd must only generate error messages that provide information necessary for corrective actions without revealing sensitive or potentially harmful information in error logs and administrative messages. The mod_status module generates the status overview of the webserver. The information covers: uptime average throughput current throughput active connections and their state While this information is useful on a development system, production systems must not have mod_status enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /opt/vmware/etc/lighttpd/lighttpd.conf | awk '/server\.modules/,/\)/' If the "mod_status" module is listed, this is a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-240257`

### Rule: Lighttpd must have debug logging disabled.

**Rule ID:** `SV-240257r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Since this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information. While this information is useful on a development system, production systems must not have debug logging enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^debug.log-request-handling' /opt/vmware/etc/lighttpd/lighttpd.conf If the value for "debug.log-request-handling" is not set to "disable", this is a finding.

## Group: SRG-APP-000315-WSR-000003

**Group ID:** `V-240258`

### Rule: Lighttpd must be configured to utilize the Common Information Model Object Manager.

**Rule ID:** `SV-240258r879692_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be able to enforce remote access policy requirements or work in conjunction with enterprise tools designed to enforce policy requirements. As the web server for the vRA Virtual Appliance Management Interface (vAMI), Lighttpd is the primary remote access management system for vRA. vRA uses CIMOM to Authenticate the sysadmin and to enforce policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /opt/vmware/etc/lighttpd/lighttpd.conf | awk '/cimom/,/}/' Note: The return value should produce the following output: $HTTP["url"] =~ "^/cimom" { proxy.server = ( "" => (( "host" => "127.0.0.1", "port" => "5488" )) ) } If the return value does not match the above output, this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-240259`

### Rule: Lighttpd must restrict inbound connections from nonsecure zones.

**Rule ID:** `SV-240259r879692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be capable of restricting access from what the DoD defines as nonsecure zones. Nonsecure zones are defined as any IP, subnet, or region that is defined as a threat to the organization. The nonsecure zones must be defined for public web servers logically located in a DMZ, as well as private web servers with perimeter protection devices. By restricting access from nonsecure zones, through internal web server access list, the web server can stop or slow denial of service (DoS) attacks on the web server. As the web server for the vRA Virtual Appliance Management Interface (vAMI), Lighttpd is the primary remote access management system for vRA. Lighttpd must be configured to restrict inbound connections from nonsecure zones. To accomplish this, the SSL engine must be enabled. The SSL engine forces Lighttpd to only listen via secure protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -A 4 'remoteip' /opt/vmware/etc/lighttpd/lighttpd.conf If the command does not return any output, this is a finding. Note: The output should look like the following: $HTTP["remoteip"] !~ "a.a.a.a" { url.access-deny = ( "" ) } Where a.a.a.a is an allowed IP address.

## Group: SRG-APP-000358-WSR-000063

**Group ID:** `V-240260`

### Rule: Lighttpd must be configured to use syslog.

**Rule ID:** `SV-240260r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Writing events to a centralized management audit system offers many benefits to the enterprise over having dispersed logs. Centralized management of audit records and logs provides for efficiency in maintenance and management of records, enterprise analysis of events, and backup and archiving of event records enterprise-wide. The web server and related components are required to be capable of writing logs to centralized audit log servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'accesslog.use-syslog' /opt/vmware/etc/lighttpd/lighttpd.conf | grep -v ^# If the value for "accesslog.use-syslog" is not set to "enable" or is missing, this is a finding.

## Group: SRG-APP-000358-WSR-000163

**Group ID:** `V-240261`

### Rule: Lighttpd must be configured to use syslog.

**Rule ID:** `SV-240261r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server will typically utilize logging mechanisms for maintaining a historical log of activity that occurs within a hosted application. This information can then be used for diagnostic purposes, forensics purposes, or other purposes relevant to ensuring the availability and integrity of the hosted application. While it is important to log events identified as being critical and relevant to security, it is equally important to notify the appropriate personnel in a timely manner so they are able to respond to events as they occur. Manual review of the web server logs may not occur in a timely manner, and each event logged is open to interpretation by a reviewer. By integrating the web server into an overall or organization-wide log review, a larger picture of events can be viewed, and analysis can be done in a timely and reliable manner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'accesslog.use-syslog' /opt/vmware/etc/lighttpd/lighttpd.conf | grep -v ^# If the value for "accesslog.use-syslog" is not set to "enable" or is missing, this is a finding.

## Group: SRG-APP-000359-WSR-000065

**Group ID:** `V-240262`

### Rule: The web server must use a logging mechanism that is configured to provide a warning to the ISSO and SA when allocated record storage volume reaches 75% of maximum log record storage capacity.

**Rule ID:** `SV-240262r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process logs as required. Log processing failures include: software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. If log capacity were to be exceeded, then events subsequently occurring would not be recorded. Organizations shall define a maximum allowable percentage of storage capacity serving as an alarming threshold (e.g., web server has exceeded 75% of log storage capacity allocated), at which time the web server or the logging mechanism the web server utilizes will provide a warning to the ISSO and SA at a minimum. This requirement can be met by configuring the web server to utilize a dedicated log tool that meets this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'accesslog.use-syslog' /opt/vmware/etc/lighttpd/lighttpd.conf | grep -v ^# If the value for "accesslog.use-syslog" is not set to "enable" or is missing, this is a finding.

## Group: SRG-APP-000374-WSR-000172

**Group ID:** `V-240263`

### Rule: Lighttpd audit records must be mapped to a time stamp.

**Rule ID:** `SV-240263r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis across multiple devices and log records. Time stamps generated by the web server include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. In order to ensure that Lighttpd is correctly logging timestamps, the accesslog.format setting must be enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'accesslog.format' /opt/vmware/etc/lighttpd/lighttpd.conf | grep -v ^# If no value is returned or if the "accesslog.format" is commented out, this is a finding.

## Group: SRG-APP-000375-WSR-000171

**Group ID:** `V-240264`

### Rule: Lighttpd must record time stamps for log records to a minimum granularity of time.

**Rule ID:** `SV-240264r879748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the web server include date and time and must be to a granularity of one second. In order to ensure that Lighttpd is correctly logging timestamps, the accesslog.format setting must be configured correctly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'accesslog.format' /opt/vmware/etc/lighttpd/lighttpd.conf | grep -v ^# If no value is returned or if the "accesslog.format" is commented out, this is a finding.

## Group: SRG-APP-000380-WSR-000072

**Group ID:** `V-240265`

### Rule: Lighttpd must prohibit non-privileged accounts from accessing the application, libraries, and configuration files.

**Rule ID:** `SV-240265r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As a rule, accounts on the Lighttpd server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the Lighttpd server. The resources to which these accounts have access must also be closely monitored and controlled. Only the system administrator needs access to all the system's capabilities, while the web administrator and associated staff require access and control of the web content and the Lighttpd server configuration files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: stat -c "%a %g %G %n" `find /opt/vmware/share/htdocs /opt/vmware/etc/lighttpd /opt/vmware/share/lighttpd -type f` | awk '$1 !~ /^..0/ || $3 !~ /root/ {print}' If any files are returned, this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-240266`

### Rule: Lighttpd must not be configured to listen to unnecessary ports.

**Rule ID:** `SV-240266r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers must provide the capability to disable or deactivate network-related services that are deemed to be non-essential to the server mission, are too unsecure, or are prohibited by the PPSM CAL and vulnerability assessments. Lighttpd will listen on ports that are specified with the server.port configuration parameter. Lighttpd listens to port 5480 to provide remote access to the Virtual Appliance Management Interface (vAMI). Lighttpd must not be configured to listen to any other port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /opt/vmware/etc/lighttpd/lighttpd.conf | awk '$0 ~ /server\.port/ { print }' If any value returned other than "server.port=5480", this is a finding.

## Group: SRG-APP-000416-WSR-000118

**Group ID:** `V-240267`

### Rule: Lighttpd must be configured with FIPS 140-2 compliant ciphers for https connections.

**Rule ID:** `SV-240267r879944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is optional for a public web server. However, if authentication is being performed, then the use of the TLS protocol is required. Without the use of TLS, the authentication data would be transmitted unencrypted and would become vulnerable to disclosure. Using TLS along with DoD PKI certificates for encryption of the authentication data protects the information from being accessed by all parties on the network. To further protect the authentication data, the web server must use a FIPS 140-2 approved TLS version and all non-FIPS-approved SSL versions must be disabled. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^ssl.cipher-list' /opt/vmware/etc/lighttpd/lighttpd.conf If the value returned in not "ssl.cipher-list = "FIPS: +3DES:!aNULL" "or is commented out, this is a finding.

## Group: SRG-APP-000435-WSR-000147

**Group ID:** `V-240268`

### Rule: Lighttpd must be protected from being stopped by a non-privileged user.

**Rule ID:** `SV-240268r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker has at least two reasons to stop a web server. The first is to cause a DoS, and the second is to put in place changes the attacker made to the web server configuration. To prohibit an attacker from stopping the Lighttpd, the process ID (pid) must be owned by privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ps -f -U root | awk '$0 ~ /vami-lighttpd/ && $0 !~ /awk/ {print}' If the "vami-lighttpd" process is not owned by "root", this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-240269`

### Rule: Lighttpd must be configured to use the SSL engine.

**Rule ID:** `SV-240269r928837_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. In order to protect the integrity and confidentiality of the remote sessions, Lighttpd uses SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: $ grep '^ssl.engine' /opt/vmware/etc/lighttpd/lighttpd.conf If the value returned for "ssl.engine" is not set to "enable", this is a finding.

## Group: SRG-APP-000439-WSR-000152

**Group ID:** `V-240270`

### Rule: Lighttpd must be configured to use the SSL engine.

**Rule ID:** `SV-240270r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. In order to protect the integrity and confidentiality of the remote sessions, Lighttpd uses SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: $ grep '^ssl.engine' /opt/vmware/etc/lighttpd/lighttpd.conf If the value returned for "ssl.engine" is not set to "enable", this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-240271`

### Rule: Lighttpd must use an approved TLS version for encryption.

**Rule ID:** `SV-240271r879810_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications. SSL/TLS is a collection of protocols. Weaknesses have been identified with earlier SSL protocols, including SSLv2 and SSLv3, hence SSL versions 1, 2, and 3 should no longer be used. The best practice for transport layer protection is to only provide support for the TLS protocols - TLS 1.0, TLS 1.1 and TLS 1.2. This configuration will provide maximum protection against skilled and determined attackers and is appropriate for applications handling sensitive data or performing critical operations. Lighttpd must explicitly disable all of the SSL-series protocols. If these protocols are not disabled, the vRA appliance may be vulnerable to a loss of confidentiality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: Note: The command should return 2 outputs: ssl.use-sslv2 and ssl.use-sslv3 grep '^ssl.use-sslv' /opt/vmware/etc/lighttpd/lighttpd.conf If the value returned for "ssl.use-sslv2" and "ssl.use-sslv3" are not set to "disable", this is a finding.

## Group: SRG-APP-000439-WSR-000188

**Group ID:** `V-240272`

### Rule: Lighttpd must remove all export ciphers to transmitted information.

**Rule ID:** `SV-240272r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the web server, the client sends a list of supported cipher suites in order of preference. The Lighttpd will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the web server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^ssl.cipher-list' /opt/vmware/etc/lighttpd/lighttpd.conf If the value returned in not "ssl.cipher-list = "FIPS: +3DES:!aNULL" "or is commented out, this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-240273`

### Rule: Lighttpd must be configured to use SSL.

**Rule ID:** `SV-240273r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. In order to protect the integrity and confidentiality of the remote sessions, Lighttpd uses SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: $ grep '^ssl.engine' /opt/vmware/etc/lighttpd/lighttpd.conf If the value for "ssl.engine" is not set to "enable", this is a finding.

## Group: SRG-APP-000456-WSR-000187

**Group ID:** `V-240274`

### Rule: Lighttpd must have the latest approved security-relevant software updates installed.

**Rule ID:** `SV-240274r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All vRA components, to include Lighttpd, are under VMware configuration management control. The CM process ensures that all patches, functions, and modules have been thoroughly tested before being introduced into the production version. By using the most current version of Lighttpd, the Lighttpd server will always be using the most stable and known baseline.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine whether Lighttpd has the latest approved security-relevant software updates installed. If the latest approved security-relevant software updates are not installed, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-240275`

### Rule: Lighttpd must disable IP forwarding.

**Rule ID:** `SV-240275r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP forwarding permits Lighttpd to forward packets from one network interface to another. The ability to forward packets between two networks is only appropriate for systems acting as routers. Lighttpd is not implemented as a router. With the url.redirect configuration parameter, Lighttpd can be configured to forward IPv4 packets. This configuration parameter is prohibited, unless Lighttpd is redirecting packets to localhost, 127.0.0.1.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E 'url\.redirect' /opt/vmware/etc/lighttpd/lighttpd.conf | grep -v '^#' If any values are returned, this is a finding.

## Group: SRG-APP-000456-WSR-000187

**Group ID:** `V-258452`

### Rule: The version of vRealize Automation 7.x Lighttpd running on the system must be a supported version.

**Rule ID:** `SV-258452r928883_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Automation 7.x Lighttpd is no longer supported by the vendor. If the system is running vRealize Automation 7.x Lighttpd, this is a finding.

