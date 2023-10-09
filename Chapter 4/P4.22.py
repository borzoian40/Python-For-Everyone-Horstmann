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
    # derive input from the user
    numbers_input = int(input("Enter the number of rows: "))

    # determine the number of rows
    for rows in range(1, numbers_input + 1):

        # determine the number of columns for spaces
        for col in range(rows, numbers_input + 1):
            print(" ", end='')

        # print the set of stars in an ascending order from right to left
        for k in range(rows):
            print("*", end='')
        # print the set of stars in a descending order from right to left
        for l in range(1, rows):
            print("*", end='')

        print()

    for row_descending in range(2, numbers_input + 1):
        for x in range(row_descending):
            print(" ", end='')

        for y in range(row_descending, numbers_input + 1):
            print("*", end='')

        for p in range(row_descending, numbers_input):
            print("*", end='')

        print()


if __name__ == "__main__":
    main()

