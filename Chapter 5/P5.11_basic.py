"""
•• P5.11 Enhance the intName function so that it works correctly for values < 1,000,000,000.
"""
def main():
    value = int(input("Please enter a positive integer < 10000: "))
    print(intName(value))


def intName(number):
    part = number
    name = ""

    if part >= 1000:
        name = digitName(part // 1000) + " thousand"
        part = part % 1000

    if part >= 100:
        name = name + " " + hundredsName(part)
        part = part % 100

    if part <= 100:
        name = name + " " + tensName(part)
        part = part % 10

    elif part >= 10:
        name = name + " " + teenName(part)
        part = 0

    if part > 0:
        name = name + " " + digitName(part)

    return name


def digitName(digit):
    if digit == 1: return "one"
    if digit == 2: return "two"
    if digit == 3: return "three"
    if digit == 4: return "four"
    if digit == 5: return "five"
    if digit == 6: return "six"
    if digit == 7: return "seven"
    if digit == 8: return "eight"
    if digit == 9: return "nine"

    return ""


def teenName(number):
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "fourteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"

    return ""


def tensName(number):
    if number >= 90: return "ninety"
    if number >= 80: return "eighty"
    if number >= 70: return "seventy"
    if number >= 60: return "sixty"
    if number >= 50: return "fifty"
    if number >= 40: return "forty"
    if number >= 30: return "thirty"
    if number >= 20: return "twenty"

    return ""


def hundredsName(number):
    if number >= 900: return "nine hundred"
    if number >= 800: return "eight hundred"
    if number >= 700: return "seven hundred"
    if number >= 600: return "six hundred"
    if number >= 500: return "five hundred"
    if number >= 400: return "four hundred"
    if number >= 300: return "three hundred"
    if number >= 200: return "two hundred"
    if number >= 100: return "one hundred"

    return ""


if __name__ == "__main__":
    main()
