import hashlib

def calculate_merkle_root(leaves):
    if not leaves:
        return ""
    current = [hashlib.sha256(l.encode('utf-8')).hexdigest() for l in leaves]
    while len(current) > 1:
        if len(current) % 2 != 0:
            current.append(current[-1])
        next_layer = []
        for i in range(0, len(current), 2):
            combined = current[i] + current[i+1]
            next_layer.append(hashlib.sha256(combined.encode('utf-8')).hexdigest())
        current = next_layer
    return current[0]

def test_sha256_deterministic_hashing():
    payload = "UAV-TEST-PAYLOAD"
    hash1 = hashlib.sha256(payload.encode('utf-8')).hexdigest()
    hash2 = hashlib.sha256(payload.encode('utf-8')).hexdigest()
    assert hash1 == hash2

def test_merkle_root_single_leaf():
    leaves = ["hash_a"]
    root = calculate_merkle_root(leaves)
    expected = hashlib.sha256("hash_a".encode('utf-8')).hexdigest()
    assert root == expected

def test_merkle_root_even_leaves():
    leaves = ["hash_a", "hash_b"]
    root = calculate_merkle_root(leaves)
    h_a = hashlib.sha256("hash_a".encode('utf-8')).hexdigest()
    h_b = hashlib.sha256("hash_b".encode('utf-8')).hexdigest()
    expected = hashlib.sha256((h_a + h_b).encode('utf-8')).hexdigest()
    assert root == expected
