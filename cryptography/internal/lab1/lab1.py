from __future__ import annotations

import itertools
import random
import sys

from pydantic import BaseModel


class Alphabet(BaseModel):
    characters: str
    table_height: int
    table_width: int

    @staticmethod
    def RU() -> Alphabet:
        return Alphabet(
            characters="ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ:., ",
            table_height=7,
            table_width=5,
        )

    @staticmethod
    def EN() -> Alphabet:
        return Alphabet(
            characters="QWERTYUIOPASDFGHJKLZXCVBNM:., ",
            table_height=6,
            table_width=5,
        )


class Table(BaseModel):
    table: list[list[str]] | None = None

    def generate_table(
        self,
        alphabet: Alphabet,
        *,
        random_seed: int | float | str | bytes | bytearray | None = None,
    ) -> None:
        prng = random.Random(random_seed)
        chars = list(alphabet.characters)
        prng.shuffle(chars)
        self.table = list(map(list, itertools.batched(chars, alphabet.table_width)))
        ...

    def get_char(self, y: int, x: int) -> str:
        return self.table[y][x]

    def get_char_position(self, char: str) -> tuple[int, int]:
        for y in range(len(self.table)):
            for x in range(len(self.table[y])):
                if self.table[y][x] == char:
                    return (y, x)

        raise Exception(f"char {char} not found")


class AlgorithmData(BaseModel):
    alphabet: Alphabet
    random_seed: int | float | str | bytes | None = None
    left_table: Table | None = None
    right_table: Table | None = None

    @staticmethod
    def DEFAULT():
        return AlgorithmData(alphabet=Alphabet.RU())

    def generate_tables(
        self,
        random_seed: int | float | str | bytes | None = None,
    ) -> None:
        def init():  # создание таблиц
            self.left_table = Table()
            self.right_table = Table()

        def generate():  # заполнение таблиц
            self.left_table.generate_table(self.alphabet, random_seed=self.random_seed)
            self.right_table.generate_table(self.alphabet, random_seed=self.random_seed)

        if random_seed is not None:  # если новый сид
            self.random_seed = random_seed  # сохраняем его
            if self.left_table is None:  # если нет таблиц
                init()  # создаем
            generate()  # заполняем таблицы

        elif self.random_seed is None:  # если нет сида
            self.random_seed = random.randrange(sys.maxsize)  # создаем его
            if self.left_table is None:  # если нет таблиц
                init()  # создаем
            generate()  # заполняем таблицы

        else:
            if self.left_table is None:  # если нет таблиц
                init()  # создаем
                generate()  # и заполняем


class Algorithm:
    def __init__(self, data: AlgorithmData) -> None:
        self.data = data
        self.data.generate_tables()

    def encrypt(self, value: str) -> str:
        if len(value) % 2 == 1:
            value += " "

        chars = ""

        for index in range(0, len(value), 2):
            left_char = value[index]
            right_char = value[index + 1]

            (left_y, left_x) = self.data.left_table.get_char_position(left_char)
            (right_y, right_x) = self.data.right_table.get_char_position(right_char)

            chars += self.data.right_table.get_char(left_y, right_x)
            chars += self.data.left_table.get_char(right_y, left_x)

        return chars

    def decrypt(self, value: str) -> str:
        assert len(value) & 0

        chars = ""

        for index in range(0, len(value), 2):
            left_char = value[index]
            right_char = value[index + 1]

            (left_y, left_x) = self.data.right_table.get_char_position(left_char)
            (right_y, right_x) = self.data.left_table.get_char_position(right_char)

            chars += self.data.left_table.get_char(left_y, right_x)
            chars += self.data.right_table.get_char(right_y, left_x)

        return chars
