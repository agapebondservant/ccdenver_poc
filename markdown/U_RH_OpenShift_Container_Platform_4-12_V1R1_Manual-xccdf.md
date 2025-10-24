# STIG Benchmark: Red Hat OpenShift Container Platform 4.12 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014-CTR-000035

**Group ID:** `V-257505`

### Rule: OpenShift must use TLS 1.2 or greater for secure container image transport from trusted sources.

**Rule ID:** `SV-257505r921458_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The authenticity and integrity of the container image during the container image lifecycle is part of the overall security posture of the container platform. This begins with the container image creation and pull of a base image from a trusted source for child container image creation and the instantiation of the new image into a running service. If an insecure protocol is used during transmission of container images at any step of the lifecycle, a bad actor may inject nefarious code into the container image. The container image, when instantiated, then becomes a security risk to the container platform, the host server, and other containers within the container platform. To thwart the injection of code during transmission, a secure protocol (TLS 1.2 or newer) must be used. Further guidance on secure transport protocols can be found in NIST SP 800-52.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that no insecure registries are configured by executing the following: oc get image.config.openshift.io/cluster -ojsonpath='{.spec.allowedRegistriesForImport}' | jq -r '.[] | select(.insecure == true)' If the above query finds any registries, this is a finding. Empty output is not a finding. Verify that no insecure registries are configured by executing the following: oc get image.config.openshift.io/cluster -ojsonpath='{.spec.registrySources.insecureRegistries}' If the above query returns anything, then this is a finding. Empty output is not a finding.

## Group: SRG-APP-000014-CTR-000040

**Group ID:** `V-257506`

### Rule: OpenShift must use TLS 1.2 or greater for secure communication.

**Rule ID:** `SV-257506r921461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The authenticity and integrity of the container platform and communication between nodes and components must be secure. If an insecure protocol is used during transmission of data, the data can be intercepted and manipulated. The manipulation of data can be used to inject status changes of the container platform, causing the execution of containers or reporting an incorrect healthcheck. To thwart the manipulation of the data during transmission, a secure protocol (TLS 1.2 or newer) must be used. Further guidance on secure transport protocols can be found in NIST SP 800-52. Satisfies: SRG-APP-000014-CTR-000040, SRG-APP-000560-CTR-001340</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the TLS Security Profile is not set to a profile that does not enforce TLS 1.2 or above. View the TLS security profile for the ingress controllers by executing the following: oc get --all-namespaces ingresscontrollers.operator.openshift.io -ocustom-columns="NAME":.metadata.name,"NAMESPACE":.metadata.namespace,"TLS PROFILE":.spec.tlsSecurityProfile View the TLS security profile for the control plane by executing the following: oc get APIServer cluster -ocustom-columns="TLS PROFILE":.spec.tlsSecurityProfile View the TLS profile for the Kubelet by executing the following: oc get kubeletconfigs -ocustom-columns="NAME":.metadata.name,"TLS PROFILE":.spec.tlsSecurityProfile If any of the above returns a TLS profile of "Old", this is a finding. If any of the above returns a TLS profile of "Custom" and the minTLSVersion is not set to "VersionTLS12" or greater, this is a finding. If the above returns "<none>" TLS profile, this is not a finding as the TLS profile defaults to "Intermediate". If the kubelet TLS profile check does not return any kubeletconfigs, this is not a finding as the default OCP installation uses defaults only.

## Group: SRG-APP-000023-CTR-000055

**Group ID:** `V-257507`

### Rule: OpenShift must use a centralized user management solution to support account management functions.

**Rule ID:** `SV-257507r921464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift supports several different types of identity providers. To add users and grant access to OpenShift, an identity provider must be configured. Some of the identity provider types such as HTPassword only provide simple user management and are not intended for production. Other types are public services like GitHub. These provider types are not appropriate as they are managed by public service providers, and therefore are unable to enforce the organizations account management requirements. Use either the LDAP or the OpenIDConnect Identity Provider type to configure OpenShift to use the organizations centrally managed IdP that is able to enforce the organization's policies regarding user identity management.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the authentication operator is configured to use either an LDAP or a OpenIDConnect provider by executing the following: oc get oauth cluster -o jsonpath="{.spec.identityProviders[*].type}{'\n'}" If the output lists any other type besides LDAP or OpenID, this is a finding.

## Group: SRG-APP-000023-CTR-000055

**Group ID:** `V-257508`

### Rule: The kubeadmin account must be disabled.

**Rule ID:** `SV-257508r921467_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using a centralized user management solution for account management functions enhances security, simplifies administration, improves user experience, facilitates compliance, and provides scalability and integration capabilities. It is a foundational element of effective identity and access management practices. OpenShift supports several different types of identity providers. To add users and grant access to OpenShift, an identity provider needs to be configured. Some of the identity provider types, such as HTPassword, only provide simple user management and are not intended for production. Other types are public services, like GitHub. These provider types may not be appropriate as they are managed by public service providers and therefore are unable to enforce the organizations account management requirements. After a new install, the default authentication uses kubeadmin as the default cluster-admin account. This default account must be disabled and another user account must be given cluster-admin rights.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the kubeadmin account is disabled by executing the following: oc get secrets kubeadmin -n kube-system If the command returns an error, the secret was not found, and this is not a finding. (Example output: Error from server (NotFound): secrets "kubeadmin" not found) If the command returns a listing that includes the kubeadmin secret, its type, the data count, and age, this is a finding. (Example Output for not a finding: NAME TYPE DATA AGE kubeadmin Opaque 1 6h3m)

## Group: SRG-APP-000026-CTR-000070

**Group ID:** `V-257509`

### Rule: OpenShift must automatically audit account creation.

**Rule ID:** `SV-257509r921470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create a new account. Auditing account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail documents the creation of application user accounts and, as required, notifies administrators and/or application owners exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Red Hat Enterprise Linux CoreOS (RHCOS) generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow". Logging on as administrator, check the auditing rules in "/etc/audit/audit.rules" by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME: "; grep /etc/shadow /etc/audit/audit.rules /etc/audit/rules.d/*'; done (Example output: -w /etc/shadow -p wa -k identity) If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-APP-000027-CTR-000075

**Group ID:** `V-257510`

### Rule: OpenShift must automatically audit account modification.

**Rule ID:** `SV-257510r921473_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to modify an existing account. Auditing of account modifications is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail documents the creation of application user accounts and, as required, notifies administrators and/or application owners exists. Such a process greatly reduces the risk that accounts will be surreptitiously modified and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to offload those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify for each of the files that contain account information the system is configured to emit an audit event in case of a write by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; for f in /etc/passwd /etc/group /etc/gshadow /etc/security/opasswd /etc/shadow /etc/sudoers /etc/sudoers.d/; do grep -q "\-w $f \-p wa \-k" /etc/audit/audit.rules || echo "rule for $f not found"; done' 2>/dev/null; done If for any of the files a line saying "rule for $filename not found" is printed, this is a finding.

## Group: SRG-APP-000028-CTR-000080

**Group ID:** `V-257511`

### Rule: OpenShift must generate audit rules to capture account related actions.

**Rule ID:** `SV-257511r921476_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management actions, such as creation, modification, disabling, removal, and enabling are important changes within the system. When management actions are modified, user accessibility is affected. Once an attacker establishes access to an application, the attacker often attempts to disable authorized accounts to disrupt services or prevent the implementation of countermeasures. In the event of a security incident or policy violation, having detailed audit logs for account creation, modification, disabling, removal, and enabling actions is crucial for incident response and forensic investigations. These logs provide a trail of activities that can be analyzed to determine the cause, impact, and scope of the incident, aiding in the investigation and remediation process. Satisfies: SRG-APP-000028-CTR-000080, SRG-APP-000291-CTR-000675, SRG-APP-000292-CTR-000680, SRG-APP-000293-CTR-000685, SRG-APP-000294-CTR-000690, SRG-APP-000319-CTR-000745, SRG-APP-000320-CTR-000750, SRG-APP-000509-CTR-001305</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit rules capture account creation, modification, disabling, removal, and enabling actions by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e user-modify -e group-modify -e audit_rules_usergroup_modification /etc/audit/rules.d/* /etc/audit/audit.rules' 2>/dev/null; done Confirm the following rules exist on each node: -w /etc/group -p wa -k audit_rules_usergroup_modification -w /etc/gshadow -p wa -k audit_rules_usergroup_modification -w /etc/security/opasswd -p wa -k audit_rules_usergroup_modification -w /etc/passwd -p wa -k audit_rules_usergroup_modification -w /etc/shadow -p wa -k audit_rules_usergroup_modification If the above rules are not listed on each node, this is a finding.

## Group: SRG-APP-000029-CTR-000085

**Group ID:** `V-257512`

### Rule: Open Shift must automatically audit account removal actions.

**Rule ID:** `SV-257512r921479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are removed, user accessibility is affected. Once an attacker establishes access to an application, the attacker often attempts to remove authorized accounts to disrupt services or prevent the implementation of countermeasures. Auditing account removal actions provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/audit mechanisms meeting or exceeding access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit rules capture the execution of setuid and setgid binaries by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e key=privileged /etc/audit/audit.rules || echo "not found"' 2>/dev/null; done If "not found" is printed, this is a finding. Confirm the following rules exist on each node: -a always,exit -S all -F path=/usr/libexec/dbus-1/dbus-daemon-launch-helper -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/sbin/grub2-set-bootflag -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/libexec/openssh/ssh-keysign -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/chage -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/fusermount3 -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/fusermount -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/gpasswd -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/mount -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/newgrp -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/passwd -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/pkexec -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/sudo -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/su -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/umount -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/bin/write -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/libexec/sssd/krb5_child -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/libexec/sssd/ldap_child -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/libexec/sssd/proxy_child -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/libexec/sssd/selinux_child -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/libexec/utempter -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/lib/polkit-1/polkit-agent-helper-1 -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/sbin/mount.nfs -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/sbin/pam_timestamp_check -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -S all -F path=/usr/sbin/unix_chkpwd -F auid>=1000 -F auid!=unset -F key=privileged To find all setuid binaries on the system, execute the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; find / -xdev -type f -perm -4000 -o -type f -perm -2000 2>/dev/null'; done If any setuid binary does not have a corresponding audit rule, this is a finding.

## Group: SRG-APP-000033-CTR-000090

**Group ID:** `V-257513`

### Rule: OpenShift RBAC access controls must be enforced.

**Rule ID:** `SV-257513r921482_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Controlling and limiting users access to system services and resources is key to securing the platform and limiting the intentional or unintentional compromising of the system and its services. OpenShift provides a robust RBAC policy system that allows for authorization policies to be as detailed as needed. Additionally, there are two layers of RBAC policies. The first is Cluster RBAC policies which administrators can control who has what access to cluster level services. The other is Local RBAC policies, which allow project developers/administrators to control what level of access users have to a given project or namespace. OpenShift provides a set of default roles out of the box, and additional roles may be added as needed. Each role has a set of rules controlling what access that role may have, and users and/or groups may be bound to one or more roles. The cluster-admin cluster level RBAC role has complete super admin privileges and it is a required role for select cluster administrators to have. The OpenShift Container Platform includes a built-in image registry. The primary purpose is to allow users to create, import, and generally manage images running in the cluster. This registry is integrated with the authentication and authorization (RBAC) services on the cluster. Restricting access permissions and providing access only to the necessary components and resources within the OpenShift environment reduces the potential impact of security breaches and unauthorized activities. Satisfies: SRG-APP-000033-CTR-000090, SRG-APP-000033-CTR-000095, SRG-APP-000033-CTR-000100, SRG-APP-000133-CTR-000290, SRG-APP-000133-CTR-000295, SRG-APP-000133-CTR-000300, SRG-APP-000133-CTR-000305, SRG-APP-000133-CTR-000310, SRG-APP-000148-CTR-000350, SRG-APP-000153-CTR-000375, SRG-APP-000340-CTR-000770, SRG-APP-000378-CTR-000880, SRG-APP-000378-CTR-000885, SRG-APP-000378-CTR-000890, SRG-APP-000380-CTR-000900, SRG-APP-000386-CTR-000920</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The administrator must verify that OpenShift is configured with the necessary RBAC access controls. Review the RBAC configuration. As the cluster-admin, view the cluster roles and their associated rule sets by executing the following: oc describe clusterrole.rbac Now, view the current set of cluster role bindings, which shows the users and groups that are bound to various roles by executing the following: oc describe clusterrolebinding.rbac Local roles and bindings can be determined by executing the following: oc describe rolebinding.rbac If these results show users with privileged access that do not require that access, this is a finding.

## Group: SRG-APP-000038-CTR-000105

**Group ID:** `V-257514`

### Rule: OpenShift must enforce network policy on the namespace for controlling the flow of information within the container platform based on organization-defined information flow control policies.

**Rule ID:** `SV-257514r921485_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift provides several layers of protection to control the flow of information between the container platform components and user services. Each user project is given a separate namespace and OpenShift enforces RBAC policies controlling which projects and services users can access. OpenShift forces the use of namespaces. Service accounts are a namespace resource as well, so they are segregated. RBAC policies apply to service accounts. In addition, Network Policies are used to control the flow of requests between containers hosted on the container platform. It is important to define a default Network Policy on the namespace that will be applied automatically to new projects to prevent unintended requests. These policies can be updated by the project's administrator (with the appropriate RBAC permissions) to apply a policy that is appropriate to the service(s) within the project namespace.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that each user namespace has a Network Policy by executing the following: for ns in $(oc get namespaces -ojson | jq -r '.items[] | select((.metadata.name | startswith("openshift") | not) and (.metadata.name | startswith("kube-") | not) and .metadata.name != "default") | .metadata.name '); do oc get networkpolicy -n$ns; done If the above returns any lines saying "No resources found in <PROJECT> namespace.", this is a finding. Empty output is not a finding.

