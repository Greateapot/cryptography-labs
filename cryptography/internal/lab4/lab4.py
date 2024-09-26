from math import ceil, log2


def encrypt_block(
    key: int,
    block: int,
    *,
    rounds: int = 4,
    bits: int = 16,
) -> int:
    half_bits = bits // 2
    truncator = int(pow(2, half_bits)) - 1

    left = (block >> half_bits) & truncator
    right = block & truncator

    for i in range(rounds):
        subkey = (key ^ (i * 0x3F)) & truncator
        left, right = right, left ^ (right ^ subkey)

    return (right << half_bits) | left


def decrypt_block(
    key: int,
    encrypted_block: int,
    *,
    rounds: int = 4,
    bits: int = 16,
) -> int:
    half_bits = bits // 2
    truncator = int(pow(2, half_bits)) - 1

    left = (encrypted_block >> half_bits) & truncator
    right = encrypted_block & truncator

    for i in range(rounds - 1, -1, -1):
        subkey = (key ^ (i * 0x3F)) & truncator
        left, right = right, left ^ (right ^ subkey)

    return (right << half_bits) | left


def encrypt(
    key_bytes: bytes,
    message_bytes: bytes,
    *,
    rounds: int = 4,
    block_size: int = 16,
    key_size: int = 16,
) -> bytes:
    assert rounds > 0
    assert block_size > 7 and log2(block_size).is_integer()
    assert key_size > 7 and log2(key_size).is_integer()

    block_size = block_size // 8
    key_size = key_size // 8

    key_bytes = key_bytes[:key_size]
    key = int.from_bytes(key_bytes)

    message_bytes_length = len(message_bytes)
    encrypted_message_bytes = bytes()
    blocks = ceil(message_bytes_length / block_size)

    for index in range(blocks):
        offset = index * block_size
        block_bytes = message_bytes[
            offset : offset + min(block_size, message_bytes_length - offset)
        ]
        block = int.from_bytes(block_bytes)
        encrypted_block = encrypt_block(
            key,
            block,
            rounds=rounds,
            bits=block_size * 8,
        )
        encrypted_block_bytes = encrypted_block.to_bytes(block_size)
        encrypted_message_bytes += encrypted_block_bytes

    return encrypted_message_bytes


def decrypt(
    key_bytes: bytes,
    encrypted_message_bytes: bytes,
    *,
    rounds: int = 4,
    block_size: int = 16,
    key_size: int = 16,
) -> bytes:
    assert rounds > 0
    assert block_size > 7 and log2(block_size).is_integer()
    assert key_size > 7 and log2(key_size).is_integer()

    block_size = block_size // 8
    key_size = key_size // 8

    key_bytes = key_bytes[:key_size]
    key = int.from_bytes(key_bytes)

    encrypted_message_bytes_length = len(encrypted_message_bytes)
    decrypted_message_bytes = bytes()
    blocks = ceil(encrypted_message_bytes_length / block_size)

    for index in range(blocks):
        offset = index * block_size
        encrypted_block_bytes = encrypted_message_bytes[
            offset : offset + min(block_size, encrypted_message_bytes_length - offset)
        ]
        encrypted_block = int.from_bytes(encrypted_block_bytes)
        decrypted_block = decrypt_block(
            key,
            encrypted_block,
            rounds=rounds,
            bits=block_size * 8,
        )
        decrypted_block_bytes = decrypted_block.to_bytes(block_size)
        decrypted_message_bytes += decrypted_block_bytes

    return decrypted_message_bytes


__all__ = (
    "encrypt",
    "decrypt",
)
