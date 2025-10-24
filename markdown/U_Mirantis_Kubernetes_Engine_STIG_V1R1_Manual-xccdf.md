# STIG Benchmark: Mirantis Kubernetes Engine Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000190-CTR-000500

**Group ID:** `V-260903`

### Rule: The Lifetime Minutes and Renewal Threshold Minutes Login Session Controls on MKE must be set.

**Rule ID:** `SV-260903r966066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "Lifetime Minutes" and "Renewal Threshold Minutes" login session controls in MKE are part of security features that help manage user sessions within the MKE environment. Setting these controls is essential. MKE must terminate all network connections associated with a communications session at the end of the session, or as follows: For in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the MKE web UI and navigate to admin >> Admin Settings >> Authentication & Authorization. Ensure that "Lifetime Minutes" is set to "10" and "Renewal Threshold Minutes" is set to "0". If these settings are not configured as specified, this is a finding.

## Group: SRG-APP-000133-CTR-000290

**Group ID:** `V-260904`

### Rule: In an MSR organization, user permissions and repositories must be configured.

**Rule ID:** `SV-260904r966069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring user permissions, organizations, and repositories in MSR is crucial for maintaining a secure, organized, and efficient container image management environment. This will provide access control, security, and compliance when utilizing MSR.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MSR is not being utilized, this is Not Applicable. Verify the organization, user permissions, and repositories in MSR are configured per the System Security Plan (SSP). Obtain and review the SSP. 1. Log in to the MSR web UI as Admin and navigate to "Organizations". Verify the list of organizations are setup per the SSP. 2. Navigate to "Users" and verify that the list of users are assigned to appropriate organizations per the SSP. 3. Click on the user and verify the assigned repositories are appropriate per the SSP. If the organization, user, or assigned repositories in MSR are not configured per the SSP, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260905`

### Rule: User-managed resources must be created in dedicated namespaces.

**Rule ID:** `SV-260905r966072_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Dedicated namespaces act as security boundaries, limiting the blast radius in case of security incidents or misconfigurations. If an issue arises within a specific namespace, it is contained within that namespace and does not affect the resources in other namespaces. Kubernetes provides Role-Based Access Control (RBAC) mechanisms, and namespaces are a fundamental unit for access control. Using dedicated namespaces for user-managed resources provides a level of isolation. Each namespace acts as a separate environment, allowing users or teams to deploy their applications and services without interfering with the resources in other namespaces. This isolation helps prevent unintentional conflicts and ensures a more predictable deployment environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies when using Kubernetes orchestration. Log in to the MKE web UI and navigate to Kubernetes >> Namespaces. The default namespaces are: "default", "kube-public", and "kube-node-lease". 1. In the top right corner, if "Set context for all namespaces" is not enabled, this is a finding. 2. Navigate to Kubernetes >> Services. Confirm that no service except "kubernetes" has the "default" namespace listed. Confirm that only approved system services have the "kube-system" namespace listed. If "default" has a service other than the "kubernetes" services, this is a finding. If "kube-system" has a service that is not listed in the System Security Plan (SSP), this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-260906`

### Rule: Least privilege access and need to know must be required to access MKE runtime and instantiate container images.

**Rule ID:** `SV-260906r966075_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To control what is instantiated within MKE, it is important to control access to the runtime. Without this control, container platform specific services and customer services can be introduced without receiving approval and going through proper testing. Only those individuals and roles approved by the organization can have access to the container platform runtime.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access to use the docker CLI must be limited to root only. 1. Log on to the host CLI and execute the following: stat -c %U:%G /var/run/docker.sock | grep -v root:docker If any output is present, this is a finding. 2. Verify that the docker group has only the required users by executing: getent group docker If any users listed are not required to have direct access to MCR, this is a finding. 3. Execute the following command to verify the Docker socket file has permissions of 660 or more restrictive: stat -c %a /var/run/docker.sock If permissions are not set to "660", this is a finding.

## Group: SRG-APP-000142-CTR-000325

**Group ID:** `V-260907`

### Rule: Only required ports must be open on containers in MKE.

