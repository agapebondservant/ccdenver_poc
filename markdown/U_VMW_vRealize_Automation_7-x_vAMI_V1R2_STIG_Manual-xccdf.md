# STIG Benchmark: VMware vRealize Automation 7.x vAMI Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-240926`

### Rule: The vAMI must use FIPS 140-2 approved ciphers when transmitting management data during remote access management sessions.

**Rule ID:** `SV-240926r879519_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Remote management access is accomplished by leveraging common communication protocols and establishing a remote connection to the application server via a network for the purposes of managing the application server. If cryptography is not used, then the session data traversing the remote connection could be intercepted and compromised. Types of management interfaces utilized by an application server include web-based HTTPS interfaces as well as command line-based management interfaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^ssl.cipher-list' /opt/vmware/etc/lighttpd/lighttpd.conf If the value of "ssl.cipher-list" is not set to "FIPS: +3DES:!aNULL", or is missing or is commented out, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-240927`

### Rule: The vAMI must restrict inbound connections from nonsecure zones.

**Rule ID:** `SV-240927r879520_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encryption is critical for protection of remote access sessions. If encryption is not being used for integrity, malicious users may gain the ability to modify the application server configuration. The use of cryptography for ensuring integrity of remote access sessions mitigates that risk. Application servers utilize a web management interface and scripted commands when allowing remote access. Web access requires the use of TLS and scripted access requires using ssh or some other form of approved cryptography. Application servers must have a capability to enable a secure remote admin capability. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for Government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^ssl.engine' /opt/vmware/etc/lighttpd/lighttpd.conf If the value of "ssl.engine" is not set to "enable", or is missing or is commented out, this is a finding.

## Group: SRG-APP-000090-AS-000051

**Group ID:** `V-240928`

### Rule: The vAMI configuration file must be owned by root.

**Rule ID:** `SV-240928r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the application server, (e.g., httpd, beans, etc.) From an application perspective, certain specific application functionalities may be logged, as well. The list of logged events is the set of events for which logs are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating log records (e.g., logable events, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked). Application servers utilize role-based access controls in order to specify the individuals who are allowed to configure application component logable events. The application server must be configured to select which personnel are assigned the role of selecting which logable events are to be logged. The personnel or roles that can select logable events are only the ISSM (or individuals or roles appointed by the ISSM).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lL /opt/vmware/etc/sfcb/sfcb.cfg If the sfcb.cfg file is not owned by root, this is a finding.

## Group: SRG-APP-000101-AS-000072

**Group ID:** `V-240929`

### Rule: The vAMI must have sfcb logging enabled.

