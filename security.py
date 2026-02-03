import hashlib

# for passord and pin hashing


def hash_value(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def verify_value(value: str, hashed: str) -> bool:
    return hash_value(value) == hashed
