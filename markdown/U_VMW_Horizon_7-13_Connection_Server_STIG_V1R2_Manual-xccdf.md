# STIG Benchmark: VMware Horizon 7.13 Connection Server Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-AS-000001

**Group ID:** `V-246882`

### Rule: The Horizon Connection Server must limit the number of concurrent client sessions.

**Rule ID:** `SV-246882r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Connection Server has the ability to limit the number of simultaneous client connections. This capability is helpful in limiting resource exhaustion risks related to denial of service attacks. By default, in code, the Connection Server allows up to 2000 client connections at one time, over all protocol types. For larger deployments, this limit can be increased to a tested and supported maximum of 4000 by making modifications to the "locked.properties" file. Ensure any changes to the number of allowed simultaneous connections is supported by VMware for the choice of protocols and that this value is documented as part of the SSP. Satisfies: SRG-APP-000001-AS-000001, SRG-APP-000435-AS-000163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, this is NOT a finding. Open "locked.properties" in a text editor. Find the "maxConnections" setting. The "maxConnections" setting may be set higher than the default of "2000" (up to 4000) in certain, large Horizon deployments. If there is no "maxConnections" setting, this is NOT a finding. If "maxConnections" is set to more than "4000", this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-246883`

### Rule: The Horizon Connection Server must be configured to only support TLS 1.2 connections.

**Rule ID:** `SV-246883r879520_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the application server take measures to employ strong cryptographic mechanisms to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for Government systems. According to NIST and as of publication, TLS 1.1 must not be used and TLS 1.2 will be configured. Note: Mandating TLS 1.2 may affect certain client types. Test and implement carefully. Satisfies: SRG-APP-000015-AS-000010, SRG-APP-000014-AS-000009, SRG-APP-000156-AS-000106, SRG-APP-000172-AS-000120, SRG-APP-000439-AS-000155, SRG-APP-000439-AS-000274 , SRG-APP-000440-AS-000167, SRG-APP-000442-AS-000259</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, confirm with the SA if TLS 1.2 was enforced at a global level via ADSI EDIT. If no such global change was made, this is a finding. Open "locked.properties" in a text editor. Find the "secureProtocols.1" and "preferredSecureProtocol" settings. Ensure they are set as follows: secureProtocols.1=TLSv1.2 preferredSecureProtocol=TLSv1.2 If there is a "secureProtocols.2" or "secureProtocols.3" setting, this is a finding. If the "secureProtocols.1" and "preferredSecureProtocol" are not exactly as above, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-246884`

### Rule: The Blast Secure Gateway must be configured to only support TLS 1.2 connections.

**Rule ID:** `SV-246884r879520_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the application server take measures to employ strong cryptographic mechanisms to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for Government systems. According to NIST and as of publication, TLS 1.1 must not be used and TLS 1.2 will be configured. Note: Mandating TLS 1.2 may affect certain client types. Test and implement carefully.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\appblastgateway". If a file named "absg.properties" does not exist in this path, this is a finding. Open "absg.properties" in a text editor. Find the "localHttpsProtocolLow" and "localHttpsProtocolHigh" settings. Ensure they are set as follows: localHttpsProtocolLow=tls1.2 localHttpsProtocolHigh=tls1.2 If the "localHttpsProtocolLow" or "localHttpsProtocolHigh" settings do not exist, this is a finding. If the "localHttpsProtocolLow" and "localHttpsProtocolHigh" are not exactly as above, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-246885`

### Rule: The Horizon Connection Server must force server cipher preference.

**Rule ID:** `SV-246885r879520_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, during the initial setup of a Transport Layer Security (TLS) connection to the Horizon Connection Server, the client sends a list of supported cipher suites in order of preference. The Connection Server replies with the cipher suite it will use for communication, chosen from the client list. This is not ideal since the untrusted client is setting the boundaries and conditions for the connection to proceed. The client could potentially specify known weak cipher combinations that would make the communication more susceptible to interception. By adding the "honorClientOrder" setting to the locked.properties file, the Connection Server will reject the client preference and force the client to choose from the server ordered list of preferred ciphers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, confirm with the SA if forcing server-side cipher order was enforced at a global level via ADSI EDIT. If no such global change was made, this is a finding. Open "locked.properties" in a text editor. Find the "honorClientOrder" setting. Ensure they are set as follows: secureProtocols.1=TLSv1.2 preferredSecureProtocol=TLSv1.2 If there is no "honorClientOrder" setting, this is a finding. If the "honorClientOrder" is not set to "false", this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-246886`