## Group: SRG-APP-000039-CTR-000110

**Group ID:** `V-257515`

### Rule: OpenShift must enforce approved authorizations for controlling the flow of information within the container platform based on organization-defined information flow control policies.

**Rule ID:** `SV-257515r921488_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift provides several layers of protection to control the flow of information between the container platform components and user services. Each user project is given a separate namespace and OpenShift enforces RBAC policies controlling which projects and services users can access. In addition, Network Policies are used to control the flow of requests to and from externally integrated services to services hosted on the container platform. It is important to define a default Network Policy that will be applied automatically to new projects to prevent unintended requests. These policies can be updated by the project's administrator (with the appropriate RBAC permissions) to apply a policy that is appropriate to the service(s) within the project namespace.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for Network Policy. Verify a default project template is defined by executing the following: oc get project.config.openshift.io/cluster -o jsonpath="{.spec.projectRequestTemplate.name}" If no project request template is in use by the project config, this is a finding. Verify the project request template creates a Network Policy: oc get templates/<PROJECT-REQUEST-TEMPLATE> -n openshift-config -o jsonpath="{.objects[?(.kind=='NetworkPolicy')]}{'\n'}" Replace <PROJECT-REQUEST-TEMPLATE> with the name of the project request template returned from the earlier query. If the project template is not defined, or there are no Network Policy definitions in it, this is a finding.

## Group: SRG-APP-000068-CTR-000120

**Group ID:** `V-257516`

### Rule: OpenShift must display the Standard Mandatory DOD Notice and Consent Banner before granting access to platform components.

**Rule ID:** `SV-257516r921491_rule`
**Severity:** low

**Description:**
<VulnDiscussion>OpenShift has countless components where different access levels are needed. To control access, the user must first log into the component and then be presented with a DOD-approved use notification banner before granting access to the component. This guarantees privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the OpenShift CLI tool is configured to display the DOD Notice and Consent Banner, do either of the following steps: Log in to OpenShift using the oc CLI tool. oc login -u <USER> <OPENSHIFT_URL> enter password when prompted If the DOD Notice and Consent Banner is not displayed, this is a finding. Or Verify that motd config map exists and contains the DOD Notice and Consent Banner by executing the following: oc describe configmap/motd -n openshift If the configmap does not exist, or it does not contain the DOD Notice and Consent Banner text in the message data attribute, this is a finding.

## Group: SRG-APP-000089-CTR-000150

**Group ID:** `V-257517`

### Rule: OpenShift must generate audit records for all DOD-defined auditable events within all components in the platform.

**Rule ID:** `SV-257517r921494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OpenShift Platform supports three audit levels: Default, WriteRequestBodies, and AllRequestBodies. The identities of the users are logged for all three audit levels log level. The WriteRequestBodies will log the metadata and the request body for any create, update, or patch request. The AllRequestBodies will log the metadata and the request body for all read and write requests. As this generates a significant number of logs, this level is only to be used as needed. To capture sufficient data to investigate an issue, it is required to set the audit level to WriteRequestBodies. For more detailed documentation on what is being logged, refer to https://docs.openshift.com/container-platform/4.8/security/audit-log-view.html. Satisfies: SRG-APP-000089-CTR-000150, SRG-APP-000090-CTR-000155, SRG-APP-000101-CTR-000205, SRG-APP-000510-CTR-001310, SRG-APP-000516-CTR-000790</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine at what level the OpenShift audit policy logging verbosity is configured, as a cluster-administrator:execute the following command: oc get apiserver.config.openshift.io/cluster -ojsonpath='{.spec.audit.profile}' If the output from the options does not return WriteRequestBodies or AllRequestBodies, this is a finding.

## Group: SRG-APP-000091-CTR-000160

**Group ID:** `V-257518`

### Rule: OpenShift must generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-257518r921497_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift and its components must generate audit records successful/unsuccessful attempts to access or delete security objects, security levels, and privileges occur. All the components must use the same standard so that the events can be tied together to understand what took place within the overall container platform. This must establish, correlate, and help assist with investigating the events relating to an incident, or identify those responsible. Without audit record generation, access controls levels can be accessed by unauthorized users unknowingly for malicious intent, creating vulnerabilities within the container platform. Satisfies: SRG-APP-000091-CTR-000160, SRG-APP-000492-CTR-001220, SRG-APP-000493-CTR-001225, SRG-APP-000494-CTR-001230, SRG-APP-000500-CTR-001260, SRG-APP-000507-CTR-001295</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OpenShift is configured to generate audit records when successful/unsuccessful attempts to access or delete security objects, security levels, and privileges occur by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e "key=perm_mod" -e "key=unsuccessful-create" -e "key=unsuccessful-modification" -e "key=unsuccessful-access" /etc/audit/audit.rules|| echo "not found"' 2>/dev/null; done Confirm the following rules exist on each node: -a always,exit -F arch=b32 -S fchmodat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S setxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchmodat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S setxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S open -F a1&0x40 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S open -F a1&0x40 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S openat,open_by_handle_at -F a2&0x40 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S openat,open_by_handle_at -F a2&0x40 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S open -F a1&0x40 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S open -F a1&0x40 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S openat,open_by_handle_at -F a2&0x40 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S openat,open_by_handle_at -F a2&0x40 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S open -F a1&0x203 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S open -F a1&0x203 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S openat,open_by_handle_at -F a2&0x203 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S openat,open_by_handle_at -F a2&0x203 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S open -F a1&0x203 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S open -F a1&0x203 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S openat,open_by_handle_at -F a2&0x203 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S openat,open_by_handle_at -F a2&0x203 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-access -a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-access -a always,exit -F arch=b64 -S open,truncate,ftruncate,creat,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-access -a always,exit -F arch=b64 -S open,truncate,ftruncate,creat,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-access -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification On each node, if the above rules are not listed, or the return is "not found", this is a finding.

## Group: SRG-APP-000092-CTR-000165

**Group ID:** `V-257519`

### Rule: Red Hat Enterprise Linux CoreOS (RHCOS) must initiate session audits at system startup.

**Rule ID:** `SV-257519r921500_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Initiating session audits at system startup allows for comprehensive monitoring of user activities and system events from the moment the system is powered on. Audit logs capture information about login attempts, commands executed, file access, and other system activities. By starting session audits at system startup, RHCOS ensures that all relevant events are recorded, providing a complete security monitoring solution. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. By initiating session audits at system startup, RHCOS enhances security monitoring, aids in timely incident detection and response, meets compliance requirements, facilitates forensic analysis, and promotes accountability and governance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the RHCOS boot loader configuration has audit enabled, including backlog: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep audit /boot/loader/entries/*.conf || echo "not found"' 2>/dev/null; done If "audit" is not set to "1" or returns "not found", this is a finding. If "audit_backlog" is not set to 8192 or returns "not found", this is a finding.

## Group: SRG-APP-000095-CTR-000170

**Group ID:** `V-257520`

### Rule: All audit records must identify what type of event has occurred within OpenShift.

**Rule ID:** `SV-257520r921503_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the container platform, audit data can be generated from any of the deployed container platform components. This audit data is important when there are issues such as security incidents that must be investigated. Identifying the type of event in audit records helps classify and categorize different activities or actions within OpenShift. This classification allows for easier analysis, reporting, and filtering of audit logs based on specific event types. It helps distinguish between user actions, system events, policy violations, or security incidents, providing a clearer understanding of the activities occurring within the platform. Satisfies: SRG-APP-000095-CTR-000170, SRG-APP-000409-CTR-000990, SRG-APP-000508-CTR-001300, SRG-APP-000510-CTR-001310</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit service is enabled and active by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; systemctl is-enabled auditd.service; systemctl is-active auditd.service' 2>/dev/null; done If the auditd service is not "enabled" and "active" this is a finding.

## Group: SRG-APP-000096-CTR-000175

**Group ID:** `V-257521`

### Rule: OpenShift audit records must have a date and time association with all events.

**Rule ID:** `SV-257521r921506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the container platform, audit data can be generated from any of the deployed container platform components. This audit data is important when there are issues, such as security incidents, that must be investigated. To make the audit data worthwhile for the investigation of events, it is necessary to know when the event occurred. To establish the time of the event, the audit record must contain the date and time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify Red Hat Enterprise Linux CoreOS (RHCOS) Audit Daemon is configured to resolve audit information before writing to disk by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep "log_format" /etc/audit/auditd.conf' 2>/dev/null; done If the "log_format" option is not "ENRICHED", or the line is missing or commented out, this is a finding. 2. Verify RHCOS takes the appropriate action when an audit processing failure occurs. Verify RHCOS takes the appropriate action when an audit processing failure occurs by executing following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep disk_error_action /etc/audit/auditd.conf' 2>/dev/null; done If the value of the "disk_error_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is missing or commented out, ask the system administrator to indicate how the system takes appropriate action when an audit process failure occurs. If there is no evidence of appropriate action, this is a finding. 3. Verify the SA and ISSO (at a minimum) are notified when the audit storage volume is full. Check which action RHEL takes when the audit storage volume is full by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep max_log_file_action /etc/audit/auditd.conf' 2>/dev/null; done If the value of the "max_log_file_action" option is set to "ignore", "rotate", or "suspend", or the line is missing or commented out, ask the system administrator to indicate how the system takes appropriate action when an audit storage volume is full. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-APP-000099-CTR-000190

**Group ID:** `V-257522`

### Rule: All audit records must generate the event results within OpenShift.

**Rule ID:** `SV-257522r921509_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the container platform, audit data can be generated from any of the deployed container platform components. Since the audit data may be part of a larger audit system, it is important for the audit data to also include the container platform name for traceability back to the container platform itself and not just the container platform components. This audit data is important when there are issues, such as security incidents, that must be investigated. To make the audit data worthwhile for the investigation of events, it is necessary to know the outcome of the event. Protecting the integrity of the tools used for auditing purposes is a critical step to ensuring the integrity of audit data. Audit data includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is common for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed in order to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files. Satisfies: SRG-APP-000099-CTR-000190, SRG-APP-000097-CTR-000180, SRG-APP-000098-CTR-000185, SRG-APP-000100-CTR-000195, SRG-APP-000100-CTR-000200, SRG-APP-000109-CTR-000215, SRG-APP-000290-CTR-000670, SRG-APP-000357-CTR-000800</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify Red Hat Enterprise Linux CoreOS (RHCOS) Audit Daemon is configured to resolve audit information before writing to disk, by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep "log_format" /etc/audit/auditd.conf' 2>/dev/null; done If the "log_format" option is not "ENRICHED", or the line is missing or commented out, this is a finding. 2. Verify RHCOS takes the appropriate action when an audit processing failure occurs by executing following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep disk_error_action /etc/audit/auditd.conf' 2>/dev/null; done If the value of the "disk_error_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is missing, or commented out, ask the system administrator to indicate how the system takes appropriate action when an audit process failure occurs. If there is no evidence of appropriate action, this is a finding. 3. Verify the SA and ISSO (at a minimum) are notified when the audit storage volume is full. Check which action RHEL takes when the audit storage volume is full by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep max_log_file_action /etc/audit/auditd.conf' 2>/dev/null; done If the value of the "max_log_file_action" option is set to "ignore", "rotate", or "suspend", or the line is missing or commented out, ask the system administrator to indicate how the system takes appropriate action when an audit storage volume is full. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-APP-000109-CTR-000215

**Group ID:** `V-257523`

### Rule: OpenShift must take appropriate action upon an audit failure.

**Rule ID:** `SV-257523r921512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the container platform is at risk of failing to process audit logs as required that it takes action to mitigate the failure. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. Because availability of the services provided by the container platform, approved actions in response to an audit failure are as follows: (i) If the failure was caused by the lack of audit record storage capacity, the container platform must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. (ii) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the container platform must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action must be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there is a Prometheus rule to watch for audit events by executing the following: oc get prometheusrule -o yaml --all-namespaces | grep apiserver_audit Output: sum by (apiserver,instance)(rate(apiserver_audit_error_total{apiserver=~".+-apiserver"}[5m])) / sum by (apiserver,instance) (rate(apiserver_audit_event_total{apiserver=~".+-apiserver"}[5m])) > 0 If the output above is not displayed, this is a finding.

## Group: SRG-APP-000111-CTR-000220

**Group ID:** `V-257524`

### Rule: OpenShift components must provide the ability to send audit logs to a central enterprise repository for review and analysis.

**Rule ID:** `SV-257524r921515_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sending audit logs to a central enterprise repository allows for centralized log management. Instead of scattered logs across multiple OpenShift components, having a centralized repository simplifies log storage, retention, and retrieval. It provides a single source of truth for audit logs, making it easier to manage and analyze log data. Centralized audit logs are crucial for incident response and forensic investigations. When a security incident occurs, having audit logs in a central repository allows security teams to quickly access relevant log data for analysis. It facilitates incident reconstruction, root cause analysis, and the identification of the scope and impact of the incident. This is vital for effective incident response and minimizing the impact of security breaches. Satisfies: SRG-APP-000111-CTR-000220, SRG-APP-000092-CTR-000165, SRG-APP-000358-CTR-000805</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if cluster log forwarding is configured. 1. Verify the cluster-logging operator is installed by executing the following: oc get subscription/cluster-logging -n openshift-logging (Example Output: NAME PACKAGE SOURCE CHANNEL cluster-logging cluster-logging redhat-operators stable ) If the cluster-logging operator is not present, this is a finding. 2. List the cluster log forwarders defined by executing the following: oc get clusterlogforwarder -n openshift-logging If there are no clusterlogforwarders defined, this is a finding. 3. For each cluster log forwarder listed above, view the configuration details by executing the following: oc describe clusterlogforwarder/<CLF_NAME> -n openshift-logging Review the details of the cluster log forwarder. If the configuration is not set to forward logs the organization's centralized logging service, this is a finding.

