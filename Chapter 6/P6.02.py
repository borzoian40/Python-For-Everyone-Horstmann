def main():
    numbers = []  # Initialize an empty list to store the numbers

    while len(numbers) < 10:  # Continue until the list contains ten numbers
        try:
            num = float(input("Enter a number: "))

            if num not in numbers:
                numbers.append(num)
            else:
                print("Number already in the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"List of numbers: {numbers}")


if __name__ == "__main__":
    main()
