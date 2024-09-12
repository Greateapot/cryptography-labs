import reflex as rx

from cryptography.internal.lab2 import (
    generate_primes,
    generate_keys,
    encrypt,
    decrypt,
)


class Lab2State(rx.State):
    # backend-only vars
    _p: int | None = None
    _q: int | None = None
    _e: int | None = None
    _d: int | None = None
    _n: int | None = None

    # input fields values
    message: str = ""
    encrypted_message: str = ""
    decrypted_message: str = ""

    # vars

    @rx.var
    def p(self) -> str:
        return str(self._p)

    @rx.var
    def q(self) -> str:
        return str(self._q)

    @rx.var
    def e(self) -> str:
        return str(self._e)

    @rx.var
    def d(self) -> str:
        return str(self._d)

    @rx.var
    def n(self) -> str:
        return str(self._n)

    @rx.var
    def primes_generated(self) -> bool:
        return self._p is not None and self._q is not None

    @rx.var
    def keys_generated(self) -> bool:
        return self._e is not None and self._d is not None and self._n is not None

    # event handlers

    def generate_primes(self) -> None:
        (self._p, self._q) = generate_primes(128)
        (self._e, self._d, self._n) = (None, None, None)
        ...  # return None

    def generate_keys(self) -> None:
        ((self._e, self._n), (self._d, self._n)) = generate_keys(self._p, self._q)
        ...  # return None

    def encrypt(self, data: dict) -> None:
        message: str | None = data.get("input_message", None)

        if message is None:
            return  # do nothing

        self.encrypted_message = encrypt(message, (self._e, self._n))
        ...  # return None

    def decrypt(self, data: dict) -> None:
        encrypted_message: str | None = data.get("encrypted_message", None)

        if encrypted_message is None:
            return  # do nothing

        self.decrypted_message = decrypt(encrypted_message, (self._d, self._n))
        ...  # return None
