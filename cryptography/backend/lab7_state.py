import reflex as rx

from cryptography.internal.lab7 import hash


class Lab7State(rx.State):
    # input fields values
    hashed_password: str = ""

    # event handlers

    def hash(self, data: dict) -> None:
        password: str | None = data.get("input_password", None)

        if password is None:
            return  # do nothing

        self.hashed_password = hash(password)
        ...  # return None
