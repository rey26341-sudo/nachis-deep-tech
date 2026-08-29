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

```bash
docker compose up --build
