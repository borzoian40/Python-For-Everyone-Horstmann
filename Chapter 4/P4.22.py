"""
•• P4.22 Write a program that reads an integer and displays, using asterisks, a filled diamond
of the given side length. For example, if the side length is 4, the program should display
    *
   ***
  *****
 *******
  *****
   ***
    *
"""

def main():
    numbers_input = int(input("Enter the number of rows: "))

    for i in range(1, numbers_input + 1):
        for j in range(i, numbers_input + 1):
            print(" ", end='')

        for k in range(1, i):
            print("*", end='')

        for j in range(i):
            print("*", end='')

        print()

    for z in range(2, numbers_input + 1):
        for t in range(z):
            print(" ", end='')

        for k in range(z, numbers_input + 1):
            print("*", end='')

        for h in range(z, numbers_input):
            print("*", end='')

        print()


if __name__ == "__main__":
    main()
