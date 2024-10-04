import reflex as rx

from cryptography.templates import template
from cryptography.backend import Lab4State

UPLOAD_TAG = "lab4_upload_file"


@template(route="/lab4", title="Лаб. №4")
def lab4_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Лабораторная работа №4. Блочное шифрование", size="6"),
        rx.blockquote(
            "Вариант №15 (№19): Реализовать шифрование бинарного файла, "
            "методом блочного шифрования, используя блоки длиной 16 бит, "
            "ключ длиной 16 бит, реализуя в алгоритме шифрования методику DES.",
            size="4",
        ),
        rx.text(f"Кол-во раундов: {Lab4State.rounds}"),
        rx.slider(
            default_value=Lab4State.rounds,
            min=4,
            max=16,
            on_value_commit=Lab4State.on_rounds_commit,
            width="40%",
        ),
        rx.text(f"Размер блока (в битах): {Lab4State.block_size}"),
        rx.slider(
            default_value=Lab4State.block_size,
            min=8,
            max=64,
            step=8,
            on_value_commit=Lab4State.on_block_size_commit,
            width="40%",
        ),
        rx.text(f"Размер ключа (в битах): {Lab4State.key_size}"),
        rx.slider(
            default_value=Lab4State.key_size,
            min=8,
            max=64,
            step=8,
            on_value_commit=Lab4State.on_key_size_commit,
            width="40%",
        ),
        rx.input(
            placeholder="Введите ключ...",
            required=True,
            on_blur=Lab4State.on_key_blur,
            width="40%",
        ),
        rx.upload(
            rx.vstack(
                rx.hstack(rx.foreach(rx.selected_files(UPLOAD_TAG), rx.text)),
                rx.text("Перетащите сюда файл или нажмите для выбора файла"),
            ),
            id=UPLOAD_TAG,
            max_files=1,
        ),
        rx.hstack(
            rx.button(
                "Зашифровать",
                on_click=Lab4State.encrypt(rx.upload_files(upload_id=UPLOAD_TAG)),
            ),
            rx.button(
                "Расшифровать",
                on_click=Lab4State.decrypt(rx.upload_files(upload_id=UPLOAD_TAG)),
            ),
            rx.button(
                "Сбросить выбранный файл",
                on_click=rx.clear_selected_files(UPLOAD_TAG),
            ),
            width="50%",
        ),
        width="100%",
    )
