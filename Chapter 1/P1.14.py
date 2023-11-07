"""
Write a program that prints a two-column list of your friends’ birthdays. In the 
first column, print the names of your best friends; in the second column, print their 
birthdays.
"""
def print_birthdays(friends):
    print("Friends' Birthdays:")
    print("{:<20} {:<15}".format("Name", "Birthday"))
    for friend, birthday in friends.items():
        print("{:<20} {:<15}".format(friend, birthday))

# Dictionary with friends' names as keys and their birthdays as values
friends_birthdays = {
    "Lisa": "Feb 28, 1993",
    "Brz": "December 14, 1991",
    "Charlie": "November 20, 1995",
    "David": "March 10, 1992"
    # Add more friends and their birthdays as needed
}

print_birthdays(friends_birthdays)
