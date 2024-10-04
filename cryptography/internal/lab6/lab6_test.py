from cryptography.internal.lab6 import (
    compress,
    decompress,
)


def lab6_test() -> None:
    input_file = "uploaded_files/lab6_data_file.txt"
    compressed_file = "uploaded_files/compressed_lab6_data_file.haffman.lzw"
    decompressed_file = "uploaded_files/decompressed_lab6_data_file.txt"

    ...  # / Compress
    with (
        open(input_file, "rb") as i_file,
        open(compressed_file, "wb") as c_file,
    ):
        c_file.write(compress(i_file.read()))

    ...  # / Decompress
    with (
        open(compressed_file, "rb") as c_file,
        open(decompressed_file, "wb") as d_file,
    ):
        d_file.write(decompress(c_file.read()))

    ...  # / Validation
    with (
        open(input_file, "rb") as i_file,
        open(decompressed_file, "rb") as d_file,
    ):
        assert i_file.read() == d_file.read()

    ...  # return None


if __name__ == "__main__":
    lab6_test()
