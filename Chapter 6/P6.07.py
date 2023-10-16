"""
• P6.7 Write a function removeMin that removes the minimum value from a list without using 
the min function or remove method.
"""
import random

def removeMin(lst):
    if len(lst) == 0:
        return

    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i

    print(f"Minimum number removed from the list: {lst[min_index]}")
    lst.pop(min_index)

    return lst


def main():
    lists = []
    for i in range(1, 10):
        lists.append(random.randint(1, 100))

    print(f"List with minimum: {lists}")
    updated_lists = removeMin(lists)
    print(f"List without minimum: {updated_lists}")


if __name__ == "__main__":
    main()

