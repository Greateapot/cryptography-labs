import reflex as rx

from cryptography.templates import template
from cryptography.backend import Lab8State

UPLOAD_TAG = "lab8_upload_file"


@template(route="/lab8", title="Лаб. №8")
def lab8_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Лабораторная работа №8. Блочное шифрование", size="6"),
        rx.blockquote(
            "Вариант №15 (№10): Реализовать шифрование файла методом "
            "однократного гаммирования, используя блоки открытого текста "
            "длиной 32 бита и используя в алгоритме шифрования операцию сложения.",
            size="4",
        ),
        rx.text(f"Размер блока (в байтах): {Lab8State.block_size}"),
        rx.slider(
            default_value=Lab8State.block_size,
            min=4,
            max=16,
            on_value_commit=Lab8State.on_block_size_commit,
            width="40%",
        ),
        rx.upload(
            rx.vstack(
                rx.hstack(rx.foreach(rx.selected_files(UPLOAD_TAG), rx.text)),
                rx.text("Перетащите сюда файл или нажмите для выбора файла"),
            ),
            id=UPLOAD_TAG,
            max_files=2,
        ),
        rx.hstack(
            rx.button(
                "Зашифровать",
                on_click=Lab8State.encrypt(rx.upload_files(upload_id=UPLOAD_TAG)),
            ),
            rx.button(
                "Расшифровать",
                on_click=Lab8State.decrypt(rx.upload_files(upload_id=UPLOAD_TAG)),
            ),
            rx.button(
                "Сбросить выбранные файлы",
                on_click=rx.clear_selected_files(UPLOAD_TAG),
            ),
            width="50%",
        ),
        width="100%",
    )
