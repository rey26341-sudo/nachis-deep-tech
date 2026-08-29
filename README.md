# nachis-deep-tech

> **Sovereign Telemetry Normalization & Cryptographic Audit Pipeline**  
> *Deterministic, zero-trust telemetry processing middleware for defense prime contractors and dual-use hardware manufacturers.*

---

## **Overview**

`nachis-deep-tech` provides lightweight, sub-5ms telemetry normalization and deterministic cryptographic hash verification for uncrewed systems, autonomous logistics, and industrial IoT hardware.

By transforming heterogeneous protocol payloads (STANAG-4586, MAVLink-v2, and custom IoT formats) into standardized gRPC schemas, the system continuously appends verified frame hashes to an in-memory Merkle Tree for real-time auditability.

---

## **Live Multi-Protocol Verification Demos**

The gRPC telemetry microservice has been verified (`STATUS_HEALTHY`) across three hardware payload profiles. Click any link below to watch the live execution recordings:

| Protocol Standard | Domain Focus | Verification Link |
| :--- | :--- | :--- |
| **STANAG-4586** | Tactical Defense Telemetry | [![Watch Demo](https://img.shields.io/badge/Demo-STANAG--4586-blue?style=flat-square&logo=youtube)](https://youtu.be/03R_nQ4Qx5Y) |
| **MAVLink-v2** | Autonomous Commercial Logistics | [![Watch Demo](https://img.shields.io/badge/Demo-MAVLink--v2-blue?style=flat-square&logo=youtube)](https://youtu.be/G2R5m6G2gWk) |
| **Custom Industrial IoT** | Asset Health & Thermal Sensing | [![Watch Demo](https://img.shields.io/badge/Demo-Industrial%20IoT-blue?style=flat-square&logo=youtube)](https://youtu.be/TCAUter-gVY) |

*(Note: Videos are hosted as unlisted demonstrations intended for technical reviewers and evaluators).*

---

## **System Architecture & Module Mapping**

| Module Path | Primary Responsibility | Technical Stack | Implementation Status |
| :--- | :--- | :--- | :--- |
| `/proto` | Protocol Buffer definitions (`.proto`) for gRPC contracts | Protobuf v3 | **Live / Verified** |
| `/telemetry-normalization` | Multi-protocol parsing and standard frame extraction | Python 3.11, gRPC | **Live / Verified** |
| `/merkle-audit` | Cryptographic SHA-256 Merkle root hash computation | Python, PyCryptodome | **Live / Verified** |
| `/docs` | Architecture diagrams and technical evaluation appendix | Markdown | **Live** |
| `/benchmarks` | High-frequency stress-testing scripts (1,000+ fps) | Pytest, Locust | *In Progress* |

---

## **Evaluator Quickstart**

### **Prerequisites**
* **Docker Desktop** (v20.10+ recommended)
* **Docker Compose** (v2.0+)
* Available ports on host machine: `8080` (gRPC Web UI) and `50051` (gRPC Server)

### **Local Execution**
Run the full multi-container pipeline locally with a single command:

```bash
docker compose up --build
```

<img width="1920" height="1020" alt="Screenshot 2026-08-29 123128" src="https://github.com/user-attachments/assets/857d1381-8ee1-4b9e-961d-1732aac269f3" />

<img width="1920" height="1020" alt="Screenshot 2026-08-29 141434" src="https://github.com/user-attachments/assets/cff7fd0d-3a2b-44cc-9d2f-ae65576832ae" />

