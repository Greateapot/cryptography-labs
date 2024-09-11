import reflex as rx

from cryptography.templates import template


@template(route="/", title="Домашняя страница")
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Привет, мир!", size="6"),
        width="100%",
    )
