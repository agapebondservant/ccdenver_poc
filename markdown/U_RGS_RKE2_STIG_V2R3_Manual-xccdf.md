# STIG Benchmark: Rancher Government Solutions RKE2 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014-CTR-000035

**Group ID:** `V-254553`

### Rule: Rancher RKE2 must protect authenticity of communications sessions with the use of FIPS-validated 140-2 or 140-3 security requirements for cryptographic modules.

**Rule ID:** `SV-254553r1016525_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use strong TLS settings. RKE2 uses FIPS validated BoringCrypto modules. RKE2 Server can prohibit the use of SSL and unauthorized versions of TLS protocols to properly secure communication. There is a lot of traffic between RKE2 nodes to deploy, update, and delete resources so it is important to set strong TLS settings on top of this default feature. It is also important to use approved cypher suites. This ensures the protection of the transmitted information, confidentiality, and integrity so that the attacker cannot read or alter this communication. The use of unsupported protocol exposes vulnerabilities to the Kubernetes by rogue traffic interceptions, man-in-the-middle attacks, and impersonation of users or services from the container platform runtime, registry, and key store. To enable the enforcement of minimum version of TLS and cipher suites to be used by the various components of RKE2, the settings "tls-min-version" and "tls-cipher-suites" must be set. Further documentation of the FIPS modules can be found here: https://docs.rke2.io/security/fips_support. Satisfies: SRG-APP-000014-CTR-000035, SRG-APP-000014-CTR-000040, SRG-APP-000219-CTR-000550, SRG-APP-000441-CTR-001090, SRG-APP-000442-CTR-001095, SRG-APP-000514-CTR-001315, SRG-APP-000560-CTR-001340, SRG-APP-000605-CTR-001380, SRG-APP-000610-CTR-001385, SRG-APP-000635-CTR-001405, SRG-APP-000645-CTR-001410</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use strong TLS settings. On an RKE2 server, run each command: /bin/ps -ef | grep kube-apiserver | grep -v grep /bin/ps -ef | grep kube-controller-manager | grep -v grep /bin/ps -ef | grep kube-scheduler | grep -v grep For each, look for the existence of tls-min-version (use this command for an aid "| grep tls-min-version"): If the setting "tls-min-version" is not configured or it is set to "VersionTLS10" or "VersionTLS11", this is a finding. For each, look for the existence of the tls-cipher-suites. If "tls-cipher-suites" is not set for all servers, or does not contain the following, this is a finding: --tls-cipher-suites=suites=TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

## Group: SRG-APP-000023-CTR-000055

**Group ID:** `V-254554`

### Rule: RKE2 must use a centralized user management solution to support account management functions.

**Rule ID:** `SV-254554r1043176_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Kubernetes Controller Manager is a background process that embeds core control loops regulating cluster system state through the API Server. Every process executed in a pod has an associated service account. By default, service accounts use the same credentials for authentication. Implementing the default settings poses a high risk to the Kubernetes Controller Manager. Setting the use-service-account-credential value lowers the attack surface by generating unique service accounts settings for each controller instance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure use-service-account-credentials argument is set correctly. Run this command on the RKE2 Control Plane: /bin/ps -ef | grep kube-controller-manager | grep -v grep If --use-service-account-credentials argument is not set to "true" or is not configured, this is a finding.

## Group: SRG-APP-000026-CTR-000070

**Group ID:** `V-254555`

