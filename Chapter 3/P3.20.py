"""
•• P3.20 The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a 
given month and day.
Ifmonth is1,2, or 3,season = "Winter"
Elseifmonth is4,5,or6,season = "Spring" 
Elseifmonthis7,8,or9,season = "Summer" 
Elseifmonthis10,11,or12,season = "Fall"
Ifmonth is divisibleby 3 and day>=21 
Ifseason is"Winter",season = "Spring"
Else ifseason is"Spring",season = "Summer" 
Elseifseasonis"Summer",season = "Fall" 
Elseseason = "Winter"
Write a program that prompts the user for a month
and day and then printsthe season, as determined 
by this algorithm
"""
def main():
    while True:
        try:
            # Get month input
            while True:
                month = int(input("Please enter month (1-12): "))
                if 1 <= month <= 12:
                    break
                else:
                    print("Please enter a valid month between 1 and 12.")

            # Get day input
            while True:
                day = int(input("Please enter your day (1-31): "))
                if 1 <= day <= 31:
                    break
                else:
                    print("Please enter a valid day between 1 and 31.")

            season = ""

            if month == 1 or month == 2 or month == 3:
                season += "Winter"
            elif month == 4 or month == 5 or month == 6:
                season += "Spring"
            elif month == 7 or month == 8 or month == 9:
                season += "Summer"
            elif month == 10 or month == 11 or month == 12:
                season += "Fall"

            if month % 3 == 0 and day >= 21:
                if season == "Winter":
                    season = "Spring"
                elif season == "Spring":
                    season = "Summer"
                elif season == "Summer":
                    season = "Fall"
                else:
                    season = "Winter"

            print("Season:", season)

            # Ask the user if they want to continue
            user_input = input("Do you want to continue? (yes/no): ").lower()
            if user_input != 'yes':
                print("Goodbye...")
                break  # Exit the loop if the user does not want to continue

        except ValueError:
            print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
