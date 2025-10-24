# STIG Benchmark: Palo Alto Networks Prisma Cloud Compute Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014-CTR-000040

**Group ID:** `V-253522`

### Rule: Prisma Cloud Compute Console must use TLS 1.2 for user interface and API access. Communication TCP ports must adhere to the Ports, Protocols, and Services Management Category Assurance Levels (PSSM CAL).

**Rule ID:** `SV-253522r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Communication to Prisma Cloud Compute Console's User Interface (UI) and API is protected by TLS v1.2+ (HTTPS). By default, only HTTPS communication to the Console's UI and API endpoints is enabled. Prisma Cloud Compute TCP port usage is configurable. Default configuration: TCP 8081 Console user interface and API (HTTP) - disabled by default. TCP 8083 Console user interface and API TLS v1.2 (HTTPS) TCP 8084 Console-to-Defender communication via mutual TLS v1.2 WebSocket session. Satisfies: SRG-APP-000014-CTR-000040, SRG-APP-000142-CTR-000325, SRG-APP-000185-CTR-000490, SRG-APP-000645-CTR-001410</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Kubernetes deployment: Query the ports used by the twistlock-console service: $ kubectl describe svc twistlock-console -n twistlock If the TargetPort management-port-http exists and has a port assignment, this is a finding. Port: management-port-http 8081/TCP TargetPort: 8081/TCP For Docker deployment: Determine the name of the Console container: docker ps|grep console For example, the Console container is: ad8b41a2fec9 twistlock/private:console_22_01_840 Inspect the container's PortBindings: docker inspect ad8b41a2fec9|grep PortBindings -A 20 If port 8081 is listed, this is a finding.

## Group: SRG-APP-000023-CTR-000055

**Group ID:** `V-253523`

### Rule: Access to Prisma Cloud Compute must be managed based on user need and least privileged using external identity providers for authentication and grouping to role-based assignments when possible.

**Rule ID:** `SV-253523r1043176_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Integration with an organization's existing identity management policies technologies reduces the threat of account compromise and misuse. Centralized authentication services provide additional functionality to fulfill security requirements: - Multifactor authentication. - Disabling users after a period of time. - Encrypted storage and transmission of secure information. - Secure authentication protocols such as LDAP over TLS or LDAPS using FIPS 140-2 approved encryption modules. - PKI-based authentication. Satisfies: SRG-APP-000023-CTR-000055, SRG-APP-000024-CTR-000060, SRG-APP-000025-CTR-000065, SRG-APP-000033-CTR-000095, SRG-APP-000065-CTR-000115, SRG-APP-000068-CTR-000120, SRG-APP-000069-CTR-000125, SRG-APP-000149-CTR-000355, SRG-APP-000150-CTR-000360, SRG-APP-000151-CTR-000365, SRG-APP-000152-CTR-000370, SRG-APP-000163-CTR-000395, SRG-APP-000165-CTR-000405, SRG-APP-000170-CTR-000430, SRG-APP-000173-CTR-000445, SRG-APP-000174-CTR-000450, SRG-APP-000291-CTR-000675, SRG-APP-000292-CTR-000680, SRG-APP-000293-CTR-000685, SRG-APP-000294-CTR-000690, SRG-APP-000317-CTR-000735, SRG-APP-000318-CTR-000740, SRG-APP-000345-CTR-000785, SRG-APP-000397-CTR-000955</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm the Prisma Cloud Console has been configured from SAML-based authentication. Navigate to Prisma Cloud Compute Console's Manage >> Authentication >> Identity Providers tab. Verify SAML settings are "Enabled" and an identity provider has been configured. If SAML settings are not enabled and an identity provider has not been configured, this is a finding.

## Group: SRG-APP-000033-CTR-000100

**Group ID:** `V-253524`

### Rule: Users requiring access to Prisma Cloud Compute's Credential Store must be assigned and accessed by the appropriate role holders.

