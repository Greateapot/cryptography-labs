from cryptography.internal.utils import (
    # decode_b64,
    # encode_b64,
    bytes_to_bits,
    bits_to_bytes,
)


def calculate_dividend(dividend: list[int], divisor: list[int]) -> list[int]:
    dividend = list(dividend)
    divisor = list(divisor)

    while len(dividend) >= len(divisor):
        if dividend[0] == 1:
            for i in range(len(divisor)):
                dividend[i] = dividend[i] ^ divisor[i]
        dividend.pop(0)
    return dividend


def encode_block(data: list[int], polynome: list[int]) -> list[int]:
    data = list(data) + [0] * (len(polynome) - 1)
    remainder = calculate_dividend(data, polynome)
    return data[: len(data) - len(polynome) + 1] + remainder


def decode_block(received: list[int], polynome: list[int]) -> list[int]:
    syndrome = calculate_dividend(received, polynome)

    if any(syndrome):
        for i in range(len(received)):
            received[i] ^= 1
            new_syndrome = calculate_dividend(received, polynome)
            if not any(new_syndrome):
                return received[: len(received) - len(polynome) + 1]
            received[i] ^= 1

    return received[: len(received) - len(polynome) + 1]


def encode(string: str, polynome: list[int]) -> str:
    binary = bytes_to_bits(string.encode())

    encoded_binary = []
    for i in range(0, len(binary), 8):
        data_block = binary[i : i + 8]
        if len(data_block) < 8:
            data_block += [0] * (8 - len(data_block))
        encoded_block = encode_block(data_block, polynome)
        encoded_binary.extend(encoded_block)

    encoded_string = "".join(map(str, encoded_binary))
    return encoded_string


def decode(encoded_string: str, polynome: list[int]) -> str:
    encoded_binary = list(map(int, encoded_string))

    decoded_binary = []
    for i in range(0, len(encoded_binary), 8 + 7):
        received_block = encoded_binary[i : i + 8 + 7]
        decoded_block = decode_block(received_block, polynome)
        decoded_binary.extend(decoded_block)

    decoded_string = bytes(bits_to_bytes(decoded_binary)).decode()
    return decoded_string


__all__ = (
    "encode",
    "decode",
)
