"""
••• Business P4.35 Credit Card Number Check. The last digit of a credit card number isthe check 
digit, which protects against transcription errors such as an error in a single digit or 
switching two digits. The following method is used to verify actual credit card numbers but, for simplicity, we will describe it for numbers with 8 digits instead of 16:
• Starting from the rightmost digit, form the sum of every other digit. For 
example, if the credit card number is 4358 9795, then you form the sum 5 + 7 + 
8 + 3 = 23.
• Double each of the digits that were not included in the preceding step. Add all 
digits of the resulting numbers. For example, with the number given above, 
doubling the digits, starting with the next-to-last one, yields 18 18 10 8. Adding 
all digitsin these values yields 1 + 8 + 1 + 8 + 1 + 0 + 8 = 27.
• Add the sums of the two preceding steps. If the last digit of the result is 0, the 
number is valid. In our case, 23 + 27 = 50, so the number is valid.
Write a program that implements this algorithm. The user should supply an 8-digit 
number, and you should print out whether the number is valid or not. If it is not 
valid, you should print the value of the check digit that would make it valid.
"""
#Raw file for P4.35. After spending almost 3 hours!!! 
def main():
    count = 0
    while count <= 3:
        sum1 = 0
        value_input = input("Please enter your 8 digit credit card number: ")
        value_input = value_input.replace(" ", "")
        # Convert the input to a string
        conversion = str(value_input)
        # Use slicing to get every other digit starting from the first digit (index 0)
        array_conversion1 = conversion[1::2]
        array_conversion2 = conversion[::2]
        list = []
        for i in range(len(array_conversion1)):
            # Convert each character back to an integer before adding to sum
            sum1 += int(array_conversion1[i])

        for j in range(len(array_conversion2)):
            list.append(int(array_conversion2[j]) * 2)

        string_conversion = " "

        liststr = string_conversion.join([str(element) for element in list])
        liststr = liststr.replace(" ", "")

        sum2 = 0
        addition_liststr = liststr[::]
        for i in range(len(addition_liststr)):
            sum2 += int(addition_liststr[i])

        final_sum = sum1 + sum2

        if final_sum % 10 == 0:
            print("Your card is valid!")
            break
        else:
            count += 1
            if count == 3:
                print("Your card is blocked!")
                break

            print("Your CARD IS NOT VALID! PLEASE TRY AGAIN!")


if __name__ == "__main__":
    main()

