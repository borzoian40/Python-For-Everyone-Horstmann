"""
••• P6.13 Write a function def sameElements(a, b) that checks whether two lists have the same 
elements in some order, with the same multiplicities. For example,
1 4 9 16 9 7 4 9 11
and
11 1 4 9 16 9 7 4 9
would be considered identical, but
1 4 9 16 9 7 4 9 11
and
11 11 7 9 16 4 1 4 9
would not. You will probably need one or more helper functions
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
