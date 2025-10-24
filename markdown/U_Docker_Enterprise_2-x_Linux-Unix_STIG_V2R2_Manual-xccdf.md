# STIG Benchmark: Docker Enterprise 2.x Linux/UNIX Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-235775`

### Rule: The Docker Enterprise Per User Limit Login Session Control in the Universal Control Plane (UCP) Admin Settings must be set to an organization-defined value for all accounts and/or account types.

**Rule ID:** `SV-235775r960735_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The UCP component of Docker Enterprise includes a built-in access authorization mechanism called eNZi which can be integrated with an LDAP server and subsequently configured to limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types. Per-user session control limits are configured with a default of 10. For reference, the per user limit in UCP specifies the maximum number of sessions that any user can have active at any given time. If creating a new session would put a user over this limit then the least recently used session will be deleted. A value of zero disables limiting the number of sessions that users may have. This configuration applies to both the UCP and DTR management consoles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the "Per User Limit" Login Session Control in the UCP Admin Settings is set according to the values defined in the System Security Plan. via UI: In the UCP web console, navigate to "Admin Settings" | "Authentication & Authorization" and verify the "Per User Limit" field is set according to the number specified in the System Security Plan. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands from a machine with connectivity to the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml|grep per_user_limit If the "per_user_limit" entry under the "[auth.sessions]" section in the output is not set according to the value defined in the SSP, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-235776`

### Rule: TCP socket binding for all Docker Engine - Enterprise nodes in a Universal Control Plane (UCP) cluster must be disabled.

**Rule ID:** `SV-235776r960759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UCP component of Docker Enterprise configures and leverages Swarm Mode for node-to-node cluster communication. Swarm Mode is built in to Docker Engine - Enterprise and uses TLS 1.2 at a minimum for encrypting communications. Under the hood, Swarm Mode includes an embedded public key infrastructure (PKI) system. When a UCP cluster is initialized, the first node in the cluster designates itself as a manager node. That node subsequently generates a new root Certificate Authority (CA) along with a key pair, which are used to secure communications with other UCP nodes that join the swarm. One can also specify his/her own externally-generated root CA upon initialization of a UCP cluster. The manager node also generates two tokens to use when joining additional nodes to the cluster: one worker token and one manager token. Each token includes the digest of the root CA’s certificate and a randomly generated secret. When a node joins the cluster, the joining node uses the digest to validate the root CA certificate from the remote manager. The remote manager uses the secret to ensure the joining node is an approved node. Each time a new node joins the cluster, the manager issues a certificate to the node. The certificate contains a randomly generated node ID to identify the node under the certificate common name (CN) and the role under the organizational unit (OU). The node ID serves as the cryptographically secure node identity for the lifetime of the node in the current swarm. In this mutual TLS architecture, all nodes encrypt communications using a minimum of TLS 1.2, thereby satisfying the requirements of this control. This information can also be referenced at https://docs.docker.com/engine/swarm/how-swarm-mode-works/pki/ and https://docs.docker.com/ee/ucp/ucp-architecture/. By itself, Docker Engine - Enterprise is configured by default to listen for API requests via a UNIX domain socket (or IPC socket) created at /var/run/docker.sock on supported Linux distributions and via a named pipe at npipe:////./pipe/docker_engine on Windows Server 2016 and newer. Docker Engine - Enterprise can also be configured to listen for API requests via additional socket types, including both TCP and FD (only on supported systemd-based Linux distributions). If configured to listen for API requests via the TCP socket type over TCP port 2376 and with the daemon flags and SSL certificates, then, at a minimum, TLS 1.2 is used for encryption; therefore this control is applicable and is inherently met in this configuration. If configured to listen for API requests via the TCP socket type, but without TLS verification and certifications, then the instance remains vulnerable and is not properly configured to meet the requirements of this control. If configured to listen for API requests via the FD socket type, then this control is not applicable. More information can be found at https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option. The TCP socket binding should be disabled when running Engine as part of a UCP cluster. Satisfies: SRG-APP-000014, SRG-APP-000141, SRG-APP-000219, SRG-APP-000383, SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442, SRG-APP-000142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the Docker Engine - Enterprise component of Docker Enterprise. via CLI: Linux: Verify the daemon has not been started with the "-H TCP://[host]" argument by running the following command: ps -ef | grep dockerd If -H UNIX://, this is not a finding. If the "-H TCP://[host]" argument appears in the output, then this is a finding.

## Group: SRG-APP-000015

**Group ID:** `V-235777`

### Rule: FIPS mode must be enabled on all Docker Engine - Enterprise nodes.

**Rule ID:** `SV-235777r960762_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When FIPS mode is enabled on a Docker Engine - Enterprise node, it uses FIPS-validated cryptography to protect the confidentiality of remote access sessions to any bound TCP sockets with TLS enabled and configured. FIPS mode in Docker Engine - Enterprise is automatically enabled when FIPS mode is also enabled on the underlying host operating system. This control is only configurable for the Docker Engine - Enterprise component of Docker Enterprise as only the Engine includes FIPS-validated cryptography. Neither Universal Control Plane (UCP) nor Docker Trusted Registry (DTR) include FIPS-validated cryptography at this time. However, both UCP and DTR will include FIPS-validated cryptography in a future release. Therefore, for UCP/DTR this control is applicable but not yet met. Satisfies: SRG-APP-000015, SRG-APP-000231, SRG-APP-000014, SRG-APP-000570, SRG-APP-000395, SRG-APP-000514, SRG-APP-000416, SRG-APP-000156, SRG-APP-000172, SRG-APP-000179, SRG-APP-000224, SRG-APP-000411, SRG-APP-000412, SRG-APP-000555, SRG-APP-000635</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to Docker Engine - Enterprise. Verify FIPS mode is enabled on the host operating system. Execute the following command to verify that FIPS mode is enabled on the Engine: docker info The "Security Options" section in the response should show a "fips" label, indicating that, when configured, the remotely accessible Engine API uses FIPS-validated digital signatures in conjunction with an approved hash function to protect the integrity of remote access sessions. If the "fips" label is not shown in the "Security Options" section, then this is a finding.

## Group: SRG-APP-000016

**Group ID:** `V-235778`

### Rule: The audit log configuration level must be set to request in the Universal Control Plane (UCP) component of Docker Enterprise.

**Rule ID:** `SV-235778r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UCP and Docker Trusted Registry (DTR) components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise. Satisfies: SRG-APP-000016, SRG-APP-000089, SRG-APP-000515, SRG-APP-000510, SRG-APP-000509, SRG-APP-000508, SRG-APP-000507, SRG-APP-000506, SRG-APP-000505, SRG-APP-000504, SRG-APP-000503, SRG-APP-000502, SRG-APP-000501, SRG-APP-000500, SRG-APP-000499, SRG-APP-000498, SRG-APP-000497, SRG-APP-000496, SRG-APP-000495, SRG-APP-000494, SRG-APP-000493, SRG-APP-000492, SRG-APP-000484, SRG-APP-000447, SRG-APP-000381, SRG-APP-000343, SRG-APP-000101, SRG-APP-000100, SRG-APP-000099, SRG-APP-000098, SRG-APP-000097, SRG-APP-000096, SRG-APP-000095, SRG-APP-000093, SRG-APP-000092, SRG-APP-000091</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Verify that the audit log configuration level in UCP is set to "request": Via UI: As a Docker EE Admin, navigate to "Admin Settings" | "Audit Logs" in the UCP management console, and verify "Audit Log Level" is set to "Request". If the audit log configuration level is not set to "Request", this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands from a machine that can communicate with the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "level" entry under the "[audit_log_configuration]" section in the output, and verify that it is set to "request". If the "level" entry under the "[audit_log_configuration]" section in the output is not set to "request", then this is a finding.

## Group: SRG-APP-000016

**Group ID:** `V-235779`

### Rule: The host operating systems auditing policies for the Docker Engine - Enterprise component of Docker Enterprise must be set.

**Rule ID:** `SV-235779r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise. Satisfies: SRG-APP-000016, SRG-APP-000090, SRG-APP-000091, SRG-APP-000097, SRG-APP-000098, SRG-APP-000496, SRG-APP-000504, SRG-APP-000510, SRG-APP-000509, SRG-APP-000508, SRG-APP-000507, SRG-APP-000506, SRG-APP-000505, SRG-APP-000503, SRG-APP-000502, SRG-APP-000500, SRG-APP-000499, SRG-APP-000498, SRG-APP-000497, SRG-APP-000495, SRG-APP-000494, SRG-APP-000493, SRG-APP-000492, SRG-APP-000485, SRG-APP-000484, SRG-APP-000381, SRG-APP-000343, SRG-APP-000115, SRG-APP-000111, SRG-APP-000101, SRG-APP-000100, SRG-APP-000099, SRG-APP-000096, SRG-APP-000095, SRG-APP-000092, SRG-APP-000089, SRG-APP-000501, SRG-APP-000447</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the underlying host operating system on which the Docker Engine - Enterprise instance is running. Verify that the auditing capabilities provided by the underlying host have been properly configured to audit Docker Engine - Enterprise: (Linux) Check that auditd has been installed and that audit rules are configured against the following components of Docker Engine - Enterprise: auditctl -l | grep -e /usr/bin/docker -e /var/lib/docker -e /etc/docker -e /etc/default/docker -e /etc/docker/daemon.json -e /usr/bin/docker-containerd -e /usr/bin/docker-runc systemctl show -p FragmentPath docker.service or auditctl -l | grep docker.service systemctl show -p FragmentPath docker.socket or auditctl -l | grep docker.sock If audit rules aren't properly configured for the paths and services listed above, then this is a finding.

## Group: SRG-APP-000023

**Group ID:** `V-235780`

### Rule: LDAP integration in Docker Enterprise must be configured.

**Rule ID:** `SV-235780r960768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both the Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise leverage the same authentication and authorization backplane known as eNZi. The eNZi backplane provides automated mechanisms for supporting account management functions and allows for LDAP integration in UCP and DTR. While eNZi includes its own managed user database, it is recommended that LDAP integration be configured to more completely satisfy the requirements of this control. Satisfies: SRG-APP-000023, SRG-APP-000405, SRG-APP-000404, SRG-APP-000403, SRG-APP-000401, SRG-APP-000397, SRG-APP-000392, SRG-APP-000148, SRG-APP-000141, SRG-APP-000391</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that LDAP integration is enabled and properly configured in the UCP Admin Settings and verify that the LDAP/AD server is configured per the requirements set forth in the appropriate OS STIG. via UI: In the UCP web console, navigate to "Admin Settings" | "Authentication & Authorization" and verify "LDAP Enabled" is set to "Yes" and that it is properly configured. If it is not set to yes and if the LDAP server is not configured then this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands from a machine with connectivity to the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "backend" entry under the "[auth]" section in the output, and verify that it is set to "ldap". *NOTE: For security reasons, the "[auth.ldap]" section is not stored in the config file and can only be viewed from the UCP Admin Settings UI. If the "backend =" entry under the "[auth]" section in the output is not set to "ldap", then this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-235781`

### Rule: A policy set using the built-in role-based access control (RBAC) capabilities in the Universal Control Plane (UCP) component of Docker Enterprise must be configured.

**Rule ID:** `SV-235781r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both the UCP and Docker Trusted Registry (DTR) components of Docker Enterprise leverage the same authentication and authorization backplane known as eNZi. eNZi provides UCP and DTR with role-based access control functionality to enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. The eNZi backplane includes its own managed user database, and also allows for LDAP integration in UCP and DTR. While role-based access control mechanisms are provided regardless of whether or not LDAP integration is enabled, it is recommended to enable LDAP integration to better meet the requirements of this control. Satisfies: SRG-APP-000033, SRG-APP-000038, SRG-APP-000039, SRG-APP-000080, SRG-APP-000243, SRG-APP-000246, SRG-APP-000247, SRG-APP-000267, SRG-APP-000311, SRG-APP-000313, SRG-APP-000314, SRG-APP-000328, SRG-APP-000340, SRG-APP-000342, SRG-APP-000378, SRG-APP-000380, SRG-APP-000384</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Verify that the applied RBAC policy sets in UCP are configured per the requirements set forth by the System Security Plan (SSP). via UI: As a Docker EE Admin, navigate to "Access Control" | "Grants" in the UCP web console. Verify that all grants and cluster role bindings applied to Swarm are configured per the requirements set forth by the System Security Plan (SSP). If the applied RBAC policy sets in UCP are not configured per the requirements set forth by the SSP, then this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands on a machine that can communicate with the UCP management console: AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/collectionGrants?subjectType=all&expandUser=true&showPaths=true Verify that all grants applied to Swarm in the API response are configured per the requirements set forth by the System Security Plan (SSP). If the applied RBAC policy sets in UCP are not configured per the requirements set forth by the SSP, then this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-235782`

### Rule: A policy set using the built-in role-based access control (RBAC) capabilities in the Docker Trusted Registry (DTR) component of Docker Enterprise must be set.