**Rule ID:** `SV-253524r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The container platform keystore is used to store credentials that are used to build a trust between the container platform and an external source. This trust relationship is authorized by the organization. If a malicious user were to have access to the container platform keystore, two negative scenarios could develop: 1. Keys not approved could be introduced. 2. Approved keys could be deleted, leading to the introduction of container images from sources the organization never approved. To thwart this threat, it is important to protect the container platform keystore and give access to only individuals and roles approved by the organization. Satisfies: SRG-APP-000033-CTR-000100, SRG-APP-000118-CTR-000240, SRG-APP-000121-CTR-000255, SRG-APP-000133-CTR-000300, SRG-APP-000211-CTR-000530, SRG-APP-000233-CTR-000585, SRG-APP-000340-CTR-000770, SRG-APP-000380-CTR-000900</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Authentication >> Users tab. Inspect the users' role assignments: - Review role assigned to users. If role and/or the Collection assignment is incorrect, this is a finding. - If a user is not assigned a role, this is a finding. - Review users assigned the administrator role. If a user has the administrator role and does not require access, this is a finding. Navigate to Prisma Cloud Compute Console's >> Manage >> Authentication >> Groups tab. (Only the Administrator, Operator Prisma Cloud Compute roles have the ability to create/modify policy that could affect runtime behaviors.) Inspect the groups' role assignments: - If any users or groups are assigned the Auditor or higher role and do not require access to audit information, this is a finding. - If a group is not assigned a role, this is a finding. - If role and/or Collection assignment is incorrect, this is a finding. - Review groups assigned the Administrator or Operator role. If a group has the Administrator or Operator role and does not require access to Prisma Cloud Compute's Credential Store, this is a finding.

## Group: SRG-APP-000038-CTR-000105

**Group ID:** `V-253525`

### Rule: Prisma Cloud Compute Collections must be used to partition views and enforce organizational-defined need-to-know access.

**Rule ID:** `SV-253525r960801_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prisma Cloud Compute Collections are used to scope rules to target specific resources in an environment, partition views, and enforce which views specific users and groups can access. Collections can control access to data on a need-to-know basis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Collections and Tags >> Collections tab. Review the Collections according to organizational policy. If no organizational-specific Collections are defined, this is a finding.

## Group: SRG-APP-000039-CTR-000110

**Group ID:** `V-253526`

### Rule: Prisma Cloud Compute Cloud Native Network Firewall (CNNF) automatically monitors layer 4 (TCP) intercontainer communications. Enforcement policies must be created.

**Rule ID:** `SV-253526r960804_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network segmentation and compartmentalization are important parts of a comprehensive defense-in-depth strategy. CNNF works as an east-west firewall for containers. It limits damage by preventing attackers from moving laterally through the environment when they have already compromised the perimeter. Satisfies: SRG-APP-000039-CTR-000110, SRG-APP-000384-CTR-000915</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Radars >> Settings. If Container network monitoring is disabled, this is a finding. If Host network monitoring is disabled, this is a finding.

## Group: SRG-APP-000097-CTR-000180

**Group ID:** `V-253527`

### Rule: Prisma Cloud Compute Defender must be deployed to containerization nodes that are to be monitored.

**Rule ID:** `SV-253527r960897_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Container platforms distribute workloads across several nodes. The ability to uniquely identify an event within an environment is critical. Prisma Cloud Compute Container Runtime audits record the time, container, corresponding image, and node where the event occurred. Satisfies: SRG-APP-000097-CTR-000180, SRG-APP-000100-CTR-000200</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Defenders >> Manage tab. Verify Prisma Cloud Compute Defenders have been deployed to all container runtime nodes to be monitored. Review the list of deployed Defenders. If a Defender is missing, this is a finding.

## Group: SRG-APP-000099-CTR-000190

**Group ID:** `V-253528`

### Rule: Prisma Cloud Compute must be configured for forensic data collection.