**Rule ID:** `SV-260907r966078_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Ports, protocols, and services within MKE runtime must be controlled and conform to the PPSM CAL. Those ports, protocols, and services that fall outside the PPSM CAL must be blocked by the runtime. Instructions on the PPSM can be found in DOD Instruction 8551.01 Policy. A container can be run just with the ports defined in the Dockerfile for its image or can be arbitrarily passed runtime parameters to open a list of ports. A periodic review of open ports must be performed. By default, all the ports that are listed in the Dockerfile under EXPOSE instruction for an image are opened when a container is run with -P or --publish-all flag.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be executed on all nodes in an MKE cluster to ensure that mapped ports are the ones that are needed by the containers. Via CLI: Linux: As an administrator, execute the following command using a Universal Control Plane (MKE) client bundle: docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure the ports mapped are those needed for the container. If there are any mapped ports not documented by the System Security Plan (SSP), this is a finding.

## Group: SRG-APP-000172-CTR-000440

**Group ID:** `V-260908`

### Rule: FIPS mode must be enabled.

**Rule ID:** `SV-260908r966081_rule`
**Severity:** high

**Description:**
<VulnDiscussion>During any user authentication, MKE must use FIPS-validated SHA-2 or later protocol to protect the integrity of the password authentication process. FIPS mode enforces the use of cryptographic algorithms and modules. This ensures a higher level of cryptographic security, reducing the risk of vulnerabilities related to cryptographic functions. FIPS-compliant cryptographic modules are designed to provide strong protection for sensitive data. Enabling FIPS mode helps safeguard cryptographic operations, securing data both at rest and in transit within containerized applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the MKE controller, verify FIPS mode is enabled. Execute the following command through the CLI: docker info The "Security Options" section in the response must show a "fips" label, indicating that, when configured, the remotely accessible MKE UI uses FIPS-validated digital signatures in conjunction with an approved hash function to protect the integrity of remote access sessions. If the "fips" label is not shown in the "Security Options" section, then this is a finding.

## Group: SRG-APP-000023-CTR-000055

**Group ID:** `V-260909`

### Rule: MKE must be configured to integrate with an Enterprise Identity Provider.

**Rule ID:** `SV-260909r966084_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring MKE to integrate with an Enterprise Identity Provider enhances security, simplifies user management, ensures compliance, provides auditing capabilities, and offers a more seamless and consistent user experience. It aligns MKE with enterprise standards and contributes to a more efficient and secure environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Enterprise Identity Provider integration is enabled and properly configured in the MKE Admin Settings. 1. Log in to the MKE web UI and navigate to admin >> Admin Settings >> Authentication & Authorization. If LDAP or SAML are not set to "Enabled", this is a finding. 2. Identity Provider configurations: When using LDAP, ensure the following are set: - LDAP/AD server's URL. - Reader DN. - Reader Password. When using SAML: In the "SAML IdP Server" section, ensure the following: - URL for the identity provider exists in the "IdP Metadata URL" field. - Skip TLS Verification is unchecked. - Root Certificate Bundle is filled. In the "SAML Service Provider" section, ensure the MKE Host field has the MKE UI IP address. If the Identity Provider configurations do not match the System Security Plan (SSP), this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-260910`

### Rule: SSH must not run within Linux containers.

**Rule ID:** `SV-260910r966087_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To limit the attack surface of MKE, it is important that the nonessential services are not installed. Containers are designed to be lightweight and isolated, and introducing SSH can add attack vectors. Unauthorized access or exploitation of SSH vulnerabilities would compromise the security of the container and the host system. SSH is not necessary for process management within containers, as container orchestration platforms provide mechanisms for starting, stopping, and monitoring containerized processes. SSH access within containers may bypass auditing mechanisms, making it harder to track and audit user activities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be executed on all nodes in a Docker Enterprise cluster. Verify no running containers have a process for SSH server. Using CLI, execute the following: for i in $(docker container ls --format "{{.ID}}"); do pid=$(docker inspect -f '{{.State.Pid}}' "$i") ps -h --ppid "$pid" -o cmd done | grep sshd If a container is output, it has a process for SSH server, this is a finding.

## Group: SRG-APP-000033-CTR-000100

**Group ID:** `V-260911`

### Rule: Swarm Secrets or Kubernetes Secrets must be used.

**Rule ID:** `SV-260911r966090_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Swarm Secrets in Docker Swarm and Kubernetes Secrets both provide mechanisms for encrypting sensitive data at rest. This adds an additional layer of security, ensuring that even if unauthorized access occurs, the stored secrets remain encrypted. MKE keystore must implement encryption to prevent unauthorized disclosure of information at rest within MKE. By leveraging Docker Secrets or Kubernetes secrets to store configuration files and small amounts of user-generated data (up to 500 kb in size), the data is encrypted at rest by the Engine's FIPS-validated cryptography.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the System Security Plan (SSP) and identify applications that leverage configuration files and/or small amounts of user-generated data, and ensure the data is stored in Docker Secrets or Kubernetes Secrets. When using Swarm orchestration, log in to the MKE web UI and navigate to Swarm >> Secrets and view the configured secrets. If items identified for secure storage are not included in the secrets, this is a finding. When using Kubernetes orchestration, log on to the MKE Controller node then run the following command: kubectl get all -o jsonpath='{range .items[?(@..secretKeyRef)]} {.kind} {.metadata.name} {"\n"}{end}' -A Or, using API, configure the $AUTH variable to contain the token for the SCIM API endpoint: curl -k 'Accept: application/json' -H "Authorization: Bearer $AUTH" -s "https://$MKE_ADDRESS/api/MKE/config/kubernetes" | jq '.KMSEnabled' true If any of the values returned reference environment variables, this is a finding.

## Group: SRG-APP-000038-CTR-000105

**Group ID:** `V-260912`

### Rule: MKE must have Grants created to control authorization to cluster resources.

**Rule ID:** `SV-260912r966093_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MKE uses Role-Based Access Controls (RBAC) to enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. Using an IDP (per this STIG) still requires configure mapping. Refer to the following for more information: https://docs.mirantis.com/mke/3.7/ops/authorize-rolebased-access/rbac-tutorials/access-control-standard.html#access-control-standard.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the applied RBAC policies set in MKE are configured per the requirements set forth by the System Security Plan (SSP). Log in to the MKE web UI as an MKE Admin and navigate to Access Control >> Grants. When using Kubernetes orchestration, select the "Kubernetes" tab and verify that cluster role bindings are configured per the requirements set forth by the SSP. When using Swarm orchestration, select the "Swarm" tabs. Verify that all grants are configured per the requirements set forth by the SSP. If the grants are not configured per the requirements set forth by the SSP, then this is a finding.

## Group: SRG-APP-000039-CTR-000110

**Group ID:** `V-260913`

### Rule: MKE host network namespace must not be shared.

**Rule ID:** `SV-260913r966096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MKE can be built with privileges that are not approved within the organization. To limit the attack surface of MKE, it is essential that privileges meet organization requirements. The networking mode on a container when set to --net=host, skips placing the container inside a separate network stack. This is potentially dangerous because it allows the container process to open low-numbered ports like any other root process. Thus, a container process can potentially do unexpected things such as shutting down the Docker host. Do not use this option. By default, bridge mode is used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using Kubernetes orchestration, ensure that Pods do not use the host machine's network namespace and uses its own isolated network namespace. Note: If the hostNetwork field is not explicitly set in the Pod's specification, it will use the default behavior, which is equivalent to hostNetwork: false. Execute the following for all pods: kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.hostNetwork == true) | .metadata.name' If the above command returns a namespace then the "hostNetwork" = true, this is a finding unless a documented exception is present in the System Security Plan (SSP). When using Swarm orchestration, check that the host's network namespace is not shared. Via CLI: Linux: As an administrator, execute the following command using a Universal Control Plane (MKE) client bundle: docker ps --filter "label=com.docker.ucp.version" | awk '{print $1}' | xargs docker inspect --format '{{ .Name }}: NetworkMode={{ .HostConfig.NetworkMode }}' If the above command returns NetworkMode=host, this is a finding unless a documented exception is present in the SSP.