### Rule: Rancher RKE2 components must be configured in accordance with the security configuration settings based on DOD security configuration or implementation guidance, including SRGs, STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-254555r1056186_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to modify an existing account. Auditing of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail documents the creation of application user accounts and, as required, notifies administrators and/or application when accounts are created. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. Within Rancher RKE2, audit data can be generated from any of the deployed container platform components. This audit data is important when there are issues, such as security incidents, that must be investigated. To make the audit data worthwhile for the investigation of events, it is necessary to know where within the container platform the event occurred. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to offload those access control functions and focus on core application features and functionality. Satisfies: SRG-APP-000026-CTR-000070, SRG-APP-000027-CTR-000075, SRG-APP-000028-CTR-000080, SRG-APP-000092-CTR-000165, SRG-APP-000095-CTR-000170, SRG-APP-000096-CTR-000175, SRG-APP-000097-CTR-000180, SRG-APP-000098-CTR-000185, SRG-APP-000099-CTR-000190, SRG-APP-000100-CTR-000195, SRG-APP-000101-CTR-000205, SRG-APP-000319-CTR-000745, SRG-APP-000320-CTR-000750, SRG-APP-000343-CTR-000780, SRG-APP-000358-CTR-000805, SRG-APP-000374-CTR-000865, SRG-APP-000375-CTR-000870, SRG-APP-000381-CTR-000905, SRG-APP-000409-CTR-000990, SRG-APP-000492-CTR-001220, SRG-APP-000493-CTR-001225, SRG-APP-000494-CTR-001230, SRG-APP-000495-CTR-001235, SRG-APP-000496-CTR-001240, SRG-APP-000497-CTR-001245, SRG-APP-000498-CTR-001250, SRG-APP-000499-CTR-001255, SRG-APP-000500-CTR-001260, SRG-APP-000501-CTR-001265, SRG-APP-000502-CTR-001270, SRG-APP-000503-CTR-001275, SRG-APP-000504-CTR-001280, SRG-APP-000505-CTR-001285, SRG-APP-000506-CTR-001290, SRG-APP-000507-CTR-001295, SRG-APP-000508-CTR-001300, SRG-APP-000509-CTR-001305, SRG-APP-000510-CTR-001310, SRG-APP-000516-CTR-000790, SRG-APP-00516-CTR-001325</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Audit logging and policies: 1. On all hosts running RKE2 Server, run the command: /bin/ps -ef | grep kube-apiserver | grep -v grep If --audit-policy-file is not set, this is a finding. If --audit-log-mode is not = "blocking-strict", this is a finding. 2. Ensure the RKE2 Server configuration file on all RKE2 Server hosts, located at /etc/rancher/rke2/config.yaml, contains CIS profile setting. Run the following command: cat /etc/rancher/rke2/config.yaml RKE2 can be started with the profile flag set to cis, cis-1.23, or cis-1.6 depending on the RKE2 version. Available with October 2023 releases (v1.25.15+rke2r1, v1.26.10+rke2r1, v1.27.7+rke2r1, v1.28.3+rke2r1), use the generic profile: "cis". If a value for profile is not found or is not set correctly, this is a finding. (Example: "profile: cis") 3. Check the contents of the audit-policy file. By default, RKE2 expects the audit-policy file to be located at /etc/rancher/rke2/audit-policy.yaml; however, this location can be overridden in the /etc/rancher/rke2/config.yaml file with argument 'kube-apiserver-arg: "audit-policy-file=/etc/rancher/rke2/audit-policy.yaml"'. If the audit policy file does not exist or does not look like the following, this is a finding. apiVersion: audit.k8s.io/v1 kind: Policy metadata: name: rke2-audit-policy rules: - level: Metadata resources: - group: "" resources: ["secrets"] - level: RequestResponse resources: - group: "" resources: ["*"]

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-254556`

### Rule: The Kubernetes Controller Manager must have secure binding.

**Rule ID:** `SV-254556r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of attack vectors and implementing authentication and encryption on the endpoints available to external sources is paramount when securing the overall Kubernetes cluster. The Controller Manager API service exposes port 10252/TCP by default for health and metrics information use. This port does not encrypt or authenticate connections. If this port is exposed externally, an attacker can use this port to attack the entire Kubernetes cluster. By setting the bind address to only localhost (i.e., 127.0.0.1), only those internal services that require health and metrics information can access the Control Manager API.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure bind-address is set correctly. Run this command on the RKE2 Control Plane: /bin/ps -ef | grep kube-controller-manager | grep -v grep If --bind-address is not set to "127.0.0.1" or is not configured, this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-254557`

### Rule: The Kubernetes Kubelet must have anonymous authentication disabled.

**Rule ID:** `SV-254557r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>RKE2 registry is used to store images and is the keeper of truth for trusted images within the platform. To guarantee the images' integrity, access to the registry must be limited to those individuals who need to perform tasks to the images such as the update, creation, or deletion. Without this control access, images can be deleted that are in use by RKE2 causing a denial of service (DoS), and images can be modified or introduced without going through the testing and validation process allowing for the intentional or unintentional introduction of containers with flaws and vulnerabilities. By allowing anonymous connections, the controls put in place to secure the Kubelet can be bypassed. Setting anonymous authentication to "false" also disables unauthenticated requests from kubelets. While there are instances where anonymous connections may be needed (e.g., health checks) and Role-Based Access Controls (RBAC) are in place to limit the anonymous access, this access must be disabled and only enabled when necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure anonymous-auth is set correctly so anonymous requests will be rejected. Run this command on each node: /bin/ps -ef | grep kubelet | grep -v grep If --anonymous-auth is set to "true" or is not configured, this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-254558`