### Rule: The Horizon Connection Server must be configured to debug level logging.

**Rule ID:** `SV-246886r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure that all security-relevant information and events are logged, the Horizon Connection Server must be configured with the "debug" logging level. This is the default value but since it could be changed to "info", this configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, launch the Registry Editor. Traverse the registry tree to "HKLM\Software\VMware, Inc.\VMware VDM". Locate the "DebugEnabled" key. If "DebugEnabled" does not exist, this is NOT a finding. If "DebugEnabled" does not have a value of "true", this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-246887`

### Rule: The Horizon Connection Server administrators must be limited in terms of quantity, scope, and permissions.

**Rule ID:** `SV-246887r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Role based access and least privilege are two fundamental security concepts that must be properly implemented in Horizon View to ensure the right user and groups have the right permissions on the right objects. Horizon View allows for assigning of roles (pre-defined sets of permissions) to specific users and groups and on a specific Access Group (set of objects). Administrators must ensure that minimal permissions are assigned to the right entities, in the right scope, and stay so over time. Satisfies: SRG-APP-000033-AS-000024, SRG-APP-000118-AS-000078, SRG-APP-000121-AS-000081, SRG-APP-000122-AS-000082, SRG-APP-000123-AS-000083, SRG-APP-000290-AS-000174, SRG-APP-000315-AS-000094, SRG-APP-000340-AS-000185, SRG-APP-000343-AS-000030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Administrators. From the "Administrators and Groups" tab, review each user and group in the left pane and their associated roles in the right pane. Anyone with any privilege can log on to the Console and view potentially sensitive configurations, system details, and events. If there are any users or groups that should not be viewed as trusted "Administrators" of the Horizon system, this is a finding. Permissions must be as restrictive as possible and their scope (Access Group) as limited as possible. Ensure no user or group has unnecessary permissions and that their Access Group is appropriately limited. Pay special attention to the "Local Administrator" and "Administrator" roles on the root Access Group as those user and groups have total control over the environment local and global environment, respectively. If any user or group has permissions that are greater than the minimum necessary, this is a finding. If any user or group has any permissions on an overly broad access group, this is a finding.

## Group: SRG-APP-000080-AS-000045

**Group ID:** `V-246888`

### Rule: The Horizon Connection Server must require DoD PKI for administrative logins.

**Rule ID:** `SV-246888r879554_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Horizon Connection Server console supports CAC login as required for cryptographic non-repudiation. CAC login can be configured as disabled, optional or required but for maximum assurance it must be set to "required". Setting CAC login as "optional" may be appropriate at some sites to support a "break glass" scenario where PKI is failing but there is an emergency access account configured with username/password. Satisfies: SRG-APP-000080-AS-000045, SRG-APP-000149-AS-000102, SRG-APP-000151-AS-000103, SRG-APP-000153-AS-000104, SRG-APP-000177-AS-000126, SRG-APP-000392-AS-000240, SRG-APP-000391-AS-000239, SRG-APP-000403-AS-000248</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon Connection Server Console. From the left pane, navigate to Settings >> Servers. In the right pane, select the "Connection Servers" tab. For each Connection Server listed, select the server and click "Edit". Click the "Authentication" tab. Scroll down to "Horizon Administrator Authentication". Find the value in the drop down next to "Smart card authentication for administrators". If "Smart card authentication for administrators" is not set to "Required", this is a finding. NOTE: If another form of DoD approved PKI is used, and configured to be required for administrative logins, this is not a finding.

## Group: SRG-APP-000089-AS-000050

