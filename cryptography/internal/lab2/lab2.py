import base64
import math

from cryptography.internal.utils.prime_utils import generate_prime

Key = tuple[int, int]


def generate_primes(k: int = 512) -> tuple[int, int]:
    p = generate_prime(k)
    q = p

    while q == p:
        q = generate_prime(k)

    return p, q


def generate_keys(p: int, q: int) -> tuple[Key, Key]:
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while math.gcd(e, phi) != 1:
        e += 1

    d = pow(e, -1, phi)

    return ((e, n), (d, n))


def get_key_len(key: Key) -> int:
    _, n = key
    return n.bit_length() // 8  # no bits, only bytes


def base64_to_bytes(s: str) -> bytes:
    return base64.decodebytes(s.encode())


def bytes_to_base64(b: bytes) -> str:
    return base64.encodebytes(b).decode()


def str_to_bytes(s: str) -> bytes:
    return s.encode()


def bytes_to_str(b: bytes) -> str:
    return b.decode()


def int_to_bytes(i: int, length: int) -> bytes:
    return i.to_bytes(length)


def bytes_to_int(b: bytes) -> int:
    return int.from_bytes(b)


def encrypt_int(i: int, public_key: Key) -> int:
    e, n = public_key
    return pow(i, e, n)


def decrypt_int(i: int, private_key: Key) -> int:
    d, n = private_key
    return pow(i, d, n)


def encrypt_bytes(b: bytes, public_key: Key) -> bytes:
    k = get_key_len(public_key)
    k += 1 if k % 8 else 0

    i = bytes_to_int(b)
    ei = encrypt_int(i, public_key)
    rb = int_to_bytes(ei, k)

    # print(i, ei, i.bit_length(), ei.bit_length())
    # print(b, rb)

    return rb


def decrypt_bytes(b: bytes, private_key: Key) -> bytes:
    k = get_key_len(private_key)
    k += 1 if k % 8 else 0

    i = bytes_to_int(b)
    di = decrypt_int(i, private_key)
    rb = int_to_bytes(di, k)

    # print(i, di, i.bit_length(), di.bit_length())
    # print(b, rb)

    return rb


def encrypt(s: str, public_key: Key) -> str:
    b = str_to_bytes(s)
    k = get_key_len(public_key)
    k -= 1

    rb = bytes()
    for i in range(len(b) // k + (1 if len(b) % k else 0)):
        bp = b[i * k : i * k + k]
        bpc = encrypt_bytes(bp, public_key)
        # print(f"bp: {bp}; bpc: {bpc}")
        rb += bpc

    # print(b)

    return bytes_to_base64(rb)


def decrypt(s: str, private_key: Key) -> str:
    b = base64_to_bytes(s)
    k = get_key_len(private_key)
    k += 1 if k % 8 else 0

    rb = bytes()
    for i in range(len(b) // k + (1 if len(b) % k else 0)):
        bp = b[i * k : i * k + k]
        bpd = decrypt_bytes(bp, private_key)
        # print(f"bp: {bp}; bpd: {bpd}")
        rb += bpd.replace(b"\x00", b"")  # clear chunks padding

    # print(rb)

    return bytes_to_str(rb)
