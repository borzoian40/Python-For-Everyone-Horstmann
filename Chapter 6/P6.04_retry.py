"""
•• P6.4 Write list functionsthat carry out the following tasks for a list of integers. For each 
function, provide a test program.
a. Swap the first and last elements in the list.
b. Shift all elements by one to the right and move the last element into the first position. For example, 1 4 9 16 25 would be transformed into 25 1 4 9 16.
c. Replace all even elements with 0.
d. Replace each element except the first and last by the larger of its two neighbors.
e. Remove the middle element if the list length is odd, or the middle two elements 
if the length is even.
f. Move all even elements to the front, otherwise preserving the order of the 
elements.
g. Return the second-largest element in the list.
h. Return true if the list is currently sorted in increasing order.
i. Return true if the list contains two adjacent duplicate elements.
j. Return true if the list contains duplicate elements (which need not be adjacent).
"""
import random

def main():
    lists = []
    for i in range(6):
        lists.append(random.randint(1, 100))
    print(lists)
    # a)

    temp = lists[0]
    lists[0] = lists[-1]
    lists[-1] = temp
    print(lists)


if __name__ == "__main__":
    main()

