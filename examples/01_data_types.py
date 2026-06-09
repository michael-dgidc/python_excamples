"""Examples of common Python data types."""


def main():
    name = "Ada"
    age = 36
    height_m = 1.65
    is_programmer = True
    favorite_language = None

    print("String:", name)
    print("Integer:", age)
    print("Float:", height_m)
    print("Boolean:", is_programmer)
    print("None:", favorite_language)

    print("\nType checks:")
    print(type(name))
    print(type(age))
    print(type(height_m))
    print(type(is_programmer))
    print(type(favorite_language))

    print("\nSimple operations:")
    print("Greeting:", "Hello, " + name)
    print("Age next year:", age + 1)
    print("Height in cm:", height_m * 100)
    print("Programmer answer:", not is_programmer)


if __name__ == "__main__":
    main()

