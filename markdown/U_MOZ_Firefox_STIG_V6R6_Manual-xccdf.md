# STIG Benchmark: Mozilla Firefox Security Technical Implementation Guide

---

**Version:** 6

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000456

**Group ID:** `V-251545`

### Rule: The installed version of Firefox must be supported.

**Rule ID:** `SV-251545r961683_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using versions of an application that are not supported by the vendor is not permitted. Vendors respond to security flaws with updates and patches. These updates are not available for unsupported versions, which can leave the application vulnerable to attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run Firefox. Click the ellipsis button >> Help >> About Firefox, and view the version number. If the Firefox version is not a supported version, this is a finding.

## Group: SRG-APP-000560

**Group ID:** `V-251546`

### Rule: Firefox must be configured to allow only TLS 1.2 or above.

**Rule ID:** `SV-251546r961869_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of versions prior to TLS 1.2 are not permitted. SSL 2.0 and SSL 3.0 contain a number of security flaws. These versions must be disabled in compliance with the Network Infrastructure and Secure Remote Computing STIGs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "SSLVersionMin" is not displayed under Policy Name or the Policy Value is not "tls1.2" or "tls1.3", this is a finding.

## Group: SRG-APP-000177

**Group ID:** `V-251547`

### Rule: Firefox must be configured to ask which certificate to present to a website when a certificate is required.

**Rule ID:** `SV-251547r1067550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a website asks for a certificate for user authentication, Firefox must be configured to have the user choose which certificate to present. Websites within DOD require user authentication for access, which increases security for DOD information. Access will be denied to the user if certificate management is not configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "Preferences" is not displayed under Policy Name and the Policy Value does not include "security.default_personal_cert" with a value of "Ask Every Time" and status of "locked", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251548`

### Rule: Firefox must be configured to not automatically check for updated versions of installed search plugins.

**Rule ID:** `SV-251548r1067552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Updates must be controlled and installed from authorized and trusted servers. This setting overrides a number of other settings that may direct the application to access external URLs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "Preferences" is not displayed under Policy Name or the Policy Value does not include "browser.search.update" with a value of "false" and status of "locked", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251549`

### Rule: Firefox must be configured to not automatically update installed add-ons and plugins.

**Rule ID:** `SV-251549r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Set this to false to disable checking for updated versions of the Extensions/Themes. Automatic updates from untrusted sites puts the enclave at risk of attack and may override security settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "ExtensionUpdate" is not displayed under Policy Name or the Policy Value is not "false", this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-251550`

### Rule: Firefox must be configured to not automatically execute or download MIME types that are not authorized for auto-download.

**Rule ID:** `SV-251550r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some files can be downloaded or execute without user interaction. This setting ensures these files are not downloaded and executed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:preferences" in the browser address bar. Type "Applications" in the Find bar in the upper-right corner. Determine if any of the following file extensions are listed: HTA, JSE, JS, MOCHA, SHS, VBE, VBS, SCT, WSC, FDF, XFDF, LSL, LSO, LSS, IQY, RQY, DOS, BAT, PS, EPS, WCH, WCM, WB1, WB3, WCH, WCM, AD. If the entry exists and the "Action" is "Save File" or "Always Ask", this is not a finding. If an extension exists and the entry in the Action column is associated with an application that does/can execute the code, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251551`

### Rule: Firefox must be configured to disable form fill assistance.

**Rule ID:** `SV-251551r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect privacy and sensitive data, Firefox provides the ability to configure the program so that data entered into forms is not saved. This mitigates the risk of a website gleaning private information from prefilled information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "DisableFormHistory" is not displayed under Policy Name or the Policy Value is not "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251552`

### Rule: Firefox must be configured to not use a password store with or without a master password.

**Rule ID:** `SV-251552r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firefox can be set to store passwords for sites visited by the user. These individual passwords are stored in a file and can be protected by a master password. Autofill of the password can then be enabled when the site is visited. This feature could also be used to autofill the certificate PIN, which could lead to compromise of DoD information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "PasswordManagerEnabled" is not displayed under Policy Name or the Policy Value is not "false", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251553`

### Rule: Firefox must be configured to block pop-up windows.