**Group ID:** `V-246889`

### Rule: The Horizon Connection Server must be configured with an events database.

**Rule ID:** `SV-246889r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Connection Server stores application level events and actions in a dedicated database versus log files. This makes day-to-day administration easier while offloading these events to a separate system for resiliency. An events database is configured after Connection Server deployment. It need only be done once, in the case of multiple grouped Connection Servers, as the configuration will be applied to the other servers automatically. Satisfies: SRG-APP-000089-AS-000050, SRG-APP-000091-AS-000052, SRG-APP-000095-AS-000056, SRG-APP-000096-AS-000059, SRG-APP-000097-AS-000060, SRG-APP-000098-AS-000061, SRG-APP-000099-AS-000062, SRG-APP-000100-AS-000063, SRG-APP-000101-AS-000072, SRG-APP-000266-AS-000168, SRG-APP-000380-AS-000088, SRG-APP-000495-AS-000220, SRG-APP-000499-AS-000224, SRG-APP-000503-AS-000228, SRG-APP-000504-AS-000229, SRG-APP-000505-AS-000230, SRG-APP-000509-AS-000234</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Monitor >> Events. If the right pane is empty or shows "Events DB is not configured.", this is a finding.

## Group: SRG-APP-000090-AS-000051

**Group ID:** `V-246890`

### Rule: The Horizon Connection Server must limit access to the global configuration privilege.

**Rule ID:** `SV-246890r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Connection Server comes with pre-defined privileges that can be combined in any combination into a role. That role is then assigned to a user or group. Any role that has the "Manage Global Configuration and Policies" has the ability to change the configuration of the Connection Server, including the events database. This privilege must be restricted and monitored over time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Administrators. From the "Role Privileges" tab, review each role in the left pane and their associated privileges in the right pane. Note any role with the "Manage Global Configuration and Policies" privilege. Switch to the "Role Permissions" tab. For each noted role, if there are any users or group listed who are not permitted to change the events database configuration, this is a finding.

## Group: SRG-APP-000175-AS-000124

**Group ID:** `V-246891`

### Rule: The Horizon Connection Server must perform full path validation on server-to-server TLS connection certificates.

**Rule ID:** `SV-246891r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Connection Server performs certificate revocation checking on its own certificate and on those of the security servers paired to it. Each instance also checks the certificates of vCenter and View Composer servers whenever it establishes a connection to them. If a SAML 2.0 authenticator is configured for use by a Connection Server instance, the Connection Server also performs certificate revocation checking on the SAML 2.0 server certificate. By default, all certificates in the chain are checked except the root certificate. This must be changed so that the full path, including the root, is validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, launch the Registry Editor. Traverse the registry tree to "HKLM\Software\VMware, Inc.\VMware VDM\Security". Locate the "CertificateRevocationCheckType" key. If the "CertificateRevocationCheckType" key does not exist, this is a finding. If the "CertificateRevocationCheckType" key does not have a value of "3", this is a finding.

## Group: SRG-APP-000175-AS-000124

**Group ID:** `V-246892`

### Rule: The Horizon Connection Server must validate client and administrator certificates.

**Rule ID:** `SV-246892r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Connection Server can be configured to check the revocation status of PKI certificates over both OCSP and CRL. This capability is disabled by default and must be enabled post-deployment. There are a number of other configurations that are supported, including OCSP and CRL location override but those will be site and architecture specific. The suggested configuration is OCSP with failover to CRL and override the AIA locations via a local OCSP responder, if present. See below: enableRevocationChecking=true ocspCRLFailover=true ocspSendNonce=true enableOCSP=true allowCertCRLs=false crlLocation=http://<crl.myagency.mil> ocspURL=http://<ca.myagency.mil/ocsp ocspSigningCert=ca.myagency.mil.cer Set enableRevocationChecking to true to enable smart card certificate revocation checking. Set ocspCRLFailover to enable CRL checking is OCSP fails. Set ocspSendNonce to true to prevent OCSP repeated responses. Set enableOCSP to true to enable OCSP certificate revocation checking. Set allowCertCRLs to false to disable pulling the CRL distribution point from the certificate. Set crlLocation to the local file of http URL to use for the CRL distribution point. Set ocspURL to the URL of the OCSP Responder. Set ocspSigningCert to the location of the file that contains the OCSP Responder's signing certificate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, this is a finding. Open "locked.properties" in a text editor. Find the "enableRevocationChecking" setting. If "enableRevocationChecking" does not exist, this is a finding. If "enableRevocationChecking" is not set to "true", this is a finding.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-246893`

