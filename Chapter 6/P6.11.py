"""
•• P6.11 Write a function def equals(a, b) that checks whether two lists have the same elements in the same order
**NOTE: SAME ELEMENTS IN THE SAME ORDER!!
"""
def main():
    # List1
    numbers = input("Please enter values of list1:\n")
    values = numbers.split()

    list1 = []
    for digits in values:
        x = int(digits)
        list1.append(x)

    # List2
    numbers2 = input("Please enter values of list2:\n")

    values2 = numbers2.split()
    list2 = []
    for digits in values2:
        x2 = int(digits)
        list2.append(x2)

    print(equals(list1, list2))


def equals(lst1, lst2):
    length1 = len(lst1)
    length2 = len(lst2)
    
    """
    The mistake that I made at first is make a true if statement return True.
    if length1 == length2:
        for i in range(length1):
            if lst1[i] == lst2[i]:
                return True
            else:
                return False

        return True
    """
    if length1 != length2:
        return False
    for i in range(length1):
        if lst1[i] != lst2[i]:
            return False
    return True

if __name__ == "__main__":
    main()
