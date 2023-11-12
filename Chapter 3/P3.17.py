"""
P3.17 Write a program that reads in a string and prints whether it
• contains only letters.
• contains only uppercase letters.
• contains only lowercase letters.
• contains only digits.
• contains only letters and digits.
• starts with an uppercase letter.
• ends with a period.
"""
def main():
    while True:
        input_string = input("Enter your string or press '+' to exit: ")
        if input_string == "+":
            print("Exiting program:")
            for i in range(3, 0, -1):
                print(f"{i}")
                if i == 1:
                    print("BOOOOOOOOOOOOOOOM!!")

            break

        # A) Only Letters
        if input_string.isalpha():
            print("It contains only letters.")

        # B) Contains only uppercase letters
        elif input_string.isupper():
            print("It contains only uppercase letters.")
          
        # C) Contains only lowercase letters
        elif input_string.islower():
            print("It contains only lowercase letters.")
          
        # D) Contains only digits
        elif input_string.isdigit():
            print("It contains only digits")
          
        # E) Letters and digits
        elif input_string.isalnum():
            print("It contains both strings and digits.")

        # F) First index is uppercase
        elif input_string[0].isupper():
            print("The first index contains an uppercase letter.")
          
        # G) String ends with dot
        elif input_string.endswith('.'):
            print("It's a sentence!")
          
        else:
            print("Why dont you just take a break my friend? Do it again.")


if __name__ == "__main__":
    main()

  
