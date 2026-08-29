import sys
import os
import time
import hashlib
from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import proto.telemetry_v1_pb2 as pb2
import proto.telemetry_v1_pb2_grpc as pb2_grpc

class MerkleAuditEngine:
    def __init__(self):
        self.leaf_hashes = []

    def add_leaf(self, payload_hash_hex):
        self.leaf_hashes.append(payload_hash_hex)

    def build_root(self):
        if not self.leaf_hashes:
            return ""
        current_layer = [hashlib.sha256(h.encode('utf-8')).hexdigest() for h in self.leaf_hashes]
        while len(current_layer) > 1:
            if len(current_layer) % 2 != 0:
                current_layer.append(current_layer[-1])
            next_layer = []
            for i in range(0, len(current_layer), 2):
                combined = current_layer[i] + current_layer[i+1]
                parent_hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
                next_layer.append(parent_hash)
            current_layer = next_layer
        return current_layer[0]

class TelemetryServicer(pb2_grpc.TelemetryServiceServicer):
    def __init__(self):
        self.audit_engine = MerkleAuditEngine()

    def NormalizeStream(self, request, context):
        raw_bytes = request.raw_payload.encode('utf-8')
        sha256_hash = hashlib.sha256(raw_bytes).hexdigest()
        
        self.audit_engine.add_leaf(sha256_hash)
        merkle_root = self.audit_engine.build_root()

        frame = pb2.TelemetryFrame(
            device_id="UAV-LIVE-001",
            timestamp=time.time(),
            altitude_m=120.5,
            battery_pct=95.0,
            status=pb2.STATUS_HEALTHY,
            payload_hash=sha256_hash.encode('utf-8')
        )

        print(f"[gRPC SERVER RECEIVED]: Protocol={request.source_protocol} | Payload={request.raw_payload}")
        print(f"[gRPC AUDIT UPDATED]: Dynamic Merkle Root = {merkle_root}\n")

        return pb2.NormalizationResponse(
            frame=frame,
            is_valid=True,
            sha256_audit_hash=sha256_hash
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TelemetryServiceServicer_to_server(TelemetryServicer(), server)
    
    # Enable gRPC Reflection for Web UI auto-discovery
    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name['TelemetryService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    print("--- LIVE gRPC MERKLE AUDIT SERVER RUNNING ON PORT 50051 ---")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
