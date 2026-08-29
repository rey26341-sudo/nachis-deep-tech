import json
import hashlib
import time
from jsonschema import validate, ValidationError

# 1. Define Standard Normalized Telemetry Schema
SCHEMA = {
    "type": "object",
    "properties": {
        "device_id": {"type": "string"},
        "timestamp": {"type": "number"},
        "altitude_m": {"type": "number"},
        "battery_pct": {"type": "number"},
        "status": {"type": "string"}
    },
    "required": ["device_id", "timestamp", "altitude_m", "battery_pct", "status"]
}

# 2. Raw Mock Telemetry Data Input
raw_telemetry_stream = [
    {"raw_id": "UAV-DEFENSE-001", "alt": 142.5, "bat": 88, "sys_ok": True},
    {"raw_id": "UAV-CIVILIAN-002", "alt": 95.0, "bat": 12, "sys_ok": False}
]

def normalize_and_audit(raw_item):
    # Data Normalization
    normalized = {
        "device_id": raw_item["raw_id"],
        "timestamp": time.time(),
        "altitude_m": float(raw_item["alt"]),
        "battery_pct": float(raw_item["bat"]),
        "status": "HEALTHY" if raw_item["sys_ok"] else "WARNING"
    }

    # Schema Validation
    try:
        validate(instance=normalized, schema=SCHEMA)
        valid = True
    except ValidationError as e:
        valid = False

    # Cryptographic Hash (Append-Only Audit Proof)
    payload_bytes = json.dumps(normalized, sort_keys=True).encode('utf-8')
    data_hash = hashlib.sha256(payload_bytes).hexdigest()

    return normalized, valid, data_hash

if __name__ == "__main__":
    print("--- DUAL-USE TELEMETRY NORMALIZATION BENCHMARK ---\n")
    for item in raw_telemetry_stream:
        data, is_valid, payload_hash = normalize_and_audit(item)
        print(f"[INPUT RAW]: {item}")
        print(f"[NORMALIZED]: {json.dumps(data)}")
        print(f"[VALIDATED]: {is_valid} | [SHA256 AUDIT HASH]: {payload_hash}\n")