### Rule: The Horizon Connection Server must only use FIPS 140-2 validated cryptographic modules.

**Rule ID:** `SV-246893r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms or poor implementation. The Horizon Connection Server can be configured to exclusively use FIPS 140-2 validated cryptographic modules but only at installation time, not post deployment. Reference VMware documentation for up-to-date requirements for enabling FIPS in Horizon View. Satisfies: SRG-APP-000179-AS-000129, SRG-APP-000224-AS-000152, SRG-APP-000416-AS-000140</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, launch an elevated command prompt. Run the following commands: # cd C:\ProgramData\VMware\VDM # findstr /C:"Broker started in FIPS mode" log-*.txt If the "findstr" command produces no output, this is a finding.

## Group: SRG-APP-000220-AS-000148

**Group ID:** `V-246894`

### Rule: The Horizon Connection Server must time out administrative sessions after 15 minutes or less.

**Rule ID:** `SV-246894r879637_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If communications sessions remain open for extended periods of time even when unused, there is the potential for an adversary to hijack the session and use it to gain access to the system. Horizon 7 Console sessions can and must be limited in the amount of idle time that will be allowed before automatic logoff. By default, 30 minutes of idle time is allowed but this must be changed to 15 minutes or less for DoD systems. This configuration must be verified and maintained over time. Satisfies: SRG-APP-000220-AS-000148, SRG-APP-000295-AS-000263, SRG-APP-000389-AS-000253</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Global Settings. In the right pane, click the "General Settings" tab. Find the “Connection Server Session Timeout” value. If "Connection Server Session Timeout" is set to more than 15 minutes, this is a finding.

## Group: SRG-APP-000267-AS-000170

**Group ID:** `V-246895`

### Rule: The Horizon Connection Server must protect log files from unauthorized access.

**Rule ID:** `SV-246895r879656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Error logs can contain sensitive information about system errors and system architecture that need to be protected from unauthorized access and modification. By default, Horizon Connection Server logs are only accessible by local windows Administrators. This configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "C:\ProgramData\VMware\VDM". Right-click the "logs" folder and select "Properties". Change to the "Security" tab. By default, only built-in system accounts such as "SYSTEM" and "NETWORK SERVICE" plus the local "Administrators" group have access to the "logs" folder. If any other groups have any permissions on this folder, this is a finding.

## Group: SRG-APP-000358-AS-000064

**Group ID:** `V-246896`

### Rule: The Horizon Connection Server must offload events to a central log server in real time.

**Rule ID:** `SV-246896r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Centralized management of log records provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. The Horizon Connection Server can be configured to send all events to a syslog receiver. Multiple servers can be configured but only the UDP protocol is supported at this time. Satisfies: SRG-APP-000358-AS-000064, SRG-APP-000515-AS-000203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Event Configuration. The configured syslog servers are located in the right pane under "Syslog". If there are no valid syslog servers configured, this is a finding.

## Group: SRG-APP-000427-AS-000264

**Group ID:** `V-246897`

### Rule: The Horizon Connection Server must be configured with a DoD-issued TLS certificate.

**Rule ID:** `SV-246897r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority (CA). If the CA used for verifying the certificate is not DoD-approved, trust of this CA has not been established. The Horizon Connection Server supports the replacement of the default, self-signed certificate with one issued by the DoD. This is accomplished through the normal Windows Server certificate management tools, focusing on the certificate with the "vdm"-friendly name. Satisfies: SRG-APP-000427-AS-000264, SRG-APP-000514-AS-000137</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, open "certlm.msc or certmgr.msc" (Certificate Management - Local Computer). Select Personal >> Certificates. In the right pane, locate the certificate with the "Friendly Name" of "vdm". For this certificate, locate the issuer in the "Issued By" column. If the Horizon Connection Server broker certificate is not "Issued By" a trusted DoD CA, or other AO-approved certificate, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246898`

