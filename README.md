# Nachis Sovereign AI & Telemetry Middleware Platform

We are an enterprise B2B Deep Tech software platform providing telemetry normalization and automated cryptographic compliance auditing for defense prime contractors and dual-use hardware manufacturers."

> **Status:** Pre-Seed Functional Prototype & Architecture Baseline  
> **Target Verticals:** Aerospace & Defense Supply Chains, Autonomous Hardware, Regulated Logistics  

An air-gapped, zero-trust middleware engine designed for sub-5ms telemetry ingestion, local model guardrails, and cryptographic SHA-256 Merkle auditing for enterprise and dual-use edge systems.

---

## System Architecture & Module Mapping

* **[INGRESS]**: Hardware Schema Normalization — Live (`/telemetry-normalization`)
* **[AUDITING]**: SHA-256 Merkle Audit Ledger — Live (`/merkle-audit`)
* **[TRANSPORT]**: Sub-5ms gRPC Protobuf Pipeline — In Progress (`/proto`)
* **[EXECUTION]**: Local Air-Gapped Model Gateway — Planned
* **[SECURITY]**: Zero-Trust Threat Guardrails — Planned

---

## Active Engine Modules

* **`/telemetry-normalization`**: Hardware stream parsing, JSON schema validation, and SHA-256 payload hashing.
* **`/merkle-audit`**: Merkle Tree aggregation engine building immutable audit roots from stream hashes.
* **`/proto`**: Defines Protocol Buffer schemas (`telemetry_v1.proto`) for low-latency edge-to-cloud serialization.

---

## Evaluator Quickstart (Local Verification)

Execute the full multi-container pipeline locally:

<img width="1920" height="1020" alt="Screenshot 2026-08-29 124333" src="https://github.com/user-attachments/assets/1c33fe15-ccd3-4a25-a6ed-2f5f208a7eb8" />

<img width="1920" height="1020" alt="Screenshot 2026-08-29 141434" src="https://github.com/user-attachments/assets/d0452164-534c-498d-91d9-13fc3527e004" />


```bash
docker compose up --build
```

### **Live Interactive Microservice Dashboard**

Evaluators can test gRPC payload normalization and Merkle root calculations interactively via the built-in web dashboard at `http://localhost:8080`:

![Live gRPC UI Demo]

<img width="1920" height="1020" alt="Screenshot 2026-08-29 145450" src="https://github.com/user-attachments/assets/e1a192eb-bd27-4a2e-9ba7-032b3652e3ca" />


### **Live Protocol Normalization & Verification**

The gRPC telemetry microservice has been live-tested and verified (`STATUS_HEALTHY`) across three distinct protocol standards:

| Protocol Standard | Domain Focus | Verification Demo |
| :--- | :--- | :--- |
| **STANAG-4586** | Tactical Defense Telemetry | `https://youtu.be/cWCkhfw4TPM` |
| **MAVLink-v2** | Autonomous Commercial Logistics | `https://youtu.be/brUwTL_9I0Y` |
| **Industrial IoT** | Infrastructure & Thermal Sensing | `https://youtu.be/TCAUter-gVY ` |