**Rule ID:** `SV-235782r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both the Universal Control Plane (UCP) and DTR components of Docker Enterprise leverage the same authentication and authorization backplane known as eNZi. eNZi provides UCP and DTR with role-based access control functionality to enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. These policies are defined in the System Security Plan along with organization information, application user roles, system resources and access requirements. The eNZi backplane includes its own managed user database, and also allows for LDAP integration in UCP and DTR. While role-based access control mechanisms are provided regardless of whether or not LDAP integration is enabled, it is recommended to enable LDAP integration to better meet the requirements of this control. Satisfies: SRG-APP-000033, SRG-APP-000243, SRG-APP-000246, SRG-APP-000247, SRG-APP-000267, SRG-APP-000328, SRG-APP-000340, SRG-APP-000342, SRG-APP-000378, SRG-APP-000380, SRG-APP-000384, SRG-APP-000038, SRG-APP-000039, SRG-APP-000080, SRG-APP-000311, SRG-APP-000313, SRG-APP-000314</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the DTR component of Docker Enterprise. Verify that the organization, team and user permissions in DTR are configured per the System Security Plan (SSP). Obtain and review SSP. Identify organization roles, teams and users. via UI: As a Docker EE Admin, navigate to "Organizations" and verify the list of organizations and teams within those organizations are setup per the SSP. Navigate to "Users" and verify that the list of users are assigned to appropriate organizations, teams and repositories per the SSP. If the organization, team and user permissions in DTR are not configured per the SSP, this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE admin, execute the following commands on a machine that can communicate with the DTR management console: AUTHTOKEN=$(curl -kLsS -u <username>:<password> "https://[dtr_url]/auth/token" | jq -r .token) Execute the following command to verify that the teams associated with an organization have access to the appropriate repositories per the System Security Plan: curl -k -H "Authorization: Bearer $AUTHTOKEN" -X GET "https://[dtr_url]/api/v0/accounts/[org_name]/teams/[team_name]/repositoryAccess" Execute the following commands on a machine that can communicate with the UCP management console to verify that the members of the team with access to these repositories is appropriate per the SSP: AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/accounts/[orgNameOrID]/teams/[teamNameOrID]/members If the organization, team and user permissions in DTR are not configured per the SSP, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-235783`

### Rule: Docker Enterprise sensitive host system directories must not be mounted on containers.

**Rule ID:** `SV-235783r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sensitive host system directories such as below should not be allowed to be mounted as container volumes especially in read-write mode. Linux: / /boot /dev /etc /lib /proc /sys /usr Windows: %windir% (C:\Windows) %windir%\system32 (C:\Windows\system32) %programdata% %programData%\docker C:\Program Files C:\Program Files (x86) C:\Users If sensitive directories are mounted in read-write mode, it would be possible to make changes to files within those sensitive directories. The changes might bring down security implications or unwarranted changes that could put the Docker host in compromised state. Docker defaults to a read-write volume but the user can also mount a directory read-only. By default, no sensitive host directories are mounted on containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise. Verify that no running containers have mounted sensitive host system directories. Refer to System Security Plan for list of sensitive folders. via CLI: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}' | grep -iv "ucp\|kubelet\|dtr" Verify in the output that no containers are running with mounted RW access to sensitive host system directories. If there are containers mounted with RW access to sensitive host system directories, this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-235784`

### Rule: The Docker Enterprise hosts process namespace must not be shared.

**Rule ID:** `SV-235784r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Process ID (PID) namespaces isolate the PID number space, meaning that processes in different PID namespaces can have the same PID. This is process level isolation between containers and the host. PID namespace provides separation of processes. The PID Namespace removes the view of the system processes, and allows process IDs to be reused including PID 1. If the host's PID namespace is shared with the container, it would allow processes within the container to see all of the processes on the host system. This breaks the benefit of process level isolation between the host and the containers. Someone having access to the container can eventually know all the processes running on the host system and can even kill the host system processes from within the container. Hence, do not share the host's process namespace with the containers. Container processes cannot see the processes on the host system. In certain cases, the container should share the host's process namespace. For example, the user could build a container with debugging tools like strace or gdb, but want to use these tools when debugging processes within the container. If this is desired, then share only one (or needed) host process by using the -p switch. Example: docker run --pid=host rhel7 strace -p 1234 By default, all containers have the PID namespace enabled and the host's process namespace is not shared with the containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system. Ensure the host's process namespace is not shared. via CLI: Linux: As a Docker EE Admin, execute the following command using a UCP client bundle: docker ps --all | grep -iv "ucp\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: PidMode={{ .HostConfig.PidMode }}' If PidMode = "host", it means the host PID namespace is shared with the container and this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-235785`

### Rule: The Docker Enterprise hosts IPC namespace must not be shared.

**Rule ID:** `SV-235785r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IPC (POSIX/SysV IPC) namespace provides separation of named shared memory segments, semaphores, and message queues. IPC namespace on the host thus should not be shared with the containers and should remain isolated. IPC namespace provides separation of IPC between the host and containers. If the host's IPC namespace is shared with the container, it would allow processes within the container to see all of the IPC on the host system. This breaks the benefit of IPC level isolation between the host and the containers. Someone having access to the container can eventually manipulate the host IPC. Hence, do not share the host's IPC namespace with the containers. Shared memory segments are used to accelerate inter-process communication. It is commonly used by high-performance applications. If such applications are containerized into multiple containers, the user might need to share the IPC namespace of the containers to achieve high performance. In such cases, the user should still be sharing container specific IPC namespaces only and not the host IPC namespace. The user may share the container's IPC namespace with another container as below: Example: docker run --interactive --tty --ipc=container:e3a7a1a97c58 centos /bin/bash By default, all containers have the IPC namespace enabled and host IPC namespace is not shared with any container.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system. Ensure the host's IPC namespace is not shared. via CLI: Linux: As a Docker EE Admin, execute the following command using a UCP client bundle: docker ps --all | grep -iv "ucp\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: IpcMode={{ .HostConfig.IpcMode }}' If IpcMode="shareable", then the host's IPC namespace is shared and this is a finding.

## Group: SRG-APP-000090

**Group ID:** `V-235786`

### Rule: log-opts on all Docker Engine - Enterprise nodes must be configured.

**Rule ID:** `SV-235786r960882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. All audit logs generated by UCP and DTR can be forwarded to a remote log aggregation system by configuring an appropriate log driver plugin on all Docker Engine - Enterprise nodes in a cluster. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify this check on all Docker Engine - Enterprise nodes in the cluster. via CLI: Linux: Execute the following commands as a trusted user on the host operating system: Note: daemon.json file does not exist by default and must be created. Refer to https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file for all options. cat /etc/docker/daemon.json Verify that the "log-opts" object includes the "max-size" and "max-file" properties and that they are set accordingly in the output. If the "log-opts" object does not include the "max-size" and "max-file" properties and/or are not set accordingly, then this is a finding.

## Group: SRG-APP-000108

**Group ID:** `V-235787`

### Rule: Docker Enterprise must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-235787r960912_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. All audit logs generated by UCP and DTR can be forwarded to a remote log aggregation system by configuring an appropriate log driver plugin on all Docker Engine - Enterprise nodes in a cluster. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
via CLI: Linux: Execute the following commands as a trusted user on the host operating system: cat /etc/docker/daemon.json Verify that the "log-driver" property is set to one of the following: "syslog", "awslogs", "splunk", "gcplogs", "logentries" or "<plugin>" (where <plugin> is the naming of a third-party Docker logging driver plugin). Work with the SIEM administrator to determine if an alert is configured when audit data is no longer received as expected. If "log-driver" is not set, or if alarms are not configured in the SIEM, then this is a finding.

## Group: SRG-APP-000131

**Group ID:** `V-235788`

### Rule: Docker Incs official GPG key must be added to the host using the users operating systems respective package repository management tooling.

**Rule ID:** `SV-235788r960954_rule`
**Severity:** low

**Description:**
<VulnDiscussion>All packaged components of Docker Enterprise are digitally signed using GPG keys maintained by Docker, Inc. The Docker Engine - Enterprise daemon, itself, is digitally signed. Furthermore, all Docker, Inc-managed Linux repositories are themselves signed using GPG keys. On Windows, if Docker is installed via the PowerShell PackageManagement (aka OneGet) provider, the provider is managed by Microsoft, and provider artifacts are signed by Microsoft. The Universal Control Plane (UCP) and Docker Trusted Registry (DTR) installation images are digitally signed by Docker, Inc using Docker Content Trust.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Linux systems, verify that the host is configured to trust Docker Inc's repository GPG keys and that Docker Engine - Enterprise is installed from these repositories as such. If installing in an offline environment, validate that the Engine's package signature matches that as published by Docker, Inc. Execute the following command to validate the Docker image signature digests of UCP and DTR: docker trust inspect docker/ucp:[ucp_version] docker/dtr:[dtr_version] Check that the "SignedTags" array for both images in the output includes a "Digest" field. If the SignedTags array does not contain a Digest field, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235789`

### Rule: The insecure registry capability in the Docker Engine - Enterprise component of Docker Enterprise must be disabled.

**Rule ID:** `SV-235789r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Docker considers a private registry either secure or insecure. By default, registries are considered secure. Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of Universal Control Plane (UCP) and Docker Trusted Registry (DTR) and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the Docker Engine - Enterprise component of Docker Enterprise. via CLI: Linux: As a trusted user on the underlying host operating system, execute the following command: ps -ef | grep dockerd Ensure that the "--insecure-registry" parameter is not present. If it is present, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235790`

### Rule: On Linux, a non-AUFS storage driver in the Docker Engine - Enterprise component of Docker Enterprise must be used.

**Rule ID:** `SV-235790r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The aufs storage driver is the oldest storage driver. It is based on a Linux kernel patch-set that is unlikely to be merged into the main Linux kernel. aufs driver is also known to cause some serious kernel crashes. aufs just has legacy support from Docker. Most importantly, aufs is not a supported driver in many Linux distributions using latest Linux kernels. Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of Universal Control Plane (UCP) and Docker Trusted Registry (DTR) and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the Docker Engine - Enterprise component of Docker Enterprise and only when it is used on a Linux host operating system. via CLI: Linux: As a trusted user on the underlying host operating system, execute the following command: docker info | grep -e "^Storage Driver:\s*aufs\s*$" If the Storage Driver setting contains *aufs, then this is a finding. If the above command returns no values, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235791`

### Rule: The userland proxy capability in the Docker Engine - Enterprise component of Docker Enterprise must be disabled.

**Rule ID:** `SV-235791r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The docker daemon starts a userland proxy service for port forwarding whenever a port is exposed. Where hairpin NAT is available, this service is generally superfluous to requirements and can be disabled. Docker engine provides two mechanisms for forwarding ports from the host to containers, hairpin NAT, and a userland proxy. In most circumstances, the hairpin NAT mode is preferred as it improves performance and makes use of native Linux iptables functionality instead of an additional component. Where hairpin NAT is available, the userland proxy should be disabled on startup to reduce the attack surface of the installation. Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of Universal Control Plane (UCP) and Docker Trusted Registry (DTR) and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the Docker Engine - Enterprise component of Docker Enterprise and only when it is not being operated as part of a UCP cluster. via CLI: Linux: As a trusted user on the underlying host operating system, execute the following command: ps -ef | grep dockerd Ensure that the "--userland-proxy" parameter is set to "false". If it is not, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235792`

### Rule: Experimental features in the Docker Engine - Enterprise component of Docker Enterprise must be disabled.

**Rule ID:** `SV-235792r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Avoid experimental features in production. Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of Universal Control Plane (UCP) and Docker Trusted Registry (DTR) and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the Docker Engine - Enterprise component of Docker Enterprise. via CLI: Linux: As a trusted user on the underlying host operating system, execute the following command: docker version --format '{{ .Server.Experimental }}' Ensure that the "Experimental" property is set to "false". If it is not, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235793`

### Rule: The Docker Enterprise self-signed certificates in Universal Control Plane (UCP) must be replaced with DoD trusted, signed certificates.

**Rule ID:** `SV-235793r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of Docker Trusted Registry (DTR) and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that UCP has been integrated with a trusted certificate authority (CA). via UI: In the UCP web console, navigate to "Admin Settings" | "Certificates" and click on the "Download UCP Server CA Certificate" link. Verify that the contents of the downloaded "ca.pem" file match that of the trusted CA certificate. via CLI: Linux: Execute the following command and verify the certificate chain in the output is valid and matches that of the trusted CA: echo "" | openssl s_client -connect [ucp_url]:443 | openssl x509 -noout -text If the certificate chain does not match the chain as defined by the System Security Plan, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235794`

### Rule: The Docker Enterprise self-signed certificates in Docker Trusted Registry (DTR) must be replaced with DoD trusted, signed certificates.

**Rule ID:** `SV-235794r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of Universal Control Plane (UCP) and DTR and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that DTR has been integrated with a trusted certificate authority (CA). via UI: In the DTR web console, navigate to "System" | "General" and click on the "Show TLS settings" link in the "Domain & Proxies" section. Verify the certificate chain in "TLS Root CA" box is valid and matches that of the trusted CA. via CLI: Linux: Execute the following command and verify the certificate chain in the output is valid and matches that of the trusted CA: echo "" | openssl s_client -connect [dtr_url]:443 | openssl x509 -noout -text If the certificate chain in the output is not valid and does not match that of the trusted CA, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235795`

### Rule: The option in Universal Control Plane (UCP) allowing users and administrators to schedule containers on all nodes, including UCP managers and Docker Trusted Registry (DTR) nodes must be disabled in Docker Enterprise.

**Rule ID:** `SV-235795r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of UCP and DTR and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that admins and users are not allowed to schedule containers on manager nodes and DTR nodes. via UI: As a Docker EE Admin, navigate to "Admin Settings" | "Scheduler" in the UCP management console. Verify that the "Allow administrators to deploy containers on UCP managers or nodes running DTR" and "Allow users to schedule on all nodes, including UCP managers and DTR nodes" options are both unchecked. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands on a machine that can communicate with the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "enable_admin_ucp_scheduling" entry under the "[scheduling_configuration]" section in the output, and verify that it is set to "false". If "enable_admin_ucp_scheduling" is not set to "false", this is a finding. Execute the following command: curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/collectionGrants?subjectType=all&expandUser=true&showPaths=true Ensure a Grant for the "Scheduler" role against the "/" collection for the "docker-datacenter" organization does not exist in the output. If it does, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235796`

### Rule: The Create repository on push option in Docker Trusted Registry (DTR) must be disabled in Docker Enterprise.

**Rule ID:** `SV-235796r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of Universal Control Plane (UCP) and DTR and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the DTR component of Docker Enterprise. Verify that the "Create repository on push" option is disabled in DTR: via UI: As a Docker EE Admin, navigate to "System" | "General" in the DTR management console. Verify that the "Create repository on push" slider is turned off. via CLI: Linux (requires curl and jq): AUTHTOKEN=$(curl -sk -u <username>:<password> "https://[dtr_url]/auth/token" | jq -r .token) curl -k -H "Authorization: Bearer $AUTHTOKEN"" -X GET ""https://[dtr_url]/api/v0/meta/settings" Look for the "createRepositoryOnPush" field in the output and verify that it is set to "false". If it is not, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235797`

### Rule: Periodic data usage and analytics reporting in Universal Control Plane (UCP) must be disabled in Docker Enterprise.

**Rule ID:** `SV-235797r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of UCP and Docker Trusted Registry (DTR) and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Verify that usage and API analytics tracking is disabled in UCP: via UI: As a Docker EE Admin, navigate to "Admin Settings" | "Usage" in the UCP management console. Verify that the "Enable hourly usage reporting" and "Enable API and UI tracking" options are both unchecked. If either box is checked, this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands on a machine that can communicate with the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "disable_usageinfo" and "disable_tracking" entries under the "[tracking_configuration]" section in the output, and verify that they are both set to "true". If they are not, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235798`

### Rule: Periodic data usage and analytics reporting in Docker Trusted Registry (DTR) must be disabled in Docker Enterprise.

**Rule ID:** `SV-235798r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Docker Enterprise includes the following capabilities that are considered non-essential: *NOTE: disabling these capabilities negatively affects the operation of Universal Control Plane (UCP) and DTR and should be disregarded when UCP and DTR are installed. The security capabilities provided by UCP and DTR offset any potential vulnerabilities associated with not disabling these essential capabilities the Engine provides. (Docker Engine - Enterprise: Standalone) - The majority of these items were originally identified as part of the CIS Docker Benchmark, which as of the CIS Docker Benchmark v1.2.0, are still applicable to Docker Engine - Enterprise 18.09 - inter-container communication (icc)* (CIS Docker Benchmark Recommendation 2.1) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - userland proxy for loopback traffic* (CIS Docker Benchmark Recommendation 2.15) - experimental features (CIS Docker Benchmark Recommendation 2.17) - Swarm Mode (CIS Docker Benchmark Recommendation 7.1) (Docker Engine - Enterprise: As part of a UCP cluster) - insecure registry communication (CIS Docker Benchmark Recommendation 2.4) - AUFS storage driver (applicable on Linux only) (CIS Docker Benchmark Recommendation 2.5) - listening on the TCP Daemon socket - experimental features (CIS Docker Benchmark Recommendation 2.17) (UCP) - Managed user database - self-signed certificates - periodic usage reporting and API tracking - allow users and administrators to schedule containers on all nodes, including UCP managers and DTR nodes (DTR) - periodic data usage/analytics reporting - create repository on push - self-signed certificates</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the DTR component of Docker Enterprise. Verify that usage and API analytics tracking is disabled in DTR: via UI: As a Docker EE Admin, navigate to "System" | "General" in the DTR management console. Verify that the "Send data" option is disabled. via CLI: Linux (requires curl and jq): AUTHTOKEN=$(curl -sk -u <username>:<password> "https://[dtr_url]/auth/token" | jq -r .token) curl -k -H "Authorization: Bearer $AUTHTOKEN"" -X GET ""https://[dtr_url]/api/v0/meta/settings" Look for the "reportAnalytics" field in the output and verify that it is set to "false". If it is not, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235799`

### Rule: An appropriate AppArmor profile must be enabled on Ubuntu systems for Docker Enterprise.

**Rule ID:** `SV-235799r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>AppArmor protects the Ubuntu OS and applications from various threats by enforcing security policy which is also known as AppArmor profile. The user can create their own AppArmor profile for containers or use the Docker's default AppArmor profile. This would enforce security policies on the containers as defined in the profile. By default, docker-default AppArmor profile is applied for running containers and this profile can be found at /etc/apparmor.d/docker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on the Ubuntu host operating system and should be executed on all nodes in a Docker Enterprise cluster. Verify that all running containers include a valid AppArmor profile: via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: AppArmorProfile={{ .AppArmorProfile }}' Verify that all containers include a valid AppArmor Profile in the output. If they do not, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235800`

### Rule: SELinux security options must be set on Red Hat or CentOS systems for Docker Enterprise.

**Rule ID:** `SV-235800r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SELinux provides a Mandatory Access Control (MAC) system on RHEL and CentOS that greatly augments the default Discretionary Access Control (DAC) model. The user can thus add an extra layer of safety by enabling SELinux on the RHEL or CentOS host. By default, no SELinux security options are applied on containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on either the Red Hat Enterprise Linux or CentOS host operating systems where SELinux is in use and should be executed on all nodes in a Docker Enterprise cluster. Verify that the appropriate security options are configured for all running containers: via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Name }}: SecurityOpt={{ .HostConfig.SecurityOpt }}' | grep -iv "ucp\|kube\|dtr" If SecurityOpt=[label=disable], then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235801`

