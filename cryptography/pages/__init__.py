"""Pages."""

#! Import order == navbar/sidebar order
from cryptography.pages.index import index
from cryptography.pages.lab1_page import lab1_page
from cryptography.pages.lab2_page import lab2_page
from cryptography.pages.lab3_page import lab3_page
from cryptography.pages.lab4_page import lab4_page
from cryptography.pages.lab5_page import lab5_page
from cryptography.pages.lab6_page import lab6_page
from cryptography.pages.settings import settings


__all__ = (
    "index",
    "lab1_page",
    "lab2_page",
    "lab3_page",
    "lab4_page",
    "lab5_page",
    "lab6_page",
    "settings",
)
