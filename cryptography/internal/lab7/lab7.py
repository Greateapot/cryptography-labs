from cryptography.internal.lab4 import encrypt

# / Encryption Params
KEY = b"STATIC_KEY"
KEY_SIZE = 64
BLOCK_SIZE = 64
ROUNDS = 16


def hash(value: str) -> str:
    assert len(value) >= 4 and len(value) <= 24, "invalid value length"

    encrypted = encrypt(
        key_bytes=KEY,
        message_bytes=value.encode(),
        rounds=ROUNDS,
        block_size=BLOCK_SIZE,
        key_size=KEY_SIZE,
    )
    hash = hex(int.from_bytes(encrypted))[2:]
    return hash


__all__ = ("hash",)
