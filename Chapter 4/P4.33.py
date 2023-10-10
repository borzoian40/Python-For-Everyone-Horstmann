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

"""
def main():
    # Constants
    total_tickets = 100
    max_tickets_per_buyer = 4
    total_buyers = 0

    # Loop until all tickets are sold
    while total_tickets > 0:
        # Prompt the user for the desired number of tickets
        try:
            desired_tickets = int(input("Enter the number of tickets you want to buy (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 4.")
            continue

        if desired_tickets < 1 or desired_tickets > max_tickets_per_buyer:
            print(f"You can buy between 1 and {max_tickets_per_buyer} tickets at a time.")
        elif desired_tickets > total_tickets:
            print(f"Sorry, there are only {total_tickets} tickets remaining.")
        else:
            # Sell the tickets
            total_tickets -= desired_tickets
            total_buyers += 1
            print(f"Sold {desired_tickets} ticket(s). {total_tickets} ticket(s) remaining.")

    # All tickets have been sold
    print("All tickets have been sold.")
    print(f"Total number of buyers: {total_buyers}")

if __name__ == "__main__":
    main()
"""

