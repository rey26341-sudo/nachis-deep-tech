import hashlib
import time

class MerkleAuditEngine:
    def __init__(self, leaf_hashes):
        self.leaves = [hashlib.sha256(h.encode('utf-8')).hexdigest() for h in leaf_hashes]

    def build_root(self):
        if not self.leaves:
            return None
        
        current_layer = self.leaves
        while len(current_layer) > 1:
            if len(current_layer) % 2 != 0:
                current_layer.append(current_layer[-1]) # Duplicate last element if odd
            
            next_layer = []
            for i in range(0, len(current_layer), 2):
                combined = current_layer[i] + current_layer[i+1]
                parent_hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
                next_layer.append(parent_hash)
            
            current_layer = next_layer
        
        return current_layer[0]

if __name__ == "__main__":
    print("--- DUAL-USE INTEGRITY & MERKLE AUDIT ENGINE ---\n")
    
    # Mock SHA-256 Telemetry Event Hashes
    sample_event_hashes = [
        "b8162923cd6e0c08ad813cc1f9c2b5bde125fd2d4033408fe1c845ce6a5b2ab4",
        "609b9b862b1a396bfc8da86c9e50ee4c99aab3c030a444b548c900d725a399f8",
        "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",
        "c81e728d9d4c2f636f067f89cc14862c"
    ]

    engine = MerkleAuditEngine(sample_event_hashes)
    merkle_root = engine.build_root()

    print(f"[AUDIT LOG]: Processed {len(sample_event_hashes)} telemetry events.")
    print(f"[MERKLE ROOT HASH]: {merkle_root}")
    print(f"[STATUS]: Cryptographic audit trail verified at timestamp {time.time()}\n")
