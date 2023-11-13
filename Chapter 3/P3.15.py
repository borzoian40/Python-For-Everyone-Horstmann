"""
•• P3.15 Write a program that reads in three floating-point numbers and prints the largest of 
the three inputs without using the max function. For example:
Enter a number: 4 
Enter a number: 9 
Enter a number: 2.5
The largest number is 9.0
"""
def main():
    num = int(input("How many numbers would you like: "))
    num_list = []

    for i in range(num):
        while True:
            try:
                number = int(input(f"{i+1}. Enter a number: "))
                num_list.append(number)
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    max = num_list[0]
    for i in range(num):
        if max <= num_list[i]:
            max = num_list[i]

    print(num_list)
    print(f"The largest number is: {max}")

if __name__ == "__main__":
    main()
