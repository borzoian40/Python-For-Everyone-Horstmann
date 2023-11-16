"""
P6.29 Write a function def appendList(a, b) that appends one list 
after another. For example, if a is
1 4 9 16
and b is
9 7 4 9 11
then appendList returns a new list containing the values
1 4 9 16 9 7 4 9 11
"""
def appendList(a, b):
    final_list = a + b
    return final_list

def main():
    # input the numbers with spaces included
    input_str = input("Please enter your numbers:\n")
    numbers = input_str.split()  # add them to a list
    # introduce an empty list
    list_numbers = []
    # now add those numbers as int to "list_numbers"
    for num in numbers:
        x = int(num)
        list_numbers.append(x)

    # Do the same process for the second list
    input_str2 = input("Please enter your numbers:\n")
    numbers2 = input_str2.split()

    list_numbers2 = []

    for num in numbers2:
        x2 = int(num)
        list_numbers2.append(x2)

    # Call out the bloody function
    answer = appendList(list_numbers, list_numbers2)
    print(answer)

if __name__ == "__main__":
    main()
