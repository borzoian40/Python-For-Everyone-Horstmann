"""
•• Business P4.34 You need to control the number of people who can be in an oyster bar at the same
time. Groups of people can always leave the bar, but a group cannot enter the bar 
if they would make the number of people in the bar exceed the maximum of 100 
occupants. Write a program that reads the sizes of the groups that arrive or depart.
Use negative numbers for departures. After each input, display the current number 
of occupants. As soon as the bar holds the maximum number of people, report that 
the bar is full and exit the program
"""
def main():
    # Constants
    max_occupants = 100
    current_occupants = 0

    # Loop to manage the oyster bar
    while current_occupants <= max_occupants:
        try:
            change = int(
                input("Enter the size of the group (positive for arrivals, negative for departures, 0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Check if the user wants to exit
        if change == 0:
            break

        # Update the current number of occupants
        current_occupants += change

        # Ensure the number of occupants doesn't exceed the maximum
        if current_occupants > max_occupants:
            print("The oyster bar is full!")
            print(f"Number of extra people are: {current_occupants - max_occupants}")
            break

        # Display the current number of occupants
        print(f"Current number of occupants: {current_occupants}")

    print("Exiting the program.")


if __name__ == "__main__":
    main()
   
