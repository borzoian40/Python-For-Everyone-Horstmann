"""
•• P5.7 Write a function
def countWords(string)
that returns a count of all words in the string string. Words are separated by spaces. 
For example, countWords("Mary had a little lamb") should return 5.
"""
def main():
    
    user_input = input("Please enter your sentence:\n")
    count = countWords(user_input)
    print(f"Total number of words: {count}")


def countWords(string):
    count = 0

    for char in string:
        if char == " ":
            count += 1

    return count + 1


if __name__ == "__main__":
    main()
