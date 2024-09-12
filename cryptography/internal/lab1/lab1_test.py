from cryptography.internal.lab1.lab1 import RU_ALGORITHM


def lab1_test() -> None:
    algorithm = RU_ALGORITHM
    print(f"algorithm: {algorithm}")

    (left_table, right_table) = algorithm.generate_tables()
    print(f"left_table: {left_table}")
    print(f"right_table: {right_table}")

    message = "ПРИВЕТ, МИР."
    print(f"message: {message}")

    encrypted_message = algorithm.encrypt(message, (left_table, right_table))
    print(f"encrypted_message: {encrypted_message}")

    decrypted_message = algorithm.decrypt(encrypted_message, (left_table, right_table))
    print(f"decrypted_message: {decrypted_message}")


if __name__ == "__main__":
    lab1_test()
