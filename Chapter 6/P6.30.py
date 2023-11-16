"""
P6.30 Write a function def merge(a, b) that merges two lists, alternating elements from both 
lists. If one list is shorter than the other, then alternate as long as you can and then 
append the remaining elements from the longer list. For example, if a is
1 4 9 16
and b is
9 7 4 9 11
then merge returns a new list containing the values
1 9 4 7 9 4 16 9 11
"""
def merge(a, b):
    result = []
    min_length = min(len(a), len(b))

    for i in range(min_length):
        result.append(a[i])
        result.append(b[i])

    if len(a) > min_length:
        result.extend(a[min_length:])
    elif len(b) > min_length:
        result.extend(b[min_length:])

    return result

def main():

    list1 = input("Elements of first list:\n")
    numsplit = list1.split()

    list1_numbers = []

    for num in numsplit:
        x = int(num)
        list1_numbers.append(x)

    list2 = input("Elements of second list:\n")
    numsplit2 = list2.split()

    list2_numbers = []

    for num in numsplit2:
        x = int(num)
        list2_numbers.append(x)

    answer = merge(list1_numbers, list2_numbers)
    print(answer)


if __name__ == "__main__":
    main()


