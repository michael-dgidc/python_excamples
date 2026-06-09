"""Examples of Python data structures."""


def main():
    fruits = ["apple", "banana", "cherry"]
    coordinates = (10, 20)
    student = {"name": "Maya", "score": 92}
    unique_numbers = {1, 2, 2, 3, 3, 3}

    print("List:", fruits)
    print("First fruit:", fruits[0])
    fruits.append("orange")
    print("After append:", fruits)

    print("\nTuple:", coordinates)
    print("X coordinate:", coordinates[0])

    print("\nDictionary:", student)
    print("Student name:", student["name"])
    student["passed"] = True
    print("After adding passed:", student)

    print("\nSet:", unique_numbers)
    unique_numbers.add(4)
    print("After add:", unique_numbers)

    print("\nLooping through a list:")
    for fruit in fruits:
        print("-", fruit)

    print("\nLooping through a dictionary:")
    for key, value in student.items():
        print(key, "=", value)


if __name__ == "__main__":
    main()

