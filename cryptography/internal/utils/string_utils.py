import base64


def encode_str(string: str, bits: int, encoding: str = "utf-8") -> list[int]:
    byte_array = bytearray(string, encoding)

    z = []

    k = bits // 8
    j = -1 * k
    for i in range(len(byte_array)):
        if i % k == 0:
            j += k
            z.append(0)
        z[j // k] += byte_array[i] * (2 ** (8 * (i % k)))

    return z


def decode_str(bytes: list[int], bits: int, encoding: str = "utf-8") -> str:
    bytes_array = []

    k = bits // 8
    for num in bytes:
        for i in range(k):
            temp = num
            for j in range(i + 1, k):
                temp = temp % (2 ** (8 * j))
            letter = temp // (2 ** (8 * i))
            bytes_array.append(letter)
            num = num - (letter * (2 ** (8 * i)))

    decodedText = bytearray(b for b in bytes_array).decode(encoding)

    return decodedText.replace("\x00", "").strip()


def encode_b64(cipher: list[int], bits: int) -> str:
    b = bytes()

    for x in cipher:
        b += x.to_bytes(bits * 2 // 8)

    return base64.encodebytes(b).decode()


def decode_b64(b64: str, bits: int) -> str:
    b = base64.decodebytes(b64.encode())
    xs = bits * 2 // 8
    return [int.from_bytes(b[i * xs : i * xs + xs]) for i in range(len(b) // xs)]


__all__ = (
    "encode_str",
    "decode_str",
    "encode_b64",
    "decode_b64",
)
