# STIG Benchmark: Kubernetes Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014-CTR-000035

**Group ID:** `V-242376`

### Rule: The Kubernetes Controller Manager must use TLS 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination.

**Rule ID:** `SV-242376r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes Controller Manager will prohibit the use of SSL and unauthorized versions of TLS protocols to properly secure communication. The use of unsupported protocol exposes vulnerabilities to the Kubernetes by rogue traffic interceptions, man-in-the-middle attacks, and impersonation of users or services from the container platform runtime, registry, and key store. To enable the minimum version of TLS to be used by the Kubernetes Controller Manager, the setting "tls-min-version" must be set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i tls-min-version * If the setting "tls-min-version" is not configured in the Kubernetes Controller Manager manifest file or it is set to "VersionTLS10" or "VersionTLS11", this is a finding.

## Group: SRG-APP-000014-CTR-000035

**Group ID:** `V-242377`

### Rule: The Kubernetes Scheduler must use TLS 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination.

**Rule ID:** `SV-242377r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes Scheduler will prohibit the use of SSL and unauthorized versions of TLS protocols to properly secure communication. The use of unsupported protocol exposes vulnerabilities to the Kubernetes by rogue traffic interceptions, man-in-the-middle attacks, and impersonation of users or services from the container platform runtime, registry, and keystore. To enable the minimum version of TLS to be used by the Kubernetes API Server, the setting "tls-min-version" must be set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i tls-min-version * If the setting "tls-min-version" is not configured in the Kubernetes Scheduler manifest file or it is set to "VersionTLS10" or "VersionTLS11", this is a finding.

## Group: SRG-APP-000014-CTR-000040

**Group ID:** `V-242378`

### Rule: The Kubernetes API Server must use TLS 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination.

**Rule ID:** `SV-242378r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes API Server will prohibit the use of SSL and unauthorized versions of TLS protocols to properly secure communication. The use of unsupported protocol exposes vulnerabilities to the Kubernetes by rogue traffic interceptions, man-in-the-middle attacks, and impersonation of users or services from the container platform runtime, registry, and keystore. To enable the minimum version of TLS to be used by the Kubernetes API Server, the setting "tls-min-version" must be set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i tls-min-version * If the setting "tls-min-version" is not configured in the Kubernetes API Server manifest file or it is set to "VersionTLS10" or "VersionTLS11", this is a finding.

## Group: SRG-APP-000014-CTR-000035

**Group ID:** `V-242379`

### Rule: The Kubernetes etcd must use TLS to protect the confidentiality of sensitive data during electronic dissemination.

**Rule ID:** `SV-242379r927237_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes etcd will prohibit the use of SSL and unauthorized versions of TLS protocols to properly secure communication. The use of unsupported protocol exposes vulnerabilities to the Kubernetes by rogue traffic interceptions, man-in-the-middle attacks, and impersonation of users or services from the container platform runtime, registry, and keystore. To enable the minimum version of TLS to be used by the Kubernetes API Server, the setting "--auto-tls" must be set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i auto-tls * If the setting "--auto-tls" is not configured in the Kubernetes etcd manifest file or it is set to true, this is a finding.

## Group: SRG-APP-000014-CTR-000035

**Group ID:** `V-242380`

### Rule: The Kubernetes etcd must use TLS to protect the confidentiality of sensitive data during electronic dissemination.

**Rule ID:** `SV-242380r927238_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes API Server will prohibit the use of SSL and unauthorized versions of TLS protocols to properly secure communication. The use of unsupported protocol exposes vulnerabilities to the Kubernetes by rogue traffic interceptions, man-in-the-middle attacks, and impersonation of users or services from the container platform runtime, registry, and keystore. To enable the minimum version of TLS to be used by the Kubernetes API Server, the setting "--peer-auto-tls" must be set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -I peer-auto-tls * If the setting "--peer-auto-tls" is not configured in the Kubernetes etcd manifest file or it is set to "true", this is a finding.

## Group: SRG-APP-000023-CTR-000055

**Group ID:** `V-242381`

### Rule: The Kubernetes Controller Manager must create unique service accounts for each work payload.

**Rule ID:** `SV-242381r927239_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Kubernetes Controller Manager is a background process that embeds core control loops regulating cluster system state through the API Server. Every process executed in a pod has an associated service account. By default, service accounts use the same credentials for authentication. Implementing the default settings poses a High risk to the Kubernetes Controller Manager. Setting the "--use-service-account-credential" value lowers the attack surface by generating unique service accounts settings for each controller instance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i use-service-account-credentials * If the setting "--use-service-account-credentials" is not configured in the Kubernetes Controller Manager manifest file or it is set to "false", this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-242382`

### Rule: The Kubernetes API Server must enable Node,RBAC as the authorization mode.

**Rule ID:** `SV-242382r927240_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., networks, web servers, and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Node,RBAC is the method within Kubernetes to control access of users and applications. Kubernetes uses roles to grant authorization API requests made by kubelets. Satisfies: SRG-APP-000340-CTR-000770, SRG-APP-000033-CTR-000095, SRG-APP-000378-CTR-000880, SRG-APP-000033-CTR-000090</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i authorization-mode * If the setting authorization-mode is set to "AlwaysAllow" in the Kubernetes API Server manifest file or is not configured, this is a finding.

## Group: SRG-APP-000038-CTR-000105

**Group ID:** `V-242383`

### Rule: User-managed resources must be created in dedicated namespaces.

**Rule ID:** `SV-242383r879533_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Creating namespaces for user-managed resources is important when implementing Role-Based Access Controls (RBAC). RBAC allows for the authorization of users and helps support proper API server permissions separation and network micro segmentation. If user-managed resources are placed within the default namespaces, it becomes impossible to implement policies for RBAC permission, service account usage, network policies, and more.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view the available namespaces, run the command: kubectl get namespaces The default namespaces to be validated are default, kube-public, and kube-node-lease if it is created. For the default namespace, execute the commands: kubectl config set-context --current --namespace=default kubectl get all For the kube-public namespace, execute the commands: kubectl config set-context --current --namespace=kube-public kubectl get all For the kube-node-lease namespace, execute the commands: kubectl config set-context --current --namespace=kube-node-lease kubectl get all The only valid return values are the kubernetes service (i.e., service/kubernetes) and nothing at all. If a return value is returned from the "kubectl get all" command and it is not the kubernetes service (i.e., service/kubernetes), this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-242384`

### Rule: The Kubernetes Scheduler must have secure binding.

**Rule ID:** `SV-242384r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of attack vectors and implementing authentication and encryption on the endpoints available to external sources is paramount when securing the overall Kubernetes cluster. The Scheduler API service exposes port 10251/TCP by default for health and metrics information use. This port does not encrypt or authenticate connections. If this port is exposed externally, an attacker can use this port to attack the entire Kubernetes cluster. By setting the bind address to localhost (i.e., 127.0.0.1), only those internal services that require health and metrics information can access the Scheduler API.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i bind-address * If the setting "bind-address" is not set to "127.0.0.1" or is not found in the Kubernetes Scheduler manifest file, this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-242385`

### Rule: The Kubernetes Controller Manager must have secure binding.

**Rule ID:** `SV-242385r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of attack vectors and implementing authentication and encryption on the endpoints available to external sources is paramount when securing the overall Kubernetes cluster. The Controller Manager API service exposes port 10252/TCP by default for health and metrics information use. This port does not encrypt or authenticate connections. If this port is exposed externally, an attacker can use this port to attack the entire Kubernetes cluster. By setting the bind address to only localhost (i.e., 127.0.0.1), only those internal services that require health and metrics information can access the Control Manager API.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i bind-address * If the setting bind-address is not set to "127.0.0.1" or is not found in the Kubernetes Controller Manager manifest file, this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-242386`

### Rule: The Kubernetes API server must have the insecure port flag disabled.

**Rule ID:** `SV-242386r927241_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, the API server will listen on two ports. One port is the secure port and the other port is called the "localhost port". This port is also called the "insecure port", port 8080. Any requests to this port bypass authentication and authorization checks. If this port is left open, anyone who gains access to the host on which the Control Plane is running can bypass all authorization and authentication mechanisms put in place, and have full control over the entire cluster. Close the insecure port by setting the API server's "--insecure-port" flag to "0", ensuring that the "--insecure-bind-address" is not set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i insecure-port * If the setting "--insecure-port" is not set to "0" or is not configured in the Kubernetes API server manifest file, this is a finding. Note: "--insecure-port" flag has been deprecated and can only be set to "0". **This flag will be removed in v1.24.*

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-242387`

