"""
•• Business P4.32 Your company has shares of stock it would like to sell when their value exceeds a 
certain target price. Write a program that reads the target price and then reads the 
current stock price until it is at least the target price. Your program should read
a sequence of floating-point values from standard input. Once the minimum is 
reached, the program should report that the stock price exceeds the target price.

"""
def main():
    # Read the target price from the user
    target_price = float(input("Enter the target price: "))

    # Loop to read and compare stock prices
    while True:
        current_price = float(input("Enter the current stock price: "))

        if current_price >= target_price:
            print("Stock price exceeds the target price.")
            break


if __name__ == "__main__":
    main()
    
