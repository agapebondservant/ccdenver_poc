# STIG Benchmark: Microsoft Intune MDM Service Desktop & Mobile Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000003-UEM-000003

**Group ID:** `V-273867`

### Rule: Microsoft Intune service must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-273867r1101448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock but may be at the application level where the application interface window is secured instead. Satisfies: SRG-APP-000003-UEM-000003, SRG-APP-000295-UEM-000169</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the inactivity timeout is configured for 15 minutes or less, follow the steps outlined below: 1. Sign in to portal.office365.com (or .us if the user is a GCCH or DOD tenant). 2. Navigate to Admin >> Settings >> Org Settings >> Security and Privacy (tab on top of page) >> Idle Session Timeout. 3. Select the check box to enable "Turn on to set the period of inactivity". 4. Select custom option, then verify it has been set to 15. If the inactivity timeout is not set to 15 minutes or less, this is a finding.

## Group: SRG-APP-000125-UEM-000074

**Group ID:** `V-273868`

### Rule: Microsoft Intune service must be configured to transfer Intune logs to another server for storage, analysis, and reporting at least every seven days.

**Rule ID:** `SV-273868r1101588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: UEM server logs include logs of UEM events and logs transferred to Microsoft Intune service by UEM agents of managed devices. Protection of log data includes ensuring log data is not accidentally lost or deleted. Backing up audit records to a different system or onto separate media than the system being audited on an organizationally defined frequency helps ensure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. This requirement only applies to applications that have a native backup capability for audit records. Operating system backup requirements cover applications that do not provide native backup functions. Satisfies: SRG-APP-000125-UEM-000074, SRG-APP-000275-UEM-000157, SRG-APP-000358-UEM-000228</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the site has configured Intune to off-load Intune logs to a third-party log management server or to an Azure log storage and monitoring service like Azure monitor. Verification procedures are determined by the method used at the site. Ask the site Intune Administrator how logs are managed by the site and demonstrate that Intune logs are being off-loaded. If site is off-loading Intune logs to the Azure monitor, do the following (refer to https://learn.microsoft.com/en-us/mem/intune-service/fundamentals/review-logs-using-azure-monitor): 1. Sign in to the Microsoft Intune admin center. 2. Select Reports >> Diagnostics settings. 3. Verify logs are being sent to the Azure monitor: a. A storage account has been configured. b. A Stream has been configured to stream logs to the Azure Event Hubs. c. Intune logs have been configured to be sent to Log Analytics. If the site is not transferring Intune audit logs to a third-party audit log management server or to an Azure audit log storage and monitoring service, this is a finding.