### Rule: The Kubernetes Kubelet must have the "readOnlyPort" flag disabled.

**Rule ID:** `SV-242387r918149_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Kubelet serves a small REST API with read access to port 10255. The read-only port for Kubernetes provides no authentication or authorization security control. Providing unrestricted access on port 10255 exposes Kubernetes pods and containers to malicious attacks or compromise. Port 10255 is deprecated and should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On each Control Plane and Worker Node, run the command: ps -ef | grep kubelet If the "--read-only-port" option exists, this is a finding. Note the path to the config file (identified by --config). Run the command: grep -i readOnlyPort <path_to_config_file> If the setting "readOnlyPort" exists and is not set to "0", this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-242388`

### Rule: The Kubernetes API server must have the insecure bind address not set.

**Rule ID:** `SV-242388r927242_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, the API server will listen on two ports and addresses. One address is the secure address and the other address is called the "insecure bind" address and is set by default to localhost. Any requests to this address bypass authentication and authorization checks. If this insecure bind address is set to localhost, anyone who gains access to the host on which the Control Plane is running can bypass all authorization and authentication mechanisms put in place and have full control over the entire cluster. Close or set the insecure bind address by setting the API server's "--insecure-bind-address" flag to an IP or leave it unset and ensure that the "--insecure-bind-port" is not set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i insecure-bind-address * If the setting "--insecure-bind-address" is found and set to "localhost" in the Kubernetes API manifest file, this is a finding.

## Group: SRG-APP-000033-CTR-000100

**Group ID:** `V-242389`

### Rule: The Kubernetes API server must have the secure port set.

**Rule ID:** `SV-242389r927243_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the API server will listen on what is rightfully called the secure port, port 6443. Any requests to this port will perform authentication and authorization checks. If this port is disabled, anyone who gains access to the host on which the Control Plane is running has full control of the entire cluster over encrypted traffic. Open the secure port by setting the API server's "--secure-port" flag to a value other than "0".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i secure-port * If the setting "--secure-port" is set to "0" or is not configured in the Kubernetes API manifest file, this is a finding.

## Group: SRG-APP-000033-CTR-000100

**Group ID:** `V-242390`

### Rule: The Kubernetes API server must have anonymous authentication disabled.

**Rule ID:** `SV-242390r927244_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Kubernetes API Server controls Kubernetes via an API interface. A user who has access to the API essentially has root access to the entire Kubernetes cluster. To control access, users must be authenticated and authorized. By allowing anonymous connections, the controls put in place to secure the API can be bypassed. Setting "--anonymous-auth" to "false" also disables unauthenticated requests from kubelets. While there are instances where anonymous connections may be needed (e.g., health checks) and Role-Based Access Controls (RBACs) are in place to limit the anonymous access, this access should be disabled, and only enabled when necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i anonymous-auth * If the setting "--anonymous-auth" is set to "true" in the Kubernetes API Server manifest file, this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-242391`

### Rule: The Kubernetes Kubelet must have anonymous authentication disabled.

**Rule ID:** `SV-242391r918152_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A user who has access to the Kubelet essentially has root access to the nodes contained within the Kubernetes Control Plane. To control access, users must be authenticated and authorized. By allowing anonymous connections, the controls put in place to secure the Kubelet can be bypassed. Setting anonymous authentication to "false" also disables unauthenticated requests from kubelets. While there are instances where anonymous connections may be needed (e.g., health checks) and Role-Based Access Controls (RBAC) are in place to limit the anonymous access, this access must be disabled and only enabled when necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On each Control Plane and Worker Node, run the command: ps -ef | grep kubelet If the "--anonymous-auth" option exists, this is a finding. Note the path to the config file (identified by --config). Inspect the content of the config file: Locate the "anonymous" section under "authentication". In this section, if the field "enabled" does not exist or is set to "true", this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-242392`

### Rule: The Kubernetes kubelet must enable explicit authorization.

**Rule ID:** `SV-242392r918155_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Kubelet is the primary agent on each node. The API server communicates with each kubelet to perform tasks such as starting/stopping pods. By default, kubelets allow all authenticated requests, even anonymous ones, without requiring any authorization checks from the API server. This default behavior bypasses any authorization controls put in place to limit what users may perform within the Kubernetes cluster. To change this behavior, the default setting of AlwaysAllow for the authorization mode must be set to "Webhook".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On each Control Plane and Worker Node, run the command: ps -ef | grep kubelet If the "--authorization-mode" option exists, this is a finding. Note the path to the config file (identified by --config). Inspect the content of the config file: Locate the "authorization" section. If the field "mode" does not exist or is not set to "Webhook", this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-242393`

### Rule: Kubernetes Worker Nodes must not have sshd service running.

**Rule ID:** `SV-242393r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Worker Nodes are maintained and monitored by the Control Plane. Direct access and manipulation of the nodes should not take place by administrators. Worker nodes should be treated as immutable and updated via replacement rather than in-place upgrades.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to each worker node. Verify that the sshd service is not running. To validate that the service is not running, run the command: systemctl status sshd If the service sshd is active (running), this is a finding. Note: If console access is not available, SSH access can be attempted. If the worker nodes cannot be reached, this requirement is "not a finding".

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-242394`

### Rule: Kubernetes Worker Nodes must not have the sshd service enabled.

**Rule ID:** `SV-242394r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Worker Nodes are maintained and monitored by the Control Plane. Direct access and manipulation of the nodes must not take place by administrators. Worker nodes must be treated as immutable and updated via replacement rather than in-place upgrades.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to each worker node. Verify that the sshd service is not enabled. To validate the service is not enabled, run the command: systemctl is-enabled sshd.service If the service sshd is enabled, this is a finding. Note: If console access is not available, SSH access can be attempted. If the worker nodes cannot be reached, this requirement is "not a finding".

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-242395`

### Rule: Kubernetes dashboard must not be enabled.

**Rule ID:** `SV-242395r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While the Kubernetes dashboard is not inherently insecure on its own, it is often coupled with a misconfiguration of Role-Based Access control (RBAC) permissions that can unintentionally over-grant access. It is not commonly protected with "NetworkPolicies", preventing all pods from being able to reach it. In increasingly rare circumstances, the Kubernetes dashboard is exposed publicly to the internet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Control Plane, run the command: kubectl get pods --all-namespaces -l k8s-app=kubernetes-dashboard If any resources are returned, this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-242396`

### Rule: Kubernetes Kubectl cp command must give expected access and results.

**Rule ID:** `SV-242396r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One of the tools heavily used to interact with containers in the Kubernetes cluster is kubectl. The command is the tool System Administrators used to create, modify, and delete resources. One of the capabilities of the tool is to copy files to and from running containers (i.e., kubectl cp). The command uses the "tar" command of the container to copy files from the container to the host executing the "kubectl cp" command. If the "tar" command on the container has been replaced by a malicious user, the command can copy files anywhere on the host machine. This flaw has been fixed in later versions of the tool. It is recommended to use kubectl versions newer than 1.12.9.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Control Plane and each Worker node, check the version of kubectl by executing the command: kubectl version --client If the Control Plane or any Worker nodes are not using kubectl version 1.12.9 or newer, this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-242397`

### Rule: The Kubernetes kubelet staticPodPath must not enable static pods.