### Rule: The Kubernetes API server must have the insecure port flag disabled.

**Rule ID:** `SV-254558r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, the API server will listen on two ports. One port is the secure port and the other port is called the "localhost port". This port is also called the "insecure port", port 8080. Any requests to this port bypass authentication and authorization checks. If this port is left open, anyone who gains access to the host on which the master is running can bypass all authorization and authentication mechanisms put in place, and have full control over the entire cluster. Close the insecure port by setting the API server's --insecure-port flag to "0", ensuring that the --insecure-bind-address is not set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure insecure-port is set correctly. If running v1.20 through v1.23, this is default configuration so no change is necessary if not configured. If running v1.24, this check is Not Applicable. Run this command on the RKE2 Control Plane: /bin/ps -ef | grep kube-apiserver | grep -v grep If --insecure-port is not set to "0" or is not configured, this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-254559`

### Rule: The Kubernetes Kubelet must have the read-only port flag disabled.

**Rule ID:** `SV-254559r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Kubelet serves a small REST API with read access to port 10255. The read-only port for Kubernetes provides no authentication or authorization security control. Providing unrestricted access on port 10255 exposes Kubernetes pods and containers to malicious attacks or compromise. Port 10255 is deprecated and should be disabled. Close the read-only-port by setting the API server's read-only port flag to "0".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure read-only-port is set correctly so anonymous requests will be rejected. Run this command on each node: /bin/ps -ef | grep kubelet | grep -v grep If --read-only-port is not set to "0" or is not configured, this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-254560`

### Rule: The Kubernetes API server must have the insecure bind address not set.

**Rule ID:** `SV-254560r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, the API server will listen on two ports and addresses. One address is the secure address and the other address is called the "insecure bind" address and is set by default to localhost. Any requests to this address bypass authentication and authorization checks. If this insecure bind address is set to localhost, anyone who gains access to the host on which the master is running can bypass all authorization and authentication mechanisms put in place and have full control over the entire cluster. Close or set the insecure bind address by setting the API server's --insecure-bind-address flag to an IP or leave it unset and ensure that the --insecure-bind-port is not set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If running rke2 Kubernetes version > 1.20, this requirement is not applicable (NA). Ensure insecure-bind-address is set correctly. Run the command: ps -ef | grep kube-apiserver If the setting insecure-bind-address is found and set to "localhost", this is a finding.

## Group: SRG-APP-000033-CTR-000095

**Group ID:** `V-254561`

### Rule: The Kubernetes kubelet must enable explicit authorization.

**Rule ID:** `SV-254561r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Kubelet is the primary agent on each node. The API server communicates with each kubelet to perform tasks such as starting/stopping pods. By default, kubelets allow all authenticated requests, even anonymous ones, without requiring any authorization checks from the API server. This default behavior bypasses any authorization controls put in place to limit what users may perform within the Kubernetes cluster. To change this behavior, the default setting of AlwaysAllow for the authorization mode must be set to "Webhook".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure authorization-mode is set correctly in the kubelet on each rke2 node. Run this command on each node: /bin/ps -ef | grep kubelet | grep -v grep If --authorization-mode is not set to "Webhook" or is not configured, this is a finding.

## Group: SRG-APP-000033-CTR-000100

**Group ID:** `V-254562`

