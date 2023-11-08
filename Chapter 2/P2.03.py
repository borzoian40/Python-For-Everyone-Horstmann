"""
• P2.3 Write a program that reads a number and displays the square, cube, and fourth 
power. Use the ** operator only for the fourth power.
"""
import math
def main():
    # Read a number from the user
    number = float(input("Enter a number: "))

    # Calculate square and cube
    square = number * number
    cube = number * number * number
    fourth_power = number ** 4  # Using ** operator for the fourth power

    # Display the results with aligned output using format specifiers
    print(f"Square of {number} is:      {square:11.2f}")
    print(f"Cube of {number} is:        {cube:11.2f}")
    print(f"Fourth power of {number} is: {fourth_power:10.2f}")


if __name__ == "__main__":
    main()