**Rule ID:** `SV-242397r927245_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing kubelet to set a staticPodPath gives containers with root access permissions to traverse the hosting filesystem. The danger comes when the container can create a manifest file within the /etc/kubernetes/manifests directory. When a manifest is created within this directory, containers are entirely governed by the Kubelet not the API Server. The container is not susceptible to admission control at all. Any containers or pods that are instantiated in this manner are called "static pods" and are meant to be used for pods such as the API server, scheduler, controller, etc., not workload pods that need to be governed by the API Server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that Kubernetes static PodPath is not enabled on each Control Plane and Worker node. On the Control Plane and Worker nodes, run the command: ps -ef | grep kubelet Note the path to the config file (identified by --config). Run the command: grep -i staticPodPath <path_to_config_file> If any of the Control Plane and Worker nodes return a value for "staticPodPath", this is a finding.

## Group: SRG-APP-000033-CTR-000100

**Group ID:** `V-242398`

### Rule: Kubernetes DynamicAuditing must not be enabled.

**Rule ID:** `SV-242398r918161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the audit data from change or deletion is important when an attack occurs. One way an attacker can cover their tracks is to change or delete audit records. This will either make the attack unnoticeable or make it more difficult to investigate how the attack took place and what changes were made. The audit data can be protected through audit log file protections and user authorization. One way for an attacker to thwart these measures is to send the audit logs to another source and filter the audited results before sending them on to the original target. This can be done in Kubernetes through the configuration of dynamic audit webhooks through the DynamicAuditing flag.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, change to the manifests' directory at /etc/kubernetes/manifests and run the command: grep -i feature-gates * Review the feature-gates setting, if one is returned. If the feature-gates setting is available and contains the DynamicAuditing flag set to "true", this is a finding. On each Control Plane and Worker node, run the command: ps -ef | grep kubelet If the "--feature-gates" option exists, this is a finding. Note the path to the config file (identified by: --config). Inspect the content of the config file: If the "featureGates" setting is present and has the "DynamicAuditing" flag set to "true", this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-242399`

### Rule: Kubernetes DynamicKubeletConfig must not be enabled.

**Rule ID:** `SV-242399r918164_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes allows a user to configure kubelets with dynamic configurations. When dynamic configuration is used, the kubelet will watch for changes to the configuration file. When changes are made, the kubelet will automatically restart. Allowing this capability bypasses access restrictions and authorizations. Using this capability, an attacker can lower the security posture of the kubelet, which includes allowing the ability to run arbitrary commands in any container running on that node.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is only applicable for Kubernetes versions 1.25 and older. On the Control Plane, change to the manifests' directory at /etc/kubernetes/manifests and run the command: grep -i feature-gates * In each manifest file, if the feature-gates does not exist, or does not contain the "DynamicKubeletConfig" flag, or sets the flag to "true", this is a finding. On each Control Plane and Worker node, run the command: ps -ef | grep kubelet Verify the "feature-gates" option is not present. Note the path to the config file (identified by --config). Inspect the content of the config file: If the "featureGates" setting is not present, or does not contain the "DynamicKubeletConfig", or sets the flag to "true", this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-242400`

### Rule: The Kubernetes API server must have Alpha APIs disabled.

**Rule ID:** `SV-242400r927246_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes allows alpha API calls within the API server. The alpha features are disabled by default since they are not ready for production and likely to change without notice. These features may also contain security issues that are rectified as the feature matures. To keep the Kubernetes cluster secure and stable, these alpha features must not be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, change to the manifests' directory at /etc/kubernetes/manifests and run the command: grep -i feature-gates * Review the "--feature-gates" setting, if one is returned. If the "--feature-gate"s setting is available and contains the "AllAlpha" flag set to "true", this is a finding.

## Group: SRG-APP-000092-CTR-000165

**Group ID:** `V-242402`

### Rule: The Kubernetes API Server must have an audit log path set.

**Rule ID:** `SV-242402r927248_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Kubernetes is started, components and user services are started for auditing startup events, and events for components and services, it is important that auditing begin on startup. Within Kubernetes, audit data for all components is generated by the API server. To enable auditing to begin, an audit policy must be defined for the events and the information to be stored with each event. It is also necessary to give a secure location where the audit logs are to be stored. If an audit log path is not specified, all audit data is sent to studio.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i audit-log-path * If the "--audit-log-path" is not set, this is a finding.

## Group: SRG-APP-000026-CTR-000070

**Group ID:** `V-242403`

### Rule: Kubernetes API Server must generate audit records that identify what type of event has occurred, identify the source of the event, contain the event results, identify any users, and identify any containers associated with the event.

**Rule ID:** `SV-242403r927249_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within Kubernetes, audit data for all components is generated by the API server. This audit data is important when there are issues, to include security incidents that must be investigated. To make the audit data worthwhile for the investigation of events, it is necessary to have the appropriate and required data logged. To fully understand the event, it is important to identify any users associated with the event. The API server policy file allows for the following levels of auditing: None - Do not log events that match the rule. Metadata - Log request metadata (requesting user, timestamp, resource, verb, etc.) but not request or response body. Request - Log event metadata and request body but not response body. RequestResponse - Log event metadata, request, and response bodies. Satisfies: SRGID:SRG-APP-000092-CTR-000165, SRG-APP-000026-CTR-000070, SRG-APP-000027-CTR-000075, SRG-APP-000028-CTR-000080, SRG-APP-000101-CTR-000205, SRG-APP-000100-CTR-000200, SRG-APP-000100-CTR-000195, SRG-APP-000099-CTR-000190, SRG-APP-000098-CTR-000185, SRG-APP-000095-CTR-000170, SRG-APP-000096-CTR-000175, SRG-APP-000097-CTR-000180, SRG-APP-000507-CTR-001295, SRG-APP-000504-CTR-001280, SRG-APP-000503-CTR-001275, SRG-APP-000501-CTR-001265, SRG-APP-000500-CTR-001260, SRG-APP-000497-CTR-001245, SRG-APP-000496-CTR-001240, SRG-APP-000493-CTR-001225, SRG-APP-000492-CTR-001220, SRG-APP-000343-CTR-000780, SRG-APP-000381-CTR-000905</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i audit-policy-file If the audit-policy-file is not set, this is a finding. The file given is the policy file and defines what is audited and what information is included with each event. The policy file must look like this: # Log all requests at the RequestResponse level. apiVersion: audit.k8s.io/vX (Where X is the latest apiVersion) kind: Policy rules: - level: RequestResponse If the audit policy file does not look like above, this is a finding.

## Group: SRG-APP-000133-CTR-000290

**Group ID:** `V-242404`

### Rule: Kubernetes Kubelet must deny hostname override.

**Rule ID:** `SV-242404r918167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes allows for the overriding of hostnames. Allowing this feature to be implemented within the kubelets may break the TLS setup between the kubelet service and the API server. This setting also can make it difficult to associate logs with nodes if security analytics needs to take place. The better practice is to setup nodes with resolvable FQDNs and avoid overriding the hostnames.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane and Worker nodes, run the command: ps -ef | grep kubelet If the option "--hostname-override" is present, this is a finding.

## Group: SRG-APP-000133-CTR-000295

**Group ID:** `V-242405`

### Rule: The Kubernetes manifests must be owned by root.

**Rule ID:** `SV-242405r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The manifest files contain the runtime configuration of the API server, proxy, scheduler, controller, and etcd. If an attacker can gain access to these files, changes can be made to open vulnerabilities and bypass user authorizations inherit within Kubernetes with RBAC implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, change to the /etc/kubernetes/manifest directory. Run the command: ls -l * Each manifest file must be owned by root:root. If any manifest file is not owned by root:root, this is a finding.

## Group: SRG-APP-000133-CTR-000300

**Group ID:** `V-242406`

### Rule: The Kubernetes KubeletConfiguration file must be owned by root.

**Rule ID:** `SV-242406r918168_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The kubelet configuration file contains the runtime configuration of the kubelet service. If an attacker can gain access to this file, changes can be made to open vulnerabilities and bypass user authorizations inherent within Kubernetes with RBAC implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Kubernetes Control Plane and Worker nodes, run the command: ps -ef | grep kubelet Check the config file (path identified by: --config): Change to the directory identified by --config (example /etc/sysconfig/) run the command: ls -l kubelet Each kubelet configuration file must be owned by root:root. If any manifest file is not owned by root:root, this is a finding.

## Group: SRG-APP-000133-CTR-000305

**Group ID:** `V-242407`

### Rule: The Kubernetes KubeletConfiguration files must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242407r918171_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The kubelet configuration file contains the runtime configuration of the kubelet service. If an attacker can gain access to this file, changes can be made to open vulnerabilities and bypass user authorizations inherit within Kubernetes with RBAC implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Kubernetes Control Plane and Worker nodes, run the command: ps -ef | grep kubelet Check the config file (path identified by: --config): Change to the directory identified by --config (example /etc/sysconfig/) and run the command: ls -l kubelet Each KubeletConfiguration file must have permissions of "644" or more restrictive. If any KubeletConfiguration file is less restrictive than "644", this is a finding.

## Group: SRG-APP-000133-CTR-000310

**Group ID:** `V-242408`

### Rule: The Kubernetes manifest files must have least privileges.

