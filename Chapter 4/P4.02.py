"""
 P4.2 Write programs that read a sequence of integer inputs and print
a. The smallest and largest of the inputs.
b. The number of even and odd inputs.
c. Cumulative totals. For example, if the input is 1 7 2 9, the program should print 
1 8 10 19. 
"""
def main():
    number_str = int(input("How many numbers do you want in your list? "))
    sum = 0
    list_ofnumbers = [0] * number_str
    list_even = []
    list_odd = []
    for index in range(number_str):
        number = int(input(f"{index + 1}. Type in your number: "))
        list_ofnumbers[index] = number

    max = list_ofnumbers[0]
    min = list_ofnumbers[0]
    for index in range(number_str):
        if (list_ofnumbers[index] % 2 == 0):
            list_even.append(list_ofnumbers[index])
        else:
            list_odd.append(list_ofnumbers[index])

        sum += list_ofnumbers[index]
        if (list_ofnumbers[index] > max):
            max = list_ofnumbers[index]
        elif (list_ofnumbers[index] <= min):
            min = list_ofnumbers[index]

        print(f"The sum value is: {sum - list_ofnumbers[index]} + {list_ofnumbers[index]} = {sum}")
    print("********************")
    print(f"The maximum value is: {max}\nThe minimum value is: {min}\nThe list of even numbers are: {sorted(list_even)}"
          f"\nThe list of odd numbers are: {sorted(list_odd)}")

if __name__ == "__main__":
    main()