### Rule: Linux Kernel capabilities must be restricted within containers as defined in the System Security Plan (SSP) for Docker Enterprise.

**Rule ID:** `SV-235801r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, Docker starts containers with a restricted set of Linux Kernel Capabilities. It means that any process may be granted the required capabilities instead of root access. Using Linux Kernel Capabilities, the processes do not have to run as root for almost all the specific areas where root privileges are usually needed. Docker supports the addition and removal of capabilities, allowing the use of a non-default profile. This may make Docker more secure through capability removal, or less secure through the addition of capabilities. It is thus recommended to remove all capabilities except those explicitly required for the user's container process. By default, below capabilities are available for Linux containers: AUDIT_WRITE CHOWN DAC_OVERRIDE FOWNER FSETID KILL MKNOD NET_BIND_SERVICE NET_RAW SETFCAP SETGID SETPCAP SETUID SYS_CHROOT</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Verify that the added and dropped Linux Kernel Capabilities are in line with the ones needed for container processes for each container instance as defined in the SSP. via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: CapAdd={{ .HostConfig.CapAdd }} CapDrop={{ .HostConfig.CapDrop }}' If Linux Kernel Capabilities exceed what is defined in the SSP, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235802`

### Rule: Privileged Linux containers must not be used for Docker Enterprise.

**Rule ID:** `SV-235802r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using the --privileged flag gives all Linux Kernel Capabilities to the container thus overwriting the --cap-add and --cap-drop flags. Ensure that it is not used. The --privileged flag gives all capabilities to the container, and it also lifts all the limitations enforced by the device cgroup controller. In other words, the container can then do almost everything that the host can do. This flag exists to allow special use-cases, like running Docker within Docker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Verify that no containers are running with the --privileged flag. The --privileged flag provides full kernel capabilities. Capabilities must be specified in the System Security Plan (SSP) rather than allowing full privileges. via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | grep -iv "ucp\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: Privileged={{ .HostConfig.Privileged }}' Verify in the output that no containers are running with the --privileged flag. If there are, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235803`

### Rule: SSH must not run within Linux containers for Docker Enterprise.

**Rule ID:** `SV-235803r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH server should not be running within the container. The user should instead use Universal Control Plane (UCP) to console in to running containers. Running SSH within the container increases the complexity of security management by making it: - Difficult to manage access policies and security compliance for SSH server - Difficult to manage keys and passwords across various containers - Difficult to manage security upgrades for SSH server - It is possible to have shell access to a container without using SSH, the needlessly increasing the complexity of security management should be avoided By default, SSH server is not running inside the container. Only one process per container is allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Verify that no running containers have a process for SSH server. via CLI: for i in $(docker ps -qa); do echo $i; docker exec $i ps -el | grep -i sshd;done Container not running errors are not a finding. If running containers have a process for SSH server, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235804`

### Rule: Only required ports must be open on the containers in Docker Enterprise.

**Rule ID:** `SV-235804r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Dockerfile for a container image defines the ports to be opened by default on a container instance. The list of ports may or may not be relevant to the application running within the container. A container can be run just with the ports defined in the Dockerfile for its image or can be arbitrarily passed run time parameters to open a list of ports. Additionally, over time, Dockerfile may undergo various changes and the list of exposed ports may or may not be relevant to the application running within the container. Opening unneeded ports increase the attack surface of the container and the containerized application. As a recommended practice, do not open unneeded ports. By default, all the ports that are listed in the Dockerfile under EXPOSE instruction for an image are opened when a container is run with -P or --publish-all flag.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that mapped ports are the ones that are needed by the containers. This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure that the ports mapped are the ones that are really needed for the container. If there are any mapped ports that aren't documented by the System Security Plan (SSP), then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235805`

### Rule: Docker Enterprise hosts network namespace must not be shared.

**Rule ID:** `SV-235805r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The networking mode on a container when set to --net=host, skips placing the container inside separate network stack. In essence, this choice tells Docker to not containerize the container's networking. This would network-wise mean that the container lives "outside" in the main Docker host and has full access to its network interfaces. This is potentially dangerous. It allows the container process to open low-numbered ports like any other root process. It also allows the container to access network services like D-bus on the Docker host. Thus, a container process can potentially do unexpected things such as shutting down the Docker host. Do not use this option. By default, container connects to Docker bridge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the host's network namespace is not shared. This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --all | grep -iv "ucp\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: NetworkMode={{ .HostConfig.NetworkMode }}' If the above command returns NetworkMode=host, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235806`

### Rule: Memory usage for all containers must be limited in Docker Enterprise.

**Rule ID:** `SV-235806r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, all containers on a Docker host share the resources equally. By using the resource management capabilities of Docker host, such as memory limit, the amount of memory that a container may consume can be controlled. By default, container can use all of the memory on the host. The user can use memory limit mechanism to prevent a denial of service arising from one container consuming all of the host’s resources such that other containers on the same host cannot perform their intended functions. Having no limit on memory can lead to issues where one container can easily make the whole system unstable, and as a result, unusable. By default, all containers on a Docker host share the resources equally. No memory limits are enforced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure memory limits are in place for all containers. This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Memory={{ .HostConfig.Memory }}' If the above command returns 0, it means the memory limits are not in place and this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235807`

### Rule: Docker Enterprise CPU priority must be set appropriately on all containers.

**Rule ID:** `SV-235807r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By default, all containers on a Docker host share the resources equally. By using the resource management capabilities of Docker host, such as CPU shares, the user control the host CPU resources that a container may consume. By default, CPU time is divided between containers equally. If it is desired, to control the CPU time amongst the container instances, use CPU sharing feature. CPU sharing allows to prioritize one container over the other and forbids the lower priority container to claim CPU resources more often. This ensures that the high priority containers are served better. If CPU shares are not properly set, the container process may have to starve if the resources on the host are not available. If the CPU resources on the host are free, CPU shares do not place any restrictions on the CPU that the container may use. By default, all containers on a Docker host share the resources equally. No CPU shares are enforced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure CPU shares are in place for all containers. This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: CpuShares={{ .HostConfig.CpuShares }}' If the above command returns 0 or 1024, it means the CPU shares are not in place and this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235808`

### Rule: All Docker Enterprise containers root filesystem must be mounted as read only.

**Rule ID:** `SV-235808r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The container's root filesystem should be treated as a 'golden image' by using Docker run's --read-only option. This prevents any writes to the container's root filesystem at container runtime and enforces the principle of immutable infrastructure. Enabling this option forces containers at runtime to explicitly define their data writing strategy to persist or not persist their data. This also reduces security attack vectors since the container instance's filesystem cannot be tampered with or written to unless it has explicit read-write permissions on its filesystem folder and directories. Enabling --read-only at container runtime may break some container OS packages if a data writing strategy is not defined. Define what the container's data should and should not persist at runtime to determine which recommendation procedure to utilize. Example: - Enable use --tmpfs for temporary file writes to /tmp - Use Docker shared data volumes for persistent data writes By default, a container will have its root filesystem writable allowing all container processes to write files owned by the container's runtime user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure all containers' root filesystem is mounted as read only. This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs -L 1 docker inspect --format '{{ .Id }}: ReadonlyRootfs={{ .HostConfig.ReadonlyRootfs }}' If ReadonlyRootfs=false, it means the container's root filesystem is writable and this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235809`

### Rule: Docker Enterprise host devices must not be directly exposed to containers.

**Rule ID:** `SV-235809r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Host devices can be directly exposed to containers at runtime. Do not directly expose host devices to containers especially for containers that are not trusted. The --device option exposes the host devices to the containers and consequently, the containers can directly access such host devices. Do not require the container to run in privileged mode to access and manipulate the host devices. By default, the container will be able to read, write and mknod these devices. Additionally, it is possible for containers to remove block devices from the host. Hence, do not expose host devices to containers directly. If at all, expose the host device to a container, use the sharing permissions appropriately: r - read only w - writable m - mknod allowed The user would not be able to use the host devices directly within the containers. By default, no host devices are exposed to containers. If the user does not provide sharing permissions and choose to expose a host device to a container, the host device would be exposed with read, write, and mknod permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure host devices are not directly exposed to containers. Verify that the host device needs to be accessed from within the container and the permissions required are correctly set. This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Devices={{ .HostConfig.Devices }}' The above command lists out each device with below information: - CgroupPermissions - For example, rwm - PathInContainer - Device path within the container - PathOnHost - Device path on the host If Devices=[], or Devices=<no value>, this is not a finding. If Devices are listed and the host device is not documented and approved in the System Security Plan (SSP), this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235810`

### Rule: Mount propagation mode must not set to shared in Docker Enterprise.

