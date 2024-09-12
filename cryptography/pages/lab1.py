import reflex as rx

from cryptography import styles
from cryptography.templates import template
from cryptography.backend import Lab1State


def table(title: str, iterable: rx.Var) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            size="4",
        ),
        rx.grid(
            rx.foreach(
                iterable,
                lambda i: rx.center(
                    rx.text(i),
                    border=styles.border,
                    border_radius=styles.border_radius,
                    padding="0.5em",
                ),
            ),
            columns="5",
            spacing="1",
            width="100%",
        ),
        width="100%",
        align="center",
    )


@template(route="/lab1", title="Лаб. №1")
def lab1() -> rx.Component:
    return rx.vstack(
        rx.heading("Лабораторная работа №1. Шифры перестановки и замены", size="6"),
        rx.blockquote(
            "Вариант №16: Реализовать шифрование текстового "
            "сообщения, используя шифр «двойной квадрат» Уитстона",
            size="4",
        ),
        rx.hstack(
            rx.text("Алфавит: "),
            rx.markdown("`RU`"),
            rx.switch(
                checked=Lab1State.is_en_alphabet,
                on_change=Lab1State.switch_alphabet,
            ),
            rx.markdown("`EN`"),
            align="center",
        ),
        rx.button(
            rx.text(
                "Сгенерировать таблицы",
                size="3",
            ),
            variant="outline",
            on_click=Lab1State.generate_tables,
        ),
        rx.cond(
            Lab1State.tables_generated,
            rx.hstack(
                table(
                    "Левая таблица",
                    Lab1State.left_table,
                ),
                rx.spacer(),
                table(
                    "Правая таблица",
                    Lab1State.right_table,
                ),
            ),
            rx.box(),
        ),
        rx.cond(
            Lab1State.tables_generated,
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="input_message",
                        placeholder="Введите сообщение...",
                        required=True,
                        width="80%",
                    ),
                    rx.button(
                        "Зашифровать",
                        type="submit",
                        width="20%",
                    ),
                ),
                on_submit=Lab1State.encrypt,
                width="100%",
            ),
            rx.box(),
        ),
        rx.cond(
            Lab1State.tables_generated,
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="encrypted_message",
                        value=Lab1State.encrypted_message,
                        placeholder="Зашифрованное сообщение...",
                        read_only=True,
                        width="80%",
                    ),
                    rx.button(
                        "Расшифровать",
                        type="submit",
                        width="20%",
                    ),
                ),
                on_submit=Lab1State.decrypt,
                width="100%",
            ),
            rx.box(),
        ),
        rx.cond(
            Lab1State.tables_generated,
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="decrypted_message",
                        value=Lab1State.decrypted_message,
                        placeholder="Расшифрованное сообщение...",
                        read_only=True,
                        width="100%",
                    ),
                ),
                width="100%",
            ),
            rx.box(),
        ),
        width="100%",
    )
