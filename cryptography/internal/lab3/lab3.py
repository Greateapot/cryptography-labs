import random

from cryptography.internal.abc import ABCKey
from cryptography.internal.utils import (
    find_primitive_root,
    generate_prime,
    encode_b64,
    encode_str,
    decode_b64,
    decode_str,
)


class PublicKey(ABCKey):
    p: int
    g: int
    y: int


class PrivateKey(ABCKey):
    p: int
    g: int
    x: int


def generate_keys(bits: int) -> tuple[PublicKey, PrivateKey]:
    p = generate_prime(bits)
    g = find_primitive_root(p)
    x = random.randint(1, (p - 1) // 2)
    y = pow(g, x, p)
    return (
        PublicKey(bits=bits, p=p, g=g, y=y),
        PrivateKey(bits=bits, p=p, g=g, x=x),
    )


def encrypt(public_key: PublicKey, message: str) -> str:
    encoded_message = encode_str(message, public_key.bits // 2)

    encrypted_bytes: list[tuple[int, int]] = []

    for m in encoded_message:
        k = random.randint(2, public_key.p - 2)
        a = pow(public_key.g, k, public_key.p)
        b = (m * pow(public_key.y, k, public_key.p)) % public_key.p
        encrypted_bytes.append((a, b))

    return "|".join(
        map(
            lambda x: encode_b64(x, public_key.bits // 2),
            zip(*encrypted_bytes),
        )
    )


def decrypt(private_key: PrivateKey, encrypted_message: str) -> str:
    encrypted_bytes = list(
        zip(
            *map(
                lambda x: decode_b64(x, private_key.bits // 2),
                encrypted_message.split("|"),
            ),
        ),
    )

    decrypted_bytes: list[int] = []

    for a, b in encrypted_bytes:
        s = pow(a, private_key.x, private_key.p)
        r = (b * pow(s, private_key.p - 2, private_key.p)) % private_key.p
        decrypted_bytes.append(r)

    return decode_str(decrypted_bytes, private_key.bits // 2)


__all__ = (
    "PrivateKey",
    "PublicKey",
    "generate_keys",
    "encrypt",
    "decrypt",
)
