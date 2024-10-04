from cryptography.internal.lab6 import (
    compress,
    decompress,
)


def lab6_test() -> None:
    input_file = "uploaded_files/large.txt"
    encoded_file = "uploaded_files/compressed_large.haffman.lzw"
    decoded_file = "uploaded_files/decompressed_large.txt"

    with open(input_file, "rb") as fileA:
        with open(encoded_file, "wb") as fileB:
            fileB.write(compress(fileA.read()))

    with open(encoded_file, "rb") as fileA:
        with open(decoded_file, "wb") as fileB:
            fileB.write(decompress(fileA.read()))

    with open(input_file, "rb") as fileA:
        with open(decoded_file, "rb") as fileB:
            assert fileA.read() == fileB.read()

    ...  # return None


if __name__ == "__main__":
    lab6_test()
