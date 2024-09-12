import reflex as rx

from cryptography.templates import template
from cryptography.backend import Lab2State


@template(route="/lab2", title="Лаб. №2")
def lab2() -> rx.Component:
    return rx.vstack(
        rx.heading("Лабораторная работа №2. Алгоритм RSA", size="6"),
        rx.blockquote(
            "Вариант №15 (№7): Выполнить шифрование строки исходного текста, методом "
            "RSA, используя в качестве p и q простые числа с разрядностью не меньшей "
            "двенадцати, выполнив условие случайности p и q для каждого нового шифрования. ",
            size="4",
        ),
        rx.button(
            rx.text(
                "Сгенерировать простые числа",
                size="3",
            ),
            variant="outline",
            on_click=Lab2State.generate_primes,
        ),
        rx.cond(
            Lab2State.primes_generated,
            rx.box(
                rx.markdown(
                    f"`p`: {Lab2State.p}",
                    width="100%",
                ),
                rx.markdown(
                    f"`q`: {Lab2State.q}",
                    width="100%",
                ),
            ),
            rx.box(),
        ),
        rx.cond(
            Lab2State.primes_generated,
            rx.button(
                rx.text(
                    "Сгенерировать RSA ключи",
                    size="3",
                ),
                variant="outline",
                on_click=Lab2State.generate_keys,
            ),
            rx.box(),
        ),
        rx.cond(
            Lab2State.keys_generated,
            rx.box(
                rx.markdown(
                    f"`e`: {Lab2State.e}",
                    width="100%",
                ),
                rx.markdown(
                    f"`d`: {Lab2State.d}",
                    width="100%",
                ),
                rx.markdown(
                    f"`n`: {Lab2State.n}",
                    width="100%",
                ),
            ),
            rx.box(),
        ),
        rx.cond(
            Lab2State.keys_generated,
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
                on_submit=Lab2State.encrypt,
                width="100%",
            ),
            rx.box(),
        ),
        rx.cond(
            Lab2State.keys_generated,
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="encrypted_message",
                        value=Lab2State.encrypted_message,
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
                on_submit=Lab2State.decrypt,
                width="100%",
            ),
            rx.box(),
        ),
        rx.cond(
            Lab2State.keys_generated,
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="decrypted_message",
                        value=Lab2State.decrypted_message,
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
