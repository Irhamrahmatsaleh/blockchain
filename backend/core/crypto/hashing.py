import hashlib
import json

# 🔁 Fungsi umum untuk hashing objek/data
def hash_data(data) -> str:
    if isinstance(data, (dict, list)):
        serialized = json.dumps(data, sort_keys=True)
    elif isinstance(data, str):
        serialized = data
    else:
        serialized = str(data)

    return hashlib.sha256(serialized.encode()).hexdigest()

# 🔁 Hash string langsung
def hash_string(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()
