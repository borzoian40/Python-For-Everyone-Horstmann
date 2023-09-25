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
    number_of_rows = int(input("Enter the number of rows: "))

    for i in range(number_of_rows):
        print("*")




if __name__ == "__main__":
    main()
