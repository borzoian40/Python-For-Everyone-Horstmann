"""
 P5.2 Write the following functions and provide a program to test them.
a. def allTheSame(x, y, z) (returning true if the arguments are all the same)
b. def allDifferent(x, y, z) (returning true if the arguments are all different)
c. def sorted(x, y, z) (returning true if the arguments are sorted, with the 
smallest one coming first)
"""
def main():
    x = int(input("Please enter your first number: "))
    y = int(input("Please enter your second number: "))
    z = int(input("Please enter your third number: "))

    #A
    same = allTheSame(x, y, z)
    #B
    different = allDifferent(x, y, z)
    #C
    sort_number = sort_numbers(x, y, z)
    print(f"Are all the numbers same?: %7s" % same)
    print("Are all the numbers different?:%5s" % different)
    print(f"Are the numbers sorted?:%7s" %sort_number)

#A
def allTheSame(x, y, z):
    if x == y and y == z:
        return True
    else:
        return False

#B
def allDifferent(x, y, z):
    if x!= y and y != z:
        return True
    else:
        return False
#C
def sort_numbers(x, y, z):
    sorted_values = sorted((x, y, z))
    return sorted_values == [x, y, z]

if __name__ == "__main__":
    main()