**Rule ID:** `SV-253528r960903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prisma Cloud Compute correlates raw audit data to actionable security intelligence, enabling a more rapid and effective response to incidents. This reduces the manual, time-consuming task of correlating data. Prisma Cloud Forensics is a lightweight distributed data recorder that runs alongside all containers in the environment. Prisma Cloud continuously collects detailed runtime information to help incident response teams understand what happened before, during, and after a breach. Forensic data consists of additional supplemental runtime events that complement the data (audits) already captured by Prisma Cloud's runtime sensors. It provides additional context when trying to identify the root cause of an incident. Satisfies: SRG-APP-000099-CTR-000190, SRG-APP-000409-CTR-000990</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> System >> Forensics tab. If "Forensics data collection" is disabled, this is a finding.

## Group: SRG-APP-000101-CTR-000205

**Group ID:** `V-253529`

### Rule: The configuration integrity of the container platform must be ensured and runtime policies must be configured.

**Rule ID:** `SV-253529r960909_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Prisma Cloud Compute's runtime defense is the set of features that provides both predictive and threat-based active protection for running containers. Consistent application of Prisma Cloud Compute runtime policies ensures the continual application of policies and the associated effects. Prisma Cloud Compute's configurations must be monitored for configuration drift and addressed according to organizational policy. Satisfies: SRG-APP-000101-CTR-000205, SRG-APP-000384-CTR-000915, SRG-APP-000447-CTR-001100, SRG-APP-000450-CTR-001105, SRG-APP-000507-CTR-001295, SRG-APP-000508-CTR-001300</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify runtime policies are enabled. Navigate to Prisma Cloud Compute Console's Defend >> Runtime. Select "Container policy". - If a rule does not exist, this is a finding. - If "Enable automatic runtime learning" is set to "off", this is a finding. - Click the three dots in the "Actions" column for the rule. - If the policy is disabled, this is a finding. - Click the Container runtime policy. - If the policy is not scoped to "All", this is a finding. Select the "App-Embedded policy" tab. - If a rule does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default - alert on suspicious runtime behavior". - If the policy is disabled, this is a finding. - Click the "Default - alert on suspicious runtime behavior" policy row. - If the "Default - alert on suspicious runtime behavior" policy is not scoped to "All", this is a finding. Select the "Host policy" tab. - If a rule does not exist, this is a finding. - Click the three dots in the "Actions" column for the rule. - If the policy is disabled, this is a finding. - Click the Host runtime policy. - If the policy is not scoped to "All", this is a finding.

## Group: SRG-APP-000111-CTR-000220

**Group ID:** `V-253530`

### Rule: Prisma Cloud Compute must be configured to send events to the hosts' syslog.

