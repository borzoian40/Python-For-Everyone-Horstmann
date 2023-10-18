"""
•• P6.14 Modify the program in Worked Example 6.2 to use randomly-generated numbers 
for the die values instead of reading them from the user.
"""
def main():
    numbers = input("Please enter values of list1:\n")
    values = numbers.split()

    list1 = []
    for digits in values:
        num = int(digits)
        list1.append(num)

    numbers2 = input("Please enter values of list2:\n")
    values2 = numbers2.split()

    list2 = []
    for digits2 in values2:
        num2 = int(digits2)
        list2.append(num2)

    print(sameSet(list1, list2))


def sameSet(a, b):
    if set(a) != set(b):
        return False
    else:
        return True


if __name__ == "__main__":
    main()