**Rule ID:** `SV-242408r918174_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The manifest files contain the runtime configuration of the API server, scheduler, controller, and etcd. If an attacker can gain access to these files, changes can be made to open vulnerabilities and bypass user authorizations inherent within Kubernetes with RBAC implemented. Satisfies: SRG-APP-000133-CTR-000310, SRG-APP-000133-CTR-000295, SRG-APP-000516-CTR-001335</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On both Control Plane and Worker Nodes, change to the /etc/kubernetes/manifest directory. Run the command: ls -l * Each manifest file must have permissions "644" or more restrictive. If any manifest file is less restrictive than "644", this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-242409`

### Rule: Kubernetes Controller Manager must disable profiling.

**Rule ID:** `SV-242409r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes profiling provides the ability to analyze and troubleshoot Controller Manager events over a web interface on a host port. Enabling this service can expose details about the Kubernetes architecture. This service must not be enabled unless deemed necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i profiling * If the setting "profiling" is not configured in the Kubernetes Controller Manager manifest file or it is set to "True", this is a finding.

## Group: SRG-APP-000142-CTR-000325

**Group ID:** `V-242410`

### Rule: The Kubernetes API Server must enforce ports, protocols, and services (PPS) that adhere to the Ports, Protocols, and Services Management Category Assurance List (PPSM CAL).

**Rule ID:** `SV-242410r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes API Server PPSs must be controlled and conform to the PPSM CAL. Those PPS that fall outside the PPSM CAL must be blocked. Instructions on the PPSM can be found in DoD Instruction 8551.01 Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep kube-apiserver.manifest -I -secure-port * grep kube-apiserver.manifest -I -etcd-servers * -edit manifest file: VIM <Manifest Name> Review livenessProbe: HttpGet: Port: Review ports: - containerPort: hostPort: - containerPort: hostPort: Run Command: kubectl describe services –all-namespace Search labels for any apiserver names spaces. Port: Any manifest and namespace PPS or services configuration not in compliance with PPSM CAL is a finding. Review the information systems documentation and interview the team, gain an understanding of the API Server architecture, and determine applicable PPS. If there are any ports, protocols, and services in the system documentation not in compliance with the CAL PPSM, this is a finding. Any PPS not set in the system documentation is a finding. Review findings against the most recent PPSM CAL: https://cyber.mil/ppsm/cal/ Verify API Server network boundary with the PPS associated with the CAL Assurance Categories. Any PPS not in compliance with the CAL Assurance Category requirements is a finding.

## Group: SRG-APP-000142-CTR-000325

**Group ID:** `V-242411`

### Rule: The Kubernetes Scheduler must enforce ports, protocols, and services (PPS) that adhere to the Ports, Protocols, and Services Management Category Assurance List (PPSM CAL).

**Rule ID:** `SV-242411r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes Scheduler PPS must be controlled and conform to the PPSM CAL. Those ports, protocols, and services that fall outside the PPSM CAL must be blocked. Instructions on the PPSM can be found in DoD Instruction 8551.01 Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep kube-scheduler.manifest -I -insecure-port grep kube-scheduler.manifest -I -secure-port -edit manifest file: VIM <Manifest Name> Review livenessProbe: HttpGet: Port: Review ports: - containerPort: hostPort: - containerPort: hostPort: Run Command: kubectl describe services –all-namespace Search labels for any scheduler names spaces. Port: Any manifest and namespace PPS configuration not in compliance with PPSM CAL is a finding. Review the information systems documentation and interview the team, gain an understanding of the Scheduler architecture, and determine applicable PPS. Any PPS in the system documentation not in compliance with the CAL PPSM is a finding. Any PPSs not set in the system documentation is a finding. Review findings against the most recent PPSM CAL: https://cyber.mil/ppsm/cal/ Verify Scheduler network boundary with the PPS associated with the CAL Assurance Categories. Any PPS not in compliance with the CAL Assurance Category requirements is a finding.

## Group: SRG-APP-000142-CTR-000330

**Group ID:** `V-242412`

### Rule: The Kubernetes Controllers must enforce ports, protocols, and services (PPS) that adhere to the Ports, Protocols, and Services Management Category Assurance List (PPSM CAL).

**Rule ID:** `SV-242412r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes Controller ports, protocols, and services must be controlled and conform to the PPSM CAL. Those PPS that fall outside the PPSM CAL must be blocked. Instructions on the PPSM can be found in DoD Instruction 8551.01 Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep kube-scheduler.manifest -I -secure-port -edit manifest file: VIM <Manifest Name: Review livenessProbe: HttpGet: Port: Review ports: - containerPort: hostPort: - containerPort: hostPort: Run Command: kubectl describe services –all-namespace Search labels for any controller names spaces. Any manifest and namespace PPS or services configuration not in compliance with PPSM CAL is a finding. Review the information systems documentation and interview the team, gain an understanding of the Controller architecture, and determine applicable PPS. Any PPS in the system documentation not in compliance with the CAL PPSM is a finding. Any PPS not set in the system documentation is a finding. Review findings against the most recent PPSM CAL: https://cyber.mil/ppsm/cal/ Verify Controller network boundary with the PPS associated with the Controller for Assurance Categories. Any PPS not in compliance with the CAL Assurance Category requirements is a finding.

## Group: SRG-APP-000142-CTR-000325

**Group ID:** `V-242413`

### Rule: The Kubernetes etcd must enforce ports, protocols, and services (PPS) that adhere to the Ports, Protocols, and Services Management Category Assurance List (PPSM CAL).

**Rule ID:** `SV-242413r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes etcd PPS must be controlled and conform to the PPSM CAL. Those PPS that fall outside the PPSM CAL must be blocked. Instructions on the PPSM can be found in DoD Instruction 8551.01 Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep kube-apiserver.manifest -I -etcd-servers * -edit etcd-main.manifest file: VIM <Manifest Name: Review livenessProbe: HttpGet: Port: Review ports: - containerPort: hostPort: - containerPort: hostPort: Run Command: kubectl describe services –all-namespace Search labels for any apiserver names spaces. Port: Any manifest and namespace PPS configuration not in compliance with PPSM CAL is a finding. Review the information systems documentation and interview the team, gain an understanding of the etcd architecture, and determine applicable PPS. Any PPS in the system documentation not in compliance with the CAL PPSM is a finding. Any PPS not set in the system documentation is a finding. Review findings against the most recent PPSM CAL: https://cyber.mil/ppsm/cal/ Verify etcd network boundary with the PPS associated with the CAL Assurance Categories. Any PPS not in compliance with the CAL Assurance Category requirements is a finding.

## Group: SRG-APP-000142-CTR-000330

**Group ID:** `V-242414`

### Rule: The Kubernetes cluster must use non-privileged host ports for user pods.

**Rule ID:** `SV-242414r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged ports are those ports below 1024 and that require system privileges for their use. If containers can use these ports, the container must be run as a privileged user. Kubernetes must stop containers that try to map to these ports directly. Allowing non-privileged ports to be mapped to the container-privileged port is the allowable method when a certain port is needed. An example is mapping port 8080 externally to port 80 in the container.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: kubectl get pods --all-namespaces The list returned is all pods running within the Kubernetes cluster. For those pods running within the user namespaces (System namespaces are kube-system, kube-node-lease and kube-public), run the command: kubectl get pod podname -o yaml | grep -i port Note: In the above command, "podname" is the name of the pod. For the command to work correctly, the current context must be changed to the namespace for the pod. The command to do this is: kubectl config set-context --current --namespace=namespace-name (Note: "namespace-name" is the name of the namespace.) Review the ports that are returned for the pod. If any host-privileged ports are returned for any of the pods, this is a finding.

## Group: SRG-APP-000171-CTR-000435

**Group ID:** `V-242415`

### Rule: Secrets in Kubernetes must not be stored as environment variables.

