def telenumber(number):

    number_size = len(number)
    telephone_number = ""
    area_code = number[:3]
    exchange_code = number[3:6]
    line_number = number[6:10]

    print(f"({area_code}) {exchange_code}-{line_number}")
    # print(f"The area code is: {area_code}")
    # print(f"Exchange code is: {exchange_code}")
    # print(f"The line number is: {line_number}")


if __name__ == "__main__":
    number = input("Please enter your phone number: ")
    telenumber(number)
