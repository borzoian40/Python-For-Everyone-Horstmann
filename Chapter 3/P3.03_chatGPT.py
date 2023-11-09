
def main():
    # Read an integer from the user
    number = int(input("Enter an integer: "))

    # If the number is negative, convert it to positive
    if number < 0:
        number *= -1  # Multiply by -1 to make it positive

    # Initialize variables to count the number of digits
    count = 0
    temp = number

    # Calculate the number of digits by checking powers of 10
    while temp > 0:
        temp //= 10  # Divide by 10 to reduce the number
        count += 1  # Increment the count for each division

    # Print the number of digits in the original number
    print(f"The number has {count} digit(s).")


if __name__ == "__main__":
    main()
