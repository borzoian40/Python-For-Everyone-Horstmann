"""
•• Business P4.33 Write an application to pre-sell a limited number of cinema tickets. Each buyer can 
buy as many as 4 tickets. No more than 100 tickets can be sold. Implement a program that prompts the user for the desired number of tickets and then displays the 
number of remaining tickets. Repeat until all tickets have been sold, and then display 
the total number of buyers.

"""
def main():
    total_tickets = 100
    count_buyers = 0

    while total_tickets != 0:

        buyer = int(input("How many tickets would you like to buy? (1, 2, 3 or 4)\n"))
        if buyer > 4:
            print("You can't buy more than 4 tickets. PLEASE TRY AGAIN!")
            buyer = int(input("How many tickets would you like to buy? (1, 2, 3 or 4)\n"))

        total_tickets = total_tickets - buyer
        print(f"The number of remaining tickets: {total_tickets}")
        count_buyers += 1

    print(f"Number of buyers: {count_buyers}")


if __name__ == "__main__":
    main()

