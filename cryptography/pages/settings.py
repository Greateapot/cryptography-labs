import reflex as rx

from cryptography.templates import template
from cryptography.views.color_picker import primary_color_picker, secondary_color_picker
from cryptography.views.radius_picker import radius_picker
from cryptography.views.scaling_picker import scaling_picker


@template(route="/settings", title="Настройки")
def settings() -> rx.Component:
    return rx.vstack(
        rx.heading("Настройки", size="5"),
        # Primary color picker
        rx.vstack(
            rx.hstack(
                rx.icon("palette", color=rx.color("accent", 10)),
                rx.heading("Первичный цвет", size="6"),
                align="center",
            ),
            primary_color_picker(),
            spacing="4",
            width="100%",
        ),
        # Secondary color picker
        rx.vstack(
            rx.hstack(
                rx.icon("blend", color=rx.color("gray", 11)),
                rx.heading("Вторичный цвет", size="6"),
                align="center",
            ),
            secondary_color_picker(),
            spacing="4",
            width="100%",
        ),
        # Radius picker
        radius_picker(),
        # Scaling picker
        scaling_picker(),
        spacing="7",
        width="100%",
    )
