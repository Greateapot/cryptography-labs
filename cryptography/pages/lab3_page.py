import reflex as rx

from cryptography.templates import template
from cryptography.backend import Lab3State


@template(route="/lab3", title="Лаб. №3")
def lab3_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Лабораторная работа №3. Алгоритм Эль-Гамаля", size="6"),
        rx.blockquote(
            "Вариант №15 (№25): Выполнить шифрование текстового сообщения "
            "длиной не меньшей 256 символов, методом Эль-Гамаля, используя "
            "в качестве x и g простые числа с разрядностью не меньшей "
            "двенадцати и p и k не менее двадцати, выполнив условие "
            "случайности x и g для каждого нового шифрования.",
            size="4",
        ),
        rx.button(
            rx.text(
                "Сгенерировать ключи",
                size="3",
            ),
            variant="outline",
            on_click=Lab3State.generate_keys,
        ),
        rx.cond(
            Lab3State.keys_generated,
            rx.box(
                rx.markdown(
                    f"`p`: {Lab3State.p}",
                    width="100%",
                ),
                rx.markdown(
                    f"`g`: {Lab3State.g}",
                    width="100%",
                ),
                rx.markdown(
                    f"`y`: {Lab3State.y}",
                    width="100%",
                ),
                rx.markdown(
                    f"`x`: {Lab3State.x}",
                    width="100%",
                ),
            ),
            rx.box(),
        ),
        rx.cond(
            Lab3State.keys_generated,
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
                on_submit=Lab3State.encrypt,
                width="100%",
            ),
            rx.box(),
        ),
        rx.cond(
            Lab3State.keys_generated,
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="encrypted_message",
                        value=Lab3State.encrypted_message,
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
                on_submit=Lab3State.decrypt,
                width="100%",
            ),
            rx.box(),
        ),
        rx.cond(
            Lab3State.keys_generated,
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="decrypted_message",
                        value=Lab3State.decrypted_message,
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