### Rule: The Horizon Connection Server must reauthenticate users after a network interruption.

**Rule ID:** `SV-246898r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Given the remote access nature of Horizon Connection Server, the client must be ensured to be under positive control as much as is possible from the server side. As such, whenever a network interruption causes a client disconnect, that session must be reauthenticated upon reconnection. To allow a session resumption would be convenient but would allow for the possibility of the endpoint being taken out of the control of the intended user and reconnected to a different network, in control of a bad actor who could then resume the disconnected session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Global Settings. In the right pane, click the "Security Settings" tab. Locate the "Reauthenticate Secure Tunnel Connections After Network Interruption" setting. If the "Reauthenticate Secure Tunnel Connections After Network Interruption" setting is set to "No", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246899`

### Rule: The Horizon Connection Server must disconnect users after a maximum of ten hours.

**Rule ID:** `SV-246899r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Horizon Connection Server is intended to provide remote desktops and applications, generally during working hours and for no more than an extended workday. Leaving sessions active for more than what is reasonable for a work day leaves open the possibility of a session becoming unoccupied and insecure on the client side. For example, if a client connection is opened at 0900, there are few day-to-day reasons that the connection should still be open after 1900, therefore the connection must be terminated. If the user is still active, they can reauthenticate immediately and get back on for another ten hours.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Global Settings. In the right pane, click the "General Settings" tab. Locate the "Forcibly Disconnect Users" setting. If the "Forcibly Disconnect Users" setting is set to "Never", this is a finding. If the "Forcibly Disconnect Users" setting is set to greater than "600" minutes (ten hours), this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246900`

### Rule: The Horizon Connection Server must disconnect applications after two hours of idle time.

**Rule ID:** `SV-246900r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Horizon View is intended to provide remote desktops and applications during for more or less continuous use. If an application is open and goes used for more than two hours, that application must be closed to eliminate the risk of that idle application being usurped. For desktops, sessions will not be disconnected after two hours but the credentials stored with Horizon will be invalidated. Subsequent desktop connection attempts will require reauthentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Global Settings. In the right pane, click the "General Settings" tab. Locate the "Disconnect Applications and Discard SSO Credentials for Idle Users" setting. If the "Disconnect Applications and Discard SSO Credentials for Idle Users" setting is set to "Never", this is a finding. If the "Disconnect Applications and Discard SSO Credentials for Idle Users" setting is set to greater than "120" minutes (two hours), this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246901`

### Rule: The Horizon Connection Server must discard SSO credentials after 15 minutes.

**Rule ID:** `SV-246901r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Horizon Connection Server caches user credentials temporarily to ensure that the user can connect to their desktop pools without reauthenticating, right after logging in to the broker. However, this grace period must be restricted so that SSO credentials are only retained for 15 minutes before being discarded. Subsequent desktop connection attempts will require reauthentication, even if the user is still connected to the broker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Global Settings. In the right pane, click the "General Settings" tab. Locate the "Discard SSO credentials" setting. If the "Discard SSO Credentials" setting is set to "Never", this is a finding. If the "Discard SSO Credentials" setting is set to greater than "15 minutes", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246902`

### Rule: The Horizon Connection Server must not accept pass-through client credentials.

**Rule ID:** `SV-246902r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Horizon Connection Server has the ability to allow clients to authenticate using the local session credentials of their local endpoint. While convenient, this must be disabled for DoD deployments as the server cannot ascertain the method of endpoint login, whether that user's client certificate has since been revoked, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Servers. In the right pane, select the "Connection Servers" tab. For each Connection Server listed, select the server and click "Edit". Click the "Authentication" tab. Scroll down to the "Current User Authentication" and note the "Accept logon as current user" checkbox. If the "Accept logon as current user" checkbox is checked, this is a finding. Note: If "Smart card authentication for users" is set to "Required", this setting is automatically disabled and greyed out. This would be not applicable.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246903`

