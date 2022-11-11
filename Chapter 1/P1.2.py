#P1.2: Write a program that prints the sum of the first ten positive integers, 1 + 2 + … + 10.

#At first we define a function called sum.
#In the next step we assign a variable "ans" 
#We then create a for loop range from 0 up until the number given by the user, which in this case is 10.
def sum(num):
    ans = 0
    for i in range(num):
        ans += i

    return ans
 
print(sum(10))


#If we didn't have an inital input:
def main(number):
    ans = 0

    for i in range(number):
        ans += i

    print(ans)

if __name__ == "__main__":
    number = int(input())
    main(number)