**Rule ID:** `SV-235810r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mount propagation mode allows mounting volumes in shared, slave or private mode on a container. Do not use shared mount propagation mode until needed. A shared mount is replicated at all mounts and the changes made at any mount point are propagated to all mounts. Mounting a volume in shared mode does not restrict any other container to mount and make changes to that volume. This unintended volume changes could potentially impact data hosted on the mounted volume. Do not set mount propagation mode to shared until needed. By default, the container mounts are private.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure mount propagation mode is not set to shared or rshared. This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --all | grep -iv "ucp\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: Propagation={{range $mnt := .Mounts}} {{json $mnt.Propagation}} {{end}}' If Propagation=shared or Propagation-rshared, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235811`

### Rule: The Docker Enterprise hosts UTS namespace must not be shared.

**Rule ID:** `SV-235811r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>UTS namespaces provide isolation of two system identifiers: the hostname and the NIS domain name. It is used for setting the hostname and the domain that is visible to running processes in that namespace. Processes running within containers do not typically require to know hostname and domain name. Hence, the namespace should not be shared with the host. Sharing the UTS namespace with the host provides full permission to the container to change the hostname of the host. This must not be allowed. By default, all containers have the UTS namespace enabled and host UTS namespace is not shared with any container.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Ensure the host's UTS namespace is not shared. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: UTSMode={{ .HostConfig.UTSMode }}' If the above command returns host, it means the host UTS namespace is shared with the container and this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235812`

### Rule: The Docker Enterprise default seccomp profile must not be disabled.

**Rule ID:** `SV-235812r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Seccomp filtering provides a means for a process to specify a filter for incoming system calls. The default Docker seccomp profile works on whitelist basis and allows 311 system calls blocking all others. It should not be disabled unless it hinders the container application usage. A large number of system calls are exposed to every userland process with many of them going unused for the entire lifetime of the process. Most of the applications do not need all the system calls and thus benefit by having a reduced set of available system calls. The reduced set of system calls reduces the total kernel surface exposed to the application and thus improvises application security. The default seccomp profile blocks syscalls, regardless of --cap-add passed to the container. Create a custom seccomp profile in such cases. Disable the default seccomp profile by passing --security-opt=seccomp:unconfined on docker run. When running a container, it uses the default profile unless it is overridden with the --security-opt option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Ensure the default seccomp profile is not disabled. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --all | grep -iv "ucp\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: SecurityOpt={{ .HostConfig.SecurityOpt }}' If seccomp:=unconfined, then the container is running without any seccomp profiles and this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235813`

### Rule: Docker Enterprise exec commands must not be used with privileged option.

**Rule ID:** `SV-235813r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Do not use docker exec with --privileged option. Using --privileged option in docker exec gives extended Linux capabilities to the command. Do not run docker exec with the --privileged option, especially when running containers with dropped capabilities or with enhanced restrictions. By default, docker exec command runs without --privileged option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Ensure the default seccomp profile is not disabled, if applicable. via CLI: Linux: As a trusted user on the host operating system, use the below command to filter out docker exec commands that used --privileged option. sudo ausearch -k docker | grep exec | grep privileged If there are any in the output, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235814`

### Rule: Docker Enterprise exec commands must not be used with the user option.

**Rule ID:** `SV-235814r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Do not docker exec with --user option. Using --user option in docker exec executes the command within the container as that user. Do not run docker exec with the --user option , especially when running containers with dropped capabilities or with enhanced restrictions. For example, suppose the container is running as tomcat user (or any other non-root user), it would be possible to run a command through docker exec as rootwith --user=root option. By default, docker exec command runs without --user option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Ensure docker exec commands are not used with the user option. via CLI: Linux: As a trusted user on the host operating system, use the below command to filter out docker exec commands that used --privileged option. sudo ausearch -k docker | grep exec | grep user If there are any in the output, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235815`

### Rule: cgroup usage must be confirmed in Docker Enterprise.

**Rule ID:** `SV-235815r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is possible to attach to a particular cgroup on container run. Confirming cgroup usage would ensure that containers are running under defined cgroups. System administrators typically define cgroups under which containers are supposed to run. Even if cgroups are not explicitly defined by the system administrators, containers run under docker cgroup by default. At run-time, it is possible to attach to a different cgroup other than the one that was expected to be used. This usage should be monitored and confirmed. By attaching to a different cgroup than the one that is expected, excess permissions and resources might be granted to the container and thus, can prove to be unsafe. By default, containers run under docker cgroup.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Ensure cgroup usage is confirmed. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: CgroupParent={{ .HostConfig.CgroupParent }}' If the cgroup is blank, the container is running under default docker cgroup. If the containers are found to be running under cgroup other than the one that is documented in the System Security Plan (SSP), then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235816`

### Rule: All Docker Enterprise containers must be restricted from acquiring additional privileges.

**Rule ID:** `SV-235816r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Restrict the container from acquiring additional privileges via suid or sgid bits. A process can set the no_new_priv bit in the kernel. It persists across fork, clone, and execve. The no_new_priv bit ensures that the process or its children processes do not gain any additional privileges via suid or sgid bits. This way a lot of dangerous operations become a lot less dangerous because there is no possibility of subverting privileged binaries. no_new_priv prevents LSMs like SELinux from transitioning to process labels that have access not allowed to the current process. By default, new privileges are not restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Ensure all containers are restricted from acquiring additional privileges. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs -L 1 docker inspect --format '{{ .Id }}: SecurityOpt={{ .HostConfig.SecurityOpt }}' The above command returns the security options currently configured for the running containers, if 'SecurityOpt=' setting does not include the 'no-new-privileges' flag, this is a finding."

## Group: SRG-APP-000141

**Group ID:** `V-235817`

### Rule: The Docker Enterprise hosts user namespace must not be shared.

**Rule ID:** `SV-235817r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Do not share the host's user namespaces with the containers. User namespaces ensure that a root process inside the container will be mapped to a non-root process outside the container. Sharing the user namespaces of the host with the container thus does not isolate users on the host with users on the containers. By default, the host user namespace is shared with the containers until user namespace support is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system and should be executed on all nodes in a Docker Enterprise cluster. Ensure PIDs cgroup limit is used. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: UsernsMode={{ .HostConfig.UsernsMode }}' Ensure that it does not return any value for UsernsMode. If it returns a value of host, it means the host user namespace is shared with the containers and this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235818`

### Rule: The Docker Enterprise socket must not be mounted inside any containers.

**Rule ID:** `SV-235818r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The docker socket docker.sock (Linux) and \\.\pipe\docker_engine (Windows) should not be mounted inside a container, with the exception case being during the installation of Universal Control Plane (UCP) component of Docker Enterprise as it is required for install. If the docker socket is mounted inside a container it would allow processes running within the container to execute docker commands which effectively allows for full control of the host. By default, docker.sock (linux) and \\.\pipe\docker_engine (windows) is not mounted inside containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: As a Docker EE Admin, execute the following command using a UCP client bundle: docker ps --all | grep -iv "ucp\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}' | grep -i "docker.sock\|docker_engine" If the Docker socket is mounted inside containers, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-235819`

### Rule: Docker Enterprise privileged ports must not be mapped within containers.

**Rule ID:** `SV-235819r960966_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The TCP/IP port numbers below 1024 are considered privileged ports. Normal users and processes are not allowed to use them for various security reasons. Docker allows a container port to be mapped to a privileged port. By default, if the user does not specifically declare the container port to host port mapping, Docker automatically and correctly maps the container port to one available in 49153-65535 block on the host. But, Docker allows a container port to be mapped to a privileged port on the host if the user explicitly declared it. This is so because containers are executed with NET_BIND_SERVICE Linux kernel capability that does not restrict the privileged port mapping. The privileged ports receive and transmit various sensitive and privileged data. Allowing containers to use them can bring serious implications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check should be executed on all nodes in a Docker Enterprise cluster. Verify that no running containers are mapping host port numbers below 1024. via CLI: Linux: Execute the following command as a trusted user on the host operating system: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure that container ports are not mapped to host port numbers below 1024. If they are, then this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-235820`

### Rule: Docker Enterprise incoming container traffic must be bound to a specific host interface.

**Rule ID:** `SV-235820r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, Docker containers can make connections to the outside world, but the outside world cannot connect to containers. Each outgoing connection will appear to originate from one of the host machine's own IP addresses. Only allow container services to be contacted through a specific external interface on the host machine. If there are multiple network interfaces on the host machine, the container can accept connections on the exposed ports on any network interface. This might not be desired and may not be secured. Many times, a particular interface is exposed externally and services such as intrusion detection, intrusion prevention, firewall, load balancing, etc. are run on those interfaces to screen incoming public traffic. Hence, do not accept incoming connections on any interface. Only allow incoming connections from a particular external interface. By default, Docker exposes the container ports on 0.0.0.0, the wildcard IP address that will match any possible incoming network interface on the host machine.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure incoming container traffic is bound to a specific host interface. This check should be executed on all nodes in a Docker Enterprise cluster. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle to list all the running instances of containers and their port mapping: docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure that the exposed container ports are tied to a particular interface and not to the wildcard IP address - 0.0.0.0. If they are, then this is a finding. For example, if the above command returns as below the container can accept connections on any host interface on the specified port 49153, this is a finding. Ports=map[443/TCP:<nil> 80/TCP:[map[HostPort:49153 HostIp:0.0.0.0]]] However, if the exposed port is tied to a particular interface on the host as below, then this recommendation is configured as desired and is compliant. Ports=map[443/TCP:<nil> 80/TCP:[map[HostIp:10.2.3.4 HostPort:49153]]]

## Group: SRG-APP-000149

**Group ID:** `V-235821`

### Rule: SAML integration must be enabled in Docker Enterprise.

**Rule ID:** `SV-235821r960972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both the Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise leverage the same authentication and authorization backplane known as eNZi. The eNZi backplane includes its own managed user database, and also allows for LDAP and SAML integration in UCP and DTR. To meet the requirements of this control, configure LDAP and SAML integration. Satisfies: SRG-APP-000149, SRG-APP-000150, SRG-APP-000151, SRG-APP-000152, SRG-APP-000153, SRG-APP-000391, SRG-APP-000392, SRG-APP-000402, SRG-APP-000403, SRG-APP-000404, SRG-APP-000405</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SAML integration is enabled and properly configured in the UCP Admin Settings. via UI: In the UCP web console, navigate to "Admin Settings" | "Authentication & Authorization" and verify "SAML Enabled" is set to "Yes" and that it is properly configured. If SAML authentication is not enabled, this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands from a machine with connectivity to the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Verify that the "samlEnabled" entry under the "[auth]" section is set to "true". If the "samlEnabled" entry under the "[auth]" section is not set to "true", then this is a finding.

## Group: SRG-APP-000175

**Group ID:** `V-235822`

### Rule: The certificate chain used by Universal Control Plane (UCP) client bundles must match what is defined in the System Security Plan (SSP) in Docker Enterprise.

**Rule ID:** `SV-235822r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both the UCP and Docker Trusted Registry (DTR) components of Docker Enterprise leverage the same authentication and authorization backplane known as eNZi. UCP has the ability to use external certificates or internal self-signed. In the case of self-signed UCP includes a certificate authority which is used to sign client bundles and to authenticate users via the eNZi backplane. With an external certificate authority (CA) users will use their existing x509 certs. The external CA will be added in an administrative function and will dictate the root CA for the user's chain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
via CLI: Execute the following command from within the directory in which the UCP client bundle is located. (Linux) openssl x509 -noout -text -in cert.pem |grep "Subject\|Issuer" Verify that the Subject and Issuer output matches that which is defined in the SSP. If the Subject and Issuer do not match what is documented in the SSP, this is a finding.

## Group: SRG-APP-000176

**Group ID:** `V-235823`

### Rule: Docker Enterprise Swarm manager must be run in auto-lock mode.

**Rule ID:** `SV-235823r961041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Run Docker swarm manager in auto-lock mode. When Docker restarts, both the TLS key used to encrypt communication among swarm nodes, and the key used to encrypt and decrypt Raft logs on disk, are loaded into each manager node's memory. Protect the mutual TLS encryption key and the key used to encrypt and decrypt Raft logs at rest. This protection could be enabled by initializing swarm with --autolock flag. With --autolock enabled, when Docker restarts, unlock the swarm first, using a key encryption key generated by Docker when the swarm was initialized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure swarm manager is run in auto-lock mode. via CLI: Linux: As a Docker EE Admin, follow the steps below using a Universal Control Plane (UCP) client bundle: Run the below command. If it outputs the key, it means swarm was initialized with the --autolock flag. docker swarm unlock-key If the output is no unlock key is set, it means that swarm was NOT initialized with the --autolock flag and this is a finding.

## Group: SRG-APP-000176

**Group ID:** `V-235824`

### Rule: Docker Enterprise secret management commands must be used for managing secrets in a Swarm cluster.