### Rule: The Horizon Connection Server must require DoD PKI for client logins.

**Rule ID:** `SV-246903r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Before clients can pick a desktop or app to access, they must first authenticate to the broker, the Connection Server itself. If the client is accessing the broker directly, then the allowed authentication methods must be specified. These include RADIUS, SecurID, user/pass and smart card. In the DoD, CAC login must be enforced at all times, for all client connections. If the client is connecting through a Security Server or the UAG appliance, this requirement does not apply.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Servers. In the right pane, select the "Connection Servers" tab. For each Connection Server listed, select the server and click "Edit". Click the "Authentication" tab. Under "Horizon Authentication", find the value in the dropdown below "Smart card authentication for users". If "Smart card authentication for users" is set to "Optional" or "Not Allowed", a SAML Authenticator must be configured and that external IdP must be configured to require CAC authentication. If these requirements are not met, this is a finding. If "Smart card authentication for users" is set to "Required" on each of the listed Connection Servers, this is not a finding. Note: If the Connection Server is paired with a Security Server, this requirement is not applicable on the Connection Server but is applicable on the Security Server. NOTE: If another form of DoD approved PKI is used, and configured to be required for client logins, this is not a finding. If the Connection Server is paired with a Unified Access Gateway (UAG) that is performing authentication, this requirement is not applicable.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246904`

### Rule: The Horizon Connection Server must backup its configuration daily.

**Rule ID:** `SV-246904r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Servers. In the right pane, select the "Connection Servers" tab. For each Connection Server listed, select the server and click "Edit". Select the "Backup" tab. Validate that "Automatic backup frequency" is set to a least "Every day". If the Connection Server is not set to be backed up daily (or less), this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246905`

### Rule: The Horizon Connection Server Instant Clone domain account must be configured with limited permissions.

**Rule ID:** `SV-246905r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Instant Clone Domain Accounts. In the right pane, validate that the accounts listed are User accounts in Active Directory and have only the following permissions on the container for the instant-clone computer account: List Contents Read All Properties Write All Properties Read Permissions Reset Password Create Computer Objects Delete Computer Objects Ensure the permissions apply to the correct container and to all child objects of the container. If the Instant Clone domain account has more than the minimum required permissions, this is a finding. Note: If Instant Clones is not used, this is not applicable.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246906`

### Rule: The Horizon Connection Server must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-246906r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, launch the Registry Editor. Traverse the registry tree to "HKLM\Software\VMware, Inc.\VMware VDM\Plugins\wsnm\TunnelService\Params". Locate the "JvmOptions" key. If "JvmOptions" does not exist, or the path does not exist, this is NOT a finding. If "JvmOptions" does not include the "-Djdk.tls.rejectClientInitiatedRenegotiation=true" option, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246907`

### Rule: The Horizon Connection Server must have X-Frame-Options enabled.

**Rule ID:** `SV-246907r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>RFC 7034 HTTP Header Field X-Frame-Options, also known as counter clickjacking, is enabled by default on the Horizon Connection Server. It can be disabled by adding the entry "x-frame-options=OFF" to the locked.properties file, usually for troubleshooting purposes. The default configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, this is NOT a finding. Open "locked.properties" in a text editor. Find the "X-Frame-Options" setting. If there is no "X-Frame-Options" setting, this is NOT a finding. If "X-Frame-Options" is set to "OFF", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246908`

### Rule: The Horizon Connection Server must have Origin Checking enabled.

