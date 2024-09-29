import reflex as rx

from cryptography.internal.lab5 import (
    encode,
    decode,
)


class Lab5State(rx.State):
    # backend-only values
    _POLYNOME = [1, 0, 0, 0, 1, 0, 0, 1]  # x^7 + x^3 + 1 (137)

    # input fields values
    encoded_message: str = ""
    decoded_message: str = ""

    # event handlers

    def encode(self, data: dict) -> None:
        message: str | None = data.get("input_message", None)

        if message is None:
            return  # do nothing

        self.encoded_message = encode(message, self._POLYNOME)
        ...  # return None

    def decode(self, data: dict) -> None:
        encoded_message: str | None = data.get("encoded_message", None)

        if encoded_message is None:
            return  # do nothing

        self.decoded_message = decode(encoded_message, self._POLYNOME)
        ...  # return None
