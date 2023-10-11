"""
 P5.1 Write the following functions and provide a program to test them.
a. def smallest(x, y, z) (returning the smallest of the arguments)
b. def average(x, y, z) (returning the average of the arguments)
"""
def main():
    x = int(input("Please enter your first number: "))
    y = int(input("Please enter your second number: "))
    z = int(input("Please enter your third number: "))

    min_val = smallest(x, y, z)
    avg = average(x, y, z)
    print(f"The smallest number is: {min_val}")
    print(f"The average is: {avg}")

    smallest(x, y, z)
    average(x, y, z)


def smallest(x, y, z):
    return min(x, y, z)


def average(x, y, z):
    return (x + y + z) // 3


if __name__ == "__main__":
    main()