## Group: SRG-APP-000116-CTR-000235

**Group ID:** `V-257525`

### Rule: OpenShift must use internal system clocks to generate audit record time stamps.

**Rule ID:** `SV-257525r921518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Knowing when a sequence of events for an incident occurred is crucial to understand what may have taken place. Without a common clock, the components generating audit events could be out of synchronization and would then present a picture of the event that is warped and corrupted. To give a clear picture, it is important that the container platform and its components use a common internal clock.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the chronyd service is enabled and active by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; systemctl is-enabled chronyd.service; systemctl is-active chronyd.service' 2>/dev/null; done If the auditd service is not "enabled" and "active", this is a finding.

## Group: SRG-APP-000116-CTR-000235

**Group ID:** `V-257526`

### Rule: The Red Hat Enterprise Linux CoreOS (RHCOS) chrony Daemon must use multiple NTP servers to generate audit record time stamps.

**Rule ID:** `SV-257526r921521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Utilizing multiple NTP servers for the chrony daemon in RHCOS ensures accurate and reliable audit record timestamps. It improves time synchronization, mitigates time drift, provides redundancy, and enhances resilience against attacks. Knowing when a sequence of events for an incident occurred is crucial to understand what may have taken place. Without a common clock, the components generating audit events could be out of synchronization and would then present a picture of the event that is warped and corrupted. To give a clear picture, it is important that the container platform and its components use a common internal clock.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Red Hat Enterprise Linux CoreOS (RHCOS) chrony Daemon is configured to use multiple NTP servers by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep "server" /etc/chrony.d/*' 2>/dev/null; done (Sample output: server <SERVER1.EXAMPLE.COM> minpoll 4 maxpoll 10 server <SERVER2.EXAMPLE.COM> minpoll 4 maxpoll 10) If multiple NTP servers are not configured, this is a finding.

## Group: SRG-APP-000118-CTR-000240

**Group ID:** `V-257527`

### Rule: OpenShift must protect audit logs from any type of unauthorized access.

**Rule ID:** `SV-257527r921524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to their advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from all unauthorized access. This includes read, write, and copy access. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, applications with user interfaces to audit records must not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs have a mode of "0600" by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; stat -c "%a %n" /var/log/audit/audit.log' 2>/dev/null; done (Sample Output: 600 /var/log/audit/audit.log) If the audit log has a mode more permissive than "0600", this is a finding. Determine if the audit log is owned by "root" executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; ls -l /var/log/audit/audit.log' 2>/dev/null; done (Sample Output: rw------- 2 root root 23 Jun 11 11:56 /var/log/audit/audit.log) If the audit log is not owned by "root", this is a finding. Verify the audit log directory is group-owned by "root" to prevent unauthorized read access by executing the following. for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; ls -ld /var/log/audit' 2>/dev/null; done (Sample Output: drw------- 2 root root 23 Jun 11 11:56 /var/log/audit) If the audit log directory is not group-owned by "root", this is a finding. Verify the audit log directories have a mode of "0700" by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; stat -c "%a %n" /var/log/audit' 2>/dev/null; done (Sample Output: 700 /var/log/audit) If the audit log directory has a mode more permissive than "0700", this is a finding.

## Group: SRG-APP-000118-CTR-000240

**Group ID:** `V-257528`

### Rule: OpenShift must protect system journal file from any type of unauthorized access by setting file permissions.

**Rule ID:** `SV-257528r921527_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is a fundamental security practice to enforce the principle of least privilege, where only the necessary permissions are granted to authorized entities. OpenShift must protect the system journal file from any type of unauthorized access by setting file permissions. The system journal file contains important log data that helps in troubleshooting and monitoring the system. Unauthorized access or tampering with the journal file can compromise the integrity of this data. By setting appropriate file permissions, OpenShift ensures that only authorized users or processes have access to the journal file, maintaining the integrity and reliability of system logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system journal file has mode "0640" or less permissive by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; machine_id=$(systemd-machine-id-setup --print); stat -c "%a %n" /var/log/journal/$machine_id/system.journal' 2>/dev/null; done If a value of "0640" or less permissive is not returned, this is a finding.

## Group: SRG-APP-000118-CTR-000240

**Group ID:** `V-257529`

### Rule: OpenShift must protect system journal file from any type of unauthorized access by setting owner permissions.

**Rule ID:** `SV-257529r921530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift follows the principle of least privilege, which aims to restrict access to resources based on user roles and responsibilities. This separation of privileges helps mitigate the risk of unauthorized modifications or unauthorized access by users or processes that do not need to interact with the file. Protecting the system journal file from unauthorized access helps safeguard against potential security threats. The system journal file contains critical log data that is vital for system analysis, troubleshooting, and security auditing. Unauthorized users gaining access to the file may exploit vulnerabilities, tamper with logs, or extract sensitive information. By setting strict file owner permissions, OpenShift minimizes the risk of unauthorized individuals or processes accessing or modifying the journal file, reducing the likelihood of security breaches.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "system journal" file is group-owned by systemd-journal and owned by root by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; machine_id=$(systemd-machine-id-setup --print); stat -c "%U %G" /var/log/journal/$machine_id/system.journal' 2>/dev/null; done Example output: ip-10-0-150-1 root systemd-journal If "root" is not returned as the owner, this is a finding. If "systemd-journald" is not returned as the group owner, this is a finding.

## Group: SRG-APP-000118-CTR-000240

**Group ID:** `V-257530`

### Rule: OpenShift must protect log directory from any type of unauthorized access by setting file permissions.

**Rule ID:** `SV-257530r921533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files contain sensitive information such as user credentials, system configurations, and potentially even security-related events. Unauthorized access to log files can expose this sensitive data to malicious actors. By protecting the log directory, OpenShift ensures that only authorized users or processes can access the log files, preserving the confidentiality of the information contained within them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log" directory has a mode of "0755" or less by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; stat -c "%a %n" /var/log' 2>/dev/null; done If a value of "0755" or less permissive is not returned, this is a finding.

## Group: SRG-APP-000118-CTR-000240

**Group ID:** `V-257531`

### Rule: OpenShift must protect log directory from any type of unauthorized access by setting owner permissions.

**Rule ID:** `SV-257531r921536_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift follows the principle of least privilege, which aims to restrict access to resources based on user roles and responsibilities. This separation of privileges helps mitigate the risk of unauthorized modifications or unauthorized access by users or processes that do not need to interact with the file. Protecting the /var/log directory from unauthorized access helps safeguard against potential security threats. Unauthorized users gaining access to the file may exploit vulnerabilities, tamper with logs, or extract sensitive information. By setting strict file owner permissions, OpenShift minimizes the risk of unauthorized individuals or processes accessing or modifying the directory, reducing the likelihood of security breaches.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log" directory is group-owned by root by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; stat -c "%G" /var/log' 2>/dev/null; done If "root" is not returned as a result, this is a finding.

## Group: SRG-APP-000118-CTR-000240

**Group ID:** `V-257532`

### Rule: OpenShift must protect pod log files from any type of unauthorized access by setting owner permissions.

**Rule ID:** `SV-257532r921539_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Pod log files may contain sensitive information such as application data, user credentials, or system configurations. Unauthorized access to these log files can expose sensitive data to malicious actors. By setting owner permissions, OpenShift ensures that only authorized users or processes with the necessary privileges can access the pod log files, preserving the confidentiality of the logged information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the permissions and ownership of files located under "/var/log/pods" that store the output of pods are set to protect from unauthorized access. 1. Verify the files are readable only by the owner by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; find /var/log/pods/ -type f \( -perm /022 -o -perm /044 \)' 2>/dev/null; done If any files are returned, this is a finding. 2. Verify files are group-owned by root and owned by root by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; find /var/log/pods/ -type f \! -user 0' 2>/dev/null; done (Example output: ip-10-0-150-1 root root) If "root" is not returned as the owner, this is a finding. If "root" is not returned as the group owner, this is a finding.

## Group: SRG-APP-000119-CTR-000245

**Group ID:** `V-257533`

### Rule: OpenShift must protect audit information from unauthorized modification.

**Rule ID:** `SV-257533r921542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult if not impossible to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from all unauthorized access. This includes read, write, and copy access. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, applications with user interfaces to audit records must not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-APP-000119-CTR-000245, SRG-APP-000120-CTR-000250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n ""$HOSTNAME ""; grep "^\-e\s2\s*$" /etc/audit/audit.rules /etc/audit/rules.d/* || echo "not found"' 2>/dev/null; done If the check returns "not found", the audit system is not set to be immutable by adding the ""-e 2"" option to the ""/etc/audit/audit.rules"", this is a finding.

## Group: SRG-APP-000121-CTR-000255

**Group ID:** `V-257534`

### Rule: OpenShift must prevent unauthorized changes to logon UIDs.

**Rule ID:** `SV-257534r921545_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logon UIDs are used to uniquely identify and authenticate users within the system. By preventing unauthorized changes to logon UIDs, OpenShift ensures that user identities remain consistent and accurate. This helps maintain the integrity of user accounts and ensures that users can be properly authenticated and authorized for their respective resources and actions. User accounts and associated logon UIDs are important for security monitoring, auditing, and accountability purposes. By preventing unauthorized changes to logon UIDs, OpenShift ensures that actions performed by users can be accurately traced and attributed to the correct user account. This helps with incident investigation, compliance requirements, and maintaining overall system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes to logon UIDs by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -i immutable /etc/audit/audit.rules || echo "not found"' 2>/dev/null; done If the login UIDs are not set to be immutable by adding the "--loginuid-immutable" option to the "/etc/audit/audit.rules", this is a finding.

## Group: SRG-APP-000121-CTR-000255

**Group ID:** `V-257535`

### Rule: OpenShift must protect audit tools from unauthorized access.

**Rule ID:** `SV-257535r921548_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-APP-000121-CTR-000255, SRG-APP-000122-CTR-000260, SRG-APP-000123-CTR-000265</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
List the users and groups who have permission to view the cluster logging configuration by executing the following two commands: oc policy who-can view ClusterLogging -n openshift-logging oc policy who-can view ClusterLoggingForwarder -n openshift-logging Review the list of users and groups who have view access to the cluster logging resources. If any user or group listed must not have access to view the cluster logging resources, this is a finding.

## Group: SRG-APP-000126-CTR-000275

**Group ID:** `V-257536`

### Rule: OpenShift must use FIPS-validated cryptographic mechanisms to protect the integrity of log information.

**Rule ID:** `SV-257536r921551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To fully investigate an incident and to have trust in the audit data that is generated, it is important to put in place data protections. Without integrity protections, unauthorized changes may be made to the audit files and reliable forensic analysis and discovery of the source of malicious system activity may be degraded. Although digital signatures are one example of protecting integrity, this control is not intended to cause a new cryptographic hash to be generated every time a record is added to a log file. Integrity protections can also be implemented by using cryptographic techniques for security function isolation and file system protections to protect against unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Cluster Log Forwarder is using an encrypted transport by executing the following: oc get clusterlogforwarder -n openshift-logging For each Cluster Log Forwarder, run the following command to display the configuration. oc describe clusterlogforwarder <name> -n openshift-logging Review the configuration and determine if the transport is secure, such as tls:// or https://. If there are any transports configured that are not secured by TLS, this is a finding.

## Group: SRG-APP-000131-CTR-000285

**Group ID:** `V-257537`

### Rule: OpenShift must verify container images.

**Rule ID:** `SV-257537r921554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The container platform must be capable of validating that container images are signed and that the digital signature is from a recognized and source approved by the organization. Allowing any container image to be introduced into the registry and instantiated into a container can allow for services to be introduced that are not trusted and may contain malicious code, which introduces unwanted services. These unwanted services can cause harm and security risks to the hosting server, the container platform, other services running within the container platform, and the overall organization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if a policy has been put in place by running the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; cat /etc/containers/policy.json' 2>/dev/null; done If the policy is not set to "reject" by default, or the signature keys are not configure appropriately on the registries, this is a finding. The following is an example of how this will look on a system using Red Hat's public registries: <pre> { "default": [{"type": "reject"}], "transports": { "docker": { "registry.access.redhat.com": [ { "type": "signedBy", "keyType": "GPGKeys", "keyPath": "/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release" } ], "registry.redhat.io": [ { "type": "signedBy", "keyType": "GPGKeys", "keyPath": "/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release" } ], ... }

## Group: SRG-APP-000141-CTR-000320

**Group ID:** `V-257538`

### Rule: OpenShift must contain only container images for those capabilities being offered by the container platform.

**Rule ID:** `SV-257538r921557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing container images to reside within the container platform registry that are not essential to the capabilities being offered by the container platform becomes a potential security risk. By allowing these nonessential container images to exist, the possibility for accidental instantiation exists. The images may be unpatched, not supported, or offer nonapproved capabilities. Those images for customer services are considered essential capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To review the container images within the container platform registry, execute the following: oc get images Review the container platform container images to validate that only container images necessary for the functionality of the information system are present. If unnecessary container images exist, this is a finding.

## Group: SRG-APP-000142-CTR-000325

**Group ID:** `V-257539`

### Rule: OpenShift runtime must enforce ports, protocols, and services that adhere to the PPSM CAL.

**Rule ID:** `SV-257539r921560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift Container Platform uses several IPV4 and IPV6 ports and protocols to facilitate cluster communication and coordination. Not all these ports are identified and approved by the PPSM CAL. Those ports, protocols, and services that fall outside the PPSM CAL must be blocked by the runtime or registered. Instructions on the PPSM can be found in DOD Instruction 8551.01 Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the OpenShift documentation and configuration. For additional information, refer to https://docs.openshift.com/container-platform/4.12/installing/installing_platform_agnostic/installing-platform-agnostic.html. 1. Interview the application administrator. 2. Identify the TCP/IP port numbers OpenShift is configured to use and is utilizing by using a combination of relevant OS commands and application configuration utilities. 3. Identify the network ports and protocols that are used by kube-apiserver by executing the following: oc get configmap kube-apiserver-pod -n openshift-kube-apiserver -o "jsonpath={ .data['pod\.yaml'] }" | jq '..|.containerPort?' | grep -v "null" oc get configmap kube-apiserver-pod -n openshift-kube-apiserver -o "jsonpath={ .data['pod\.yaml'] }" | jq '..|.hostPort?' | grep -v "null" oc get services -A --show-labels | grep apiserver | awk '{print $6,$8}' | grep apiserver 4. Identify the network ports and protocols used by kube-scheduler by executing the following: oc get configmap kube-scheduler-pod -n openshift-kube-scheduler -o "jsonpath={ .data['pod\.yaml'] }" | jq '..|.containerPort?' | grep -v "null" oc get services -A --show-labels | grep scheduler | awk '{print $6,$8}' | grep scheduler 5. Identify the network ports and protocols used by kube-controller-manager by executing the following: oc get configmap kube-controller-manager-pod -n openshift-kube-controller-manager -o "jsonpath={ .data['pod\.yaml'] }" | jq '..|.containerPort?' | grep -v "null" oc get services -A --show-labels | grep kube-controller 6. Identify the network ports and protocols used by etcd by executing the following: oc get configmap etcd-pod -n openshift-etcd -o "jsonpath={ .data['pod\.yaml'] }" | grep -Po '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]+' | sort -u Review the PPSM web page at: http://www.disa.mil/Network-Services/Enterprise-Connections/PPSM. Review the PPSM Category Assurance List (CAL) directly at the following link: https://disa.deps.mil/ext/cop/iase/ppsm/Pages/cal.aspx. Verify the ports used by the OpenShift are approved by the PPSM CAL. If the ports, protocols, and services have not been registered locally, this is a finding.

## Group: SRG-APP-000148-CTR-000335

**Group ID:** `V-257540`

### Rule: OpenShift must disable root and terminate network connections.

**Rule ID:** `SV-257540r921563_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Direct login as the "root" user must be disabled to prevent unrestricted access and control over the entire system. Terminating an idle session within a short time reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single operating system level network connection. This does not mean that the application terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-APP-000148-CTR-000335, SRG-APP-000190-CTR-000500</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH is restricted from logging on as root and network connections are terminated. Prevent logging on directly as "root" using SSH by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -i PermitRootLogin /etc/ssh/sshd_config' 2>/dev/null; done If the "PermitRootLogin" keyword is set to "yes", is missing, or is commented out, this is a finding. Verify all network connections associated with SSH traffic are automatically terminated at the end of the session or after 10 minutes of inactivity. Check the "ClientAliveCountMax" and ClientAliveInterval by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -i clientalive /etc/ssh/sshd_config ' 2>/dev/null; done If "ClientAliveCountMax" do not exist, is not set to a value of "0" in "/etc/ssh/sshd_config", or is commented out, this is a finding. If "ClientAliveInterval" does not exist, or has a value of > 600 in "/etc/ssh/sshd_config", or is commented out, this is a finding.

## Group: SRG-APP-000149-CTR-000355

**Group ID:** `V-257541`

### Rule: OpenShift must use multifactor authentication for network access to accounts.

**Rule ID:** `SV-257541r921566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged and nonprivileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. A nonprivileged account is any information system account with authorizations of a nonprivileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). Satisfies: SRG-APP-000149-CTR-000355, SRG-APP-000150-CTR-000360</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the authentication operator is configured to use either an LDAP or a OpenIDConnect provider by executing the following: oc get oauth cluster -o jsonpath="{.spec.identityProviders[*].type}{'\n'}" If the output lists any other type besides LDAP or OpenID, this is a finding.

## Group: SRG-APP-000156-CTR-000380

**Group ID:** `V-257542`

### Rule: OpenShift must use FIPS-validated SHA-1 or higher hash function to provide replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-257542r921569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. Anti-replay is a cryptographically based mechanism; thus, it must use FIPS-approved algorithms. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Note that the anti-replay service is implicit when data contains monotonically increasing sequence numbers and data integrity is assured. Use of DOD PKI is inherently compliant with this requirement for user and device access. Use of Transport Layer Security (TLS), including application protocols such as HTTPS and DNSSEC, that use TLS/SSL as the underlying security protocol is also complaint. Configure the information system to use the hash message authentication code (HMAC) algorithm for authentication services to Kerberos, SSH, web management tool, and any other access method.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the authentication operator is configured to use a secure transport to an OpenIDConnect provider: oc get oauth cluster -o jsonpath="{.spec.identityProviders[*]}{'\n'}" If the transport is not secure (ex. HTTPS), this is a finding.

## Group: SRG-APP-000172-CTR-000440

**Group ID:** `V-257543`

### Rule: OpenShift must use FIPS validated LDAP or OpenIDConnect.

**Rule ID:** `SV-257543r921572_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected on entry, in transmission, during authentication, and when stored. If compromised at any of these security points, a nefarious user can use the password along with stolen user account information to gain access or to escalate privileges. The container platform may require account authentication during container platform tasks and before accessing container platform components (e.g., runtime, registry, and keystore). During any user authentication, the container platform must use FIPS-validated SHA-2 or later protocol to protect the integrity of the password authentication process. Satisfies: SRG-APP-000172-CTR-000440, SRG-APP-000024-CTR-000060, SRG-APP-000025-CTR-000065, SRG-APP-000065-CTR-000115, SRG-APP-000151-CTR-000365, SRG-APP-000152-CTR-000370, SRG-APP-000157-CTR-000385, SRG-APP-000163-CTR-000395, SRG-APP-000164-CTR-000400, SRG-APP-000165-CTR-000405, SRG-APP-000166-CTR-000410, SRG-APP-000167-CTR-000415, SRG-APP-000168-CTR-000420, SRG-APP-000169-CTR-000425, SRG-APP-000170-CTR-000430, SRG-APP-000171-CTR-000435, SRG-APP-000173-CTR-000445, SRG-APP-000174-CTR-000450, SRG-APP-000177-CTR-000465, SRG-APP-000317-CTR-000735, SRG-APP-000318-CTR-000740, SRG-APP-000345-CTR-000785, SRG-APP-000391-CTR-000935, SRG-APP-000397-CTR-000955, SRG-APP-000401-CTR-000965, SRG-APP-000402-CTR-000970</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the authentication operator is configured to use either an LDAP or a OpenIDConnect provider by executing the following: oc get oauth cluster -o jsonpath="{.spec.identityProviders[*].type}{'\n'}" If the output lists any other type besides LDAP or OpenID, this is a finding.

## Group: SRG-APP-000190-CTR-000500

**Group ID:** `V-257544`

### Rule: OpenShift must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity.

**Rule ID:** `SV-257544r921575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In OpenShift, the "session token inactivity timeout" on OAuth clients is set to ensure security and protect against potential unauthorized access to user sessions. OAuth is an open standard for secure authorization and authentication between different services. By setting a session token inactivity timeout, OpenShift reduces the risk of unauthorized access to a user's session if they become inactive or leave their session unattended. It helps protect against potential session hijacking or session replay attacks. OpenShift is designed to efficiently manage resources across the cluster. Active sessions consume resources such as memory and CPU. By setting timeouts, OpenShift can reclaim these resources if a session remains inactive for a certain duration. This helps optimize resource allocation and ensures that resources are available for other active sessions and workloads. OpenShift provides the ability for automatic time-out to debug node sessions on client versions starting with 4.8.36. By setting a time-out, OpenShift can manage the allocation of resources efficiently. It prevents the scenario where a debug session remains active indefinitely, potentially consuming excessive resources and impacting the performance of other applications running on the cluster. Allowing debug sessions to run indefinitely could introduce security risks. If a session is left unattended or unauthorized access is gained to a debug session, it could potentially compromise the application or expose sensitive information. By enforcing time-outs, OpenShift reduces the window of opportunity for unauthorized access and helps maintain the security and stability of the platform. Satisfies: SRG-APP-000190-CTR-000500, SRG-APP-000389-CTR-000925</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On each administrators terminal, verify the OC client version includes the required idle timeout by executing the following. oc version If the client version < "4.8.36", this is a finding. Determine if the session token inactivity timeout is set on the oauthclients by executing the following. oc get oauthclients -ojsonpath='{range .items[*]}{.metadata.name}{"\t"}{.accessTokenInactivityTimeoutSeconds}{"\n"}' The output will list each oauth client name followed by a number. The number represents the timeout in seconds. If no number is displayed, or the timeout value is >600, this is a finding.

## Group: SRG-APP-000211-CTR-000530

**Group ID:** `V-257545`

### Rule: OpenShift must separate user functionality (including user interface services) from information system management functionality.

**Rule ID:** `SV-257545r921578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Red Hat Enterprise Linux CoreOS (RHCOS) is a single-purpose container operating system. RHCOS is only supported as a component of the OpenShift Container Platform. Remote management of the RHCOS nodes is performed at the OpenShift Container Platform API level. Any direct access to the RHCOS nodes is unnecessary. RHCOS only has two user accounts defined, root(0) and core(1000). These are the only two user accounts that should exist on the RHCOS nodes. As any administrative access or actions are to be done through the OpenShift Container Platform's administrative APIs, direct logon access to the RHCOS host must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that root and core are the only user accounts on the nodes by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; cat /etc/passwd' 2>/dev/null; done The output will look similar to: <node_name> root:x:0:0:root:/root:/bin/bash core:x:1000:1000:CoreOS Admin:/var/home/core:/bin/bash containers:x:993:995:User for housing the sub ID range for containers:/var/home/containers:/sbin/nologin If there are any user accounts in addition to root, containers, and core, this is a finding. Verify the root and core users are set to disable password logon by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e "^root" -e "^core" /etc/shadow' 2>/dev/null; done The output will look similar to: <node_name> root:*:18367:0:99999:7::: core:*:18939:0:99999:7::: If the password entry has anything other than '*', this is a finding.

## Group: SRG-APP-000219-CTR-000550

**Group ID:** `V-257546`

### Rule: OpenShift must protect authenticity of communications sessions with the use of FIPS-validated 140-2 or 140-3 validated cryptography.

**Rule ID:** `SV-257546r921581_rule`
**Severity:** high

**Description:**
<VulnDiscussion>FIPS compliance is one of the most critical components required in highly secure environments, to ensure that only supported cryptographic technologies are allowed on nodes. Because FIPS must be enabled before the operating system used by the cluster boots for the first time, FIPS cannot be disabled after a cluster is deployed. OpenShift employs industry-validated cryptographic algorithms, key management practices, and secure protocols, reducing the likelihood of cryptographic vulnerabilities and attacks. Satisfies: SRG-APP-000219-CTR-000550, SRG-APP-000635-CTR-001405, SRG-APP-000126-CTR-000275, SRG-APP-000411-CTR-000995, SRG-APP-000412-CTR-001000, SRG-APP-000416-CTR-001015, SRG-APP-000514-CTR-001315</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To validate the OpenShift cluster is running with FIPS enabled on each node by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; sysctl crypto.fips_enabled' 2>/dev/null; done If any lines of output end in anything other than 1, this is a finding.

## Group: SRG-APP-000233-CTR-000585

**Group ID:** `V-257547`

### Rule: OpenShift runtime must isolate security functions from nonsecurity functions.

**Rule ID:** `SV-257547r921584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in several ways, including through the provision of security kernels via processor rings or processor modes. For nonkernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Operating systems restrict access to security functions using access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Red Hat Enterprise Linux CoreOS (RHCOS) verifies correct operation of all security functions by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; getenforce' 2>/dev/null; done If "SELinux" is not active and not in "Enforcing" mode, this is a finding.

## Group: SRG-APP-000243-CTR-000600

**Group ID:** `V-257548`

### Rule: OpenShift must prevent unauthorized and unintended information transfer via shared system resources and enable page poisoning.

**Rule ID:** `SV-257548r921587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling page poisoning in OpenShift improves memory safety, mitigates memory corruption vulnerabilities, aids in fault isolation, assists with debugging. It enhances the overall security and stability of the platform, reducing the risk of memory-related exploits and improving the resilience of applications running on OpenShift.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the current CoreOS boot loader configuration has page poisoning enabled by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep page_poison /boot/loader/entries/*.conf|| echo "not found"' 2>/dev/null; done If "page_poison" is not set to "1" or returns "not found", this is a finding.

## Group: SRG-APP-000243-CTR-000600

**Group ID:** `V-257549`

### Rule: OpenShift must disable virtual syscalls.

**Rule ID:** `SV-257549r921590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virtual syscalls are a mechanism that allows user-space programs to make privileged system calls without transitioning to kernel mode. However, this feature can introduce additional security risks. Disabling virtual syscalls helps to mitigate potential vulnerabilities associated with this mechanism. By reducing the attack surface and limiting the ways in which user-space programs can interact with the kernel, OpenShift can enhance the overall security posture of the platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the current CoreOS boot loader configuration has virtual syscalls disabled by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep vsyscall=none boot/loader/entries/*.conf || echo "not found"' 2>/dev/null; done If "vsyscall" is not set to "none" or returns "not found", this is a finding.

## Group: SRG-APP-000243-CTR-000600

**Group ID:** `V-257550`

### Rule: OpenShift must enable poisoning of SLUB/SLAB objects.

**Rule ID:** `SV-257550r921593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling poisoning of SLUB/SLAB objects, OpenShift can detect and identify use-after-free scenarios more effectively. The poisoned objects are marked as invalid or inaccessible, causing crashes or triggering alerts when an application attempts to access them. This helps identify and mitigate potential security vulnerabilities before they can be exploited.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Red Hat Enterprise Linux CoreOS (RHCOS) is configured to enable poisoning of SLUB/SLAB objects to mitigate use-after-free vulnerabilities by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep slub_debug /boot/loader/entries/*.conf ' 2>/dev/null; done If "slub_debug" is not set to "P" or is missing, this is a finding.

## Group: SRG-APP-000243-CTR-000600

**Group ID:** `V-257551`

### Rule: OpenShift must set the sticky bit for world-writable directories.

**Rule ID:** `SV-257551r921596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing world-writable permissions or setting the sticky bit helps enforce access control on directories within the OpenShift platform. World-writable permissions allow any user to modify or delete files within the directory, which can introduce security risks. By removing these permissions or setting the sticky bit, OpenShift restricts modifications to the directory's owner and prevents unauthorized or unintended changes by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all world-writable directories have the sticky bit set. List any world-writeable directories that do not have the sticky bit set by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; find / -type d \( -perm -0002 -a ! -perm -1000 ! -path "/var/lib/containers/*" ! -path "/var/lib/kubelet/pods/*" ! -path "/sysroot/ostree/deploy/*" \) -print 2>/dev/null' 2>/dev/null; done If there are any directories listed in the results, this is a finding.

## Group: SRG-APP-000243-CTR-000600

**Group ID:** `V-257552`

### Rule: OpenShift must restrict access to the kernel buffer.

**Rule ID:** `SV-257552r921599_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting access to the kernel buffer in OpenShift is crucial for preventing unauthorized access, protecting system stability, mitigating kernel-level attacks, preventing information leakage, and adhering to the principle of least privilege. It enhances the security posture of the platform and helps maintain the confidentiality, integrity, and availability of critical system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Red Hat Enterprise Linux CoreOS (RHCOS) is configured to restrict access to the kernel message buffer. Check the status of the kernel.dmesg_restrict kernel parameter by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; sysctl kernel.dmesg_restrict' 2>/dev/null; done If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding.

## Group: SRG-APP-000243-CTR-000600

**Group ID:** `V-257553`

### Rule: OpenShift must prevent kernel profiling.

**Rule ID:** `SV-257553r921602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel profiling involves monitoring and analyzing the behavior of the kernel, including its internal operations and system calls. This level of access and visibility into the kernel can potentially be exploited by attackers to gather sensitive information or launch attacks. By preventing kernel profiling, the attack surface is minimized and the risk of unauthorized access or malicious activities targeting the kernel is reduced. Kernel profiling can introduce additional overhead and resource utilization, potentially impacting the stability and performance of the system. Profiling tools and techniques often involve instrumenting the kernel code, injecting hooks, or collecting detailed data, which may interfere with the normal operation of the kernel. By disallowing kernel profiling, OpenShift helps ensure the stability and reliability of the platform, preventing any potential disruptions caused by profiling activities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Red Hat Enterprise Linux CoreOS (RHCOS) is configured to prevent kernel profiling by unprivileged users. Check the status of the kernel.perf_event_paranoid kernel parameter by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; sysctl kernel.perf_event_paranoid ' 2>/dev/null; done If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding.

## Group: SRG-APP-000246-CTR-000605

**Group ID:** `V-257554`

### Rule: OpenShift must restrict individuals the ability to launch organizational-defined Denial-of-Service (DOS) attacks against other information systems by setting a default Resource Quota.

**Rule ID:** `SV-257554r921605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift allows administrators to define resource quotas on a namespace basis. This allows tailoring of the shared resources based on a project needs. However, when a new project is created, unless a default project resource quota is configured, that project will not have any limits or quotas defined. This could allow someone to create a new project and then deploy services that exhaust or overuse the shared cluster resources. Thus, it is necessary to ensure that there is a default resource quota configured for all new projects. A Cluster Admin may increase resource quotas on a given project namespace, if that project requires additional resources at any time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for Resource Quota. Verify a default project template is defined by executing the following: oc get project.config.openshift.io/cluster -o jsonpath="{.spec.projectRequestTemplate.name}" If no project request template is in use by the project config, this is a finding. Verify the project template includes a default resource quota. oc get templates/<PROJECT-REQUEST-TEMPLATE> -n openshift-config -o jsonpath="{.objects[?(.kind=='ResourceQuota')]}{'\n'}" Replace <PROJECT-REQUEST-TEMPLATE> with the name of the project request template returned from the earlier query. If the project template is not defined, or there are no ResourceQuota definitions in it, this is a finding.

## Group: SRG-APP-000246-CTR-000605

**Group ID:** `V-257555`

### Rule: OpenShift must restrict individuals the ability to launch organizational-defined Denial-of-Service (DOS) attacks against other information systems by rate-limiting.

**Rule ID:** `SV-257555r921608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By setting rate limits, OpenShift can control the number of requests or connections allowed from a single source within a specific period. This prevents an excessive influx of requests that can overwhelm the application and degrade its performance or availability. Setting rate limits also ensures fair resource allocation, prevents service degradation, protects backend systems, and enhances overall security. Along with, helping to maintain the availability, performance, and security of the applications hosted on the platform, contributing to a reliable and robust application infrastructure. OpenShift has an option to set the rate limit for Routes (refer to link below) when creating new Routes. All routes outside the OpenShift namespaces and the kube namespaces must use the rate-limiting annotations. https://docs.openshift.com/container-platform/4.9/networking/routes/route-configuration.html#nw-route-specific-annotations_route-configuration</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all namespaces except those that start with kube-* or openshift-* use the rate-limiting annotation by executing the following: oc get routes --all-namespaces -o json | jq '[.items[] | select(.metadata.namespace | startswith("kube-") or startswith("openshift-") | not) | select(.metadata.annotations["haproxy.router.openshift.io/rate-limit-connections"] == "true" | not) | .metadata.name]' If the above command returns any namespaces, this is a finding.

## Group: SRG-APP-000297-CTR-000705

**Group ID:** `V-257556`

### Rule: OpenShift must display an explicit logout message indicating the reliable termination of authenticated communication sessions.

**Rule ID:** `SV-257556r921611_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The OpenShift CLI tool includes an explicit logout option. The web console's default logout will invalidate the user's session token and redirect back to the console page, which will redirect the user to the authentication page. There is no explicit logout message. And in addition, if the IdP provider type is OIDC, the session token from the SSO provider will remain valid, which would effectively keep the user logged in. To correct this, the web console needs to be configured to redirect the user to a logout page. If using an OIDC provider, this would be the logout page for that provider.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the logout redirect setting in web console configuration is set by executing the following: oc get console.config.openshift.io cluster -o jsonpath='{.spec.authentication.logoutRedirect}{"\n"}' If nothing is returned, this is a finding.

## Group: SRG-APP-000342-CTR-000775

**Group ID:** `V-257557`

### Rule: Container images instantiated by OpenShift must execute using least privileges.

**Rule ID:** `SV-257557r921614_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Container images running on OpenShift must support running as any arbitrary UID. OpenShift will then assign a random, nonprivileged UID to the running container instance. This avoids the risk from containers running with specific UIDs that could map to host service accounts, or an even greater risk of running as root level service. OpenShift uses the default security context constraints (SCC), restricted, to prevent containers from running as root or other privileged user IDs. Pods must be configured to use an SCC policy that allows the container to run as a specific UID, including root(0) when approved. Only a cluster administrator may grant the change of an SCC policy. https://docs.openshift.com/container-platform/4.8/openshift_images/create-images.html#images-create-guide-openshift_create-images Satisfies: SRG-APP-000342-CTR-000775, SRG-APP-000142-CTR-000330, SRG-APP-000243-CTR-000595</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SCC: 1. Identify any SCC policy that allows containers to access the host network or filesystem resources, or allows privileged containers or where runAsUser is not MustRunAsRange by executing the following: oc get scc -ojson | jq '.items[]|select(.allowHostIPC or .allowHostPID or .allowHostPorts or .allowHostNetwork or .allowHostDirVolumePlugin or .allowPrivilegedContainer or .runAsUser.type != "MustRunAsRange" )|.metadata.name,{"Group:":.groups},{"User":.users}' For each SCC listed, if any of those users or groups are anything other than the following, this is a finding: * system:cluster-admins * system:nodes * system:masters * system:admin * system:serviceaccount:openshift-infra:build-controller * system:serviceaccount:openshift-infra:pv-recycler-controller * system:serviceaccount:openshift-machine-api:machine-api-termination-handler The group "system:authenticated" is the default group for any authenticated user, this group should only be associated with the restricted profile. If this group is listed under any other SCC Policy, or the restricted SCC policy has been altered to allow any of the nonpermitted actions, this is a finding. 2. Determine if there are any cluster roles or local roles that allow the use of use of nonpermitted SCC policies. The following commands will print the role's name and namespace, followed by a list of resource names and if that resource is an SCC. oc get clusterrole.rbac -ojson | jq -r '.items[]|select(.rules[]?|select( (.apiGroups[]? == ("security.openshift.io")) and (.resources[]? == ("securitycontextconstraints")) and (.verbs[]? == ("use"))))|.metadata.name,{"scc":(.rules[]?|select((.resources[]? == ("securitycontextconstraints"))).resourceNames[]?)}' oc get role.rbac --all-namespaces -ojson | jq -r '.items[]|select(.rules[]?|select( (.apiGroups[]? == ("security.openshift.io")) and (.resources[]? == ("securitycontextconstraints")) and (.verbs[]? == ("use"))))|.metadata.name,{"scc":(.rules[]?|select((.resources[]? == ("securitycontextconstraints"))).resourceNames[]?)}' Excluding platform specific roles, identify any roles that allow use of nonpermitted SCC policies. For example, the follow output shows that the role 'examplePrivilegedRole' allows use of the 'privileged' SCC. examplePrivilegedRole { "scc": "privileged" } 3. Determine if there are any role bindings to cluster or local roles that allow use of nonpermitted SCCs by executing the following: oc get clusterrolebinding.rbac -ojson | jq -r '.items[]|select(.roleRef.kind == ("ClusterRole","Role") and .roleRef.name == (<CLUSTER_ROLE_LIST>))|{ "crb": .metadata.name, "roleRef": .roleRef, "subjects": .subjects}' oc get rolebinding.rbac --all-namespaces -ojson | jq -r '.items[]|select(.roleRef.kind == ("ClusterRole","Role") and .roleRef.name == (<LOCAL_ROLE_LIST>))|{ "crb": .metadata.name, "roleRef": .roleRef, "subjects": .subjects}' Where <CLUSTER_ROLE_LIST> and <LOCAL_ROLE_LIST> are comma-separated lists of the roles allowing use of nonpermitted SCC policies as identified above. For example: ... .roleRef.name == ("system:openshift:scc:privileged","system:openshift:scc:hostnetwork","system:openshift:scc:hostaccess") ... Excluding any platform namespaces (kube-*,openshift-*), if there are any rolebindings to roles that are not permitted, this is a finding.

## Group: SRG-APP-000357-CTR-000800

**Group ID:** `V-257558`

### Rule: Red Hat Enterprise Linux CoreOS (RHCOS) must allocate audit record storage capacity to store at least one weeks' worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-257558r921617_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To ensure RHCOS has a sufficient storage capacity in which to write the audit logs, operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify RHCOS allocates audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility. Check the size of the partition to which audit records are written (with the example being /var/log/audit/) by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; df -h /var/log/audit/' 2>/dev/null; done <node> Filesystem Size Used Avail Use% Mounted on /dev/sdb4 1.0T 27G 998G 3% /var If the audit record partition is not allocated for sufficient storage capacity, this is a finding. Note: The partition size needed to capture a week of audit records is based on the activity level of the system and the total storage capacity available. Typically, 10.0 GB of storage space for audit records should be sufficient. If the partition used is not exclusively for audit logs, then determine the amount of additional space needed to support the partition reserving enough space for audit logs.

## Group: SRG-APP-000360-CTR-000815

**Group ID:** `V-257559`

### Rule: OpenShift must configure Alert Manger Receivers to notify SA and ISSO of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-257559r921620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less). Satisfies: SRG-APP-000360-CTR-000815, SRG-APP-000474-CTR-001180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AlertManager config includes a configured receiver. 1. From the Administrator perspective on the OpenShift web console, navigate to Administration >> Cluster Settings >> Configuration >> Alertmanager. 2. View the list of receivers and inspect the configuration. 3. Verify that at least one receiver is configured as either PagerDuty, Webhook, Email, or Slack according to the organizations policy. If an alert receiver is not configured according to the organizational policy, this is a finding.

## Group: SRG-APP-000381-CTR-000905

**Group ID:** `V-257560`

### Rule: OpenShift must enforce access restrictions and support auditing of the enforcement actions.

**Rule ID:** `SV-257560r921623_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing access restrictions helps protect the OpenShift environment and its resources from unauthorized access, misuse, or malicious activities. By implementing access controls, OpenShift ensures that only authorized users or processes can access sensitive data, make changes to configurations, or perform privileged actions. This helps prevent unauthorized individuals or entities from compromising the system's security and integrity. Enforcing access restrictions and auditing the enforcement actions ensures accountability for actions performed within the OpenShift environment. It helps identify the individuals or processes responsible for specific activities, whether they are legitimate actions or potential security breaches. This accountability discourages unauthorized or malicious behavior and supports incident response and forensic investigations. Auditing the enforcement actions provides administrators with visibility into the system's security posture, access patterns, and potential security risks. It helps identify anomalies, detect suspicious activities, and monitor compliance with established security policies. This operational visibility enables timely detection and response to security incidents, ensuring the ongoing security and stability of the OpenShift environment. Satisfies: SRG-APP-000381-CTR-000905, SRG-APP-000343-CTR-000780</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OpenShift is configured to audit the execution of the "execve" system call by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e "execpriv" /etc/audit/audit.rules' 2>/dev/null; done Confirm the following rules exist on each node: -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv If the above rules are not listed on each node, this is a finding.

## Group: SRG-APP-000384-CTR-000915

**Group ID:** `V-257561`

### Rule: OpenShift must prevent the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-257561r921626_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Integrity of the OpenShift platform is handled by the cluster version operator. The cluster version operator will by default GPG verify the integrity of the release image before applying it. The release image contains a sha256 digest of machine-os-content which is used by the machine config operators for updates. On the host, the container runtime (podman) verifies the integrity of that sha256 when pulling the image before the machine config operator reads its content. Hence, there is end-to-end GPG-verified integrity for the operating system updates (as well as the rest of the cluster components which run as regular containers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify integrity of the cluster version, execute the following: oc get clusterversion version If the Cluster Version Operator is not installed or the AVAILABLE is not set to True, this is a finding. Run the following command to retrieve the Cluster Version objects in the system: oc get clusterversion version -o yaml If "verified: true", under status history for each item is not present, this is a finding.

## Group: SRG-APP-000400-CTR-000960

**Group ID:** `V-257562`

### Rule: OpenShift must set server token max age no greater than eight hours.

**Rule ID:** `SV-257562r921629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The setting for OAuth server token max age is used to control the maximum duration for which an issued OAuth access token remains valid. Access tokens serve as a form of authentication and authorization in OAuth-based systems. By setting a maximum age for these tokens, OpenShift helps mitigate security risks associated with long-lived tokens. If a token is compromised, its impact is limited to the maximum age duration, as the token will expire and become invalid after that period. It reduces the window of opportunity for unauthorized access and enhances the security of the system. By setting a maximum age for access tokens, OpenShift encourages the use of token refresh rather than relying on the same token for an extended period. Regular token refresh helps maintain a higher level of security by ensuring that tokens are periodically revalidated and rotated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check if the OAuth server token max age is configured, execute the following: oc get oauth cluster -ojsonpath='{.spec.tokenConfig.accessTokenMaxAgeSeconds}' If the output timeout value on the OAuth server is >"28800" or missing, this is a finding. Check the OAuth client token value (this can be set on each client also). Check all clients OAuth client token max age configuration by execute the following: oc get oauthclients -ojson | jq -r '.items[] | { accessTokenMaxAgeSeconds: .accessTokenMaxAgeSeconds}' If the output returns a timeout value of >"28800" for any client, this is a finding.

## Group: SRG-APP-000414-CTR-001010

**Group ID:** `V-257563`

### Rule: Vulnerability scanning applications must implement privileged access authorization to all OpenShift components, containers, and container images for selected organization-defined vulnerability scanning activities.

**Rule ID:** `SV-257563r921632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift uses service accounts to provide applications running on or off the platform access to the API service using the enforced RBAC policies. Vulnerability scanning applications that need access to the container platform may use a service account to grant that access. That service account can then be bound to the appropriate role required. The highest level of access granted is the cluster-admin role. Any account bound to that role can access and modify anything on the platform. It is strongly recommended to limit the number of accounts bound to that role. Instead, there are other predefined cluster level roles that may support the scanning to, such as the view or edit cluster roles. Additionally, custom roles may be defined to tailor fit access as needed by the scanning tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no vulnerability scanning tool is used, this requirement is Not Applicable. Identify the service accounts used by the vulnerability scanning tools. If the tool runs as a container on the platform, then service account information can be found in the pod details by executing the following: (oc get pods to list pods) oc get pod <POD_ID> -o jsonpath='{.spec.serviceAccount}{"\n"}' If no service account exists for the vulnerability scanning tool, this is a finding. View cluster role bindings to determine which role the service account is bound to by executing the following: oc get clusterrolebinding -ojson | jq '.items[]|select(.subjects[]?|select(.kind == "ServiceAccount" and .name == "ingress-to-route-controller"))|{ "crb": .metadata.name, "roleRef": .roleRef, "subjects": .subjects}' Find the role to which the service account is bound, if the service account is not bound to a cluster role, or the role does not provide sufficient access, this is a finding.

## Group: SRG-APP-000429-CTR-001060

**Group ID:** `V-257564`

### Rule: OpenShift keystore must implement encryption to prevent unauthorized disclosure of information at rest within the container platform.

**Rule ID:** `SV-257564r921635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, etcd data is not encrypted in OpenShift Container Platform. Enable etcd encryption for the cluster to provide an additional layer of data security. For example, it can help protect the loss of sensitive data if an etcd backup is exposed to the incorrect parties. When users enable etcd encryption, the following OpenShift API server and Kubernetes API server resources are encrypted: Secrets Config maps Routes OAuth access tokens OAuth authorize tokens When users enable etcd encryption, encryption keys are created. These keys are rotated on a weekly basis. Users must have these keys to restore from an etcd backup.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the API server encryption by running by executing the following: oc edit apiserver EXAMPLE OUTPUT spec: encryption: type: aescbc If the encryption type is not "aescbc", this is a finding.

## Group: SRG-APP-000435-CTR-001070

**Group ID:** `V-257565`

### Rule: OpenShift must protect against or limit the effects of all types of Denial-of-Service (DoS) attacks by employing organization-defined security safeguards by including a default resource quota.

**Rule ID:** `SV-257565r921638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DNS attacks that are internal to the container platform (exploited or otherwise malicious applications) can have a limited blast radius by adhering to least privilege RBAC and Network access: https://docs.openshift.com/container-platform/4.8/post_installation_configuration/network-configuration.html#post-install-configuring-network-policy Additionally, applications can even be limited using OpenShift Service Mesh Operator. DoS attacks coming from outside the cluster (ingress) can also be limited using an external cloud load balancer or by using 3scale API Gateway: https://docs.openshift.com/container-platform/4.8/security/container_security/security-platform.html Resource quotas must be set on a given namespace or across multiple namespaces. Using resource quotas will help to mitigate a DoS attack by limiting how much CPU, memory, and pods may be consumed in a project. This helps protect other projects (namespaces) from being denied resources to process. https://docs.openshift.com/container-platform/4.8/applications/quotas/quotas-setting-per-project.html</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the new project template includes a default resource quota by executing the following: oc get templates/project-request -n openshift-config -o jsonpath="{.objects[?(.kind=='ResourceQuota')]}{'\n'}" Review the ResourceQuota definition. If nothing is return, this is a finding.

## Group: SRG-APP-000435-CTR-001070

**Group ID:** `V-257566`

### Rule: OpenShift must protect against or limit the effects of all types of Denial-of-Service (DoS) attacks by defining resource quotas on a namespace.

**Rule ID:** `SV-257566r921641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift allows administrators to define resource quotas on a namespace basis. This allows tailoring of the shared resources based on a project needs. However, when a new project is created, unless a default project resource quota is configured, that project will not have any limits or quotas defined. This could allow someone to create a new project and then deploy services that exhaust or overuse the shared cluster resources. It is necessary to ensure that all existing namespaces with user-defined workloads have an applied resource quota configured. Using resource quotas will help to mitigate a DoS attack by limiting how much CPU, memory, and pods may be consumed in a project. This helps protect other projects (namespaces) from being denied resources to process. https://docs.openshift.com/container-platform/4.8/applications/quotas/quotas-setting-per-project.html Satisfies: SRG-APP-000435-CTR-001070, SRG-APP-000246-CTR-000605, SRG-APP-000450-CTR-001105</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: CNTR-OS-000140 is a prerequisite to this control. A Network Policy must exist to run this check. Verify that each user namespace has a ResourceQuota defined by executing the following: for ns in $(oc get namespaces -ojson | jq -r '.items[] | select((.metadata.name | startswith("openshift") | not) and (.metadata.name | startswith("kube-") | not) and .metadata.name != "default") | .metadata.name '); do oc get resourcequota -n$ns; done If the above returns any lines saying "No resources found in <PROJECT> namespace.", this is a finding. Empty output is not a finding.

## Group: SRG-APP-000439-CTR-001080

**Group ID:** `V-257567`

### Rule: OpenShift must protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-257567r921644_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift provides for two types of application level ingress types, Routes, and Ingresses. Routes have been a part of OpenShift since version 3. Ingresses were promoted out of beta in Aug 2020 (kubernetes v1.19). Routes provides for three type of TLS configuration options; Edge, Passthrough, and Re-encrypt. Each of those options provide TLS encryption over HTTP for inbound transmissions originating outside the cluster. Ingresses will have an IngressController associated that manages the routing and proxying of inbound transmissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that routes and ingress are using secured transmission ports and protocols by executing the following: oc get routes --all-namespaces Review the ingress ports, if the Ingress is not using a secure TLS transport, this is a finding.

## Group: SRG-APP-000450-CTR-001105

**Group ID:** `V-257568`

### Rule: Red Hat Enterprise Linux CoreOS (RHCOS) must implement nonexecutable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-257568r921647_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The NX bit is a hardware feature that prevents the execution of code from data memory regions. By enabling NX bit execute protection, OpenShift ensures that malicious code or exploits cannot execute from areas of memory that are intended for data storage. This helps protect against various types of buffer overflow attacks, where an attacker attempts to inject and execute malicious code in data memory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NX (no-execution) bit flag is set on the system by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; dmesg | grep Execute ' 2>/dev/null; done Example Output:([ 0.000000] NX (Execute Disable) protection: active) If "dmesg" does not show "NX (Execute Disable) protection active", check the cpuinfo settings by executing the following command: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; less /proc/cpuinfo | grep 'nx' /proc/cpuinfo | uniq' 2>/dev/null; done (Example Output: flags : fpu vme de pse tsc ms nx rdtscp lm constant_tsc...) If "flags" does not contain the "nx" flag, this is a finding.

## Group: SRG-APP-000450-CTR-001105

**Group ID:** `V-257569`

### Rule: Red Hat Enterprise Linux CoreOS (RHCOS) must implement ASLR (Address Space Layout Randomization) from unauthorized code execution.

**Rule ID:** `SV-257569r921650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASLR is a security technique that randomizes the memory layout of processes, making it more difficult for attackers to predict the location of system components and exploit memory-based vulnerabilities. By implementing ASLR, OpenShift reduces the effectiveness of common attacks such as buffer overflow, return-oriented programming (ROP), and other memory corruption exploits. ASLR enhances the resilience of the OpenShift platform by introducing randomness into the memory layout. This randomization makes it harder for attackers to exploit vulnerabilities and launch successful attacks. Even if a vulnerability exists in the system, the randomized memory layout introduced by ASLR reduces the chances of the attacker being able to reliably exploit it, increasing the overall security of the platform. ASLR is particularly effective in mitigating remote code execution attacks. By randomizing the memory layout, ASLR prevents attackers from precisely predicting the memory addresses needed to execute malicious code. This makes it significantly more challenging for attackers to successfully exploit vulnerabilities and execute arbitrary code on the system. Protection of Shared Libraries: ASLR also protects shared libraries used by applications running on OpenShift. By randomizing the base addresses of shared libraries, ASLR makes it harder for attackers to leverage vulnerabilities in shared libraries to compromise applications or gain unauthorized access to the system. It adds an extra layer of protection to prevent attacks targeting shared library vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Red Hat Enterprise Linux CoreOS (RHCOS) implements ASLR by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; sysctl kernel.randomize_va_space ' 2>/dev/null; done If "kernel.randomize_va_space" is not set to "2", this is a finding.

## Group: SRG-APP-000454-CTR-001110

**Group ID:** `V-257570`

### Rule: OpenShift must remove old components after updated versions have been installed.

**Rule ID:** `SV-257570r921653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of OpenShift components that are not removed from the container platform after updates have been installed may be exploited by adversaries by causing older components to execute which contain vulnerabilities. When these components are deleted, the likelihood of this happening is removed. Satisfies: SRG-APP-000454-CTR-001110, SRG-APP-000454-CTR-001115</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the imagepruner is configured and is not in a suspended state by executing the following: oc get imagepruners.imageregistry.operator.openshift.io/cluster -o jsonpath='{.spec}{"\n"}' Review the settings. If "suspend" is set to "true", this is a finding.

## Group: SRG-APP-000456-CTR-001125

**Group ID:** `V-257571`

### Rule: OpenShift must contain the latest images with most recent updates and execute within the container platform runtime as authorized by IAVM, CTOs, DTMs, and STIGs.

**Rule ID:** `SV-257571r921656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical to the security and stability of the container platform and the software services running on the platform to ensure that images are deployed through a trusted software supply chain. The OpenShift platform can be configured to limit and control which image source repositories may be used by the platform and the users of the platform. By configuring this to only allow users to deploy images from trusted sources, lowers the risk for a user to deploy unsafe or untested images that would be detrimental to the security and stability of the platform. In order to help users manage images, OpenShift uses image streams to provide a level of obstruction for the users. In this way the users can trigger automatic redeployments as images are updated. It is also possible to configure the image stream to periodically check the image source repository for any updates and automatically pull in the latest updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the image source policy is configured by executing the following: oc get image.config.openshift.io/cluster -o jsonpath='{.spec.registrySources}{"\nAllowedRegistriesForImport: "}{.spec.allowedRegistriesForImport}{"\n"}' If nothing is returned, this is a finding. If the registries listed under allowedRegistries, insecureRegistries, or AllowedRegistriesForImport are not from trusted sources as defined by the organization, this is a finding.

## Group: SRG-APP-000456-CTR-001130

**Group ID:** `V-257572`

### Rule: OpenShift runtime must have updates installed within the period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-257572r921659_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift runtime must be carefully monitored for vulnerabilities, and when problems are detected, they must be remediated quickly. A vulnerable runtime exposes all containers it supports, as well as the host itself, to potentially significant risk. Organizations must use tools to look for Common Vulnerabilities and Exposures (CVEs) in the runtimes deployed, to upgrade any instances at risk, and to ensure that orchestrators only allow deployments to properly maintained runtimes. Satisfies: SRG-APP-000456-CTR-001130, SRG-APP-000456-CTR-001125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To list all the imagestreams and identify which imagestream tags are configured to periodically check for updates (imagePolicy = { scheduled: true }), execute the following: oc get imagestream --all-namespaces -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{range .spec.tags[*]}{"\t"}{.name}{": "}{.importPolicy}{"\n"}' The output will be similar to: httpd 2.4: {} 2.4-el7: {} 2.4-el8: {} latest: {} : installer latest: {"scheduled":true} : installer-artifacts latest: {"scheduled":true} : Review the listing, and for each imagestream tag version that does not have the value '{"scheduled":true}' that should otherwise check for updates, this is a finding.

## Group: SRG-APP-000472-CTR-001170

**Group ID:** `V-257573`

### Rule: The Compliance Operator must be configured.

**Rule ID:** `SV-257573r921662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Compliance Operator enables continuous compliance monitoring within OpenShift. It regularly assesses the environment against defined compliance policies and automatically detects and reports any deviations. This helps organizations maintain a proactive stance towards compliance, identify potential issues in real-time, and take corrective actions promptly. The Compliance Operator assesses compliance of both the Kubernetes API resources of OpenShift Container Platform, as well as the nodes running the cluster. The Compliance Operator uses OpenSCAP, a NIST-certified tool, to scan and enforce security policies provided by the content. This allows an organization to define organizational policy to align with the SSP, combine it with standardized vendor-provided content, and periodically scan the platform in accordance with organization-defined policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Red Hat OpenShift Compliance Operator is not used, this check is Not Applicable. Note: If Red Hat OpenShift Compliance Operator is not used, run the checks manually. Review the cluster configuration to validate that all required security functions are being validated with the Compliance Operator. To determine if any scans have been applied to the cluster and the status of the scans, execute the following: oc get compliancescan -n openshift-compliance Example output: NAME PHASE RESULT ocp4-cis DONE NON-COMPLIANT ocp4-cis-manual DONE NON-COMPLIANT ocp4-cis-node-master DONE NON-COMPLIANT ocp4-cis-node-master-manual DONE NON-COMPLIANT ocp4-cis-node-worker DONE NON-COMPLIANT ocp4-cis-node-worker-manual DONE NON-COMPLIANT ocp4-moderate DONE NON-COMPLIANT ocp4-moderate-manual DONE NON-COMPLIANT rhcos4-moderate-master DONE NON-COMPLIANT rhcos4-moderate-master-manual DONE NON-COMPLIANT rhcos4-moderate-worker DONE NON-COMPLIANT rhcos4-moderate-worker-manual DONE NON-COMPLIANT If no ComplianceScan names return, the scans do not align to the organizationally-defined appropriate security functions, the command returns with an error, or any of the results show "NON-COMPLIANT" as their result, then this is a finding.

## Group: SRG-APP-000473-CTR-001175

**Group ID:** `V-257574`

### Rule: OpenShift must perform verification of the correct operation of security functions: upon startup and/or restart; upon command by a user with privileged access; and/or every 30 days.

**Rule ID:** `SV-257574r921665_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security functionality includes, but is not limited to, establishing system accounts, configuring access authorization (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. The Compliance Operator enables continuous compliance monitoring within OpenShift. It regularly assesses the environment against defined compliance policies and automatically detects and reports any deviations. This helps organizations maintain a proactive stance towards compliance, identify potential issues in real-time, and take corrective actions promptly. The Compliance Operator assesses compliance of both the Kubernetes API resources of OpenShift Container Platform, as well as the nodes running the cluster. The Compliance Operator uses OpenSCAP, a NIST-certified tool, to scan and enforce security policies provided by the content. This allows an organization to define organizational policy to align with the SSP, combine it with standardized vendor-provided content, and periodically scan the platform in accordance with organization-defined policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Red Hat OpenShift Compliance Operator is not used, this check is Not Applicable. Review the cluster configuration to validate that all required security functions are being validated with the Compliance Operator. To map the schedule of every profile through its ScanSettingBinding and output the schedules on which each Profile or TailoredProfile is run, execute the following commands: declare -A binding_profiles declare -A binding_schedule while read binding setting profiles; do binding_profiles[$binding]="$profiles"; binding_schedule[$binding]=$(oc get scansetting -n openshift-compliance $setting -ojsonpath='{.schedule}'); done < <(oc get scansettingbinding -n openshift-compliance -ojsonpath='{range .items[*]}{.metadata.name} {.settingsRef.name} {range .profiles[*]}{.name} {end}{"\n"}{end}') for binding in "${!binding_profiles[@]}"; do for profile in ${binding_profiles[$binding]}; do echo "$profile: ${binding_schedule[$binding]}"; done; done If any error is returned, this is a finding. If the schedules are not at least monthly or within the organizationally defined periodicity, this is a finding. Check the profiles that are bound to schedules by executing the following: To determine which rules are enforced by the profiles that are currently bound to the scheduled periodicities, execute the following commands: for binding in "${!binding_profiles[@]}"; do for profile in ${binding_profiles[$binding]}; do for rule in $(oc get profile.compliance $profile -n openshift-compliance -ojsonpath='{range .rules[*]}{$}{"\n"}{end}'); do echo "$rule: ${binding_schedule[$binding]}"; done; done; done | sort -u If the profiles that are bound to schedules do not cover the organization-designed security functions, this is a finding.

## Group: SRG-APP-000495-CTR-001235

**Group ID:** `V-257575`

### Rule: OpenShift must generate audit records when successful/unsuccessful attempts to modify privileges occur.

**Rule ID:** `SV-257575r921668_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide a crucial source of information for security monitoring and incident response. By generating audit records for privilege modification attempts, OpenShift enables administrators and security teams to track and investigate any unauthorized or suspicious changes to privileges. These records serve as an essential source of evidence for detecting and responding to potential security incidents. Audit records for unsuccessful attempts to modify privileges help in identifying unauthorized activities or potential attacks. If an unauthorized entity attempts to modify privileges, the audit records can serve as an early warning sign of a security threat. By monitoring and analyzing such records, administrators can detect and mitigate potential security breaches before they escalate. Audit records play a vital role in forensic analysis and investigation. In the event of a security incident or suspected compromise, audit logs for privilege modifications provide valuable information for understanding the scope and impact of the incident.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OpenShift is configured to generate audit records when successful/unsuccessful attempts to modify privileges occur by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e "key=unsuccessful-create" -e "key=unsuccessful-modification" -e "key=delete" -e "key=unsuccessful-access" -e "actions" -e "key=perm_mod" -e "audit_rules_usergroup_modification" -e "module-change" -e "logins" /etc/audit/audit.rules' 2>/dev/null; done Confirm the following rules exist on each node: -w /etc/group -p wa -k audit_rules_usergroup_modification -w /etc/gshadow -p wa -k audit_rules_usergroup_modification -w /etc/passwd -p wa -k audit_rules_usergroup_modification -w /etc/security/opasswd -p wa -k audit_rules_usergroup_modification -w /etc/shadow -p wa -k audit_rules_usergroup_modification -a always,exit -F arch=b32 -S openat,open_by_handle_at -F a2&0x40 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S openat,open_by_handle_at -F a2&0x40 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S open -F a1&0x40 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S open -F a1&0x40 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S openat,open_by_handle_at -F a2&0x40 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S openat,open_by_handle_at -F a2&0x40 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S open -F a1&0x40 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S open -F a1&0x40 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-create -a always,exit -F arch=b32 -S openat,open_by_handle_at -F a2&0x203 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S openat,open_by_handle_at -F a2&0x203 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S open -F a1&0x203 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S open -F a1&0x203 -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S openat,open_by_handle_at -F a2&0x203 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S openat,open_by_handle_at -F a2&0x203 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modmodule-changeification -a always,exit -F arch=b32 -S open -F a1&0x203 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S open -F a1&0x203 -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b64 -S truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-modification -a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-access -a always,exit -F arch=b64 -S open,truncate,ftruncate,creat,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-access -a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-access -a always,exit -F arch=b64 -S open,truncate,ftruncate,creat,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-access -w /etc/sudoers.d -p wa -k actions -w /etc/sudoers -p wa -k actions -a always,exit -F arch=b32 -S chmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S chown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchmodat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchmodat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S delete_module -F key=module-change -a always,exit -F arch=b64 -S delete_module -F key=module-change -a always,exit -F arch=b32 -S finit_module -F key=module-change -a always,exit -F arch=b64 -S finit_module -F key=module-change -a always,exit -F arch=b32 -S init_module -F key=module-change -a always,exit -F arch=b64 -S init_module -F key=module-change -w /var/log/lastlog -p wa -k logins -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S renameat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S renameat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b32 -S rename -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S rename -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b32 -S rmdir -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S rmdir -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b32 -S setxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S setxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S umount2 -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S umount2 -F auid>=1000 -F auid!=unset -F key=perm_mod If the above rules are not listed on each node, this is a finding.

## Group: SRG-APP-000496-CTR-001240

**Group ID:** `V-257576`

### Rule: OpenShift must generate audit records when successful/unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-257576r921671_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift and its components must generate audit records when modifying security objects. All the components must use the same standard so that the events can be tied together to understand what took place within the overall container platform. This must establish, correlate, and help assist with investigating the events relating to an incident, or identify those responsible. Without audit record generation, unauthorized users can modify security objects unknowingly for malicious intent creating vulnerabilities within the container platform. Satisfies: SRG-APP-000496-CTR-001240, SRG-APP-000497-CTR-001245, SRG-APP-000498-CTR-001250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Red Hat Enterprise Linux CoreOS (RHCOS) is configured to generate audit records when successful/unsuccessful attempts to modify security categories or objects occur by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e "key=privileged" -e "key=perm_mod" /etc/audit/audit.rules' 2>/dev/null; done Confirm the following rules exist on each node: -a always,exit -F arch=b64 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F path=/usr/bin/chcon -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/restorecon -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/semanage -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/setfiles -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/setsebool -F auid>=1000 -F auid!=unset -F key=privileged If the above rules are not listed on each node, this is a finding.

## Group: SRG-APP-000499-CTR-001255

**Group ID:** `V-257577`

### Rule: OpenShift must generate audit records when successful/unsuccessful attempts to delete privileges occur.

**Rule ID:** `SV-257577r921674_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records for unsuccessful attempts to delete privileges help in identifying unauthorized activities or potential attacks. If an unauthorized entity attempts to remove privileges, the audit records can serve as an early warning sign of a security threat. By monitoring and analyzing such records, administrators can detect and mitigate potential security breaches before they escalate. Audit records play a vital role in forensic analysis and investigation. In the event of a security incident or suspected compromise, audit logs for privilege deletions provide valuable information for understanding the scope and impact of the incident.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OpenShift is configured to generate audit records when successful/unsuccessful attempts to delete security privileges occur by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e "key=delete" -e "key=perm_mod" -e "key=privileged" -e "audit_rules_usergroup_modification" /etc/audit/audit.rules' 2>/dev/null; done Confirm the following rules exist on each node: -w /etc/group -p wa -k audit_rules_usergroup_modification -w /etc/gshadow -p wa -k audit_rules_usergroup_modification -w /etc/passwd -p wa -k audit_rules_usergroup_modification -w /etc/security/opasswd -p wa -k audit_rules_usergroup_modification -w /etc/shadow -p wa -k audit_rules_usergroup_modification -a always,exit -F arch=b32 -S chmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S chown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchmodat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchmodat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S renameat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S renameat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b32 -S rename -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S rename -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b32 -S rmdir -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S rmdir -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b32 -S setxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S setxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S umount2 -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S umount2 -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S unlinkat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S unlinkat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b32 -S unlink -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S unlink -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F path=/usr/bin/chage -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/chcon -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/chsh -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/crontab -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/gpasswd -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/newgrp -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/passwd -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/sudoedit -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/sudo -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/su -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/umount -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/libexec/openssh/ssh-keysign -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/libexec/pt_chown -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/pam_timestamp_check -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/postdrop -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/postqueue -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/semanage -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/setfiles -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/setsebool -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/unix_chkpwd -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/userhelper -F auid>=1000 -F auid!=unset -F key=privileged If the above rules are not listed on each node, this is a finding.

## Group: SRG-APP-000501-CTR-001265

**Group ID:** `V-257578`

### Rule: OpenShift must generate audit records when successful/unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-257578r921677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By generating audit records for security object deletions, OpenShift enables administrators and security teams to track and investigate any unauthorized or suspicious removal of security objects. These records serve as valuable evidence for detecting and responding to potential security incidents. Audit records for unsuccessful attempts to delete security objects help in identifying unauthorized activities or potential attacks. If an unauthorized entity attempts to delete security objects, the audit records can serve as an early warning sign of a security threat. By monitoring and analyzing such records, administrators can detect and mitigate potential security breaches before they escalate. Audit records play a vital role in forensic analysis and investigation. In the event of a security incident or suspected compromise, audit logs for security object deletions provide valuable information for understanding the scope and impact of the incident. Satisfies: SRG-APP-000501-CTR-001265, SRG-APP-000502-CTR-001270</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Red Hat Enterprise Linux CoreOS (RHCOS) is configured to generate audit records when successful/unsuccessful attempts to delete security objects or categories of information occur by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e "key=access" -e "key=delete" -e "key=unsuccessful-delete" -e "key=privileged" -e "key=perm_mod" /etc/audit/audit.rules' 2>/dev/null; done Confirm the following rules exist on each node: -a always,exit -F arch=b32 -S unlink,unlinkat,rename,renameat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-delete -a always,exit -F arch=b64 -S unlink,unlinkat,rename,renameat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=unsuccessful-delete -a always,exit -F arch=b32 -S unlink,unlinkat,rename,renameat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-delete -a always,exit -F arch=b64 -S unlink,unlinkat,rename,renameat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=unsuccessful-delete -a always,exit -F arch=b32 -S chmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S chown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchmodat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchmodat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchmod -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S fsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S lsetxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S removexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S renameat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S renameat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S renameat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b64 -S renameat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S renameat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S renameat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S rename -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S rename -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S rename -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b64 -S rename -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S rename -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S rename -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S rmdir -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S rmdir -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b32 -S setxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S setxattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S umount2 -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S umount2 -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S unlinkat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S unlinkat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S unlinkat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b64 -S unlinkat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S unlinkat -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S unlinkat -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S unlink -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S unlink -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S unlink -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b64 -S unlink -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S unlink -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F arch=b32 -S unlink -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=access -a always,exit -F path=/usr/bin/chage -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/chcon -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/chsh -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/crontab -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/gpasswd -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/newgrp -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/passwd -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/sudoedit -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/sudo -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/su -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/bin/umount -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/libexec/openssh/ssh-keysign -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/libexec/pt_chown -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/pam_timestamp_check -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/postdrop -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/postqueue -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/semanage -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/setfiles -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/setsebool -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/unix_chkpwd -F auid>=1000 -F auid!=unset -F key=privileged -a always,exit -F path=/usr/sbin/userhelper -F auid>=1000 -F auid!=unset -F key=privileged If the above rules are not listed on each node, this is a finding.

## Group: SRG-APP-000503-CTR-001275

**Group ID:** `V-257579`

### Rule: OpenShift must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-257579r921680_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide valuable information for security monitoring and intrusion detection. By generating audit logs for logon attempts, OpenShift enables administrators and security teams to track and investigate any unauthorized or suspicious access attempts. These records serve as a vital source of information for detecting and responding to potential security breaches or unauthorized logon activities. Generating audit records for logon attempts supports user accountability. Audit logs provide a trail of logon activities, allowing administrators to attribute specific logon events to individual users or entities. This promotes accountability and helps in identifying any unauthorized access attempts or suspicious behavior by specific users. By monitoring logon activity logs, administrators and security teams can identify unusual or suspicious patterns of logon attempts. Forensic analysts can examine these records to reconstruct the timeline of logon activities and determine the scope and nature of the incident.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that logons are audited by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n ""$HOSTNAME ""; grep ""logins"" /etc/audit/audit.rules /etc/audit/rules.d/*' 2>/dev/null; done The output will look similar to: node-name /etc/audit/<file>:-w /var/run/faillock -p wa -k logins /etc/audit/<file>:-w /var/log/lastlog -p wa -k logins If the two rules above are not found on each node, this is a finding.

## Group: SRG-APP-000504-CTR-001280

**Group ID:** `V-257580`

### Rule: Red Hat Enterprise Linux CoreOS (RHCOS) must be configured to audit the loading and unloading of dynamic kernel modules.

**Rule ID:** `SV-257580r921683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By generating audit logs for the loading and unloading of dynamic kernel modules, OpenShift enables administrators and security teams to track and investigate any unauthorized or suspicious changes to the kernel modules. These records serve as a vital source of information for detecting and responding to potential security breaches or unauthorized module manipulations. Audit records play a crucial role in forensic analysis and investigation. In the event of a security incident or suspected compromise, audit logs for dynamic kernel module loading and unloading provide valuable information for understanding the sequence of events and identifying any unauthorized or malicious module manipulations. Audit records for module loading and unloading can be used for system performance analysis and troubleshooting. By reviewing these records, administrators can identify any problematic or misbehaving modules that may affect system performance or stability. This helps in diagnosing and resolving issues related to kernel modules more effectively.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit rules capture loading and unloading of kernel modules by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e module-load -e module-unload -e module-change /etc/audit/rules.d/* /etc/audit/audit.rules' 2>/dev/null; done Confirm the following rules exist on each node. -a always,exit -F arch=b32 -S init_module,finit_module -F key=module-load -a always,exit -F arch=b64 -S init_module,finit_module -F key=module-load -a always,exit -F arch=b32 -S delete_module -F key=module-unload -a always,exit -F arch=b64 -S delete_module -F key=module-unload -a always,exit -F arch=b32 -S delete_module -k module-change -a always,exit -F arch=b64 -S delete_module -k module-change -a always,exit -F arch=b32 -S finit_module -k module-change -a always,exit -F arch=b64 -S finit_module -k module-change -a always,exit -F arch=b32 -S init_module -k module-change -a always,exit -F arch=b64 -S init_module -k module-change If the above rules are not listed for each node, this is a finding.

## Group: SRG-APP-000505-CTR-001285

**Group ID:** `V-257581`

### Rule: OpenShift audit records must record user access start and end times.

**Rule ID:** `SV-257581r921686_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift must generate audit records showing start and end times for users and services acting on behalf of a user accessing the registry and keystore. These components must use the same standard so that the events can be tied together to understand what took place within the overall container platform. This must establish, correlate, and help assist with investigating the events relating to an incident, or identify those responsible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Red Hat Enterprise Linux CoreOS (RHCOS) is configured to generate audit records showing starting and ending times for user access by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -e "-k session" /etc/audit/audit.rules' 2>/dev/null; done Confirm the following rules exist on each node: -w /var/log/btmp -p wa -k session -w /var/log/utmp -p wa -k session If the above rules are not listed on each node, this is a finding.

## Group: SRG-APP-000506-CTR-001290

**Group ID:** `V-257582`

### Rule: OpenShift must generate audit records when concurrent logons from different workstations and systems occur.

**Rule ID:** `SV-257582r921689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenShift and its components must generate audit records for concurrent logons from workstations perform remote maintenance, runtime instances, connectivity to the container registry, and keystore. All the components must use the same standard so the events can be tied together to understand what took place within the overall container platform. This must establish, correlate, and help assist with investigating the events relating to an incident, or identify those responsible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that concurrent logons are audited by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep "logins" /etc/audit/audit.rules /etc/audit/rules.d/*' 2>/dev/null; done The output will look similar to: node-name /etc/audit/<file>:-w /var/run/faillock -p wa -k logins /etc/audit/<file>:-w /var/log/lastlog -p wa -k logins If the two rules above are not found on each node, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-257583`

### Rule: Red Hat Enterprise Linux CoreOS (RHCOS) must disable SSHD service.

**Rule ID:** `SV-257583r921692_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Any direct remote access to the RHCOS nodes is not allowed. RHCOS is a single-purpose container operating system and is only supported as a component of the OpenShift Container Platform. Remote management of the RHCOS nodes is performed at the OpenShift Container Platform API level. Disabling the SSHD service reduces the attack surface and potential vulnerabilities associated with SSH access. SSH is a commonly targeted vector by malicious actors, and disabling the service eliminates the potential risks associated with unauthorized SSH access or exploitation of SSH-related vulnerabilities. By disabling SSHD, OpenShift can restrict access to the platform to only authorized channels and protocols. This helps mitigate the risk of unauthorized access attempts and reduces the exposure to potential brute-force attacks or password-guessing attacks against SSH. Disabling SSHD encourages the use of more secure and controlled access mechanisms, such as API-based access or secure remote management tools provided by OpenShift. These mechanisms offer better access control and auditing capabilities, allowing administrators to manage and monitor access to the platform more effectively. Satisfies: SRG-APP-000141-CTR-000315, SRG-APP-000185-CTR-000490</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSHD service is inactive and disabled by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; systemctl is-enabled sshd.service; systemctl is-active sshd.service' 2>/dev/null; done If the SSHD service is either active or enabled this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-257584`

### Rule: Red Hat Enterprise Linux CoreOS (RHCOS) must disable USB Storage kernel module.

**Rule ID:** `SV-257584r921695_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling the USB Storage kernel module helps protect against potential data exfiltration or unauthorized access to sensitive data. USB storage devices can be used to transfer data in and out of the system, which poses a risk if unauthorized or untrusted devices are connected. By disabling the USB Storage kernel module, OpenShift can prevent the use of USB storage devices and reduce the risk of data breaches or unauthorized data transfers. USB storage devices can potentially introduce malware or malicious code into the system. Disabling the USB Storage kernel module helps mitigate the risk of malware infections or the introduction of malicious software from external storage devices. It prevents unauthorized execution of code from USB storage devices, reducing the attack surface and protecting the system from potential security threats. Disabling USB storage prevents unauthorized data transfers to and from the system. This helps enforce data loss prevention (DLP) policies and mitigates the risk of sensitive or confidential data being copied or stolen using USB storage devices. It adds an additional layer of control to protect against data leakage or unauthorized data movement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the USB Storage kernel module by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -r usb-storage /etc/modprobe.d/* | grep -i "/bin/true"' 2>/dev/null; done install usb-storage /bin/true If the command does not return any output, or the line is commented out, and use of USB Storage is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-APP-000141-CTR-000315

**Group ID:** `V-257585`

### Rule: Red Hat Enterprise Linux CoreOS (RHCOS) must use USBGuard for hosts that include a USB Controller.

**Rule ID:** `SV-257585r921698_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USBGuard adds an extra layer of security to the overall OpenShift infrastructure. It provides an additional control mechanism to prevent potential security threats originating from USB devices. By monitoring and controlling USB access, USBGuard helps mitigate risks associated with unauthorized or malicious devices that may attempt to exploit vulnerabilities within the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Determine if the host devices include a USB Controller by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; lspci' 2>/dev/null; done If there is not a USB Controller, then this requirement is Not Applicable. 2. Verify the USBGuard service is installed by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; rpm -q usbguard' 2>/dev/null; done If the output returns "package usbguard is not installed", this is a finding. 3. Verify that USBGuard is set up to log into the Linux audit log. for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; grep -r AuditBackend /etc/usbguard/usbguard-daemon.conf' 2>/dev/null; done The output should return: "AuditBackend=LinuxAudit". If it does not, this is a finding. 4. Verify the USBGuard has a policy configured with by executing the following: for node in $(oc get node -oname); do oc debug $node -- chroot /host /bin/bash -c 'echo -n "$HOSTNAME "; usbguard list-rules' 2>/dev/null; done If USBGuard is not found or the results do not match the organizationally defined rules, this is a finding.

## Group: SRG-APP-000516-CTR-001335

**Group ID:** `V-257586`

### Rule: OpenShift must continuously scan components, containers, and images for vulnerabilities.

**Rule ID:** `SV-257586r921701_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Finding vulnerabilities quickly within the container platform and within containers deployed within the platform is important to keep the overall platform secure. When a vulnerability within a component or container is unknown or allowed to remain unpatched, other containers and customers within the platform become vulnerability. The vulnerability can lead to the loss of application data, organizational infrastructure data, and Denial-of-Service (DoS) to hosted applications. Vulnerability scanning can be performed by the container platform or by external applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check if the Container Security Operator is running, execute the following: oc get deploy -n openshift-operators container-security-operator -ojsonpath='{.status.readyReplicas}' If this command returns an error or the number 0, and a separate tool is not being used to perform continuous vulnerability scans of components, containers, and container images, this is a finding.

## Group: SRG-APP-000610-CTR-001385

**Group ID:** `V-257587`

### Rule: OpenShift must use FIPS-validated SHA-2 or higher hash function for digital signature generation and verification (nonlegacy use).

**Rule ID:** `SV-257587r921704_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using a FIPS-validated SHA-2 or higher hash function for digital signature generation and verification in OpenShift ensures strong cryptographic security, compliance with industry standards, and protection against known attacks. It promotes the integrity, authenticity, and nonrepudiation of digital signatures, which are essential for secure communication and data exchange in the OpenShift platform. SHA1 is disabled in digital signatures when FIPS mode is enabled. OpenShift must verify that the certificates in /etc/kubernetes and /etc/pki are using sha256 signatures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the use of a FIPS-compliant hash function for digital signature generation and validation, by executing and reviewing the following commands: update-crypto-policies --show If the return is not "FIPS", this is a finding. Verify the crypto-policies by executing the following: openssl x509 -in /etc/kubernetes/kubelet-ca.crt -noout -text | grep Algorithm openssl x509 -in /etc/kubernetes/ca.crt -noout -text | grep Algorithm If any of the crypto-policies listed are not FIPS compliant, this is a finding. Details of algorithms can be reviewed at the following knowledge base article: https://access.redhat.com/articles/3642912

