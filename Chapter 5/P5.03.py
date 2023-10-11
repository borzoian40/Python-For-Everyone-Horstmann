"""
P5.3 Write the following functions and provide a program to test them.
a. def firstDigit(n) (returning the first digit of the argument)
b. def lastDigit(n) (returning the last digit of the argument)
c. def digits(n) (returning the number of digits in the argument)
For example, firstDigit(1729) is 1, lastDigit(1729) is 9, and digits(1729) is 4

"""
def main():
    user_num = input("Please enter your number: ")

    if user_num.isdigit():
        first = firstDigit(user_num)
        last = lastDigit(user_num)
        length = digits(user_num)

        # A
        print(f"The first digit of your number is: {first}")
        # B
        print(f"The last digit of your number is: {last}")
        # C
        print(f"The length of your number is: {length}")
    else:
        print("Invalid input. Please enter a valid number.")

# A
def firstDigit(n):
    return n[0]

# B
def lastDigit(n):
    return n[-1]

# C
def digits(n):
    return len(n)

if __name__ == "__main__":
    main()

  
