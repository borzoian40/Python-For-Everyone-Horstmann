"""
 P2.2 Write a program that computes and displays the perimeter of a letter-size (8.5 × 11 
inch) sheet of paper and the length of its diagonal.
"""
import math

def main():
    # Constants
    INCH_TO_MM = 25.4  # 25.4 millimeters per inch
    LETTER_WIDTH_INCHES = 8.5
    LETTER_HEIGHT_INCHES = 11

    # Calculating dimensions in millimeters
    letter_width_mm = LETTER_WIDTH_INCHES * INCH_TO_MM
    letter_height_mm = LETTER_HEIGHT_INCHES * INCH_TO_MM
    perimeter = 2 * (letter_height_mm + letter_width_mm)
    diagonal = math.sqrt(letter_height_mm ** 2 + letter_width_mm ** 2)

    # Displaying dimensions in millimeters
    print(f"Dimensions of a letter-size sheet of paper:")
    print(f"Width: {letter_width_mm:.2f} mm")
    print(f"Height: {letter_height_mm:.2f} mm")
    print(f"Perimeter: {perimeter: .2f} mm")
    print(f"Diagonal: {diagonal: .2f} mm")


if __name__ == "__main__":
    main()
