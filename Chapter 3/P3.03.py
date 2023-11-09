"""
•• P3.3 Write a program that reads an integer and prints how many digits the number has, by 
checking whether the number is � 10, � 100, and so on. (Assume that all integers are
less than ten billion.) If the number is negative, first multiply it by –1.
"""
#My approach
def main():
    user_input = input("Please enter your number: ")
    length = len(user_input)
    if user_input[0] == '-':
        length = len(user_input) - 1
    print(f"{length}")


if __name__ == "__main__":
    main()
