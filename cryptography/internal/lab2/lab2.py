import math

from cryptography.internal.abc import ABCKey
from cryptography.internal.utils import (
    generate_prime,
    encode_b64,
    encode_str,
    decode_b64,
    decode_str,
)


class PublicKey(ABCKey):
    e: int
    n: int


class PrivateKey(ABCKey):
    d: int
    n: int


def generate_keys(bits: int) -> tuple[PublicKey, PrivateKey]:
    p = generate_prime(bits)
    q = p

    while q == p:
        q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while math.gcd(e, phi) != 1:
        e += 1

    d = pow(e, -1, phi)

    return (
        PublicKey(bits=bits, e=e, n=n),
        PrivateKey(bits=bits, d=d, n=n),
    )


def encrypt(public_key: PublicKey, string: str) -> str:
    encoded_string = encode_str(string, public_key.bits)

    return encode_b64(
        [pow(i, public_key.e, public_key.n) for i in encoded_string],
        public_key.bits,
    )


def decrypt(private_key: PrivateKey, encrypted_string: str) -> str:
    cipher = decode_b64(encrypted_string, private_key.bits)

    return decode_str(
        [pow(i, private_key.d, private_key.n) for i in cipher],
        private_key.bits,
    )


__all__ = (
    "PrivateKey",
    "PublicKey",
    "generate_keys",
    "encrypt",
    "decrypt",
)
