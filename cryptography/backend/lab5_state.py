import reflex as rx

from cryptography.internal.lab5 import (
    encrypt,
    decrypt,
)


class Lab5State(rx.State):
    # backend-only values
    _POLYNOME = [1, 0, 0, 0, 1, 0, 0, 1]  # x^7 + x^3 + 1 (137)

    # input fields values
    encrypted_message: str = ""
    decrypted_message: str = ""

    # event handlers

    def encrypt(self, data: dict) -> None:
        message: str | None = data.get("input_message", None)

        if message is None:
            return  # do nothing

        self.encrypted_message = encrypt(message, self._POLYNOME)
        ...  # return None

    def decrypt(self, data: dict) -> None:
        encrypted_message: str | None = data.get("encrypted_message", None)

        if encrypted_message is None:
            return  # do nothing

        self.decrypted_message = decrypt(encrypted_message, self._POLYNOME)
        ...  # return None
