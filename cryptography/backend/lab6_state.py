import reflex as rx

from cryptography.internal.lab6 import (
    compress,
    decompress,
)


class Lab6State(rx.State):
    # / on_click event handlers
    async def encrypt(self, files: list[rx.UploadFile]):
        file = files[0]
        upload_data = await file.read()

        compressed_data = compress(upload_data)

        return rx.download(
            data=compressed_data,
            filename="compressed_file.haffman.lzw",
        )

    async def decrypt(self, files: list[rx.UploadFile]):
        file = files[0]
        upload_data = await file.read()

        decompressed_data = decompress(upload_data)

        return rx.download(
            data=decompressed_data,
            filename="decompressed_file.txt",
        )