## Group: SRG-APP-000092-CTR-000165

**Group ID:** `V-260914`

### Rule: Audit logging must be enabled on MKE.

**Rule ID:** `SV-260914r966099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling audit logging on MKE enhances security, supports compliance efforts, provides user accountability, and offers valuable insights for incident response and operational management. It is an essential component of maintaining a secure, compliant, and well-managed Kubernetes environment. Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check auditing configuration level for MKE nodes and controller: Log in to the MKE web UI and navigate to admin >> Admin Settings >> Logs & Audit Logs. If "AUDIT LOG LEVEL" is not set to "Request", this is a finding. If "DEBUG LEVEL" is set to "ERROR", this is a finding.

## Group: SRG-APP-000109-CTR-000215

**Group ID:** `V-260915`

### Rule: MKE must be configured to send audit data to a centralized log server.

**Rule ID:** `SV-260915r966102_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sending audit data from MKE to a centralized log server enhances centralized monitoring, facilitates efficient incident response, scales effectively, provides redundancy, and helps organizations meet compliance requirements. This is the recommended best practice for managing Kubernetes environments, especially in enterprise settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check centralized log server configuration. Via CLI, execute the following commands as a trusted user on the host operating system: cat /etc/docker/daemon.json Verify that the "log-driver" property is set to one of the following: "syslog", "journald", or "<plugin>" (where <plugin> is the naming of a third-party Docker logging driver plugin). Work with the SIEM administrator to determine if an alert is configured when audit data is no longer received as expected. If "log-driver" is not set, or if alarms are not configured in the SIEM, then this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260916`

### Rule: MSR's self-signed certificates must be replaced with DOD trusted, signed certificates.

**Rule ID:** `SV-260916r966105_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Self-signed certificates pose security risks, as they are not issued by a trusted third party. DOD trusted, signed certificates have undergone a validation process by a trusted CA, reducing the risk of man-in-the-middle attacks and unauthorized access. Using these certificates enhances the trust and authenticity of the communication between clients and the MSR server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MSR is not being utilized, this is Not Applicable. Check that MSR has been integrated with a trusted certificate authority (CA). 1. In one terminal window execute the following: kubectl port-forward service/msr 8443:443 2. In a second terminal window execute the following: openssl s_client -connect localhost:8443 -showcerts </dev/null If the certificate chain in the output is not valid and does not match that of the trusted CA, then this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260917`

### Rule: Allowing users and administrators to schedule containers on all nodes must be disabled.

**Rule ID:** `SV-260917r966108_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MKE and MSR are set to disallow administrators and users to schedule containers. This setting must be checked for allowing administrators or users to schedule containers may override essential settings, and therefore is not permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure this setting has not been modified follow these steps on each node: Log in to the MKE web UI and navigate to admin >> Admin Settings >> Orchestration. Scroll to down "Container Scheduling". Verify that the "Allow administrators to deploy containers on MKE managers or nodes running MSR" is disabled. If it is checked (enabled), this is a finding. Verify that the "Allow users to schedule on all nodes, including MKE managers and MSR nodes" is disabled. If it is checked (enabled), this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260918`

### Rule: MKE telemetry must be disabled.

**Rule ID:** `SV-260918r966111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MKE provides a telemetry service that automatically records and transmits data to Mirantis through an encrypted channel for monitoring and analysis purposes. While this channel is secure, it introduces an attack vector and must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that usage and API analytics tracking is disabled in MKE. Log in to the MKE web UI and navigate to admin >> Admin Settings >> Usage. Verify the "Enable hourly usage reporting" and "Enable API and UI tracking" options are both unchecked. If either box is checked, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260919`

### Rule: MSR telemetry must be disabled.

**Rule ID:** `SV-260919r966114_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MSR provides a telemetry service that automatically records and transmits data to Mirantis through an encrypted channel for monitoring and analysis purposes. While this channel is secure, it introduces an attack vector and must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MSR is not being utilized, this is Not Applicable. Verify that usage and API analytics tracking is disabled in MSR. Log in to the MSR web UI and navigate to System >> General Tab. Scroll to the "Analytics" section. If the "Send data" option is enabled, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260920`

### Rule: For MKE's deployed on an Ubuntu host operating system, the AppArmor profile must be enabled.

**Rule ID:** `SV-260920r966117_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>AppArmor protects the Ubuntu OS and applications from various threats by enforcing security policy which is also known as AppArmor profile. The user can either create their own AppArmor profile for containers or use the Docker default AppArmor profile. This would enforce security policies on the containers as defined in the profile. By default, docker-default AppArmor profile is applied for running containers and this profile can be found at /etc/apparmor.d/docker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MKE is not being used on an Ubuntu host operating system, this is Not Applicable. If AppArmor is not in use, this is Not Applicable. This check must be executed on all nodes in a cluster. Via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps -a -q | xargs -I {} docker inspect {} --format '{{ .Name }}: AppArmorProfile={{ .AppArmorProfile }}, Privileged={{ .HostConfig.Privileged }}' | grep 'AppArmorProfile=unconfined' | grep 'Privileged=false' If any output, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260921`

### Rule: If MKE is deployed on a Red Hat or CentOS system, SELinux security must be enabled.

**Rule ID:** `SV-260921r966120_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SELinux provides a Mandatory Access Control (MAC) system on RHEL and CentOS that greatly augments the default Discretionary Access Control (DAC) model. The user can thus add an extra layer of safety by enabling SELinux on the RHEL or CentOS host. When applied to containers, SELinux helps isolate and restrict the actions that containerized processes can perform, reducing the risk of container escapes and unauthorized access. By default, no SELinux security options are applied on containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using MKE on operating systems other than Red Hat Enterprise Linux or CentOS host operating systems where SELinux is in use, this check is Not Applicable. Execute on all nodes in a cluster. Verify that the appropriate security options are configured for all running containers: Via CLI: Linux: Execute the following command as a user on the host operating system: docker info --format '{{.SecurityOptions}}' expected output [name=seccomp, profile=default name=selinux name=fips] If there is no output or name does not equal SELinux, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260922`

### Rule: The Docker socket must not be mounted inside any containers.

**Rule ID:** `SV-260922r966123_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Docker socket docker.sock must not be mounted inside a container, with the exception case being during the installation of Universal Control Plane (UCP) component of Docker Enterprise as it is required for install. If the Docker socket is mounted inside a container, it would allow processes running within the container to execute docker commands which effectively allows for full control of the host. By default, docker.sock (Linux) and \\.\pipe\docker_engine (Windows) is not mounted inside containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using Kubernetes orchestration, this check is Not Applicable. When using Swarm orchestration, log in to the CLI as an MKE Admin, and execute the following command using an MKE client bundle: docker ps --all --filter "label=com.docker.ucp.version" | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}' | grep -i "docker.sock\|docker_engine" If the Docker socket is mounted inside containers, this is a finding. If "volumes" is not present or if "docker.sock" is listed, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260923`

