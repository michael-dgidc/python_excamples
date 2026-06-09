"""Examples of defining and using Python functions."""


def greet(name):
    return f"Hello, {name}!"


def add_numbers(a, b):
    return a + b


def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def describe_person(name, age, city="Unknown"):
    return f"{name} is {age} years old and lives in {city}."


def main():
    print(greet("Sam"))
    print("2 + 3 =", add_numbers(2, 3))
    print("Average:", calculate_average([10, 20, 30]))
    print(describe_person("Lina", 28, "London"))
    print(describe_person("Noah", 31))


if __name__ == "__main__":
    main()

