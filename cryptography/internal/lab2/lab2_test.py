from cryptography.internal.lab2.lab2 import (
    generate_primes,
    generate_keys,
    encrypt,
    decrypt,
)


def lab2_test() -> None:
    p, q = generate_primes(128)
    print(f"p: {p}")
    print(f"q: {q}")

    (public_key, private_key) = generate_keys(p, q)
    print(f"public_key: {public_key}")
    print(f"private_key: {private_key}")

    message = "От топота копыт, пыль по полю летит!"
    print(f"message: {message}")

    encrypted_message = encrypt(message, public_key)
    print(f"encrypted_message: {repr(encrypted_message)}")  # repr cuz of \n from b64

    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"decrypted_message: {decrypted_message}")


if __name__ == "__main__":
    lab2_test()