### Rule: The Kubernetes API server must have anonymous authentication disabled.

**Rule ID:** `SV-254562r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Kubernetes API Server controls Kubernetes via an API interface. A user who has access to the API essentially has root access to the entire Kubernetes cluster. To control access, users must be authenticated and authorized. By allowing anonymous connections, the controls put in place to secure the API can be bypassed. Setting anonymous authentication to "false" also disables unauthenticated requests from kubelets. While there are instances where anonymous connections may be needed (e.g., health checks) and Role-Based Access Controls (RBAC) are in place to limit the anonymous access, this access should be disabled, and only enabled when necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure anonymous-auth argument is set correctly. Run this command on the RKE2 Control Plane: /bin/ps -ef | grep kube-apiserver | grep -v grep If --anonymous-auth is set to "true" or is not configured, this is a finding.

## Group: SRG-APP-000100-CTR-000200

**Group ID:** `V-254563`

### Rule: All audit records must identify any containers associated with the event within Rancher RKE2.

**Rule ID:** `SV-254563r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensure that the --audit-log-maxage argument is set to 30 or as appropriate. Retaining logs for at least 30 days ensures that you can go back in time and investigate or correlate any events. Set your audit log retention period to 30 days or as per your business requirements. Result: Pass</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure audit-log-maxage is set correctly. Run the below command on the RKE2 Control Plane: /bin/ps -ef | grep kube-apiserver | grep -v grep If --audit-log-maxage argument is not set to at least 30 or is not configured, this is a finding. (By default, RKE2 sets the --audit-log-maxage argument parameter to 30.)

## Group: SRG-APP-000133-CTR-000300

**Group ID:** `V-254564`

### Rule: Configuration and authentication files for Rancher RKE2 must be protected.

**Rule ID:** `SV-254564r1016531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>There are various configuration files, logs, access credentials, and other files stored on the host filesystem that contain sensitive information. These files could potentially put at risk, along with other specific workloads and components: - API server. - proxy. - scheduler. - controller. - etcd. - Kubernetes administrator account information. - audit log access, modification, and deletion. - application access, modification, and deletion. - container runtime files. If an attacker can gain access to these files, changes can be made to open vulnerabilities and bypass user authorizations inherent within Kubernetes with RBAC implemented. It is crucial to ensure user permissions are enforced down through to the operating system. Protecting file permissions will ensure that if a nonprivileged user gains access to the system they will still not be able to access protected information from the cluster API, cluster configuration, and sensitive cluster information. This control relies on the underlying operating system also having been properly configured to allow only least privileged access to perform required operations. Satisfies: SRG-APP-000133-CTR-000300, SRG-APP-000133-CTR-000295, SRG-APP-000133-CTR-000305, SRG-APP-000133-CTR-000310</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
File system permissions: 1. Ensure correct permissions of the files in /etc/rancher/rke2 cd /etc/rancher/rke2 ls -l all owners are root:root all permissions are 0600 2. Ensure correct permissions of the files in /var/lib/rancher/rke2 cd /var/lib/rancher/rke2 ls -l all owners are root:root 3. Ensure correct permissions of the files and directories in /var/lib/rancher/rke2/agent cd /var/lib/rancher/rke2/agent ls -l owners and group are root:root File permissions set to 0640 for the following: rke2controller.kubeconfig kubelet.kubeconfig kubeproxy.kubeconfig Certificate file permissions set to 0600 client-ca.crt client-kubelet.crt client-kube-proxy.crt client-rke2-controller.crt server-ca.crt serving-kubelet.crt Key file permissions set to 0600 client-kubelet.key serving-kubelet.key client-rke2-controller.key client-kube-proxy.key The directory permissions to 0700 pod-manifests etc 4. Ensure correct permissions of the files in /var/lib/rancher/rke2/bin cd /var/lib/rancher/rke2/bin ls -l all owners are root:root all files are 0750 5. Ensure correct permissions of the directory /var/lib/rancher/rke2/data cd /var/lib/rancher/rke2 ls -l all owners are root:root permissions are 0750 6. Ensure correct permissions of each file in /var/lib/rancher/rke2/data cd /var/lib/rancher/rke2/data ls -l all owners are root:root all files are 0640 7. Ensure correct permissions of /var/lib/rancher/rke2/server cd /var/lib/rancher/rke2/server ls -l all owners are root:root The following directories are set to 0700 cred db tls The following directories are set to 0750 manifests logs The following file is set to 0600 token 8. Ensure the RKE2 Server configuration file on all RKE2 Server hosts contain the following: (cat /etc/rancher/rke2/config.yaml) write-kubeconfig-mode: "0600" If any of the permissions specified above do not match the required level, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-254565`

