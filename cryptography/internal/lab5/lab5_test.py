from cryptography.internal.lab5.lab5 import (
    encode,
    decode,
)


def lab5_test() -> None:
    ...
    text = "Привет, мир! 👋🌍"
    print("Исходный текст:", text)

    ...
    polynome = [1, 0, 0, 0, 1, 0, 0, 1]  # Порождающий полином (x^7 + x^3 + 1)

    ...
    encoded_text = encode(text, polynome)
    print("Закодированный текст:", repr(encoded_text))

    ...
    _encoded_text = encoded_text[:]
    encoded_text = encoded_text[:-1]
    encoded_text += "0" if _encoded_text[-1] == "1" else "1"
    print("Поврежденный текст:", repr(encoded_text))

    ...
    decoded_text = decode(_encoded_text, polynome)
    print("Декодированный текст:", decoded_text)

    ...


if __name__ == "__main__":
    lab5_test()
