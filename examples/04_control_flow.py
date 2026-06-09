"""Examples of conditions and loops in Python."""


def main():
    temperature = 18

    if temperature >= 25:
        print("It is warm.")
    elif temperature >= 15:
        print("It is mild.")
    else:
        print("It is cold.")

    print("\nFor loop:")
    for number in range(1, 6):
        print(number)

    print("\nWhile loop:")
    countdown = 3
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Go!")

    print("\nBreak and continue:")
    for number in range(1, 8):
        if number == 3:
            continue
        if number == 6:
            break
        print(number)


if __name__ == "__main__":
    main()