### Rule: Rancher RKE2 must be configured with only essential configurations.

**Rule ID:** `SV-254565r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is important to disable any unnecessary components to reduce any potential attack surfaces. RKE2 allows disabling the following components: - rke2-canal - rke2-coredns - rke2-ingress-nginx - rke2-kube-proxy - rke2-metrics-server If utilizing any of these components presents a security risk, or if any of the components are not required then they can be disabled by using the "disable" flag. If any of the components are not required, they can be disabled by using the "disable" flag. Satisfies: SRG-APP-000141-CTR-000315, SRG-APP-000384-CTR-000915</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the RKE2 Server configuration file on all RKE2 Server hosts contains a "disable" flag only if there are default RKE2 components that need to be disabled. If there are no default components that need to be disabled, this is not a finding. Run this command on the RKE2 Control Plane: cat /etc/rancher/rke2/config.yaml RKE2 allows disabling the following components. If any of the components are not required, they can be disabled: - rke2-canal - rke2-coredns - rke2-ingress-nginx - rke2-kube-proxy - rke2-metrics-server If services not in use are enabled, this is a finding.

## Group: SRG-APP-000142-CTR-000325

**Group ID:** `V-254566`

### Rule: Rancher RKE2 runtime must enforce ports, protocols, and services that adhere to the PPSM CAL.

**Rule ID:** `SV-254566r1050657_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ports, protocols, and services within the RKE2 runtime must be controlled and conform to the PPSM CAL. Those ports, protocols, and services that fall outside the PPSM CAL must be blocked by the runtime. Instructions on the PPSM can be found in DOD Instruction 8551.01 Policy. RKE2 sets most ports and services configuration upon initiation; however, these ports can be changed after the fact to noncompliant configurations. It is important to verify core component configurations for compliance. API Server, Scheduler, Controller, ETCD, and User Pods should all be checked to ensure proper PPS configuration. Satisfies: SRG-APP-000142-CTR-000325, SRG-APP-000142-CTR-000330, SRG-APP-000383-CTR-000910</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check Ports, Protocols, and Services (PPS). Change to the /var/lib/rancher/rke2/agent/pod-manifests directory on the Kubernetes RKE2 Control Plane. Run the command: grep kube-apiserver.yaml -I -insecure-port grep kube-apiserver.yaml -I -secure-port grep kube-apiserver.yaml -I -etcd-servers * Review findings against the most recent PPSM CAL: https://cyber.mil/ppsm/cal/ Any manifest and namespace PPS or services configuration not in compliance with PPSM CAL or otherwise approved by the information system security officer (ISSO) is a finding. If there are any ports, protocols, and services in the system documentation not in compliance with the CAL PPSM or otherwise approved by the ISSO, this is a finding. Any PPS not set in the system documentation is a finding. Verify API Server network boundary with the PPS associated with the CAL Assurance Categories. Any PPS not in compliance with the CAL Assurance Category requirements or otherwise approved by the ISSO is a finding. Review findings against the most recent PPSM CAL: https://cyber.mil/ppsm/cal/ Running these commands individually will show what ports are currently configured to be used by each of the core components. Inspect this output and ensure only proper ports are being used. If any ports not defined as the proper ports are being used, this is a finding. /var/lib/rancher/rke2/bin/kubectl get po -n kube-system -l component=kube-controller-manager -o=jsonpath="{.items[*].spec.containers[*].args}" /var/lib/rancher/rke2/bin/kubectl get po -n kube-system -l component=kube-scheduler -o=jsonpath="{.items[*].spec.containers[*].args}" /var/lib/rancher/rke2/bin/kubectl get po -n kube-system -l component=kube-apiserver -o=jsonpath="{.items[*].spec.containers[*].args}" | grep tls-min-version Verify user pods: User pods will also need to be inspected to ensure compliance. This will need to be on a case-by-case basis. cat /var/lib/rancher/rke2/server/db/etcd/config If any ports not defined as the proper ports are being used or otherwise approved by the ISSO, this is a finding.