**Rule ID:** `SV-253530r960918_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Event log collection is critical in ensuring the security of a containerized environment due to the ephemeral nature of the workloads. In an environment that is continually in flux, audit logs must be properly collected and secured. Prisma Cloud Compute can be configured to send audit events to the host node's syslog in RFC5424-compliant format. Satisfies: SRG-APP-000111-CTR-000220, SRG-APP-000181-CTR-000485, SRG-APP-000358-CTR-000805, SRG-APP-000474-CTR-001180, SRG-APP-000516-CTR-000790</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Alerts >> Logging tab. If the Syslog setting is "disabled", this is a finding. Select the "Manage" tab. If no Alert Providers are configured, this is a finding.

## Group: SRG-APP-000133-CTR-000295

**Group ID:** `V-253531`

### Rule: Prisma Cloud Compute host compliance baseline policies must be set.

**Rule ID:** `SV-253531r960960_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Consistent application of Prisma Cloud Compute compliance policies ensures the continual application of policies and the associated effects. Satisfies: SRG-APP-000133-CTR-000295, SRG-APP-000133-CTR-000310, SRG-APP-000141-CTR-000315, SRG-APP-000384-CTR-000915</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Defend >> Compliance >> Hosts tab >> Running hosts tab. If a "Default - alert on critical and high" rule does not exist, this is a finding. Check all the rules to verify the following Actions are not set to "Ignore". (Click "Rule name".) <Filter on Rule ID> ID = 8112 - Verify the --anonymous-auth argument is set to false (kube-apiserver) - master node. ID = 8212 - Verify the --anonymous-auth argument is set to false (kubelet) - worker node. ID = 8311 - Verify the --anonymous-auth argument is set to false (federation-apiserver). ID = 81427 - Verify the Kubernetes PKI directory and file ownership are set to root:root. ID = 81428 - Verify the Kubernetes PKI certificate file permissions are set to 644 or more restrictive. ID = 8214 - Verify the --client-ca-file argument is set as appropriate (kubelet). ID = 8227 - Verify the certificate authorities file permissions are set to 644 or more restrictive (kubelet). ID = 8115 - Verify the --kubelet-https argument is set to true (kube-apiserver). ID = 8116 - Verify the --insecure-bind-address argument is not set (kube-apiserver). ID = 8117 - Verify the --insecure-port argument is set to 0 (kube-apiserver) can determine if the Kubernetes API is configured to only listen on the TLS-enabled port (TCP 6443). ID = 8118 - Verify the --secure-port argument is not set to 0 (kube-apiserver). ID = 81122 - Verify the --kubelet-certificate-authority argument is set as appropriate (kube-apiserver). ID = 81123 - Verify the --kubelet-client-certificate and --kubelet-client-key arguments are set as appropriate (kube-apiserver). ID = 81129 - Verify the --tls-cert-file and --tls-private-key-file arguments are set as appropriate (kube-apiserver). ID = 82112 - Verify the --tls-cert-file and --tls-private-key-file arguments are set as appropriate (kubelet). ID = 81141 - Verify the --authorization-mode argument includes RBAC (kube-apiserver). If any of these checks are set to "Ignore", to all host nodes within the intended monitored environment, this is a finding.

## Group: SRG-APP-000133-CTR-000305

**Group ID:** `V-253532`

### Rule: The configuration integrity of the container platform must be ensured and compliance policies must be configured.

**Rule ID:** `SV-253532r960960_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Consistent application of Prisma Cloud Compute compliance policies ensures the continual application of policies and the associated effects. Prisma Cloud Compute's configurations must be monitored for configuration drift and addressed according to organizational policy. Satisfies: SRG-APP-000133-CTR-000305, SRG-APP-000384-CTR-000915, SRG-APP-000435-CTR-001070, SRG-APP-000472-CTR-001170</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify compliance policies are enabled. Navigate to Prisma Cloud Compute Console's Defend >> Compliance. Select the "Code repositories" tab. Select the "Repositories" and "CI" tab. - If "Default – alert all components" does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default - alert all components". - If the policy is disabled, this is a finding. - Click the "Default – alert all components" policy row. - If the "Default - alert on critical and high" policy is not scoped to "All", this is a finding. Select the "Containers and images" tab. For the "Deployed" and "CI" tab: - If the "Default - alert on critical and high" does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default - alert on critical and high". - If the policy is disabled, this is a finding. - Click the "Default - alert on critical and high" policy row. - If the "Default - alert on critical and high" policy is not scoped to "All", this is a finding. Select the "Hosts" tab. For the "Running hosts" and "VM images" tab: - If the "Default - alert on critical and high" does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default - alert on critical and high". - If the policy is disabled, this is a finding. - Click the "Default - alert on critical and high" policy row. - If the "Default - alert on critical and high" policy is not scoped to "All", this is a finding. Select the "Functions" tab. For the "Functions" and "CI" tab: - If the "Default – alert all components" does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default -alert all components". - If the policy is disabled, this is a finding. - Click the "Default - alert all components" policy row. - If the "Default - alert on critical and high" policy is not scoped to "All", this is a finding.

## Group: SRG-APP-000141-CTR-000320

**Group ID:** `V-253533`

### Rule: Images stored within the container registry must contain only images to be run as containers within the container platform.

**Rule ID:** `SV-253533r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Prisma Cloud Compute Trusted Images feature allows the declaration, by policy, of which registries, repositories, and images to trust and how to respond when untrusted images are started in the organization's environment. Satisfies: SRG-APP-000141-CTR-000320, SRG-APP-000386-CTR-000920</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Defend >> Compliance Trusted Images tab. Select the "Trust groups" tab. If there is no Group, this is a finding. Select the "Policy" tab. If the Trusted Images Rules is set to "off", this is a finding. If a rule does not exist, this is a finding. Click the three dots in the "Actions" column for rule. If the policy is disabled, this is a finding. Click the policy row. If the policy is not scoped to "All", this is a finding.

