"""
•• P2.8 Write a program that asks the user for the lengths of the sides of a rectangle. Then 
print
• The area and perimeter of the rectangle
• The length of the diagonal
"""
import math

def main():
    print("*****RECTANGLE CALCULATOR*****")
    width = float(input("Please enter your width: "))
    height = float(input("Please enter your height: "))
    area = width*height
    perimeter = 2*(width + height)

    diagonal = math.sqrt(width**2 + height**2)

    print(f"Area ={area:10.2f}")
    print(f"Perimeter ={perimeter:8.2f}")
    print()
    print(f"Length of diagonal is:{diagonal:5.2f}")


if __name__ == "__main__":
    main()

