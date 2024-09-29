import reflex as rx

# Import all the pages.
from cryptography.pages import *  # noqa: F403
from cryptography import styles


# Create the app.
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    title="Cryptography Labs",
)