## Group: SRG-APP-000142-CTR-000330

**Group ID:** `V-253534`

### Rule: Prisma Cloud Compute must use TCP ports above 1024.

**Rule ID:** `SV-253534r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged ports are ports below 1024 that require system privileges for their use. If containers are able to use these ports, the container must be run as a privileged user. The container platform must stop containers that try to map to these ports directly. Allowing nonprivileged ports to be mapped to the container-privileged port is the allowable method when a certain port is needed. Prisma Cloud Compute default TCP ports are 8083 (Console UI and API) and 8084 (Console-to-Defender communication). To use TCP ports below 1024, the Console would have to be configured to use privileged ports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Kubernetes deployment: Query the ports used by the twistlock-console service: $ kubectl describe svc twistlock-console -n twistlock If any port number is below 1024, this is a finding. For Docker deployment: Determine the name of the Console container: docker ps|grep console For example, the Console container is: ad8b41a2fec9 ad8b41a2fec9 twistlock/private:console_22_01_840 Inspect the container's PortBindings: docker inspect ad8b41a2fec9|grep PortBindings -A 20 If the port is below 1024, this is a finding.

## Group: SRG-APP-000148-CTR-000335

**Group ID:** `V-253535`

### Rule: All Prisma Cloud Compute users must have a unique, individual account.

**Rule ID:** `SV-253535r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prisma Cloud Compute does not have a default account. During installation, the installer creates an administrator. This account can be removed once other accounts have been added. To ensure accountability and prevent unauthenticated access, users must be identified and authenticated to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm there is only one "break glass" local administrative account. Navigate to Prisma Cloud Compute Console's Manage >> Authentication >> Users tab. Only the administrative break glass account is allowed to have Authentication Method = Local. For all other accounts, Authentication Method = SAML. If any local account, except the administrative break glass account, has Authentication Method set to other than "SAML", this is a finding.

## Group: SRG-APP-000148-CTR-000345

**Group ID:** `V-253536`

### Rule: Prisma Cloud Compute Console must run as nonroot user (uid 2674).

**Rule ID:** `SV-253536r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Containers not requiring root-level permissions must run as a unique user account. To ensure accountability and prevent unauthenticated access to containers, the user the container is using to execute must be uniquely identified and authenticated to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the node in which the Prisma Cloud Compute Console container is running. Determine the process owner for "app/server". Execute: "ps -aux | grep "/app/server" If the process is owned by root, this is a finding.

## Group: SRG-APP-000153-CTR-000375

**Group ID:** `V-253537`

### Rule: Prisma Cloud Compute must be configured with unique user accounts.

**Rule ID:** `SV-253537r1015785_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sharing accounts, such as group accounts, reduces the accountability and integrity of Prisma Cloud Compute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Authentication >> Users tab. Review the accounts for uniqueness. If there are shared local accounts, this is a finding.

## Group: SRG-APP-000164-CTR-000400

**Group ID:** `V-253538`

### Rule: Prisma Cloud Compute local accounts must enforce strong password requirements.

