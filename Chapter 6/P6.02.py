"""
• P6.2 Write a program that reads numbers and adds them to a list if they aren’t already 
contained in the list. When the list contains ten numbers, the program displays the 
contents and quits.
"""
def main():
    numbers = []  # Initialize an empty list to store the numbers
    
    while len(numbers) < 10:  # Continue until the list contains ten numbers
        try:
            num = float(input("Enter a number: "))
            
            if num not in numbers:
                numbers.append(num)
            else:
                print("Number already in the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("List of numbers:")
    for number in numbers:
        print(number)

if __name__ == "__main__":
    main()
