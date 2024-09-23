from cryptography.internal.lab2 import (
    generate_keys,
    encrypt,
    decrypt,
)


def lab2_test() -> None:
    bits = 64
    print(f"bits: {bits}")

    (public_key, private_key) = generate_keys(bits)
    print(f"public_key: {public_key}")
    print(f"private_key: {private_key}")

    message = "От топота копыт, пыль по полю летит!"
    print(f"message: {message}")

    encrypted_message = encrypt(public_key, message)
    print(f"encrypted_message: {repr(encrypted_message)}")  # repr cuz of \n from b64

    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"decrypted_message: {decrypted_message}")
    ...


if __name__ == "__main__":
    lab2_test()
