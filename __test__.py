from cryptography.internal.lab1.lab1_test import lab1_test
from cryptography.internal.lab2.lab2_test import lab2_test
from cryptography.internal.lab3.lab3_test import lab3_test
from cryptography.internal.lab4.lab4_test import lab4_test


__all__ = (
    "lab1_test",
    "lab2_test",
    "lab3_test",
    "lab4_test",
)


def cyclic() -> None:
    while True:
        main()
    ...


def main() -> None:
    # lab1_test()
    # lab2_test()
    # lab3_test()
    lab4_test()
    ...


if __name__ == "__main__":
    # cyclic()
    main()
    ...
