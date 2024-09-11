import reflex as rx

from cryptography.templates import template


@template(route="/lab1", title="Лаб. №1")
def lab1() -> rx.Component:
    return rx.vstack(
        rx.heading("Лабораторная работа №1. Шифры перестановки и замены", size="6"),
        rx.blockquote(
            "Вариант №16: Реализовать шифрование текстового "
            "сообщения, используя шифр «двойной квадрат» Уитстона",
            size="4",
        ),
        width="100%",
    )