### Rule: Linux Kernel capabilities must be restricted within containers.

**Rule ID:** `SV-260923r966126_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, MKE starts containers with a restricted set of Linux Kernel Capabilities. Any process may be granted the required capabilities instead of root access. Using Linux Kernel Capabilities, the processes do not have to run as root for almost all the specific areas where root privileges are usually needed. MKE supports the addition and removal of capabilities, allowing the use of a nondefault profile. Remove all capabilities except those explicitly required for the user's container process. By default, below capabilities are available for Linux containers: AUDIT_WRITE CHOWN DAC_OVERRIDE FOWNER FSETID KILL MKNOD NET_BIND_SERVICE NET_RAW SETFCAP SETGID SETPCAP SETUID SYS_CHROOT</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using Kubernetes orchestration this check is Not Applicable. When using Swarm orchestration, via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Name }}: CapAdd={{ .HostConfig.CapAdd }} CapDrop={{ .HostConfig.CapDrop }}' The command will output all Linux Kernel Capabilities. If Linux Kernel Capabilities exceed what is defined in the System Security Plan (SSP), this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260924`

### Rule: Incoming container traffic must be bound to a specific host interface.

**Rule ID:** `SV-260924r966129_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged ports are those ports below 1024 and that require system privileges for their use. If containers are able to use these ports, the container must be run as a privileged user. MKE must stop containers that try to map to these ports directly. Allowing nonprivileged ports to be mapped to the container-privileged port is the allowable method when a certain port is needed. An example is mapping port 8080 externally to port 80 in the container. By default, if the user does not specifically declare the container port to host port mapping, MKE automatically and correctly maps the container port to one available in 49153-65535 block on the host. But, MKE allows a container port to be mapped to a privileged port on the host if the user explicitly declared it. This is because containers are executed with NET_BIND_SERVICE Linux kernel capability that does not restrict the privileged port mapping. The privileged ports receive and transmit various sensitive and privileged data. Allowing containers to use them can bring serious implications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be executed on all nodes in an MKE cluster. Verify that no running containers are mapping host port numbers below 1024. Via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure that container ports are not mapped to host port numbers below 1024. If they are, then this is a finding. Ensure that there is no such container to host privileged port mapping declarations in the Mirantis config file. View the config file. If container to host privileged port mapping declarations exist, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260925`

### Rule: CPU priority must be set appropriately on all containers.

**Rule ID:** `SV-260925r966132_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All containers on a Docker host share the resources equally. By using the resource management capabilities of Docker host, such as CPU shares, the user controls the host CPU resources that a container may consume. By default, CPU time is divided between containers equally. If CPU shares are not properly set, the container process may have to starve if the resources on the host are not available. If the CPU resources on the host are free, CPU shares do not place any restrictions on the CPU that the container may use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure Resource Quotas and CPU priority is set for each namespace. When using Kubernetes orchestration: Log in to the MKE web UI, navigate to Kubernetes >> Namespace, and then click on each defined Namespace. If the Namespace states "Quotas Nothing has been defined for this resource." or the limits.cpu or the limits.memory settings do not match the System Security Plan (SSP), this is a finding. When using Swarm orchestration: 1. Check Resource Quotas: Linux: As an administrator, execute the following command using a Universal Control Plane (MKE) client bundle: docker ps --quiet --filter """"label=com.docker.ucp.version"""" | xargs docker inspect --format '{{ .Name }}: Memory={{ .HostConfig.Memory }}' If the above command returns "0", it means the memory limits are not in place, and this is a finding. 2. Check CPU Priority: When using Swarm orchestration, to ensure CPU priority is set, use the CLI: Linux: As an MKE Admin, execute the following command using a Universal Control Plane (MKE) client bundle: docker ps --quiet --filter ""label=com.docker.ucp.version"" | xargs docker inspect --format '{{ .Name }}: CpuShares={{ .HostConfig.CpuShares }}' Compare the output against the SSP, if any containers are set to "0" or "1024", and they are not documented in the System Security Plan (SSP), this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-260926`

