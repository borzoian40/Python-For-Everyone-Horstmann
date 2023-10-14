"""
•• P5.16 Write a recursive function
def isPalindrome(string)
that returns True if string is a palindrome, that is, a word that is the same when 
reversed. Examples of palindromes are “deed”, “rotor”, or “aibohphobia”. Hint: A 
word is a palindrome if the first and last letters match and the remainder is also a 
palindrome
"""
def isPalindrome(string):
    # Base case: If the string is empty or has only one character, it's a palindrome.
    if len(string) <= 1:
        return True
    else:
        # Check if the first and last characters are the same.
        if string[0] == string[-1]:
            # Recursively check the remainder of the string.
            return isPalindrome(string[1:-1])
        else:
            return False

# Example usage:
def main():
    input_string = input("Please enter your string:\n")
    result = isPalindrome(input_string)
    print(f"'{input_string}' is a palindrome: {result}")

if __name__ == "__main__":
    main()

