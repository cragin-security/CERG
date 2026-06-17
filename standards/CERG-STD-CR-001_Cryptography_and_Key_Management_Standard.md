
# SURGE: Cyber Engineering, Risk & Governance

## CRYPTOGRAPHY AND KEY MANAGEMENT STANDARD
### Approved Algorithms · TLS · Certificates · Keys · Secrets · API Tokens · CMK · FIPS

---

| | |
|---|---|
| **Document ID** | CERG-STD-CR-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Platforms) |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-RES-001](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **Review Cycle** | Annual / On NIST FIPS publication change · On crypto algorithm deprecation |
| **Frameworks** | NIST FIPS 140-3 · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (SC family) · [NIST 800-57](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) · [NIST 800-131A](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final) · NIST 800-175B |
| **Regulations** | NERC-CIP (BCSI) · [CMMC L2](https://dodcio.defense.gov/CMMC/) / 800-171r3 (3.13.x) · SOX ITGC · FedRAMP |
| **Environments** | All in-scope assets |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Approved and Prohibited Algorithms](#2-approved-and-prohibited-algorithms)
3. [Cryptographic Use Cases](#3-cryptographic-use-cases)
4. [TLS and Certificate Management](#4-tls-and-certificate-management)
5. [Key Management](#5-key-management)
6. [Customer-Managed Keys (CMK) Decision Guide](#6-customer-managed-keys-cmk-decision-guide)
7. [Secrets, API Keys, and Tokens](#7-secrets-api-keys-and-tokens)
8. [Rotation Cadence](#8-rotation-cadence)
9. [FIPS / FedRAMP / CUI Cryptography Checklist](#9-fips--fedramp--cui-cryptography-checklist)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

The Cybersecurity Policy requires encryption in transit and at rest. The IT, CUI, and Access standards each impose specific cryptographic requirements; the Risk Management Framework calls out FIPS-validated cryptography in CUI scope; the OT standard requires protection of BES Cyber System Information (BCSI). Until this standard, those requirements existed in fragments.

This standard establishes a unified cryptographic policy: which algorithms are approved, which are prohibited, how TLS and certificates are managed, how keys / secrets / API tokens are stored and rotated, when customer-managed keys are required, and the FIPS profile for regulated scopes.

It applies to every in-scope asset, every credential and secret used by CERG-managed systems, and every cryptographic use case, data at rest, data in transit, signing, integrity, authentication, and key wrapping.

> **The Crypto Standard Reads Like a Floor, Not a Ceiling**
>
> The algorithms and key sizes named below are minimums. Where a regulator, vendor capability, or specific workload supports a stronger configuration (post-quantum-ready KEM hybrid, larger key size, shorter rotation), CERG adopts it. The standard is the worst the program is willing to accept.

---

## 2. Approved and Prohibited Algorithms

### 2.1 Approved ([NIST 800-131A](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final) current, FIPS 140-3 module where required)

| **Use** | **Approved** | **Minimum Strength** |
|---|---|---|
| Symmetric encryption | AES-128, AES-192, AES-256 (GCM or CBC with HMAC) | AES-128 for non-Restricted; AES-256 for Restricted/CUI/BCSI |
| Hashing | SHA-256, SHA-384, SHA-512 | SHA-256 |
| HMAC | HMAC-SHA-256 and stronger | - |
| Digital signature | RSA-PSS ≥ 3072; ECDSA P-256/P-384/P-521; Ed25519 | RSA 3072 / ECDSA P-256 |
| Key agreement | ECDHE (P-256+), DH (3072+); ML-KEM hybrid where workloads support it | ECDHE P-256 |
| Key derivation | HKDF, PBKDF2 (≥ 600,000 iterations), Argon2id | - |
| Authenticated encryption | AES-GCM, ChaCha20-Poly1305 | - |
| Random number generation | NIST 800-90A approved DRBG; OS CSPRNG | - |

### 2.2 Prohibited (Without Exception)

| **Algorithm / Protocol** | **Why Prohibited** |
|---|---|
| DES, 3DES | Insufficient key strength; deprecated by [NIST 800-131A](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final). |
| MD5 (any use) | Collision attacks make it unfit for any security purpose. |
| SHA-1 (any new use) | Collisions demonstrated; permitted only for HMAC-SHA-1 in legacy compatibility, with a sunset plan. |
| RC4, Blowfish, IDEA | Deprecated / cryptographically weak. |
| SSL 2.0, SSL 3.0 | Deprecated; protocol-level breaks (POODLE et al.). |
| TLS 1.0, TLS 1.1 | Deprecated by all major standards bodies. |
| RSA < 2048 | Insufficient key strength. |
| ECDSA / ECDH on non-NIST curves (other than Ed25519 / Curve25519) | Outside the approved set. |
| ECB mode (any cipher) | Pattern-preserving; unsafe for general data. |
| PKCS#1 v1.5 padding for new use | RSA-PSS required for new signatures. |
| Static IV with stream ciphers / GCM | Catastrophic if reused. |
| Plaintext credentials / secrets at rest | See Section 7. |
| Custom / home-grown algorithms | Cryptographic agility requires reviewed standards. |

> **Exception Requests for Prohibited Algorithms**
>
> Exceptions to the prohibited list are not entertained as compensating-control bargains. The path to using a prohibited algorithm runs through replacing the system, not through a risk acceptance. The only acceptable exception is a time-bounded transitional one with a named sunset date.

### 2.3 Deprecation and Sunset Tracker

| **Algorithm** | **Status** | **Internal Sunset** |
|---|---|---|
| TLS 1.0 / 1.1 | Prohibited | Already retired - confirm via DISH scan |
| SHA-1 (signing) | Prohibited new use | Transitional only - flag for replacement |
| RSA-2048 | Approved (current); plan migration toward 3072 / EC / PQ-hybrid | Roadmap track |
| Classical-only KEMs | Approved; plan ML-KEM hybrid adoption where supported | Roadmap track |

---

## 3. Cryptographic Use Cases

CERG controls cryptography at four use cases. Each names the required algorithm class and the key source.

### 3.1 Data at Rest

- **Volume / disk encryption:** AES-256 via OS or storage platform; keys in HSM or cloud KMS; rotation per Section 8.
- **Database TDE / column-level encryption:** AES-256; CMK for Restricted/CUI/SOX in-scope; rotation per Section 8.
- **Object storage:** server-side encryption with CMK for Restricted/CUI; client-side encryption optional where adversary model includes provider compromise.
- **Backups:** AES-256; key separate from production credentials (see [`CERG-STD-RES-001`](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) Section 4).

### 3.2 Data in Transit

- **External / public-facing services:** TLS 1.2 minimum; TLS 1.3 preferred; HSTS enforced.
- **Internal services:** TLS 1.2 minimum; mTLS where the workload supports it and exposure warrants.
- **Service-to-service in cloud:** provider-native mTLS or service mesh-managed mTLS.
- **Email:** TLS for SMTP transport; S/MIME or PGP for content where CUI or sensitive content is in scope.

### 3.3 Authentication

- **Human authentication credentials:** see [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) (phishing-resistant MFA, password storage requirements).
- **Machine identities:** certificates, signed JWTs, or workload identity (cloud-native), see Section 7.

### 3.4 Signing and Integrity

- **Code signing:** RSA-PSS 3072+ or ECDSA P-256+; keys in HSM; access logged.
- **Container image signing:** cosign / sigstore; signature verification enforced at admission per [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) Section 7.
- **Log integrity:** WORM storage and / or signing per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).
- **Document signing:** PKCS#7 / CAdES with RSA-PSS or ECDSA per use case.

---

## 4. TLS and Certificate Management

### 4.1 TLS Configuration

| **Parameter** | **Public-Facing** | **Internal** |
|---|---|---|
| Minimum protocol | TLS 1.2 | TLS 1.2 |
| Preferred protocol | TLS 1.3 | TLS 1.3 |
| Cipher suites | [NIST 800-52r2](https://csrc.nist.gov/pubs/sp/800/52/r2/final) approved set, AEAD only | Same |
| HSTS | Required | Where applicable |
| Forward secrecy | Required (ECDHE) | Required |
| Renegotiation | Secure renegotiation only | Same |
| OCSP stapling | Required where supported | - |

### 4.2 Certificate Inventory and Lifecycle

| **Step** | **Requirement** |
|---|---|
| Issuance | From an approved internal CA or commercial CA; named in approved-issuers list. |
| Inventory | Authoritative certificate inventory (CA + endpoints + monitored expiry). |
| Validity period | Public TLS ≤ 398 days; internal ≤ 825 days; code signing per HSM-residency policy. |
| Renewal | Automated where supported; alert thresholds at 60 / 30 / 14 days. |
| Revocation | Documented revocation procedure; CRL/OCSP exercised quarterly. |
| Private key storage | HSM or platform key store; never plaintext on disk. |
| Pinning | Limited to mobile and high-risk client/server pairs; pinning rotation procedure required. |
| Wildcard | Avoided for high-value services; permitted with documented risk acceptance. |

---

## 5. Key Management

### 5.1 Key Hierarchy

| **Key Type** | **Storage** | **Rotation (default)** | **Owner** |
|---|---|---|---|
| Root / signing CA keys | HSM (offline for offline root) | n/a (CA refresh ≥ 5y) | Engineering - Platforms |
| Issuing CA keys | HSM | 1–2 years | Engineering - Platforms |
| Data encryption keys (DEKs) | KMS / HSM-backed | Per platform default; ≤ 1 year | Engineering - Platforms |
| Key encryption keys (KEKs) | KMS / HSM | 1 year | Engineering - Platforms |
| Customer-Managed Keys (CMK) | Cloud KMS HSM-backed | Per Section 8 | Engineering - Platforms |
| Code signing keys | HSM | n/a (key rotation triggers re-sign) | Engineering - Platforms / Release |
| TLS certificate keys | HSM or platform key store | Per certificate lifecycle | Engineering - Platforms |

### 5.2 Key Operations

- **Generation**: in HSM or platform KMS; never on developer workstations.
- **Distribution**: via KMS APIs / agent enrollment; never email, chat, or ticket attachments.
- **Storage**: encrypted under a KEK; access logged.
- **Use**: least privilege; key admin separated from key user.
- **Rotation**: scheduled and event-driven (see Section 8).
- **Backup / escrow**: for keys that protect long-lived data, an escrow procedure exists; the escrow itself is HSM-resident and access-controlled.
- **Destruction**: keys destroyed via crypto-shred procedures with documented evidence.

### 5.3 Separation of Duties

| **Action** | **Performed By** | **Approved By** | CISO |---|---|
| Generate root or issuing CA key | Two named operators | Engineering Pillar Leader |
| Rotate KEK | Engineering - Platforms | Engineering Pillar Leader |
| Generate CMK in production | Engineering - Platforms | Workload Owner + Engineering Pillar Leader |
| Destroy / disable production key | Two named operators | Engineering Pillar Leader |
| Export key material (rare; exceptional) | Two named operators | Engineering Pillar Leader + CISO |

---

## 6. Customer-Managed Keys (CMK) Decision Guide

The CMK decision is about who controls the master key, the customer (us) or the provider. CERG requires CMK for the cases below; otherwise provider-managed keys are acceptable.

### 6.1 CMK Required

- Data classified **Restricted** at rest.
- **CUI** in cloud / SaaS scopes (where the regulator permits a provider-managed alternative, CERG defaults to CMK anyway for crypto independence).
- **BCSI** stored in non-OT cloud / SaaS.
- **SOX** in-scope data where the auditor expects independent key control.
- **High-Impact** workloads where adversary model includes provider-side compromise.
- Any workload subject to a **contractual obligation** requiring customer control of keys.

### 6.2 CMK Not Required

- Internal-classification data in standard cloud/SaaS.
- Non-production environments.
- Workloads where the provider's default key management has been assessed and accepted via the [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) Inheritance Evidence Package and risk-register entry.

### 6.3 CMK Operational Requirements

- Keys generated in cloud KMS HSM-backed (FIPS 140-2/3 Level 2+).
- Rotation per Section 8; rotation reuses prior key for read; new writes use new key.
- Key policy and access reviewed quarterly.
- Key material is **never** exported outside the HSM boundary except under the documented exception process.

> **What Inheritance Looks Like When CMK Is Not Required**
>
> "We use the provider's default key management" is only acceptable when the Inheritance Evidence Package in [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) Section 5 is on file. Provider attestation, shared responsibility line item, customer-side configuration prerequisites, and re-papering trigger, all six elements, or CMK is required.

---

## 7. Secrets, API Keys, and Tokens

Plaintext secrets in source code, configuration files, environment variables on disk, or chat history are prohibited under this standard. The handling pattern below is the only acceptable approach.

### 7.1 Storage

| **Secret Type** | **Storage** |
|---|---|
| Application secret (database password, API key consumed by an app) | Secrets manager (HashiCorp Vault, AWS Secrets Manager / Parameter Store, Azure Key Vault, GCP Secret Manager). |
| OAuth client secret | Secrets manager. |
| API token issued by an internal service | Issued by an IdP-integrated token service where possible; otherwise secrets manager. |
| Service account credential | Workload identity (preferred); otherwise short-lived issued credential. |
| Personal access token (PAT) for human use | Created via IdP, time-bounded, scope-bounded, logged. |
| Break-glass credential | Vaulted per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md). |

### 7.2 Distribution and Use

- **Pull, never push.** Workloads retrieve secrets at runtime from the secrets manager; secrets are not baked into images or configs.
- **Short-lived where possible.** Tokens issued by IdP or STS preferred over long-lived static credentials.
- **Scope-bounded.** Each token is scoped to the minimum required resource and action.
- **Logged.** Issuance, retrieval, and revocation events flow to SIEM.

### 7.3 Detection and Hygiene

- Repositories scanned for committed secrets; finding revokes the secret and triggers credential reissue.
- CI/CD pipelines instrumented with secret-scanning gates.
- SBOMs reviewed for embedded secrets in third-party dependencies.

---

## 8. Rotation Cadence

| **Item** | **Default Rotation** | **Tighter For Restricted/CUI/BES** |
|---|---|---|
| Human passwords (where still permitted) | Length and strength controls over rotation; rotate on compromise indicator only | Same |
| Privileged interactive credentials | Same as above; PAM-mediated | PAM-mediated, vaulted, JIT |
| Break-glass account credentials | 90 days or on use | 90 days or on use |
| Service account passwords (where unavoidable) | 90 days | 60 days |
| API keys (long-lived) | 90 days | 60 days |
| OAuth client secrets | 180 days | 90 days |
| Bearer tokens / session tokens | Per IdP / app session policy (short-lived) | Per IdP, short-lived |
| Workload / machine identity certificates | 1 year | 1 year, mTLS preferred |
| TLS server certificates (public) | ≤ 398 days | - |
| TLS server certificates (internal) | ≤ 825 days | ≤ 398 days |
| Data Encryption Keys (DEKs) | Per platform / annually | Annually |
| Key Encryption Keys (KEKs) | Annually | Annually or per event |
| Customer-Managed Keys (CMKs) | Annually + on event | Annually + on event |
| Code-signing keys | Per HSM policy; rotated on suspected compromise | Per HSM policy |
| Issuing CA keys | 1–2 years | Same |
| Root CA keys | ≥ 5 years; offline | Same |

### 8.1 Event-Driven Rotation Triggers

Rotation is also triggered by, not on a schedule alone:

- Suspected key / secret / credential compromise.
- Workforce changes affecting individuals with key access.
- HSM / KMS administrative anomaly.
- Vendor incident notification (per SCCT per [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)).
- Algorithm deprecation or policy update.

---

## 9. FIPS / FedRAMP / CUI Cryptography Checklist

The checklist below is the minimum for any system in CUI scope, FedRAMP Moderate scope, or other regulatory scope that requires FIPS-validated cryptography. It is used at architecture review ([`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)) and at [CMMC](https://dodcio.defense.gov/CMMC/) assessment readiness ([`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md)).

| **Check** | **Required** | **Evidence** |
|---|---|---|
| Cryptographic module is FIPS 140-2 (Level 1+) or FIPS 140-3 validated | ✓ | CMVP certificate number recorded |
| Module is operated in FIPS-approved mode | ✓ | Configuration screenshot / IaC declaration |
| Algorithms in use are on the FIPS-approved list | ✓ | Crypto inventory |
| Keys are HSM-resident or HSM-backed | ✓ | KMS/HSM configuration |
| TLS termination uses FIPS-validated module | ✓ | Load balancer / gateway configuration |
| Cloud provider's FIPS endpoints used where required | ✓ | Endpoint configuration evidence |
| FedRAMP equivalency for CUI cloud / SaaS handled per [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) Inheritance Evidence Package | ✓ | TPRM record |
| CMK in use for CUI data at rest | ✓ (per Section 6) | KMS key inventory |
| CUI data in transit uses FIPS-validated TLS | ✓ | Configuration evidence |
| Secrets manager backing CUI workloads is FIPS-validated | ✓ | Vendor attestation |

---

## 10. Roles and Responsibilities

| **Role** | **Cryptography Responsibility** |
|---|---|
| **Cyber Engineering - Platforms** | Owns this standard. Maintains the cryptographic inventory (algorithms in use, keys, certificates). Operates the KMS/HSM and secrets management platforms. Drives migrations off deprecated algorithms. |
| **Identity Engineer** | Implements credential-side controls per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md); integrates IdP/PAM token issuance with this standard. |
| **Cyber Risk** | Detects use of prohibited algorithms via DISH and other tooling; tracks deprecation risk in the risk register. |
| **Cyber Governance** | Maintains exceptions register for transitional algorithms; tracks audit-facing evidence; cross-references with control library. |
| **Asset Owners** | Choose CMK vs. provider-managed key per Section 6 with Engineering guidance; budget for HSM/KMS cost where applicable. |
| **Procurement / TPRM** | Includes cryptographic conformance in vendor assessments; flags vendor advisories that affect cryptographic posture. |

---
## 11. Document Control

| | |
|---|---|
| **Document ID** | CERG-STD-CR-001 |
| **Version** | 1.21 |
| **Approved By** | CISO |
| **Next Review** | Annual / on FIPS publication change / on algorithm deprecation |
| **Change Log** | 1.0 - Initial publication. Approved/prohibited algorithms, TLS/cert lifecycle, key management, CMK decision guide, secrets/tokens, rotation cadence, FIPS profile. |

