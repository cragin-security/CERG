## NETWORK SECURITY AND SEGMENTATION STANDARD
### Zero-Trust Principles · Segmentation · Boundary Control · IT/OT Separation · Remote Access

---

| | |
|---|---|
| **Document ID** | CERG-STD-NET-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Platforms) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) · [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Review Cycle** | Annual / On material change to network architecture |
| **Frameworks** | [NIST 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) (Zero Trust Architecture) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (SC, AC families) · [CIS Controls v8](https://www.cisecurity.org/controls) (Controls 12, 13) · [IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) (zones and conduits) |
| **Regulations** | NERC-CIP (CIP-005 electronic security perimeter) · CMMC L2 / 800-171r3 (3.13.x) · SOX ITGC |
| **Environments** | All in-scope networks: owned, hybrid, cloud, SaaS access paths, and OT |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [Zero-Trust Architecture](#3-zero-trust-architecture)
4. [Network Segmentation](#4-network-segmentation)
5. [Boundary Control](#5-boundary-control)
6. [The IT/OT Boundary](#6-the-itot-boundary)
7. [Remote Access](#7-remote-access)
8. [Cloud Network Security](#8-cloud-network-security)
9. [Network Monitoring](#9-network-monitoring)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

The network is where an intruder moves. A foothold on one system becomes a breach of the estate only if the network lets the intruder travel. The IT, OT, and Access standards each impose network-adjacent requirements; none of them owns the network itself. This standard does.

This standard establishes the requirements for network security across CERG-managed environments: the zero-trust principles that govern how access to network resources is decided, how the estate is segmented, how boundaries between segments are controlled, how the IT and OT networks are separated, how remote access is granted, and how networks are monitored.

It applies to every network CERG-managed systems use: physical and virtual networks in owned data centers, cloud virtual networks, the network paths to SaaS, and operational technology networks.

> **Segmentation Is What Turns an Incident Into a Contained Incident**
>
> Every significant breach retrospective contains the same sentence in some form: the attacker moved laterally from the initial foothold. Lateral movement is a network event. A flat network means one compromised laptop can reach the domain controller, the financial system, and the control network. A segmented network means the compromised laptop reaches the things that laptop legitimately needs and nothing else. Segmentation does not prevent the incident. It decides how bad the incident gets.

---

## 2. Principles

1. **The network is not a trust boundary.** Being on the internal network grants nothing. Access to a resource is decided per request against identity, device posture, and context, not by network location.
2. **Default deny.** Network paths are denied unless explicitly allowed. A segment, a firewall, a security group starts closed. Connectivity is added deliberately and recorded.
3. **Segment by function and criticality.** Systems are grouped into segments by what they do and how critical they are, per the criticality tiers in [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md). A breach in one segment does not become a breach of another for free.
4. **The boundary is enforced and watched.** Every boundary between segments is enforced by a control and monitored. An unenforced boundary is not a boundary.
5. **OT is separated, not just segmented.** The boundary between the IT network and the OT network is the most consequential boundary in the estate and is held to a higher bar than any other.
6. **Every allowed path has an owner and a reason.** A firewall rule, a security group entry, a peering connection exists because someone needed it and someone owns it. Rules with no owner and no recorded reason are removed.

---

## 3. Zero-Trust Architecture

CERG networks are designed toward the zero-trust model in NIST 800-207. The estate does not have to reach a fully mature zero-trust architecture on day one; it does have to move deliberately in that direction and never away from it.

1. **Access is per-session and per-resource.** A user or service is granted access to a specific resource for a specific session, not to a network zone indefinitely.
2. **Every access decision uses identity and device posture.** Access decisions combine the authenticated identity per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) with the posture of the device making the request per [`CERG-STD-EP-001`](CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md).
3. **Encryption in transit is assumed everywhere.** Traffic is encrypted in transit per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md), including traffic between internal segments. The network is treated as hostile.
4. **The policy decision point is logged.** Every access decision a zero-trust enforcement point makes is logged per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).

> **Zero Trust Is a Direction, Not a Product**
>
> No purchase makes an organization zero-trust. Zero trust is an architecture an estate moves toward over years: removing implicit network trust, adding identity and posture to access decisions, encrypting internal traffic, shrinking segments. CERG asks one thing of every network change: does it move the estate toward the zero-trust model, or away from it? Changes that move away from it are exceptions and are filed as such.

---

## 4. Network Segmentation

1. **The estate is segmented.** The network is divided into segments. A single flat network for the whole estate is not permitted for any environment beyond a trivial one.
2. **Segments are defined by function and criticality.** At minimum the estate separates: user endpoints, servers and production workloads, management and administrative interfaces, infrastructure and security tooling, untrusted and guest networks, and OT (Section 6). Critical-tier systems are segmented from lower-tier systems.
3. **Management interfaces are isolated.** Administrative and management interfaces of infrastructure are placed in a dedicated management segment reachable only through controlled paths. A management plane reachable from the user network is a finding.
4. **Inter-segment traffic is default-deny.** Traffic between segments is denied unless an explicit, owned rule allows it (Section 5).
5. **Segmentation is documented.** The segment map, what each segment contains and which segments may talk to which, is documented and kept current as an architecture artifact. An undocumented network cannot be reasoned about.

---

## 5. Boundary Control

1. **Every inter-segment boundary is enforced.** A boundary between segments is enforced by a firewall, a cloud security group, an access control list, or an equivalent control. The enforcement point is itself a Critical or High asset per [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md).
2. **Rules are least-privilege.** A boundary rule allows the narrowest source, destination, port, and protocol that satisfies the need. Any-to-any rules are prohibited except at a deliberately open boundary, and that exception is recorded.
3. **Every rule has an owner and a reason.** Each rule records who owns it and why it exists. A rule traceable to neither is removed.
4. **Rules are reviewed.** The boundary rule set is reviewed at least annually. The review removes rules that are no longer needed, tightens rules that are broader than needed, and confirms each remaining rule still has an owner. Stale rules accumulate; the review is how they are removed.
5. **Rule changes are change-controlled.** A change to a boundary rule set follows change management. For SOX-relevant boundaries, the change record is audit evidence.
6. **The internet boundary is hardened.** The boundary between the estate and the internet enforces both ingress and egress control. Unrestricted outbound traffic is a data-exfiltration path; egress is filtered and monitored.

---

## 6. The IT/OT Boundary

This section applies to organizations that operate operational technology. For NERC-CIP entities, it operates alongside the electronic security perimeter requirements in [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md); where the two are read together, the stricter requirement governs.

1. **IT and OT networks are separated.** The OT network is not a segment of the IT network. It is a separate network joined to IT only through a controlled, monitored boundary.
2. **The boundary is a single, defined set of crossing points.** Traffic crosses the IT/OT boundary only through a defined, minimal set of crossing points. Every crossing point is documented, enforced, and monitored. Undocumented crossings are findings of the highest severity.
3. **The boundary is default-deny and minimal.** Only the specific flows an operational need requires cross the boundary. The direction of each flow is constrained; data flowing out of OT for monitoring is not a path for traffic to flow into OT.
4. **No direct internet path to OT.** OT systems do not have a direct path to or from the internet. Remote access to OT follows Section 7 and the additional constraints of [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md).
5. **The boundary is designed with IEC 62443 zones and conduits.** The IT/OT boundary and the segmentation within OT use the zones-and-conduits model of IEC 62443.

> **The IT/OT Boundary Is the Most Important Boundary in the Estate**
>
> A compromise that crosses from IT into OT moves from a data problem to a physical and safety problem. The IT/OT boundary is held to a higher standard than any other boundary in CERG: fewer crossing points, tighter rules, stricter direction control, and continuous monitoring. When the IT/OT boundary requirement here and the electronic security perimeter requirement in the OT standard appear to differ, the stricter one is followed. There is no acceptable reason to relax this boundary for convenience.

---

## 7. Remote Access

1. **Remote access is identified, authenticated, and authorized.** Every remote connection into the estate authenticates the identity per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md), including multi-factor authentication, and is authorized to a specific set of resources.
2. **Remote access is least-privilege.** A remote session reaches the resources the session needs, not the whole internal network. Remote access that drops a user onto a flat internal network is prohibited.
3. **Device posture is checked.** A device connecting remotely is checked for posture before access is granted, per [`CERG-STD-EP-001`](CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md).
4. **Remote administrative access is brokered and recorded.** Privileged remote access to infrastructure goes through a privileged access broker per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md). Privileged remote sessions are recorded.
5. **Vendor and third-party remote access is time-bound and supervised.** A vendor granted remote access receives it for a defined window, scoped to defined systems, and the access is removed when the window closes. Standing vendor access is prohibited. This aligns with [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md).
6. **Remote access to OT is exceptional.** Remote access into the OT network is granted only where operationally necessary, is brokered, is supervised in real time where it affects control systems, and follows [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md).

---

## 8. Cloud Network Security

1. **Cloud virtual networks are segmented.** The principles in Sections 4 and 5 apply to cloud virtual networks: function-based segmentation, default-deny between subnets, least-privilege security groups, and owned rules.
2. **The cloud landing zone enforces network baseline.** Network segmentation, boundary defaults, and egress control are part of the cloud landing zone governed by [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) and are enforced through infrastructure-as-code per [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md).
3. **Cloud-to-on-premises connectivity is a controlled boundary.** A private interconnect or VPN between cloud and owned environments is an inter-segment boundary and is governed by Section 5.
4. **Public exposure is deliberate.** A cloud resource is reachable from the internet only by an explicit, owned decision. Inadvertent public exposure of storage, databases, or management interfaces is a finding.

---

## 9. Network Monitoring

1. **Boundary enforcement points log.** Firewalls, security groups, and other enforcement points send logs to the platform governed by [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).
2. **East-west traffic is visible.** Monitoring covers traffic between internal segments, not only traffic crossing the internet boundary. Lateral movement is an east-west event; monitoring that sees only the perimeter does not see it.
3. **The IT/OT boundary is continuously monitored.** Every crossing point of the IT/OT boundary is monitored continuously, using OT-safe methods per [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md).
4. **Detection content covers the network.** Detection use cases include network-based indicators: anomalous inter-segment traffic, boundary rule violations, and unexpected egress. Detection content is owned per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).

---

## 10. Roles and Responsibilities

Roles below are the canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Network Security Responsibility** |
|---|---|
| **Engineering Pillar Leader** | Owns this standard. Accountable for network architecture, the segment map, and the zero-trust trajectory. |
| **Cloud Security Engineer** | Owns cloud network security: virtual network segmentation, security groups, landing-zone network baseline, and cloud interconnects. |
| **OT Security Engineer** | Owns the IT/OT boundary design and the OT network segmentation, in coordination with [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md). |
| **Identity Engineer** | Owns the identity and device-posture inputs to zero-trust access decisions and the privileged access broker for remote administrative access. |
| **Endpoint Engineer** | Provides the device posture signal used in remote access and zero-trust decisions. |
| **Detection Engineer** | Owns network-based detection content; consumes boundary and east-west logs. |
| **Exposure Management Lead** | Tracks network-device vulnerabilities and exposed-service findings. |
| **Vendor Risk Analyst** | Coordinates time-bound vendor remote access with [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). |
| **Governance Pillar Leader** | Tracks boundary-rule review completion and exceptions; cross-references this standard with the control baseline. |
| **Policy & Standards Manager** | Maintains this document, its version, and its review cycle. |

---

## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Standard** |
|---|---|---|
| NIST 800-207 | Zero Trust Architecture tenets | Section 3 |
| NIST 800-53r5 | SC-7 (boundary protection), AC-17 (remote access), SC-8 (transmission), AC-4 (information flow) | Sections 5, 6, 7 |
| CIS Controls v8 | Control 12 (network infrastructure), Control 13 (network monitoring and defense) | Sections 4, 5, 9 |
| IEC 62443 | Zones and conduits model | Section 6 |
| NERC-CIP | CIP-005 (electronic security perimeter and remote access) | Sections 6, 7 |
| NIST 800-171r3 / CMMC L2 | 3.13.1, 3.13.5, 3.13.6 (boundary protection and network separation) | Sections 4, 5, 6 |
| SOX ITGC | Network boundary change control | Section 5 |

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-NET-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Platforms) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to network architecture |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST 800-207; NIST 800-53r5 (SC, AC); CIS Controls v8 (12, 13); IEC 62443 |
| **Regulations** | NERC-CIP (CIP-005); CMMC L2 / 800-171r3; SOX ITGC |
| **Environments** | All in-scope networks |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-21 | Cyber Engineering | Initial release. Establishes zero-trust architecture direction, network segmentation by function and criticality, boundary control with owned and reviewed rules, the elevated-bar IT/OT boundary, remote access requirements including time-bound vendor access, cloud network security, and network monitoring including east-west visibility. |

### Review Triggers

- Material change to network architecture or to the cloud landing zone
- Revision of NIST 800-207, NERC-CIP CIP-005, or IEC 62443
- A significant incident involving lateral movement or boundary failure
- Internal audit or regulatory finding affecting network security
- Direction from the CISO

Cyber Engineering owns this document. The Engineering Pillar Leader (Platforms) is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| IT / Cloud / SaaS Security Standard | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | Cloud landing-zone network baseline |
| Grid Control Systems Security Standard | [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | Electronic security perimeter; OT network constraints |
| Access Management Standard | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Identity for zero-trust decisions; privileged access broker |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Criticality tiers that drive segmentation |
| Secure Configuration Baseline Standard (DISH) | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Hardening of network devices |
| Cryptography and Key Management Standard | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Encryption in transit |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Boundary logging; network detection content |
| Secure Software Development and Application Security Standard | [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) | Infrastructure-as-code enforcement of network baseline |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendor remote access |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `NET` domain |
