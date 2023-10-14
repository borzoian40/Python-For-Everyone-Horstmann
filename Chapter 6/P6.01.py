"""
•• P6.1 Write a program that initializes a list with ten random integers and then prints four
lines of output, containing:
• Every element at an even index.
• Every even element.
• All elements in reverse order.
• Only the first and last element
"""
import random

def main():
    # Define a primary list
    primary_list = [0] * 10
    # Define an even list
    even_list = []

    # Create a random list with 10 random integers.
    # A)
    for i in range(10):
        primary_list[i] = random.randint(1, 10)
    print(f"a. {primary_list}")

    # B) Even indices
    print(f"b. {primary_list[1::2]}")

    # C) Every even element
    for j in range(10):
        if primary_list[j] % 2 == 0:
            even_list.append(primary_list[j])
    print(f"c. {even_list}")

    # D) Reverse order
    print(f"d. {primary_list[::-1]}")
    # E) Only the first element and the last element
    print(f"e. {primary_list[0], primary_list[-1]}")


if __name__ == "__main__":
    main()