### Rule: MKE must use a non-AUFS storage driver.

**Rule ID:** `SV-260926r966135_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The aufs storage driver is an old driver based on a Linux kernel patch-set that is unlikely to be merged into the main Linux kernel. aufs driver is also known to cause some serious kernel crashes. aufs only has legacy support from Docker. Most importantly, aufs is not a supported driver in many Linux distributions using latest Linux kernels.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default storage driver for MCR is overlay2. To confirm this has not been changed via CLI: As a trusted user on the underlying host operating system, execute the following command: docker info | grep -e "Storage Driver:" If the Storage Driver setting contains *aufs or *btrfs, then this is a finding. If the above command returns no values, this is not a finding.

## Group: SRG-APP-000141-CTR-000320

**Group ID:** `V-260927`

### Rule: MKE's self-signed certificates must be replaced with DOD trusted, signed certificates.

**Rule ID:** `SV-260927r966138_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Self-signed certificates pose security risks, as they are not issued by a trusted third party. DOD trusted, signed certificates have undergone a validation process by a trusted CA, reducing the risk of man-in-the-middle attacks and unauthorized access. MKE uses TLS to protect sessions. Using trusted certificates ensures that only trusted sources can access the MKE cluster.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Kubernetes ingress is being used, this is Not Applicable. Check that MKE has been integrated with a trusted certificate authority (CA). Log in to the MKE web UI and navigate to admin >> Admin Settings >> Certificates. Click "Download MKE Server CA Certificate". Verify that the contents of the downloaded "ca.pem" file match that of the trusted CA certificate. If the certificate chain does not match the chain as defined by the System Security Plan (SSP), then this is a finding.

## Group: SRG-APP-000141-CTR-000320

**Group ID:** `V-260928`

### Rule: The "Create repository on push" option in MSR must be disabled.

**Rule ID:** `SV-260928r966141_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing repositories to be created on a push can override essential settings and must not be allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MSR is not being utilized, this is Not Applicable. Verify the "Create repository on push" option is disabled in MSR: Log in to the MSR web UI as an administrator and navigate to System >> General Tab >>Repositories Section. Verify the "Create repository on push" slider is turned off. If it is turned on, this is a finding.

## Group: SRG-APP-000142-CTR-000330

**Group ID:** `V-260929`

### Rule: Containers must not map to privileged ports.

**Rule ID:** `SV-260929r966144_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged ports are those ports below 1024 and that require system privileges for their use. If containers are able to use these ports, the container must be run as a privileged user. MKE must stop containers that try to map to these ports directly. Allowing nonprivileged ports to be mapped to the container-privileged port is the allowable method when a certain port is needed. An example is mapping port 8080 externally to port 80 in the container. By default, if the user does not specifically declare the container port to host port mapping, MKE automatically and correctly maps the container port to one available in 49153-65535 block on the host. But, MKE allows a container port to be mapped to a privileged port on the host if the user explicitly declared it. This is because containers are executed with NET_BIND_SERVICE Linux kernel capability that does not restrict the privileged port mapping. The privileged ports receive and transmit various sensitive and privileged data. Allowing containers to use them can bring serious implications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be executed on all nodes in an MKE cluster. Verify no running containers are mapping host port numbers below 1024. Via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure container ports are not mapped to host port numbers below 1024. If they are, then this is a finding.

## Group: SRG-APP-000148-CTR-000345

**Group ID:** `V-260930`

### Rule: MKE must not permit users to create pods that share host process namespace.

**Rule ID:** `SV-260930r966147_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Controlling information flow between MKE components and container user services instantiated by MKE must enforce organization-defined information flow policies. Example methods for information flow control are: using labels for containers to segregate services; user permissions and roles to limit what user services are available to each user; controlling the user the services are able to execute as; and limiting inter-container network traffic and the resources containers can consume. Process ID (PID) namespaces isolate the PID number space, meaning that processes in different PID namespaces can have the same PID. This is process level isolation between containers and the host. PID namespace provides separation of processes and removes the view of the system processes, and allows process IDs to be reused including PID 1. If the host's PID namespace is shared with the container, it would allow processes within the container to view all of the processes on the host system. Container processes cannot view the processes on the host system. In certain cases, such as system-level containers, the container must share the host's process namespace. System-level containers have a defined label and this access must be documented. By default, all containers have the PID namespace enabled and the host's process namespace is not shared with the containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using Kubernetes orchestration, this check is Not Applicable. When using Swarm orchestration, to ensure the host's process namespace is not shared, log in via CLI: Execute the following using the MKE client bundle: container_ids=$(docker ps --quiet --filter=label=com.docker.ucp.version) for container_id in $container_ids do container_name=$(docker inspect -f '{{.Name}}' $container_id | cut -c2-) pid_mode=$(docker inspect -f '{{.HostConfig.PidMode}}' $container_id) echo "Container Name: $container_name, ID: $container_id, PidMode: $pid_mode" done If PidMode = "host", this is a finding.

## Group: SRG-APP-000158-CTR-000390

**Group ID:** `V-260931`

### Rule: IPSec network encryption must be configured.

**Rule ID:** `SV-260931r966150_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IPsec encrypts the data traffic between nodes in a Kubernetes cluster, ensuring that the information exchanged is confidential and protected from unauthorized access. This is particularly important when sensitive or confidential data is transmitted over the network. IPsec not only provides encryption but also ensures the integrity of the transmitted data. Through the use of cryptographic mechanisms, IPsec can detect and prevent tampering or modification of data during transit. In a Kubernetes cluster managed by MKE, nodes communicate with each other for various purposes, such as pod networking, service discovery, and cluster coordination. IPsec helps secure these communications, reducing the risk of man-in-the-middle attacks and unauthorized interception.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IPSec network encryption. For Swarm orchestration log in to the MKE web UI and navigate to Swarm >> Networks. If the "scope" is not local and the "driver" is not overlay, this is a finding. Kubernetes orchestration: Note: The path may need to be edited. cat /etc/mke/config.toml | grep secure_overlay If the "secure_overlay" settings is not set to "true", this is a finding.

