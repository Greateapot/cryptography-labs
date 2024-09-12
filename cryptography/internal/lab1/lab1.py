from __future__ import annotations

import random

from pydantic import BaseModel


class Algorithm(BaseModel):
    characters: str
    table_height: int
    table_width: int

    def generate_table(self) -> str:
        chars = list(self.characters)
        random.shuffle(chars)
        return "".join(chars)

    def get_char(self, table: str, y: int, x: int) -> str:
        return table[y * self.table_width + x]

    def get_char_position(self, table: str, char: str) -> tuple[int, int]:
        index = table.index(char)
        return (index // self.table_width, index % self.table_width)

    def generate_tables(self) -> tuple[str, str]:
        return (self.generate_table(), self.generate_table())

    def encrypt(self, message: str, tables: tuple[str, str]) -> str:
        if len(message) % 2 == 1:
            message += " "

        (left_table, right_table) = tables
        chars = ""

        for index in range(0, len(message), 2):
            left_char = message[index]
            right_char = message[index + 1]

            (left_y, left_x) = self.get_char_position(left_table, left_char)
            (right_y, right_x) = self.get_char_position(right_table, right_char)

            chars += self.get_char(right_table, left_y, right_x)
            chars += self.get_char(left_table, right_y, left_x)

        return chars

    def decrypt(self, encrypted_message: str, tables: tuple[str, str]) -> str:
        assert len(encrypted_message) % 2 == 0

        (left_table, right_table) = tables
        chars = ""

        for index in range(0, len(encrypted_message), 2):
            left_char = encrypted_message[index]
            right_char = encrypted_message[index + 1]

            (left_y, left_x) = self.get_char_position(right_table, left_char)
            (right_y, right_x) = self.get_char_position(left_table, right_char)

            chars += self.get_char(left_table, left_y, right_x)
            chars += self.get_char(right_table, right_y, left_x)

        return chars


RU_ALGORITHM = Algorithm(
    characters="ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ:., ",
    table_height=7,
    table_width=5,
)

EN_ALGORITHM = Algorithm(
    characters="QWERTYUIOPASDFGHJKLZXCVBNM:., ",
    table_height=6,
    table_width=5,
)
