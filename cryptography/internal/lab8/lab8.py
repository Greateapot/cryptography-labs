import os

BLOCK_SIZE = 4  # 4 * 8 = 32 bits
ZERO_BYTE = b"\x00"


def encrypt(
    data: bytes,
    *,
    block_size: int = BLOCK_SIZE,
) -> tuple[bytes, bytes]:
    offset, data_length = 0, len(data)

    result_data, key_data = bytes(), bytes()

    while offset < data_length:
        key = os.urandom(block_size)
        block = data[offset : min(offset + block_size, data_length)]
        offset += block_size

        if len(block) < block_size:
            block += ZERO_BYTE * (block_size - len(block))

        key_data += key
        result_data += bytes(map(lambda b, k: b ^ k, block, key))

    return (result_data, key_data)


def decrypt(
    data: bytes,
    key_data: bytes,
    *,
    block_size: int = BLOCK_SIZE,
) -> bytes:
    offset, data_length = 0, len(data)

    assert len(key_data) == data_length

    result_data = bytes()

    while offset < data_length:
        key = key_data[offset : min(offset + block_size, data_length)]
        block = data[offset : min(offset + block_size, data_length)]
        offset += block_size
        result_data += bytes(map(lambda b, k: b ^ k, block, key))

    return result_data.rstrip(ZERO_BYTE)


__all__ = (
    "BLOCK_SIZE",
    "encrypt",
    "decrypt",
)
