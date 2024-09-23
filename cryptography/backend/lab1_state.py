import reflex as rx

from cryptography.internal.lab1 import (
    Algorithm,
    RU_ALGORITHM,
    EN_ALGORITHM,
)


class Lab1State(rx.State):
    # backend-only vars
    _left_table: str | None = None
    _right_table: str | None = None

    # switchers flags
    is_en_alphabet: bool = False

    # input fields values
    message: str = ""
    encrypted_message: str = ""
    decrypted_message: str = ""

    # vars

    @rx.var
    def left_table(self) -> list[str]:
        return list(self._left_table) if self._left_table is not None else []

    @rx.var
    def right_table(self) -> list[str]:
        return list(self._right_table) if self._right_table is not None else []

    @rx.var
    def tables_generated(self) -> bool:
        return self._left_table is not None and self._right_table is not None

    # event handlers

    def algorithm(self) -> Algorithm:
        return EN_ALGORITHM if self.is_en_alphabet else RU_ALGORITHM

    def clear_input(self) -> None:
        self.message = ""
        self.encrypted_message = ""
        self.decrypted_message = ""
        ...  # return None

    def switch_alphabet(self, checked: bool) -> None:
        self.is_en_alphabet = checked
        (self._left_table, self._right_table) = (None, None)
        self.clear_input()
        ...  # return None

    def generate_tables(self) -> None:
        (self._left_table, self._right_table) = self.algorithm().generate_tables()
        ...  # return None

    def encrypt(self, data: dict) -> None:
        message: str | None = data.get("input_message", None)

        if message is None:
            return  # do nothing

        algorithm = self.algorithm()

        for char in message:
            if char not in algorithm.characters:
                self.encrypted_message = "Сообщение содержит недопустимые символы!"
                return

        self.encrypted_message = algorithm.encrypt(
            message,
            (self._left_table, self._right_table),
        )
        ...  # return None

    def decrypt(self, data: dict) -> None:
        encrypted_message: str | None = data.get("encrypted_message", None)

        if encrypted_message is None:
            return  # do nothing

        self.decrypted_message = self.algorithm().decrypt(
            encrypted_message,
            (self._left_table, self._right_table),
        )

        ...  # return None