## Group: SRG-APP-000226-CTR-000575

**Group ID:** `V-260932`

### Rule: MKE must preserve any information necessary to determine the cause of the disruption or failure.

**Rule ID:** `SV-260932r966153_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a failure occurs within MKE, preserving the state of MKE and its components, along with other container services, helps to facilitate container platform restart and return to the operational mode of the organization with less disruption to mission essential processes. When preserving state, considerations for preservation of data confidentiality and integrity must be taken into consideration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using Swarm orchestration, this check is Not Applicable. Review the Kubernetes configuration to determine if information necessary to determine the cause of a disruption or failure is preserved. Notes: - The ReadWriteOnce access mode in the PVC means the volume can be mounted as read-write by a single node. Ensure the storage backend supports this mode. - Adjust the sleep duration in the writer pod as needed. - Ensure that the namespace and PVC names match the setup. Steps to verify data durability: 1. Create a namespace to manage the testing: apiVersion: v1 kind: Namespace metadata: name: stig 2. PersistentVolumeClaim (PVC): Ensure a PVC is created. If using a storage class like Longhorn, it would look similar to: apiVersion: v1 kind: PersistentVolumeClaim metadata: name: stig-pvc namespace: stig spec: accessModes: - ReadWriteOnce storageClassName: longhorn # Replace with your storage class if different, e.g. NFS resources: requests: storage: 5Gi 3. Deploying the Initial Pod: Create a pod that writes data to the PVC. This pod will use a simple loop to write data (e.g., timestamps) to a file on the mounted PVC. Example: apiVersion: v1 kind: Pod metadata: name: write-pod namespace: stig spec: volumes: - name: log-storage persistentVolumeClaim: claimName: stig-pvc containers: - name: writer image: busybox command: ["/bin/sh", "-c"] args: ["while true; do date >> /data/logs.log; sleep 10; done"] volumeMounts: - name: log-storage mountPath: /data 4. Simulate Pod Failure: After the pod has been writing data for some time, it can be deleted to simulate a failure by executing the following: kubectl delete pod write-pod -n stig 5. Deploying a New Pod to Verify Data: Deploy another pod that mounts the same PVC to verify that the data is still there. apiVersion: v1 kind: Pod metadata: name: read-pod namespace: stig spec: volumes: - name: log-storage persistentVolumeClaim: claimName: stig-pvc containers: - name: reader image: busybox command: ["/bin/sh", "-c"] args: ["sleep infinity"] volumeMounts: - name: log-storage mountPath: /data 6. Verify Data Persistence: Check the contents of the log file in the new pod to ensure that the data written by the first pod is still there by executing the following: kubectl exec read-pod -n stig -- cat /data/logs.log If there is no log data, this is a finding.

## Group: SRG-APP-000233-CTR-000585

**Group ID:** `V-260933`

### Rule: MKE must enable kernel protection.

**Rule ID:** `SV-260933r966156_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System kernel is responsible for memory, disk, and task management. The kernel provides a gateway between the system hardware and software. Kubernetes requires kernel access to allocate resources to the Control Plane. Threat actors that penetrate the system kernel can inject malicious code or hijack the Kubernetes architecture. It is vital to implement protections through Kubernetes components to reduce the attack surface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify kernel protection. When using Kubernetes orchestration, change to the /etc/sysconfig/ directory on the Kubernetes Control Plane using the command: grep -i protect-kernel-defaults kubelet If the setting "protect-kernel-defaults" is set to false or not set in the Kubernetes Kubelet, this is a finding. When using Swarm orchestration: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Name }}: CapAdd={{ .HostConfig.CapAdd }} CapDrop={{ .HostConfig.CapDrop }}' The command will output all Linux Kernel Capabilities. If Linux Kernel Capabilities exceed what is defined in the System Security Plan (SSP), this is a finding.

## Group: SRG-APP-000243-CTR-000595

**Group ID:** `V-260934`

### Rule: All containers must be restricted from acquiring additional privileges.