**Rule ID:** `SV-242415r879608_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Secrets, such as passwords, keys, tokens, and certificates should not be stored as environment variables. These environment variables are accessible inside Kubernetes by the "Get Pod" API call, and by any system, such as CI/CD pipeline, which has access to the definition file of the container. Secrets must be mounted from files or stored within password vaults.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Kubernetes Control Plane, run the following command: kubectl get all -o jsonpath='{range .items[?(@..secretKeyRef)]} {.kind} {.metadata.name} {"\n"}{end}' -A If any of the values returned reference environment variables, this is a finding.

## Group: SRG-APP-000211-CTR-000530

**Group ID:** `V-242417`

### Rule: Kubernetes must separate user functionality.

**Rule ID:** `SV-242417r879631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Separating user functionality from management functionality is a requirement for all the components within the Kubernetes Control Plane. Without the separation, users may have access to management functions that can degrade the Kubernetes architecture and the services being offered, and can offer a method to bypass testing and validation of functions before introduced into a production environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: kubectl get pods --all-namespaces Review the namespaces and pods that are returned. Kubernetes system namespaces are kube-node-lease, kube-public, and kube-system. If any user pods are present in the Kubernetes system namespaces, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242418`

### Rule: The Kubernetes API server must use approved cipher suites.

**Rule ID:** `SV-242418r927250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes API server communicates to the kubelet service on the nodes to deploy, update, and delete resources. If an attacker were able to get between this communication and modify the request, the Kubernetes cluster could be compromised. Using approved cypher suites for the communication ensures the protection of the transmitted information, confidentiality, and integrity so that the attacker cannot read or alter this communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i tls-cipher-suites * If the setting feature tls-cipher-suites is not set in the Kubernetes API server manifest file or contains no value or does not contain TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242419`

### Rule: Kubernetes API Server must have the SSL Certificate Authority set.

**Rule ID:** `SV-242419r918176_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes control plane and external communication are managed by API Server. The main implementation of the API Server is to manage hardware resources for pods and containers using horizontal or vertical scaling. Anyone who can access the API Server can effectively control the Kubernetes architecture. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols such as TLS. TLS provides the Kubernetes API Server with a means to authenticate sessions and encrypt traffic. To enable encrypted communication for API Server, the parameter client-ca-file must be set. This parameter gives the location of the SSL Certificate Authority file used to secure API Server communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i client-ca-file * If the setting feature client-ca-file is not set in the Kubernetes API server manifest file or contains no value, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242420`

### Rule: Kubernetes Kubelet must have the SSL Certificate Authority set.

**Rule ID:** `SV-242420r918179_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes container and pod configuration are maintained by Kubelet. Kubelet agents register nodes with the API Server, mount volume storage, and perform health checks for containers and pods. Anyone who gains access to Kubelet agents can effectively control applications within the pods and containers. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols such as TLS. TLS provides the Kubernetes API Server with a means to authenticate sessions and encrypt traffic. To enable encrypted communication for Kubelet, the clientCAFile must be set. This parameter gives the location of the SSL Certificate Authority file used to secure Kubelet communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: ps -ef | grep kubelet If the "--client-ca-file" option exists, this is a finding. Note the path to the config file (identified by --config). Run the command: grep -i clientCAFile <path_to_config_file> If the setting "clientCAFile" is not set or contains no value, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242421`

### Rule: Kubernetes Controller Manager must have the SSL Certificate Authority set.

**Rule ID:** `SV-242421r927251_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes Controller Manager is responsible for creating service accounts and tokens for the API Server, maintaining the correct number of pods for every replication controller and provides notifications when nodes are offline. Anyone who gains access to the Controller Manager can generate backdoor accounts, take possession of, or diminish system performance without detection by disabling system notification. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes Controller Manager with a means to be able to authenticate sessions and encrypt traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i root-ca-file * If the setting "--root-ca-file" is not set in the Kubernetes Controller Manager manifest file or contains no value, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242422`

### Rule: Kubernetes API Server must have a certificate for communication.

**Rule ID:** `SV-242422r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes control plane and external communication is managed by API Server. The main implementation of the API Server is to manage hardware resources for pods and container using horizontal or vertical scaling. Anyone who can access the API Server can effectively control the Kubernetes architecture. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for API Server, the parameter etcd-cafile must be set. This parameter gives the location of the SSL Certificate Authority file used to secure API Server communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i tls-cert-file * grep -i tls-private-key-file * If the setting tls-cert-file and private-key-file is not set in the Kubernetes API server manifest file or contains no value, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242423`

### Rule: Kubernetes etcd must enable client authentication to secure service.

**Rule ID:** `SV-242423r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes container and pod configuration are maintained by Kubelet. Kubelet agents register nodes with the API Server, mount volume storage, and perform health checks for containers and pods. Anyone who gains access to Kubelet agents can effectively control applications within the pods and containers. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for Kubelet, the parameter client-cert-auth must be set. This parameter gives the location of the SSL Certificate Authority file used to secure Kubelet communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i client-cert-auth * If the setting client-cert-auth is not configured in the Kubernetes etcd manifest file or set to "false", this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242424`

### Rule: Kubernetes Kubelet must enable tlsPrivateKeyFile for client authentication to secure service.

**Rule ID:** `SV-242424r918182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes container and pod configuration are maintained by Kubelet. Kubelet agents register nodes with the API Server, mount volume storage, and perform health checks for containers and pods. Anyone who gains access to Kubelet agents can effectively control applications within the pods and containers. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols such as TLS. TLS provides the Kubernetes API Server with a means to authenticate sessions and encrypt traffic. To enable encrypted communication for Kubelet, the tlsPrivateKeyFile must be set. This parameter gives the location of the SSL Certificate Authority file used to secure Kubelet communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: ps -ef | grep kubelet If the "--tls-private-key-file" option exists, this is a finding. Note the path to the config file (identified by --config). Run the command: grep -i tlsPrivateKeyFile <path_to_config_file> If the setting "tlsPrivateKeyFile" is not set or contains no value, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242425`

### Rule: Kubernetes Kubelet must enable tlsCertFile for client authentication to secure service.

**Rule ID:** `SV-242425r918185_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes container and pod configuration are maintained by Kubelet. Kubelet agents register nodes with the API Server, mount volume storage, and perform health checks for containers and pods. Anyone who gains access to Kubelet agents can effectively control applications within the pods and containers. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols such as TLS. TLS provides the Kubernetes API Server with a means to authenticate sessions and encrypt traffic. To enable encrypted communication for Kubelet, the parameter tlsCertFile must be set. This parameter gives the location of the SSL Certificate Authority file used to secure Kubelet communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: ps -ef | grep kubelet If the argument for "--tls-cert-file" option exists, this is a finding. Note the path to the config file (identified by --config). Run the command: grep -i tlsCertFile <path_to_config_file> If the setting "tlsCertFile" is not set or contains no value, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242426`

### Rule: Kubernetes etcd must enable client authentication to secure service.

**Rule ID:** `SV-242426r927252_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes container and pod configuration are maintained by Kubelet. Kubelet agents register nodes with the API Server, mount volume storage, and perform health checks for containers and pods. Anyone who gains access to Kubelet agents can effectively control applications within the pods and containers. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server with a means to be able to authenticate sessions and encrypt traffic. Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive and should be accessible only by authenticated etcd peers in the etcd cluster. The parameter "--peer-client-cert-auth" must be set for etcd to check all incoming peer requests from the cluster for valid client certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i peer-client-cert-auth * If the setting "--peer-client-cert-auth" is not configured in the Kubernetes etcd manifest file or set to "false", this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242427`

### Rule: Kubernetes etcd must have a key file for secure communication.

**Rule ID:** `SV-242427r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes stores configuration and state information in a distributed key-value store called etcd. Anyone who can write to etcd can effectively control the Kubernetes cluster. Even just reading the contents of etcd could easily provide helpful hints to a would-be attacker. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server and etcd with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for etcd, the parameter key-file must be set. This parameter gives the location of the key file used to secure etcd communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i key-file * If the setting "key-file" is not configured in the etcd manifest file, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242428`

### Rule: Kubernetes etcd must have a certificate for communication.

**Rule ID:** `SV-242428r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes stores configuration and state information in a distributed key-value store called etcd. Anyone who can write to etcd can effectively control a Kubernetes cluster. Even just reading the contents of etcd could easily provide helpful hints to a would-be attacker. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server and etcd with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for etcd, the parameter cert-file must be set. This parameter gives the location of the SSL certification file used to secure etcd communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i cert-file * If the setting "cert-file" is not configured in the Kubernetes etcd manifest file, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242429`

### Rule: Kubernetes etcd must have the SSL Certificate Authority set.

**Rule ID:** `SV-242429r927253_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes stores configuration and state information in a distributed key-value store called etcd. Anyone who can write to etcd can effectively control a Kubernetes cluster. Even just reading the contents of etcd could easily provide helpful hints to a would-be attacker. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server and etcd with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for etcd, the parameter "--etcd-cafile" must be set. This parameter gives the location of the SSL Certificate Authority file used to secure etcd communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i etcd-cafile * If the setting "--etcd-cafile" is not configured in the Kubernetes API Server manifest file, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242430`

### Rule: Kubernetes etcd must have a certificate for communication.

**Rule ID:** `SV-242430r927254_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes stores configuration and state information in a distributed key-value store called etcd. Anyone who can write to etcd can effectively control the Kubernetes cluster. Even just reading the contents of etcd could easily provide helpful hints to a would-be attacker. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server and etcd with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for etcd, the parameter "--etcd-certfile" must be set. This parameter gives the location of the SSL certification file used to secure etcd communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i etcd-certfile * If the setting "--etcd-certfile" is not set in the Kubernetes API Server manifest file, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242431`

### Rule: Kubernetes etcd must have a key file for secure communication.

**Rule ID:** `SV-242431r927255_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes stores configuration and state information in a distributed key-value store called etcd. Anyone who can write to etcd can effectively control a Kubernetes cluster. Even just reading the contents of etcd could easily provide helpful hints to a would-be attacker. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server and etcd with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for etcd, the parameter "--etcd-keyfile" must be set. This parameter gives the location of the key file used to secure etcd communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i etcd-keyfile * If the setting "--etcd-keyfile" is not configured in the Kubernetes API Server manifest file, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242432`

### Rule: Kubernetes etcd must have peer-cert-file set for secure communication.

**Rule ID:** `SV-242432r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes stores configuration and state information in a distributed key-value store called etcd. Anyone who can write to etcd can effectively control the Kubernetes cluster. Even just reading the contents of etcd could easily provide helpful hints to a would-be attacker. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server and etcd with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for etcd, the parameter peer-cert-file must be set. This parameter gives the location of the SSL certification file used to secure etcd communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i peer-cert-file * If the setting "peer-cert-file" is not configured in the Kubernetes etcd manifest file, this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-242433`

### Rule: Kubernetes etcd must have a peer-key-file set for secure communication.

**Rule ID:** `SV-242433r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes stores configuration and state information in a distributed key-value store called etcd. Anyone who can write to etcd can effectively control a Kubernetes cluster. Even just reading the contents of etcd could easily provide helpful hints to a would-be attacker. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server and etcd with a means to be able to authenticate sessions and encrypt traffic. To enable encrypted communication for etcd, the parameter peer-key-file must be set. This parameter gives the location of the SSL certification file used to secure etcd communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i peer-key-file * If the setting "peer-key-file" is not set in the Kubernetes etcd manifest file, this is a finding.

