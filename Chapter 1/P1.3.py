# P1.3 - Write a program that prints the product of the first ten positive integers, 1 × 2 × … × 10. (Use * to indicate multiplication in Python.)

#At first we define a function called Product
#And then intialize a variable called "final_ans" which is equal to 1.
#In the for loop we have to start from number 1 to number+1. The reason we start from 1 is because that in Python the index starts from 0.
#So if we start from 0 our final answer would always be zero. Hence we start from 1. 
#And the reason we end with "number + 1" in our range is that because we want the final number of our range to be included as well hence we add\
#\one to the index for it to be included as well.

#First approach
def product(number):
    final_ans = 1

    for i in range(1,number+1):
        final_ans = (final_ans * i)

    return final_ans


#number = int(input()) In case if you want to command a different number to the program.
print(product(10))

#Second approach
#By using the built-in module called factorial. 
import math

def main(number):

   return print(math.factorial(number)) 

if __name__ == "__main__":
    main(10)