**Rule ID:** `SV-260934r966159_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To limit the attack surface of MKE, it is important that the nonessential services are not installed and access to the host system uses the concept of least privilege. Restrict the container from acquiring additional privileges via suid or sgid bits. A process can set the no_new_priv bit in the kernel. It persists across fork, clone, and execve. The no_new_priv bit ensures that the process or its children processes do not gain any additional privileges via suid or sgid bits. This way, many dangerous operations become a lot less dangerous because there is no possibility of subverting privileged binaries. no_new_priv prevents LSMs like SELinux from transitioning to process labels that have access not allowed to the current process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be executed on all nodes in an MKE cluster to ensure all containers are restricted from acquiring additional privileges. Via CLI: Linux: As an MKE Admin, execute the following command using a Universal Control Plane (MKE) client bundle: docker ps --quiet --all | xargs -L 1 docker inspect --format '{{ .Id }}: SecurityOpt={{ .HostConfig.SecurityOpt }}' The above command returns the security options currently configured for the running containers. If the "SecurityOpt=" setting does not include the "no-new-privileges" flag, this is a finding.

## Group: SRG-APP-000243-CTR-000600

**Group ID:** `V-260935`

### Rule: Host IPC namespace must not be shared.

**Rule ID:** `SV-260935r966162_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IPC (POSIX/SysV IPC) namespace provides separation of named shared memory segments, semaphores, and message queues. IPC namespace on the host must not be shared with the containers and remain isolated unless required. If the host's IPC namespace is shared with the container, it would allow processes within the container to view all of the IPC on the host system. This breaks the benefit of IPC level isolation between the host and the containers. Having access to the container can eventually manipulate the host IPC. Do not share the host's IPC namespace with the containers. Only containers with the proper label will share IPC namespace and this access must be documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the "IpcMode" is set to "host" for a running or stopped container. Log in to the MKE WebUI and Navigate to admin >> Admin Settings >> Privileges. If hostIPC is checked for User account privileges or Service account privileges, consult the System Security Plan (SSP). If hostIPC is not allowed per the SSP, this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-260936`

### Rule: All containers must be restricted to mounting the root filesystem as read only.

**Rule ID:** `SV-260936r966165_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The container's root filesystem must be treated as a "golden image" by using Docker run's --read-only option. This prevents any writes to the container's root filesystem at container runtime and enforces the principle of immutable infrastructure. Enabling this option forces containers at runtime to explicitly define their data writing strategy to persist or not persist their data. This also reduces security attack vectors since the container instance's filesystem cannot be tampered with or written to unless it has explicit read-write permissions on its filesystem folder and directories.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using Kubernetes orchestration, this check is Not Applicable. For Swarm orchestration, check via CLI: Linux: As an MKE Admin, execute the following command using a Universal Control Plane (MKE) client bundle: docker ps --quiet --all | xargs -L 1 docker inspect --format '{{ .Name }}: ReadonlyRootfs={{ .HostConfig.ReadonlyRootfs }}' If ReadonlyRootfs=false, it means the container's root filesystem is writable and this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-260937`

### Rule: The default seccomp profile must not be disabled.

**Rule ID:** `SV-260937r966168_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Seccomp filtering provides a means for a process to specify a filter for incoming system calls. The default seccomp profile works on a whitelist basis and allows 311 system calls, blocking all others. It must not be disabled unless it hinders the container application usage. The default seccomp profile blocks syscalls, regardless of --cap-add passed to the container. A large number of system calls are exposed to every user and process, with many of them going unused for the entire lifetime of the process. Most of the applications do not need all the system calls and thus benefit by having a reduced set of available system calls. The reduced set of system calls reduces the total kernel surface exposed to the application and thus improvises application security. When running a container, it uses the default profile unless it is overridden with the --security-opt option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using Kubernetes orchestration, this check is Not Applicable. For Swarm orchestration, to ensure the default seccomp profile is not disabled, log in to the CLI: Linux: As an MKE Admin, execute the following command using a Universal Control Plane (MKE) client bundle: docker ps --quiet --filter "label=com.docker.ucp.version" | xargs docker inspect --format '{{ .Id }}: SecurityOpt={{ .HostConfig.SecurityOpt }}' If seccomp:=unconfined, then the container is running without any seccomp profiles and this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-260938`

### Rule: Docker CLI commands must be run with an MKE client trust bundle and without unnecessary permissions.

**Rule ID:** `SV-260938r966171_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Running docker CLI commands remotely with a client trust bundle ensures that authentication and role permissions are checked for the command. Using --privileged option or --user option in docker exec gives extended Linux capabilities to the command. Do not run docker exec with the --privileged or --user options, especially when running containers with dropped capabilities or with enhanced restrictions. By default, docker exec command runs without --privileged or --user options.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The host OS must be locked down so that only authorized users with a client bundle can access docker commands. To ensure that no commands with privilege or user authorizations are present via CLI: Linux: As a trusted user on the host operating system, use the below command to filter out docker exec commands that used --privileged or --user option. sudo ausearch -k docker | grep exec | grep privileged | grep user If there are any in the output, then this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-260939`

### Rule: MKE users must not have permissions to create containers or pods that share the host user namespace.

**Rule ID:** `SV-260939r966174_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To limit the attack surface of MKE, it is important that the nonessential services are not installed and access to the host system uses the concept of least privilege. User namespaces ensure that a root process inside the container will be mapped to a nonroot process outside the container. Sharing the user namespaces of the host with the container thus does not isolate users on the host with users on the containers. By default, the host user namespace is shared with the containers until user namespace support is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using Kubernetes orchestration, this check is Not Applicable. When using Swarm orchestration, ensure that the PIDs cgroup limit is used. Log in to the CLI as an MKE Admin and execute the following command using a Universal Control Plane (MKE) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: UsernsMode={{ .HostConfig.UsernsMode }}' Ensure it does not return any value for UsernsMode. If it returns a value of "host", that means the host user namespace is shared with the containers, and this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-260940`

### Rule: Use of privileged Linux containers must be limited to system containers.

