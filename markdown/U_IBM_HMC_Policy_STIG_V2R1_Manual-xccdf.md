# STIG Benchmark: IBM Hardware Management Console (HMC) Policies Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000360-GPOS-00147

**Group ID:** `V-256853`

### Rule: Initial Program Load (IPL) Procedures must exists for each partition defined to the system.

**Rule ID:** `SV-256853r890905_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If procedures for performing IPLs are not in place, it is extremely difficult to ensure overall operating system integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the Systems Administrator validate that IPL Procedures Documentation exists for all partitions that are defined on the system. Using the Hardware Management Console, do the following: 1) Access CPC Images Group displays. (This will list the LPARs.) 2) Compare the partition names listed on the Partition Page to validate that IPL procedures exist for each entered on the Central Processor Complex Domain/LPAR Names. If IPL Procedures do not exist for each partition, this is a FINDING.

## Group: SRG-OS-000360-GPOS-00147

**Group ID:** `V-256854`

### Rule: Power On Reset (POR) Procedures must be documented for each system.

**Rule ID:** `SV-256854r890908_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If procedures for performing PORs are not in place, it is extremely difficult to ensure overall operating system integrity</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the POR procedures with the System Administrator. Review documentation for completeness and accuracy. If no documentation exists, this is a FINDING

## Group: SRG-OS-000360-GPOS-00147

**Group ID:** `V-256855`

### Rule: System shutdown procedures documentation must exist for each partition defined to the system.

**Rule ID:** `SV-256855r890911_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If procedures for performing system shutdowns are not in place, it is extremely difficult to ensure overall data and operating system integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the System Administrator validate that System Shutdown Documentation exists for all partitions that are defined on the system. a) Using the Hardware Management Console, do the following: 1) Access CPC Images Group displays. (This will list the LPARs.) 2) Compare the partition names listed on the Partition Page to validate that System Shutdown procedures exist for each entered on the Central Processor Complex Domain/LPAR Names. If System Shutdown Procedures do not exist for each partition, this is a FINDING.

## Group: SRG-OS-000360-GPOS-00147

**Group ID:** `V-256856`

### Rule: Backup of critical data for the HMC and its components  must be documented and tracked

**Rule ID:** `SV-256856r890914_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If procedures for performing backup and recovery of critical data for the HMC is not in place, system recoverability may be jeopardized and overall security compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the documentation for backup of critical data for a HMC with the System Administrator. Review documentation for completeness and accuracy. If no documentation exists, this is a FINDING.

