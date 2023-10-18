"""
P6.9 Write a function that reversesthe sequence of elementsin a list. For example, if you 
call the function with the list
1 4 9 16 9 7 4 9 11
then the list is changed to
11 9 4 7 9 16 9 4 1
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

    reverse_function(numbers)


def reverse_function(lst):
    for x in reversed(lst):
        digits = int(x)
        print(digits, end=" ")


if __name__ == "__main__":
    main()