**Rule ID:** `SV-253538r1015786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that must be tested before the password is compromised. Satisfies: SRG-APP-000164-CTR-000400, SRG-APP-000166-CTR-000410, SRG-APP-000167-CTR-000415, SRG-APP-000168-CTR-000420, SRG-APP-000169-CTR-000425, SRG-APP-000389-CTR-000925, SRG-APP-000391-CTR-000935, SRG-APP-000400-CTR-000960</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Authentication >> Logon tab. - If "Token validity period" is greater than 15, this is a finding. - If "Enable context sensitive help and single sign on to the Prisma Cloud Support site" is set to "on", this is a finding. - If "Disable basic authentication for the API" is set to "off", this is a finding. - If "Require strong passwords for local accounts" is set to "off", this is a finding. - If "Require strict certificate validation in Defender installation links" is set to "on", this is a finding.

## Group: SRG-APP-000177-CTR-000465

**Group ID:** `V-253539`

### Rule: Prisma Cloud Compute must be configured to require local user accounts to use x.509 multifactor authentication.

**Rule ID:** `SV-253539r1015787_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). User access to Prisma Cloud Compute must use multifactor (x.509 based) authentication. Satisfies: SRG-APP-000177-CTR-000465, SRG-APP-000391-CTR-000935, SRG-APP-000401-CTR-000965, SRG-APP-000402-CTR-000970, SRG-APP-000605-CTR-001380</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Authentication >> System Certificate tab. If not performing direct smart card authentication to the console, this is not a finding. If performing direct smart card authentication to the console: Revocation block: If "Enable certificate revocation checking" is set to "Off", this is a finding. Show Advanced certificate configuration: - In the "Certificate-based authentication to Console" block, verify the issuing CA(s) of the end users' certificates are within the Console CA certificate(s) field. - If there is no users' certificates, this is a finding. Click the "Users" tab. Review accounts with Authentication method "Local". If the local user account's name does not match the user's x.509 certificate's subjectName or the subject alternative name's PrincipalName value, this is a finding.

## Group: SRG-APP-000243-CTR-000595

**Group ID:** `V-253540`

### Rule: Prisma Cloud Compute must prevent unauthorized and unintended information transfer.

**Rule ID:** `SV-253540r961149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prisma Cloud Compute Compliance policies must be enabled to ensure running containers do not access privileged resources. Satisfies: SRG-APP-000243-CTR-000595, SRG-APP-000243-CTR-000600, SRG-APP-000246-CTR-000605, SRG-APP-000342-CTR-000775</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's Defend >> Compliance >> Containers and images tab >> Deployed tab. For each rule name, click the rule and confirm the following checks: (Filter on ID) ID = 54: Do not use privileged container ID = 5525: Restrict container from acquiring additional privileges are not configured ID = 59: Do not share the host's network namespace ID = 515: Do not share the host's process namespace ID = 516: Do not share the host's IPC namespace ID = 517: Do not directly expose host devices to containers ID = 520: Do not share the host's UTS namespace ID = 530: Do not share the host's user namespaces ID = 55: Do not mount sensitive host system directories on containers ID = 57: Do not map privileged ports within containers ID = 5510: Limit memory usage for container ID = 5511: Set container CPU priority appropriately ID = 599: Container is running as root ID = 41 Image should be created with a non-root user If the action for each rule is set to "Ignore", this is a finding.

## Group: SRG-APP-000266-CTR-000625

**Group ID:** `V-253541`

### Rule: Prisma Cloud Compute must not write sensitive data to event logs.

**Rule ID:** `SV-253541r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The determination of what is sensitive data varies from organization to organization. The organization must ensure the recipients for the event log information have a need to know and the log is sanitized based on the audience.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> System >> General tab. Inspect the Log Scrubbing section. If "Automatically scrub secrets from runtime events" is "off", this is a finding.

## Group: SRG-APP-000357-CTR-000800

**Group ID:** `V-253542`

### Rule: The node that runs Prisma Cloud Compute containers must have sufficient disk space to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-253542r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure sufficient storage capacity in which to write the audit logs, Prisma Cloud compute must be able to allocate audit record storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When deploying Prisma Cloud Compute within a Kubernetes cluster, the Console's persistent value is by default 100GB. The logs are stored within this persistent volume. Within the Kubernetes cluster, issue the command "kubectl get pv". If the twistlock/twistlock-console claim's capacity is not 100GB or greater, this is a finding.

## Group: SRG-APP-000384-CTR-000915

**Group ID:** `V-253543`

### Rule: The configuration integrity of the container platform must be ensured and vulnerabilities policies must be configured.

