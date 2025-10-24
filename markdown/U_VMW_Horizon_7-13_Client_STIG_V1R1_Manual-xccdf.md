# STIG Benchmark: VMware Horizon 7.13 Client Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246875`

### Rule: The Horizon Client must not send anonymized usage data.

**Rule ID:** `SV-246875r768585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the Horizon Client collects anonymized data from the client systems to help improve software and hardware compatibility. To eliminate any possibility of sensitive DoD configurations being known to unauthorized parties, even when anonymized, this setting must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Horizon Client Configuration. Double-click the "Allow data sharing" setting. If "Allow data sharing" is set to "Enabled" or "Not Configured", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246876`

### Rule: The Horizon Client must not connect to servers without fully verifying the server certificate.

**Rule ID:** `SV-246876r768588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the application server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). The Horizon Client connects to the Connection Server, UAG or other gateway via a TLS connection. This initial connection must be trusted, otherwise the sensitive information flowing over the tunnel could potentially be open to interception. The Horizon Client can be configured to ignore any certificate validation errors, warn or fail. By default, the Client will warn and let the user decide to proceed or not. This decision must not be left to the end user. In a properly configured, enterprise environment, there should be no trouble with the presented certificate. On the other hand, a TLS connection could be easily intercepted and middle-manned with the assumption that a user will just click away any errors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Horizon Client Configuration >> Security Settings. Double-click "Certificate verification mode". If "Certificate verification mode" is "Not Configured" or "Disabled", this is a finding. If "Certificate verification mode" is not set to "Full Security", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246877`

### Rule: The Horizon Client must not show the Log in as current user option.

**Rule ID:** `SV-246877r768591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Connection Server STIG disabled the "Log in as current user" option, for reasons described there. Displaying this option and allowing users to select it would lead to unnecessary confusion and therefore must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Horizon Client Configuration >> Security Settings. Double-click "Display option to Log in as current user". If "Display option to Log in as current user" is not set to "Disabled", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246878`

### Rule: The Horizon Client must not ignore certificate revocation problems.

**Rule ID:** `SV-246878r768594_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the Horizon Client connects to the server, by default, the server TLS certificate will be validated on the client side. If the revocation status cannot be determined or if the certificate is revoked, the connection will fail due to an untrusted connection. This default behavior can be overridden, however, to ignore revocation errors and proceed with revoked or certificates of unknown status. The default, secure, configuration must be validated and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Horizon Client Configuration >> Security Settings. Double-click "Ignore certificate revocation problems". If "Ignore certificate revocation problems" is set to "Enabled", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246879`

### Rule: The Horizon Client must require TLS connections.

**Rule ID:** `SV-246879r768597_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In older versions of Horizon, before 5.0, remote desktop connections could be established without TLS encryption. In order to protect data-in-transit when potentially connecting to very old Horizon servers, TLS tunnels must be mandated. The default configuration attempts TLS but will fall back to no encryption if it is not supported. This must be corrected and maintained over time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Horizon Client Configuration >> Security Settings. Double-click "Enable SSL encrypted framework channel". If "Enable SSL encrypted framework channel" is set to "Disabled" or "Not Configured", this is a finding. In the dropdown beneath "Enable SSL encrypted framework channel", if "Enforce" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246880`

### Rule: The Horizon Client must use approved ciphers.

**Rule ID:** `SV-246880r768600_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Client disables the older TLS v1.0 protocol and the SSL v2 and SSL v3 protocols by default. TLS v1.1 is still enabled in the default configuration, despite known shortcomings, for the sake of backward compatibility with older servers and clients. The Horizon Connection Server STIG mandates TLS v1.2 in order to protect sensitive data-in-flight and the Client must follow suite. Note: Mandating TLS 1.2 may affect certain thin and zero clients. Test and implement carefully.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Horizon Client Configuration >> Security Settings. Double-click "Configures SSL protocols and cryptographic algorithms". If "Configures SSL protocols and cryptographic algorithms" is set to "Disabled" or "Not Configured", this is a finding. If the field beneath "Configures SSL protocols and cryptographic algorithms", is not set to "TLSv1.2:!aNULL:kECDH+AESGCM:ECDH+AESGCM:RSA+AESGCM:kECDH+AES:ECDH+AES:RSA+AES", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246881`

### Rule: The Horizon Client must not allow command line credentials.

**Rule ID:** `SV-246881r768603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Client has a number of command line options including authentication parameters, by default. This can include a smart card PIN, if so configured by the end user. This would normally be implemented by a script, which would mean plain text sensitive authenticators sitting on disk. Hard coding of credentials of any sort, but especially smart card PINs, must be explicitly disallowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Horizon Client Configuration >> Security Settings. Double-click "Allow command line credentials". If "Allow command line credentials" is "Not Configured" or "Enabled", this is a finding.

