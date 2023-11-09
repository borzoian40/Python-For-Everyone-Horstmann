"""
•• P3.2 Write a program that reads a floating-point number and prints “zero” if the number 
is zero. Otherwise, print “positive” or “negative”. Add “small” if the absolute value 
of the number is less than 1, or “large” if it exceeds 1,000,000.
"""
"""
Write a program that reads an integer
and prints whether its negative, zero, or positive
"""
def main():
    while True:
        user_input = input("Press a number or 'e' to exit: ")

        if user_input.lower() == 'e':
            print("Exiting program")
            break

        num_input = float(user_input)

        if num_input < 0:
            print("Negative")
        elif num_input > 0:
            print("Positive")
        else:
            print("ZERO")

        if num_input < 1:
            print("Your number is small.")
        elif num_input > 1_000_000:
            print("Your number is too big.")


if __name__ == "__main__":
    main()
   