**Rule ID:** `SV-253543r961473_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Prisma Cloud Compute's vulnerabilities defense is the set of features that provides both predictive and threat-based active protection for running containers. Consistent application of Prisma Cloud Compute vulnerabilities policies ensures the continual application of policies and the associated effects. Prisma Cloud Compute's configurations must be monitored for configuration drift and addressed according to organizational policy. Satisfies: SRG-APP-000384-CTR-000915, SRG-APP-000384-CTR-000915, SRG-APP-000456-CTR-001125, SRG-APP-000516-CTR-001335</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that vulnerabilities policies are enabled, navigate to Prisma Cloud Compute Console's Defend >> Vulnerabilities. Select the "Code repositories" tab. For the "Repositories" and "CI" tab: - If "Default - alert all components" does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default - alert all components". - If the policy is disabled, this is a finding. - Click the "Default - alert all components" policy row. - If "Default - alert all components" is not scoped to "All", this is a finding. Select the "Images" tab. For the "CI" and "Deployed" tab: - If "Default - alert all components" does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default - alert all components". - If the policy is disabled, this is a finding. - Click the "Default - alert all components" policy row. - If "Default - alert all components" is not scoped to "All", this is a finding. Select the "Hosts" tab. For the "Running hosts" and "VM images" tab: - If the "Default - alert all components" does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default - alert all components". - If the policy is disabled, this is a finding. - Click the "Default - alert all components" policy row. - If "Default - alert all components" is not scoped to "All", this is a finding. Select the "Functions" tab. For the "Functions" and "CI" tab: - If the "Default - alert all components" does not exist, this is a finding. - Click the three dots in the "Actions" column for rule "Default - alert all components". - If the policy is disabled, this is a finding. - Click the "Default - alert all components" policy row. - If "Default - alert all components" is not scoped to "All", this is a finding.

## Group: SRG-APP-000384-CTR-000915

**Group ID:** `V-253544`

### Rule: Prisma Cloud Compute must be configured to scan images that have not been instantiated as containers.

**Rule ID:** `SV-253544r961473_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Prisma Cloud Compute ships with "only scan images with running containers" set to "on". To meet the requirements, "only scan images with running containers" must be set to "off" to disable or remove components that are not required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> System >> Scan tab. Verify that for Running images, For Running images, "Only scan images with running containers" is set to "Off". If "Only scan images with running containers" is set to "On", this is a finding.

## Group: SRG-APP-000390-CTR-000930

**Group ID:** `V-253545`

### Rule: Prisma Cloud Compute Defender must reestablish communication to the Console via mutual TLS v1.2 WebSocket session.

**Rule ID:** `SV-253545r986174_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the secure WebSocket session between the Prisma Cloud Compute Console and Defenders is disconnected, the Defender will continually attempt to reestablish the session. Without reauthentication, unidentified or unknown devices may be introduced; thereby facilitating malicious activity. The Console must be configured to remove a Defender that has not established a connection in a specified period of days.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Defenders. Select the "Manage" tab. Select the "Defenders" tab. Click "Advanced Settings". If "Automatically remove disconnected Defenders after (days)" is not configured to the organization's policies, this is a finding.

## Group: SRG-APP-000414-CTR-001010

**Group ID:** `V-253546`

### Rule: Prisma Cloud Compute Defender containers must run as root.

**Rule ID:** `SV-253546r1050656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, the nature of the vulnerability scanning may be more intrusive, or the container platform component that is the subject of the scanning may contain highly sensitive information. To protect the sensitive nature of such scanning, Prisma Cloud Compute Defenders perform the vulnerability scanning function. The Defender container must run as root and not privileged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that when deploying the Defender via daemonSet, "Run Defenders as privileged" is set to "On". Verify the Defender containers were deployed using the daemonSet.yaml in which the securityContext is privileged (privileged = "on"). If "Run Defenders as privileged" is not set to "On" or the Defender containers were not deployed using the daemonSet.yaml in which the securityContext - privileged = "on", this is a finding.

