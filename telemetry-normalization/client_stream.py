import sys
import os
import time
import grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import proto.telemetry_v1_pb2 as pb2
import proto.telemetry_v1_pb2_grpc as pb2_grpc

def run_client():
    server_host = os.getenv("AUDIT_SERVER_HOST", "localhost")
    target = f"{server_host}:50051"
    print(f"--- CONNECTING TELEMETRY CLIENT TO gRPC SERVER AT {target} ---")
    
    time.sleep(3)
    
    with grpc.insecure_channel(target) as channel:
        stub = pb2_grpc.TelemetryServiceStub(channel)
        
        telemetry_samples = [
            '{"raw_id": "UAV-DEFENSE-001", "alt": 142.5, "bat": 88, "sys_ok": true}',
            '{"raw_id": "UAV-DEFENSE-002", "alt": 210.0, "bat": 64, "sys_ok": true}',
            '{"raw_id": "UAV-CIVILIAN-003", "alt": 45.0, "bat": 15, "sys_ok": false}'
        ]
        
        for sample in telemetry_samples:
            try:
                request = pb2.NormalizationRequest(
                    raw_payload=sample,
                    source_protocol="MAVLink-v2"
                )
                response = stub.NormalizeStream(request)
                print(f"[gRPC CLIENT TRANSMITTED]: {sample}")
                print(f"[gRPC SERVER ACK]: Valid={response.is_valid} | Hash={response.sha256_audit_hash}")
            except Exception as e:
                print(f"[gRPC CLIENT ERROR]: {e}")
            time.sleep(2)

if __name__ == "__main__":
    run_client()
