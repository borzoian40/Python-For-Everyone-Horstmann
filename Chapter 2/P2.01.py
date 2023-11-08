"""
• P2.1 Write a program that displays the dimensions of a letter-size (8.5 × 11 inch) sheet of 
paper in millimeters. There are 25.4 millimeters per inch. Use constants and comments in your program.
"""
def main():
    # Constants
    INCH_TO_MM = 25.4  # 25.4 millimeters per inch
    LETTER_WIDTH_INCHES = 8.5
    LETTER_HEIGHT_INCHES = 11

    # Calculating dimensions in millimeters
    letter_width_mm = LETTER_WIDTH_INCHES * INCH_TO_MM
    letter_height_mm = LETTER_HEIGHT_INCHES * INCH_TO_MM

    # Displaying dimensions in millimeters
    print(f"Dimensions of a letter-size sheet of paper:")
    print(f"Width: {letter_width_mm:.2f} mm")
    print(f"Height: {letter_height_mm:.2f} mm")


if __name__ == "__main__":
    main()