**Rule ID:** `SV-251553r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Pop-up windows may be used to launch an attack within a new browser window with altered settings. This setting blocks pop-up windows created while the page is loading.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "PopupBlocking" is not displayed under Policy Name or the Policy Value is not "Default" "true", this is a finding. If "PopupBlocking" is not displayed under Policy Name or the Policy Value is not "Locked" "true", this is a finding. "PopupBlocking" "Enabled" may be used to specify an allowlist of sites where pop-ups are desired, this is optional.

## Group: SRG-APP-000141

**Group ID:** `V-251554`

### Rule: Firefox must be configured to prevent JavaScript from moving or resizing windows.

**Rule ID:** `SV-251554r1067554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JavaScript can make changes to the browser's appearance. This activity can help disguise an attack taking place in a minimized background window. Configure the browser setting to prevent scripts on visited websites from moving and resizing browser windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "Preferences" is not displayed under Policy Name or the Policy Value does not include "dom.disable_window_move_resize" with a value of "true" and status of "locked", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251555`

### Rule: Firefox must be configured to prevent JavaScript from raising or lowering windows.

**Rule ID:** `SV-251555r1067556_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JavaScript can raise and lower browser windows to cause improper input. Configure the browser setting to prevent scripts on visited websites from raising and lowering browser windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "Preferences" is not displayed under Policy Name or the Policy Value does not include "dom.disable_window_flip" with a value of "true" and status of "locked", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251557`

### Rule: Firefox must be configured to disable the installation of extensions.

**Rule ID:** `SV-251557r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A browser extension is a program that has been installed into the browser to add functionality. Where a plug-in interacts only with a web page and usually a third-party external application (e.g., Flash, Adobe Reader), an extension interacts with the browser program itself. Extensions are not embedded in web pages and must be downloaded and installed in order to work. Extensions allow browsers to avoid restrictions that apply to web pages. For example, an extension can be written to combine data from multiple domains and present it when a certain page is accessed, which can be considered cross-site scripting. If a browser is configured to allow unrestricted use of extensions, plug-ins can be loaded and installed from malicious sources and used on the browser.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "InstallAddonsPermission" is not displayed under Policy Name or the Policy Value is not "Default" "false", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251558`

### Rule: Background submission of information to Mozilla must be disabled.

**Rule ID:** `SV-251558r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firefox by default sends information about Firefox to Mozilla servers. There should be no background submission of technical and other information from DoD computers to Mozilla with portions posted publicly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "DisableTelemetry" is not displayed under Policy Name or the Policy Value is not "true", this is a finding.

## Group: SRG-APP-000266

**Group ID:** `V-251559`

### Rule: Firefox development tools must be disabled.

**Rule ID:** `SV-251559r961167_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web browser includes any information about the web browser and plug-ins or modules being used. When debugging or trace information is enabled in a production web browser, information about the web browser, such as web browser type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any back ends being used for data storage may be displayed. Because this information may be placed in logs and general messages during normal operation of the web browser, an attacker does not have to cause an error condition to gain this information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "DisableDeveloperTools" is not displayed under Policy Name or the Policy Value is not "true", this is a finding.

## Group: SRG-APP-000175

**Group ID:** `V-251560`

### Rule: Firefox must have the DOD root certificates installed.

**Rule ID:** `SV-251560r1067559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DOD root certificates will ensure that the trust chain is established for server certificates issued from the DOD Certificate Authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:preferences#privacy" in the browser window. Scroll down to the bottom and select "View Certificates...". In the Certificate Manager window, select the "Authorities" tab. Scroll through the Certificate Name list to the U.S. Government heading. Look for the entries for DOD Root CA 3, DOD Root CA 4, and DOD Root CA 5. If there are entries for DOD Root CA 3, DOD Root CA 4, and DOD Root CA 5, select them individually. Click "View". Verify the issuer name is "US Government". If there are no entries for the appropriate DOD root certificates, this is a finding. If other AO-approved certificates are used, this is not a finding. If SIPRNet-specific certificates are used, this is not a finding. Note: In a Windows environment, use of policy setting "security.enterprise_roots.enabled=true" will point Firefox to the Windows Trusted Root Certification Authority Store. This is not a finding. It can also be set via the policy Certificates >> ImportEnterpriseRoots, which can be verified via "about:policies".

## Group: SRG-APP-000326

**Group ID:** `V-251562`

### Rule: Firefox must prevent the user from quickly deleting data.

**Rule ID:** `SV-251562r987660_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>There should not be an option for a user to "forget" work they have done. This is required to meet non-repudiation controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "DisableForgetButton" is not displayed under Policy Name or the Policy Value is not "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251563`

