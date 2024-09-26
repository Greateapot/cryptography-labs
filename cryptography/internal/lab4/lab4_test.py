from cryptography.internal.lab4 import (
    encrypt,
    decrypt,
)


def lab4_test() -> None:
    key = "Какой-то ключ".encode()
    message = "Какое-то сообщение".encode()
    rounds = 16
    block_size = 32
    key_size = 8

    print(f"key: {key.decode()}")
    print(f"message: {message.decode()}")

    encrypted_message = encrypt(
        key,
        message,
        rounds=rounds,
        block_size=block_size,
        key_size=key_size,
    )
    print(f"encrypted_message: {encrypted_message}")

    decrypted_message = decrypt(
        key,
        encrypted_message,
        rounds=rounds,
        block_size=block_size,
        key_size=key_size,
    ).replace(b"\x00", b"")
    print(f"decrypted_message: {decrypted_message.decode()}")


if __name__ == "__main__":
    lab4_test()