## Group: SRG-APP-000233-CTR-000585

**Group ID:** `V-242434`

### Rule: Kubernetes Kubelet must enable kernel protection.

**Rule ID:** `SV-242434r918188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>System kernel is responsible for memory, disk, and task management. The kernel provides a gateway between the system hardware and software. Kubernetes requires kernel access to allocate resources to the Control Plane. Threat actors that penetrate the system kernel can inject malicious code or hijack the Kubernetes architecture. It is vital to implement protections through Kubernetes components to reduce the attack surface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: ps -ef | grep kubelet If the "--protect-kernel-defaults" option exists, this is a finding. Note the path to the config file (identified by --config). Run the command: grep -i protectKernelDefaults <path_to_config_file> If the setting "protectKernelDefaults" is not set or is set to false, this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-242436`

### Rule: The Kubernetes API server must have the ValidatingAdmissionWebhook enabled.

**Rule ID:** `SV-242436r879719_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enabling the admissions webhook allows for Kubernetes to apply policies against objects that are to be created, read, updated, or deleted. By applying a pod security policy, control can be given to not allow images to be instantiated that run as the root user. If pods run as the root user, the pod then has root privileges to the host system and all the resources it has. An attacker can use this to attack the Kubernetes cluster. By implementing a policy that does not allow root or privileged pods, the pod users are limited in what the pod can do and access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Prior to version 1.21, to enforce security policiesPod Security Policies (psp) were used. Those are now deprecated and will be removed from version 1.25. Migrate from PSP to PSA: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/ Pre-version 1.25 Check: Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i ValidatingAdmissionWebhook * If a line is not returned that includes enable-admission-plugins and ValidatingAdmissionWebhook, this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-242437`

### Rule: Kubernetes must have a pod security policy set.

**Rule ID:** `SV-242437r879719_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enabling the admissions webhook allows for Kubernetes to apply policies against objects that are to be created, read, updated, or deleted. By applying a pod security policy, control can be given to not allow images to be instantiated that run as the root user. If pods run as the root user, the pod then has root privileges to the host system and all the resources it has. An attacker can use this to attack the Kubernetes cluster. By implementing a policy that does not allow root or privileged pods, the pod users are limited in what the pod can do and access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Prior to version 1.21, to enforce security policiesPod Security Policies (psp) were used. Those are now deprecated and will be removed from version 1.25. Migrate from PSP to PSA: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/ Pre-version 1.25 Check: On the Control Plane, run the command: kubectl get podsecuritypolicy If there is no pod security policy configured, this is a finding. For any pod security policies listed, edit the policy with the command: kubectl edit podsecuritypolicy policyname (Note: "policyname" is the name of the policy.) Review the runAsUser, supplementalGroups and fsGroup sections of the policy. If any of these sections are missing, this is a finding. If the rule within the runAsUser section is not set to "MustRunAsNonRoot", this is a finding. If the ranges within the supplementalGroups section has min set to "0" or min is missing, this is a finding. If the ranges within the fsGroup section has a min set to "0" or the min is missing, this is a finding.

## Group: SRG-APP-000435-CTR-001070

**Group ID:** `V-242438`

### Rule: Kubernetes API Server must configure timeouts to limit attack surface.

**Rule ID:** `SV-242438r927258_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes API Server request timeouts sets the duration a request stays open before timing out. Since the API Server is the central component in the Kubernetes Control Plane, it is vital to protect this service. If request timeouts were not set, malicious attacks or unwanted activities might affect multiple deployments across different applications or environments. This might deplete all resources from the Kubernetes infrastructure causing the information system to go offline. The "--request-timeout" value must never be set to "0". This disables the request-timeout feature. (By default, the "--request-timeout" is set to "1 minute".)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -I request-timeout * If Kubernetes API Server manifest file does not exist, this is a finding. If the setting "--request-timeout" is set to "0" in the Kubernetes API Server manifest file, or is not configured this is a finding.

## Group: SRG-APP-000454-CTR-001110

**Group ID:** `V-242442`

### Rule: Kubernetes must remove old components after updated versions have been installed.