### Rule: Firefox private browsing must be disabled.

**Rule ID:** `SV-251563r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private browsing allows the user to browse the internet without recording their browsing history/activity. From a forensics perspective, this is unacceptable. Best practice requires that browser history is retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "DisablePrivateBrowsing" is not displayed under Policy Name or the Policy Value is not "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251564`

### Rule: Firefox search suggestions must be disabled.

**Rule ID:** `SV-251564r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Search suggestions must be disabled as this could lead to searches being conducted that were never intended to be made.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "SearchSuggestEnabled" is not displayed under Policy Name or the Policy Value is not "false", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251565`

### Rule: Firefox autoplay must be disabled.

**Rule ID:** `SV-251565r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Autoplay allows the user to control whether videos can play automatically (without user consent) with audio content. The user must be able to select content that is run within the browser window.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "Permissions" is not displayed under Policy Name or the Policy Value is not "Autoplay" with a value of "Default" and "Block-audio-video", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251566`

### Rule: Firefox network prediction must be disabled.

**Rule ID:** `SV-251566r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If network prediction is enabled, requests to URLs are made without user consent. The browser should always make a direct DNS request without prefetching occurring.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser window. If "NetworkPrediction" is not displayed under Policy Name or the Policy Value is not "false", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251567`

### Rule: Firefox fingerprinting protection must be enabled.

**Rule ID:** `SV-251567r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Content Blocking/Tracking Protection feature stops Firefox from loading content from malicious sites. The content might be a script or an image, for example. If a site is on one of the tracker lists that Firefox is set to use, the fingerprinting script (or other tracking script/image) will not be loaded from that site. Fingerprinting scripts collect information about browser and device configuration, such as operating system, screen resolution, and other settings. By compiling these pieces of data, fingerprinters create a unique profile that can be used to track the user around the web.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "EnableTrackingProtection" is not displayed under Policy Name or the Policy Value is not "Fingerprinting" with a value of "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251568`

### Rule: Firefox cryptomining protection must be enabled.

**Rule ID:** `SV-251568r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Content Blocking/Tracking Protection feature stops Firefox from loading content from malicious sites. The content might be a script or an image, for example. If a site is on one of the tracker lists that Firefox is set to use, the fingerprinting script (or other tracking script/image) will not be loaded from that site. Cryptomining scripts use a computer's central processing unit to invisibly mine cryptocurrency.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "EnableTrackingProtection" is not displayed under Policy Name or the Policy Value is not "Cryptomining" with a value of "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251569`

### Rule: Firefox Enhanced Tracking Protection must be enabled.

**Rule ID:** `SV-251569r1067561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tracking generally refers to content, cookies, or scripts that can collect browsing data across multiple sites. It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include but are not limited to advertising software or browser plug-ins that are not related to requirements or provide a wide array of functionality not required for every mission but that cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "Preferences" is not displayed under Policy Name or the Policy Value does not include "browser.contentblocking.category" with a value of "strict" and status of "locked", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251570`

### Rule: Firefox extension recommendations must be disabled.

**Rule ID:** `SV-251570r1067563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Recommended Extensions program makes it easier for users to discover extensions that have been reviewed for security, functionality, and user experience. Allowed extensions are to be centrally managed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "Preferences" is not displayed under Policy Name and the Policy Value does not include "extensions.htmlaboutaddons.recommendations.enabled" with a value of "false" and status of "locked", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251571`

### Rule: Firefox deprecated ciphers must be disabled.

**Rule ID:** `SV-251571r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A weak cipher is defined as an encryption/decryption algorithm that uses a key of insufficient length. Using an insufficient length for a key in an encryption/decryption algorithm opens up the possibility (or probability) that the encryption scheme could be broken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "DisabledCiphers" is not displayed under Policy Name or the Policy Value is not "TLS_RSA_WITH_3DES_EDE_CBC_SHA" with a value of "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251572`

### Rule: Firefox must not recommend extensions as the user is using the browser.

**Rule ID:** `SV-251572r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Recommended Extensions program recommends extensions to users as they surf the web. The user must not be encouraged to install extensions from the websites they visit. Allowed extensions are to be centrally managed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "UserMessaging" is not displayed under Policy Name or the Policy Value is not "ExtensionRecommendations" with a value of "false", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251573`

