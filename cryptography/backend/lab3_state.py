import reflex as rx

from cryptography.internal.lab3 import (
    PrivateKey,
    PublicKey,
    generate_keys,
    encrypt,
    decrypt,
)


class Lab3State(rx.State):
    # backend-only vars
    _public_key: PublicKey | None = None
    _private_key: PrivateKey | None = None

    # input fields values
    message: str = ""
    encrypted_message: str = ""
    decrypted_message: str = ""

    # vars

    @rx.var
    def p(self) -> str:
        return str(self._public_key.p) if self._public_key is not None else ""

    @rx.var
    def g(self) -> str:
        return str(self._public_key.g) if self._public_key is not None else ""

    @rx.var
    def y(self) -> str:
        return str(self._public_key.y) if self._public_key is not None else ""

    @rx.var
    def x(self) -> str:
        return str(self._private_key.x) if self._private_key is not None else ""

    @rx.var
    def keys_generated(self) -> bool:
        return self._public_key is not None and self._private_key is not None

    # event handlers

    def generate_keys(self) -> None:
        (self._public_key, self._private_key) = generate_keys(128)
        ...  # return None

    def encrypt(self, data: dict) -> None:
        message: str | None = data.get("input_message", None)

        if message is None:
            return  # do nothing

        self.encrypted_message = encrypt(self._public_key, message)
        ...  # return None

    def decrypt(self, data: dict) -> None:
        encrypted_message: str | None = data.get("encrypted_message", None)

        if encrypted_message is None:
            return  # do nothing

        self.decrypted_message = decrypt(self._private_key, encrypted_message)
        ...  # return None