**Rule ID:** `SV-235824r961041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use Docker's in-built secret management commands for managing sensitive data that which can be stored in key/value pairs. Examples include API tokens, database connection strings and credentials, SSL certificates, and the like.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure Docker's secret management commands are used for managing secrets in a Swarm cluster. Refer to the System Security Plan (SSP) and verify that it includes documented processes for using Docker secrets commands to manage sensitive data that can be stored in key/value pairs. Examples include API tokens, database connection strings and credentials, SSL certificates, and the like. If the SSP does not have this documented, then this is a finding.

## Group: SRG-APP-000190

**Group ID:** `V-235825`

### Rule: The Lifetime Minutes and Renewal Threshold Minutes Login Session Controls must be set to 10 and 0 respectively in Docker Enterprise.

**Rule ID:** `SV-235825r961068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) component of Docker Enterprise includes a built-in access authorization mechanism called eNZi which can be integrated with an LDAP server and subsequently terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for user sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity, except to fulfill documented and validated mission requirements. The lifetime minutes login session control is configured with a default of 60 minutes (1 hour) and the renewal threshold minutes is configured with a default of 20 minutes. For reference, the lifetime login session control in UCP specifies the initial lifetime (in minutes) of a session from the moment it is generated. The renewal threshold setting indicates a period of time (in minutes) before the expiration of a session where, if used, a session will be extended by the current configured lifetime from then. This value cannot be greater than the configured lifetime. A value equal to the lifetime means that sessions will be extended with every use. A value of zero indicates that sessions should never be extended but this may result in unexpectedly being logged out if the session expires while performing a series of actions in the UI. This configuration only applies to both the UCP and Docker Trusted Registry (DTR) management consoles and not when connecting via the command line. When connecting via the command line, this control is not applicable. It's important to note that the notion of a session varies depending on how one is connecting to a UCP cluster or DTR. In all of these cases, there is no specific session termination capability. Either the session times out, the user's client bundle has expired, or a user explicitly logs out. This has been outlined as follows: (UCP and DTR UIs) When connecting to a UCP cluster or DTR via the web console, a user's session is active until any of the following conditions is met: - the session expires based on the values configured for "Lifetime Minutes" and "Renewal Threshold Minutes" in the UCP Admin Settings - the user explicitly clicks the "Sign Out" button (UCP and DTR CLIs) When connecting to a UCP cluster or DTR via the command line using a client bundle, a user's session is active until any of the following conditions is met: - the certificate contained within a user's client bundle hasn't expired - the public key in the certificate contained with a user's client bundle is no long associated with that user (i.e. a client bundle is revoked from within the UCP user management options) - the user's account is no longer active (either explicitly disabled from within the UCP user management options or at the LDAP server) - the user's password is changed Satisfies: SRG-APP-000190, SRG-APP-000002, SRG-APP-000003, SRG-APP-000295, SRG-APP-000389, SRG-APP-000400</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "Lifetime Minutes" and "Renewal Threshold Minutes" Login Session Controls in the Universal Control Plane (UCP) Admin Settings to "10" and "0" respectively. via UI: In the UCP web console, navigate to "Admin Settings" | "Authentication & Authorization" and verify the "Lifetime Minutes" field is set to "10" and "Renewal Threshold Minutes" field is set to "0". If they are not, then this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands from a machine with connectivity to the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "lifetime_minutes" and "renewal_threshold_minutes" entries under the "[auth.sessions]" section in the output, and verify that the "lifetime_minutes" field is set to "10" and the "renewal_threshold_minutes" field is set to "0". If they are not, then this is a finding.

## Group: SRG-APP-000231

**Group ID:** `V-235826`

### Rule: Docker Secrets must be used to store configuration files and small amounts of user-generated data (up to 500 kb in size) in Docker Enterprise.

**Rule ID:** `SV-235826r961128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By leveraging Docker Secrets or Kubernetes secrets to store configuration files and small amounts of user-generated data (up to 500 kb in size), the data is encrypted at rest by the Engine's FIPS-validated cryptography.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan (SSP) and identify applications that leverage configuration files and/or small amounts of user-generated data, ensure that data is stored in Docker Secrets or Kubernetes Secrets. Using a Universal Control Plane (UCP) client bundle, verify that secrets are in use by executing the following commands: docker secret ls Confirm containerized applications identified in SSP as utilizing Docker secrets have a corresponding secret configured. If the SSP requires Docker secrets be used but the containerized application does not use Docker secrets, this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-235827`

### Rule: Docker Enterprise container health must be checked at runtime.

**Rule ID:** `SV-235827r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the container image does not have an HEALTHCHECK instruction defined, use --health-cmd parameter at container runtime for checking container health. One of the important security triads is availability. If the container image being used does not have a pre-defined HEALTHCHECK instruction, use the --health-cmd parameter to check container health at runtime. Based on the reported health status, take necessary actions. By default, health checks are not done at container runtime.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure container health is checked at runtime. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: Run the below command and ensure that all the containers are reporting health status: docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Health={{ .State.Health.Status }}' If Health does not = "Healthy", this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-235828`

### Rule: PIDs cgroup limits must be used in Docker Enterprise.

**Rule ID:** `SV-235828r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use --pids-limit flag at container runtime. Attackers could launch a fork bomb with a single command inside the container. This fork bomb can crash the entire system and requires a restart of the host to make the system functional again. PIDs cgroup --pids-limit will prevent this kind of attacks by restricting the number of forks that can happen inside a container at a given time. The Default value for --pids-limit is 0 which means there is no restriction on the number of forks. Also, note that PIDs cgroup limit works only for the kernel versions 4.3+.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system. Ensure PIDs cgroup limit is used. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: PidsLimit={{ .HostConfig.PidsLimit }}' Ensure that PidsLimit is not set to 0 or -1. A PidsLimit of 0 or -1 means that any number of processes can be forked inside the container concurrently. If the PidsLimit is set to either 0 or -1 then this is a finding.

## Group: SRG-APP-000295

**Group ID:** `V-235829`

### Rule: The Docker Enterprise per user limit login session control must be set per the requirements in the System Security Plan (SSP).

**Rule ID:** `SV-235829r961221_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) component of Docker Enterprise includes a built-in access authorization mechanism called eNZi which can be integrated with an LDAP server and allows for automatic user session termination after organization-defined conditions or trigger events requiring session disconnect. The lifetime minutes login session control is configured with a default of 60 minutes (1 hour) and the renewal threshold minutes is configured with a default of 20 minutes. For reference, the lifetime login session control in UCP specifies the initial lifetime (in minutes) of a session from the moment it is generated. The renewal threshold setting indicates a period of time (in minutes) before the expiration of a session where, if used, a session will be extended by the current configured lifetime from then. This value cannot be greater than the configured lifetime. A value equal to the lifetime means that sessions will be extended with every use. A value of zero indicates that sessions should never be extended but this may result in unexpectedly being logged out if the session expires while performing a series of actions in the UI. This configuration only applies to both the UCP and Docker Trusted Registry (DTR) management consoles and not when connecting via the command line. When connecting via the command line, this control is not applicable. It's important to note that the notion of a session varies depending on how one is connecting to a UCP cluster or DTR. In all of these cases, there is no specific session termination capability. Either the session times out, the user's client bundle has expired, or a user explicitly logs out. This has been outlined as follows: (UCP and DTR UIs) When connecting to a UCP cluster or DTR via the web console, a user's session is active until any of the following conditions is met: - the session expires based on the values configured for "Lifetime Minutes" and "Renewal Threshold Minutes" in the UCP Admin Settings - the user explicitly clicks the "Sign Out" button (UCP and DTR CLIs) When connecting to a UCP cluster or DTR via the command line using a client bundle, a user's session is active until any of the following conditions is met: - the certificate contained within a user's client bundle hasn't expired - the public key in the certificate contained with a user's client bundle is no long associated with that user (i.e. a client bundle is revoked from within the UCP user management options) - the user's account is no longer active (either explicitly disabled from within the UCP user management options or at the LDAP server) - the user's password is changed *NOTE: Docker Engine - Enterprise, by itself, does not meet the requirements of this control. If the intent is to use Docker in a model consistent with the access control policies as required by this control, obtain and properly configure the UCP component of Docker Enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the "Per User Limit" Login Session Control in the UCP Admin Settings are set according to the System Security Plan but not set to "0". via UI: In the UCP web console, navigate to "Admin Settings" | "Authentication & Authorization" and verify the "Per User Limit" field is set according to the settings described in the SSP. If the per user limit setting is not set to the value defined in the SSP or is set to "0", this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands from a machine with connectivity to the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "per_user_limit" entry under the "[auth.sessions]" section in the output, and verify that it is set according to the requirements of this control. If the "per_user_limit" entry under the "[auth.sessions]" section in the output is not set according to the value defined in the SSP, or if the per user limit is set to "0", then this is a finding.

## Group: SRG-APP-000342

**Group ID:** `V-235830`

### Rule: Docker Enterprise images must be built with the USER instruction to prevent containers from running as root.

**Rule ID:** `SV-235830r961359_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both the Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise leverage the same authentication and authorization backplane known as eNZi. The eNZi backplane includes its own managed user database, and also allows for LDAP integration in UCP and DTR. To meet the requirements of this control, configure LDAP integration. Apply an applicable set of role-based access control (RBAC) policies using the built-in capabilities provided by UCP in order to prevent organization-defined software from executing at higher privilege levels than users executing the software. By default, Docker images that are built without the USER instruction will be run as containers as root. Therefore, it is imperative that container images include the USER instruction and that the referenced UID/GID has been defined in the base image or previous instruction set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all containers are running as non-root users. via CLI: As a Docker EE admin, execute the following command using a client bundle: docker ps -q -a | xargs docker inspect --format '{{ .Id }}: User={{ .Config.User }}' Ensure that a non-admin username or user ID is returned for all containers in the output. If User is 0, root or undefined, this is a finding.

## Group: SRG-APP-000343

**Group ID:** `V-235831`

### Rule: An appropriate Docker Engine - Enterprise log driver plugin must be configured to collect audit events from Universal Control Plane (UCP) and Docker Trusted Registry (DTR).

**Rule ID:** `SV-235831r961362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UCP and DTR components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. All audit logs generated by UCP and DTR can be forwarded to a remote log aggregation system by configuring an appropriate log driver plugin on all Docker Engine - Enterprise nodes in a cluster. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise. Satisfies: SRG-APP-000343, SRG-APP-000381, SRG-APP-000492, SRG-APP-000493, SRG-APP-000494, SRG-APP-000495, SRG-APP-000496, SRG-APP-000497, SRG-APP-000498, SRG-APP-000499, SRG-APP-000501, SRG-APP-000502, SRG-APP-000503, SRG-APP-000504, SRG-APP-000505, SRG-APP-000506, SRG-APP-000507, SRG-APP-000508, SRG-APP-000509, SRG-APP-000510, SRG-APP-000500</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
via CLI: Linux: Execute the following commands as a trusted user on the host operating system: cat /etc/docker/daemon.json | grep -i log-driver Verify that the "log-driver" property is set to one of the following: "syslog", "awslogs", "splunk", "gcplogs", "logentries" or "<plugin>" (where <plugin> is the naming of a third-party Docker logging driver plugin). If "log-driver" is not set, then this is a finding.

## Group: SRG-APP-000357

**Group ID:** `V-235832`

### Rule: The Docker Enterprise max-size and max-file json-file drivers logging options in the daemon.json configuration file must be configured to allocate audit record storage capacity for Universal Control Plane (UCP) and Docker Trusted Registry (DTR) per the requirements set forth by the System Security Plan (SSP).

**Rule ID:** `SV-235832r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the UCP and DTR components of Docker Enterprise leverage the "json-file" Engine logging driver. This driver has configurable "max-size" and "max-file" options which are applicable in the context of this control. The "max-size" option defines the maximum size of the log before it is rolled. By default it is set to "unlimited" and is never rolled. The "max-file" option defines the maximum number of log files that can be present whereby if rolling the logs creates excess files, the oldest file is removed. This setting is only effective when "max-size" is also set. By default, "max-file" is set to "1". The Docker Engine - Enterprise audit logs are stored in default locations according to the chart on this site https://docs.docker.com/config/daemon/#read-the-logs. For the Engine's daemon logs, allocate sufficient storage for the default log locations on the underlying host operating system per the requirements set forth by the SSP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the Docker Engine - Enterprise component of Docker Enterprise. via CLI: Linux: Execute the following commands as a trusted user on the host operating system: cat /etc/docker/daemon.json Verify that the "log-opts" object includes the "max-size" and "max-file" properties and that they are set according to requirements specified in the SSP. If they are not configured according to values defined in the SSP, this is a finding.

## Group: SRG-APP-000358

**Group ID:** `V-235833`

### Rule: All Docker Engine - Enterprise nodes must be configured with a log driver plugin that sends logs to a remote log aggregation system (SIEM).

**Rule ID:** `SV-235833r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. All audit logs generated by UCP and DTR can be forwarded to a remote log aggregation system by configuring an appropriate log driver plugin on all Docker Engine - Enterprise nodes in a cluster. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
via CLI: Linux: Execute the following commands as a trusted user on the host operating system: cat /etc/docker/daemon.json Verify that the "log-driver" property is set to one of the following: "syslog", "awslogs", "splunk", "gcplogs", "logentries" or "<plugin>" (where <plugin> is the naming of a third-party Docker logging driver plugin). Ask the sys admin to demonstrate how the login driver that is being used is configured to send log events to a log aggregation server or SIEM. If "log-driver" is not set and configured to send logs to an aggregation server or SIEM, then this is a finding.

## Group: SRG-APP-000359

**Group ID:** `V-235834`

### Rule: Log aggregation/SIEM systems must be configured to alarm when audit storage space for Docker Engine - Enterprise nodes exceed 75% usage.

**Rule ID:** `SV-235834r961398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. All audit logs generated by UCP and DTR can be forwarded to a remote log aggregation system by configuring an appropriate log driver plugin on all Docker Engine - Enterprise nodes in a cluster. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Work with the SIEM administrator to determine if an alert is configured to alarm when audit storage space for Docker Engine - Enterprise nodes exceed 75% usage. If there is no alert configured, this is a finding.

## Group: SRG-APP-000360

**Group ID:** `V-235835`

### Rule: Log aggregation/SIEM systems must be configured to notify SA and ISSO on Docker Engine - Enterprise audit failure events.

**Rule ID:** `SV-235835r961401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) and Docker Trusted Registry (DTR) components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. All audit logs generated by UCP and DTR can be forwarded to a remote log aggregation system by configuring an appropriate log driver plugin on all Docker Engine - Enterprise nodes in a cluster. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Work with the SIEM administrator to determine if an alert is configured to notify the SA and ISSO when audit failure events occur. If there is no alert configured, this is a finding.

## Group: SRG-APP-000377

**Group ID:** `V-235836`

### Rule: The Docker Enterprise log aggregation/SIEM systems must be configured to send an alert the ISSO/ISSM when unauthorized software is installed.

