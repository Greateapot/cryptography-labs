from cryptography.internal.lab7 import hash


def lab7_test() -> None:
    a = "Te$Tpa$$wdL0L"
    ha = hash(a)
    print(f"a: {a};\tha: {ha}")

    b = "S0MeinVaL11Dpa$$"
    hb = hash(b)
    print(f"b: {b};\thb: {hb}")

    c = "Te$Tpa$$wdL0L"
    hc = hash(c)
    print(f"c: {c};\thc: {hc}")

    print(f"\nha == hb: {ha == hb};\nhc == hb: {hc == hb};\nha == hc: {ha == hc}")
    ...


if __name__ == "__main__":
    lab7_test()