## Group: SRG-APP-000171-CTR-000435

**Group ID:** `V-254567`

### Rule: Rancher RKE2 must store only cryptographic representations of passwords.

**Rule ID:** `SV-254567r1016559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secrets, such as passwords, keys, tokens, and certificates should not be stored as environment variables. These environment variables are accessible inside RKE2 by the "Get Pod" API call, and by any system, such as CI/CD pipeline, which has access to the definition file of the container. Secrets must be mounted from files or stored within password vaults.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the RKE2 Control Plane, run the following commands: kubectl get pods -A kubectl get jobs -A kubectl get cronjobs -A This will output all running pods, jobs, and cronjobs. Evaluate each of the above commands using the respective commands below: kubectl get pod -n <namespace> <pod> -o yaml kubectl get job -n <namespace> <job> -o yaml kubectl get cronjob -n <namespace> <cronjob> -o yaml If any contain sensitive values as environment variables, this is a finding.

## Group: SRG-APP-000190-CTR-000500

**Group ID:** `V-254568`

### Rule: Rancher RKE2 must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after five minutes of inactivity.

**Rule ID:** `SV-254568r1016534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating-system-level network connection. This does not mean that the application terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure streaming-connection-idle-timeout argument is set correctly. Run this command on each node: /bin/ps -ef | grep kubelet | grep -v grep If --streaming-connection-idle-timeout is set to < "5m", missing or the parameter is not configured, this is a finding.

## Group: SRG-APP-000233-CTR-000585

**Group ID:** `V-254569`

### Rule: Rancher RKE2 runtime must isolate security functions from nonsecurity functions.

**Rule ID:** `SV-254569r1016537_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>RKE2 runs as isolated as possible. RKE2 is a container-based Kubernetes distribution. A container image is essentially a complete and executable version of an application, which relies only on the host's OS kernel. Running containers use resource isolation features in the OS kernel, such as cgroups in Linux, to run multiple independent containers on the same OS. Unless part of the core RKE2 system or configured explicitly, containers managed by RKE2 should not have access to host resources. Proper hardening of the surrounding environment is independent of RKE2 but ensures overall security stature. When Kubernetes launches a container, there are several mechanisms available to ensure complete deployments: - When a primary container process fails it is destroyed rebooted. - When Liveness checks fail for the container deployment it is destroyed rebooted. - If a readiness check fails at any point after the deployment the container is destroyed rebooted. - Kubernetes has the ability to rollback a deployment configuration to a previous state if a deployment fails. - Failover traffic to a working replica if any of the previous problems are encountered. System kernel is responsible for memory, disk, and task management. The kernel provides a gateway between the system hardware and software. Kubernetes requires kernel access to allocate resources to the Control Plane. Threat actors that penetrate the system kernel can inject malicious code or hijack the Kubernetes architecture. It is vital to implement protections through Kubernetes components to reduce the attack surface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure protect-kernel-defaults argument is set correctly. Run this command on each node: /bin/ps -ef | grep kubelet | grep -v grep If --protect-kernel-defaults is not set to "true", missing or is not configured, this is a finding.

## Group: SRG-APP-000243-CTR-000600

**Group ID:** `V-254570`

### Rule: Rancher RKE2 runtime must maintain separate execution domains for each container by assigning each container a separate address space to prevent unauthorized and unintended information transfer via shared system resources.

**Rule ID:** `SV-254570r1016539_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Separating user functionality from management functionality is a requirement for all the components within the Kubernetes Control Plane. Without the separation, users may have access to management functions that can degrade the Kubernetes architecture and the services being offered, and can offer a method to bypass testing and validation of functions before introduced into a production environment. Satisfies: SRG-APP-000243-CTR-000600, SRG-APP-000431-CTR-001065, SRG-APP-000211-CTR-000530, SRG-APP-000243-CTR-000595</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
System namespaces are reserved and isolated. To view the available namespaces, run the command: kubectl get namespaces The namespaces to be validated include: default kube-public kube-system kube-node-lease For the default namespace, execute the commands: kubectl config set-context --current --namespace=default kubectl get all For the kube-public namespace, execute the commands: kubectl config set-context --current --namespace=kube-public kubectl get all For the kube-node-lease namespace, execute the commands: kubectl config set-context --current --namespace=kube-node-lease kubectl get all The only return values are the Kubernetes service objects (e.g., service/kubernetes). For the kube-system namespace, execute the commands: kubectl config set-context --current --namespace=kube-system kubectl get all The values returned include the following resources: - ETCD - Helm - Kubernetes API Server - Kubernetes Controller Manager - Kubernetes Proxy - Kubernetes Scheduler - Kubernetes Networking Components - Ingress Controller Components - Metrics Server If a return value from the "kubectl get all" command is not the Kubernetes service, one from the above lists, or a service otherwise approved by your Information Systems Security Officer (ISSO), this is a finding.