**Rule ID:** `SV-246908r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>RFC 6454 Origin Checking, which protects against cross-site request forging, is enabled by default on the Horizon Connection Server. When an administrator opens the Horizon 7 Console or a user connects to Blast HTML Access, the server checks that the origin URL for the web request matches the configured secure tunnel URL or "localhost". When the Connection Server is load balanced or front-ended by a Unified Access Gateway (UAG) appliance, origin checking will fail. This is commonly resolved by disabling origin checking entirely by specifying "checkOrigin=false" in the "locked.properties" file. This is not the proper solution. Instead, origin checking must be enabled and the load balancer and UAG appliances must be allowlisted via the "balancedHost" and "portalHost.X" settings in "locked.properties", respectively. Origin checking can be disabled by adding the entry "checkOrigin=false" to locked.properties, usually for troubleshooting purposes. The default, "checkOrigin=true" or unspecified configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, this is NOT a finding. Open "locked.properties" in a text editor. Find the "checkOrigin" setting. If there is no "checkOrigin" setting, this is NOT a finding. If "checkOrigin" is set to "false", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246909`

### Rule: The Horizon Connection Server must enable the Content Security Policy.

**Rule ID:** `SV-246909r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Connection Server Content Security Policy (CSP) feature mitigates a broad class of content injection vulnerabilities, such as cross-site scripting (XSS), clickjacking and other code injection attacks resulting from execution of malicious content in the trusted web page context. The Connection Server defines the policy and the client browser enforces the policy. This feature is enabled by default but must be validated and maintained over time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, this is NOT a finding. Open "locked.properties" in a text editor. Find the "enableCSP" setting. If there is no "enableCSP" setting, this is NOT a finding. If "enableCSP" is set to "false", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246910`

### Rule: The Horizon Connection Server must enable the proper Content Security Policy directives.

**Rule ID:** `SV-246910r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Connection Server Content Security Policy (CSP) feature mitigates a broad class of content injection vulnerabilities such as cross-site scripting (XSS), clickjacking and other code injection attacks resulting from execution of malicious content in the trusted web page context. The Connection Server has default CSP directives that block XSS attacks, enable x-frame restrictions and more. If the default configurations are overridden, the protections may be disabled even though the CSP itself is still enabled. This default policy must be validated and maintained over time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, this is NOT a finding. Open "locked.properties" in a text editor. Find the following settings: content-security-policy content-security-policy-newadmin content-security-policy-portal content-security-policy-rest If any of the above settings are present, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246911`

### Rule: The PCoIP Secure Gateway must be configured with a DoD-issued TLS certificate.

**Rule ID:** `SV-246911r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority (CA). If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The Blast Secure Gateway supports the replacement of the default, self-signed certificate with one issued by the DoD. This is accomplished through the normal Windows Server certificate management tools. For simplicity, it is recommended to use the same certificate as previously configured for Connection Server itself via the "vdm" common name.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, launch the Registry Editor. Traverse the registry tree to "HKEY_LOCAL_MACHINE\SOFTWARE\Teradici\SecurityGateway". Locate the "SSLCertWinCertFriendlyName" key. If "SSLCertWinCertFriendlyName" does not exist, this is a finding. If "SSLCertWinCertFriendlyName" is set to "vdm", this is not a finding. Note the value of "SSLCertWinCertFriendlyName". This is the friendly name of the PCoIP Secure Gateway certificate. On the Horizon Connection Server, open "certlm.msc or certmgr.msc" (Certificate Management - Local Computer). Select Personal >> Certificates. In the right pane, locate the certificate with the "Friendly Name" of the previously noted value of "SSLCertWinCertFriendlyName". For this certificate, locate the issuer in the "Issued By" column. If the PCoIP Secure Gateway certificate is not "Issued By" a trusted DoD CA, this is a finding. Note: If the PCoIP Secure Gateway is not enabled, this is not applicable.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246912`

### Rule: The Horizon Connection Server must not allow unauthenticated access.

**Rule ID:** `SV-246912r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the Horizon native smart card capability is not set to "Required", the option for "Unauthenticated Access" is enabled. This would be true in the case of an external IdP providing authentication via SAML. The "Unauthenticated Access" option allows users to access published applications from a Horizon Client without requiring AD credentials. This is typically implemented as a convenience when serving up an application that has its own security and user management. This configuration is not acceptable in the DoD and must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Servers. In the right pane, select the "Connection Servers" tab. For each Connection Server listed, select the server and click "Edit". Click the "Authentication" tab. Under "Horizon Authentication", find the value in the drop-down below "Unauthenticated Access". If "Unauthenticated Access" is set to "Enabled", this is a finding. Note: If "Smart card authentication for users" is set to "Required", this setting is automatically disabled and greyed out. This would be not applicable.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246913`