**Rule ID:** `SV-242442r879825_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of Kubernetes components that are not removed after updates have been installed may be exploited by adversaries by allowing the vulnerabilities to still exist within the cluster. It is important for Kubernetes to remove old pods when newer pods are created using new images to always be at the desired security state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view all pods and the images used to create the pods, from the Control Plane, run the following command: kubectl get pods --all-namespaces -o jsonpath="{..image}" | \ tr -s '[[:space:]]' '\n' | \ sort | \ uniq -c Review the images used for pods running within Kubernetes. If there are multiple versions of the same image, this is a finding.

## Group: SRG-APP-000456-CTR-001125

**Group ID:** `V-242443`

### Rule: Kubernetes must contain the latest updates as authorized by IAVMs, CTOs, DTMs, and STIGs.

**Rule ID:** `SV-242443r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes software must stay up to date with the latest patches, service packs, and hot fixes. Not updating the Kubernetes control plane will expose the organization to vulnerabilities. Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant container platform components may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the IAVM process. The container platform components will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The container platform registry will ensure the images are current. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Authenticate on the Kubernetes Control Plane. Run the command: kubectl version --short If kubectl version has a setting not supporting Kubernetes skew policy, this is a finding. Note: Kubernetes Skew Policy can be found at: https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242444`

### Rule: The Kubernetes component manifests must be owned by root.

**Rule ID:** `SV-242444r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes manifests are those files that contain the arguments and settings for the Control Plane services. These services are etcd, the api server, controller, proxy, and scheduler. If these files can be changed, the scheduler will be implementing the changes immediately. Many of the security settings within the document are implemented through these manifests.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ownership of the Kubernetes manifests files by using the command: stat -c %U:%G /etc/kubernetes/manifests/* | grep -v root:root If the command returns any non root:root file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242445`

### Rule: The Kubernetes component etcd must be owned by etcd.

**Rule ID:** `SV-242445r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes etcd key-value store provides a way to store data to the Control Plane. If these files can be changed, data to API object and the Control Plane would be compromised. The scheduler will implement the changes immediately. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ownership of the Kubernetes etcd files by using the command: stat -c %U:%G /var/lib/etcd/* | grep -v etcd:etcd If the command returns any non etcd:etcd file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242446`

### Rule: The Kubernetes conf files must be owned by root.

**Rule ID:** `SV-242446r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes conf files contain the arguments and settings for the Control Plane services. These services are controller and scheduler. If these files can be changed, the scheduler will be implementing the changes immediately. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Kubernetes conf files by using the command: stat -c %U:%G /etc/kubernetes/admin.conf | grep -v root:root stat -c %U:%G /etc/kubernetes/scheduler.conf | grep -v root:root stat -c %U:%G /etc/kubernetes/controller-manager.conf | grep -v root:root If the command returns any non root:root file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242447`

### Rule: The Kubernetes Kube Proxy kubeconfig must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242447r927260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes Kube Proxy kubeconfig contain the argument and setting for the Control Planes. These settings contain network rules for restricting network communication between pods, clusters, and networks. If these files can be changed, data traversing between the Kubernetes Control Panel components would be compromised. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if Kube-Proxy is running and obtain --kubeconfig parameter use the following command: ps -ef | grep kube-proxy If Kube-Proxy exists: Review the permissions of the Kubernetes Kube Proxy by using the command: stat -c %a <location from --kubeconfig> If the file has permissions more permissive than "644", this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242448`

### Rule: The Kubernetes Kube Proxy kubeconfig must be owned by root.

**Rule ID:** `SV-242448r927261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes Kube Proxy kubeconfig contain the argument and setting for the Control Planes. These settings contain network rules for restricting network communication between pods, clusters, and networks. If these files can be changed, data traversing between the Kubernetes Control Panel components would be compromised. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if Kube-Proxy is running use the following command: ps -ef | grep kube-proxy If Kube-Proxy exists: Review the permissions of the Kubernetes Kube Proxy by using the command: stat -c %U:%G <location from --kubeconfig>| grep -v root:root If the command returns any non root:root file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242449`

### Rule: The Kubernetes Kubelet certificate authority file must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242449r919324_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes kubelet certificate authority file contains settings for the Kubernetes Node TLS certificate authority. Any request presenting a client certificate signed by one of the authorities in the client-ca-file is authenticated with an identity corresponding to the CommonName of the client certificate. If this file can be changed, the Kubernetes architecture could be compromised. The scheduler will implement the changes immediately. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: ps -ef | grep kubelet If the "--client-ca-file" option exists, this is a finding. Note the path to the config file (identified by --config). Run the command: grep -i clientCAFile <path_to_config_file> Note the path to the client ca file. Run the command: stat -c %a <path_to_client_ca_file> If the client ca file has permissions more permissive than "644", this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242450`

### Rule: The Kubernetes Kubelet certificate authority must be owned by root.

**Rule ID:** `SV-242450r918196_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes kube proxy kubeconfig contain the argument and setting for the Control Planes. These settings contain network rules for restricting network communication between pods, clusters, and networks. If these files can be changed, data traversing between the Kubernetes Control Panel components would be compromised. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: ps -ef | grep kubelet If the "client-ca-file" option exists, this is a finding. Note the path to the config file (identified by --config). Run the command: grep -i clientCAFile <path_to_config_file> Note the path to the client ca file. Run the command: stat -c %U:%G <path_to_client_ca_file> If the command returns any non root:root file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242451`

### Rule: The Kubernetes component PKI must be owned by root.

**Rule ID:** `SV-242451r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes PKI directory contains all certificates (.crt files) supporting secure network communications in the Kubernetes Control Plane. If these files can be modified, data traversing within the architecture components would become unsecure and compromised. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PKI files in Kubernetes by using the command: ls -laR /etc/kubernetes/pki/ If the command returns any non root:root file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242452`

### Rule: The Kubernetes kubelet KubeConfig must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242452r918197_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes kubelet agent registers nodes with the API Server, mounts volume storage for pods, and performs health checks to containers within pods. If these files can be modified, the information system would be unaware of pod or container degradation. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions of the Kubernetes Kubelet conf by using the command: stat -c %a /etc/kubernetes/kubelet.conf If any of the files are have permissions more permissive than "644", this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242453`

### Rule: The Kubernetes kubelet KubeConfig file must be owned by root.

**Rule ID:** `SV-242453r918204_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes kubelet agent registers nodes with the API server and performs health checks to containers within pods. If these files can be modified, the information system would be unaware of pod or container degradation. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Kubernetes Kubelet conf files by using the command: stat -c %U:%G /etc/kubernetes/kubelet.conf| grep -v root:root If the command returns any non root:root file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242454`

### Rule: The Kubernetes kubeadm.conf must be owned by root.

**Rule ID:** `SV-242454r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes kubeeadm.conf contains sensitive information regarding the cluster nodes configuration. If this file can be modified, the Kubernetes Platform Plane would be degraded or compromised for malicious intent. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Kubeadm.conf file : Get the path for Kubeadm.conf by running: sytstemctl status kubelet Note the configuration file installed by the kubeadm is written to (Default Location: /etc/systemd/system/kubelet.service.d/10-kubeadm.conf) stat -c %U:%G <kubeadm.conf path> | grep -v root:root If the command returns any non root:root file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001325

**Group ID:** `V-242455`

### Rule: The Kubernetes kubeadm.conf must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242455r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes kubeadm.conf contains sensitive information regarding the cluster nodes configuration. If this file can be modified, the Kubernetes Platform Plane would be degraded or compromised for malicious intent. Many of the security settings within the document are implemented through this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the kubeadm.conf file : Get the path for kubeadm.conf by running: systemctl status kubelet Note the configuration file installed by the kubeadm is written to (Default Location: /etc/systemd/system/kubelet.service.d/10-kubeadm.conf) stat -c %a <kubeadm.conf path> If the file has permissions more permissive than "644", this is a finding.

## Group: SRG-APP-000516-CTR-001330

**Group ID:** `V-242456`

### Rule: The Kubernetes kubelet config must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242456r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes kubelet agent registers nodes with the API server and performs health checks to containers within pods. If this file can be modified, the information system would be unaware of pod or container degradation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions of the Kubernetes config.yaml by using the command: stat -c %a /var/lib/kubelet/config.yaml If any of the files are have permissions more permissive than "644", this is a finding.

## Group: SRG-APP-000516-CTR-001330

**Group ID:** `V-242457`

### Rule: The Kubernetes kubelet config must be owned by root.

**Rule ID:** `SV-242457r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes kubelet agent registers nodes with the API Server and performs health checks to containers within pods. If this file can be modified, the information system would be unaware of pod or container degradation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Kubernetes Kubeadm kubelet conf file by using the command: stat -c %U:%G /var/lib/kubelet/config.yaml| grep -v root:root If the command returns any non root:root file permissions, this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242459`

### Rule: The Kubernetes etcd must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242459r918200_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes etcd key-value store provides a way to store data to the Control Plane. If these files can be changed, data to API object and Control Plane would be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions of the Kubernetes etcd by using the command: ls -AR /var/lib/etcd/* If any of the files have permissions more permissive than "644", this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242460`

### Rule: The Kubernetes admin kubeconfig must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242460r927262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes admin kubeconfig files contain the arguments and settings for the Control Plane services. These services are controller and scheduler. If these files can be changed, the scheduler will be implementing the changes immediately.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions of the Kubernetes config files by using the command: stat -c %a /etc/kubernetes/admin.conf stat -c %a /etc/kubernetes/scheduler.conf stat -c %a /etc/kubernetes/controller-manager.conf If any of the files are have permissions more permissive than "644", this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242461`

### Rule: Kubernetes API Server audit logs must be enabled.

**Rule ID:** `SV-242461r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes API Server validates and configures pods and services for the API object. The REST operation provides frontend functionality to the cluster share state. Enabling audit logs provides a way to monitor and identify security risk events or misuse of information. Audit logs are necessary to provide evidence in the case the Kubernetes API Server is compromised requiring a Cyber Security Investigation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: grep -i audit-policy-file * If the setting "audit-policy-file" is not set or is found in the Kubernetes API manifest file without valid content, this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242462`

### Rule: The Kubernetes API Server must be set to audit log max size.

**Rule ID:** `SV-242462r927263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes API Server must be set for enough storage to retain log information over the period required. When audit logs are large in size, the monitoring service for events becomes degraded. The function of the maximum log file size is to set these limits.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i audit-log-maxsize * If the setting "--audit-log-maxsize" is not set in the Kubernetes API Server manifest file or it is set to less than "100", this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242463`

### Rule: The Kubernetes API Server must be set to audit log maximum backup.

**Rule ID:** `SV-242463r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes API Server must set enough storage to retain logs for monitoring suspicious activity and system misconfiguration, and provide evidence for Cyber Security Investigations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i audit-log-maxbackup * If the setting "audit-log-maxbackup" is not set in the Kubernetes API Server manifest file or it is set less than "10", this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242464`

### Rule: The Kubernetes API Server audit log retention must be set.

**Rule ID:** `SV-242464r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes API Server must set enough storage to retain logs for monitoring suspicious activity and system misconfiguration, and provide evidence for Cyber Security Investigations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i audit-log-maxage * If the setting "audit-log-maxage" is not set in the Kubernetes API Server manifest file or it is set less than "30", this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242465`

### Rule: The Kubernetes API Server audit log path must be set.

**Rule ID:** `SV-242465r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kubernetes API Server validates and configures pods and services for the API object. The REST operation provides frontend functionality to the cluster share state. Audit logs are necessary to provide evidence in the case the Kubernetes API Server is compromised requiring Cyber Security Investigation. To record events in the audit log the log path value must be set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i audit-log-path * If the setting audit-log-path is not set in the Kubernetes API Server manifest file or it is not set to a valid path, this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242466`

### Rule: The Kubernetes PKI CRT must have file permissions set to 644 or more restrictive.

**Rule ID:** `SV-242466r927264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes PKI directory contains all certificates (.crt files) supporting secure network communications in the Kubernetes Control Plane. If these files can be modified, data traversing within the architecture components would become unsecure and compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions of the Kubernetes PKI cert files by using the command: sudo find /etc/kubernetes/pki/* -name "*.crt" | xargs stat -c '%n %a' If any of the files have permissions more permissive than "644", this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-242467`

### Rule: The Kubernetes PKI keys must have file permissions set to 600 or more restrictive.

**Rule ID:** `SV-242467r918207_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes PKI directory contains all certificate key files supporting secure network communications in the Kubernetes Control Plane. If these files can be modified, data traversing within the architecture components would become unsecure and compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions of the Kubernetes PKI key files by using the command: sudo find /etc/kubernetes/pki -name "*.key" | xargs stat -c '%n %a' If any of the files have permissions more permissive than "600", this is a finding.

## Group: SRG-APP-000190-CTR-000500

**Group ID:** `V-245541`

### Rule: Kubernetes Kubelet must not disable timeouts.

**Rule ID:** `SV-245541r918210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Idle connections from the Kubelet can be used by unauthorized users to perform malicious activity to the nodes, pods, containers, and cluster within the Kubernetes Control Plane. Setting the streamingConnectionIdleTimeout defines the maximum time an idle session is permitted prior to disconnect. Setting the value to "0" never disconnects any idle sessions. Idle timeouts must never be set to "0" and should be defined at "5m" (the default is 4hr).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, run the command: ps -ef | grep kubelet If the "--streaming-connection-idle-timeout" option exists, this is a finding. Note the path to the config file (identified by --config). Run the command: grep -i streamingConnectionIdleTimeout <path_to_config_file> If the setting "streamingConnectionIdleTimeout" is set to less than "5m" or is not configured, this is a finding.

## Group: SRG-APP-000439-CTR-001080

**Group ID:** `V-245542`

### Rule: Kubernetes API Server must disable basic authentication to protect information in transit.

**Rule ID:** `SV-245542r918141_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Kubernetes basic authentication sends and receives request containing username, uid, groups, and other fields over a clear text HTTP communication. Basic authentication does not provide any security mechanisms using encryption standards. PKI certificate-based authentication must be set over a secure channel to ensure confidentiality and integrity. Basic authentication must not be set in the manifest file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i basic-auth-file * If "basic-auth-file" is set in the Kubernetes API server manifest file this is a finding.

## Group: SRG-APP-000439-CTR-001080

**Group ID:** `V-245543`

### Rule: Kubernetes API Server must disable token authentication to protect information in transit.

**Rule ID:** `SV-245543r927259_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Kubernetes token authentication uses password known as secrets in a plaintext file. This file contains sensitive information such as token, username and user uid. This token is used by service accounts within pods to authenticate with the API Server. This information is very valuable for attackers with malicious intent if the service account is privileged having access to the token. With this token a threat actor can impersonate the service account gaining access to the Rest API service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i token-auth-file * If "--token-auth-file" is set in the Kubernetes API server manifest file, this is a finding.

## Group: SRG-APP-000439-CTR-001080

**Group ID:** `V-245544`

### Rule: Kubernetes endpoints must use approved organizational certificate and key pair to protect information in transit.

**Rule ID:** `SV-245544r918217_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Kubernetes control plane and external communication is managed by API Server. The main implementation of the API Server is to manage hardware resources for pods and container using horizontal or vertical scaling. Anyone who can gain access to the API Server can effectively control your Kubernetes architecture. Using authenticity protection, the communication can be protected against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. The communication session is protected by utilizing transport encryption protocols, such as TLS. TLS provides the Kubernetes API Server with a means to be able to authenticate sessions and encrypt traffic. By default, the API Server does not authenticate to the kubelet HTTPs endpoint. To enable secure communication for API Server, the parameter -kubelet-client-certificate and kubelet-client-key must be set. This parameter gives the location of the certificate and key pair used to secure API Server communication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests/ directory on the Kubernetes Control Plane. Run the command: grep -i kubelet-client-certificate * grep -I kubelet-client-key * If the setting "--kubelet-client-certificate" is not configured in the Kubernetes API server manifest file or contains no value, this is a finding. If the setting "--kubelet-client-key" is not configured in the Kubernetes API server manifest file or contains no value, this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-254800`

### Rule: Kubernetes must have a Pod Security Admission control file configured.

**Rule ID:** `SV-254800r927257_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An admission controller intercepts and processes requests to the Kubernetes API prior to persistence of the object, but after the request is authenticated and authorized. Kubernetes (> v1.23)offers a built-in Pod Security admission controller to enforce the Pod Security Standards. Pod security restrictions are applied at the namespace level when pods are created. The Kubernetes Pod Security Standards define different isolation levels for Pods. These standards define how to restrict the behavior of pods in a clear, consistent fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Change to the /etc/kubernetes/manifests directory on the Kubernetes Control Plane. Run the command: "grep -i admission-control-config-file *" If the setting "--admission-control-config-file" is not configured in the Kubernetes API Server manifest file, this is a finding. Inspect the .yaml file defined by the --admission-control-config-file. Verify PodSecurity is properly configured. If least privilege is not represented, this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-254801`

### Rule: Kubernetes must enable PodSecurity admission controller on static pods and Kubelets.

**Rule ID:** `SV-254801r918279_rule`
**Severity:** high

**Description:**
<VulnDiscussion>PodSecurity admission controller is a component that validates and enforces security policies for pods running within a Kubernetes cluster. It is responsible for evaluating the security context and configuration of pods against defined policies. To enable PodSecurity admission controller on Static Pods (kube-apiserver, kube-controller-manager, or kube-schedule), the argument "--feature-gates=PodSecurity=true" must be set. To enable PodSecurity admission controller on Kubelets, the featureGates PodSecurity=true argument must be set. (Note: The PodSecurity feature gate is GA as of v1.25.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Control Plane, change to the manifests' directory at /etc/kubernetes/manifests and run the command: grep -i feature-gates * For each manifest file, if the "--feature-gates" setting does not exist, does not contain the "--PodSecurity" flag, or sets the flag to "false", this is a finding. On each Control Plane and Worker Node, run the command: ps -ef | grep kubelet If the "--feature-gates" option exists, this is a finding. Note the path to the config file (identified by --config). Inspect the content of the config file: If the "featureGates" setting is not present, does not contain the "PodSecurity" flag, or sets the flag to "false", this is a finding.