## Group: SRG-APP-000340-CTR-000770

**Group ID:** `V-254571`

### Rule: Rancher RKE2 must prevent nonprivileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-254571r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Admission controllers intercept requests to the Kubernetes API before an object is instantiated. Enabling the admissions webhook allows for Kubernetes to apply policies against objects that are to be created, read, updated or deleted. Admissions controllers can be used for: - Prevent pod’s ability to run privileged containers - Prevent pod’s ability to use privileged escalation - Controlling pod’s access to volume types - Controlling pod’s access to host file system - Controlling pod’s usage of host networking objects and configuration Satisfies: SRG-APP-000340-CTR-000770, SRG-APP-000342-CTR-000775</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using RKE2 v1.24 or older: On the Server Node, run the command: kubectl get podsecuritypolicy For any pod security policies listed, with the exception of system-unrestricted-psp (which is required for core Kubernetes functionality), edit the policy with the command: kubectl edit podsecuritypolicy policyname Where policyname is the name of the policy Review the runAsUser, supplementalGroups, and fsGroup sections of the policy. If any of these sections are missing, this is a finding. If the rule within the runAsUser section is not set to "MustRunAsNonRoot", this is a finding. If the ranges within the supplementalGroups section has min set to "0" or min is missing, this is a finding. If the ranges within the fsGroup section have a min set to "0" or the min is missing, this is a finding. If using RKE2 v1.25 or newer: On each controlplane node, validate that the file "/etc/rancher/rke2/rke2-pss.yaml" exists and the default configuration settings match the following: defaults: audit: restricted audit-version: latest enforce: restricted enforce-version: latest warn: restricted warn-version: latest If the configuration file differs from the above, this is a finding.

## Group: SRG-APP-000378-CTR-000880

**Group ID:** `V-254572`

### Rule: Rancher RKE2 must prohibit the installation of patches, updates, and instantiation of container images without explicit privileged status.

