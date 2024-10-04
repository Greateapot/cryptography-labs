from cryptography.internal.utils import (
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


def encrypt_block(data: list[int], polynome: list[int]) -> list[int]:
    data = list(data) + [0] * (len(polynome) - 1)
    remainder = calculate_dividend(data, polynome)
    return data[: len(data) - len(polynome) + 1] + remainder


def decrypt_block(received: list[int], polynome: list[int]) -> list[int]:
    syndrome = calculate_dividend(received, polynome)

    if any(syndrome):
        for i in range(len(received)):
            received[i] ^= 1
            new_syndrome = calculate_dividend(received, polynome)
            if not any(new_syndrome):
                return received[: len(received) - len(polynome) + 1]
            received[i] ^= 1

    return received[: len(received) - len(polynome) + 1]


def encrypt(string: str, polynome: list[int]) -> str:
    binary = bytes_to_bits(string.encode())

    encrypted_binary = []
    for i in range(0, len(binary), 8):
        data_block = binary[i : i + 8]
        if len(data_block) < 8:
            data_block += [0] * (8 - len(data_block))
        encrypted_block = encrypt_block(data_block, polynome)
        encrypted_binary.extend(encrypted_block)

    encrypted_string = "".join(map(str, encrypted_binary))
    return encrypted_string


def decrypt(encrypted_string: str, polynome: list[int]) -> str:
    encrypted_binary = list(map(int, encrypted_string))

    decrypted_binary = []
    for i in range(0, len(encrypted_binary), 8 + 7):
        received_block = encrypted_binary[i : i + 8 + 7]
        decrypted_block = decrypt_block(received_block, polynome)
        decrypted_binary.extend(decrypted_block)

    decrypted_string = bytes(bits_to_bytes(decrypted_binary)).decode()
    return decrypted_string


__all__ = (
    "encrypt",
    "decrypt",
)