**Rule ID:** `SV-235836r961452_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A Docker image is analogous to software in the context of this control. All components of Docker Enterprise can be configured to send logs to a remote syslog server in order to meet the requirements of this control. Universal Control Plane (UCP) remote syslog configuration is done via the UCP configuration settings. Docker Trusted Registry (DTR) remote syslog configuration is done via an appropriate Docker Engine - Enterprise logging driver. The UCP and DTR components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Work with the SIEM administrator to determine if an alert is configured to notify the ISSO/ISSM when unauthorized software is installed on Docker nodes. If there is no alert configured, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-235837`

### Rule: Docker Enterprise network ports on all running containers must be limited to what is needed.

**Rule ID:** `SV-235837r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By itself, Docker Engine - Enterprise is configured by default to listen for API requests via a UNIX domain socket (or IPC socket) created at /var/run/docker.sock on supported Linux distributions and via a named pipe at npipe:////./pipe/docker_engine on Windows Server 2016 and newer. In this configuration, this control is not applicable. Docker Engine - Enterprise can also be configured to listen for API requests via additional socket types, including both TCP and FD (only on supported systemd-based Linux distributions). If configured to listen for API requests via the TCP socket type over TCP port 2376 and with the daemon flags and SSL certificates, then, at a minimum, TLS 1.2 is used for encryption; therefore this control is applicable and is inherently met in this configuration. If configured to listen for API requests via the TCP socket type, but without TLS verification and certifications, then the instance remains vulnerable and is not properly configured to meet the requirements of this control. If configured to listen for API requests via the fd socket type, then this control is not applicable. More information can be found at https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option. The TCP socket binding should be disabled when running Engine as part of a UCP cluster. A container can be run just with the ports defined in the Dockerfile for its image or can be arbitrarily passed run time parameters to open a list of ports. Additionally, over time, Dockerfiles may undergo various changes and the list of exposed ports may or may not be relevant to the application running within the container. Opening unneeded ports increase the attack surface of the container and the containerized application. Per the requirements set forth by the System Security Plan (SSP), ensure only needed ports are open on all running containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that only needed ports are open on all running containers. via CLI: As a Docker EE admin, execute the following command using a client bundle: docker ps -q | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure that the ports mapped are the ones really needed for the containers per the requirements set forth by the SSP. If ports are not documented and approved in the SSP, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-235838`

### Rule: Content Trust enforcement must be enabled in Universal Control Plane (UCP) in Docker Enterprise.

**Rule ID:** `SV-235838r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UCP and Docker Trusted Registry (DTR) components of Docker Enterprise can be used in concert to perform an integrity check of organization-defined software at startup. In the context of Docker Enterprise, software would be analogous to Docker images that have been pulled from trusted or untrusted sources. Docker Hub is the most common upstream endpoint for retrieving Docker images. However, only "Docker Certified" images on Docker Hub are considered trusted and come with SLAs and trusted signatures from their respective vendors. All other images from Docker Hub or other external registries must be carefully inspected and triaged prior to use. Docker Content Trust (DCT) provides for content integrity checking mechanisms on Docker images. DCT can be combined with LDAP, Docker Trusted Registry (DTR) and Universal Control Plane (UCP) to enforce image signatures from users/accounts in LDAP. Therefore, to meet the requirements of this control, it is imperative that UCP has LDAP integration enabled and that content trust enforcement is enabled and properly configured. An operational requirement of this control is that of the required use of an established continuous integration and deployment workflow that effectively dictates exactly what software is allowed to run on UCP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Check that UCP is configured to only run signed images by applicable Orgs and Teams. via UI: In the UCP web console, navigate to "Admin Settings" | "Docker Content Trust" and verify that "Run only signed images" is checked. Verify that the Orgs and Teams that images must be signed by in the dropdown that follows matches that of your organizational policies. If "Run only signed images" box is not checked, this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands on a machine that can communicate with the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "require_content_trust" entry under the "[trust_configuration]" section in the output, and verify that it is set to "true". If require_content_trust is not set to true, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-235839`

### Rule: Only trusted, signed images must be on Universal Control Plane (UCP) in Docker Enterprise.

**Rule ID:** `SV-235839r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UCP and Docker Trusted Registry (DTR) components of Docker Enterprise can be used in concert to perform an integrity check of organization-defined software at startup. In the context of Docker Enterprise, software would be analogous to Docker images that have been pulled from trusted or untrusted sources. Docker Hub is the most common upstream endpoint for retrieving Docker images. However, only "Docker Certified" images on Docker Hub are considered trusted and come with SLAs and trusted signatures from their respective vendors. All other images from Docker Hub or other external registries must be carefully inspected and triaged prior to use. Docker Content Trust (DCT) provides for content integrity checking mechanisms on Docker images. DCT can be combined with LDAP, DTR and UCP to enforce image signatures from users/accounts in LDAP. Therefore, to meet the requirements of this control, it is imperative that UCP has LDAP integration enabled and that content trust enforcement is enabled and properly configured. An operational requirement of this control is that of the required use of an established continuous integration and deployment workflow that effectively dictates exactly what software is allowed to run on UCP. Satisfies: SRG-APP-000386, SRG-APP-000480, SRG-APP-000484, SRG-APP-000485, SRG-APP-000475</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Verify that all images sitting on a UCP cluster are signed. via CLI: Linux: As a Docker EE Admin, execute the following commands using a client bundle: docker trust inspect $(docker images | awk '{print $1 ":" $2}') Verify that all image tags in the output have valid signatures. If the images are not signed, this is a finding.

## Group: SRG-APP-000414

**Group ID:** `V-235840`

### Rule: Vulnerability scanning must be enabled for all repositories in the Docker Trusted Registry (DTR) component of Docker Enterprise.

**Rule ID:** `SV-235840r961563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DTR can scan Docker images for vulnerabilities and this capability should be enabled to meet the requirements of this control. When enabled, for every Docker image that is pushed to DTR, a scan of each of the image layers is conducted. An analysis of all packages and compiled binaries is done for each image layer and if a package or binary is associated with a known vulnerability as identified by the MITRE CVE or NIST NVD databases, then it is flagged in DTR.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the DTR component of Docker Enterprise. Check image vulnerability scanning enabled for all repositories: via UI: As a Docker EE Admin, navigate to "System" | "Security" in the DTR management console. Verify that the "Enable Scanning" slider is turned on and that the vulnerability database has been successfully synced (online)/uploaded (offline). If "Enable Scanning" is tuned off or if the vulnerability database is not synced or uploaded, this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands from a machine with connectivity to the DTR management console: AUTHTOKEN=$(curl -sk -u <username>:<password> "https://[dtr_url]/auth/token" | jq -r .token) curl -k -H "Authorization: Bearer $AUTHTOKEN" -X GET "https://[dtr_url]/api/v0/imagescan/status" Verify that that the response is successful with HTTP Status Code 200, and look for the "lastDBUpdateFailed" and "lastVulnOverridesDBUpdateFailed" properties in the "Response body", and verify that are both "false". If they are both not "false", this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-235841`

### Rule: Universal Control Plane (UCP) must be integrated with a trusted certificate authority (CA) in Docker Enterprise.

**Rule ID:** `SV-235841r961596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both the UCP and Docker Trusted Registry (DTR) components of Docker Enterprise leverage the same authentication and authorization backplane known as eNZi. The eNZi backplane includes its own managed user database, and also allows for LDAP integration in UCP and DTR. To meet the requirements of this control, configure LDAP integration. UCP also includes two certificate authorities for establishing root of trust. One CA is used to sign client bundles and the other is used for TLS communication between UCP components and nodes. Both of these CAs should be integrated with an external, trusted CA. DTR should be integrated with this same external, trusted CA as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Check that UCP has been integrated with a trusted CA. via UI: In the UCP web console, navigate to "Admin Settings" | "Certificates" and click on the "Download UCP Server CA Certificate" link. Verify that the contents of the downloaded "ca.pem" file match that of the trusted CA certificate. If the certificate chain is not valid or does not match the trusted CA, this is a finding. via CLI: Linux: Execute the following command and verify the certificate chain in the output is valid and matches that of the trusted CA: echo "" | openssl s_client -connect [ucp_url]:443 | openssl x509 -noout -text If the certificate chain is not valid or does not match the trusted CA, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-235842`

### Rule: Docker Trusted Registry (DTR) must be integrated with a trusted certificate authority (CA) in Docker Enterprise.

**Rule ID:** `SV-235842r961596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both the Universal Control Plane (UCP) and DTR components of Docker Enterprise leverage the same authentication and authorization backplane known as eNZi. The eNZi backplane includes its own managed user database, and also allows for LDAP integration in UCP and DTR. To meet the requirements of this control, configure LDAP integration. UCP also includes two certificate authorities for establishing root of trust. One CA is used to sign client bundles and the other is used for TLS communication between UCP components and nodes. Both of these CAs should be integrated with an external, trusted CA. DTR should be integrated with this same external, trusted CA as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the DTR component of Docker Enterprise. Check that DTR has been integrated with a trusted CA. via UI: In the DTR web console, navigate to "System" | "General" and click on the "Show TLS settings" link in the "Domain & Proxies" section. Verify the certificate chain in "TLS Root CA" box is valid and matches that of the trusted CA. via CLI: Linux: Execute the following command and verify the certificate chain in the output is valid and matches that of the trusted CA: echo "" | openssl s_client -connect [dtr_url]:443 | openssl x509 -noout -text If the certificate chain is not valid or does not match the trusted CA, this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-235843`

### Rule: The on-failure container restart policy must be is set to 5 in Docker Enterprise.

**Rule ID:** `SV-235843r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using the --restart flag in docker run command, specify a restart policy for how a container should or should not be restarted on exit. Choose the on-failure restart policy and limit the restart attempts to 5. If indefinitely trying to start the container, it could possibly lead to a denial of service on the host. It could be an easy way to do a distributed denial of service attack especially if there are many containers on the same host. Additionally, ignoring the exit status of the container and always attempting to restart the container leads to non-investigation of the root cause behind containers getting terminated. If a container gets terminated, investigate on the reason behind it instead of just attempting to restart it indefinitely. Thus, it is recommended to use on-failure restart policy and limit it to maximum of 5 restart attempts. The container would attempt to restart only for 5 times. By default, containers are not configured with restart policies. Hence, containers do not attempt to restart of their own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure 'on-failure' container restart policy is set to 5. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --all | grep -iv "ucp\|kube\|dtr" | awk '{print $1}' | xargs docker inspect --format '{{ .Id }}: RestartPolicyName={{ .HostConfig.RestartPolicy.Name }} MaximumRetryCount={{ .HostConfig.RestartPolicy.MaximumRetryCount }}' If RestartPolicyName= "" and MaximumRetryCount=0, this is not a finding. If RestartPolicyName=always, this is a finding. If RestartPolicyName=on-failure, verify that the number of restart attempts is set to 5 or less by looking at MaximumRetryCount. If RestartPolicyName=failure and MaximumRetryCount is > 5, this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-235844`

### Rule: The Docker Enterprise default ulimit must not be overwritten at runtime unless approved in the System Security Plan (SSP).

**Rule ID:** `SV-235844r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default ulimit is set at the Docker daemon level. However, override the default ulimit setting, if needed, during container runtime. ulimit provides control over the resources available to the shell and to processes started by it. Setting system resource limits judiciously prevents many disasters such as a fork bomb. Sometimes, even friendly users and legitimate processes can overuse system resources and in-turn can make the system unusable. The default ulimit set at the Docker daemon level should be honored. If the default ulimit settings are not appropriate for a particular container instance, override them as an exception. But, do not make this a practice. If most of the container instances are overriding default ulimit settings, consider changing the default ulimit settings to something that is appropriate for your needs. If the ulimits are not set properly, the desired resource control might not be achieved and might even make the system unusable. Container instances inherit the default ulimit settings set at the Docker daemon level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the use of Docker Engine - Enterprise on a Linux host operating system. Ensure the default ulimit is not overwritten at runtime unless approved in the SSP. via CLI: Linux: As a Docker EE Admin, execute the following command using a Universal Control Plane (UCP) client bundle: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Ulimits={{ .HostConfig.Ulimits }}' If each container instance returns Ulimits=<no value>, this is not a finding. If a container sets a Ulimit and the setting is not approved in the SSP, this is a finding.

## Group: SRG-APP-000454

**Group ID:** `V-235845`

### Rule: Docker Enterprise older Universal Control Plane (UCP) and Docker Trusted Registry (DTR) images must be removed from all cluster nodes upon upgrading.

