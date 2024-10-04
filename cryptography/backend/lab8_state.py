import reflex as rx

from cryptography.internal.lab8 import (
    BLOCK_SIZE,
    encrypt,
    decrypt,
)


class Lab8State(rx.State):
    # / server-side values
    _block_size: int = BLOCK_SIZE

    # / client-side values
    @rx.var
    def block_size(self) -> int:
        return self._block_size

    # / slider event handlers
    def on_block_size_commit(self, block_size: list[int] | int) -> None:
        self._block_size = block_size if isinstance(block_size, int) else block_size[0]
        ...  # return None

    # / on_click event handlers
    async def encrypt(self, files: list[rx.UploadFile]):
        file = files[0]
        upload_data = await file.read()

        encrypted_data, key_data = encrypt(
            upload_data,
            block_size=self._block_size,
        )

        yield rx.download(
            data=encrypted_data,
            filename="encrypted.dat",
        )
        yield rx.download(
            data=key_data,
            filename="key.dat",
        )

    async def decrypt(self, files: list[rx.UploadFile]):
        if len(files) < 2:
            return rx.toast.error("Необходимо 2 файла! (зашифрованный текст и ключ)")

        encrypted_data = await files[0].read()
        key_data = await files[1].read()

        decrypted_data = decrypt(
            encrypted_data,
            key_data,
            block_size=self._block_size,
        )

        return rx.download(
            data=decrypted_data,
            filename="decrypted.dat",
        )