## Group: SRG-APP-000431-CTR-001065

**Group ID:** `V-253547`

### Rule: Prisma Cloud Compute must run within a defined/separate namespace (e.g., Twistlock).

**Rule ID:** `SV-253547r961608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Namespaces are a key boundary for network policies, orchestrator access control restrictions, and other important security controls. Prisma Cloud Compute containers running within a separate and exclusive namespace will inherit the namespace's security features. Separating workloads into namespaces can help contain attacks and limit the impact of mistakes or destructive actions by authorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the Kubernetes namespace in which Prisma Cloud Compute is deployed: $ kubectl get pods -n twistlock NAME READY STATUS RESTARTS AGE twistlock-console-855744b66b-xs9cm 1/1 Running 0 4d6h twistlock-defender-ds-99zj7 1/1 Running 0 58d twistlock-defender-ds-drsh8 1/1 Running 0 58d Inspect the list of pods. If a non-Prisma Cloud Compute (does not start with "twistlock") pod is running in the same namespace, this is a finding.

## Group: SRG-APP-000439-CTR-001080

**Group ID:** `V-253548`

### Rule: Prisma Cloud Compute must protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-253548r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> System >> General tab. Inspect the Telemetry section. If "Share telemetry on product usage with Palo Alto Networks" is "On", this is a finding. If "Allow admins and operators to upload logs to Customer Support directly from Console UI" is "On", this is a finding.

## Group: SRG-APP-000454-CTR-001110

**Group ID:** `V-253549`

### Rule: Prisma Cloud Compute must be running the latest release.

**Rule ID:** `SV-253549r961677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prisma Cloud Compute releases are distributed as Docker images. Each release updates or removes components as needed based on the vulnerabilities associated with the component or the functional need of the component.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the Prisma Cloud Compute Console. In the top right corner, click the bell icon. A banner with the version will display. If there is a newer version, this is a finding.

## Group: SRG-APP-000456-CTR-001130

**Group ID:** `V-253550`

### Rule: Prisma Cloud Compute's Intelligence Stream must be kept up to date.

**Rule ID:** `SV-253550r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Prisma Cloud Compute Console pulls the latest vulnerability and threat information from the Intelligence Stream (intelligence.twistlock.com). The Prisma Cloud Intelligence Stream provides timely vulnerability data collected and processed from a variety of certified upstream sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> System >> Intelligence tab. If the "Last streams update" date is older than 36 hours, this is a finding.

## Group: SRG-APP-000473-CTR-001175

**Group ID:** `V-253551`

### Rule: Configuration of Prisma Cloud Compute must be continuously verified.

**Rule ID:** `SV-253551r961734_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prisma Cloud Compute's configuration of Defender deployment must be monitored to ensure monitoring and protection of the environment is in accordance with organizational policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Prisma Cloud Compute Console's >> Manage >> Defenders. Select the "Manage" tab. Select the "Defenders" tab. Determine the deployment status of the Defenders. If a Defender is not deployed to intended workload(s) to be protected, this is a finding.

## Group: SRG-APP-000610-CTR-001385

**Group ID:** `V-253552`

### Rule: Prisma Cloud Compute release tar distributions must have an associated SHA-256 digest.

**Rule ID:** `SV-253552r961896_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Each Prisma Cloud Compute release's tar file has an associated SHA-256 digest hash value to ensure the components have not been modified.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Offline Intelligence Stream: If using Iron Bank distribution of Prisma Cloud Compute Console and Defenders, verify the Console and Defender imageID SHA256 values match the Palo Alto Networks published release values. For the Console and Defender images, perform the following command: $ docker inspect twistlock/private:console_22_01_839 | grep '"Image":' "Image": "sha256:dcd881fe9c796ed08867c242389737c4f2e8ab463377a90deddc0add4c3e8524", If the imageID values do not match the published release SHA256 for the version of the image release, this is a finding. Note: Image tag will be the release number, e.g., console_22_01_839. Published release image sha values are published here: https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-compute-edition-public-sector/isolated_upgrades/releases.html