### Rule: The Horizon Connection Server must require CAC reauthentication after user idle timeouts.

**Rule ID:** `SV-246913r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user VDI session times out due to activity, the user must be assumed to not be active and have their resource locked. These resources should only be made available again upon the user reauthenticating versus reusing the initial connection. This ensures that the connection has not been hijacked and re-stablishes nonrepudiation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Global Settings. In the right pane, click the "General Settings" tab. Locate the "Enable 2-Factor Reauthentication" setting. If the "Enable 2-Factor Reauthentication" setting is set to "No", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246914`

### Rule: The Horizon Connection Server must be configured to restrict USB passthrough access.

**Rule ID:** `SV-246914r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One of the many benefits of VDI is the separation of the end user from the "desktop" they are accessing. This helps mitigate the risks imposed by physical access. In a traditional desktop scenario, and from a security perspective, physical access is equivalent to ownership. USB devices are physical devices that interact at the driver layer with the guest operating system and are inherently problematic. There are numerous risks posed by USB including the driver stack, data loss prevention, malicious devices, etc. Client USB devices are not necessary for general purpose VDI desktops and must be disabled broadly and enabled selectively. Note: USB mouse, keyboard and smart card devices are abstracted by Horizon and are not affected by any of these Horizon configurations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA. USB devices can be blocked in a number of ways: 1. The desktop OS 2. A third party DLP solution 3. Horizon Agent configuration and GPOs 4. Horizon Connection Server global policies 5. Horizon Connection Server per-pool policies If 1, 2, or 3 are implemented in this environment, this control is not applicable. Number three is addressed in the Horizon Agent STIG. Step One - Disable USB Access Globally: Log in to the Horizon 7 Console. From the left pane, navigate to Settings >> Global Policies. In the right pane, confirm that "USB Access" is set to "Deny". If "USB Access" is not set to "Deny", this is a finding. Step Two - Confirm per-pool settings: Log in to the Horizon 7 Console. From the left pane, navigate to Inventory >> Desktops. In the right pane, click the name of each pool that does not explicitly require access to USB devices. In the next screen, click the "Policies" tab. Confirm that "Applied Policy" is set to "Deny". If "Applied Policy" is not set to "Deny", this is a finding. Click the "Policy Overrides" tab. Highlight each user. If "USB Access" is set to "Allow" for any user, ensure the exception is required and authorized. If any user has an override configured that is not required or authorized, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246915`

### Rule: The Horizon Connection Server must prevent MIME type sniffing.

**Rule ID:** `SV-246915r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MIME types define how a given type of file is intended to be processed by the browser. Modern browsers are capable of determining the content type of a file by byte headers and content inspection and can then override the type dictated by the server. An example would be a ".js" that was sent as the "jpg" mime type vs the JavaScript mime type. The browser would "correct" this and process the file as JavaScript. The danger is that a given file could be disguised as something else on the server, like JavaScript, opening up the door to cross-site scripting. To disable browser "sniffing" of content type, the Connection Server sends the "x-content-type-options: nosniff" header by default. This configuration must be validated and maintained over time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Horizon Connection Server, navigate to "<install_directory>\VMware\VMware View\Server\sslgateway\conf". If a file named "locked.properties" does not exist in this path, this is NOT a finding. Open "locked.properties" in a text editor. Find the "x-content-type-options" setting. If there is no "x-content-type-options" setting, this is NOT a finding. If "x-content-type-options" is set to "false", this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-246916`

### Rule: All Horizon components must be running supported versions.

**Rule ID:** `SV-246916r951010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Horizon 7.x is no longer supported by the vendor. If any of the system components are running Horizon 7.x, this is a finding.

