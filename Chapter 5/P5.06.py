"""
P5.6 Write a function
def countVowels(string)
that returns a count of all vowels in the string. Vowels are the letters a, e, i, o, 
and u, and their uppercase variants
"""
def main():
    user_string = input("Please enter your string: ")
    vowel_count = countVowels(user_string)
    print(f"The number of vowels in the string is: {vowel_count}")

def countVowels(string):
    count = 0
    letters = ["a", "e", "i", "o", "u"]

    new_string = string.lower()
    for char in new_string:
        if char in letters:
            count += 1

    return count

if __name__ == "__main__":
    main()
