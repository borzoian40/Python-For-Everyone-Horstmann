"""
•• P6.31 Write a function def mergeSorted(a, b) that merges two sorted lists, producing a new 
sorted list. Keep an index into each list, indicating how much of it has been processed 
already. Each time, append the smallest unprocessed element from either list, then 
advance the index. For example, if a is
1 4 9 16
and b is
4 7 9 9 11
then mergeSorted returns a new list containing the values
1 4 4 7 9 9 9 11 16
"""
def mergeSorted(a, b):
    result = []
    min_length = min(len(a), len(b))

    for i in range(min_length):
        result.append(a[i])
        result.append(b[i])

    if len(a) > min_length:
        result.extend(a[min_length:])
    elif len(b) > min_length:
        result.extend(b[min_length:])

    return sorted(result)

def main():
    input_list = input("List 1:\n")
    num = input_list.split()

    list1 = []
    for x in num:
        number = int(x)
        list1.append(number)

    input_list2 = input("List 2:\n")
    num2 = input_list2.split()

    list2 = []
    for x in num2:
        number2 = int(x)
        list2.append(number2)

    answer = mergeSorted(list1, list2)
    print(answer)

if __name__ == "__main__":
    main()
