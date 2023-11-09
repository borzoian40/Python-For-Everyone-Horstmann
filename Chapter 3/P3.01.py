"""
P3.1 Write a program that reads an integer and prints whether it is negative, zero, or 
positive.
"""
def main():

    while True:
        user_input = input("Enter an integer (or 'e' to exit): ")

        if user_input.lower() == 'e':
            print("Exiting the program.")
            break  # Exit the while loop if the user inputs 'e'

        number = int(user_input)  # Convert the user input to an integer

        # Check if the number is negative, zero, or positive
        if number < 0:
            print("The number is negative.")
        elif number == 0:
            print("The number is zero.")
        else:
            print("The number is positive.")


if __name__ == "__main__":
    main()
