"""
 P8.1 Write a new version of the program intname.py from Chapter 5 that uses a dictionary
instead of if statements.
https://github.com/borzoian40/Python-For-Everyone-Horstmann/blob/main/Chapter%205/P5.11_basic.py
"""

def main():
    value = int(input("Please enter a positive integer < 10000: "))
    print(intName(value))


def intName(number):
    part = number
    name = ""

    number_mappings = {
        0: "",
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    if part >= 1000:
        name = number_mappings[part // 1000] + " thousand"
        part %= 1000

    if part >= 100:
        name += " " + number_mappings[part // 100] + " hundred"
        part %= 100

    if part >= 20:
        name += " " + number_mappings[part // 10 * 10]
        part %= 10

    if part > 0:
        name += " " + number_mappings[part]

    return name


if __name__ == "__main__":
    main()
