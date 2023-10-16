"""
•• P6.6 Write a function sumWithoutSmallest that computes the sum of a list of values, except 
for the smallest one, in a single loop. In the loop, update the sum and the smallest value. After the loop,
subtract the smallest value from the sum and return the difference.
"""
import random

def sumWithoutSmallest(lst):
    if len(lst) == 0:
        return 0

    total_sum = lst[0]
    smallest = lst[0]

    for num in lst[1:]:
        total_sum += num

        if num < smallest:
            smallest = num

    return total_sum - smallest


def main():
    lists = []
    for i in range(1, 10):
        lists.append(random.randint(1, 100))

    answer = sumWithoutSmallest(lists)
    print(f"The sum will be: {answer}")


if __name__ == "__main__":
    main()