**Rule ID:** `SV-240929r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged commands are commands that change the configuration or data of the application server. Since this type of command changes the application server configuration and could possibly change the security posture of the application server, these commands need to be logged to show the full-text of the command executed. Without the full-text, reconstruction of harmful events or forensic analysis is not possible. Organizations can consider limiting the additional log information to only that information explicitly needed for specific log requirements. At a minimum, the organization must log either full-text recording of privileged commands or the individual identities of group users, or both. The organization must maintain log trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep traceLevel /opt/vmware/etc/sfcb/sfcb.cfg If the value of "traceLevel" is not set to "1", or is missing or is commented out, this is a finding.

## Group: SRG-APP-000118-AS-000078

**Group ID:** `V-240930`

### Rule: The vAMI must protect log information from unauthorized read access.

**Rule ID:** `SV-240930r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to his or her advantage. Application servers contain admin interfaces that allow reading and manipulation of log records. Therefore, these interfaces should not allow unfettered access to those records. Application servers also write log data to log files that are stored on the OS, so appropriate file permissions must also be used to restrict access. Log information includes all information (e.g., log records, log settings, transaction logs, and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized read access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lL /opt/vmware/var/log/vami /opt/vmware/var/log/sfcb If any log files are world-readable, this is a finding.

## Group: SRG-APP-000119-AS-000079

**Group ID:** `V-240931`

### Rule: The vAMI must protect log information from unauthorized modification.

**Rule ID:** `SV-240931r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to his or her advantage. Application servers contain admin interfaces that allow reading and manipulation of log records. Therefore, these interfaces should not allow unfettered access to those records. Application servers also write log data to log files that are stored on the OS, so appropriate file permissions must also be used to restrict access. Log information includes all information (e.g., log records, log settings, transaction logs and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lL /opt/vmware/var/log/vami /opt/vmware/var/log/sfcb If any log files are world-writable, this is a finding.

## Group: SRG-APP-000120-AS-000080

**Group ID:** `V-240932`

### Rule: The vAMI must protect log information from unauthorized deletion.

**Rule ID:** `SV-240932r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. Application servers contain admin interfaces that allow reading and manipulation of log records. Therefore, these interfaces should not allow for unfettered access to those records. Application servers also write log data to log files that are stored on the OS, so appropriate file permissions must also be used to restrict access. Log information includes all information (e.g., log records, log settings, transaction logs, and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized deletion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lL /opt/vmware/var/log/vami /opt/vmware/var/log/sfcb If log files are not owned by root, this is a finding.

## Group: SRG-APP-000125-AS-000084

**Group ID:** `V-240933`

### Rule: The vAMI log records must be backed up at least every seven days onto a different system or system component than the system or component being logged.

**Rule ID:** `SV-240933r879582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Backing up log records to a different system or onto separate media from the system that the vAMI is actually running on helps to assure that in the event of a catastrophic system failure, the log records will be retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine if there is a local procedure to back up log records at least every seven days onto a different system. If a procedure does not exist or is not being followed, this is a finding.

## Group: SRG-APP-000131-AS-000002

**Group ID:** `V-240934`

### Rule: Patches, service packs, and upgrades to the vAMI must be verifiably signed using a digital certificate that is recognized and approved by the organization.

**Rule ID:** `SV-240934r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the application. Verifying software components have been digitally signed using a certificate that is recognized and approved by the organization ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, or application components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The application should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine if there is a local procedure to verify the digital signature of the vAMI files prior to being installed on a production system. If a procedure does not exist or is not being followed, this is a finding.

## Group: SRG-APP-000133-AS-000092

**Group ID:** `V-240935`

### Rule: The vAMI executable files and library must not be world-writeable.

**Rule ID:** `SV-240935r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers have the ability to specify that the hosted applications utilize shared libraries. The application server must have a capability to divide roles based upon duties wherein one project user (such as a developer) cannot modify the shared library code of another project user. The application server must also be able to specify that non-privileged users cannot modify any shared library code at all.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: find /opt/vmware/share/vami -perm -0002 -type f If any files are listed, this is a finding.

## Group: SRG-APP-000133-AS-000093

**Group ID:** `V-240936`

### Rule: The vAMI installation procedures must be capable of being rolled back to a last known good configuration.

**Rule ID:** `SV-240936r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any changes to the components of the application server can have significant effects on the overall security of the system. In order to ensure a prompt response to failed application installations and application server upgrades, the application server must provide an automated rollback capability that allows the system to be restored to a previous known good configuration state prior to the application installation or application server upgrade.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine if there is a local procedure to revert to the last known good configuration in the event of failed installations and upgrades. If a procedure does not exist or is not being followed, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-240937`

### Rule: The vAMI must not contain any unnecessary functions and only provide essential capabilities.

**Rule ID:** `SV-240937r879587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Application servers provide a myriad of differing processes, features and functionalities. Some of these processes may be deemed to be unnecessary or too unsecure to run on a production DoD system. Application servers must provide the capability to disable or deactivate functionality and services that are deemed to be non-essential to the server mission or can adversely impact server performance, for example, disabling dynamic JSP reloading on production application servers as a best practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the vAMI directories and files. Determine if there are any tutorials, examples, or sample code. If any tutorials, examples, or sample code is present, this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-240938`

### Rule: The vAMI must use the sfcb HTTPS port for communication with Lighttpd.

**Rule ID:** `SV-240938r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some networking protocols may not meet organizational security requirements to protect data and components. Application servers natively host a number of various features, such as management interfaces, httpd servers and message queues. These features all run on TCPIP ports. This creates the potential that the vendor may choose to utilize port numbers or network services that have been deemed unusable by the organization. The application server must have the capability to both reconfigure and disable the assigned ports without adversely impacting application server operation capabilities. For a list of approved ports and protocols, reference the DoD ports and protocols web site at https://powhatan.iiie.disa.mil/ports/cal.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command to determine the sfcb HTTPS port: grep httpsPort /opt/vmware/etc/sfcb/sfcb.cfg | cut -d ':' -f 2 | tr -d ' ' If the httpsPort configuration is missing or commented out, this is a finding. At the command prompt, type the following command to determine the port that Lighttpd is using to communicate with sfcb: grep cimom -A 7 /opt/vmware/etc/lighttpd/lighttpd.conf | grep port | cut -d '=' -f 2 | tr -d '>' | tr -d ' ' | tr -d '"' If Lighttpd is not using the sfcb HTTPS port for communication with the vAMI, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-240939`

### Rule: The vAMI must use a site-defined, user management system to uniquely identify and authenticate users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-240939r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. This is typically accomplished via the use of a user store which is either local (OS-based) or centralized (LDAP) in nature. To ensure support to the enterprise, the authentication must utilize an enterprise solution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine the enterprise user management system being used to uniquely identify and authenticate users. If the vAMI is not configured to use the enterprise user management system, this is a finding.

## Group: SRG-APP-000172-AS-000120

**Group ID:** `V-240940`

### Rule: The vAMI must transmit only encrypted representations of passwords.

**Rule ID:** `SV-240940r879609_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Application servers have the capability to utilize either certificates (tokens) or user IDs and passwords in order to authenticate. When the application server transmits or receives passwords, the passwords must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep '^ssl.engine' /opt/vmware/etc/lighttpd/lighttpd.conf If the value of "ssl.engine" is not set to "enable", or is missing or is commented out, this is a finding.

## Group: SRG-APP-000176-AS-000125

**Group ID:** `V-240941`

### Rule: The vAMI private key must only be accessible to authenticated system administrators or the designated PKI Sponsor.

**Rule ID:** `SV-240941r879613_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and can pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys. Java-based application servers utilize the Java keystore, which provides storage for cryptographic keys and certificates. The keystore is usually maintained in a file stored on the file system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/etc/sfcb/file.pem If permissions on the key file are not -r--r----- (440), this is a finding.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-240942`

### Rule: The vAMI must use approved versions of TLS.

**Rule ID:** `SV-240942r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. The use of TLS provides confidentiality of data in transit between the application server and client. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for Government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep ssl.use-sslv /opt/vmware/etc/lighttpd/lighttpd.conf If the value of "ssl.use-sslv2" and "ssl.use-sslv3" are not "disable", this is a finding.

## Group: SRG-APP-000219-AS-000147

**Group ID:** `V-240943`

### Rule: The vAMI must use sfcBasicPAMAuthentication for authentication of the remote administrator.

**Rule ID:** `SV-240943r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This control focuses on communications protection at the session, versus packet level. At the application layer, session IDs are tokens generated by web applications to uniquely identify an application user's session. Web applications utilize session tokens or session IDs in order to establish application user identity. Proper use of session IDs addresses man-in-the-middle attacks, including session hijacking or insertion of false information into a session. Application servers must provide the capability to perform mutual authentication. Mutual authentication is when both the client and the server authenticate each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep basicAuthLib /opt/vmware/etc/sfcb/sfcb.cfg If the value of "basicAuthLib" is missing, commented out, or not "sfcBasicPAMAuthentication", this is a finding.

## Group: SRG-APP-000223-AS-000150

**Group ID:** `V-240944`

### Rule: The vAMI must use _sfcBasicAuthenticate for initial authentication of the remote administrator.

**Rule ID:** `SV-240944r879638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unique session IDs are the opposite of sequentially generated session IDs, which can be easily guessed by an attacker. Unique session identifiers help to reduce predictability of session identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. Application servers must generate a unique session identifier for each application session to prevent session hijacking.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep basicAuthEntry /opt/vmware/etc/sfcb/sfcb.cfg If the value of "basicAuthEntry" is missing, commented out, or not "_sfcBasicAuthenticate", this is a finding.

## Group: SRG-APP-000223-AS-000151

**Group ID:** `V-240945`

### Rule: The vAMI must have the correct authentication set for HTTPS connections.

**Rule ID:** `SV-240945r879638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement focuses on communications protection at the application session, versus network packet level. The intent of this control is to establish grounds for confidence at each end of a communications session in the ongoing identity of the other party and in the validity of the information being transmitted. Unique session IDs are the opposite of sequentially generated session IDs, which can be easily guessed by an attacker. Unique session identifiers help to reduce predictability of said identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep doBasicAuth /opt/vmware/etc/sfcb/sfcb.cfg If the value of "doBasicAuth" is missing, commented out, or not "true", this is a finding.

## Group: SRG-APP-000225-AS-000153

**Group ID:** `V-240946`

### Rule: The vAMI installation procedures must be part of a complete vRealize Automation deployment.

**Rule ID:** `SV-240946r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. When an application is deployed to the vAMI, if the deployment process does not complete properly and without errors, there is the potential that some application files may not be deployed or may be corrupted and an application error may occur during runtime. The vAMI must be able to perform complete application deployments. A partial deployment can leave the server in an inconsistent state. Application servers may provide a transaction rollback function to address this issue.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine if the vAMI was installed separately from a full installation of vRealize Automation. If the vAMI was installed independently of a full vRA installation, this is a finding.

## Group: SRG-APP-000225-AS-000166

**Group ID:** `V-240947`

### Rule: The vAMI must fail to a secure state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-240947r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Fail-secure is a condition achieved by the vAMI in order to ensure that in the event of an operational failure, the system does not enter into an unsecure state where intended security properties no longer hold. Preserving information system state information also facilitates system restart and return to the operational mode of the organization with less disruption of mission-essential processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine if the vAMI has ever not failed to a secure state during a system initialization failure, shutdown failure, or system abort. If the vAMI has ever not failed to a secure state under these conditions, this is a finding.

## Group: SRG-APP-000266-AS-000168

**Group ID:** `V-240948`

### Rule: The vAMI error logs must be reviewed.

**Rule ID:** `SV-240948r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The structure and content of error messages need to be carefully considered by the organization and development team. Any application providing too much information in error logs and in administrative messages to the screen risks compromising the data and security of the application and system. The extent to which the application server is able to identify and handle error conditions is guided by organizational policy and operational requirements. Adequate logging levels and system performance capabilities need to be balanced with data protection requirements. The structure and content of error messages needs to be carefully considered by the organization and development team. Application servers must have the capability to log at various levels, which can provide log entries for potential security-related error events. An example is the capability for the application server to assign a criticality level to a failed logon attempt error message, a security-related error message being of a higher criticality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA and review vRA product documentation. Determine a local procedure exists for monitoring error conditions reported by the vAMI. If a procedure does not exist or is not being followed, this is a finding.

## Group: SRG-APP-000315-AS-000094

**Group ID:** `V-240949`

### Rule: The vAMI account credentials must protected by site policies.

**Rule ID:** `SV-240949r879692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers provide remote access capability and must be able to enforce remote access policy requirements or work in conjunction with enterprise tools designed to enforce policy requirements. Automated monitoring and control of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by logging connection activities of remote users. Examples of policy requirements include, but are not limited to, authorizing remote access to the information system, limiting access based on authentication credentials, and monitoring for unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine if access credentials for the vAMI are controlled by a site policy. If a site policy does not exist, or is not being followed, this is a finding.

## Group: SRG-APP-000356-AS-000202

**Group ID:** `V-240950`

### Rule: The vAMI must utilize syslog.

**Rule ID:** `SV-240950r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A clustered application server is made up of several servers working together to provide the user a failover and increased computing capability. To facilitate uniform logging in the event of an incident and later forensic investigation, the record format and logable events need to be uniform. This can be managed best from a centralized server. Without the ability to centrally manage the content captured in the log records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep traceFile /opt/vmware/etc/sfcb/sfcb.cfg If the value of "traceFile" is not "syslog', this is a finding.

## Group: SRG-APP-000380-AS-000088

**Group ID:** `V-240951`

### Rule: The vAMI configuration file must be protected from unauthorized access.

**Rule ID:** `SV-240951r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with access restrictions pertaining to change control, it should be noted that any changes to the software and/or application server configuration can potentially have significant effects on the overall security of the system. Access restrictions for changes also include application software libraries. If the application server provides automatic code deployment capability, (where updates to applications hosted on the application server are automatically performed, usually by the developers' IDE tool), it must also provide a capability to restrict the use of automatic application deployment. Automatic code deployments are allowable in a development environment, but not in production.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lL /opt/vmware/etc/sfcb/sfcb.cfg If the permissions on the sfcb.cfg file are greater than 640, this is a finding.

## Group: SRG-APP-000416-AS-000140

**Group ID:** `V-240952`

### Rule: The vAMI must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-240952r879944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. NSA has developed Type 1 algorithms for protecting classified information. The Committee on National Security Systems (CNSS) National Information Assurance Glossary (CNSS Instruction No. 4009) defines Type 1 products as: 'Cryptographic equipment, assembly or component classified or certified by NSA for encrypting and decrypting classified and sensitive national security information when appropriately keyed. Developed using established NSA business processes and containing NSA-approved algorithms are used to protect systems requiring the most stringent protection mechanisms.' NSA-approved cryptography is required to be used for classified information system processing. The application server must utilize NSA-approved encryption modules when protecting classified data. This means using AES and other approved encryption modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'ssl.cipher-list' /opt/vmware/etc/lighttpd/lighttpd.conf If the value of "ssl.cipher-list" is not "FIPS: +3DES:!aNULL", this is a finding.

## Group: SRG-APP-000435-AS-000163

**Group ID:** `V-240953`

### Rule: The vAMI must have the keepaliveTimeout enabled.

**Rule ID:** `SV-240953r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. To reduce the possibility or effect of a DoS, the application server must employ defined security safeguards. These safeguards will be determined by the placement of the application server and the type of applications being hosted within the application server framework. There are many examples of technologies that exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy or clustering, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep keepaliveTimeout /opt/vmware/etc/sfcb/sfcb.cfg | grep -vE '^#' If the value of "keepaliveTimeout" is missing, commented out, or less than "15", this is a finding.

## Group: SRG-APP-000435-AS-000163

**Group ID:** `V-240954`

### Rule: The vAMI must have the keepaliveMaxRequest enabled.

**Rule ID:** `SV-240954r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. To reduce the possibility or effect of a DoS, the application server must employ defined security safeguards. These safeguards will be determined by the placement of the application server and the type of applications being hosted within the application server framework. There are many examples of technologies that exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy or clustering, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep keepaliveMaxRequest /opt/vmware/etc/sfcb/sfcb.cfg | grep -vE '^#' If the value of "keepaliveMaxRequest" is missing, commented out, less than "100", this is a finding.

## Group: SRG-APP-000439-AS-000155

**Group ID:** `V-240955`

### Rule: The vAMI must use approved versions of TLS.

**Rule ID:** `SV-240955r918127_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the application server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS).Transmission of data can take place between the application server and a large number of devices/applications external to the application server. Examples are a web client used by a user, a backend database, a log server, or other application servers in an application server cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for Government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep ssl.use-sslv /opt/vmware/etc/lighttpd/lighttpd.conf If the value of "ssl.use-sslv2" and "ssl.use-sslv3" are not "disable", this is a finding.

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-240956`

### Rule: The vAMI sfcb must have HTTPS enabled.

**Rule ID:** `SV-240956r879811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure or modification of transmitted information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. If data in transit is unencrypted, it is vulnerable to disclosure and modification. If approved cryptographic algorithms are not used, encryption strength cannot be assured. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for Government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'enableHttps:' /opt/vmware/etc/sfcb/sfcb.cfg | grep -v '^#' If the value of "enableHttps" is missing or is not set to "true", this is a finding.

## Group: SRG-APP-000442-AS-000259

**Group ID:** `V-240957`

### Rule: The vAMI sfcb must have HTTP disabled.

**Rule ID:** `SV-240957r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. The application server must utilize approved encryption when receiving transmitted data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'enableHttp:' /opt/vmware/etc/sfcb/sfcb.cfg | grep -v '^#' If the value of "enableHttp" is set to "true", this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-240958`

### Rule: The vAMI must have security-relevant software updates installed within the time period directed by an authoritative source (e.g. IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-240958r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes) to production systems after thorough testing of the patches within a lab environment. Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine if a local procedure exists to install security-relevant software updates in a satisfactory timeframe. If a procedure does not exist or is not being followed, this is a finding.

## Group: SRG-APP-000503-AS-000228

**Group ID:** `V-240959`

### Rule: The vAMI must log all successful login events.

**Rule ID:** `SV-240959r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging the access to the application server allows the system administrators to monitor user accounts. By logging successful/unsuccessful logons, the system administrator can determine if an account is compromised (e.g., frequent logons) or is in the process of being compromised (e.g., frequent failed logons) and can take actions to thwart the attack. Logging successful logons can also be used to determine accounts that are no longer in use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep quiet_success /etc/pam.d/vami-sfcb If the command returns any output, this is a finding.

## Group: SRG-APP-000504-AS-000229

**Group ID:** `V-240960`

### Rule: The vAMI must enable logging.

**Rule ID:** `SV-240960r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Privileged activities would occur through the management interface. This interface can be web-based or can be command line utilities. Whichever method is used by the application server, these activities must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep traceLevel /opt/vmware/etc/sfcb/sfcb.cfg If the value of "traceLevel" is not "1", this is a finding.

## Group: SRG-APP-000505-AS-000230

**Group ID:** `V-240961`

### Rule: The vAMI must have PAM logging enabled.

**Rule ID:** `SV-240961r879876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining when a user has accessed the management interface is important to determine the timeline of events when a security incident occurs. Generating these events, especially if the management interface is accessed via a stateless protocol like HTTP, the log events will be generated when the user performs a logon (start) and when the user performs a logoff (end). Without these events, the user and later investigators cannot determine the sequence of events and therefore cannot determine what may have happened and by whom it may have been done. The generation of start and end times within log events allow the user to perform their due diligence in the event of a security breach.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls /etc/pam_debug If the /etc/pam_debug file does not exist, this is a finding.

## Group: SRG-APP-000506-AS-000231

**Group ID:** `V-240962`

### Rule: The vAMI must log all login events.

**Rule ID:** `SV-240962r879877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Being able to work on a system through multiple views into the application allows a user to work more efficiently and more accurately. Before environments with windowing capabilities or multiple desktops, a user would log onto the application from different workstations or terminals. With today's workstations, this is no longer necessary and may signal a compromised session or user account. When concurrent logons are made from different workstations to the management interface, a log record needs to be generated. This allows the system administrator to investigate the incident and to be aware of the incident.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E 'auth.*unix' /etc/pam.d/vami-sfcb If no line is returned or the returned line does contain the option "debug", this is a finding.

## Group: SRG-APP-000514-AS-000136

**Group ID:** `V-240963`

### Rule: The vAMI sfcb server certificate must only be accessible to authenticated system administrators or the designated PKI Sponsor.

**Rule ID:** `SV-240963r879885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An asymmetric encryption key must be protected during transmission. The public portion of an asymmetric key pair can be freely distributed without fear of compromise, and the private portion of the key must be protected. The application server will provide software libraries that applications can programmatically utilize to encrypt and decrypt information. These application server libraries must use NIST-approved or NSA-approved key management technology and processes when producing, controlling, or distributing symmetric and asymmetric keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /opt/vmware/etc/sfcb/server.pem If permissions on the certificate file is not -r--r----- (440), this is a finding.

## Group: SRG-APP-000514-AS-000137

**Group ID:** `V-240964`

### Rule: If the vAMI uses PKI Class 3 or Class 4 certificates, the certificates must be DoD- or CNSS-approved.

If the vAMI does not use PKI Class 3 or Class 4 certificates, this requirement is Not Applicable.

**Rule ID:** `SV-240964r879885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Class 3 PKI certificates are used for servers and software signing rather than for identifying individuals. Class 4 certificates are used for business-to-business transactions. Utilizing unapproved certificates not issued or approved by DoD or CNS creates an integrity risk. The vAMI must utilize approved DoD or CNS Class 3 or Class 4 certificates for software signing and business-to-business transactions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and/or the SA. Determine if the vAMI is using PKI Class 3 or Class 4 certificates. If the vAMI is using PKI Class 3 or Class 4 certificates, and the certificates are not DoD- or CNSS-approved, this is a finding.

## Group: SRG-APP-000515-AS-000203

**Group ID:** `V-240965`

### Rule: The vAMI must utilize syslog.

**Rule ID:** `SV-240965r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Protecting log data is important during a forensic investigation to ensure investigators can track and understand what may have occurred. Off-loading should be set up as a scheduled task but can be configured to be run manually, if other processes during the off-loading are manual. Off-loading is a common process in information systems with limited log storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep traceFile /opt/vmware/etc/sfcb/sfcb.cfg If the value of "traceFile" is not "syslog', this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-240966`

### Rule: The vAMI must be configured to listen on a specific IPv4 address.

**Rule ID:** `SV-240966r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep ip4AddrList /opt/vmware/etc/sfcb/sfcb.cfg If the value of "ip4AddrList" is missing, commented out, or not set, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-240967`

### Rule: The vAMI must be configured to listen on a specific network interface.

**Rule ID:** `SV-240967r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the current vRealize Operations STIGs from the ISSO. Verify that this STIG is the most current STIG available for vRealize Operations. Assess all of the organization's vROps installations to ensure that they are fully compliant with the most current STIG. If the most current version of the vROps STIG was not used, or if the vROps appliance configuration is not compliant with the most current STIG, this is a finding.

## Group: SRG-APP-000439-AS-000274

**Group ID:** `V-240968`

### Rule: The application server must remove all export ciphers to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-240968r918128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the application server, the client sends a list of supported cipher suites in order of preference. The application server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the application server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that FIPS mode is enabled in the vRealize Automation virtual appliance management interface with the following steps: 1. Log into the vRealize Automation virtual appliance management interface (vAMI). https:// vrealize-automation-appliance-FQDN:5480 2. Select vRA Settings >> Host Settings. 3. Review the button under the Actions heading on the upper right to confirm that "enable FIPS" is selected. If "enable FIPS" is not selected, this is a finding. Alternately, check that FIPS mode is enabled in the command line using the following steps: 1. Log into the console as root. 2. Run the command: vcac-vami fips status. If FIPS is not enabled, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-258455`

### Rule: The version of vRealize Automation 7.x vAMI running on the system must be a supported version.

**Rule ID:** `SV-258455r928889_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Automation 7.x vAMI is no longer supported by the vendor. If the system is running vRealize Automation 7.x vAMI, this is a finding.

