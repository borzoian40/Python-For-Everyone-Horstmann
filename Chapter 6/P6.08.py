"""
•• P6.8 Compute the alternating sum of all elements in a list. For example, if your program 
reads the input
then it computes
1 4 9 16 9 7 4 9 11
1 – 4 + 9 – 16 + 9 – 7 + 4 – 9 + 11 = –2
"""
def main():
    # Read a line of space-separated numbers
    input_line = input("Enter numbers separated by spaces:\n")

    # Split the input line into a list of number strings
    number_strings = input_line.split()

    # Initialize an empty list for the integers
    numbers = []

    # Convert the number strings to integers and add them to the 'numbers' list
    for num_str in number_strings:
        num = int(num_str)
        numbers.append(num)

    sum = 0
    # If the number is positioned in even index multiply by 1 and add to sum
    # Else, multiply by -1 and add to sum
    for i in range(1, len(numbers) + 1):
        if i % 2 == 1:
            sum = sum + numbers[i - 1] * 1
        else:
            sum = sum + numbers[i - 1] * (-1)

    print(sum)


if __name__ == "__main__":
    main()

