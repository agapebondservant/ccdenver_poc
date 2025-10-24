# STIG Benchmark: VMware vSphere 7.0 vCenter Appliance RhttpProxy Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-256737`

### Rule: Envoy must drop connections to disconnected clients.

**Rule ID:** `SV-256737r889149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy client connections that are established but no longer connected can consume resources that might otherwise be required by active connections. It is a best practice to terminate connections that are no longer connected to an active client. Envoy is hard coded to drop connections after three minutes of idle time. The absence of any "tcpKeepAliveTimeSec" settings means this default is in effect. This configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/config/envoy/L4Filter/tcpKeepAliveTimeSec/text()' /etc/vmware-rhttpproxy/config.xml Expected result: 180 or XPath set is empty If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-256738`

### Rule: Envoy must set a limit on established connections.

**Rule ID:** `SV-256738r889152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy client connections must be limited to preserve system resources and continue servicing connections without interruption. Without a limit set, the system would be vulnerable to a trivial denial-of-service attack where connections are created en masse and vCenter resources are entirely consumed. Envoy comes hard coded with a tested and supported value for "maxHttpsConnections" that must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/config/envoy/L4Filter/maxHttpsConnections/text()' /etc/vmware-rhttpproxy/config.xml Expected result: 2048 or XPath set is empty If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-256739`

### Rule: Envoy must be configured to operate in FIPS mode.

**Rule ID:** `SV-256739r889155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy ships with FIPS 140-2 validated OpenSSL cryptographic libraries and is configured by default to run in FIPS mode. This module is used for all cryptographic operations performed by Envoy, including protection of data-in-transit over the client Transport Layer Security (TLS) connection. Satisfies: SRG-APP-000014-WSR-000006, SRG-APP-000179-WSR-000111, SRG-APP-000416-WSR-000118, SRG-APP-000439-WSR-000188, SRG-APP-000179-WSR-000110</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/config/vmacore/ssl/fips' /etc/vmware-rhttpproxy/config.xml Expected result: <fips>true</fips> If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-256740`

### Rule: Envoy must use only Transport Layer Security (TLS) 1.2 for the protection of client connections.

**Rule ID:** `SV-256740r889158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy can be configured to support TLS 1.0, 1.1, and 1.2. Due to intrinsic problems in TLS 1.0 and TLS 1.1, they are disabled by default. The <protocol> block in the rhttpproxy configuration is commented out by default, and this configuration forces TLS 1.2. The block may also be set to "tls1.2" in certain upgrade scenarios, but the effect is the same. Uncommenting the block and enabling older protocols is possible; therefore, TLS 1.2 restriction must be verified and maintained. Satisfies: SRG-APP-000015-WSR-000014, SRG-APP-000172-WSR-000104, SRG-APP-000439-WSR-000151, SRG-APP-000439-WSR-000152, SRG-APP-000439-WSR-000156, SRG-APP-000441-WSR-000181, SRG-APP-000442-WSR-000182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/config/vmacore/ssl/protocols' /etc/vmware-rhttpproxy/config.xml Expected result: XPath set is empty or <protocols>tls1.2</protocols> If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000176-WSR-000096

**Group ID:** `V-256741`

### Rule: The Envoy private key file must be protected from unauthorized access.

**Rule ID:** `SV-256741r889161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy's private key is used to prove the identity of the server to clients and securely exchange the shared secret key used to encrypt communications between the web server and clients. By gaining access to the private key, an attacker can pretend to be an authorized server and decrypt the Transport Layer Security (TLS) traffic between a client and the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At  the command prompt, run the following command: # stat -c "%n permissions are %a, is owned by %U and group owned by %G" /etc/vmware-rhttpproxy/ssl/rui.key Expected result: /etc/vmware-rhttpproxy/ssl/rui.key permissions are 600, is owned by root and group owned by root If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000315-WSR-000003

**Group ID:** `V-256742`

### Rule: Envoy must exclusively use the HTTPS protocol for client connections.

**Rule ID:** `SV-256742r889164_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remotely accessing vCenter via Envoy involves sensitive information going over the wire. To protect the confidentiality and integrity of these communications, Envoy must be configured to use an encrypted session of HTTPS rather than plain-text HTTP. The Secure Sockets Layer (SSL) configuration block inside the rhttpproxy configuration must be present and correctly configured to safely enable Transport Layer Security (TLS).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/config/ssl' /etc/vmware-rhttpproxy/config.xml Expected result: <ssl> <!-- The server private key file --> <privateKey>/etc/vmware-rhttpproxy/ssl/rui.key</privateKey> <!-- The server side certificate file --> <certificate>/etc/vmware-rhttpproxy/ssl/rui.crt</certificate> <!-- vecs server name. Currently vecs runs on all node types. --> <vecsServerName>localhost</vecsServerName> </ssl> If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000358-WSR-000063

**Group ID:** `V-256743`

### Rule: Envoy (rhttpproxy) log files must be shipped via syslog to a central log server.

**Rule ID:** `SV-256743r889167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy produces several logs that must be offloaded from the originating system. This information can then be used for diagnostic purposes, forensics purposes, or other purposes relevant to ensuring the availability and integrity of the hosted application. Envoy (rhttpproxy) rsyslog configuration is included in the "VMware-visl-integration" package and unpacked to "/etc/vmware-syslog/vmware-services-rhttpproxy.conf". Ensuring the package hashes are as expected also ensures the shipped rsyslog configuration is present and unmodified.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # rpm -V VMware-visl-integration|grep vmware-services-rhttpproxy.conf|grep "^..5......" If the command returns any output, this is a finding.

## Group: SRG-APP-000358-WSR-000063

**Group ID:** `V-256744`

### Rule: Envoy log files must be shipped via syslog to a central log server.

**Rule ID:** `SV-256744r889170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Envoy rsyslog configuration is included in the "VMware-visl-integration" package and unpacked to "/etc/vmware-syslog/vmware-services-envoy.conf". Ensuring the package hashes are as expected also ensures the shipped rsyslog configuration is present and unmodified.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # rpm -V VMware-visl-integration|grep vmware-services-envoy.conf|grep "^..5......" If the command returns any output, this is a finding.