**Rule ID:** `SV-235845r961677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When upgrading either the UCP or DTR components of Docker Enterprise, the newer images are pulled (or unpacked if offline) onto Engine nodes in a cluster. Once the upgrade is complete, one must manually remove all old image version from the cluster nodes to meet the requirements of this control. When upgrading the Docker Engine - Enterprise component of Docker Enterprise, the old package version is automatically replaced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all outdated UCP and DTR container images have been removed from all nodes in the cluster. via CLI: As a Docker EE admin, execute the following command using a client bundle: docker images --filter reference='docker/[ucp|dtr]*' Verify that there are no tags listed that are older than the currently installed versions of UCP and DTR. If any of the tags listed are older than the currently installed versions of UCP and DTR, then this is a finding.

## Group: SRG-APP-000475

**Group ID:** `V-235846`

### Rule: Only trusted, signed images must be stored in Docker Trusted Registry (DTR) in Docker Enterprise.

**Rule ID:** `SV-235846r961740_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Universal Control Plane (UCP) and DTR components of Docker Enterprise can be used in concert to perform an integrity check of organization-defined software at startup. In the context of Docker Enterprise, software would be analogous to Docker images that have been pulled from trusted or untrusted sources. Docker Hub is the most common upstream endpoint for retrieving Docker images. However, only "Docker Certified" images on Docker Hub are considered trusted and come with SLAs and trusted signatures from their respective vendors. All other images from Docker Hub or other external registries must be carefully inspected and triaged prior to use. Docker Content Trust (DCT) provides for content integrity checking mechanisms on Docker images. DCT can be combined with LDAP, DTR and UCP to enforce image signatures from users/accounts in LDAP. Therefore, to meet the requirements of this control, it is imperative that UCP has LDAP integration enabled and that content trust enforcement is enabled and properly configured. Satisfies: SRG-APP-000475, SRG-APP-000480, SRG-APP-000484, SRG-APP-000485, SRG-APP-000386</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the DTR component of Docker Enterprise. Verify that all images that are stored in DTR are trusted, signed images: via UI: As a Docker EE Admin, navigate to "Repositories" in the DTR management console. Select a repository from the list. Navigate to the "Images" tab and verify that the "Signed" checkmark is indicated for each image tag. Repeat this for all repositories stored in DTR. If images stored in DTR are not signed, this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands on a machine that can communicate with the DTR management console. Replace [dtr_url] with the DTR URL, [dtr_username] with the username of a Docker EE Admin and [dtr_password] with the password of a Docker EE Admin. AUTHTOKEN=$(curl -sk -u [dtr_username]:[dtr_password] -X GET "https://[dtr_url]/auth/token" | jq -r .token) REPOS=$(curl -sk -H "Authorization: Bearer $AUTHTOKEN" -X GET "https://[dtr_url]/api/v0/repositories" | jq -r '.repositories[] | "\(.namespace)/\(.name)"') for r in $REPOS; do curl -sk -H "Authorization: Bearer $AUTHTOKEN" -X GET "https://[dtr_url]/api/v0/repositories/$r/tags?domain=[dtr_url]"; done | jq -r '.[] | [.name, .inNotary] | @csv' Verify that "true" is output next to all tags listed. If all images stored in DTR are not signed and trusted, this is a finding.

## Group: SRG-APP-000485

**Group ID:** `V-235847`

### Rule: Docker Content Trust enforcement must be enabled in Universal Control Plane (UCP).

**Rule ID:** `SV-235847r961770_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UCP and Docker Trusted Registry (DTR) components of Docker Enterprise can be used in concert with built-in audit logging capabilities to audit detected potential integrity violations per the requirements set forth by the System Security Plan (SSP). In the context of Docker Enterprise, software would be analogous to Docker images that have been pulled from trusted or untrusted sources. Docker Hub is the most common upstream endpoint for retrieving Docker images. However, only "Docker Certified" images on Docker Hub are considered trusted and come with SLAs and trusted signatures from their respective vendors. All other images from Docker Hub or other external registries must be carefully inspected and triaged prior to use. Docker Content Trust (DCT) provides for content integrity checking mechanisms on Docker images. DCT can be combined with LDAP, DTR and UCP to enforce image signatures from users/accounts in LDAP. Therefore, to meet the requirements of this control, it is imperative that UCP has LDAP integration enabled and that content trust enforcement is enabled and properly configured. The UCP and DTR components of Docker Enterprise provide audit record generation capabilities. Audit logs capture all HTTP actions for the following endpoints: Kubernetes API, Swarm API and UCP API. The following UCP API endpoints are excluded from audit logging (where "*" designates a wildcard of exclusions): "/_ping", "/ca", "/auth", "/trustedregistryca", "/kubeauth", "/metrics", "/info", "/version*", "/debug", "/openid_keys", "/apidocs", "kubernetesdocs" and "/manage". Audit log verbosity can be set to one of the following levels: "none", "metadata", or "request". To meet the requirements of this control, the "request" verbosity level must be configured in UCP. The data captured at each level for UCP and the eNZI authentication and authorization backplane is described below: "none": audit logging is disabled "metadata": - method and API endpoint for the request - UCP user which made the request - response status (success/failure) - timestamp of the call - object ID of created/updated resource (for create/update calls) - license key - remote address "request": includes all fields from the "metadata" level, as well as the request payload DTR audits all events associated with repository activities. Events are considered as follows: create, get, delete, update, send, fail, and scan. The following types are associated with the defined audit events: repository, tag, blob, manifest, webhook, uri, promotion, push mirroring, poll mirroring, garbage collector, system. The Docker Engine - Enterprise component of Docker Enterprise relies on the underlying host operating system's auditing capabilities. By default, the host OS is not configured to audit Docker Engine - Enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Check that UCP is configured to only run signed images by applicable Orgs and Teams. via UI: In the UCP web console, navigate to "Admin Settings" | "Docker Content Trust" and verify that "Run only signed images" is checked. Verify that the Orgs and Teams that images must be signed by in the dropdown that follows matches that of the organizational policies. If "Run only signed images" is not checked, this is a finding. via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands on a machine that can communicate with the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "require_content_trust" entry under the "[trust_configuration]" section in the output, and verify that it is set to "true". If require_content_trust is not set to true, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235848`

### Rule: Docker Swarm must have the minimum number of manager nodes.

**Rule ID:** `SV-235848r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensure that the minimum number of required manager nodes is created in a swarm. Manager nodes within a swarm have control over the swarm and change its configuration modifying security parameters. Having excessive manager nodes could render the swarm more susceptible to compromise. If fault tolerance is not required in the manager nodes, a single node should be elected as a manger. If fault tolerance is required then the smallest practical odd number to achieve the appropriate level of tolerance should be configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the correct range of manager nodes have been created in a swarm. via CLI: Linux: As a Docker EE Admin, follow the steps below using a Universal Control Plane (UCP) client bundle: Run the following command. docker info --format '{{ .Swarm.Managers }}' Alternatively run the below command. docker node ls | grep 'Leader' Ensure the number of leaders is between 1 and 3. If the number of leaders is not 1, 2 or 3, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235849`

### Rule: Docker Enterprise Swarm manager auto-lock key must be rotated periodically.

**Rule ID:** `SV-235849r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Rotate swarm manager auto-lock key periodically. Swarm manager auto-lock key is not automatically rotated. Rotate them periodically as a best practice. By default, keys are not rotated automatically.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system administrator to identify the key rotation process. Determine if there is a key rotation record and if the keys are rotated at a pre-defined frequency. If the swarm manager auto-lock key is not rotated on a regular basis, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235850`

### Rule: Docker Enterprise node certificates must be rotated as defined in the System Security Plan (SSP).

**Rule ID:** `SV-235850r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Rotate swarm node certificates as appropriate. Docker Swarm uses mutual TLS for clustering operations amongst its nodes. Certificate rotation ensures that in an event such as compromised node or key, it is difficult to impersonate a node. By default, node certificates are rotated every 90 days. The user should rotate it more often or as appropriate in their environment. By default, node certificates are rotated automatically every 90 days.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure node certificates are rotated as appropriate. via CLI: Linux: As a Docker EE Admin, follow the steps below using a Universal Control Plane (UCP) client bundle: Run the below command and ensure that the node certificate Expiry Duration is set according to the System Security Plan (SSP). docker info | grep "Expiry Duration" If the expiry duration is not set according to the SSP, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235851`

### Rule: Docker Enterprise docker.service file ownership must be set to root:root.

**Rule ID:** `SV-235851r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the docker.service file ownership and group-ownership are correctly set to root. docker.service file contains sensitive parameters that may alter the behavior of Docker daemon. Hence, it should be owned and group-owned by root to maintain the integrity of the file. This file may not be present on the system. In that case, this recommendation is not applicable. By default, if the file is present, the ownership and group-ownership for this file is correctly set to root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that docker.service file ownership is set to root:root Step 1: Find out the file location: systemctl show -p FragmentPath docker.service Step 2: If the file does not exist, this is not a finding. If the file exists, execute the below command with the correct file path to verify that the file is owned and group-owned by root. Example: stat -c %U:%G /usr/lib/systemd/system/docker.service | grep -v root:root If the above command returns nothing, this is not a finding. If the command returns non root:root file permissions, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235852`

### Rule: Docker Enterprise docker.service file permissions must be set to 644 or more restrictive.

**Rule ID:** `SV-235852r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify that the docker.service file permissions are correctly set to 644 or more restrictive. docker.service file contains sensitive parameters that may alter the behavior of Docker daemon. Hence, it should not be writable by any other user other than root to maintain the integrity of the file. This file may not be present on the system. In that case, this recommendation is not applicable. By default, if the file is present, the file permissions are correctly set to 644.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that docker.service file permissions are set to 644 or more restrictive. Step 1: Find out the file location: systemctl show -p FragmentPath docker.service Step 2: If the file does not exist, this is not a finding. If the file exists, execute the below command with the correct file path to verify that the file permissions are set to 644 or more restrictive. stat -c %a /usr/lib/systemd/system/docker.service If the file permissions are not set to 644 or a more restrictive permission, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235853`

### Rule: Docker Enterprise docker.socket file ownership must be set to root:root.

**Rule ID:** `SV-235853r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the docker.socket file ownership and group ownership is correctly set to root. docker.socket file contains sensitive parameters that may alter the behavior of Docker remote API. Hence, it should be owned and group-owned by root to maintain the integrity of the file. This file may not be present on the system. In that case, this recommendation is not applicable. By default, if the file is present, the ownership and group-ownership for this file is correctly set to root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that docker.socket file ownership is set to root:root. Step 1: Find out the file location: systemctl show -p FragmentPath docker.socket Step 2: If the file does not exist, this is not a finding. If the file exists, execute the below command with the correct file path to verify that the file is owned and group-owned by root. Example: stat -c %U:%G /usr/lib/systemd/system/docker.socket | grep -v root:root If the above command returns nothing, this is not a finding. If the command returns non root:root file permissions, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235854`

### Rule: Docker Enterprise docker.socket file permissions must be set to 644 or more restrictive.

**Rule ID:** `SV-235854r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify that the docker.socket file permissions are correctly set to 644 or more restrictive. docker.socket file contains sensitive parameters that may alter the behavior of Docker remote API. Hence, it should be writable only by root to maintain the integrity of the file. This file may not be present on the system. In that case, this recommendation is not applicable. By default, if the file is present, the file permissions for this file are correctly set to 644.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that docker.socket file permissions are set to 644 or more restrictive. Step 1: Find out the file location: systemctl show -p FragmentPath docker.socket Step 2: If the file does not exist, this is not a finding. If the file exists, execute the below command with the correct file path to verify that the file permissions are set to 644 or more restrictive. stat -c %a /usr/lib/systemd/system/docker.socket If the file permissions are not set to 644 or a more restrictive permission, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235855`

### Rule: Docker Enterprise /etc/docker directory ownership must be set to root:root.

**Rule ID:** `SV-235855r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the /etc/docker directory ownership and group-ownership is correctly set to root. /etc/docker directory contains certificates and keys in addition to various sensitive files. Hence, it should be owned and group-owned by root to maintain the integrity of the directory. By default, the ownership and group-ownership for this directory is correctly set to root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that /etc/docker directory ownership is set to root:root. On CentOS host OS's, execute the below command to verify that the directory is owned and group-owned by root: stat -c %U:%G /etc/docker If root:root is not displayed, this is a finding. On Ubuntu host OS's, execute the below command to verify that the /etc/default/docker directory ownership is set to root:root: stat -c %U:%G /etc/default/docker If root:root is not displayed, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235856`

### Rule: Docker Enterprise /etc/docker directory permissions must be set to 755 or more restrictive.

**Rule ID:** `SV-235856r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify that the /etc/docker directory permissions are correctly set to 755 or more restrictive. /etc/docker directory contains certificates and keys in addition to various sensitive files. Hence, it should only be writable by root to maintain the integrity of the directory. By default, the permissions for this directory are correctly set to 755.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the below command to verify that the directory has permissions of 755 or more restrictive: stat -c %a /etc/docker If the permissions are not set to 755, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235857`

### Rule: Docker Enterprise registry certificate file ownership must be set to root:root.

**Rule ID:** `SV-235857r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that all the registry certificate files (usually found under /etc/docker/certs.d/<registry-name> directory) are owned and group-owned by root. /etc/docker/certs.d/<registry-name> directory contains Docker registry certificates. These certificate files must be owned and group-owned by root to maintain the integrity of the certificates. By default, the ownership and group-ownership for registry certificate files is correctly set to root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that registry certificate file ownership is set to root:root. Execute the below command to verify that the registry certificate files are owned and group-owned by root: stat -c %U:%G /etc/docker/certs.d/* If the certificate files are not owned by root, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235858`

### Rule: Docker Enterprise registry certificate file permissions must be set to 444 or more restrictive.

**Rule ID:** `SV-235858r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify that all the registry certificate files (usually found under /etc/docker/certs.d/<registry-name> directory) have permissions of 444 or more restrictive. /etc/docker/certs.d/<registry-name> directory contains Docker registry certificates. These certificate files must have permissions of 444 to maintain the integrity of the certificates. By default, the permissions for registry certificate files might not be 444. The default file permissions are governed by the system or user specific umaskvalues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that registry certificate file permissions are set to 444 or more restrictive. Execute the below command to verify that the registry certificate files have permissions of 444 or more restrictive: stat -c %a /etc/docker/certs.d/<registry-name>/* If the permissions are not set to 444, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235859`

### Rule: Docker Enterprise TLS certificate authority (CA) certificate file ownership must be set to root:root.

**Rule ID:** `SV-235859r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the TLS CA certificate file (the file that is passed along with --TLScacert parameter) is owned and group-owned by root. The TLS CA certificate file should be protected from any tampering. It is used to authenticate Docker server based on given CA certificate. Hence, it must be owned and group-owned by root to maintain the integrity of the CA certificate. By default, the ownership and group-ownership for TLS CA certificate file is correctly set to root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that TLS CA certificate file ownership is set to root:root. Execute the below command to verify that the TLS CA certificate file is owned and group-owned by root: stat -c %U:%G <path to TLS CA certificate file> If the TLS CA certificate permissions are not set to root:root, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235860`

