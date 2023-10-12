"""
• P5.4 Write a function
def middle(string)
that returns a string containing the middle character in string if the length of string is 
odd, or the two middle characters if the length is even. For example, middle("middle") 
returns "dd".
"""

def main():
  
    stringlength = input("Please enter your string: ")
    character = middle(stringlength)
    print(character)


def middle(string):
    if len(string) % 2 != 0:
        return string[(len(string))// 2]
    else:
        return string[len(string) // 2-1:(len(string) // 2) + 1]


if __name__ == "__main__":
    main()