**Rule ID:** `SV-254572r1016560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Controlling access to those users and roles responsible for patching and updating RKE2 reduces the risk of untested or potentially malicious software from being installed within the platform. This access may be separate from the access required to install container images into the registry and those access requirements required to instantiate an image into a service. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceeds the rights of a regular user. Kubernetes uses the API Server to control communication to the other services that makeup Kubernetes. The use of authorizations and not the default of "AlwaysAllow" enables the Kubernetes functions control to only the groups that need them. To control access, the API server must have one of the following options set for the authorization mode: --authorization-mode=ABAC Attribute-Based Access Control (ABAC) mode allows a user to configure policies using local files. --authorization-mode=RBAC Role-based access control (RBAC) mode allows a user to create and store policies using the Kubernetes API. --authorization-mode=Webhook WebHook is an HTTP callback mode that allows a user to manage authorization using a remote REST endpoint. --authorization-mode=Node Node authorization is a special-purpose authorization mode that specifically authorizes API requests made by kubelets. --authorization-mode=AlwaysDeny This flag blocks all requests. Use this flag only for testing. Satisfies: SRG-APP-000378-CTR-000880, SRG-APP-000378-CTR-000885</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure authorization-mode is set correctly in the apiserver. Run this command on all RKE2 Control Plane hosts: /bin/ps -ef | grep kube-apiserver | grep -v grep If --authorization-mode is not set to "RBAC,Node" or is not configured, this is a finding. (By default, RKE2 sets Node,RBAC as the parameter to the --authorization-mode argument.)

## Group: SRG-APP-000429-CTR-001060

**Group ID:** `V-254573`

### Rule: Rancher RKE2 keystore must implement encryption to prevent unauthorized disclosure of information at rest within Rancher RKE2.

**Rule ID:** `SV-254573r1050650_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encrypting secrets at rest in etcd. By default, RKE2 will create an encryption key and configuration file and pass these to the Kubernetes API server. The result is that RKE2 automatically encrypts Kubernetes Secret objects when writing them to etcd.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is Not Applicable for RKE2 versions 1.20 and greater. Review the encryption configuration file. As root or with root permissions, run the following command: view /var/lib/rancher/rke2/server/cred/encryption-config.json Ensure the RKE2 configuration file on all RKE2 servers, located at /etc/rancher/rke2/config.yaml, does NOT contain: secrets-encryption: false If secrets encryption is turned off, this is a finding.

## Group: SRG-APP-000454-CTR-001110

**Group ID:** `V-254574`

### Rule: Rancher RKE2 must remove old components after updated versions have been installed.

**Rule ID:** `SV-254574r961677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of Rancher RKE2 components that are not removed after updates have been installed may be exploited by adversaries by causing older components to execute which contain vulnerabilities. When these components are deleted, the likelihood of this happening is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view all pods and the images used to create the pods, from the RKE2 Control Plane, run the following command: kubectl get pods --all-namespaces -o jsonpath="{..image}" | \ tr -s '[[:space:]]' '\n' | \ sort | \ uniq -c Review the images used for pods running within Kubernetes. If there are multiple versions of the same image, this is a finding.

## Group: SRG-APP-000456-CTR-001125

**Group ID:** `V-254575`

### Rule: Rancher RKE2 registry must contain the latest images with most recent updates and execute within Rancher RKE2 runtime as authorized by IAVM, CTOs, DTMs, and STIGs.

**Rule ID:** `SV-254575r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Software supporting RKE2, images in the registry must stay up to date with the latest patches, service packs, and hot fixes. Not updating RKE2 and container images will expose the organization to vulnerabilities. Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant container platform components may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. RKE2 components will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. RKE2 registry will ensure the images are current. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Authenticate on the RKE2 Control Plane. Verify all nodes in the cluster are running a supported version of RKE2 Kubernetes. Run command: kubectl get nodes If any nodes are running an unsupported version of RKE2 Kubernetes, this is a finding. Verify all images running in the cluster are patched to the latest version. Run command: kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec.containers[*].image}" | tr -s '[[:space:]]' '\n' | sort | uniq -c If any images running in the cluster are not the latest version, this is a finding. Note: Kubernetes release support levels can be found at: https://kubernetes.io/releases/

## Group: SRG-APP-000131-CTR-000285

**Group ID:** `V-268321`

### Rule: Rancher RKE2 must be built from verified packages. 

**Rule ID:** `SV-268321r1017019_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only RKE2 images that have been properly signed by Rancher Government's authorized key will be deployed to ensure the cluster's security and compliance with organizational policies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Utilizing Hauler (https://hauler.dev), ensure all RKE2 Kubernetes Container images running in the RKE2 cluster have been obtained and their signatures have been validated and signed by Rancher Government Solutions Private Key. For reference, the public key is available at: https://raw.githubusercontent.com/rancherfederal/carbide-releases/main/carbide-key.pub For more information about verifying the signatures of Carbide images, including RKE2, see: https://rancherfederal.github.io/carbide-docs/docs/registry-docs/validating-images If any RKE2 images are identified as not being signed by the Rancher Government Solutions' private key, this is a finding.

