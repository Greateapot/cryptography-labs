import reflex as rx

from cryptography.templates import template
from cryptography.backend import Lab6State

UPLOAD_TAG = "lab6_upload_file"


@template(route="/lab6", title="Лаб. №6")
def lab6_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Лабораторная работа №6. Методы сжатия информации", size="6"),
        rx.blockquote(
            "Вариант №15 (№15): Выполнить первое сжатие, "
            "используя алгоритм Хаффмана, и повторное, "
            "используя алгоритм Лемпеля-Зива-Велча.",
            size="4",
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
                "Сжать",
                on_click=Lab6State.encrypt(rx.upload_files(upload_id=UPLOAD_TAG)),
            ),
            rx.button(
                "Расжать",
                on_click=Lab6State.decrypt(rx.upload_files(upload_id=UPLOAD_TAG)),
            ),
            rx.button(
                "Сбросить выбранный файл",
                on_click=rx.clear_selected_files(UPLOAD_TAG),
            ),
            width="50%",
        ),
        width="100%",
    )
