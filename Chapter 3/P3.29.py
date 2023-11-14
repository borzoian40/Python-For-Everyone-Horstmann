"""
••• P3.29 Write a program that asks the user to enter a month (1 for January, 2 for February, 
and so on) and then printsthe number of days in the month. For February, print “28 
or 29 days”.
Enter a month: 5
30 days
Do not use a separate if/else branch for each month. Use Boolean operators.
"""
def main():
    # Get user input for the month
    month = int(input("Enter a month (1 for January, 2 for February, and so on): "))
    days_in_month = ""
    # Use Boolean operators to determine the number of days
    if 1 <= month <= 7:
        if month % 2 == 0 and month != 2:
            days_in_month = 30
        elif month % 2 == 1:

            days_in_month = 31
        else:  # Handle February separately
            days_in_month = "28 or 29"
    elif 8 <= month <= 12:
        if month % 2 == 0:
            days_in_month = 31
        else:
            days_in_month = 30

    # Print the result
    print(f"{days_in_month} days")


if __name__ == "__main__":
    main()
