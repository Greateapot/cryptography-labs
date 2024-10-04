from cryptography.internal.lab8 import encrypt, decrypt


def lab8_test() -> None:
    input_file = "uploaded_files/lab8_data_file.txt"
    encrypted_file = "uploaded_files/lab8_encrypted_data_file.txt"
    decrypted_file = "uploaded_files/lab8_decrypted_data_file.txt"
    key_file = "uploaded_files/lab8_key_file.txt"

    ...  # / Encrypt
    with (
        open(input_file, "rb") as i_file,
        open(encrypted_file, "wb") as e_file,
        open(key_file, "wb") as k_file,
    ):
        data = i_file.read()
        (encrypted_data, key_data) = encrypt(data)
        e_file.write(encrypted_data)
        k_file.write(key_data)

    ...  # / Decrypt
    with (
        open(encrypted_file, "rb") as e_file,
        open(key_file, "rb") as k_file,
        open(decrypted_file, "wb") as d_file,
    ):
        encrypted_data = e_file.read()
        key_data = k_file.read()

        decrypted_data = decrypt(encrypted_data, key_data)
        d_file.write(decrypted_data)

    ...  # / Validation
    with (
        open(input_file, "rb") as i_file,
        open(decrypted_file, "rb") as d_file,
    ):
        assert i_file.read() == d_file.read()

    ...  # return None


if __name__ == "__main__":
    lab8_test()
