import reflex as rx

from cryptography.internal.lab4 import (
    encrypt,
    decrypt,
)


class Lab4State(rx.State):
    # / server-side values
    _rounds: int = 4
    _block_size: int = 16
    _key_size: int = 16
    _key: str = ""

    # / client-side values
    @rx.var
    def rounds(self) -> int:
        return self._rounds

    @rx.var
    def block_size(self) -> int:
        return self._block_size

    @rx.var
    def key_size(self) -> int:
        return self._key_size

    @rx.var
    def key(self) -> str:
        return self._key

    # / slider event handlers
    def on_rounds_commit(self, rounds: list[int] | int) -> None:
        self._rounds = rounds if isinstance(rounds, int) else rounds[0]
        ...  # return None

    def on_block_size_commit(self, block_size: list[int] | int) -> None:
        self._block_size = block_size if isinstance(block_size, int) else block_size[0]
        ...  # return None

    def on_key_size_commit(self, key_size: list[int] | int) -> None:
        self._key_size = key_size if isinstance(key_size, int) else key_size[0]
        ...  # return None

    # / input event handlers
    def on_key_blur(self, key: str) -> None:
        self._key = key
        ...  # return None

    # / on_click event handlers
    async def encrypt(self, files: list[rx.UploadFile]):
        file = files[0]
        upload_data = await file.read()

        encrypted_data = encrypt(
            self._key.encode(),
            upload_data,
            rounds=self._rounds,
            block_size=self._block_size,
            key_size=self._key_size,
        )

        return rx.download(
            data=encrypted_data,
            filename="encrypted.dat",
        )

    async def decrypt(self, files: list[rx.UploadFile]):
        file = files[0]
        upload_data = await file.read()

        decrypted_data = decrypt(
            self._key.encode(),
            upload_data,
            rounds=self._rounds,
            block_size=self._block_size,
            key_size=self._key_size,
        )

        return rx.download(
            data=decrypted_data,
            filename="decrypted.dat",
        )
