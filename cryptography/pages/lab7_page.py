import reflex as rx

from cryptography.templates import template
from cryptography.backend import Lab7State


@template(route="/lab7", title="Лаб. №7")
def lab7_page() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Лабораторная работа №7. Алгоритмы хеширования паролей",
            size="6",
        ),
        rx.blockquote(
            "Вариант №15 (15): Написать программу, реализующую "
            "методику хеширования паролей, используя в качестве "
            "блочного шифра для реализации алгоритма написанный "
            "ранее в лабораторной работе №4 блочный шифр (согласно "
            "варианту ЛР №4). Длина пароля должна быть не менее 4 "
            "символов и не более 24 символов.",
            size="4",
        ),
        rx.form.root(
            rx.hstack(
                rx.input(
                    name="input_password",
                    placeholder="Введите пароль...",
                    required=True,
                    type="password",
                    min_length=4,
                    max_length=24,
                    width="80%",
                ),
                rx.button(
                    "Получить хэш",
                    type="submit",
                    width="20%",
                ),
            ),
            on_submit=Lab7State.hash,
            width="100%",
        ),
        rx.form.root(
            rx.hstack(
                rx.input(
                    name="hashed_password",
                    value=Lab7State.hashed_password,
                    placeholder="Хэш пароля...",
                    read_only=True,
                    width="100%",
                ),
            ),
            width="100%",
        ),
        width="100%",
    )