**Rule ID:** `SV-260940r966177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using the --privileged flag gives all Linux Kernel Capabilities to the container, thus overwriting the --cap-add and --cap-drop flags. The --privileged flag gives all capabilities to the container, and it also lifts all the limitations enforced by the device cgroup controller. Any container that requires this privilege must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When using Kubernetes orchestration, this check is Not Applicable. When using Swarm orchestration, execute the following command as a trusted user on the host operating system via CLI: docker ps --quiet --all | grep -iv "MKE\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: Privileged={{ .HostConfig.Privileged }}' Verify in the output that no containers are running with the --privileged flag. If there are, this is a finding.

## Group: SRG-APP-000383-CTR-000910

**Group ID:** `V-260941`

### Rule: The network ports on all running containers must be limited to required ports.

**Rule ID:** `SV-260941r966180_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To validate that the services are using only the approved ports and protocols, the organization must perform a periodic scan/review of MKE and disable functions, ports, protocols, and services deemed to be unneeded or nonsecure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that only needed ports are open on all running containers. If an ingress controller is configured for the cluster, this check is not applicable. Via CLI: As a remote MKE admin, execute the following command using a client bundle: docker ps -q | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure that the ports mapped are the ones really needed for the containers per the requirements set forth by the System Security Plan (SSP). If ports are not documented and approved in the SSP, this is a finding.

## Group: SRG-APP-000386-CTR-000920

**Group ID:** `V-260942`

### Rule: MKE must only run signed images.

**Rule ID:** `SV-260942r966183_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Controlling the sources where container images can be pulled from allows the organization to define what software can be run within MKE. Allowing any container image to be introduced and instantiated within MKE may introduce malicious code and vulnerabilities to the platform and the hosting system. MKE registry must deny all container images except for those signed by organizational-approved sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On each node, check that MKE is configured to only run images signed by applicable Orgs and Teams. 1. Log in to the MKE web UI and navigate to admin >> Admin Settings >> Docker Content Trust. If Content Trust Settings "Run only signed images" is disabled, this is a finding. 2. Verify that the Orgs and Teams that images must be signed by in the drop-down matches the organizational policies. If an Org or Team selected does not match organizational policies, this is a finding. 3. Verify that all images sitting on an MKE cluster are signed. Via CLI: Linux: As an MKE Admin, execute the following commands using a client bundle: docker trust inspect $(docker images | awk '{print $1 ":" $2}') Verify that all image tags in the output have valid signatures. If the images are not signed, this is a finding.

## Group: SRG-APP-000414-CTR-001010

**Group ID:** `V-260943`

### Rule: Vulnerability scanning must be enabled for all repositories in MSR.

**Rule ID:** `SV-260943r966186_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling vulnerability scanning for all repositories in Mirantis Secure Registry (MSR) is a critical security practice that helps organizations identify and mitigate potential security risks associated with container images. Enabling scanning for all repositories in MSR helps identify and prioritize security issues that could pose risks to the containerized applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MSR is not being utilized, this is Not Applicable. Check image vulnerability scanning enabled for all repositories. Log in to the MSR web UI and navigate to System >> Security Tab. Verify that the "Enable Scanning" slider is turned on and the vulnerability database has been successfully synced (online) or uploaded (offline). If the "Enable Scanning" slider is tuned off, this is a finding. If the vulnerability database is not synced or uploaded, this is a finding.

## Group: SRG-APP-000454-CTR-001110

**Group ID:** `V-260944`

### Rule: Older Universal Control Plane (MKE) and Docker Trusted Registry (DTR) images must be removed from all cluster nodes upon upgrading.

**Rule ID:** `SV-260944r966189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When upgrading either the UCP or DTR components of MKE, the newer images are pulled (or unpacked if offline) onto engine nodes in a cluster. Once the upgrade is complete, one must manually remove all old image version from the cluster nodes to meet the requirements of this control. When upgrading the Docker Engine - Enterprise component of MKE, the old package version is automatically replaced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all outdated MKE and DTR container images have been removed from all nodes in the cluster. Via CLI: As an MKE admin, execute the following command using a client bundle: docker images --filter reference='mirantis/[ucp]*' docker images --filter reference='registry.mirantis.com/msr/[msr]*' Verify there are no tags listed older than the currently installed versions of MKE and DTR. If any of the tags listed are older than the currently installed versions of MKE and DTR, then this is a finding. If no tags are listed, this is not a finding.

## Group: SRG-APP-000456-CTR-001130

**Group ID:** `V-260945`

### Rule: MKE must contain the latest updates.

**Rule ID:** `SV-260945r966192_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MKE must stay up to date with the latest patches, service packs, and hot fixes. Not updating MKE will expose the organization to vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for updates by logging in to the MKE WebUI and Navigating to admin >> Admin Settings >> Upgrade. In the "Choose MKE Version" section, select the drop-down. The UI will provide a list of available versions. If an updated version is available in the list, this is a finding.

## Group: SRG-APP-000068-CTR-000120

**Group ID:** `V-260946`

### Rule: MKE must display the Standard Mandatory DOD Notice and Consent Banner before granting access to platform components.

**Rule ID:** `SV-260946r966195_rule`
**Severity:** low

**Description:**
<VulnDiscussion>MKE has countless components where different access levels are needed. To control access, the user must first log in to MKE and then be presented with a DOD-approved use notification banner before granting access to the component. This guarantees privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MKE configuration to determine if the Standard Mandatory DOD Notice and Consent Banner is configured to be displayed before granting access to platform components. Log in to MKE and verify that the Standard Mandatory DOD Notice and Consent Banner is being displayed before granting access. If the Standard Mandatory DOD Notice and Consent Banner is not configured or is not displayed before granting access to MKE, this is a finding.

