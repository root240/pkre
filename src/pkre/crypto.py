
import hashlib, secrets

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def secure_random_hex(nbytes: int = 32) -> str:
    return secrets.token_hex(nbytes)
