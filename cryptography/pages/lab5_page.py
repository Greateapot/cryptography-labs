import reflex as rx

from cryptography.templates import template
from cryptography.backend import Lab5State


@template(route="/lab5", title="Лаб. №5")
def lab5_page() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Лабораторная работа №5. Шифры обнаружения и коррекции ошибок",
            size="6",
        ),
        rx.blockquote(
            "Вариант №15 (№18): Реализовать коррекцию "
            "ошибки в двоичной кодовой последовательности, "
            "используя метод циклических кодов "
            "с максимальной степенью полинома 7.",
            size="4",
        ),
        rx.form.root(
            rx.hstack(
                rx.input(
                    name="input_message",
                    placeholder="Введите сообщение...",
                    required=True,
                    width="80%",
                ),
                rx.button(
                    "Закодировать",
                    type="submit",
                    width="20%",
                ),
            ),
            on_submit=Lab5State.encode,
            width="100%",
        ),
        rx.form.root(
            rx.hstack(
                rx.input(
                    name="encoded_message",
                    value=Lab5State.encoded_message,
                    on_change=Lab5State.set_encoded_message,
                    placeholder="Закодированное сообщение...",
                    required=True,
                    width="80%",
                ),
                rx.button(
                    "Декодировать",
                    type="submit",
                    width="20%",
                ),
            ),
            on_submit=Lab5State.decode,
            width="100%",
        ),
        rx.form.root(
            rx.hstack(
                rx.input(
                    name="decoded_message",
                    value=Lab5State.decoded_message,
                    placeholder="Декодированное сообщение...",
                    read_only=True,
                    width="100%",
                ),
            ),
            width="100%",
        ),
        width="100%",
    )