### Rule: The Firefox New Tab page must not show Top Sites, Sponsored Top Sites, Pocket Recommendations, Sponsored Pocket Stories, Searches, Highlights, or Snippets.

**Rule ID:** `SV-251573r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The New Tab page by default shows a list of built-in top sites, as well as the top sites the user has visited. It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to advertising software or browser plug-ins that are not related to requirements or provide a wide array of functionality not required for every mission but that cannot be disabled. The new tab page must not actively show user activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "FirefoxHome" is not displayed under Policy Name or the Policy Value does not have "Search" with a value of "false", this is a finding. If "FirefoxHome" is not displayed under Policy Name or the Policy Value does not have "TopSites" with a value of "false", this is a finding. If "FirefoxHome" is not displayed under Policy Name or the Policy Value does not have "SponsoredTopSites" with a value of "false", this is a finding. If "FirefoxHome" is not displayed under Policy Name or the Policy Value does not have "Pocket" with a value of "false", this is a finding. If "FirefoxHome" is not displayed under Policy Name or the Policy Value does not have "SponsoredPocket" with a value of "false", this is a finding. If "FirefoxHome" is not displayed under Policy Name or the Policy Value does not have "Highlights" with a value of "false", this is a finding. If "FirefoxHome" is not displayed under Policy Name or the Policy Value does not have "Snippets" with a value of "false", this is a finding. If "FirefoxHome" is not displayed under Policy Name or the Policy Value does not have "Locked" with a value of "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251577`

### Rule: Firefox must be configured so that DNS over HTTPS is disabled.

**Rule ID:** `SV-251577r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS over HTTPS has generally not been adopted in the DoD. DNS is tightly controlled. It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission, but cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "DNSOverHTTPS" is not displayed under Policy Name or the Policy Value does not have "Enabled" with a value of "false", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251578`

### Rule: Firefox accounts must be disabled.

**Rule ID:** `SV-251578r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disable Firefox Accounts integration (Sync). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to advertising software or browser plug-ins that are not related to requirements or provide a wide array of functionality not required for every mission but that cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "DisableFirefoxAccounts" is not displayed under Policy Name or the Policy Value is not "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251580`

### Rule: Firefox feedback reporting must be disabled.

**Rule ID:** `SV-251580r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disable the menus for reporting sites (Submit Feedback, Report Deceptive Site). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to advertising software or browser plug-ins that are not related to requirements or provide a wide array of functionality not required for every mission but that cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "DisableFeedbackCommands" is not displayed under Policy Name or the Policy Value is not "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251581`

### Rule: Firefox encrypted media extensions must be disabled.

**Rule ID:** `SV-251581r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enable or disable Encrypted Media Extensions and optionally lock it. If "Enabled" is set to "false", Firefox does not download encrypted media extensions (such as Widevine) unless the user consents to installing them. If "Locked" is set to "true" and "Enabled" is set to "false", Firefox will not download encrypted media extensions (such as Widevine) or ask the user to install them. It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to advertising software or browser plug-ins that are not related to requirements or provide a wide array of functionality not required for every mission but that cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "EncryptedMediaExtensions" is not displayed under Policy Name or the Policy Value does not have "Enabled" set to "false" or the Policy Value does not have "Locked" set to "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-252881`

### Rule: Firefox must be configured to not delete data upon shutdown.

**Rule ID:** `SV-252881r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For diagnostic purposes, data must remain behind when the browser is closed. This is required to meet non-repudiation controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "SanitizeOnShutdown" is not displayed under Policy Name or the Policy Value does not have {"Cache":false,"Cookies":false,"Downloads":false,"FormData":false,"Sessions":false,"History":false,"OfflineApps":false,"SiteSettings":false,"Locked":true}, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-252908`

### Rule: Pocket must be disabled.

**Rule ID:** `SV-252908r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Pocket, previously known as Read It Later, is a social bookmarking service for storing, sharing, and discovering web bookmarks. Data gathering cloud services such as this are generally disabled in the DoD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "DisablePocket" is not displayed under Policy Name or the Policy Value does not have a value of "true", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-252909`

### Rule: Firefox Studies must be disabled.

**Rule ID:** `SV-252909r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Studies try out different features and ideas before they are released to all Firefox users. Testing beta software is not in the DoD user's mission.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "about:policies" in the browser address bar. If "DisableFirefoxStudies" is not displayed under Policy Name or the Policy Value does not have a value of "true", this is a finding.