### Rule: Docker Enterprise TLS certificate authority (CA) certificate file permissions must be set to 444 or more restrictive.

**Rule ID:** `SV-235860r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify that the TLS CA certificate file (the file that is passed along with --TLScacert parameter) has permissions of 444 or more restrictive. The TLS CA certificate file should be protected from any tampering. It is used to authenticate Docker server based on given CA certificate. Hence, it must have permissions of 444 to maintain the integrity of the CA certificate. By default, the permissions for TLS CA certificate file might not be 444. The default file permissions are governed by the system or user specific umask values.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that TLS CA certificate file permissions are set to 444 or more restrictive. Execute the below command to verify that the TLS CA certificate file has permissions of 444 or more restrictive: stat -c %a <path to TLS CA certificate file> If the permissions are not set to 444, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235861`

### Rule: Docker Enterprise server certificate file ownership must be set to root:root.

**Rule ID:** `SV-235861r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the Docker server certificate file (the file that is passed along with --TLScert parameter) is owned and group-owned by root. The Docker server certificate file should be protected from any tampering. It is used to authenticate Docker server based on the given server certificate. Hence, it must be owned and group-owned by root to maintain the integrity of the certificate. By default, the ownership and group-ownership for Docker server certificate file is correctly set to root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that Docker server certificate file ownership is set to root:root. Execute the below command to verify that the Docker server certificate file is owned and group-owned by root: stat -c %U:%G <path to Docker server certificate file> If the command does not return root:root, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235862`

### Rule: Docker Enterprise server certificate file permissions must be set to 444 or more restrictive.

**Rule ID:** `SV-235862r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify that the Docker server certificate file (the file that is passed along with --TLScert parameter) has permissions of 444 or more restrictive. The Docker server certificate file should be protected from any tampering. It is used to authenticate Docker server based on the given server certificate. Hence, it must have permissions of 444 to maintain the integrity of the certificate. By default, the permissions for Docker server certificate file might not be 444. The default file permissions are governed by the system or user specific umask values.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that Docker server certificate file permissions are set to 444 or more restrictive. Execute the below command to verify that the Docker server certificate file has permissions of 444 or more restrictive: stat -c %a <path to Docker server certificate file> If the permissions are not set to 444, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235863`

### Rule: Docker Enterprise server certificate key file ownership must be set to root:root.

**Rule ID:** `SV-235863r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verify that the Docker server certificate key file (the file that is passed along with --TLSkey parameter) is owned and group-owned by root. The Docker server certificate key file should be protected from any tampering or unneeded reads. It holds the private key for the Docker server certificate. Hence, it must be owned and group-owned by root to maintain the integrity of the Docker server certificate. By default, the ownership and group-ownership for Docker server certificate key file is correctly set to root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that Docker server certificate key file ownership is set to root:root. Execute the below command to verify that the Docker server certificate key file is owned and group-owned by root: stat -c %U:%G <path to Docker server certificate key file> If the certificate file is not owned by root:root, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235864`

### Rule: Docker Enterprise server certificate key file permissions must be set to 400.

**Rule ID:** `SV-235864r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the Docker server certificate key file (the file that is passed along with --TLSkey parameter) has permissions of 400. The Docker server certificate key file should be protected from any tampering or unneeded reads. It holds the private key for the Docker server certificate. Hence, it must have permissions of 400 to maintain the integrity of the Docker server certificate. By default, the permissions for Docker server certificate key file might not be 400. The default file permissions are governed by the system or user specific umask values.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that Docker server certificate key file permissions are set to 400. Execute the below command to verify that the Docker server certificate key file has permissions of 400: stat -c %a <path to Docker server certificate key file> If the permissions are not set to 400, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235865`

### Rule: Docker Enterprise socket file ownership must be set to root:docker.

**Rule ID:** `SV-235865r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the Docker socket file is owned by root and group-owned by docker. Docker daemon runs as root. The default UNIX socket hence must be owned by root. If any other user or process owns this socket, then it might be possible for that non-privileged user or process to interact with Docker daemon. Also, such a non-privileged user or process might interact with containers. This is neither secure nor desired behavior. Additionally, the Docker installer creates a UNIX group called docker. Users can be added to this group, and then those users would be able to read and write to default Docker UNIX socket. The membership to the docker group is tightly controlled by the system administrator. If any other group owns this socket, then it might be possible for members of that group to interact with Docker daemon. Also, such a group might not be as tightly controlled as the docker group. This is neither secure nor desired behavior. Hence, the default Docker UNIX socket file must be owned by root and group-owned by docker to maintain the integrity of the socket file. By default, the ownership and group-ownership for Docker socket file is correctly set to root:docker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that Docker socket file ownership is set to root:docker. Execute the below command to verify that the Docker socket file is owned by root and group-owned by docker: stat -c %U:%G /var/run/docker.sock If docker.sock file ownership is not set to root:docker, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235866`

### Rule: Docker Enterprise socket file permissions must be set to 660 or more restrictive.

**Rule ID:** `SV-235866r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the Docker socket file has permissions of 660 or more restrictive. Only root and members of docker group should be allowed to read and write to default Docker UNIX socket. Hence, the Docket socket file must have permissions of 660 or more restrictive. By default, the permissions for Docker socket file is correctly set to 660.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that Docker socket file permissions are set to 660 or more restrictive. Execute the below command to verify that the Docker socket file has permissions of 660 or more restrictive: stat -c %a /var/run/docker.sock If the permissions are not set to 660, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235867`

### Rule: Docker Enterprise daemon.json file ownership must be set to root:root.

**Rule ID:** `SV-235867r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the daemon.json file ownership and group-ownership is correctly set to root. daemon.json file contains sensitive parameters that may alter the behavior of docker daemon. Hence, it should be owned and group-owned by root to maintain the integrity of the file. This file may not be present on the system. In that case, this recommendation is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The docker.daemon file is not created on installation and must be created. Ensure that daemon.json file ownership is set to root:root. Execute the below command to verify that the file is owned and group-owned by root: stat -c %U:%G /etc/docker/daemon.json If the docker.daemon file doesn't exist or if the file permissions are not set to root:root, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235868`

### Rule: Docker Enterprise daemon.json file permissions must be set to 644 or more restrictive.

**Rule ID:** `SV-235868r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the daemon.json file permissions are correctly set to 644 or more restrictive. daemon.json file contains sensitive parameters that may alter the behavior of docker daemon. Hence, it should be writable only by root to maintain the integrity of the file. This file may not be present on the system. In that case, this recommendation is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The docker.daemon file is not created on installation and must be created. Ensure that daemon.json file permissions are set to 644 or more restrictive. Execute the below command to verify that the file permissions are correctly set to 644 or more restrictive: stat -c %a /etc/docker/daemon.json If the permissions are not set to 644 or a more restrictive setting, this is a finding. If the permissions are not set to 644, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235869`

### Rule: Docker Enterprise /etc/default/docker file ownership must be set to root:root.

**Rule ID:** `SV-235869r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the /etc/default/docker file ownership and group-ownership is correctly set to root. /etc/default/docker file contains sensitive parameters that may alter the behavior of docker daemon. Hence, it should be owned and group-owned by root to maintain the integrity of the file. This file may not be present on the system. In that case, this recommendation is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement applies to Ubuntu Linux systems only. Ensure that /etc/default/docker file ownership is set to root:root. Execute the below command to verify that the file is owned and group-owned by root: stat -c %U:%G /etc/default/docker If file ownership it not set to root:root, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-235870`

### Rule: Docker Enterprise /etc/default/docker file permissions must be set to 644 or more restrictive.

**Rule ID:** `SV-235870r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify that the /etc/default/docker file permissions are correctly set to 644 or more restrictive. /etc/default/docker file contains sensitive parameters that may alter the behavior of docker daemon. Hence, it should be writable only by root to maintain the integrity of the file. This file may not be present on the system. In that case, this recommendation is not applicable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement applies to Ubuntu Linux systems only. Ensure that /etc/default/docker file permissions are set to 644 or more restrictive. Execute the below command to verify that the file permissions are correctly set to 644 or more restrictive: stat -c %a /etc/default/docker If the permissions are not set to 644, this is a finding.

## Group: SRG-APP-000175

**Group ID:** `V-235871`

### Rule: Docker Enterprise Universal Control Plane (UCP) must be integrated with a trusted certificate authority (CA).

**Rule ID:** `SV-235871r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When integrating the UCP and Docker Trusted Registry (DTR) management consoles with an external, trusted certificate authority (CA), both UCP and DTR will validate these certificate chains per the requirements set forth by the System Security Plan (SSP). UCP establishes mutual TLS authentication for all Engine - Enterprise nodes in a cluster using a built-in certificate authority which inherently meets the requirements of this control. This is described below. The UCP component of Docker Enterprise includes a built-in public key infrastructure (PKI) system. When a UCP cluster is initialized, the first node designates itself as a manager node. That node subsequently generates a new root CA along with a key pair, which are used to secure communications with other UCP manager and worker nodes that are joined to the cluster. One can also specify his/her own externally-generated root CA upon initialization of a UCP cluster. The manager node also generates two tokens to use when joining additional nodes to the cluster: one worker token and one manager token. Each token includes the digest of the root CA’s certificate and a randomly generated secret. When a node joins the cluster, the joining node uses the digest to validate the root CA certificate from the remote manager. The remote manager uses the secret to ensure the joining node is an approved node. Each time a new node joins the cluster, the manager issues a certificate to the node. The certificate contains a randomly generated node ID to identify the node under the certificate common name (CN) and the role under the organizational unit (OU). The node ID serves as the cryptographically secure node identity for the lifetime of the node in the current UCP cluster. In this mutual TLS architecture, all nodes encrypt communications using a minimum of TLS 1.2. This information can also be referenced at https://docs.docker.com/engine/swarm/how-swarm-mode-works/pki/.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Check that UCP has been integrated with a trusted CA. via UI: In the UCP web console, navigate to "Admin Settings" | "Certificates" and click on the "Download UCP Server CA Certificate" link. Verify that the contents of the downloaded "ca.pem" file match that of the user's trusted CA certificate. If the UCP certificate is not signed by a trusted DoD CA this is a finding. via CLI: Linux: Execute the following command and verify the certificate chain in the output is valid and matches that of the trusted CA: echo "" | openssl s_client -connect [ucp_url]:443 | openssl x509 -noout -text If the UCP certificate is not signed by a trusted DoD CA this is a finding.

## Group: SRG-APP-000416

**Group ID:** `V-235872`

### Rule: Docker Enterprise data exchanged between Linux containers on different nodes must be encrypted on the overlay network.

**Rule ID:** `SV-235872r962034_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encrypt data exchanged between containers on different nodes on the overlay network. By default, data exchanged between containers on different nodes on the overlay network is not encrypted. This could potentially expose traffic between the container nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure data exchanged between containers are encrypted on different nodes on the overlay network. via CLI: Linux: As a Docker EE Admin, follow the steps below using a Universal Control Plane (UCP) client bundle: Run the below command and ensure that each overlay network has been encrypted. docker network ls --filter driver=overlay --quiet | xargs docker network inspect --format '{{.Name}} {{ .Options }}' | grep -v "dtr\|interlock map\|ingress map" If the network overlay drivers do not show [com.docker.network.driver.overlay"encrypted:" ask for evidence that encryption is being handled at the application layer, if no evidence of encryption at the network or application layer is provided, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-235873`

### Rule: Docker Enterprise Swarm services must be bound to a specific host interface.

**Rule ID:** `SV-235873r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the docker swarm services will listen to all interfaces on the host, which may not be necessary for the operation of the swarm where the host has multiple network interfaces. When a swarm is initialized the default value for the --listen-addr flag is 0.0.0.0:2377 which means that the swarm services will listen on all interfaces on the host. If a host has multiple network interfaces this may be undesirable as it may expose the docker swarm services to networks which are not involved in the operation of the swarm. By passing a specific IP address to the --listen-addr, a specific network interface can be specified limiting this exposure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure swarm services are bound to a specific host interface. Linux: List the network listener on port 2377/TCP (the default for docker swarm) and confirm that it is only listening on specific interfaces. For example, using ubuntu this could be done with the following command: netstat -lt | grep -i 2377 If the swarm service is not bound to a specific host interface address, this is a finding.

## Group: SRG-APP-000560

**Group ID:** `V-235874`

### Rule: Docker Enterprise Universal Control Plane (UCP) must be configured to use TLS 1.2.

**Rule ID:** `SV-235874r961869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default docker UCP is configured to use TLS v1.2, if this setting is misconfigured, older protocols containing security weaknesses could be utilized. TLS requires a handshake between client and server which is where the TLS version utilized in the connection is negotiated. For DoD use cases, all TLS must be at version 1.2.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check only applies to the UCP component of Docker Enterprise. Via CLI: Linux (requires curl and jq): As a Docker EE Admin, execute the following commands from a machine that can communicate with the UCP management console. Replace [ucp_url] with the UCP URL, [ucp_username] with the username of a UCP administrator and [ucp_password] with the password of a UCP administrator. AUTHTOKEN=$(curl -sk -d '{"username":"[ucp_username]","password":"[ucp_password]"}' https://[ucp_url]/auth/login | jq -r .auth_token) curl -sk -H "Authorization: Bearer $AUTHTOKEN" https://[ucp_url]/api/ucp/config-toml Look for the "min_TLS_version =" entry under the "[cluster_config]" section in the output, and verify that it is set to "TLSv1.2". If the "min_TLS_version" entry under the "[cluster_config]" section in the output is not set to "TLSv1.2", then this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-265885`

### Rule: The version of Docker Enterprise Edition running on the system must be a supported version.

**Rule ID:** `SV-265885r999859_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Docker Enterprise Edition 2.x is no longer supported by the vendor. If the system is running Docker Enterprise Edition 2.x, this is a finding.

